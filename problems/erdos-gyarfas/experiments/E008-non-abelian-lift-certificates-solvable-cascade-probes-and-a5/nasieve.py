"""E008 — non-abelian lift certificates (attempt A009).

Per-assignment walk certificate for voltage lifts over arbitrary finite
groups, given by multiplication tables. By the group-agnostic form of
L019 (see A009), a lift over Gamma with tree-gauge assignment
x in Gamma^mu has no cycle of length L provided no tailless
non-backtracking closed walk of length L in the base has net voltage
(ordered product, right multiplication) equal to the identity. Lengths
{1,2} are subsumed by the explicit simplicity preconditions below.

Groups: cyclic (anchor), Z_7 x| Z_3 (order 21, metabelian),
Heisenberg mod 3 (order 27, exponent 3, class 2), Z_9 x| Z_3 (order 27,
exponent 9), A_5 (order 60, perfect). The solvable groups are cascade
probes with pre-registered kill predictions (A009); A_5 is the live
test.

Exact integer arithmetic; no floating point; no randomness.
"""

from __future__ import annotations

import argparse
import importlib.util
import pathlib
import sys
from itertools import permutations, product

HERE = pathlib.Path(__file__).resolve().parent
E007_DIR = HERE.parent / "E007-cyclic-lift-sieve-for-power-free-graphs"


def _load(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


LIFTS = _load("e007_lifts", E007_DIR / "lifts.py")
SAT = LIFTS.SAT
BASES = LIFTS.BASES


# ------------------------------------------------------------------ groups

class Group:
    def __init__(self, name: str, mul: list[list[int]]):
        self.name = name
        self.n = len(mul)
        self.mul = mul
        self.e = 0
        self.inv = [next(h for h in range(self.n) if mul[g][h] == 0)
                    for g in range(self.n)]

    def order_of(self, g: int) -> int:
        k, acc = 1, g
        while acc != 0:
            acc = self.mul[acc][g]
            k += 1
        return k

    def check_axioms(self) -> None:
        n, mul = self.n, self.mul
        assert all(mul[0][g] == g and mul[g][0] == g for g in range(n))
        for g in range(n):
            assert mul[g][self.inv[g]] == 0 and mul[self.inv[g]][g] == 0
        for a in range(n):
            ma = mul[a]
            for b in range(n):
                mab = mul[ma[b]]
                mb = mul[b]
                for c in range(n):
                    assert mab[c] == ma[mb[c]], (a, b, c)

    def commutator_closure_size(self) -> int:
        n, mul, inv = self.n, self.mul, self.inv
        gens = {mul[mul[g][h]][mul[inv[g]][inv[h]]]
                for g in range(n) for h in range(n)}
        closure = {0} | gens
        frontier = list(closure)
        while frontier:
            g = frontier.pop()
            for h in list(closure):
                for prod in (mul[g][h], mul[h][g]):
                    if prod not in closure:
                        closure.add(prod)
                        frontier.append(prod)
        return len(closure)

    def is_abelian(self) -> bool:
        return all(self.mul[g][h] == self.mul[h][g]
                   for g in range(self.n) for h in range(self.n))


def group_cyclic(m: int) -> Group:
    return Group(f"Z{m}", [[(g + h) % m for h in range(m)] for g in range(m)])


def group_semidirect(p: int, q: int, r: int, name: str) -> Group:
    """Z_p x| Z_q with the Z_q generator acting by multiplication by r
    (requires r^q = 1 mod p). Element (a, b) has index b*p + a."""
    assert pow(r, q, p) == 1

    def idx(a: int, b: int) -> int:
        return b * p + a

    mul = [[0] * (p * q) for _ in range(p * q)]
    for a1 in range(p):
        for b1 in range(q):
            t = pow(r, b1, p)
            for a2 in range(p):
                for b2 in range(q):
                    mul[idx(a1, b1)][idx(a2, b2)] = idx(
                        (a1 + t * a2) % p, (b1 + b2) % q
                    )
    return Group(name, mul)


def group_heisenberg3() -> Group:
    """Upper unitriangular 3x3 matrices over Z_3: order 27, exponent 3,
    nilpotency class 2. Element (x, y, z) has index x*9 + y*3 + z."""

    def idx(x: int, y: int, z: int) -> int:
        return x * 9 + y * 3 + z

    mul = [[0] * 27 for _ in range(27)]
    for x1 in range(3):
        for y1 in range(3):
            for z1 in range(3):
                for x2 in range(3):
                    for y2 in range(3):
                        for z2 in range(3):
                            mul[idx(x1, y1, z1)][idx(x2, y2, z2)] = idx(
                                (x1 + x2) % 3,
                                (y1 + y2) % 3,
                                (z1 + z2 + x1 * y2) % 3,
                            )
    return Group("Heis3", mul)


def group_a5() -> Group:
    """Even permutations of 5 points; identity gets index 0."""
    def parity(perm: tuple[int, ...]) -> int:
        inversions = sum(
            1
            for i in range(5)
            for j in range(i + 1, 5)
            if perm[i] > perm[j]
        )
        return inversions % 2

    elements = sorted(p for p in permutations(range(5)) if parity(p) == 0)
    assert elements[0] == (0, 1, 2, 3, 4) and len(elements) == 60
    index = {p: i for i, p in enumerate(elements)}
    mul = [[0] * 60 for _ in range(60)]
    for gi, g in enumerate(elements):
        for hi, h in enumerate(elements):
            composed = tuple(g[h[i]] for i in range(5))
            mul[gi][hi] = index[composed]
    return Group("A5", mul)


GROUPS = {
    "z5": lambda: group_cyclic(5),
    "z7": lambda: group_cyclic(7),
    "z9": lambda: group_cyclic(9),
    "g21": lambda: group_semidirect(7, 3, 2, "Z7:Z3"),
    "heis3": group_heisenberg3,
    "g27b": lambda: group_semidirect(9, 3, 4, "Z9:Z3"),
    "a5": group_a5,
}


# ------------------------------------------------- assignment and certificate

def arc_voltages(base, G: Group, x: tuple[int, ...]) -> list[int] | None:
    """Voltage per arc under the tree gauge, or None if the lift is not
    simple. Simplicity: loops need c != e and c*c != e; two loops at one
    vertex need d not in {c, c^-1}; parallel edges (same ordered vertex
    pair as stored; all bases store parallel edges identically oriented)
    need pairwise distinct voltages, with tree edges carrying e."""
    vol = [0] * base.narcs
    for a in range(base.narcs):
        c = base.arc_coord[a]
        if c is None:
            vol[a] = G.e
        else:
            idxc, sign = c
            vol[a] = x[idxc] if sign == 1 else G.inv[x[idxc]]
    loops_at: dict[int, list[int]] = {}
    pair_volt: dict[tuple[int, int], list[int]] = {}
    for e_i, (u, v) in enumerate(base.edges):
        volt = vol[2 * e_i]
        if u == v:
            if volt == G.e or G.mul[volt][volt] == G.e:
                return None
            loops_at.setdefault(u, []).append(volt)
        else:
            pair_volt.setdefault((u, v), []).append(volt)
    for u, volts in loops_at.items():
        for i in range(len(volts)):
            for j in range(i + 1, len(volts)):
                if volts[j] in (volts[i], G.inv[volts[i]]):
                    return None
    for pair, volts in pair_volt.items():
        if len(set(volts)) != len(volts):
            return None
    return vol


def certificate_hits(base, G: Group, x: tuple[int, ...],
                     powers: list[int], first_only: bool):
    """Power lengths L (from `powers`, ascending) at which some tailless
    non-backtracking closed walk has net voltage e — i.e. the lengths at
    which the L019 certificate FAILS. Returns None if the lift is not
    simple, else a list of hit lengths (just the first if first_only)."""
    vol = arc_voltages(base, G, x)
    if vol is None:
        return None
    n, mul, e = G.n, G.mul, G.e
    lmax = max(powers)
    want = set(powers)
    hits: list[int] = []
    start_arcs = [a for a in range(base.narcs) if base.arc_coord[a] is not None]
    starts = []
    for s in start_arcs:
        starts.append((s, base.arc_tail[s], s ^ 1))
    # synchronized DP over (start index, arc, group element)
    narcs = base.narcs
    states: set[int] = set()
    for si, (s, _, _) in enumerate(starts):
        states.add((si * narcs + s) * n + vol[s])
    length = 1
    out_arcs = base.out_arcs
    heads = base.arc_head
    while True:
        if length in want:
            for code in states:
                g = code % n
                if g != e:
                    continue
                rest = code // n
                arc = rest % narcs
                si = rest // narcs
                s, s_tail, s_rev = starts[si]
                if heads[arc] == s_tail and arc != s_rev:
                    hits.append(length)
                    if first_only:
                        return hits
                    break
        if length >= lmax:
            return hits
        nxt: set[int] = set()
        for code in states:
            g = code % n
            rest = code // n
            arc = rest % narcs
            si = rest // narcs
            banned = arc ^ 1
            base_code = si * narcs
            for a2 in out_arcs[heads[arc]]:
                if a2 == banned:
                    continue
                nxt.add((base_code + a2) * n + mul[g][vol[a2]])
        states = nxt
        length += 1


def build_lift_group(base, G: Group, x: tuple[int, ...]) -> list[int]:
    """Explicit derived graph over the group (right multiplication)."""
    vol = arc_voltages(base, G, x)
    if vol is None:
        raise ValueError("assignment not admissible (non-simple lift)")
    n = base.n * G.n
    adjacency = [0] * n

    def vid(u: int, g: int) -> int:
        return u * G.n + g

    for e_i, (u, v) in enumerate(base.edges):
        volt = vol[2 * e_i]
        for g in range(G.n):
            p, q = vid(u, g), vid(v, G.mul[g][volt])
            if p == q or adjacency[p] & (1 << q):
                raise ValueError("non-simple lift slipped past preconditions")
            adjacency[p] |= 1 << q
            adjacency[q] |= 1 << p
    return adjacency


# ------------------------------------------------------------------- probes

def power_targets(limit: int) -> list[int]:
    out, p = [], 4
    while p <= limit:
        out.append(p)
        p *= 2
    return out


def probe(group_key: str, base_name: str, lmax: int | None) -> None:
    G = GROUPS[group_key]()
    base = BASES[base_name]()
    order = base.n * G.n
    powers = power_targets(min(lmax, order) if lmax else order)
    print(f"group={G.name} (order {G.n})  base={base.describe()}")
    print(f"lift order={order}  certificate lengths={powers}")
    total = nonsimple = 0
    first_hit: dict[int, int] = {}
    survivors: list[tuple[int, ...]] = []
    for x in product(range(G.n), repeat=base.mu):
        total += 1
        hits = certificate_hits(base, G, x, powers, first_only=True)
        if hits is None:
            nonsimple += 1
        elif hits:
            first_hit[hits[0]] = first_hit.get(hits[0], 0) + 1
        else:
            survivors.append(x)
    print(f"assignments={total} nonsimple={nonsimple} "
          f"first_hit={dict(sorted(first_hit.items()))} "
          f"survivors={len(survivors)}")
    for x in survivors:
        print(f"    SURVIVOR x={x}  (certified power-free through "
              f"{powers[-1]}; counterexample candidate if order covered)")
    sys.stdout.flush()


# ------------------------------------------------------------------ anchors

def anchors() -> None:
    # A1: group axioms and structure for every constructed group.
    g21 = GROUPS["g21"]()
    heis = GROUPS["heis3"]()
    g27b = GROUPS["g27b"]()
    a5 = GROUPS["a5"]()
    for G in (group_cyclic(5), group_cyclic(9), g21, heis, g27b, a5):
        G.check_axioms()
    assert not g21.is_abelian() and g21.commutator_closure_size() == 7
    assert not heis.is_abelian() and heis.commutator_closure_size() == 3
    assert all(heis.order_of(g) in (1, 3) for g in range(27))
    assert not g27b.is_abelian() and g27b.commutator_closure_size() == 3
    assert max(g27b.order_of(g) for g in range(27)) == 9
    assert not a5.is_abelian() and a5.commutator_closure_size() == 60
    assert sorted(set(a5.order_of(g) for g in range(60))) == [1, 2, 3, 5]

    # A2: bidirectional agreement with the E007 hyperplane engine on
    # cyclic groups: for every assignment and every power length, the
    # per-assignment DP hit must equal "some walk-class vector is
    # orthogonal to x mod m".
    for base_name in ("theta3", "dumbbell"):
        base = BASES[base_name]()
        vectors = LIFTS.walk_vectors(base, [4, 8, 16])
        for m in (5, 7, 9):
            G = group_cyclic(m)
            for x in product(range(m), repeat=base.mu):
                hits = certificate_hits(base, G, x, [4, 8, 16],
                                        first_only=False)
                vol_ok = arc_voltages(base, G, x) is not None
                assert (hits is not None) == vol_ok
                if hits is None:
                    continue
                for L in (4, 8, 16):
                    hyp = any(
                        sum(c * v for c, v in zip(vec, x)) % m == 0
                        for vec in vectors[L]
                    )
                    assert ((L in hits) == hyp), (base_name, m, x, L)

    # A3: Petersen: dumbbell over Z5, x=(1,2): first and only hit at 8
    # among lengths {4, 8} (order 10).
    base = BASES["dumbbell"]()
    hits = certificate_hits(base, group_cyclic(5), (1, 2), [4, 8],
                            first_only=False)
    assert hits == [8], hits

    # A4: explicit lift over cyclic tables equals the E007 builder.
    for base_name, m, x in (("theta3", 5, (1, 3)), ("dumbbell", 5, (1, 2))):
        b = BASES[base_name]()
        assert build_lift_group(b, group_cyclic(m), x) == \
            LIFTS.build_lift(b, m, x)

    # A5-anchor: certificate soundness spot check on a real lift: the
    # Petersen lift has no C4 and has C8; the certificate said hit at 8
    # only — consistent both ways (hit direction checked by detector).
    petersen = build_lift_group(base, group_cyclic(5), (1, 2))
    assert not SAT.has_cycle_of_length(petersen, 4)
    assert SAT.has_cycle_of_length(petersen, 8)

    print("all anchors passed")


# --------------------------------------------------------------------- main

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)
    sub.add_parser("anchors")
    p_probe = sub.add_parser("probe")
    p_probe.add_argument("group", choices=sorted(GROUPS))
    p_probe.add_argument("base", choices=sorted(BASES))
    p_probe.add_argument("--lmax", type=int, default=None)
    args = parser.parse_args()
    if args.mode == "anchors":
        anchors()
    else:
        probe(args.group, args.base, args.lmax)


if __name__ == "__main__":
    main()
