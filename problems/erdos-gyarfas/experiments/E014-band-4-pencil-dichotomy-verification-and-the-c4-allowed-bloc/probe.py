"""A015 probe, two parts.

Part A: exhaustive machine check of the band-4 pencil dichotomy on every
connected C4-free graph at orders 5..N and every unordered pair at
distance 4:
  - two internally disjoint 4-paths  <=>  a C8 through both terminals;
  - otherwise all 4-paths share exactly one common internal vertex c
    (when there are >= 2 paths), and c is adjacent to a terminal;
  - the (2,2)-vertices are exactly the middles of 4-paths;
  - a unique 4-path has a unique (2,2)-vertex;
  - fan facts at a pencil c ~ x with t >= 2 strands: middles distinct,
    exits distinct, no cross chords m_i ~ b_j (i != j).
Also one fixed anchor: the triangle configuration (pairwise-intersecting
4-paths, no common vertex) is realizable WITH a C4, so C4-freeness is
essential to the dichotomy.

Part B: block probe WITHOUT the C4-free hypothesis: stream all connected
min-degree-2 graphs with >= ceil((3n-2)/2) edges (so <= 2 sub-cubic
vertices), keep 2-connected ones, scan every admissible terminal pair
(terminals = all degree-2 vertices, both terminal degrees >= 2) with the
E013 closed-band scanner.  Records every vertex-taut hit with
s_max <= 2 d(a,b): band, S, strictness, C4/C8 content.
"""

import json
import platform
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
E013 = HERE.parent / (
    "E013-full-taut-pinched-catalogue-over-all-terminal-pairs-at-order"
)
sys.path.insert(0, str(E013))
from catalogue import (g6_decode, degrees, has_c4, bfs_all, cut_vertices,
                       scan_pair_banded, all_cycles)


def four_paths(adjacency, da, db, x, y):
    """Internal triples (p1,p2,p3) of every x-y path of length 4, given
    d(x,y) = 4 (such paths are shortest, hence layered)."""
    n = len(adjacency)
    out = []
    for p1 in range(n):
        if da[p1] != 1 or db[p1] != 3:
            continue
        for p2 in range(n):
            if da[p2] != 2 or db[p2] != 2 or not adjacency[p1] >> p2 & 1:
                continue
            for p3 in range(n):
                if (da[p3] == 3 and db[p3] == 1
                        and adjacency[p2] >> p3 & 1):
                    assert adjacency[p3] >> y & 1 and adjacency[x] >> p1 & 1
                    out.append((p1, p2, p3))
    return out


def part_a(orders, c4free=True):
    total_graphs = 0
    total_pairs = 0
    stats = {"disjoint": 0, "pencil-terminal": 0, "pencil-middle": 0,
             "unique": 0}
    fan_sizes = {}
    for n in orders:
        cmd = ["geng", "-q", "-c"] + (["-f"] if c4free else []) + [str(n)]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
        graphs = 0
        for line in proc.stdout:
            line = line.strip()
            if not line:
                continue
            graphs += 1
            adj = g6_decode(line)
            if c4free:
                assert not has_c4(adj)
            dist_of = [bfs_all(adj, v) for v in range(n)]
            cycles = None  # computed lazily per graph
            for x in range(n):
                for y in range(x + 1, n):
                    if dist_of[x][y] != 4:
                        continue
                    total_pairs += 1
                    da, db = dist_of[x], dist_of[y]
                    paths = four_paths(adj, da, db, x, y)
                    assert paths, "d(x,y)=4 but no 4-path"
                    sets = [frozenset(t) for t in paths]
                    disjoint = any(not (sets[i] & sets[j])
                                   for i in range(len(sets))
                                   for j in range(i + 1, len(sets)))
                    if cycles is None:
                        cycles = all_cycles(adj)
                    want = (1 << x) | (1 << y)
                    c8xy = any(length == 8 and mask & want == want
                               for length, mask, _ in cycles)
                    assert c8xy == disjoint, (
                        f"C8-through-terminals mismatch {line} {(x, y)}")
                    middles = {t[1] for t in paths}
                    twotwo = {v for v in range(n)
                              if da[v] == 2 and db[v] == 2}
                    assert middles == twotwo, (
                        f"(2,2) != middles {line} {(x, y)}")
                    if disjoint:
                        stats["disjoint"] += 1
                        continue
                    common = frozenset.intersection(*sets)
                    assert common, f"PENCIL FAILS {line} {(x, y)}"
                    if len(sets) == 1:
                        stats["unique"] += 1
                        assert len(twotwo) == 1, (
                            f"unique path, several (2,2) {line} {(x, y)}")
                        continue
                    if not c4free:
                        # general lemma only: a common vertex exists.
                        if any(da[c] == 1 or db[c] == 1 for c in common):
                            stats["pencil-terminal"] += 1
                        else:
                            stats["pencil-middle"] += 1
                        continue
                    assert len(common) == 1, (
                        f">=2 paths share >=2 vertices {line} {(x, y)}")
                    (c,) = common
                    assert da[c] == 1 or db[c] == 1, (
                        f"middle pencil with >=2 paths {line} {(x, y)}")
                    stats["pencil-terminal"] += 1
                    t = len(sets)
                    fan_sizes[t] = fan_sizes.get(t, 0) + 1
                    if da[c] == 1:
                        ms = [p[1] for p in paths]
                        bs = [p[2] for p in paths]
                    else:
                        ms = [p[1] for p in paths]
                        bs = [p[0] for p in paths]
                    assert len(set(ms)) == t and len(set(bs)) == t, (
                        f"fan repeats a strand vertex {line} {(x, y)}")
                    for i in range(t):
                        for j in range(t):
                            if i != j:
                                assert not adj[ms[i]] >> bs[j] & 1, (
                                    f"cross chord {line} {(x, y)}")
        assert proc.wait() == 0
        total_graphs += graphs
        label = "C4-free connected" if c4free else "connected"
        print(f"A n={n}: {graphs} {label} graphs scanned")
    print(f"A total: graphs={total_graphs} distance-4 pairs={total_pairs} "
          f"outcomes={stats} fan-sizes={fan_sizes}")
    DATA.mkdir(exist_ok=True)
    payload = {
        "mode": "c4free" if c4free else "general",
        "orders": orders, "graphs": total_graphs, "pairs": total_pairs,
        "outcomes": stats, "fan_sizes": {str(k): v
                                         for k, v in sorted(fan_sizes.items())},
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
    }
    stem = "verify_c4free" if c4free else "verify_general"
    (DATA / f"{stem}.json").write_text(json.dumps(payload, indent=2))

    # Fixed anchors for the C4-free refinements' sharpness.
    # (1) Without C4-freeness two 4-paths can share TWO internal vertices
    #     (double middle: a-m-b and a-m'-b), so the <=1-shared-vertex
    #     refinement genuinely consumes C4-freeness.
    x, a, m, m2, b, y = range(6)
    edges = [(x, a), (a, m), (a, m2), (m, b), (m2, b), (b, y)]
    adj = [0] * 6
    for p, q in edges:
        adj[p] |= 1 << q
        adj[q] |= 1 << p
    da, db = bfs_all(adj, x), bfs_all(adj, y)
    assert da[y] == 4
    paths = four_paths(adj, da, db, x, y)
    assert sorted(paths) == [(a, m, b), (a, m2, b)]
    assert has_c4(adj)
    print("A anchor 1: two 4-paths sharing two internal vertices, with a "
          "C4 (a-m-b-m2) -- the <=1-shared-vertex refinement needs "
          "C4-freeness")
    # (2) Without C4-freeness a >=2-path pencil can sit at a MIDDLE
    #     vertex (product fan through m), so 'pencil vertex adjacent to
    #     a terminal' also consumes C4-freeness.
    x, a, a2, m, b, b2, y = range(7)
    edges = [(x, a), (x, a2), (a, m), (a2, m), (m, b), (m, b2), (b, y),
             (b2, y)]
    adj = [0] * 7
    for p, q in edges:
        adj[p] |= 1 << q
        adj[q] |= 1 << p
    da, db = bfs_all(adj, x), bfs_all(adj, y)
    assert da[y] == 4
    paths = four_paths(adj, da, db, x, y)
    sets = [frozenset(t) for t in paths]
    assert len(paths) == 4
    assert all(sets[i] & sets[j] for i in range(4) for j in range(i))
    assert frozenset.intersection(*sets) == frozenset({m})
    assert has_c4(adj)
    print("A anchor 2: four 4-paths pencilled at a middle vertex, with "
          "C4s -- 'pencil at a terminal neighbor' needs C4-freeness")


def part_b(orders):
    DATA.mkdir(exist_ok=True)
    summaries = []
    for n in orders:
        mine = -(-(3 * n - 2) // 2)
        cmd = ["geng", "-q", "-c", "-d2", str(n), f"{mine}:0"]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
        graphs = twoconn = pairs_scanned = 0
        hits = []
        for line in proc.stdout:
            line = line.strip()
            if not line:
                continue
            graphs += 1
            adj = g6_decode(line)
            degs = degrees(adj)
            sub = [i for i, d in enumerate(degs) if d < 3]
            if len(sub) > 2:
                continue
            if cut_vertices(adj):
                continue
            twoconn += 1
            if len(sub) == 2:
                pairs = [tuple(sub)]
            elif len(sub) == 1:
                s = sub[0]
                pairs = [(s, v) for v in range(n) if v != s]
            else:
                pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
            dist_of = [bfs_all(adj, v) for v in range(n)]
            spectrum = None
            for a, b in pairs:
                pairs_scanned += 1
                verdict, d, S, _ = scan_pair_banded(adj, dist_of, a, b,
                                                    closed=True)
                if verdict != "TAUT":
                    continue
                if spectrum is None:
                    spectrum = sorted({length for length, _, _
                                       in all_cycles(adj)})
                hits.append({
                    "graph6": line, "pair": (a, b), "band": d, "S": S,
                    "strict": max(S) <= 2 * d - 1,
                    "has_c4": has_c4(adj),
                    "has_c8": 8 in spectrum,
                    "spectrum": spectrum,
                })
        assert proc.wait() == 0
        strict_hits = [h for h in hits if h["strict"]]
        no_c8 = [h for h in hits if not h["has_c8"]]
        c4ful = [h for h in hits if h["has_c4"]]
        print(f"B n={n}: stream={graphs} 2conn<=2sub={twoconn} "
              f"pairs={pairs_scanned} closed-taut-hits={len(hits)} "
              f"strict={len(strict_hits)} with-C4={len(c4ful)} "
              f"C8-free={len(no_c8)}")
        strict_band4 = [h for h in strict_hits if h["band"] == 4]
        c8free_band4 = [h for h in no_c8 if h["band"] == 4]
        summaries.append({
            "n": n, "stream": graphs, "two_connected_le2_subcubic": twoconn,
            "pairs": pairs_scanned, "closed_taut_hits": len(hits),
            "strict_hits": len(strict_hits), "with_c4": len(c4ful),
            "c8_free": len(no_c8),
            "strict_band4_examples": strict_band4[:12],
            "c8free_band4_examples": c8free_band4[:12],
            "all_hits": hits,
        })
    (DATA / "block_probe_no_c4_assumption.json").write_text(json.dumps({
        "orders": summaries,
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
    }, indent=2))


if __name__ == "__main__":
    mode = sys.argv[1]
    orders = [int(v) for v in sys.argv[2:]]
    if mode == "a":
        part_a(orders, c4free=True)
    elif mode == "ag":
        part_a(orders, c4free=False)
    elif mode == "b":
        part_b(orders)
