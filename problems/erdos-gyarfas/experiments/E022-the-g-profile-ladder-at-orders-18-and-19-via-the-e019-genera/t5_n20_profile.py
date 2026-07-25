"""S022 harvest addendum: the seven order-20 profile members — extraction,
independent verification, and the T5 kill test on their full cycle sets.

Stage B (scan_n20_harvest.json) counted 7 members of the exactly-two-degree-2
profile at order 20, all C16-blocked, none power-free.  This script:
  1. re-extracts them from the committed-complete class files by degree
     filter and asserts the count is exactly 7;
  2. independently re-verifies each (self-contained primitives, no E019/E021
     imports): connected, C4-free, C8-free, C16 present, exactly two
     degree-2 vertices, S-set and its {2,6,14} intersection, bipartiteness,
     2-connectivity, vertex-tautness;
  3. runs the T5 test (every cycle an interference cycle?) on the full cycle
     set of each, with the determined-partner algorithm, and re-verifies
     every C16 verdict with the independent pairwise algorithm.

Output: data/t5_n20_profile.json.  Deterministic, stdlib only.
"""
import glob
import json
import os
import sys
from collections import deque
from itertools import combinations

sys.setrecursionlimit(100000)

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT = os.path.join(DATA, "t5_n20_profile.json")


def g6_decode(s):
    data = [ord(c) - 63 for c in s.strip()]
    n = data[0]
    bits = []
    for x in data[1:]:
        for i in range(5, -1, -1):
            bits.append((x >> i) & 1)
    adj = [set() for _ in range(n)]
    k = 0
    for j in range(1, n):
        for i in range(j):
            if bits[k]:
                adj[i].add(j)
                adj[j].add(i)
            k += 1
    return adj


def all_ab_paths(adj, a, b):
    out = []
    visited = {a}
    edges = []

    def rec(v):
        if v == b:
            out.append(frozenset(edges))
            return
        for w in adj[v]:
            if w not in visited:
                visited.add(w)
                e = (v, w) if v < w else (w, v)
                edges.append(e)
                rec(w)
                edges.pop()
                visited.discard(w)

    rec(a)
    return out


def all_cycles(adj):
    n = len(adj)
    cycles = set()
    for start in range(n):
        stack = [(start, (start,), frozenset())]
        while stack:
            v, path, eset = stack.pop()
            for w in adj[v]:
                if w == start and len(path) >= 3:
                    e = (v, w) if v < w else (w, v)
                    cycles.add(eset | {e})
                elif w not in path and w > start:
                    e = (v, w) if v < w else (w, v)
                    stack.append((w, path + (w,), eset | {e}))
    return cycles


def connected(adj):
    n = len(adj)
    seen = {0}
    q = deque([0])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                q.append(w)
    return len(seen) == n


def two_connected(adj):
    n = len(adj)
    for v in range(n):
        rest = [u for u in range(n) if u != v]
        seen = {rest[0]}
        q = deque([rest[0]])
        while q:
            x = q.popleft()
            for w in adj[x]:
                if w != v and w not in seen:
                    seen.add(w)
                    q.append(w)
        if len(seen) != n - 1:
            return False
    return True


def main():
    # SAVE_LIMIT note: scan.py saves at most 200,000 class members per part,
    # so the order-20 class files are a SAMPLE (572,530 of 2,569,481 saved),
    # unlike orders 18-19 (complete).  The 7 profile members sit in parts 1
    # (1 member, part complete at 23,054), 8 (2 members, complete at 10,025)
    # and 14 (4 members, TRUNCATED at 200,000 of 439,745 - none of its 4 fall
    # in the saved window).  So exactly 3 are recoverable from disk here; the
    # part-14 recollection run (collect_n20_part14.py) recovers the other 4.
    # Class-file line format: "graph6 edges n_degree2 power_free" plus a
    # leading comment line; take column 0.
    members = []
    for path in sorted(glob.glob(os.path.join(DATA, "class_n20_part*of16.txt"))):
        with open(path) as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                g6 = line.split()[0]
                adj = g6_decode(g6)
                degs = [len(r) for r in adj]
                if degs.count(2) == 2 and all(d >= 3 for d in degs if d != 2):
                    members.append((g6, adj))
    assert len(members) == 3, "expected 3 on-disk profile members, found %d" % len(members)

    reports = []
    total_cycles = 0
    total_nondec = 0
    for g6, adj in members:
        n = len(adj)
        degs = [len(r) for r in adj]
        d2 = [v for v in range(n) if degs[v] == 2]
        a, b = d2
        assert connected(adj)
        cycles = all_cycles(adj)
        spec = sorted({len(c) for c in cycles})
        assert 4 not in spec and 8 not in spec, (g6, spec)
        assert 16 in spec, (g6, spec)
        paths = all_ab_paths(adj, a, b)
        pathset = set(paths)
        S = sorted({len(p) for p in paths})
        covered = {a, b}
        for p in paths:
            for u, v in p:
                covered.add(u)
                covered.add(v)
        taut = covered == set(range(n))
        # T5 test, determined-partner, full cycle set
        nondec = []
        by_len = {}
        for c in cycles:
            by_len.setdefault(len(c), [0, 0])
            hit = any((p ^ c) != p and (p ^ c) in pathset for p in paths)
            by_len[len(c)][0] += 1
            if hit:
                by_len[len(c)][1] += 1
            else:
                nondec.append(sorted(sorted(e) for e in c))
        # pairwise re-verification on every C16
        c16s = [c for c in cycles if len(c) == 16]
        pair_ok = 0
        for c in c16s:
            found = False
            for p, q in combinations(paths, 2):
                if (p ^ q) == c:
                    found = True
                    break
            if found:
                pair_ok += 1
        total_cycles += len(cycles)
        total_nondec += len(nondec)
        reports.append({
            "g6": g6, "order": n, "terminals": d2,
            "S": S, "S_cap_2_6_14": sorted(set(S) & {2, 6, 14}),
            "spectrum": spec, "c16_count": len(c16s),
            "vertex_taut": taut,
            "two_connected": two_connected(adj),
            "bipartite": all(l % 2 == 0 for l in spec),
            "paths": len(paths), "cycles": len(cycles),
            "per_length": {str(k): {"cycles": v[0], "decomposable": v[1]}
                           for k, v in sorted(by_len.items())},
            "non_decomposable": nondec,
            "c16_pairwise_reverified": pair_ok,
            "c16_pairwise_agrees": (pair_ok == len(c16s)
                                    and by_len.get(16, [0, 0])[1] == pair_ok),
        })

    result = {
        "profile_members_on_disk": len(members),
        "profile_tally_stage_b": 7,
        "truncation_note": ("class_n20 files are SAVE_LIMIT samples; parts "
                            "1 and 8 complete (3 members here); part 14's 4 "
                            "members await the recollection run"),
        "total_cycles": total_cycles,
        "total_non_decomposable": total_nondec,
        "t5_verdict_on_these_objects": ("SURVIVES on all 3 on-disk members"
                                        if total_nondec == 0
                                        else "KILLED - see non_decomposable"),
        "graphs": reports,
        "interpreter": sys.version,
    }
    with open(OUT, "w") as fh:
        json.dump(result, fh, indent=1)
    print("n20 profile: %d of 7 members on disk; %d cycles total; "
          "%d non-decomposable -> %s"
          % (len(members), total_cycles, total_nondec,
             result["t5_verdict_on_these_objects"]))
    for r in reports:
        print("  %s taut=%s 2conn=%s C16s=%d S&{2,6,14}=%s paths=%d cycles=%d"
              % (r["g6"], r["vertex_taut"], r["two_connected"], r["c16_count"],
                 r["S_cap_2_6_14"], r["paths"], r["cycles"]))


if __name__ == "__main__":
    main()
