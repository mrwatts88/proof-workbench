# Unique Common Neighbor

- Problem ID: `P-001`
- Statement version: 0.2
- Last changed: 2026-07-23

## Exact statement

Let G be a finite simple undirected graph such that every two distinct vertices have exactly one common neighbor. Prove that G has a vertex adjacent to every other vertex.

## Definitions and conventions

- `D001` — A finite simple undirected graph is a pair \(G=(V,E)\), where
  \(V\) is a finite, nonempty set and \(E\) is a set of two-element subsets of
  \(V\). Thus loops and multiple edges are excluded.
- `D002` — For \(v\in V\), the open neighborhood is
  \(N(v)=\{w\in V:\{v,w\}\in E\}\).
- `D003` — A common neighbor of distinct vertices \(u,v\) is an element of
  \(N(u)\cap N(v)\).
- `D004` — A vertex \(c\in V\) is adjacent to every other vertex if
  \(\{c,v\}\in E\) for every \(v\in V\setminus\{c\}\). No loop at \(c\) is
  required.

## Hypotheses

1. \(G=(V,E)\) is a finite simple undirected graph in the sense of `D001`.
2. For every pair of distinct vertices \(u,v\in V\),
   \(\lvert N(u)\cap N(v)\rvert=1\).

## Quantifier form

For every pair \(G=(V,E)\) satisfying `D001`, if
\[
  \forall u,v\in V,\quad
  u\ne v\Longrightarrow \lvert N(u)\cap N(v)\rvert=1,
\]
then
\[
  \exists c\in V\ \forall v\in V\setminus\{c\},\quad \{c,v\}\in E.
\]

## Negation

There exists a finite simple undirected graph \(G=(V,E)\) satisfying the
unique-common-neighbor hypothesis such that
\[
  \forall c\in V\ \exists v\in V\setminus\{c\},\quad \{c,v\}\notin E.
\]

## Boundary and degenerate cases

- Empty/zero case: excluded by `D001`. If empty graphs were admitted, the
  hypothesis would hold vacuously and the existential conclusion would fail;
  the nonempty convention is therefore mathematically consequential.
- Singleton/unit case: the hypothesis and conclusion both hold vacuously, so the
  one-vertex graph satisfies the statement.
- Two-vertex case: no such graph satisfies the hypothesis, because two vertices
  cannot have a common neighbor in a loopless graph on only those vertices.
- Smallest nonvacuous example: \(K_3\) satisfies the hypothesis, and each of its
  vertices satisfies the conclusion.

## Provenance

The user supplied the statement on 2026-07-23 and reported that it is externally
known to be solved. As a historical fact, no source or known solution was
searched for, inspected, or cited during intake or development; the dossier was
worked under a since-retired internal-only rule. That rule was scrapped
repository-wide in `O008`: external sources are freely usable through the
import rules, and comparison with a reference solution is simply optional.

## Revision history

| Version | Date | Change | Decision |
|---|---|---|---|
| 0.1 | 2026-07-23 | Initial intake statement. | Initial creation |
| 0.2 | 2026-07-23 | Made graph conventions, quantifiers, negation, and boundary cases explicit; retained the supplied displayed statement verbatim apart from mathematical typography. | See `DECISIONS.md` |
