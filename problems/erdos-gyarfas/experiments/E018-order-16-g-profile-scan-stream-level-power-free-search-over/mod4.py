#!/usr/bin/env python3
"""E018 second instrument (attempt A021): the mod-4 kill test.

Question (A019 exit item 2, pre-registered kill condition): does the class of
vertex-taut C4-free (D)-cores with the case-(5b) terminal profile (two
degree-2 terminals, all other degrees >= 3) admit ANY mod-4 confinement of
the through-set S = S(H,a,b) compatible with the residual object's forced
memberships (S meets P = {4,8,...}, meets P-1 = {3,7,...}, avoids
P-2 = {2,6,...})?  Power-freeness is DROPPED (as in E016 A6): the probe
measures what tautness + C4-freeness + the degree profile alone force.

Kill condition (recorded in A019/problem.json): if vertex-taut cores realize
all three memberships with no mod-4 structure — residue sets unconfined —
then the congruence route is dead and case (5b) reduces to the search leg.

Method: enumerate the exactly-two-degree-2 class (the same geng stream as
scan.py) at small orders; per member compute S with an essential-vertex mask
(tautness = every vertex lies on some simple a-b path); tabulate, among taut
members, the joint distribution of (membership triple) x (S mod 4 residue
set), plus bipartiteness and ab-adjacency, and flag L034 invisible shapes
(S contained in P-2).

Output: one table per order + data/mod4_n{N}.json.  Deterministic.
"""

import json
import os
import subprocess
import sys
import time

from scan import (DATA, degrees, g6_decode, geng_args, profile_pair,
                  bipartition, cut_vertices, P_SET, P_MINUS_1, P_MINUS_2)


def paths_with_essential(adjacency, a, b):
    """(set of simple a-b path lengths, mask of vertices on some a-b path)."""
    assert a != b
    out = set()
    essential = 0
    target = 1 << b
    stack = [(a, 1 << a, 0)]
    while stack:
        v, used, length = stack.pop()
        row = adjacency[v] & ~used
        if row & target:
            out.add(length + 1)
            essential |= used | target
        row &= ~target
        while row:
            low = row & -row
            w = low.bit_length() - 1
            row ^= low
            stack.append((w, used | low, length + 1))
    return out, essential


def classify(adjacency, a, b):
    n = len(adjacency)
    s, essential = paths_with_essential(adjacency, a, b)
    taut = essential == (1 << n) - 1
    residues = frozenset(x % 4 for x in s)
    return {
        "S": sorted(s),
        "taut": taut,
        "residues": sorted(residues),
        "meets_P": bool(s & P_SET),
        "meets_P1": bool(s & P_MINUS_1),
        "avoids_P2": not (s & P_MINUS_2),
        "invisible": s <= P_MINUS_2 and bool(s),
        "bipartite": bipartition(adjacency) is not None,
        "ab_adjacent": bool(adjacency[a] >> b & 1),
        "cuts": len(cut_vertices(adjacency)),
    }


def cmd_probe(args):
    orders = [int(x) for x in args] or [10, 11, 12, 13]
    for n in orders:
        t0 = time.time()
        proc = subprocess.Popen(geng_args(n), stdout=subprocess.PIPE,
                                bufsize=1 << 20)
        rows = []
        assert proc.stdout is not None
        for raw in proc.stdout:
            adjacency = g6_decode(raw.decode())
            pair = profile_pair(degrees(adjacency))
            if pair is None:
                continue
            rec = classify(adjacency, *pair)
            rec["g6"] = raw.decode().strip()
            rows.append(rec)
        assert proc.wait() == 0

        taut_rows = [r for r in rows if r["taut"]]
        triple = [r for r in taut_rows
                  if r["meets_P"] and r["meets_P1"] and r["avoids_P2"]]
        residue_hist = {}
        for r in triple:
            key = ",".join(str(x) for x in r["residues"])
            residue_hist[key] = residue_hist.get(key, 0) + 1
        summary = {
            "order": n,
            "class": len(rows),
            "taut": len(taut_rows),
            "taut_triple": len(triple),
            "triple_residue_hist": dict(sorted(residue_hist.items())),
            "triple_bipartite": sum(r["bipartite"] for r in triple),
            "triple_ab_adjacent": sum(r["ab_adjacent"] for r in triple),
            "triple_with_cuts": sum(r["cuts"] > 0 for r in triple),
            "taut_invisible_S": sum(r["invisible"] for r in taut_rows),
            "seconds": round(time.time() - t0, 1),
        }
        print(json.dumps(summary, indent=1))
        examples = triple[:8]
        for r in examples:
            print("  taut triple example: S=%s residues=%s bip=%s cuts=%d %s"
                  % (r["S"], r["residues"], r["bipartite"], r["cuts"],
                     r["g6"]))
        os.makedirs(DATA, exist_ok=True)
        with open(os.path.join(DATA, "mod4_n%d.json" % n), "w") as fh:
            json.dump({"summary": summary, "rows": rows}, fh, indent=1)


if __name__ == "__main__":
    cmd_probe(sys.argv[1:])
