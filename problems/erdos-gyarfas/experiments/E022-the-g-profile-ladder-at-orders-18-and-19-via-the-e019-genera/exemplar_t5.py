"""S022 orchestrator addendum (follow-up stage A): the order-19 profile
exemplar's FULL cycle set against candidate lemma T5 (A023).

The exemplar R???C@?GC_B?@_aAA_aP?W_?BO@Gc? (C043) is vertex-taut for its
terminal pair (7,8), so A023 T5 predicts every one of its cycles is an
interference cycle.  A single non-decomposable cycle kills T5 as stated, at
the most relevant object in the dossier.

Algorithm (deliberately different from E021's pairwise search, so this run
is also an independent-algorithm check): a cycle C is an interference cycle
iff for some simple a-b path P, the edge set E(P) xor E(C) is itself a
simple a-b path.  (E(C) = E(P) ^ E(Q)  <=>  E(Q) = E(P) ^ E(C); soundness
and completeness are immediate.)  Membership is tested against the complete
path-edge-set index.

Self-contained on purpose: the primitives are the orchestrator's audit
implementations, which were verified this session against E021's engine on
three families (agreement everywhere they overlap).  Deterministic, stdlib
only, no randomness, no wall-clock logic.

Output: data/exemplar_t5_n19.json
"""
import json
import os
import sys

sys.setrecursionlimit(100000)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "exemplar_t5_n19.json")

G6 = "R???C@?GC_B?@_aAA_aP?W_?BO@Gc?"
A, B = 7, 8


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


def main():
    adj = g6_decode(G6)
    n = len(adj)
    assert n == 19
    degs = [len(r) for r in adj]
    assert sorted(degs) == [2, 2] + [3] * 16 + [4]
    assert [v for v in range(n) if degs[v] == 2] == [A, B]

    paths = all_ab_paths(adj, A, B)
    pathset = set(paths)
    lengths = sorted({len(p) for p in paths})
    assert lengths == list(range(5, 19)), lengths  # S = {5..18}, C043

    # vertex-tautness (T5's hypothesis), re-asserted
    covered = {A, B}
    for p in paths:
        for u, v in p:
            covered.add(u)
            covered.add(v)
    assert covered == set(range(n)), "exemplar not vertex-taut?"

    cycles = all_cycles(adj)
    by_len = {}
    for c in cycles:
        by_len.setdefault(len(c), []).append(c)
    assert sorted(by_len) == [3, 5, 6, 7] + list(range(9, 20))
    assert len(by_len[16]) == 46  # C043

    per_len = {}
    failures = []
    for ln in sorted(by_len):
        dec = 0
        for c in by_len[ln]:
            hit = False
            for p in paths:
                q = p ^ c
                if q != p and q in pathset:
                    hit = True
                    break
            if hit:
                dec += 1
            else:
                failures.append({"length": ln,
                                 "edges": sorted(sorted(e) for e in c)})
        per_len[str(ln)] = {"cycles": len(by_len[ln]), "decomposable": dec}

    total = sum(v["cycles"] for v in per_len.values())
    nondec = len(failures)
    result = {
        "graph6": G6,
        "terminals": [A, B],
        "order": n,
        "paths": len(paths),
        "path_lengths": lengths,
        "vertex_taut": True,
        "cycles_total": total,
        "per_length": per_len,
        "non_decomposable": nondec,
        "failures": failures,
        "t5_verdict_on_this_object": ("SURVIVES: every cycle is an "
                                      "interference cycle" if nondec == 0
                                      else "KILLED: non-decomposable cycle(s) "
                                           "recorded above"),
        "algorithm": "determined-partner (P xor C in pathset), independent "
                     "of E021's pairwise search",
        "interpreter": sys.version,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        json.dump(result, fh, indent=1)
    print("exemplar T5 test: %d cycles, %d non-decomposable -> %s"
          % (total, nondec, result["t5_verdict_on_this_object"]))


if __name__ == "__main__":
    main()
