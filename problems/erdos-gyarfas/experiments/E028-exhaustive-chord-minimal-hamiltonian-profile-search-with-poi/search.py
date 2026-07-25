#!/usr/bin/env python3
"""E028 -- exhaustive chord-minimal Hamiltonian profile search (P-002, S027; A027).

TARGET.  (F) for the case-(5b) residual object, restricted to pairs that
carry a Hamiltonian a-b path.  Concretely, the search decides:

    (H-F)  Is there a simple graph H of order n with two vertices a, b of
           degree 2, every other degree >= 3, no C4 and no C8, carrying a
           HAMILTONIAN a-b path, with

               S(H,a,b) cap {2,6,14,30} = empty      (no poison length)

           and (for the full (F) target) additionally no C16 and no C32?

A YES at any n in [18,35] is a case-(5b) residual object of the Hamiltonian
kind -- its 2-path closure is a tight 1-atom, the standing disproof-adjacent
pivot trigger.  A NO for every n in the window closes case (5b) below order
36 for every residual object with a Hamiltonian through-path, which is the
whole (F) program on that stratum.

THE REDUCTION THE SEARCH RESTS ON (A027 T1, proved).  Let P = v_0..v_M be a
Hamiltonian a-b path of such an H (M = n-1), and let C be its chord set
(E(H) minus E(P)).  Then

  * every internal position 0 < i < M has chord-degree >= 1 (degree >= 3),
  * positions 0 and M have chord-degree exactly 1 (degree 2),

so C is a COVER of {0,..,M}.  Pass to any inclusion-minimal subcover
C' <= C.  Then H' = P + C' is again such a graph (subgraphs stay C4/C8-free,
S(H') <= S(H) stays poison-free, the unique chords at 0 and M survive), and
in C' every chord has an endpoint of chord-degree 1.  So it suffices to
enumerate CHORD-MINIMAL systems.

THE PRUNE (A027 T2, proved).  If D = {(i_1,j_1),..,(i_t,j_t)} <= C' has
i_1 < j_1 <= i_2 < j_2 <= ... <= i_t < j_t (interior-disjoint intervals),
then replacing each arc P[i_k,j_k] by its chord yields an a-b PATH of length
M - sum_k (j_k - i_k - 1).  So a "monotone reroute" of length 2, 6, 14 or 30
kills the branch outright.  The reachable-savings set is a left-to-right DP,
so the prune fires on prefixes.

Both facts are one-directional (necessary conditions on a hypothetical
dodger), so an EMPTY search is a proof for the searched stratum, while a
survivor is only a candidate: survivors are re-checked exactly (full path
enumeration for S, cycle enumeration for C16/C32) by `verify`.

Commands:
  search.py anchors            # 80,131 checks (both interpreters before production)
  search.py brute M0 M1        # brute-force reference enumeration (small M)
  search.py search M0 M1 [c16] # the production search over M in [M0,M1]
  search.py certify [file]     # independent re-verification of stored survivors
  search.py verify [file]      # exact re-check of every stored survivor

Anchor families a6 and a7 were added after the delegated audit R003, which
found that the original suite never exercised the C16 detector on a positive
instance, nor the poison prune / symmetry break on a nonempty set (its a3
comparisons are structurally empty-vs-empty, because the {C4,C8}-free
chord-minimal class is itself empty below order 19).  Those three are the
prunes whose failure could delete a genuine counterexample, so a6/a7 are the
checks the verdict actually rests on.
"""

import json
import os
import sys
import time

sys.dont_write_bytecode = True
import importlib.util                   # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
EXPS = os.path.dirname(HERE)
E026_DIR = os.path.join(
    EXPS, "E026-s-gap-census-over-the-c4-c8-free-classes-at-orders-10-20-poi")
E026_DATA = os.path.join(E026_DIR, "data")


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_before = sorted(os.listdir(E026_DATA))
census = _load("e026_census", os.path.join(E026_DIR, "census.py"))
_after = sorted(os.listdir(E026_DATA))
assert _before == _after, "importing E026/census.py changed E026/data"
os.makedirs(DATA, exist_ok=True)
census.DATA = DATA
census.scan.DATA = DATA
census.e021.DATA = DATA
census.e021.scan.DATA = DATA
import pathlib                           # noqa: E402
census.e021.cat.DATA = pathlib.Path(DATA)

g6_decode = census.g6_decode
degrees = census.degrees
bfs_dist = census.bfs_dist
has_cycle_len = census.has_cycle_len
count_cycles_len = census.count_cycles_len
paths_with_essential = census.paths_with_essential
petersen_minus_e = census.petersen_minus_e
interpreter = census.scan.interpreter

N14_G6 = census.N14_G6
N19_G6 = census.N19_G6

# ----------------------------------------------------------------------
# constants of the target

POISON = (2, 6, 14, 30)          # S must avoid these (S+2 avoids the powers)
POWERS = (4, 8, 16, 32)          # Spec(H) must avoid these
CLASS_FORBIDDEN = (4, 8)         # the class constraint used INSIDE the search
WINDOW = (18, 35)                # order window of the residual object


# ----------------------------------------------------------------------
# primitives on the path-plus-chords graph


def path_adjacency(M):
    """Adjacency bitmasks of the bare path v_0..v_M."""
    adj = [0] * (M + 1)
    for i in range(M):
        adj[i] |= 1 << (i + 1)
        adj[i + 1] |= 1 << i
    return adj


def has_cycle_through_edge(adj, u, w, L):
    """True iff a cycle of length L uses edge uw (which must be in adj)."""
    if L < 3:
        return False
    wbit = 1 << w
    steps = L - 1                       # edges of the u..w path avoiding uw
    stack = [(u, 1 << u, 0)]
    while stack:
        v, used, d = stack.pop()
        if d == steps - 1:
            if v != u and (adj[v] >> w) & 1:
                return True
            continue
        row = adj[v] & ~used & ~wbit
        while row:
            low = row & -row
            x = low.bit_length() - 1
            row ^= low
            stack.append((x, used | low, d + 1))
    return False


def creates_forbidden(adj, u, w, forbidden):
    for L in forbidden:
        if has_cycle_through_edge(adj, u, w, L):
            return L
    return 0


# -- fast specialisations used in production (validated against the generic
#    routine above by the anchor suite on every graph it enumerates) --------


def _c4_through(adj, u, w):
    """A 4-cycle through edge uw: u-x-y-w with x,y distinct, != u,w."""
    ubit, wbit = 1 << u, 1 << w
    nw = adj[w] & ~ubit & ~wbit
    row = adj[u] & ~wbit & ~ubit
    while row:
        low = row & -row
        x = low.bit_length() - 1
        row ^= low
        if adj[x] & nw & ~low & ~ubit:
            return True
    return False


def _walk(adj, v, used, w, wbit, depth):
    """A `depth`-edge simple path from v to w avoiding `used` (w excluded)."""
    if depth == 1:
        return (adj[v] >> w) & 1
    row = adj[v] & ~used & ~wbit
    while row:
        low = row & -row
        x = low.bit_length() - 1
        row ^= low
        if _walk(adj, x, used | low, w, wbit, depth - 1):
            return True
    return False


def creates_forbidden_fast(adj, u, w, forbidden):
    """Same verdict as creates_forbidden, specialised for speed."""
    for L in forbidden:
        if L == 4:
            if _c4_through(adj, u, w):
                return 4
        elif _walk(adj, u, 1 << u, w, 1 << w, L - 1):
            return L
    return 0


def cycle_lengths_present(adj, lengths):
    """Which of `lengths` occur as cycle lengths of the whole graph."""
    return sorted(L for L in lengths if has_cycle_len(adj, L))


def through_set(adj, a, b):
    """Exact set of a-b path lengths (edges), via the E018 enumerator."""
    lens, _ = paths_with_essential(adj, a, b)
    return sorted(lens)


def savings_reach(M, chords):
    """Bitmask of savings realizable by interior-disjoint chord families."""
    into = {}
    for i, j in chords:
        into.setdefault(j, []).append(i)
    R = [0] * (M + 1)
    R[0] = 1
    for p in range(1, M + 1):
        mask = R[p - 1]
        for i in into.get(p, ()):
            mask |= R[i] << (p - i - 1)
        R[p] = mask
    return R[M]


def savings_reach_brute(M, chords):
    """Reference: enumerate interior-disjoint families directly."""
    out = {0}
    chords = sorted(chords)
    k = len(chords)

    def rec(idx, last_right, total):
        out.add(total)
        for t in range(idx, k):
            i, j = chords[t]
            if i >= last_right:
                rec(t + 1, j, total + (j - i - 1))

    rec(0, 0, 0)
    mask = 0
    for s in out:
        mask |= 1 << s
    return mask


def target_mask(M, poison=POISON):
    mask = 0
    hits = []
    for p in poison:
        t = M - p
        if 0 <= t <= M:
            mask |= 1 << t
            hits.append(p)
    return mask, hits


# ----------------------------------------------------------------------
# cover / minimality helpers (used by the brute reference and the anchors)


def is_cover(M, chords):
    seen = set()
    for i, j in chords:
        seen.add(i)
        seen.add(j)
    return len(seen) == M + 1


def chord_degrees(M, chords):
    deg = [0] * (M + 1)
    for i, j in chords:
        deg[i] += 1
        deg[j] += 1
    return deg


def is_minimal_cover(M, chords):
    if not is_cover(M, chords):
        return False
    deg = chord_degrees(M, chords)
    return all(deg[i] == 1 or deg[j] == 1 for i, j in chords)


def build(M, chords):
    adj = path_adjacency(M)
    for i, j in chords:
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    return adj


# ----------------------------------------------------------------------
# THE SEARCH


class Search(object):
    """DFS over chord-minimal covers of {0..M}, poison-pruned."""

    def __init__(self, M, forbidden=CLASS_FORBIDDEN, poison=POISON,
                 use_poison=True, require_minimal=True, symmetry=True,
                 collect_limit=100000, node_cap=None):
        self.M = M
        self.n = M + 1
        self.forbidden = tuple(forbidden)
        self.use_poison = use_poison
        self.tmask, self.thits = target_mask(M, poison)
        if not use_poison:
            self.tmask = 0
        self.require_minimal = require_minimal
        self.symmetry = symmetry
        self.collect_limit = collect_limit
        self.node_cap = node_cap
        self.adj = path_adjacency(M)
        self.deg = [0] * self.n              # chord degree, final after step p
        self.into = [[] for _ in range(self.n)]
        self.out = [[] for _ in range(self.n)]
        self.reserved = [False] * self.n     # must end with chord-degree 1
        self.R = [0] * self.n
        self.chords = []
        self.survivors = []
        self.nodes = 0
        self.prunes = {"poison": 0, "cover": 0, "minimal": 0,
                       "cycle": 0, "count": 0, "symmetry": 0, "reserve": 0}
        self.s0 = None
        self.capped = False

    # -- constraint checks -------------------------------------------------

    def _add_chord(self, i, j):
        self.adj[i] |= 1 << j
        self.adj[j] |= 1 << i
        self.deg[i] += 1
        self.deg[j] += 1
        self.into[j].append(i)
        self.out[i].append(j)
        self.chords.append((i, j))

    def _drop_chord(self, i, j):
        self.adj[i] &= ~(1 << j)
        self.adj[j] &= ~(1 << i)
        self.deg[i] -= 1
        self.deg[j] -= 1
        self.into[j].pop()
        self.out[i].pop()
        self.chords.pop()

    # -- the driver --------------------------------------------------------

    def run(self):
        self.step(0)
        return self.survivors

    def step(self, p):
        if self.node_cap is not None and self.nodes > self.node_cap:
            self.capped = True
            return
        self.nodes += 1
        M = self.M
        # 1. finalize the savings DP at p (all chords into p are decided)
        if p == 0:
            self.R[0] = 1
        else:
            mask = self.R[p - 1]
            for i in self.into[p]:
                mask |= self.R[i] << (p - i - 1)
            self.R[p] = mask
        if self.tmask and (self.R[p] & self.tmask):
            self.prunes["poison"] += 1
            return
        # 2. branch over the outgoing chord set at p
        self.choose(p, p + 2)

    def choose(self, p, start):
        M = self.M
        # (a) the current outgoing set is complete -> close position p
        self.close(p)
        # (b) extend it
        if len(self.chords) >= self.n:
            self.prunes["count"] += 1
            return
        if p == 0 and self.deg[0] >= 1:
            return                        # a has exactly one chord
        if self.require_minimal and self.reserved[p]:
            return                        # p is somebody's private endpoint
        for q in range(start, self.n):
            if self.require_minimal and self.reserved[q]:
                self.prunes["reserve"] += 1
                continue
            if q == M and self.symmetry and self.s0 is not None:
                if M - p < self.s0:
                    self.prunes["symmetry"] += 1
                    continue
            if q == M and self.deg[M] >= 1:
                continue                  # b has exactly one chord
            self._add_chord(p, q)
            bad = creates_forbidden_fast(self.adj, p, q, self.forbidden)
            if bad:
                self.prunes["cycle"] += 1
                self._drop_chord(p, q)
                continue
            if p == 0:
                self.s0 = q
            self.choose(p, q + 1)
            if p == 0:
                self.s0 = None
            self._drop_chord(p, q)

    def close(self, p):
        """Position p is now final. Check it, propagate minimality, descend."""
        M = self.M
        d = self.deg[p]
        if p == 0 or p == M:
            if d != 1:
                self.prunes["cover"] += 1
                return
        elif d == 0:
            self.prunes["cover"] += 1
            return
        held = []
        if self.require_minimal and d >= 2:
            # p is nobody's private endpoint, so EVERY chord at p must have
            # its other endpoint of final chord-degree 1
            for i in self.into[p]:
                if self.deg[i] >= 2:      # that endpoint is final and not private
                    self.prunes["minimal"] += 1
                    return
            for q in self.out[p]:
                if self.deg[q] != 1:      # another chord already touches q
                    self.prunes["minimal"] += 1
                    for r in held:
                        self.reserved[r] = False
                    return
                self.reserved[q] = True
                held.append(q)
        if p == M:
            self.record()
        else:
            self.step(p + 1)
        for r in held:
            self.reserved[r] = False

    def record(self):
        if len(self.survivors) < self.collect_limit:
            self.survivors.append(tuple(sorted(self.chords)))
        else:
            self.capped = True


# ----------------------------------------------------------------------
# brute-force reference (small M): all chord subsets


def brute_force(M, forbidden=CLASS_FORBIDDEN, poison=POISON, use_poison=True,
                require_minimal=True):
    """Independent reference enumeration.

    Deliberately unlike `Search`: it walks the flat candidate-pair list
    (not positions), tests forbidden cycles with `has_cycle_len` (the
    E019 whole-graph detector, not the incremental through-edge one),
    computes savings with `savings_reach_brute` (explicit family
    enumeration, not the DP), applies coverage/minimality only at the
    leaf, and breaks no symmetry.  Only two prunes are shared, both
    monotone and obviously sound: chord count and forbidden cycles.
    """
    n = M + 1
    cand = [(i, j) for i in range(n) for j in range(i + 2, n)]
    tmask, _ = target_mask(M, poison)
    if not use_poison:
        tmask = 0
    out = []
    k = len(cand)
    cap = n                              # a minimal cover has <= n chords

    def rec(idx, chosen, adj):
        if idx == k:
            deg = chord_degrees(M, chosen)
            if deg[0] != 1 or deg[M] != 1:
                return
            if any(deg[p] == 0 for p in range(1, M)):
                return
            if require_minimal and not all(
                    deg[i] == 1 or deg[j] == 1 for i, j in chosen):
                return
            if tmask and (savings_reach_brute(M, chosen) & tmask):
                return
            out.append(tuple(sorted(chosen)))
            return
        # remaining positions that can still be covered
        rec(idx + 1, chosen, adj)
        if len(chosen) >= cap:
            return
        i, j = cand[idx]
        adj2 = list(adj)
        adj2[i] |= 1 << j
        adj2[j] |= 1 << i
        for L in forbidden:
            if has_cycle_len(adj2, L):
                return
        rec(idx + 1, chosen + [(i, j)], adj2)

    rec(0, [], path_adjacency(M))
    return out


# ----------------------------------------------------------------------
# named objects


def load_profile_objects():
    rows = []
    for part in range(16):
        path = os.path.join(E026_DATA, "census_n19_part%dof16.json" % part)
        with open(path) as fh:
            rows.extend(json.load(fh)["exactly_two_members"])
    for part in census.N20_PARTS_ON_DISK:
        path = os.path.join(E026_DATA, "census_n20_part%dof16.json" % part)
        with open(path) as fh:
            rows.extend(json.load(fh)["exactly_two_members"])
    with open(os.path.join(E026_DATA, "census_n20supp14.json")) as fh:
        rows.extend(json.load(fh)["exactly_two_members"])
    assert len(rows) == 8
    return rows


def find_ham_path(adj, a, b):
    n = len(adj)
    full = (1 << n) - 1
    dist_b = bfs_dist(adj, b, full)
    target = 1 << b
    stack = [(a, 1 << a, [a])]
    while stack:
        v, used, path = stack.pop()
        rem = n - 1 - (len(path) - 1)
        if rem == 0:
            if v == b:
                return path
            continue
        row = adj[v] & ~used
        if rem > 1:
            row &= ~target
        while row:
            low = row & -row
            w = low.bit_length() - 1
            row ^= low
            if dist_b[w] <= rem - 1:
                stack.append((w, used | low, path + [w]))
    return None


def chords_of(adj, path):
    pos = {v: i for i, v in enumerate(path)}
    assert len(pos) == len(adj)
    out = set()
    for v, i in pos.items():
        row = adj[v]
        while row:
            low = row & -row
            w = low.bit_length() - 1
            row ^= low
            j = pos[w]
            if abs(j - i) > 1:
                out.add((min(i, j), max(i, j)))
    return sorted(out)


def minimal_subcovers(M, chords, limit=400):
    """Inclusion-minimal subcovers of {0..M} inside `chords` (up to `limit`).

    Completeness: any cover must contain a chord incident to the smallest
    uncovered position, so branching on that position reaches every cover;
    non-minimal ones are filtered out afterwards.
    """
    chords = sorted(chords)
    out = []
    seen = set()

    def rec(chosen, covered):
        if len(out) >= limit:
            return
        if len(covered) == M + 1:
            key = tuple(sorted(chosen))
            if key not in seen:
                seen.add(key)
                if is_minimal_cover(M, key):
                    out.append(key)
            return
        p = min(q for q in range(M + 1) if q not in covered)
        for (i, j) in chords:
            if (i == p or j == p) and (i, j) not in chosen:
                rec(chosen + [(i, j)], covered | {i, j})
                if len(out) >= limit:
                    return

    rec([], set())
    return out


# ----------------------------------------------------------------------
# commands


def cmd_anchors(_args):
    t0 = time.time()
    checks = []

    def ck(name, cond, extra=None):
        assert cond, "ANCHOR FAILED: %s (%r)" % (name, extra)
        checks.append(name)

    # a1 -- cycle detector micro-tests
    adj = build(3, [(0, 3)])                 # C4 on the path 0-1-2-3
    ck("a1.C4", has_cycle_len(adj, 4))
    ck("a1.C4-edge", has_cycle_through_edge(adj, 0, 3, 4))
    ck("a1.no-C8", not has_cycle_through_edge(adj, 0, 3, 8))
    adj = build(7, [(0, 7)])                 # C8
    ck("a1.C8-edge", has_cycle_through_edge(adj, 0, 7, 8))
    adj = build(4, [(0, 2), (2, 4)])         # two triangles
    ck("a1.tri", has_cycle_len(adj, 3) and not has_cycle_len(adj, 4))
    adj5 = build(4, [(0, 4)])                # a bare C5
    ck("a1.C5", has_cycle_len(adj5, 5) and not has_cycle_len(adj5, 4))
    # interior-disjoint chords create NO extra cycle with the path (the
    # would-be return arc revisits both chord intervals)
    adj = build(5, [(0, 2), (3, 5)])
    ck("a1.disjoint-no-cycle",
       not has_cycle_len(adj, 8) and not has_cycle_len(adj, 4)
       and creates_forbidden(adj, 3, 5, (4, 8)) == 0)
    # crossing pair at offset 1 -> C4; at offset 3 -> C8
    adj = build(6, [(0, 5), (1, 6)])
    ck("a1.cross1-C4", creates_forbidden(adj, 1, 6, (4,)) == 4)
    adj = build(8, [(0, 5), (3, 8)])
    ck("a1.cross3-C8", creates_forbidden(adj, 3, 8, (4, 8)) == 8)
    # nested pair with (k-i)+(j-l) = 6 -> C8; shared endpoint at gap 6 -> C8
    adj = build(11, [(0, 11), (3, 8)])
    ck("a1.nested-C8", creates_forbidden(adj, 3, 8, (4, 8)) == 8)
    adj = build(9, [(0, 2), (0, 8)])
    ck("a1.shared-C8", creates_forbidden(adj, 0, 8, (4, 8)) == 8)
    adj = build(4, [(0, 2), (2, 4)])
    ck("a1.span2-offset2-ok", creates_forbidden(adj, 2, 4, (4, 8)) == 0)
    # the production fast path must agree with the generic routine AND with
    # the independent whole-graph detector, on every edge of every system the
    # enumerator can build at small M
    agree = 0
    for M in (9, 10, 11):
        for c in Search(M, forbidden=(4,), use_poison=False,
                        symmetry=False).run():
            adj = build(M, c)
            for (u, w) in c:
                a1 = creates_forbidden(adj, u, w, (4, 8, 16))
                a2 = creates_forbidden_fast(adj, u, w, (4, 8, 16))
                ck("a1.fast-agree", a1 == a2, (M, c, u, w, a1, a2))
                agree += 1
            # every cycle of P+C uses a chord (P is a tree), so whole-graph
            # detection and per-chord detection must agree exactly
            for L in (4, 5, 6, 8, 16):
                any_edge = any(creates_forbidden_fast(adj, u, w, (L,))
                               for (u, w) in c)
                ck("a1.fast-vs-hascycle",
                   bool(has_cycle_len(adj, L)) == bool(any_edge), (M, c, L))
    checks.append("a1.fast-pairs=%d" % agree)

    # a2 -- savings DP vs brute force
    cases = [
        (10, [(0, 2), (3, 6), (6, 9)]),
        (12, [(0, 5), (2, 7), (4, 9), (7, 12)]),
        (9, [(0, 4), (1, 6), (3, 8), (5, 9), (2, 5)]),
        (14, [(0, 2), (2, 4), (5, 10), (9, 14), (6, 11)]),
    ]
    for M, ch in cases:
        ck("a2.dp[%d]" % M, savings_reach(M, ch) == savings_reach_brute(M, ch),
           (M, ch))
    # a monotone reroute really is a path of the predicted length
    for M, ch in cases:
        adj = build(M, ch)
        mask = savings_reach(M, ch)
        S = set(through_set(adj, 0, M))
        for s in range(M + 1):
            if (mask >> s) & 1:
                ck("a2.real[%d,%d]" % (M, s), (M - s) in S, (M, s, sorted(S)))

    # a3 -- the enumerator against brute force on small M (symmetry off, so
    # the two enumerations must agree as SETS, not merely up to reversal)
    for M in range(6, 13):
        got = sorted(Search(M, symmetry=False).run())
        want = sorted(brute_force(M))
        ck("a3.exact[M=%d]" % M, got == want, (M, len(got), len(want)))
    # the production setting (C16-freeness added — the (F) hypothesis) must
    # also agree with the independent reference
    for M in range(6, 13):
        got = sorted(Search(M, forbidden=(4, 8, 16), symmetry=False).run())
        want = sorted(brute_force(M, forbidden=(4, 8, 16)))
        ck("a3.c16[M=%d]" % M, got == want, (M, len(got), len(want)))
    for M in range(6, 11):
        got = sorted(Search(M, forbidden=(4, 16), use_poison=False,
                            symmetry=False).run())
        want = sorted(brute_force(M, forbidden=(4, 16), use_poison=False))
        ck("a3.c16ctrl[M=%d]" % M, got == want, (M, len(got), len(want)))
    # and without the poison prune (pure structure enumeration)
    for M in range(6, 12):
        got = sorted(Search(M, use_poison=False, symmetry=False).run())
        want = sorted(brute_force(M, use_poison=False))
        ck("a3.nopoison[M=%d]" % M, got == want, (M, len(got), len(want)))
    # symmetry breaking must not lose solutions: reversal-closure of the
    # broken run is exactly the unbroken run
    def rev(c, M):
        return tuple(sorted((M - j, M - i) for i, j in c))
    for M in range(6, 13):
        a = set(Search(M, use_poison=False).run())
        b = set(Search(M, use_poison=False, symmetry=False).run())
        ck("a3.sym[M=%d]" % M,
           a <= b and (a | {rev(c, M) for c in a}) == b, (M, len(a), len(b)))

    # a4 -- the reduction on the named objects
    prof = load_profile_objects()
    ck("a4.count", len(prof) == 8)
    prof_sig = set()
    for r in prof:
        n = r["order"]
        adj = g6_decode(r["g6"])
        ck("a4.order[%s]" % r["g6"][:6], len(adj) == n)
        a, b = r["terminals"]
        deg = degrees(adj)
        ck("a4.profile", sorted(i for i in range(n) if deg[i] == 2) ==
           sorted([a, b]), (r["g6"], deg))
        S = through_set(adj, a, b)
        ck("a4.S", S == r["S"], (r["g6"], S, r["S"]))
        ck("a4.poison", 6 in S and 14 in S, (r["g6"], S))
        ck("a4.maxS", max(S) == n - 1, (r["g6"], max(S)))
        path = find_ham_path(adj, a, b)
        ck("a4.ham", path is not None and len(path) == n, r["g6"])
        ch = chords_of(adj, path)
        M = n - 1
        for i, j in ch:
            ck("a4.span", (j - i) not in (3, 7), (r["g6"], i, j))
        deg_c = chord_degrees(M, ch)
        ck("a4.cover", deg_c[0] == 1 and deg_c[M] == 1 and
           all(deg_c[p] >= 1 for p in range(1, M)), (r["g6"], deg_c))
        tm, _ = target_mask(M)
        ck("a4.first-order-poison", savings_reach(M, ch) & tm, r["g6"])
        prof_sig.add((n, len(ch), tuple(sorted(deg))))
    # every minimal subcover of a profile object is again an exactly-two
    # {C4,C8}-free member of the same order, hence (by C046's census) one of
    # the eight: check the invariant signature lands in the recorded set.
    sub_total = 0
    for r in prof:
        n = r["order"]
        adj = g6_decode(r["g6"])
        path = find_ham_path(adj, r["terminals"][0], r["terminals"][1])
        ch = chords_of(adj, path)
        M = n - 1
        subs = minimal_subcovers(M, ch, limit=60)
        ck("a4.sub-nonempty", len(subs) >= 1, r["g6"])
        for sc in subs[:20]:
            sub_total += 1
            sadj = build(M, sc)
            for L in (4, 8):
                ck("a4.sub-class", not has_cycle_len(sadj, L), (r["g6"], sc))
            sdeg = degrees(sadj)
            ck("a4.sub-profile",
               sorted(i for i in range(n) if sdeg[i] == 2) == [0, M],
               (r["g6"], sc, sdeg))
            ck("a4.sub-sig", (n, len(sc), tuple(sorted(sdeg))) in prof_sig,
               (r["g6"], sc, len(sc), sorted(sdeg)))

    # a5 -- the calibration pair
    adj10 = petersen_minus_e()
    d10 = degrees(adj10)
    a10, b10 = [v for v in range(10) if d10[v] == 2]
    ck("a5.P10-S", through_set(adj10, a10, b10) == [4, 5, 7, 8])
    ck("a5.P10-noham", find_ham_path(adj10, a10, b10) is None)
    adj14 = g6_decode(N14_G6)
    deg14 = degrees(adj14)
    t14 = [i for i in range(14) if deg14[i] == 2]
    ck("a5.N14-two", len(t14) == 2, t14)
    S14 = through_set(adj14, t14[0], t14[1])
    ck("a5.N14-S", S14 == [x for x in range(3, 14) if x != 6], S14)
    ck("a5.N14-ham", find_ham_path(adj14, t14[0], t14[1]) is not None)
    ck("a5.N14-hasC8", has_cycle_len(adj14, 8))
    # so the order-14 calibration object is excluded by C8-freeness, not by
    # the window: the search's class hypothesis is doing the work there.
    adj19 = g6_decode(N19_G6)
    ck("a5.N19-C16", has_cycle_len(adj19, 16))

    # a6 -- POSITIVE exercise of the C16 detector (R003 F2).  Every L=16
    # comparison in a1 is False==False, because a1 runs at order <= 12 where
    # no C16 can exist; the L=16 branch of _walk (depth 15) is exactly the
    # code path that produces run B's verdict.  These checks drive it to
    # True, at every path length in the window, against two other detectors.
    pos16 = neg16 = 0
    for M in range(15, 35):
        # (i) single chord of span 15: the C16 is chord + path arc
        for i in range(0, M - 15 + 1, 3):
            adj = build(M, [(i, i + 15)])
            a = creates_forbidden_fast(adj, i, i + 15, (16,))
            b = creates_forbidden(adj, i, i + 15, (16,))
            ck("a6.span15", a == 16 and b == 16 and has_cycle_len(adj, 16),
               (M, i, a, b))
            pos16 += 1
        # (ii) single chord of span 14 or 16: no C16 through it
        for sp in (14, 16):
            if sp <= M:
                adj = build(M, [(0, sp)])
                a = creates_forbidden_fast(adj, 0, sp, (16,))
                ck("a6.neg", a == 0 and not has_cycle_len(adj, 16),
                   (M, sp, a))
                neg16 += 1
        # (iii) two crossing chords whose interference cycle is a C16
        if M >= 15:
            for i in range(0, M - 15 + 1, 4):
                ch = [(i, i + 8), (i + 7, i + 15)]
                adj = build(M, ch)
                for (u, w) in ch:
                    a = creates_forbidden_fast(adj, u, w, (16,))
                    b = creates_forbidden(adj, u, w, (16,))
                    ck("a6.cross16", a == b, (M, ch, u, w, a, b))
                ck("a6.cross16-whole", has_cycle_len(adj, 16), (M, ch))
                pos16 += 1
        # (iv) a deterministic multi-chord family, three detectors, all L
        spans = (2, 5, 9, 11, 6, 13, 4, 17)
        ch = []
        for j in range(0, M):
            sp = spans[j % len(spans)]
            if j + sp <= M:
                ch.append((j, j + sp))
        adj = build(M, ch)
        for (u, w) in ch:
            for L in (4, 8, 16):
                a = creates_forbidden_fast(adj, u, w, (L,))
                b = creates_forbidden(adj, u, w, (L,))
                ck("a6.multi", a == b, (M, u, w, L, a, b))
                if L == 16:
                    pos16 += 1 if a else 0
                    neg16 += 0 if a else 1
        for L in (4, 8, 16):
            any_edge = any(creates_forbidden_fast(adj, u, w, (L,))
                           for (u, w) in ch)
            ck("a6.multi-whole",
               bool(has_cycle_len(adj, L)) == bool(any_edge), (M, L))
    # (v) the real objects: the profile members carry 46-130 C16s each
    for r in prof:
        adj = g6_decode(r["g6"])
        path = find_ham_path(adj, r["terminals"][0], r["terminals"][1])
        M = len(adj) - 1
        ch = chords_of(adj, path)
        padj = build(M, ch)
        ck("a6.real-c16", has_cycle_len(padj, 16), r["g6"])
        hit = 0
        for (u, w) in ch:
            a = creates_forbidden_fast(padj, u, w, (16,))
            b = creates_forbidden(padj, u, w, (16,))
            ck("a6.real-agree", a == b, (r["g6"], u, w, a, b))
            if a:
                hit += 1
                pos16 += 1
            else:
                neg16 += 1
        ck("a6.real-hit", hit > 0, r["g6"])
    checks.append("a6.positive16=%d" % pos16)
    checks.append("a6.negative16=%d" % neg16)

    # a7 -- NONEMPTY exercise of the two loss-capable prunes (R003 F1).
    # The a3 comparisons are all empty-vs-empty because the {C4,C8}-free
    # chord-minimal class is empty below order 19.  These run inside the
    # real class, where it is not.
    def revsys(c, M):
        return tuple(sorted((M - j, M - i) for i, j in c))
    for M in (18, 19):
        brk = set(Search(M, use_poison=False, collect_limit=10 ** 9).run())
        full = set(Search(M, use_poison=False, symmetry=False,
                          collect_limit=10 ** 9).run())
        ck("a7.nonempty[M=%d]" % M, len(brk) > 0 and len(full) > len(brk),
           (M, len(brk), len(full)))
        ck("a7.revclosure[M=%d]" % M,
           brk <= full and (brk | {revsys(c, M) for c in brk}) == full,
           (M, len(brk), len(full)))
        # the poison prune, end to end, on those nonempty sets: the DP must
        # agree with explicit family enumeration, and switching the prune on
        # must select exactly the covers whose savings miss the targets
        tm, _ = target_mask(M)
        keep = set()
        for c in full:
            dp = savings_reach(M, list(c))
            bf = savings_reach_brute(M, list(c))
            ck("a7.dp[M=%d]" % M, dp == bf, (M, c))
            if not (dp & tm):
                keep.add(c)
        got = set(Search(M, symmetry=False, collect_limit=10 ** 9).run())
        ck("a7.poison-select[M=%d]" % M, got == keep,
           (M, len(got), len(keep)))
    # the full production configuration (symmetry ON, poison ON) against the
    # independent reference, on nonempty sets
    for M in range(8, 12):
        brk = set(Search(M, forbidden=(4,), collect_limit=10 ** 9).run())
        ref = set(brute_force(M, forbidden=(4,)))
        ck("a7.prod-nonempty[M=%d]" % M, len(ref) > 0, (M, len(ref)))
        ck("a7.prod[M=%d]" % M,
           brk <= ref and (brk | {revsys(c, M) for c in brk}) == ref,
           (M, len(brk), len(ref)))

    hist = {}
    for name in checks:
        key = name.split("[")[0].split("=")[0]
        hist[key] = hist.get(key, 0) + 1
    out = {
        "experiment": "E028",
        "interpreter": interpreter(),
        "checks": len(checks),
        "histogram": hist,               # per-family counts (the full name
                                         # list is 78k entries; the histogram
                                         # is what the two interpreters are
                                         # compared on)
        "profile_signatures": sorted(list(prof_sig)),
        "subcovers_checked": sub_total,
        "c16_positive_instances": pos16,
        "c16_negative_instances": neg16,
        "seconds": round(time.time() - t0, 2),
    }
    tag = "pypy" if "PyPy" in sys.version else "cpython"
    with open(os.path.join(DATA, "anchors_search_%s.json" % tag), "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print("anchors: %d checks passed (%s), %.1f s"
          % (len(checks), out["interpreter"], out["seconds"]))
    return 0


def cmd_brute(args):
    M0, M1 = int(args[0]), int(args[1])
    for M in range(M0, M1 + 1):
        t = time.time()
        res = brute_force(M)
        print("M=%2d brute survivors=%d  (%.1f s)" % (M, len(res),
                                                      time.time() - t))
    return 0


def cmd_search(args):
    forb = CLASS_FORBIDDEN
    suffix = ""
    if args and args[-1] in ("c16", "c4c8"):
        if args[-1] == "c16":
            forb = (4, 8, 16)
            suffix = "_c16"
        args = args[:-1]
    if "," in args[0]:
        Ms = [int(x) for x in args[0].split(",")]
        tag = args[0].replace(",", "_")
        node_cap = int(args[1]) if len(args) > 1 else None
    else:
        M0, M1 = int(args[0]), int(args[1])
        Ms = list(range(M0, M1 + 1))
        tag = "%d_%d" % (M0, M1)
        node_cap = int(args[2]) if len(args) > 2 else None
    results = {}
    for M in Ms:
        n = M + 1
        tm, hits = target_mask(M)
        if M in POISON:
            print("M=%2d n=%2d  TRIVIAL: max S = %d is itself poison" % (M, n, M))
            results[M] = {"trivial": True, "survivors": 0}
            continue
        t = time.time()
        s = Search(M, forbidden=forb, node_cap=node_cap,
                   collect_limit=10 ** 9)
        surv = s.run()
        el = time.time() - t
        # exact stage: full path enumeration + power-cycle test per survivor
        t2 = time.time()
        alive, poison_hist, power_hist, gapfree = [], {}, {}, 0
        for c in surv:
            adj = build(M, c)
            S = through_set(adj, 0, M)
            spec = cycle_lengths_present(adj, POWERS)
            pois = sorted(set(S) & set(POISON))
            poison_hist[str(pois)] = poison_hist.get(str(pois), 0) + 1
            power_hist[str(spec)] = power_hist.get(str(spec), 0) + 1
            if len(S) == max(S) - min(S) + 1:
                gapfree += 1
            if not pois and not spec:
                alive.append({"chords": [list(e) for e in c], "S": S})
        el2 = time.time() - t2
        results[M] = {
            "n": n, "targets": hits, "survivors": len(surv),
            "nodes": s.nodes, "prunes": s.prunes, "capped": s.capped,
            "seconds": round(el, 2), "exact_seconds": round(el2, 2),
            "poison_hist": poison_hist, "power_hist": power_hist,
            "gapfree_survivors": gapfree,
            "genuine_dodgers": alive,
            "examples": [list(map(list, c)) for c in surv[:200]],
        }
        print("M=%2d n=%2d poison-hit-savings=%s survivors=%d nodes=%d "
              "capped=%s (%.1f s) | exact: gapfree=%d poison=%s powers=%s "
              "GENUINE=%d (%.1f s)"
              % (M, n, [M - p for p in hits], len(surv), s.nodes,
                 s.capped, el, gapfree, poison_hist, power_hist,
                 len(alive), el2))
        if alive:
            print("*** CASE-(5b) RESIDUAL OBJECT FOUND AT ORDER %d ***" % n)
        sys.stdout.flush()
        with open(os.path.join(DATA, "search_%s%s.json" % (tag, suffix)),
                  "w") as fh:
            json.dump({"interpreter": interpreter(), "forbidden": list(forb),
                       "results": {str(k): v for k, v in results.items()}},
                      fh, indent=1, sort_keys=True)
    return 0


def all_path_lengths(adj, a, b):
    """Independent reference: plain DFS over all a-b paths, lengths only."""
    n = len(adj)
    out = set()
    stack = [(a, 1 << a, 0)]
    while stack:
        v, used, d = stack.pop()
        if v == b:
            out.add(d)
            continue
        row = adj[v] & ~used
        while row:
            low = row & -row
            w = low.bit_length() - 1
            row ^= low
            stack.append((w, used | low, d + 1))
    return sorted(out)


def two_connected(adj):
    n = len(adj)
    full = (1 << n) - 1
    for v in range(n):
        rest = full & ~(1 << v)
        start = (rest & -rest).bit_length() - 1
        seen = 1 << start
        stack = [start]
        while stack:
            x = stack.pop()
            row = adj[x] & rest & ~seen
            while row:
                low = row & -row
                y = low.bit_length() - 1
                row ^= low
                seen |= low
                stack.append(y)
        if seen != rest:
            return False
    return True


def cmd_certify(args):
    """Independent re-verification of every stored survivor."""
    files = [os.path.join(DATA, f) for f in sorted(os.listdir(DATA))
             if f.startswith("search_") and f.endswith(".json")]
    if args:
        files = [os.path.join(DATA, args[0])]
    certs = []
    t0 = time.time()
    for f in files:
        with open(f) as fh:
            blob = json.load(fh)
        for Ms, rec in sorted(blob["results"].items(),
                              key=lambda kv: int(kv[0])):
            M = int(Ms)
            n = M + 1
            for c in rec.get("examples", []):
                ch = [tuple(e) for e in c]
                adj = build(M, ch)
                deg = degrees(adj)
                assert sorted(v for v in range(n) if deg[v] == 2) == [0, M], \
                    "degree profile broken at M=%d %r" % (M, c)
                assert min(deg) == 2 and all(deg[v] >= 3 for v in range(1, M))
                for L in (4, 8):
                    assert not has_cycle_len(adj, L), \
                        "class violated at M=%d %r (C%d)" % (M, c, L)
                S1 = through_set(adj, 0, M)                # E018 enumerator
                S2 = all_path_lengths(adj, 0, M)           # independent DFS
                assert S1 == S2, ("through-set disagreement", M, c, S1, S2)
                spec = cycle_lengths_present(adj, POWERS)
                certs.append({
                    "n": n, "M": M, "chords": [list(e) for e in ch],
                    "g6": census.scan.g6_encode(adj),
                    "edges": sum(bin(x).count("1") for x in adj) // 2,
                    "degrees": sorted(deg),
                    "S": S1, "minS": min(S1), "maxS": max(S1),
                    "S_is_interval": len(S1) == max(S1) - min(S1) + 1,
                    "poison_in_S": sorted(set(S1) & set(POISON)),
                    "powers_in_spec": spec,
                    "c16_count": count_cycles_len(adj, 16),
                    "two_connected": two_connected(adj),
                    "bipartite": census.bipartition(adj) is not None,
                    "girth": min(L for L in range(3, n + 1)
                                 if has_cycle_len(adj, L)),
                })
    by_order = {}
    for c in certs:
        by_order.setdefault(c["n"], []).append(c)
    for n in sorted(by_order):
        rows = by_order[n]
        iso = len(set(census.scan.canonical_set([r["g6"] for r in rows])))
        print("order %2d: %3d certified survivors, %3d up to isomorphism; "
              "all S intervals=%s; all poison-hit=%s; all C16=%s; "
              "2-connected=%d/%d"
              % (n, len(rows), iso,
                 all(r["S_is_interval"] for r in rows),
                 all(r["poison_in_S"] for r in rows),
                 all(16 in r["powers_in_spec"] for r in rows),
                 sum(1 for r in rows if r["two_connected"]), len(rows)))
    with open(os.path.join(DATA, "certificates.json"), "w") as fh:
        json.dump({"interpreter": interpreter(), "count": len(certs),
                   "seconds": round(time.time() - t0, 1),
                   "certificates": certs}, fh, indent=1)
    print("certified %d survivors in %.1f s" % (len(certs), time.time() - t0))
    return 0


def cmd_verify(args):
    path = os.path.join(DATA, args[0]) if args else None
    files = [path] if path else [
        os.path.join(DATA, f) for f in sorted(os.listdir(DATA))
        if f.startswith("search_") and f.endswith(".json")]
    total = 0
    real = []
    for f in files:
        with open(f) as fh:
            blob = json.load(fh)
        for Ms, rec in sorted(blob["results"].items(), key=lambda kv: int(kv[0])):
            M = int(Ms)
            for c in rec.get("examples", []):
                total += 1
                ch = [tuple(e) for e in c]
                adj = build(M, ch)
                S = through_set(adj, 0, M)
                spec = cycle_lengths_present(adj, POWERS)
                poisoned = sorted(set(S) & set(POISON))
                rec_out = {"M": M, "chords": c, "S": S, "powers": spec,
                           "poison_in_S": poisoned}
                if not poisoned and not spec:
                    real.append(rec_out)
                print("M=%d chords=%d |S|=%d poison=%s powers=%s"
                      % (M, len(ch), len(S), poisoned, spec))
    print("verified %d survivors; genuine dodgers: %d" % (total, len(real)))
    with open(os.path.join(DATA, "verify.json"), "w") as fh:
        json.dump({"checked": total, "genuine": real}, fh, indent=1)
    return 0


def main():
    cmds = {"anchors": cmd_anchors, "brute": cmd_brute,
            "search": cmd_search, "verify": cmd_verify,
            "certify": cmd_certify}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        return 2
    sys.setrecursionlimit(100000)
    return cmds[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    sys.exit(main())
