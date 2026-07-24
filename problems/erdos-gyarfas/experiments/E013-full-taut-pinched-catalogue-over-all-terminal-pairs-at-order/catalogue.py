"""E013: the complete taut-pinched catalogue at orders 6-14, and the
dissection of the band-6 witnesses.

Part 1 (`run`): for every graph of the E010/E011/E012 geng stream (connected,
C4-free, min degree >= 1, at most two sub-cubic vertices via the edge bound
ceil((3n-4)/2)) and EVERY admissible terminal pair (containing all sub-cubic
vertices, degree sum >= 3), decide whether the pair is *taut pinched*: every
simple a-b path has length <= 2 d(a,b) - 1 (pinched, ratio < 2) and every
vertex lies on some simple a-b path (vertex-taut).  Unlike E012 (which
certified only S subseteq {3,4,5}), there is NO band restriction: the scan
covers every band d = d(a,b) >= 1, so it is the first search that can find a
taut pinched pair with s_min in {4,5} and s_max in {6,7} -- the actual target
of the taut s_min=4 rung -- and it completes the taut-pinched catalogue that
C028 started (sub-cubic terminals, orders 12-13) over all pairs at orders
6-14.

Soundness of the per-pair filters (each a necessary condition of the target,
so rejection loses no taut pinched pairs):

  * eccentricity: a vertex on a simple a-b path of length ell <= 2d-1 has
    dist(a,v) + dist(v,b) <= ell <= 2d-1; a pair with a violating vertex
    cannot be taut pinched (it may still be pinched non-taut: the catalogue's
    non-taut tallies are therefore partial and are recorded as such).
  * long-path abort: an arrival at b with length >= 2d refutes pinched.
    Branch pruning: from a partial path a..v of length ell with
    ell + dist(v,b) >= 2d, any completion has length >= 2d, so the branch
    aborts the pair iff b is reachable from v in the graph minus the partial
    path, and is silently pruned otherwise (no completion exists at all).

Cross-record asserts: every taut hit must have band >= 4 (band 1-2 would
refute L028, band 3 would refute L030/C029); stream totals must equal the
C027 records; at orders 12-13 the taut hits at sub-cubic terminal pairs must
be exactly the five C028 witnesses.

Part 2 (`dissect`): for every band-6 witness (the five from E011 plus any new
taut hits found by `run`), an independent structural dissection: full cycle
census (spectrum recomputed and asserted against the E011 records), the C8
inventory (count, vertex/edge coverage, terminal avoidance, BFS-layer spans),
the through-path system (all simple a-b paths with edge sets, essential
edges), the interference census (which C8s are exact symmetric differences
of two through-paths, and via which length pairs), cut vertices, pairwise
isomorphism among witnesses, and single-vertex-deletion relations between the
order-13 and order-12 witnesses.

The `runclosed` mode relaxes the ratio to CLOSED (s_max <= 2 d(a,b), excess
e <= 0): by the pendant reduction (A014 T1/T2) this is exactly the core
catalogue from which every strict-pinched taut (D)-gadget arises as a
pendant lift.  The `cores` mode verifies that reduction on the recorded
witnesses (core extraction, deduplication cross-checked against nauty
labelg, Petersen-minus-e identification, lift-completeness bijection) and
records the core-level C8 interference census.

Usage:
  python3 catalogue.py anchors
  python3 catalogue.py run 6 7 8 9 10 11 12 13 14
  python3 catalogue.py runclosed 6 7 8 9 10 11 12 13 14
  python3 catalogue.py cores
  python3 catalogue.py dissect
"""

from __future__ import annotations

import argparse
import itertools
import json
import pathlib
import platform
import subprocess
import time

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"
E011_DATA = (
    HERE.parent
    / "E011-taut-gadget-verification-lobe-structure-and-the-taut-bottom"
    / "data"
)

STREAM_EXPECTED = {  # E010 recorded stream totals (C027)
    6: 4, 7: 5, 8: 36, 9: 84, 10: 918, 11: 4058,
    12: 52331, 13: 389734, 14: 5605161, 15: 61813970,
}


# --- primitives copied verbatim from E012/scan_pairs.py ---------------------
# (there copied from E011/verify_taut.py, anchored bidirectionally against
# the independent E010 pipeline)

def g6_decode(text: str) -> list[int]:
    data = [ord(c) - 63 for c in text.strip()]
    assert data and 0 <= min(data) and max(data) <= 63
    n = data[0]
    assert n < 63, "long-form graph6 not needed here"
    bits = []
    for value in data[1:]:
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    need = n * (n - 1) // 2
    assert len(bits) >= need and not any(bits[need:])
    adjacency = [0] * n
    k = 0
    for j in range(1, n):
        for i in range(j):
            if bits[k]:
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
            k += 1
    return adjacency


def degrees(adjacency: list[int]) -> list[int]:
    return [row.bit_count() for row in adjacency]


def has_c4(adjacency: list[int]) -> bool:
    n = len(adjacency)
    for u in range(n):
        for v in range(u + 1, n):
            if (adjacency[u] & adjacency[v]).bit_count() >= 2:
                return True
    return False


def from_edges(n: int, edges: list[tuple[int, int]]) -> list[int]:
    adjacency = [0] * n
    for u, v in edges:
        assert u != v and not adjacency[u] >> v & 1
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
    return adjacency


def k33_minus_e() -> tuple[list[int], int, int]:
    adjacency = [0] * 6
    for u in (0, 1, 2):
        for v in (3, 4, 5):
            if (u, v) == (0, 3):
                continue
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u
    return adjacency, 0, 3


def bfs_all(adjacency: list[int], source: int) -> list[int]:
    n = len(adjacency)
    dist = [-1] * n
    dist[source] = 0
    seen = 1 << source
    frontier = [source]
    d = 0
    while frontier:
        d += 1
        nxt = []
        for v in frontier:
            free = adjacency[v] & ~seen
            while free:
                low = free & -free
                free ^= low
                seen |= low
                w = low.bit_length() - 1
                dist[w] = d
                nxt.append(w)
        frontier = nxt
    return dist


def candidate_pairs(degs: list[int]) -> list[tuple[int, int]]:
    """Unordered terminal pairs (a,b) compatible with condition (D): every
    sub-cubic vertex must be a terminal, and deg(a)+deg(b) >= 3."""
    n = len(degs)
    sub = [v for v in range(n) if degs[v] < 3]
    if len(sub) > 2:
        return []
    if len(sub) == 2:
        s, t = sub
        return [(s, t)] if degs[s] + degs[t] >= 3 else []
    if len(sub) == 1:
        s = sub[0]
        return [(s, v) for v in range(n) if v != s]
    return [(u, v) for u in range(n) for v in range(u + 1, n)]


# --- new machinery: the banded pair scan ------------------------------------

def reachable(adjacency: list[int], start: int, target: int,
              blocked: int) -> bool:
    """Is target reachable from start in the graph minus `blocked`?
    (start itself may be listed in blocked; target must not be.)"""
    frontier = 1 << start
    seen = blocked | frontier
    target_bit = 1 << target
    while frontier:
        if frontier & target_bit:
            return True
        nxt = 0
        while frontier:
            low = frontier & -frontier
            frontier ^= low
            nxt |= adjacency[low.bit_length() - 1]
        frontier = nxt & ~seen
        seen |= frontier
    return False


def paths_banded(adjacency: list[int], a: int, b: int, dist_b: list[int],
                 limit: int):
    """All-simple-paths DFS from a to b.  Returns (lengths, essential_mask)
    when every simple a-b path has length < limit; returns None as soon as a
    path of length >= limit is proved to exist (arrival, or a partial path
    a..v with ell + dist(v,b) >= limit whose masked continuation to b
    exists)."""
    lengths: set[int] = set()
    essential = 0
    stack = [(a, 1 << a, 0)]
    while stack:
        vertex, visited, dist = stack.pop()
        if vertex == b:
            if dist >= limit:  # unreachable given the push guard; safety
                return None
            lengths.add(dist)
            essential |= visited
            continue
        free = adjacency[vertex] & ~visited
        while free:
            low = free & -free
            free ^= low
            w = low.bit_length() - 1
            if dist + 1 + dist_b[w] >= limit:
                if reachable(adjacency, w, b, visited | low):
                    return None
                continue  # prune: no completion of this branch exists
            stack.append((w, visited | low, dist + 1))
    assert lengths, "disconnected input"
    return lengths, essential


def scan_pair_banded(adjacency, dist_of, a, b, closed: bool = False):
    """Decide whether (H,a,b) is a taut pinched pair (any band).  With
    closed=True the ratio condition is relaxed from s_max <= 2d-1 (strict,
    ratio < 2) to s_max <= 2d (closed, ratio <= 2): the core catalogue.
    Returns (verdict, band, S, essential) with verdict in:
      'reject-eccentric', 'reject-long', 'nontaut', 'TAUT'."""
    da, db = dist_of[a], dist_of[b]
    d = da[b]
    n = len(adjacency)
    ceiling = 2 * d - 1 + (1 if closed else 0)
    if any(da[v] + db[v] > ceiling for v in range(n)):
        return "reject-eccentric", d, None, None
    result = paths_banded(adjacency, a, b, db, ceiling + 1)
    if result is None:
        return "reject-long", d, None, None
    lengths, essential = result
    assert min(lengths) == d, "DFS/BFS mismatch"
    assert max(lengths) <= ceiling
    if essential == (1 << n) - 1:
        return "TAUT", d, sorted(lengths), essential
    return "nontaut", d, sorted(lengths), essential


# --- new machinery: cycles, paths with edges, structure ---------------------

def all_cycles(adjacency: list[int]):
    """Every simple cycle, once: rooted at its minimum vertex, direction
    fixed by second-vertex < last-vertex.  Returns a list of
    (length, vertex_mask, edge_frozenset) with edges as sorted tuples."""
    n = len(adjacency)
    out = []
    for root in range(n):
        high = ~((1 << (root + 1)) - 1)  # vertices > root
        stack = [(root, 1 << root, (root,))]
        while stack:
            vertex, mask, path = stack.pop()
            free = adjacency[vertex]
            candidates = free & high & ~mask
            if len(path) >= 3 and free >> root & 1 and path[1] < path[-1]:
                edges = frozenset(
                    tuple(sorted((path[i], path[i + 1])))
                    for i in range(len(path) - 1)
                ) | {tuple(sorted((path[-1], root)))}
                out.append((len(path), mask, edges))
            while candidates:
                low = candidates & -candidates
                candidates ^= low
                w = low.bit_length() - 1
                stack.append((w, mask | low, path + (w,)))
    return out


def all_ab_paths(adjacency: list[int], a: int, b: int):
    """Every simple a-b path as (length, vertex_mask, edge_frozenset)."""
    out = []
    stack = [(a, 1 << a, (a,))]
    while stack:
        vertex, mask, path = stack.pop()
        if vertex == b:
            edges = frozenset(
                tuple(sorted((path[i], path[i + 1])))
                for i in range(len(path) - 1)
            )
            out.append((len(path) - 1, mask, edges))
            continue
        free = adjacency[vertex] & ~mask
        while free:
            low = free & -free
            free ^= low
            w = low.bit_length() - 1
            stack.append((w, mask | low, path + (w,)))
    return out


def edge_list(adjacency: list[int]) -> list[tuple[int, int]]:
    n = len(adjacency)
    return [(u, v) for u in range(n) for v in range(u + 1, n)
            if adjacency[u] >> v & 1]


def cut_vertices(adjacency: list[int]) -> list[int]:
    n = len(adjacency)
    full = (1 << n) - 1
    out = []
    for v in range(n):
        rest = [w for w in range(n) if w != v]
        start = rest[0]
        if not all(
            w == start or reachable(adjacency, start, w, 1 << v)
            for w in rest
        ):
            out.append(v)
    assert full == (1 << n) - 1
    return out


def refine_profiles(adjacency: list[int]) -> list[tuple]:
    """Per-vertex invariant: (degree, sorted neighbor degrees, sorted
    distance multiset).  Used only to prune the isomorphism search."""
    n = len(adjacency)
    degs = degrees(adjacency)
    dist_of = [bfs_all(adjacency, v) for v in range(n)]
    out = []
    for v in range(n):
        nbrs = sorted(degs[w] for w in range(n) if adjacency[v] >> w & 1)
        out.append((degs[v], tuple(nbrs), tuple(sorted(dist_of[v]))))
    return out


def isomorphic(adj1: list[int], adj2: list[int],
               fixed: tuple | None = None) -> bool:
    """Exact isomorphism test by backtracking on profile classes.  When
    `fixed` = ((a1,b1),(a2,b2)), only mappings with a1 -> a2 AND b1 -> b2
    are allowed (ORDERED: callers wanting either terminal orientation must
    try both)."""
    n = len(adj1)
    if len(adj2) != n:
        return False
    p1, p2 = refine_profiles(adj1), refine_profiles(adj2)
    if sorted(p1) != sorted(p2):
        return False
    forced = {}
    if fixed is not None:
        (a1, b1), (a2, b2) = fixed
        forced = {a1: a2, b1: b2}
        if len({a1, b1}) != 2 or len({a2, b2}) != 2:
            raise ValueError("fixed terminals must be distinct")

    def extend(mapping: dict[int, int], used: int) -> bool:
        if len(mapping) == n:
            return True
        v = min((w for w in range(n) if w not in mapping),
                key=lambda w: sum(1 for u in range(n)
                                  if p1[u] == p1[w] and u not in mapping))
        for image in range(n):
            if used >> image & 1 or p1[v] != p2[image]:
                continue
            if v in forced and forced[v] != image:
                continue
            if v not in forced and image in forced.values():
                continue
            if any((adj1[v] >> u & 1) != (adj2[image] >> mapping[u] & 1)
                   for u in mapping):
                continue
            mapping[v] = image
            if extend(mapping, used | 1 << image):
                return True
            del mapping[v]
        return False

    return extend({}, 0)


def isomorphic_two_terminal(adj1, t1, adj2, t2) -> bool:
    """Isomorphism of two-terminal graphs: terminals map onto terminals in
    either orientation."""
    (a1, b1), (a2, b2) = tuple(t1), tuple(t2)
    return (isomorphic(adj1, adj2, fixed=((a1, b1), (a2, b2)))
            or isomorphic(adj1, adj2, fixed=((a1, b1), (b2, a2))))


def delete_vertex(adjacency: list[int], v: int) -> list[int]:
    n = len(adjacency)
    keep = [w for w in range(n) if w != v]
    index = {w: i for i, w in enumerate(keep)}
    out = [0] * (n - 1)
    for w in keep:
        row = adjacency[w] & ~(1 << v)
        while row:
            low = row & -row
            row ^= low
            u = low.bit_length() - 1
            out[index[w]] |= 1 << index[u]
    return out


# --- anchors ----------------------------------------------------------------

def petersen() -> list[int]:
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
    edges += [(i, i + 5) for i in range(5)]
    edges += [(5, 7), (7, 9), (9, 6), (6, 8), (8, 5)]
    return from_edges(10, edges)


def anchors() -> None:
    checks = 0

    def ok(condition: bool, message: str) -> None:
        nonlocal checks
        assert condition, message
        checks += 1

    # A1: K_{3,3}-e is caught by the banded scan as taut pinched band 3
    # with S={3,5} (positive control), and contains a C4 (stream-absent).
    adj, a, b = k33_minus_e()
    dist_of = [bfs_all(adj, v) for v in range(6)]
    verdict, band, S, _ = scan_pair_banded(adj, dist_of, a, b)
    ok(verdict == "TAUT" and band == 3 and S == [3, 5],
       "A1: K33-e not reported taut band-3 {3,5}")
    ok(has_c4(adj), "A1: K33-e should contain a C4")

    # A2: the five E011 witnesses are caught by the banded scan as taut
    # band-6 with exactly the recorded S; recomputed spectrum matches the
    # E011 record; d(a,b)=6.
    witnesses = load_e011_witnesses()
    ok(len(witnesses) == 5, "A2: expected five E011 witnesses")
    for entry in witnesses:
        adj = g6_decode(entry["graph6"])
        n = len(adj)
        ta, tb = entry["terminals"]
        dist_of = [bfs_all(adj, v) for v in range(n)]
        ok(dist_of[ta][tb] == 6, "A2: witness distance != 6")
        verdict, band, S, _ = scan_pair_banded(adj, dist_of, ta, tb)
        ok(verdict == "TAUT" and band == 6 and S == entry["S"],
           f"A2: {entry['graph6']} not caught taut band-6 with recorded S")
        spectrum = sorted({length for length, _, _ in all_cycles(adj)})
        ok(spectrum == entry["spectrum"],
           f"A2: {entry['graph6']} spectrum mismatch {spectrum}")

    # A3: cycle census machinery on known graphs: K4 (4 triangles, 3
    # squares), C6 (one hexagon), Petersen (spectrum {5,6,8,9}, twelve
    # pentagons, ten hexagons).
    k4 = from_edges(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    census = all_cycles(k4)
    by_len = {}
    for length, _, _ in census:
        by_len[length] = by_len.get(length, 0) + 1
    ok(by_len == {3: 4, 4: 3}, f"A3: K4 census wrong: {by_len}")
    c6 = from_edges(6, [(i, (i + 1) % 6) for i in range(6)])
    census = all_cycles(c6)
    ok(len(census) == 1 and census[0][0] == 6, "A3: C6 census wrong")
    pet = petersen()
    census = all_cycles(pet)
    by_len = {}
    for length, _, _ in census:
        by_len[length] = by_len.get(length, 0) + 1
    ok(sorted(by_len) == [5, 6, 8, 9], f"A3: Petersen spectrum {by_len}")
    ok(by_len[5] == 12 and by_len[6] == 10,
       f"A3: Petersen 5/6-cycle counts wrong: {by_len}")

    # A4: path/sym-diff machinery: C6 antipodal terminals have exactly two
    # paths, lengths 3 and 3, whose symmetric difference is the hexagon.
    paths = all_ab_paths(c6, 0, 3)
    ok(sorted(length for length, _, _ in paths) == [3, 3],
       "A4: C6 antipodal paths wrong")
    sym = paths[0][2] ^ paths[1][2]
    ok(sym == all_cycles(c6)[0][2], "A4: sym-diff is not the hexagon")

    # A5: cut-vertex machinery: P4 has two, K4 none, C6 none.
    p4 = from_edges(4, [(0, 1), (1, 2), (2, 3)])
    ok(cut_vertices(p4) == [1, 2], "A5: P4 cut vertices wrong")
    ok(cut_vertices(k4) == [], "A5: K4 cut vertices wrong")
    ok(cut_vertices(c6) == [], "A5: C6 cut vertices wrong")

    # A6: isomorphism machinery: relabelled Petersen is isomorphic to
    # Petersen; K4 is not isomorphic to K_{1,3}+edge counts differ; the
    # terminal-respecting variant distinguishes terminal orbits on P4.
    perm = [3, 1, 4, 0, 2, 8, 6, 9, 5, 7]
    relabelled = [0] * 10
    for u in range(10):
        row = pet[u]
        while row:
            low = row & -row
            row ^= low
            w = low.bit_length() - 1
            relabelled[perm[u]] |= 1 << perm[w]
    ok(isomorphic(pet, relabelled), "A6: Petersen self-iso failed")
    star = from_edges(4, [(0, 1), (0, 2), (0, 3)])
    ok(not isomorphic(k4, star), "A6: K4 iso K13?")
    ok(isomorphic(p4, p4, fixed=((0, 3), (0, 3))),
       "A6: P4 end-terminal iso failed")
    ok(not isomorphic(p4, p4, fixed=((0, 3), (1, 2))),
       "A6: P4 should not map ends onto middles")
    ok(isomorphic(p4, p4, fixed=((0, 1), (3, 2))),
       "A6: P4 reversal orientation should exist")
    ok(not isomorphic(p4, p4, fixed=((0, 1), (0, 2))),
       "A6: P4 has no automorphism fixing 0 and moving 1 to 2")
    triangle_pendant = from_edges(4, [(0, 1), (1, 2), (2, 0), (0, 3)])
    ok(not isomorphic(triangle_pendant, triangle_pendant,
                      fixed=((3, 1), (1, 3))),
       "A6: pendant-triangle cannot swap degree-1 with degree-2")
    ok(isomorphic_two_terminal(p4, (0, 3), p4, (3, 0)),
       "A6: two-terminal wrapper must accept either orientation")

    # A7: banded scan negative controls: Petersen (min degree 3) has no
    # taut pinched pair at any band; C6 antipodal pair is taut band-3.
    dist_of = [bfs_all(pet, v) for v in range(10)]
    for u in range(10):
        for v in range(u + 1, 10):
            verdict, _, _, _ = scan_pair_banded(pet, dist_of, u, v)
            ok(verdict != "TAUT", f"A7: Petersen pair {(u, v)} taut?")
    dist_of = [bfs_all(c6, v) for v in range(6)]
    verdict, band, S, _ = scan_pair_banded(c6, dist_of, 0, 3)
    ok(verdict == "TAUT" and band == 3 and S == [3],
       "A7: C6 antipodal should be taut band-3 S={3}")

    # A8: vertex deletion machinery.
    ok(isomorphic(delete_vertex(k4, 0),
                  from_edges(3, [(0, 1), (0, 2), (1, 2)])),
       "A8: K4 minus vertex is K3")

    # A9: the bridge composite (A014 T5): two copies of Petersen-minus-e
    # joined terminal-to-terminal by a bridge form a vertex-taut STRICT core
    # of order 20: band 9, S = {9,...,17} (Minkowski sum {4,5,7,8}+1+
    # {4,5,7,8}), spectrum still {5,6,8,9}, cut vertices exactly the bridge
    # ends.  This is the machine check that naive core-level spread-doubling
    # is false and blocks are the right level.
    pm = [row for row in pet]
    pm[0] &= ~(1 << 1)
    pm[1] &= ~1
    x1, y1 = 0, 1
    comp = [row for row in pm] + [0] * 10
    for u in range(10):
        row = pm[u]
        while row:
            low = row & -row
            row ^= low
            comp[10 + u] |= 1 << (10 + (low.bit_length() - 1))
    comp[y1] |= 1 << (10 + x1)
    comp[10 + x1] |= 1 << y1
    X, Y = x1, 10 + y1
    cdegs = degrees(comp)
    ok(cdegs[X] == 2 and cdegs[Y] == 2 and min(
        cdegs[v] for v in range(20) if v not in (X, Y)) == 3,
       "A9: composite degree profile wrong")
    ok(not has_c4(comp), "A9: composite has a C4")
    dist_of = [bfs_all(comp, v) for v in range(20)]
    verdict, band, S, _ = scan_pair_banded(comp, dist_of, X, Y, closed=True)
    ok(verdict == "TAUT" and band == 9 and S == list(range(9, 18)),
       f"A9: composite scan wrong: {verdict} {band} {S}")
    ok(max(S) == 2 * band - 1, "A9: composite should be strictly pinched")
    ok(sorted({length for length, _, _ in all_cycles(comp)}) == [5, 6, 8, 9],
       "A9: composite spectrum changed")
    ok(cut_vertices(comp) == sorted((y1, 10 + x1)),
       "A9: composite cut vertices are not the bridge ends")

    print(f"anchors: all {checks} checks passed")


# --- part 1: the catalogue scan ---------------------------------------------

def load_e011_witnesses() -> list[dict]:
    out = []
    for n in (12, 13):
        payload = json.loads((E011_DATA / f"taut_n{n}.json").read_text())
        out.extend(payload["taut_pinched"])
    return out


def run(orders: list[int], closed: bool = False) -> None:
    DATA.mkdir(exist_ok=True)
    e011_by_order: dict[int, set] = {12: set(), 13: set()}
    for entry in load_e011_witnesses():
        n = g6_decode(entry["graph6"])
        e011_by_order[len(n)].add(
            (entry["graph6"], tuple(sorted(entry["terminals"])))
        )
    for n in orders:
        started = time.time()
        mine = -(-(3 * n - 4) // 2)
        command = ["geng", "-q", "-c", "-f", "-d1", str(n), f"{mine}:0"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
        stream = 0
        eligible = 0
        counts = {"pairs": 0, "reject-eccentric": 0, "reject-long": 0,
                  "nontaut": 0, "TAUT": 0}
        by_band: dict[int, dict[str, int]] = {}
        taut_hits: list[dict] = []
        for line in process.stdout:
            line = line.strip()
            if not line:
                continue
            stream += 1
            adjacency = g6_decode(line)
            degs = degrees(adjacency)
            pairs = candidate_pairs(degs)
            if not pairs:
                continue
            assert not has_c4(adjacency), "geng -f emitted a C4 graph"
            eligible += 1
            dist_of = [bfs_all(adjacency, v) for v in range(n)]
            for a, b in pairs:
                counts["pairs"] += 1
                verdict, band, S, essential = scan_pair_banded(
                    adjacency, dist_of, a, b, closed=closed)
                counts[verdict] += 1
                slot = by_band.setdefault(band, {"nontaut": 0, "TAUT": 0})
                if verdict == "nontaut":
                    slot["nontaut"] += 1
                elif verdict == "TAUT":
                    slot["TAUT"] += 1
                    boundary = max(S) == 2 * band
                    assert band >= 4 or boundary, (
                        f"L028/L030 REFUTED at band {band}: {line} {(a, b)}"
                    )
                    spectrum = sorted(
                        {length for length, _, _ in all_cycles(adjacency)}
                    )
                    taut_hits.append({
                        "graph6": line, "terminals": [a, b], "band": band,
                        "S": S, "ratio": max(S) / min(S),
                        "boundary": boundary,
                        "spectrum": spectrum,
                        "has_c8": 8 in spectrum,
                        "subcubic_terminals":
                            degs[a] < 3 and degs[b] < 3,
                    })
        assert process.wait() == 0
        expected = STREAM_EXPECTED.get(n)
        if expected is not None:
            assert stream == expected, (n, stream, expected)
        if not closed and n in e011_by_order:
            found = {(h["graph6"], tuple(sorted(h["terminals"])))
                     for h in taut_hits if h["subcubic_terminals"]}
            assert found == e011_by_order[n], (
                f"C028 cross-check failed at n={n}: {found}"
            )
        if closed:
            strict_file = DATA / f"catalogue_n{n}.json"
            if strict_file.exists():
                strict = json.loads(strict_file.read_text())
                want = {(h["graph6"], tuple(sorted(h["terminals"])),
                         tuple(h["S"])) for h in strict["taut_hits"]}
                got = {(h["graph6"], tuple(sorted(h["terminals"])),
                        tuple(h["S"]))
                       for h in taut_hits if not h["boundary"]}
                assert got == want, f"strict/closed mismatch at n={n}"
        summary = {
            "n": n,
            "mode": "closed" if closed else "strict",
            "geng_command": " ".join(command),
            "stream_total": stream,
            "stream_matches_c027": expected is not None,
            "eligible_graphs_le2_subcubic": eligible,
            "pair_counts": counts,
            "by_band": {str(band): slot
                        for band, slot in sorted(by_band.items())},
            "taut_hits": taut_hits,
            "seconds": round(time.time() - started, 1),
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
        }
        stem = "catalogue_closed" if closed else "catalogue"
        (DATA / f"{stem}_n{n}.json").write_text(json.dumps(summary, indent=2))
        bands = " ".join(
            f"b{band}:{slot['TAUT']}" for band, slot in sorted(by_band.items())
            if slot["TAUT"]
        ) or "none"
        print(
            f"n={n}{' closed' if closed else ''}: stream={stream} "
            f"eligible={eligible} pairs={counts['pairs']} "
            f"[ecc {counts['reject-eccentric']} / long "
            f"{counts['reject-long']} / nontaut {counts['nontaut']} / "
            f"TAUT {counts['TAUT']}] taut-by-band: {bands} "
            f"({summary['seconds']}s)"
        )


# --- part 2: the band-6 dissection ------------------------------------------

def gather_witnesses() -> list[dict]:
    """The five E011 witnesses plus every taut hit recorded by `run`."""
    seen = set()
    out = []
    for entry in load_e011_witnesses():
        key = (entry["graph6"], tuple(sorted(entry["terminals"])))
        seen.add(key)
        out.append({"graph6": entry["graph6"],
                    "terminals": tuple(entry["terminals"]),
                    "source": "E011",
                    "recorded_S": entry["S"],
                    "recorded_spectrum": entry["spectrum"]})
    for path in sorted(DATA.glob("catalogue_n*.json")):
        payload = json.loads(path.read_text())
        for hit in payload["taut_hits"]:
            key = (hit["graph6"], tuple(sorted(hit["terminals"])))
            if key in seen:
                continue
            seen.add(key)
            out.append({"graph6": hit["graph6"],
                        "terminals": tuple(hit["terminals"]),
                        "source": f"E013 n={payload['n']}",
                        "recorded_S": hit["S"],
                        "recorded_spectrum": hit["spectrum"]})
    return out


def dissect() -> None:
    DATA.mkdir(exist_ok=True)
    witnesses = gather_witnesses()
    reports = []
    for entry in witnesses:
        adj = g6_decode(entry["graph6"])
        n = len(adj)
        a, b = entry["terminals"]
        degs = degrees(adj)
        assert not has_c4(adj)
        subcubic = [v for v in range(n) if degs[v] < 3]
        assert set(subcubic) <= {a, b}, "non-terminal sub-cubic vertex"
        assert degs[a] + degs[b] >= 3
        dist_a, dist_b = bfs_all(adj, a), bfs_all(adj, b)
        d = dist_a[b]

        paths = all_ab_paths(adj, a, b)
        S = sorted({length for length, _, _ in paths})
        assert S == entry["recorded_S"], "through-set mismatch with record"
        full = (1 << n) - 1
        essential_vertices = 0
        essential_edges: set = set()
        for _, mask, edges in paths:
            essential_vertices |= mask
            essential_edges |= edges
        assert essential_vertices == full, "witness not vertex-taut?"
        all_edges = set(edge_list(adj))
        inessential_edges = sorted(all_edges - essential_edges)

        census = all_cycles(adj)
        spectrum = sorted({length for length, _, _ in census})
        assert spectrum == entry["recorded_spectrum"], "spectrum mismatch"
        by_len: dict[int, list] = {}
        for length, mask, edges in census:
            by_len.setdefault(length, []).append((mask, edges))
        c8s = by_len.get(8, [])

        # C8 inventory: terminal avoidance, layer spans, coverage.
        c8_reports = []
        edge_cover: dict[tuple, int] = {}
        for mask, edges in c8s:
            uses_a = bool(mask >> a & 1)
            uses_b = bool(mask >> b & 1)
            layers_a = sorted(dist_a[v] for v in range(n) if mask >> v & 1)
            for e in edges:
                edge_cover[e] = edge_cover.get(e, 0) + 1
            c8_reports.append({
                "vertices": [v for v in range(n) if mask >> v & 1],
                "uses_terminal_a": uses_a, "uses_terminal_b": uses_b,
                "dist_a_multiset": layers_a,
                "span_a": [layers_a[0], layers_a[-1]],
                "edges_all_essential":
                    all(e in essential_edges for e in edges),
            })
        vertices_on_all_c8 = [
            v for v in range(n)
            if all(mask >> v & 1 for mask, _ in c8s)
        ] if c8s else []
        edges_on_all_c8 = sorted(
            e for e, count in edge_cover.items() if count == len(c8s)
        ) if c8s else []

        # Interference census: which C8s are exact two-path sym-diffs.
        pair_hits: dict[int, list] = {i: [] for i in range(len(c8s))}
        combos: dict[str, int] = {}
        for (l1, m1, e1), (l2, m2, e2) in itertools.combinations(paths, 2):
            sym = e1 ^ e2
            for i, (mask, edges) in enumerate(c8s):
                if sym == edges:
                    shared = len(e1 & e2)
                    key = f"{min(l1, l2)}+{max(l1, l2)}-2*{shared}"
                    combos[key] = combos.get(key, 0) + 1
                    pair_hits[i].append((min(l1, l2), max(l1, l2), shared))
        c8_from_paths = sum(1 for i in pair_hits if pair_hits[i])

        cuts = cut_vertices(adj)
        layer_sizes = [sum(1 for v in range(n) if dist_a[v] == i)
                       for i in range(max(dist_a) + 1)]

        reports.append({
            "graph6": entry["graph6"], "source": entry["source"],
            "n": n, "terminals": [a, b],
            "terminal_degrees": [degs[a], degs[b]],
            "degree_sequence": sorted(degs),
            "edge_count": len(all_edges),
            "band": d, "S": S,
            "spectrum": spectrum,
            "cycle_counts": {str(k): len(v)
                             for k, v in sorted(by_len.items())},
            "path_count_by_length": {
                str(k): sum(1 for length, _, _ in paths if length == k)
                for k in S
            },
            "layer_sizes_from_a": layer_sizes,
            "cut_vertices": cuts,
            "two_connected": not cuts,
            "inessential_edges": [list(e) for e in inessential_edges],
            "c8_count": len(c8s),
            "c8_reports": c8_reports,
            "c8_vertices_common_to_all": vertices_on_all_c8,
            "c8_edges_common_to_all": [list(e) for e in edges_on_all_c8],
            "c8_realized_as_path_symdiff": c8_from_paths,
            "c8_symdiff_length_combos": combos,
        })

    # Pairwise relations among the witness graphs.
    adjacencies = [g6_decode(r["graph6"]) for r in reports]
    iso_pairs = []
    for i, j in itertools.combinations(range(len(reports)), 2):
        if len(adjacencies[i]) != len(adjacencies[j]):
            continue
        plain = isomorphic(adjacencies[i], adjacencies[j])
        if plain:
            iso_pairs.append({
                "pair": [i, j], "graph_isomorphic": True,
                "terminal_respecting": isomorphic_two_terminal(
                    adjacencies[i], reports[i]["terminals"],
                    adjacencies[j], reports[j]["terminals"]),
            })
    deletion_relations = []
    for i, j in itertools.permutations(range(len(reports)), 2):
        if len(adjacencies[i]) != len(adjacencies[j]) + 1:
            continue
        for v in range(len(adjacencies[i])):
            smaller = delete_vertex(adjacencies[i], v)
            if isomorphic(smaller, adjacencies[j]):
                deletion_relations.append(
                    {"larger": i, "deleted_vertex": v, "smaller": j})

    payload = {
        "witness_count": len(reports),
        "witnesses": reports,
        "isomorphic_pairs": iso_pairs,
        "single_deletion_relations": deletion_relations,
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
    }
    (DATA / "dissect.json").write_text(json.dumps(payload, indent=2))

    for i, r in enumerate(reports):
        print(f"[{i}] {r['graph6']} n={r['n']} terminals={r['terminals']} "
              f"deg(a),deg(b)={r['terminal_degrees']} "
              f"band={r['band']} S={r['S']}")
        print(f"    degseq={r['degree_sequence']} m={r['edge_count']} "
              f"layers(a)={r['layer_sizes_from_a']} "
              f"cuts={r['cut_vertices']}")
        print(f"    cycles={r['cycle_counts']} "
              f"paths={r['path_count_by_length']} "
              f"inessential-edges={r['inessential_edges']}")
        avoid = sum(1 for c in r["c8_reports"]
                    if not c["uses_terminal_a"] and not c["uses_terminal_b"])
        print(f"    C8s={r['c8_count']} (terminal-free: {avoid}) "
              f"as-path-symdiff: {r['c8_realized_as_path_symdiff']} "
              f"combos={r['c8_symdiff_length_combos']}")
        print(f"    C8 common vertices={r['c8_vertices_common_to_all']} "
              f"common edges={r['c8_edges_common_to_all']}")
        for c in r["c8_reports"]:
            print(f"      C8 {c['vertices']} dist_a={c['dist_a_multiset']} "
                  f"span={c['span_a']} "
                  f"a={c['uses_terminal_a']} b={c['uses_terminal_b']} "
                  f"essential={c['edges_all_essential']}")
    print("isomorphic pairs:", payload["isomorphic_pairs"])
    print("single-deletion relations:", payload["single_deletion_relations"])


def add_pendant(adjacency: list[int], attach: int) -> list[int]:
    """Return the graph with one new vertex (index n) joined to `attach`."""
    n = len(adjacency)
    out = [row for row in adjacency] + [1 << attach]
    out[attach] |= 1 << n
    return out


def cores() -> None:
    DATA.mkdir(exist_ok=True)
    witnesses = gather_witnesses()
    assert len(witnesses) == 6, f"expected six witnesses, saw {len(witnesses)}"
    core_entries = []
    for entry in witnesses:
        adj = g6_decode(entry["graph6"])
        n = len(adj)
        a, b = entry["terminals"]
        degs = degrees(adj)
        pendant = a if degs[a] == 1 else b
        other = b if pendant == a else a
        assert degs[pendant] == 1, "no degree-1 terminal"
        attach = adj[pendant].bit_length() - 1
        assert cut_vertices(adj) == [attach], "attachment is not the sole cut"
        core = delete_vertex(adj, pendant)
        shift = (lambda v: v - 1 if v > pendant else v)
        x, y = shift(attach), shift(other)
        cdegs = degrees(core)
        assert cut_vertices(core) == [], "core not 2-connected"
        assert sorted((cdegs[x], cdegs[y])) == [2, 2], "core terminal degrees"
        assert sum(1 for d in cdegs if d < 3) == 2, "extra sub-cubic in core"
        paths = all_ab_paths(core, x, y)
        S_core = sorted({length for length, _, _ in paths})
        assert S_core == [s - 1 for s in entry["recorded_S"]], "S shift failed"
        essential = 0
        for _, mask, _ in paths:
            essential |= mask
        assert essential == (1 << (n - 1)) - 1, "core not taut"
        spectrum = sorted({length for length, _, _ in all_cycles(core)})
        assert spectrum == entry["recorded_spectrum"], "core spectrum changed"
        core_entries.append({
            "witness_graph6": entry["graph6"], "source": entry["source"],
            "core": core, "terminals": (x, y), "S": S_core,
            "spectrum": spectrum,
        })

    # Deduplicate cores up to terminal-respecting isomorphism.
    distinct: list[dict] = []
    for item in core_entries:
        for known in distinct:
            if len(known["core"]) == len(item["core"]) and (
                isomorphic_two_terminal(
                    known["core"], known["terminals"],
                    item["core"], item["terminals"])
            ):
                known["witnesses"].append(item["witness_graph6"])
                break
        else:
            item = dict(item)
            item["witnesses"] = [item.pop("witness_graph6")]
            distinct.append(item)

    # Identification: Petersen minus an edge (edge-transitive, so any edge).
    pet = petersen()
    pet_minus = [row & ~2 if i == 0 else row & ~1 if i == 1 else row
                 for i, row in enumerate(pet)]
    pet_minus[0] &= ~(1 << 1)
    pet_minus[1] &= ~(1 << 0)
    petersen_matches = []
    for i, item in enumerate(distinct):
        if len(item["core"]) == 10 and isomorphic(item["core"], pet_minus):
            petersen_matches.append(i)

    # Terminal-swap automorphism and lift completeness.
    witness_adj = [(g6_decode(w["graph6"]), tuple(w["terminals"]))
                   for w in witnesses]
    lift_report = []
    matched_witnesses = set()
    for i, item in enumerate(distinct):
        core, (x, y) = item["core"], item["terminals"]
        swap = isomorphic(core, core, fixed=((x, y), (y, x)))
        lifts = []
        for attach, far in ((x, y), (y, x)):
            lifted = add_pendant(core, attach)
            m = len(lifted)
            dist_of = [bfs_all(lifted, v) for v in range(m)]
            verdict, band, S, _ = scan_pair_banded(
                lifted, dist_of, m - 1, far)
            assert verdict == "TAUT", "pendant lift is not taut pinched"
            assert S == [s + 1 for s in item["S"]], "lift S shift failed"
            hits = [
                j for j, (wadj, wt) in enumerate(witness_adj)
                if len(wadj) == m and isomorphic_two_terminal(
                    lifted, (m - 1, far), wadj, wt)
            ]
            assert hits, "lift matches no recorded witness"
            matched_witnesses.update(hits)
            lifts.append({"attach_terminal": "x" if attach == x else "y",
                          "band": band, "matches_witnesses": hits})
        lift_report.append({
            "core_index": i, "order": len(core), "S": item["S"],
            "spectrum": item["spectrum"],
            "terminal_swap_automorphism": swap,
            "lifts": lifts,
            "witness_count": len(item["witnesses"]),
        })
        if swap:
            assert len(item["witnesses"]) == 1, "symmetric core, two witnesses?"
        else:
            assert len(item["witnesses"]) == 2, "asymmetric core, one witness?"
    assert matched_witnesses == set(range(6)), "some witness not a lift"

    # Single-deletion relations among distinct cores.
    relations = []
    for i, j in itertools.permutations(range(len(distinct)), 2):
        if len(distinct[i]["core"]) != len(distinct[j]["core"]) + 1:
            continue
        for v in range(len(distinct[i]["core"])):
            if isomorphic(delete_vertex(distinct[i]["core"], v),
                          distinct[j]["core"]):
                relations.append({"larger": i, "deleted": v, "smaller": j})

    # Core-level C8 interference census.
    census_report = []
    for i, item in enumerate(distinct):
        core, (x, y) = item["core"], item["terminals"]
        paths = all_ab_paths(core, x, y)
        c8s = [(mask, edges) for length, mask, edges in all_cycles(core)
               if length == 8]
        combos: dict[str, int] = {}
        realized = 0
        for k, (mask, edges) in enumerate(c8s):
            found = False
            for (l1, m1, e1), (l2, m2, e2) in itertools.combinations(paths, 2):
                if e1 ^ e2 == edges:
                    found = True
                    shared = len(e1 & e2)
                    key = f"{min(l1, l2)}+{max(l1, l2)}-2*{shared}"
                    combos[key] = combos.get(key, 0) + 1
            realized += found
        smin = item["S"][0]
        short = [(m, e) for length, m, e in
                 ((length, mask, edges) for length, mask, edges in paths
                  if length == smin)]
        disjoint_short = sum(
            1 for (m1, _), (m2, _) in itertools.combinations(short, 2)
            if m1 & m2 == (1 << x) | (1 << y)
        )
        census_report.append({
            "core_index": i, "c8_count": len(c8s),
            "c8_as_path_symdiff": realized,
            "symdiff_combos": combos,
            "shortest_path_count": len(short),
            "disjoint_shortest_pairs": disjoint_short,
        })

    payload = {
        "distinct_core_count": len(distinct),
        "cores": [{
            "index": i, "order": len(item["core"]),
            "terminals": list(item["terminals"]),
            "S": item["S"], "spectrum": item["spectrum"],
            "witnesses": item["witnesses"],
            "adjacency_rows": item["core"],
        } for i, item in enumerate(distinct)],
        "petersen_minus_e_core_indices": petersen_matches,
        "lift_report": lift_report,
        "single_deletion_relations": relations,
        "c8_census": census_report,
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
    }
    (DATA / "cores.json").write_text(json.dumps(payload, indent=2))

    print(f"distinct cores: {len(distinct)}")
    for i, item in enumerate(distinct):
        print(f"[core {i}] order={len(item['core'])} S={item['S']} "
              f"spectrum={item['spectrum']} "
              f"witnesses={item['witnesses']}")
    print("Petersen-minus-e matches:", petersen_matches)
    for entry in lift_report:
        print(f"  core {entry['core_index']}: swap-aut="
              f"{entry['terminal_swap_automorphism']} "
              f"lifts={entry['lifts']}")
    print("single-deletion relations among cores:", relations)
    for entry in census_report:
        print(f"  core {entry['core_index']}: C8s={entry['c8_count']} "
              f"as-symdiff={entry['c8_as_path_symdiff']} "
              f"combos={entry['symdiff_combos']}")
        print(f"    shortest paths={entry['shortest_path_count']} "
              f"disjoint pairs={entry['disjoint_shortest_pairs']}")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("anchors")
    runp = sub.add_parser("run")
    runp.add_argument("orders", nargs="+", type=int)
    closedp = sub.add_parser("runclosed")
    closedp.add_argument("orders", nargs="+", type=int)
    sub.add_parser("dissect")
    sub.add_parser("cores")
    args = parser.parse_args()
    if args.command == "anchors":
        anchors()
    elif args.command == "run":
        run(args.orders)
    elif args.command == "runclosed":
        run(args.orders, closed=True)
    elif args.command == "cores":
        cores()
    else:
        dissect()


if __name__ == "__main__":
    main()
