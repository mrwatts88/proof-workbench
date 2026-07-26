#!/usr/bin/env python3
"""THE DECISIVE MEASUREMENT for the order-21 rung.

For every order-21 degree-profile member (exactly two degree-2 vertices, all
others >= 3, {C4,C8}-free), compute:

    max S  vs  n-1      -- the HAMILTONIAN / NON-HAMILTONIAN split.
                           max S == n-1 means some a-b path visits every
                           vertex.  E028's ladder decides (F) only on the
                           Hamiltonian stratum, so whether the profile FORCES
                           this is what decides how much of case (5b) that
                           ladder actually covers.
    S cap {2,6,14,30}   -- the poison set.
    16 in Spec          -- the C16 blocking.

All primitives come from the LOCAL, already-anchored E019 instrument; nothing
here re-implements a graph property.
"""
import importlib.util
import os
import sys

sys.dont_write_bytecode = True

E019 = ("/Users/mattwatts/code/rh/problems/erdos-gyarfas/experiments/"
        "E019-dedicated-c4-c8-free-generator-geng-prune-plugin-and-the-ord")
MERGED = ("/private/tmp/claude-501/-Users-mattwatts-code-rh/"
          "34080fcf-635d-458d-88bf-8a372e5a8195/scratchpad/e024-merged")
PROFILE = os.path.join(MERGED, "profile_n21_mod144_merged.txt")

spec = importlib.util.spec_from_file_location(
    "e019_scan", os.path.join(E019, "scan.py"))
scan = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scan)

POISON = (2, 6, 14, 30)
rows = []
with open(PROFILE) as fh:
    for line in fh:
        if line.startswith("#") or not line.strip():
            continue
        g6, edges, n2, pf, part = line.split()
        rows.append((g6, int(edges), int(part)))

print("order-21 degree-profile members: %d\n" % len(rows))
print("%-26s %5s %6s %7s %8s %6s %s"
      % ("graph6", "edges", "d(a,b)", "max S", "n-1=20", "C16", "S cap {2,6,14,30}"))

ham = 0
for g6, edges, part in sorted(rows):
    adj = scan.g6_decode(g6)
    n = len(adj)
    deg = scan.degrees(adj)
    pair = scan.profile_pair(deg)
    assert pair is not None, g6
    a, b = pair
    S = scan.path_lengths(adj, a, b)
    mx = max(S)
    poison = sorted(set(S) & set(POISON))
    c16 = scan.has_cycle_len(adj, 16)
    is_ham = (mx == n - 1)
    ham += is_ham
    # sanity: the instrument's own class conditions
    assert not scan.has_c4(adj) and not scan.has_cycle_len(adj, 8), g6
    assert sum(1 for d in deg if d == 2) == 2 and min(deg) == 2, g6
    assert sum(deg) // 2 == edges, g6
    # min S == d(a,b) is the recorded invariant (C047 asserts it per row)
    assert min(S) == scan.bfs_dist(adj, a, (1 << n) - 1)[b], g6
    print("%-26s %5d %6d %7d %8s %6s %s"
          % (g6, edges, min(S), mx,
             "YES" if is_ham else "**NO**", "yes" if c16 else "NO", poison))

print("")
print("HAMILTONIAN (max S == n-1) : %d of %d" % (ham, len(rows)))
print("C16-blocked                : %d of %d"
      % (sum(1 for g6, _, _ in rows
             if scan.has_cycle_len(scan.g6_decode(g6), 16)), len(rows)))
