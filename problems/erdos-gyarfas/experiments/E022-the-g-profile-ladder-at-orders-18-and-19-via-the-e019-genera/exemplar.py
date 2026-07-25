#!/usr/bin/env python3
"""E022 -- full analysis of the boundary exemplars.

A *boundary exemplar* here is a member of the generated {C4,C8}-free class
with at most two degree-2 vertices, i.e. a graph sitting in the 0-, 1- or
2-bucket of the degree-2 histogram:

    0 degree-2 vertices  -> a minimum-degree-3 {C4,C8}-free graph (C040's class)
    1 degree-2 vertex    -> the shape of a tight 1-atom (L041)
    2 degree-2 vertices  -> the G-profile itself (L039)

scan.py already reports the counts and runs the full survivor analysis on the
power-free ones; this script records the *blocked* ones too, because they are
the nearest misses and the C16 that blocks them is the object the proof side
wants to dissect.  Nothing here prunes or proves anything -- it is descriptive
data on graphs that the scan has already classified.

    <python> exemplar.py N [max_degree_2]
reads data/class_nN*.txt (the 16-part run) and writes
data/exemplars_nN.json.
"""

import glob
import json
import os
import sys

import ladder

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")


def main():
    n = int(sys.argv[1])
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    mod = ladder.load_scan(DATA)
    paths = sorted(glob.glob(os.path.join(DATA, "class_n%d*.txt" % n)))
    assert paths, "no saved class files for order %d" % n
    rows = []
    for path in paths:
        with open(path) as fh:
            for line in fh:
                if line.startswith("#"):
                    continue
                g6, edges, n2, pf = line.split()
                if int(n2) > limit:
                    continue
                adj = mod.g6_decode(g6)
                assert len(adj) == n
                deg = mod.degrees(adj)
                assert sum(deg) // 2 == int(edges)
                # independent re-verification, second algorithm
                spec = sorted(mod.cycle_spectrum_bruteforce(adj))
                assert 4 not in spec and 8 not in spec, g6
                assert not mod.has_c4(adj), g6
                assert not mod.has_cycle_len(adj, 8), g6
                is_pf, present = mod.power_free(adj)
                assert is_pf == (int(pf) == 1)
                assert (16 in spec) == mod.has_cycle_len(adj, 16)
                small = [v for v, d in enumerate(deg) if d == 2]
                assert len(small) == int(n2)
                row = {
                    "g6": g6, "n": n, "edges": int(edges),
                    "degree_sequence": sorted(deg, reverse=True),
                    "n_degree_2": int(n2), "degree_2_vertices": small,
                    "power_free": is_pf,
                    "power_lengths_present": present,
                    "spectrum": spec,
                    "girth": min(spec),
                    "c16_count": mod.count_cycles_len(adj, 16),
                    "bipartite": mod.bipartition(adj) is not None,
                    "cut_vertices": mod.cut_vertices(adj),
                    "source_file": os.path.basename(path),
                }
                if len(small) == 2:
                    a, b = small
                    s = mod.path_lengths(adj, a, b)
                    row.update({
                        "S": sorted(s),
                        "S_hits_P_minus_2": sorted(s & mod.P_MINUS_2),
                        "in_G": not (s & mod.P_MINUS_2),
                        "S_meets_P": sorted(s & mod.P_SET),
                        "S_meets_P_minus_1": sorted(s & mod.P_MINUS_1),
                        "ab_adjacent": bool(adj[a] >> b & 1),
                        "ab_distance": mod.bfs_dist(adj, a, (1 << n) - 1)[b],
                    })
                rows.append(row)
    out = os.path.join(DATA, "exemplars_n%d.json" % n)
    with open(out, "w") as fh:
        json.dump({"order": n, "max_degree_2": limit, "found": len(rows),
                   "interpreter": mod.interpreter(), "exemplars": rows},
                  fh, indent=1)
    print("order %d: %d class member(s) with <=%d degree-2 vertices" % (n, len(rows), limit))
    for row in rows:
        print(json.dumps(row, indent=1))


if __name__ == "__main__":
    main()
