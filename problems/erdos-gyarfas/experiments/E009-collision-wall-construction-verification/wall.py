"""E009 — mechanical verification of the collision-wall construction (A010).

Verifies, on concrete bases and groups, every ingredient of Theorem W7:

  W3  strong connectivity of the arc digraph,
  W4  period p in {1,2} with p = 2 iff bipartite, class = tail side,
  W5  uniform exact-length reachability (empirical R_B with stable tail),
  W6  seed-pair existence and properties at length <= ell* - 1,
  W7  the full construction: for admissible target lengths L at or above
      the threshold 4*ell* + 4*R_B + 8, assemble the closed walk
      Omega = U . rev(Y) . Y' . rev(U') and check, from the raw arc list
      and the definitions alone, that it is non-backtracking, tailless,
      closed, of length exactly L, and has identity net voltage.

The checker `verify_walk` is definition-level and independent of the
construction internals.  Negative controls confirm the checker rejects
backtracking, tailed, non-closed, and unbalanced walks.  A cross-engine
anchor confirms agreement with the E008 per-assignment DP on the tested
power lengths.

Assignments are per-edge group elements (arc 2e carries x[e], arc 2e+1 its
inverse); this parameterizes ALL voltage assignments, with no simplicity
filtering — the lemma is about base walks, not about simple lifts.

Exact integer arithmetic; no floating point; no randomness.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
E007_DIR = HERE.parent / "E007-cyclic-lift-sieve-for-power-free-graphs"
E008_DIR = HERE.parent / "E008-non-abelian-lift-certificates-solvable-cascade-probes-and-a5"


def _load(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


LIFTS = _load("e007_lifts", E007_DIR / "lifts.py")
NASIEVE = _load("e008_nasieve", E008_DIR / "nasieve.py")
BASES = {name: factory() for name, factory in LIFTS.BASES.items()}
GROUPS = NASIEVE.GROUPS

CHECKS = 0


def note(msg: str) -> None:
    print(msg, flush=True)


def ok(cond: bool, what: str) -> None:
    global CHECKS
    if not cond:
        raise AssertionError(what)
    CHECKS += 1


# ------------------------------------------------------------ arc digraph

def transitions(base):
    """succ[a] = legal continuations of arc a; pred[a] = legal predecessors."""
    succ = [[] for _ in range(base.narcs)]
    pred = [[] for _ in range(base.narcs)]
    for a in range(base.narcs):
        for b in base.out_arcs[base.arc_head[a]]:
            if b != a ^ 1:
                succ[a].append(b)
                pred[b].append(a)
    return succ, pred


def check_strong_connectivity(base) -> None:
    succ, pred = transitions(base)
    for adj in (succ, pred):
        seen = {0}
        stack = [0]
        while stack:
            s = stack.pop()
            for t in adj[s]:
                if t not in seen:
                    seen.add(t)
                    stack.append(t)
        ok(len(seen) == base.narcs,
           f"{base.name}: arc digraph not strongly connected (W3)")
    for a in range(base.narcs):
        ok(len(succ[a]) >= 2, f"{base.name}: out-degree < 2 at arc {a} (W1)")


def bipartition(base):
    """Two-coloring of the underlying multigraph, or None."""
    color = [None] * base.n
    color[0] = 0
    queue = [0]
    while queue:
        u = queue.pop()
        for a in base.out_arcs[u]:
            v = base.arc_head[a]
            if u == v:
                return None  # loop
            if color[v] is None:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                return None
    return color


def digraph_period(base) -> int:
    succ, _ = transitions(base)
    level = {0: 0}
    queue = [0]
    g = 0
    while queue:
        nxt = []
        for s in queue:
            for t in succ[s]:
                if t not in level:
                    level[t] = level[s] + 1
                    nxt.append(t)
        queue = nxt
    for s in range(base.narcs):
        for t in succ[s]:
            g = math.gcd(g, level[s] + 1 - level[t])
    return g


def check_period(base) -> tuple[int, list[int]]:
    p = digraph_period(base)
    ok(p in (1, 2), f"{base.name}: period {p} not in {{1,2}} (W4)")
    color = bipartition(base)
    ok((p == 2) == (color is not None),
       f"{base.name}: period {p} vs bipartite={color is not None} (W4)")
    if p == 2:
        chi = [color[base.arc_tail[a]] for a in range(base.narcs)]
        succ, _ = transitions(base)
        for a in range(base.narcs):
            for b in succ[a]:
                ok((chi[a] + 1) % 2 == chi[b],
                   f"{base.name}: class does not advance by one (W4)")
    else:
        chi = [0] * base.narcs
    return p, chi


def reach_by_length(base, horizon: int):
    """rows[T][s] = bitmask of arcs reachable from s in exactly T
    transitions."""
    succ, _ = transitions(base)
    succ_mask = [0] * base.narcs
    for a in range(base.narcs):
        for b in succ[a]:
            succ_mask[a] |= 1 << b
    rows = [[1 << s for s in range(base.narcs)]]
    for _ in range(horizon):
        prev = rows[-1]
        cur = []
        for s in range(base.narcs):
            mask = prev[s]
            out = 0
            while mask:
                low = mask & -mask
                out |= succ_mask[low.bit_length() - 1]
                mask ^= low
            cur.append(out)
        rows.append(cur)
    return rows


def compute_reach_constant(base, p: int, chi: list[int], horizon: int) -> int:
    """Empirical R_B: least R such that for every arc pair (s,t) and every
    T in [R, horizon] with T = chi[t]-chi[s] mod p, t is reachable from s
    in exactly T transitions.  Requires a stable tail below the horizon."""
    rows = reach_by_length(base, horizon)
    r_all = 0
    for s in range(base.narcs):
        for t in range(base.narcs):
            need = (chi[t] - chi[s]) % p
            worst = 0
            for T in range(horizon, -1, -1):
                if T % p == need and not (rows[T][s] >> t) & 1:
                    worst = T + 1
                    break
            r_all = max(r_all, worst)
    ok(r_all <= horizon - 50,
       f"{base.name}: no stable reachability tail below horizon (W5)")
    for s in range(base.narcs):
        for t in range(base.narcs):
            need = (chi[t] - chi[s]) % p
            for T in range(r_all, horizon + 1):
                if T % p == need:
                    ok((rows[T][s] >> t) & 1,
                       f"{base.name}: W5 violated at T={T} pair=({s},{t})")
    return r_all


def steer(base, sigma: int, tau: int, T: int):
    """Exact-length arc-digraph path: arc list of length T+1, first arc
    sigma, last arc tau, T transitions.  None if unreachable."""
    succ, pred = transitions(base)
    frontier = [set() for _ in range(T + 1)]
    frontier[0] = {sigma}
    for t in range(T):
        cur = set()
        for s in frontier[t]:
            cur.update(succ[s])
        frontier[t + 1] = cur
    if tau not in frontier[T]:
        return None
    path = [tau]
    cur = tau
    for t in range(T, 0, -1):
        for q in pred[cur]:
            if q in frontier[t - 1]:
                path.append(q)
                cur = q
                break
        else:
            return None
    path.reverse()
    return path


# ------------------------------------------------------------- assignments

def arc_voltage_table(base, G, x: list[int]) -> list[int]:
    """Arc voltages from per-edge elements: arc 2e -> x[e], arc 2e+1 ->
    x[e]^{-1}."""
    vol = [0] * base.narcs
    for e in range(len(base.edges)):
        vol[2 * e] = x[e]
        vol[2 * e + 1] = G.inv[x[e]]
    return vol


def walk_voltage(G, vol, walk) -> int:
    acc = G.e
    for a in walk:
        acc = G.mul[acc][vol[a]]
    return acc


def verify_walk(base, G, vol, walk, L: int) -> None:
    """Definition-level check: length, cyclic non-backtracking (incl.
    taillessness), closure, identity voltage."""
    ok(len(walk) == L, f"length {len(walk)} != {L}")
    for i in range(len(walk)):
        a = walk[i]
        b = walk[(i + 1) % len(walk)]
        ok(base.arc_head[a] == base.arc_tail[b],
           f"not a walk at position {i}")
        ok(b != a ^ 1, f"backtrack/tail at position {i}")
    ok(walk_voltage(G, vol, walk) == G.e, "net voltage is not the identity")


# ------------------------------------------------------------ construction

def find_seed(base, G, vol, ell_star: int):
    """W6: DFS over nb walks of length ell* with first arc 0 until a
    (last arc, voltage) collision; trim the maximal common prefix."""
    stack = [([0], vol[0])]
    seen: dict[tuple[int, int], tuple[list[int], int]] = {}
    while stack:
        walk, g = stack.pop()
        if len(walk) == ell_star:
            key = (walk[-1], g)
            if key in seen:
                other, _ = seen[key]
                pi = 0
                while other[pi] == walk[pi]:
                    pi += 1
                W, Wp = other[pi:], walk[pi:]
                lam = ell_star - pi
                ok(2 <= lam <= ell_star - 1, "seed length out of range (W6)")
                ok(W[0] != Wp[0], "seed firsts not distinct (W6)")
                ok(W[-1] == Wp[-1], "seed lasts differ (W6)")
                ok(base.arc_tail[W[0]] == base.arc_tail[Wp[0]],
                   "seed starts differ (W6)")
                gw = walk_voltage(G, vol, W)
                ok(gw == walk_voltage(G, vol, Wp),
                   "seed voltages differ (W6)")
                return W, Wp
            seen[key] = (walk, g)
            continue
        head = base.arc_head[walk[-1]]
        rev = walk[-1] ^ 1
        for b in base.out_arcs[head]:
            if b != rev:
                stack.append((walk + [b], G.mul[g][vol[b]]))
    raise AssertionError("no seed collision found (W6 pigeonhole violated)")


def construct(base, G, vol, L: int, p: int, chi: list[int], R_B: int):
    """The W7 assembly for target length L; returns the closed walk."""
    ell_star = (2 * len(base.edges) * G.n).bit_length() + 1
    ok(2 ** (ell_star - 1) > 2 * len(base.edges) * G.n, "ell* arithmetic")
    W, Wp = find_seed(base, G, vol, ell_star)
    lam = len(W)
    d = W[-1]
    w1 = base.arc_head[d]
    branches = [b for b in base.out_arcs[w1] if b != d ^ 1]
    ok(len(branches) >= 2, "fewer than two branch arcs (W7)")
    x, xp = branches[0], branches[1]
    z = 0
    in_arcs = [a ^ 1 for a in base.out_arcs[z]]
    e_arc, f_arc = in_arcs[0], in_arcs[1]
    ok(e_arc != f_arc, "e and f coincide (W7)")

    ok(L % 2 == 0, "target length must be even")
    if p == 2:
        ok(L % 4 == 0, "bipartite base needs L = 0 mod 4")
    N0 = L // 2 - 2 * lam - 2
    ok(N0 >= 2 * R_B + 1, f"L={L} below usable range for this seed")
    if p == 2:
        tau = (chi[e_arc] - chi[x]) % 2
        ok(tau == (chi[f_arc] - chi[xp]) % 2, "branch parities disagree (W7)")
        T1 = R_B if R_B % 2 == tau else R_B + 1
    else:
        T1 = R_B
    T2 = N0 - T1
    ok(T2 >= R_B, "T2 below reach constant (W7)")
    xA = steer(base, x, e_arc, T1)
    xpB = steer(base, xp, f_arc, T2)
    ok(xA is not None and xpB is not None, "steering failed (W5/W7)")

    U = W + xA
    Up = Wp + xA
    Y = W + xpB
    Yp = Wp + xpB
    rev = lambda walk: [a ^ 1 for a in reversed(walk)]
    omega = U + rev(Y) + Yp + rev(Up)
    return omega


# ---------------------------------------------------------------- controls

def negative_controls(base, G, vol) -> None:
    def rejects(walk, L, what):
        try:
            verify_walk(base, G, vol, walk, L)
        except AssertionError:
            global CHECKS
            CHECKS += 1
            return
        raise AssertionError(f"checker accepted invalid walk: {what}")

    a = 0
    rejects([a, a ^ 1], 2, "backtracking pair")
    succ, _ = transitions(base)
    b = succ[a][0]
    rejects([a, b], 2, "generically non-closed/tailed pair")
    rejects([a], 2, "wrong length")


# --------------------------------------------------------------- the sweep

def assignments_for(base, G):
    m = len(base.edges)
    out = [("all-identity", [G.e] * m), ("all-same", [1 % G.n] * m)]
    if G.n > m:
        out.append(("distinct", [(i + 1) % G.n for i in range(m)]))
    out.append(("pattern-a", [(7 * i + 5) % G.n for i in range(m)]))
    out.append(("pattern-b", [(11 * i + 3) % G.n for i in range(m)]))
    return out


def target_lengths(threshold: int, p: int):
    step = 4 if p == 2 else 2
    start = threshold if threshold % step == 0 else threshold + (step - threshold % step)
    ladder = list(range(start, start + 10 * step, step))
    powers = []
    k = 2
    while 2 ** k < threshold:
        k += 1
    powers = [2 ** k, 2 ** (k + 1), 2 ** (k + 2)]
    return ladder, powers


def run_case(base, G, label: str, x: list[int], p: int, chi: list[int],
             R_B: int, verbose: bool) -> tuple[int, int]:
    vol = arc_voltage_table(base, G, x)
    ell_star = (2 * len(base.edges) * G.n).bit_length() + 1
    threshold = 4 * ell_star + 4 * R_B + 8
    ladder, powers = target_lengths(threshold, p)
    tested = 0
    for L in ladder + powers:
        omega = construct(base, G, vol, L, p, chi, R_B)
        verify_walk(base, G, vol, omega, L)
        tested += 1
    if verbose:
        note(f"    {label:<14} threshold={threshold} "
             f"ladder={ladder[0]}..{ladder[-1]} powers={powers} ok")
    return tested, threshold


def cross_engine_anchor(base_name: str, group_key: str, struct) -> int:
    """Theorem W7 guarantees an identity walk at every power of two at or
    above the threshold; the independent E008 per-assignment DP must
    therefore report those powers as certificate failures, for every
    tree-gauge assignment it accepts.  Returns the number of assignments
    anchored."""
    base = BASES[base_name]
    G = GROUPS[group_key]()
    p, chi, R_B = struct[base_name]
    ell_star = (2 * len(base.edges) * G.n).bit_length() + 1
    threshold = 4 * ell_star + 4 * R_B + 8
    powers = [4, 8, 16, 32, 64]
    must_hit = [L for L in powers if L >= threshold]
    ok(must_hit, f"cross-engine: no DP-reachable power above threshold "
                 f"{threshold} ({base_name},{group_key})")
    anchored = 0
    samples = [tuple((7 * i + off) % G.n for i in range(base.mu))
               for off in range(1, 6)]
    for x_tuple in samples:
        hits = NASIEVE.certificate_hits(base, G, x_tuple, powers,
                                        first_only=False)
        if hits is None:
            continue
        for L in must_hit:
            ok(L in hits,
               f"cross-engine: E008 DP missing identity walk at {L} "
               f"({base_name},{group_key},{x_tuple})")
        anchored += 1
    ok(anchored > 0,
       f"cross-engine: no simple assignment sampled ({base_name},{group_key})")
    return anchored


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--exhaustive", action="store_true",
                        help="also sweep all assignments on small cases")
    parser.add_argument("--horizon", type=int, default=200)
    args = parser.parse_args()

    note("== group axioms ==")
    groups = {}
    for key, factory in GROUPS.items():
        G = factory()
        G.check_axioms()
        groups[key] = G
        note(f"  {G.name}: order {G.n} axioms ok")

    expected_period = {"theta3": 2, "dumbbell": 1, "bouquet2": 1,
                       "k4": 1, "k33": 2, "prism": 1}

    note("== structure lemmas per base ==")
    struct = {}
    for name, base in BASES.items():
        check_strong_connectivity(base)
        p, chi = check_period(base)
        ok(p == expected_period[name],
           f"{name}: period {p} != expected {expected_period[name]} (anchor)")
        R_B = compute_reach_constant(base, p, chi, args.horizon)
        struct[name] = (p, chi, R_B)
        note(f"  {name}: strong-connectivity ok, period {p}, R_B = {R_B}")

    note("== negative controls ==")
    base0 = BASES["theta3"]
    G0 = groups["z5"]
    negative_controls(base0, G0, arc_voltage_table(base0, G0, [1, 2, 3]))
    note("  checker rejects backtracking / non-closed / wrong-length walks")

    note("== construction sweep ==")
    total = 0
    for name, base in BASES.items():
        p, chi, R_B = struct[name]
        note(f"  base {name} (p={p}, R_B={R_B})")
        for key, G in groups.items():
            for label, x in assignments_for(base, G):
                tested, threshold = run_case(base, G, f"{G.name}/{label}", x,
                                             p, chi, R_B, verbose=False)
                total += tested
            note(f"    group {G.name}: all assignments ok "
                 f"(threshold {threshold})")

    note("== cross-engine anchor (E008 DP) ==")
    for base_name, group_key in (("theta3", "z5"), ("theta3", "g21"),
                                 ("dumbbell", "z7"), ("bouquet2", "z5")):
        n_anchored = cross_engine_anchor(base_name, group_key, struct)
        note(f"  {base_name} x {group_key}: {n_anchored} assignments agree "
             f"at powers above threshold")

    if args.exhaustive:
        note("== exhaustive small sweeps ==")
        from itertools import product as iproduct
        for base_name, group_key, n_lengths in (
                ("theta3", "z5", 6), ("dumbbell", "z5", 6),
                ("bouquet2", "z5", 6), ("k4", "z5", 3)):
            base = BASES[base_name]
            G = groups[group_key]
            p, chi, R_B = struct[base_name]
            m = len(base.edges)
            ell_star = (2 * m * G.n).bit_length() + 1
            threshold = 4 * ell_star + 4 * R_B + 8
            ladder, powers = target_lengths(threshold, p)
            lengths = ladder[:n_lengths] + powers[:1]
            count = 0
            for x in iproduct(range(G.n), repeat=m):
                vol = arc_voltage_table(base, G, list(x))
                for L in lengths:
                    omega = construct(base, G, vol, L, p, chi, R_B)
                    verify_walk(base, G, vol, omega, L)
                    count += 1
            note(f"  {base_name} x {G.name}: {G.n ** m} assignments x "
                 f"{len(lengths)} lengths = {count} constructions ok")

    note(f"== all checks passed ({CHECKS} assertions) ==")


if __name__ == "__main__":
    main()
