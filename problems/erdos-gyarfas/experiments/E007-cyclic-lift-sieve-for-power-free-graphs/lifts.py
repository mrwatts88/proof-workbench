"""E007 — cyclic-lift sieve for power-free graphs.

Implements the machinery of attempt A008:

- base multigraphs (loops and parallel edges allowed) with spanning-tree
  gauge fixing (Lemma L020);
- exact dynamic programming for the walk-class sets V_L(B): cycle-space
  vectors of all tailless non-backtracking closed walks of length exactly
  L (the hyperplane data licensed by Lemma L019);
- the hyperplane sieve over voltage assignments x in (Z_m)^mu: an
  assignment is *certified* free of L-cycles when no vector in V_L(B) is
  orthogonal to x mod m; lengths {1,2} encode simplicity of the lift;
- explicit lift construction and ground-truth verification with the
  validated E004 detectors (the L019 direction "sieve-clean implies
  detector-clean" is asserted, never assumed silently);
- calibration counts for the four verified order-24 extremal graphs
  (exact number of 16-cycles and their edge/vertex coverage).

Exact integer arithmetic throughout; no floating point, no randomness.
Run `python3 lifts.py anchors` first; every substantive mode re-runs its
own preconditions cheaply.
"""

from __future__ import annotations

import argparse
import importlib.util
import pathlib
import sys
from itertools import product

HERE = pathlib.Path(__file__).resolve().parent
E004_DIR = HERE.parent / "E004-order-11-saturated-search"
E005_DIR = HERE.parent / "E005-markstrom-24-vertex-graphs-verification-and-reproduction"


def _load(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SAT = _load("e004_saturated", E004_DIR / "saturated.py")
E005LIB = _load("e005lib", E005_DIR / "e005lib.py")


# ------------------------------------------------------------------- bases

class Base:
    """Finite connected multigraph with arcs, reversal, and tree gauge.

    Edges are (u, v) pairs; u == v is a loop; repeats are parallel edges.
    Edge e yields arcs 2e (u->v) and 2e+1 (v->u); rev(a) = a ^ 1. A BFS
    spanning tree (loops never in the tree) gets voltage 0 by L020; each
    non-tree edge e gets a coordinate index; arc 2e contributes +1 to that
    coordinate, arc 2e+1 contributes -1.
    """

    def __init__(self, name: str, n: int, edges: list[tuple[int, int]]):
        self.name = name
        self.n = n
        self.edges = list(edges)
        self.arc_tail = []
        self.arc_head = []
        for (u, v) in self.edges:
            self.arc_tail += [u, v]
            self.arc_head += [v, u]
        self.narcs = 2 * len(self.edges)
        # BFS spanning tree over non-loop edges.
        tree = set()
        seen = {0}
        frontier = [0]
        while frontier:
            new_frontier = []
            for u in frontier:
                for e, (a, b) in enumerate(self.edges):
                    if a == b or e in tree:
                        continue
                    other = None
                    if a == u and b not in seen:
                        other = b
                    elif b == u and a not in seen:
                        other = a
                    if other is not None:
                        tree.add(e)
                        seen.add(other)
                        new_frontier.append(other)
            frontier = new_frontier
        if len(seen) != n:
            raise ValueError(f"base {name} is not connected")
        self.tree = tree
        self.free_edges = [e for e in range(len(self.edges)) if e not in tree]
        self.mu = len(self.free_edges)
        coord_of_edge = {e: i for i, e in enumerate(self.free_edges)}
        # arc -> (coordinate index, sign) or None for tree arcs
        self.arc_coord = []
        for a in range(self.narcs):
            e = a // 2
            if e in tree:
                self.arc_coord.append(None)
            else:
                self.arc_coord.append((coord_of_edge[e], 1 if a % 2 == 0 else -1))
        # out-arcs per vertex
        self.out_arcs = [[] for _ in range(n)]
        for a in range(self.narcs):
            self.out_arcs[self.arc_tail[a]].append(a)
        self.degree = [len(self.out_arcs[v]) for v in range(n)]

    def describe(self) -> str:
        return (
            f"{self.name}: n={self.n} edges={self.edges} mu={self.mu} "
            f"tree={sorted(self.tree)} degrees={self.degree}"
        )


def base_theta3() -> Base:
    return Base("theta3", 2, [(0, 1), (0, 1), (0, 1)])


def base_dumbbell() -> Base:
    # bridge, loop at 0, loop at 1 -> lifts are the I-graphs I(m, a, b)
    return Base("dumbbell", 2, [(0, 1), (0, 0), (1, 1)])


def base_bouquet2() -> Base:
    return Base("bouquet2", 1, [(0, 0), (0, 0)])


def base_k4() -> Base:
    return Base("k4", 4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])


def base_k33() -> Base:
    return Base(
        "k33", 6,
        [(u, v) for u in (0, 1, 2) for v in (3, 4, 5)],
    )


def base_prism() -> Base:
    return Base(
        "prism", 6,
        [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (0, 3), (1, 4), (2, 5)],
    )


BASES = {
    b().name: b
    for b in (base_theta3, base_dumbbell, base_bouquet2, base_k4, base_k33, base_prism)
}


# ------------------------------------------------- walk-class enumeration

def walk_vectors(base: Base, targets: list[int]) -> dict[int, set[tuple[int, ...]]]:
    """V_L(B) for each L in targets: cycle-space vectors of all tailless
    non-backtracking closed walks of length exactly L.

    DP over states (current arc, accumulated vector). Start arcs range
    over the arcs of non-tree edges only: a tailless nb closed walk cannot
    stay inside the spanning tree (a forest supports no such walk), the
    tailless condition is cyclic, and rotations preserve the vector, so
    every walk has a rotation starting with a non-tree arc in its original
    direction.
    """
    lmax = max(targets)
    want = set(targets)
    out: dict[int, set[tuple[int, ...]]] = {t: set() for t in targets}
    zero = (0,) * base.mu

    def delta(arc: int) -> tuple[int, ...]:
        c = base.arc_coord[arc]
        if c is None:
            return zero
        idx, sign = c
        return tuple(sign if i == idx else 0 for i in range(base.mu))

    def add(vec: tuple[int, ...], arc: int) -> tuple[int, ...]:
        c = base.arc_coord[arc]
        if c is None:
            return vec
        idx, sign = c
        return vec[:idx] + (vec[idx] + sign,) + vec[idx + 1:]

    start_arcs = [a for a in range(base.narcs) if base.arc_coord[a] is not None]
    for s in start_arcs:
        s_tail = base.arc_tail[s]
        s_rev = s ^ 1
        states: set[tuple[int, tuple[int, ...]]] = {(s, delta(s))}
        length = 1
        if length in want:
            for arc, vec in states:
                if base.arc_head[arc] == s_tail and arc != s_rev:
                    out[length].add(vec)
        while length < lmax:
            nxt: set[tuple[int, tuple[int, ...]]] = set()
            for arc, vec in states:
                head = base.arc_head[arc]
                banned = arc ^ 1
                for a2 in base.out_arcs[head]:
                    if a2 == banned:
                        continue
                    nxt.add((a2, add(vec, a2)))
            states = nxt
            length += 1
            if length in want:
                bucket = out[length]
                for arc, vec in states:
                    if base.arc_head[arc] == s_tail and arc != s_rev:
                        bucket.add(vec)
    return out


def walk_vectors_bruteforce(base: Base, length: int) -> set[tuple[int, ...]]:
    """Independent naive enumeration of the same sets, for anchoring."""
    results: set[tuple[int, ...]] = set()
    zero = (0,) * base.mu

    def vec_add(vec, arc):
        c = base.arc_coord[arc]
        if c is None:
            return vec
        idx, sign = c
        return vec[:idx] + (vec[idx] + sign,) + vec[idx + 1:]

    def extend(first: int, arc: int, vec, steps: int) -> None:
        if steps == length:
            if base.arc_head[arc] == base.arc_tail[first] and arc != (first ^ 1):
                results.add(vec)
            return
        for a2 in base.out_arcs[base.arc_head[arc]]:
            if a2 == (arc ^ 1):
                continue
            extend(first, a2, vec_add(vec, a2), steps + 1)

    for first in range(base.narcs):
        extend(first, first, vec_add(zero, first), 1)
    return results


def find_walk(base: Base, length: int, target: tuple[int, ...]):
    """Reconstruct one tailless nb closed walk of the given length and
    vector, or None. Audit helper for surprising vectors (e.g. zero)."""

    def vec_add(vec, arc):
        c = base.arc_coord[arc]
        if c is None:
            return vec
        idx, sign = c
        return vec[:idx] + (vec[idx] + sign,) + vec[idx + 1:]

    def l1(vec):
        return sum(abs(c) for c in vec)

    def extend(first, walk, vec, steps):
        if steps == length:
            if (
                base.arc_head[walk[-1]] == base.arc_tail[first]
                and walk[-1] != (first ^ 1)
                and vec == target
            ):
                return list(walk)
            return None
        gap = tuple(t - v for t, v in zip(target, vec))
        if l1(gap) > length - steps:
            return None
        for a2 in base.out_arcs[base.arc_head[walk[-1]]]:
            if a2 == (walk[-1] ^ 1):
                continue
            got = extend(first, walk + [a2], vec_add(vec, a2), steps + 1)
            if got is not None:
                return got
        return None

    zero = (0,) * base.mu
    for first in range(base.narcs):
        got = extend(first, [first], vec_add(zero, first), 1)
        if got is not None:
            return got
    return None


# ---------------------------------------------------------------- sieve

def power_targets(limit: int) -> list[int]:
    """Cycle lengths to exclude: powers of two >= 4 up to limit."""
    out = []
    p = 4
    while p <= limit:
        out.append(p)
        p *= 2
    return out


def sieve(base: Base, m: int, vectors: dict[int, set[tuple[int, ...]]],
          lengths: list[int]):
    """Mark every x in (Z_m)^mu hit by some vector of the given lengths.

    Returns (survivors, all_dead_reason). A vector that is zero mod m
    kills every assignment outright.
    """
    mu = base.mu
    mods: set[tuple[int, ...]] = set()
    for L in lengths:
        for vec in vectors[L]:
            mods.add(tuple(c % m for c in vec))
    if tuple([0] * mu) in mods:
        return [], "zero vector mod m at one of the sieved lengths"
    size = m ** mu
    bad = bytearray(size)
    weights = [m ** i for i in range(mu)]

    for vec in mods:
        # last coordinate with a unit-solvable structure: pick any index j
        # with vec[j] != 0 mod m; iterate the others, solve coordinate j.
        j = next(i for i in range(mu) if vec[i] % m)
        vj = vec[j] % m
        g = gcd(vj, m)
        step = m // g
        vj_red = (vj // g) % step
        inv = pow(vj_red, -1, step) if step > 1 else 0
        others = [i for i in range(mu) if i != j]
        for combo in product(range(m), repeat=mu - 1):
            rhs = 0
            idx_partial = 0
            for pos, val in zip(others, combo):
                rhs += vec[pos] * val
                idx_partial += weights[pos] * val
            rhs = (-rhs) % m
            if rhs % g:
                continue
            x0 = ((rhs // g) * inv) % step if step > 1 else 0
            for k in range(g):
                xj = x0 + k * step
                bad[idx_partial + weights[j] * xj] = 1

    survivors = []
    for idx in range(size):
        if not bad[idx]:
            x = []
            r = idx
            for _ in range(mu):
                x.append(r % m)
                r //= m
            survivors.append(tuple(x))
    return survivors, None


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def gcd_many(values, m: int) -> int:
    g = m
    for v in values:
        g = gcd(g, v)
    return g


def canonical_up_to_units(x: tuple[int, ...], m: int) -> tuple[int, ...]:
    best = None
    for c in range(1, m):
        if gcd(c, m) != 1:
            continue
        y = tuple((c * v) % m for v in x)
        if best is None or y < best:
            best = y
    return best if best is not None else x


# ------------------------------------------------------------ lift builder

def build_lift(base: Base, m: int, x: tuple[int, ...]) -> list[int]:
    """Adjacency bitmasks of the derived graph; raises on non-simplicity."""
    n = base.n * m
    adjacency = [0] * n

    def vid(u: int, g: int) -> int:
        return u * m + (g % m)

    def connect(p: int, q: int) -> None:
        if p == q:
            raise ValueError("lift has a loop; assignment not admissible")
        if adjacency[p] & (1 << q):
            raise ValueError("lift has a parallel edge; assignment not admissible")
        adjacency[p] |= 1 << q
        adjacency[q] |= 1 << p

    for e, (u, v) in enumerate(base.edges):
        arc = 2 * e
        c = base.arc_coord[arc]
        volt = 0 if c is None else (c[1] * x[c[0]]) % m
        for g in range(m):
            connect(vid(u, g), vid(v, g + volt))
    return adjacency


def is_two_connected(adjacency: list[int]) -> bool:
    n = len(adjacency)
    if n < 3 or not SAT.is_connected(adjacency):
        return False
    for v in range(n):
        # delete v, test connectivity of the rest
        mask_v = ~(1 << v)
        sub = [adjacency[u] & mask_v if u != v else 0 for u in range(n)]
        start = next(u for u in range(n) if u != v)
        seen = 1 << start
        frontier = [start]
        while frontier:
            u = frontier.pop()
            avail = sub[u] & ~seen
            while avail:
                bit = avail & -avail
                avail ^= bit
                seen |= bit
                frontier.append(bit.bit_length() - 1)
        expect = ((1 << n) - 1) & mask_v
        if seen != expect:
            return False
    return True


def girth_upto(adjacency: list[int], cap: int) -> int | None:
    """Exact girth if <= cap, else None. BFS from every vertex."""
    n = len(adjacency)
    best = None
    for s in range(n):
        dist = {s: 0}
        parent = {s: -1}
        frontier = [s]
        while frontier:
            nxt = []
            for u in frontier:
                avail = adjacency[u]
                while avail:
                    bit = avail & -avail
                    avail ^= bit
                    w = bit.bit_length() - 1
                    if w not in dist:
                        dist[w] = dist[u] + 1
                        parent[w] = u
                        nxt.append(w)
                    elif w != parent[u]:
                        cyc = dist[u] + dist[w] + 1
                        if best is None or cyc < best:
                            best = cyc
            if best is not None and dist[frontier[0]] * 2 + 1 > best:
                break
            frontier = nxt
    if best is not None and best <= cap:
        return best
    return None


def verify_lift(base: Base, m: int, x: tuple[int, ...],
                power_checks: list[int]) -> dict:
    adjacency = build_lift(base, m, x)
    n = len(adjacency)
    report = {
        "order": n,
        "degrees_min": min(SAT_degrees(adjacency)),
        "degrees_max": max(SAT_degrees(adjacency)),
        "connected": SAT.is_connected(adjacency),
        "two_connected": is_two_connected(adjacency),
        "bipartite": SAT.is_bipartite(adjacency),
        "girth<=12": girth_upto(adjacency, 12),
        "c4_free_codegree": SAT.codegree_c4_free(adjacency),
    }
    for L in power_checks:
        if L <= n:
            report[f"has_C{L}"] = SAT.has_cycle_of_length(adjacency, L)
    return report


def SAT_degrees(adjacency: list[int]) -> list[int]:
    return [row.bit_count() for row in adjacency]


# ------------------------------------------------------------- calibration

def count_cycles_of_length(adjacency: list[int], length: int):
    """Exact count of simple cycles of the given length, plus per-edge and
    per-vertex coverage. Each undirected cycle is enumerated once per
    direction from its minimum vertex; totals are halved."""
    n = len(adjacency)
    total2 = 0
    edge_count2: dict[tuple[int, int], int] = {}
    vertex_count2 = [0] * n

    def record(path: list[int]) -> None:
        nonlocal total2
        total2 += 1
        for i, u in enumerate(path):
            v = path[(i + 1) % len(path)]
            key = (u, v) if u < v else (v, u)
            edge_count2[key] = edge_count2.get(key, 0) + 1
            vertex_count2[u] += 1

    def extend(s: int, cur: int, used: int, path: list[int]) -> None:
        if len(path) == length:
            if adjacency[cur] & (1 << s):
                record(path)
            return
        avail = adjacency[cur] & ~used
        while avail:
            bit = avail & -avail
            avail ^= bit
            w = bit.bit_length() - 1
            if w <= s:
                continue
            path.append(w)
            extend(s, w, used | bit, path)
            path.pop()

    for s in range(n):
        avail = adjacency[s]
        while avail:
            bit = avail & -avail
            avail ^= bit
            w = bit.bit_length() - 1
            if w <= s:
                continue
            extend(s, w, (1 << s) | bit, [s, w])

    assert total2 % 2 == 0
    edge_counts = {k: v // 2 for k, v in edge_count2.items()}
    vertex_counts = [c // 2 for c in vertex_count2]
    return total2 // 2, edge_counts, vertex_counts


def calibrate() -> None:
    path = E005_DIR / "data" / "survivors_n24.g6"
    lines = [ln.strip() for ln in path.read_text().splitlines() if ln.strip()]
    print(f"calibration: {len(lines)} order-24 extremal graphs from E005")
    for i, line in enumerate(lines):
        adjacency = E005LIB.g6_decode(line)
        assert len(adjacency) == 24
        assert all(d == 3 for d in SAT_degrees(adjacency))
        assert SAT.codegree_c4_free(adjacency)
        assert not SAT.has_cycle_of_length(adjacency, 8)
        assert SAT.has_cycle_of_length(adjacency, 16)
        count16, edge_counts, vertex_counts = count_cycles_of_length(adjacency, 16)
        edges_all = [e for e, c in edge_counts.items() if c == count16]
        emin = min(edge_counts.get((u, v) if u < v else (v, u), 0)
                   for u in range(24) for v in range(24)
                   if u < v and adjacency[u] & (1 << v))
        emax = max(edge_counts.values()) if edge_counts else 0
        vmin, vmax = min(vertex_counts), max(vertex_counts)
        print(
            f"survivor[{i}] C16_count={count16} "
            f"edge_coverage=[{emin},{emax}] vertex_coverage=[{vmin},{vmax}] "
            f"edges_on_all_C16={len(edges_all)}"
        )


# ----------------------------------------------------------------- anchors

def anchors() -> None:
    # A1: theta3 length-2 classes are exactly the parallel-edge patterns.
    theta = base_theta3()
    v = walk_vectors(theta, [2])
    expect = {(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)}
    assert v[2] == expect, v[2]

    # A2: DP agrees with independent brute force on small lengths.
    for maker in (base_theta3, base_dumbbell, base_bouquet2, base_k4):
        b = maker()
        targets = [1, 2, 3, 4, 5, 6, 7, 8]
        dp = walk_vectors(b, targets)
        for L in targets:
            brute = walk_vectors_bruteforce(b, L)
            assert dp[L] == brute, (b.name, L, dp[L] ^ brute)

    # A3: K4 triangle and quadrilateral classes exclude the zero vector.
    k4 = base_k4()
    v34 = walk_vectors(k4, [3, 4])
    assert (0, 0, 0) not in v34[3] and (0, 0, 0) not in v34[4]
    assert v34[3] == {tuple(-c for c in t) for t in v34[3]}

    # A4: bouquet2 carries the abelian commutator at length 4.
    bouquet = base_bouquet2()
    vb = walk_vectors(bouquet, [4])
    assert (0, 0) in vb[4]
    witness = find_walk(bouquet, 4, (0, 0))
    assert witness is not None and len(witness) == 4

    # A5: dumbbell lift (m=5, x=(1,2)) is the Petersen graph.
    dumbbell = base_dumbbell()
    petersen = build_lift(dumbbell, 5, (1, 2))
    assert len(petersen) == 10
    assert SAT_degrees(petersen) == [3] * 10
    assert SAT.is_connected(petersen) and is_two_connected(petersen)
    assert girth_upto(petersen, 12) == 5
    assert SAT.codegree_c4_free(petersen)
    assert not SAT.has_cycle_of_length(petersen, 4)
    assert SAT.has_cycle_of_length(petersen, 8)
    # L019 contrapositive: the C8 upstairs must show as a hyperplane hit.
    vd = walk_vectors(dumbbell, [8])
    assert any((n1 * 1 + n2 * 2) % 5 == 0 for (n1, n2) in vd[8])

    # A6: theta3 lift (m=3, x=(1,2)) is K33: C4 present, hit at length 4.
    k33lift = build_lift(theta, 3, (1, 2))
    assert len(k33lift) == 6
    assert SAT_degrees(k33lift) == [3] * 6
    assert SAT.is_bipartite(k33lift)
    assert SAT.has_cycle_of_length(k33lift, 4)
    vt = walk_vectors(theta, [4])
    assert any((n1 * 1 + n2 * 2) % 3 == 0 for (n1, n2) in vt[4])

    # A7: zero assignment on K4 over Z_3: disjoint K4s; sieve must kill.
    k4lift = build_lift(k4, 3, (0, 0, 0))
    assert SAT.has_cycle_of_length(k4lift, 4)
    surv, reason = sieve(k4, 3, walk_vectors(k4, [1, 2, 4]), [4])
    assert (0, 0, 0) not in surv

    # A8: sieve marking agrees with a naive quadratic check, at a prime
    # modulus and at composite moduli (exercising the gcd>1 solution
    # enumeration paths).
    b = base_theta3()
    vecs = walk_vectors(b, [1, 2, 4, 8])
    for m in (7, 9, 12):
        surv, reason = sieve(b, m, vecs, [1, 2, 4, 8])
        naive = []
        allv = [vec for L in (1, 2, 4, 8) for vec in vecs[L]]
        for x in product(range(m), repeat=b.mu):
            if all(sum(c * v for c, v in zip(vec, x)) % m for vec in allv):
                naive.append(x)
        assert sorted(surv) == sorted(naive), (m, surv, naive)

    print("all anchors passed")


# ------------------------------------------------------------ truth census

def truth_census(base_name: str, m_lo: int, m_hi: int) -> None:
    """Exhaustive ground truth for one base over a range of m: build every
    Z_m lift (all assignments, both parities of m), keep the simple ones,
    and test actual presence of C4/C8/C16 with the validated detectors.

    For lift orders <= 30 the only power lengths <= order are 4, 8, 16, so
    a lift passing all applicable tests here would be a genuine
    counterexample to C001. This is truth-level (detector) data, strictly
    stronger than the walk-class certificate of the sieve."""
    base = BASES[base_name]()
    print(base.describe())
    for m in range(m_lo, m_hi + 1):
        order = base.n * m
        if order > 30:
            raise ValueError("truth census is exact only for orders <= 30")
        lengths = [L for L in (4, 8, 16) if L <= order]
        checked = simple = 0
        kill_counts = {L: 0 for L in lengths}
        survivors = []
        for x in product(range(m), repeat=base.mu):
            checked += 1
            try:
                adjacency = build_lift(base, m, x)
            except ValueError:
                continue
            simple += 1
            alive = True
            for L in lengths:
                if L == 4 and not SAT.codegree_c4_free(adjacency):
                    kill_counts[L] += 1
                    alive = False
                    break
                if L != 4 and SAT.has_cycle_of_length(adjacency, L):
                    kill_counts[L] += 1
                    alive = False
                    break
            if alive:
                survivors.append(x)
        print(f"m={m} order={order} assignments={checked} simple={simple} "
              f"killed_by={kill_counts} power_free={len(survivors)}")
        for x in survivors:
            print(f"    POWER-FREE SURVIVOR (counterexample candidate!): x={x}")
        sys.stdout.flush()


# -------------------------------------------------------------------- main

def run_sieve(base_name: str, m_lo: int, m_hi: int, lmax: int,
              odd_only: bool, verify_powers: list[int]) -> None:
    base = BASES[base_name]()
    print(base.describe())
    powers = power_targets(lmax)
    targets = [1, 2] + powers
    print(f"enumerating walk classes at lengths {targets} ...")
    vectors = walk_vectors(base, targets)
    for L in targets:
        vs = vectors[L]
        zero = (0,) * base.mu
        print(f"  |V_{L}| = {len(vs)}"
              + ("  (contains ZERO vector)" if zero in vs else ""))
    for m in range(m_lo, m_hi + 1):
        if odd_only and m % 2 == 0:
            continue
        order = base.n * m
        needed = [1, 2] + [p for p in powers if p <= order]
        exact = all(p in powers for p in power_targets(order))
        survivors, reason = sieve(base, m, vectors, needed)
        connected = [x for x in survivors
                     if gcd_many(list(x), m) == 1]
        canon = sorted({canonical_up_to_units(x, m) for x in connected})
        tag = "FULL" if exact else f"partial(only {needed[2:]} sieved)"
        print(f"m={m} order={order} [{tag}] survivors={len(survivors)} "
              f"connected={len(connected)} classes={len(canon)}"
              + (f" [{reason}]" if reason else ""))
        for x in canon[:8]:
            rep = verify_lift(base, m, x, verify_powers)
            checked = {k: v for k, v in rep.items() if k.startswith("has_C")}
            # L019 soundness: sieved lengths must be absent upstairs.
            for L in needed:
                key = f"has_C{L}"
                if key in checked and checked[key]:
                    raise AssertionError(
                        f"L019 violated: sieve-clean lift has C{L}: "
                        f"{base_name} m={m} x={x}"
                    )
            print(f"    x={x} -> {rep}")
        sys.stdout.flush()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)
    sub.add_parser("anchors")
    sub.add_parser("calibrate")
    p_vec = sub.add_parser("vectors")
    p_vec.add_argument("base", choices=sorted(BASES))
    p_vec.add_argument("lmax", type=int)
    p_sieve = sub.add_parser("sieve")
    p_sieve.add_argument("base", choices=sorted(BASES))
    p_sieve.add_argument("m_lo", type=int)
    p_sieve.add_argument("m_hi", type=int)
    p_sieve.add_argument("--lmax", type=int, default=32)
    p_sieve.add_argument("--all-m", action="store_true",
                         help="include even m (default: odd m only)")
    p_sieve.add_argument("--verify", type=int, nargs="*", default=[4, 8, 16],
                         help="power lengths to ground-truth on survivors")
    p_truth = sub.add_parser("truth")
    p_truth.add_argument("base", choices=sorted(BASES))
    p_truth.add_argument("m_lo", type=int)
    p_truth.add_argument("m_hi", type=int)
    args = parser.parse_args()

    if args.mode == "anchors":
        anchors()
    elif args.mode == "calibrate":
        calibrate()
    elif args.mode == "vectors":
        base = BASES[args.base]()
        print(base.describe())
        targets = [1, 2] + power_targets(args.lmax)
        vectors = walk_vectors(base, targets)
        zero = (0,) * base.mu
        for L in targets:
            vs = vectors[L]
            note = "  (contains ZERO vector)" if zero in vs else ""
            print(f"|V_{L}| = {len(vs)}{note}")
            if zero in vs:
                walk = find_walk(base, L, zero)
                print(f"  zero-vector witness walk (arcs): {walk}")
    elif args.mode == "sieve":
        run_sieve(args.base, args.m_lo, args.m_hi, args.lmax,
                  not args.all_m, args.verify)
    elif args.mode == "truth":
        truth_census(args.base, args.m_lo, args.m_hi)


if __name__ == "__main__":
    main()
