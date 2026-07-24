#!/usr/bin/env python3
"""E017 — sharpness certificate for the 2/3 cubic-density bound (problem P-002).

Verifies the explicit 15-vertex graph S15 of attempt A020 (deduction W2-T7).

S15 is defined on Z_5-indexed vertices:
    A = {a_i, a'_i : i in Z_5}   (intended degree 3)
    B = {b_i       : i in Z_5}   (intended degree 4)
    edges  a_i a'_i ,  a_i b_i ,  a'_i b_i ,  a_i b_{i+1} ,  a'_i b_{i+2}.

The claim under test (W2-T7): S15 satisfies simultaneously
  (S1) delta(S15) >= 3;
  (S2) every proper subgraph of S15 has minimum degree <= 2
       -- the full conclusion of Carr's Lemma 0.1 (dossier row C004);
  (S3) the vertices of degree >= 4 form an independent set (L002 / C005's
       companion) and every vertex has a neighbour of degree exactly 3 (C005);
  (S4) S15 has no 4-cycle;
  (S5) |V_3| = 10 = (2/3) * 15 exactly,
and fails only power-freeness, its unique power-of-two cycle length being 8.

Everything is exact integer / set arithmetic. No randomness, no floating point.

Usage:  python3 verify.py            (runs anchors, then the S15 certificate)
"""

import itertools
import sys

# ---------------------------------------------------------------- primitives


def adjacency(vertices, edges):
    adj = {v: set() for v in vertices}
    for e in edges:
        u, w = tuple(e)
        assert u != w, "loop"
        assert u in adj and w in adj, "endpoint outside vertex set"
        adj[u].add(w)
        adj[w].add(u)
    return adj


def degrees(adj):
    return {v: len(adj[v]) for v in adj}


def cycles_by_length(vertices, edges):
    """Exact count of simple cycles by length, by DFS with a canonical form.

    A cycle is counted once: it is enumerated from its smallest vertex in a
    fixed order, and only in the orientation whose second vertex precedes its
    last vertex.
    """
    adj = adjacency(vertices, edges)
    rank = {v: i for i, v in enumerate(vertices)}
    counts = {}
    for start in vertices:
        stack = [(start, [start], frozenset([start]))]
        while stack:
            cur, path, seen = stack.pop()
            for nxt in adj[cur]:
                if nxt == start:
                    if len(path) >= 3 and rank[path[1]] < rank[path[-1]]:
                        counts[len(path)] = counts.get(len(path), 0) + 1
                elif nxt not in seen and rank[nxt] > rank[start]:
                    stack.append((nxt, path + [nxt], seen | {nxt}))
    return dict(sorted(counts.items()))


def cycles_by_length_bruteforce(vertices, edges):
    """Independent second implementation: enumerate every vertex subset and
    every cyclic arrangement of it.  Exponential; used only on small anchors."""
    adj = adjacency(vertices, edges)
    counts = {}
    n = len(vertices)
    for size in range(3, n + 1):
        for subset in itertools.combinations(vertices, size):
            head = subset[0]
            rest = subset[1:]
            for perm in itertools.permutations(rest):
                # canonical: fix head first, and only keep perm[0] < perm[-1]
                if len(perm) >= 2 and perm[0] > perm[-1]:
                    continue
                seq = (head,) + perm
                if all(seq[(i + 1) % size] in adj[seq[i]] for i in range(size)):
                    counts[size] = counts.get(size, 0) + 1
    return dict(sorted(counts.items()))


def is_two_degenerate(vertices, edges):
    """True iff repeatedly deleting vertices of current degree <= 2 empties the
    graph -- equivalently, iff the graph has no nonempty subgraph of minimum
    degree >= 3."""
    adj = {v: set() for v in vertices}
    for e in edges:
        u, w = tuple(e)
        if u in adj and w in adj:
            adj[u].add(w)
            adj[w].add(u)
    changed = True
    while changed:
        changed = False
        for v in list(adj):
            if len(adj[v]) <= 2:
                for w in adj[v]:
                    adj[w].discard(v)
                del adj[v]
                changed = True
    return not adj


def no_proper_subgraph_of_min_degree_3(vertices, edges):
    """Lemma 0.1's conclusion for the graph itself.

    Every proper subgraph H of G satisfies H <= G-v for some vertex v (when
    V(H) != V(G)) or H <= G-e for some edge e (when V(H) = V(G)); degeneracy is
    monotone under subgraphs; so the condition is equivalent to: G-v is
    2-degenerate for every v, and G-e is 2-degenerate for every e.
    """
    vs = set(vertices)
    for v in vertices:
        if not is_two_degenerate(vs - {v}, edges):
            return False, ("vertex", v)
    for e in edges:
        if not is_two_degenerate(vs, [f for f in edges if f != e]):
            return False, ("edge", tuple(sorted(e, key=str)))
    return True, None


def max_codegree(vertices, edges):
    adj = adjacency(vertices, edges)
    best = 0
    for u, w in itertools.combinations(vertices, 2):
        best = max(best, len(adj[u] & adj[w]))
    return best


# ------------------------------------------------------------------- anchors


def petersen():
    outer = [("o", i) for i in range(5)]
    inner = [("i", i) for i in range(5)]
    V = outer + inner
    E = []
    for i in range(5):
        E.append(frozenset((("o", i), ("o", (i + 1) % 5))))
        E.append(frozenset((("i", i), ("i", (i + 2) % 5))))
        E.append(frozenset((("o", i), ("i", i))))
    return V, E


def complete(k):
    V = [("v", i) for i in range(k)]
    E = [frozenset(p) for p in itertools.combinations(V, 2)]
    return V, E


def complete_bipartite(p, q):
    V = [("x", i) for i in range(p)] + [("y", j) for j in range(q)]
    E = [frozenset((("x", i), ("y", j))) for i in range(p) for j in range(q)]
    return V, E


def cycle_graph(k):
    V = [("c", i) for i in range(k)]
    E = [frozenset((("c", i), ("c", (i + 1) % k))) for i in range(k)]
    return V, E


def run_anchors():
    fails = []

    def check(name, got, want):
        ok = got == want
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {got}")
        if not ok:
            fails.append((name, got, want))

    # A1  cycle spectrum of K_4 : 4 triangles, 3 quadrilaterals
    V, E = complete(4)
    check("A1 K4 cycle counts", cycles_by_length(V, E), {3: 4, 4: 3})
    check("A1' K4 cycle counts (brute force)",
          cycles_by_length_bruteforce(V, E), {3: 4, 4: 3})

    # A2  cycle spectrum of K_{3,3} : 9 quadrilaterals, 6 hexagons
    V, E = complete_bipartite(3, 3)
    check("A2 K33 cycle counts", cycles_by_length(V, E), {4: 9, 6: 6})
    check("A2' K33 cycle counts (brute force)",
          cycles_by_length_bruteforce(V, E), {4: 9, 6: 6})

    # A3  Petersen graph : 12 pentagons, 10 hexagons, 15 octagons, 20 nonagons
    V, E = petersen()
    check("A3 Petersen cycle counts", cycles_by_length(V, E),
          {5: 12, 6: 10, 8: 15, 9: 20})

    # A4  degeneracy detector, both verdicts
    V, E = complete(4)
    check("A4 K4 is not 2-degenerate", is_two_degenerate(V, E), False)
    V, E = cycle_graph(5)
    check("A4' C5 is 2-degenerate", is_two_degenerate(V, E), True)
    V, E = petersen()
    check("A4'' Petersen is not 2-degenerate", is_two_degenerate(V, E), False)

    # A5  Lemma 0.1 detector, negative control: K_5 has the proper subgraph K_4
    V, E = complete(5)
    ok, _ = no_proper_subgraph_of_min_degree_3(V, E)
    check("A5 K5 has a proper subgraph of min degree 3", ok, False)
    # positive control: Petersen is cubic and edge/vertex deletion kills it
    V, E = petersen()
    ok, _ = no_proper_subgraph_of_min_degree_3(V, E)
    check("A5' Petersen has none", ok, True)

    # A6  codegree detector on a known C_4-free graph (Petersen, girth 5)
    check("A6 Petersen max codegree", max_codegree(*petersen()), 1)

    return fails


# ----------------------------------------------------------------- the graph


def s15():
    def r(i):
        return (i - 1) % 5 + 1
    A = [("a", i) for i in range(1, 6)] + [("A", i) for i in range(1, 6)]
    B = [("b", i) for i in range(1, 6)]
    V = A + B
    E = []
    for i in range(1, 6):
        E.append(frozenset((("a", i), ("A", i))))
        E.append(frozenset((("a", i), ("b", i))))
        E.append(frozenset((("A", i), ("b", i))))
        E.append(frozenset((("a", i), ("b", r(i + 1)))))
        E.append(frozenset((("A", i), ("b", r(i + 2)))))
    return V, A, B, E


def run_certificate():
    fails = []

    def check(name, got, want):
        ok = got == want
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {got}")
        if not ok:
            fails.append((name, got, want))

    V, A, B, E = s15()
    adj = adjacency(V, E)
    deg = degrees(adj)

    check("n", len(V), 15)
    check("m", len(E), 25)
    check("degree multiset on A", sorted({deg[v] for v in A}), [3])
    check("degree multiset on B", sorted({deg[v] for v in B}), [4])
    check("V_3 = A", sorted(v for v in V if deg[v] == 3), sorted(A))
    check("|V_3|", len([v for v in V if deg[v] == 3]), 10)
    check("3*|V_3| == 2*n", 3 * 10, 2 * 15)                      # (S5)
    check("delta >= 3", min(deg.values()) >= 3, True)            # (S1)

    setB = set(B)
    setA = set(A)
    check("V_>=4 independent", all(not (adj[b] & setB) for b in B), True)
    check("every vertex has a degree-3 neighbour",
          all(any(deg[u] == 3 for u in adj[v]) for v in V), True)   # (S3)
    check("A-internal degrees", sorted({len(adj[v] & setA) for v in A}), [1])
    check("G[A] is a perfect matching",
          sum(len(adj[v] & setA) for v in A) // 2, 5)

    check("max codegree (C_4-free iff 1)", max_codegree(V, E), 1)   # (S4)

    ok, witness = no_proper_subgraph_of_min_degree_3(V, E)          # (S2)
    check("every proper subgraph has min degree <= 2", (ok, witness), (True, None))

    spec = cycles_by_length(V, E)
    print(f"  [   ] cycle counts by length: {spec}")
    powers = sorted(L for L in spec if L >= 4 and (L & (L - 1)) == 0)
    check("power-of-two cycle lengths present", powers, [8])
    check("no 4-cycle", 4 in spec, False)
    check("number of 8-cycles", spec.get(8), 50)

    # the counting identities of A020 W2-T0 on this instance
    p = sum(1 for v in A if len(adj[v] & setA) == 1)
    q = sum(1 for v in A if len(adj[v] & setA) == 2)
    eAB = sum(len(adj[v] & setB) for v in A)
    check("e(A,B) = sum of B-degrees", eAB, sum(deg[b] for b in B))
    check("e(A,B) = 2p + q", eAB, 2 * p + q)
    check("(p, q)", (p, q), (10, 0))

    # the link multigraph H_1 of A020 W2-T5 on this instance
    h1_edges = {frozenset(adj[v] & setB) for v in A if len(adj[v] & setB) == 2}
    check("H_1 is simple with |E| = p", len(h1_edges), p)
    check("H_1 = K_5", len(h1_edges), 10)
    check("H_1 is NOT 2-degenerate (S15 is not power-free)",
          is_two_degenerate(B, list(h1_edges)), False)
    h1spec = cycles_by_length(B, list(h1_edges))
    check("H_1 has 4-cycles (lifting to the 8-cycles of S15)",
          h1spec.get(4), 15)

    return fails


def main():
    print(f"python {sys.version.split()[0]}")
    print("anchors:")
    fails = run_anchors()
    print("S15 certificate:")
    fails += run_certificate()
    print()
    if fails:
        print(f"FAILURES: {len(fails)}")
        for f in fails:
            print("  ", f)
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
