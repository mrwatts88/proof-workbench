# Erdős–Gyárfás Conjecture

- Problem ID: `P-002`
- Statement version: 0.1
- Last changed: 2026-07-23

## Exact statement

Every finite simple undirected graph \(G\) with minimum degree
\(\delta(G)\ge 3\) contains a cycle of length \(2^k\) for some integer
\(k\ge 2\).

## Definitions and conventions

- `D001` — A graph is finite, simple, and undirected: it has finitely many
  vertices, no loops, no parallel edges, and unordered edges.
- `D002` — For \(v\in V(G)\), \(d_G(v)\) is the number of its neighbors. For a
  nonempty graph,
  \(\delta(G)=\min_{v\in V(G)}d_G(v)\). The empty graph is outside the
  hypothesis because its minimum degree is not defined here.
- `D003` — A cycle of length \(\ell\) is a sequence of \(\ell\ge 3\) distinct
  vertices \(v_0,\ldots,v_{\ell-1}\) with
  \(v_iv_{i+1}\in E(G)\) for \(0\le i<\ell-1\) and
  \(v_{\ell-1}v_0\in E(G)\).
- `D004` — A power-of-two cycle is a cycle whose length is \(2^k\) for an
  integer \(k\ge 2\). The lower bound on \(k\) is automatic under `D001` and
  `D003`, because simple graphs have no cycles of length \(1\) or \(2\).

## Hypotheses

1. \(G\) is finite, simple, and undirected.
2. Every vertex of \(G\) has degree at least \(3\).

No connectedness, regularity, planarity, or upper bound on the order or degrees
is assumed.

## Quantifier form

For every nonempty finite set \(V\) and every set
\(E\subseteq\{\{u,v\}:u,v\in V,\ u\ne v\}\), if the graph \(G=(V,E)\)
satisfies
\[
  (\forall v\in V)\ d_G(v)\ge 3,
\]
then there exist an integer \(k\ge 2\) and \(2^k\) distinct vertices
\(v_0,\ldots,v_{2^k-1}\in V\) which, in cyclic order, form a cycle in \(G\).

## Negation

There exists a finite simple undirected graph \(G\) such that
\(\delta(G)\ge 3\) and, for every integer \(k\ge 2\), \(G\) has no cycle of
length \(2^k\). Because \(G\) is finite, only the values with
\(2^k\le |V(G)|\) need to be excluded for any particular candidate.

## Boundary and degenerate cases

- The order-\(0\) graph is outside the hypothesis because `D002` leaves its
  minimum degree undefined. Orders \(1,2,3\) cannot satisfy
  \(\delta(G)\ge 3\).
- At order \(4\), the degree condition forces \(G=K_4\), which has a
  \(4\)-cycle.
- Equality \(\delta(G)=3\) is included and is expected to contain the sparse
  extremal cases.
- Disconnected graphs are included. Every connected component of such a graph
  separately has minimum degree at least \(3\), so one component suffices.
- Loops and pairs of parallel edges are excluded; otherwise cycles of lengths
  \(1\) and \(2\) would require separate conventions.

## Provenance

The user supplied the name “Erdős–Gyárfás conjecture.” The formulation above is
the conventional graph-theoretic formulation selected for this dossier. No
original paper, later survey, claimed proof, or current-status source was
inspected during intake. Accordingly, `prior_proof_status` remains `unknown`;
source correspondence is a separate open provenance task and supplies no premise
for the present deductions.

## Revision history

| Version | Date | Change | Decision |
|---|---|---|---|
| 0.1 | 2026-07-23 | Initial intake statement. | Initial creation |
