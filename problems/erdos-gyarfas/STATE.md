# Current state

- Last updated: 2026-07-23
- Problem: `P-002` — Erdős–Gyárfás Conjecture

## Exact target

Every finite simple undirected graph of minimum degree at least \(3\) contains a
cycle whose length is a power of two. See normalized `STATEMENT.md` version 0.1.

## Established

- `L001`–`L006`: block and edge-minimal reductions, a longest-path chord
  restriction, and independent proofs that every counterexample has at least
  eleven vertices.
- `L007`: cubic domination, cubic density, proper-subgraph minimality, an
  induced \(P_{13}\), and absence of \(C_4,C_8\) do not force \(C_{16}\).
- `L008`: a hypothetical counterexample can be enlarged on its fixed vertex set
  until every nonedge has a simple witness path of length \(2^k-1\). The
  resulting counterexample is connected, non-bipartite, and uniformly sparse.
- `L009`: this saturation condition fails on a connected bipartite cubic graph
  of girth at least \(17\), so it is not another property automatic in the
  large-girth obstruction family.
- `L010`: in a saturated counterexample, edges which lie on no odd cycle form a
  matching. Thus every vertex lies on an odd cycle, all bridges form a
  matching, and every nontrivial block is non-bipartite.
- `L011`: the saturation witnesses survive inside a 2-connected
  power-cycle-free leaf block, except for nonedges incident with its possible
  cut vertex.
- `L012`: if a shortest odd cycle in that block has length at least \(7\), a
  saturation witness forces an external ear.
- `L013`: 2-connectivity supplies an external ear for every shortest odd
  cycle, including triangles and \(5\)-cycles, but without a saturation-witness
  certificate in those short cases.
- `L014`: one arbitrary ear is not enough by length alone. Theta path lengths
  \(2,2r+1,4\) give cycle lengths \(2r+3,2r+5,6\), none powers of two.

## Evidence, not proof

- `E001`–`E003` provide exact finite checks only. The order-\(11\) lower bound
  has separate hand proofs, and the 18-vertex attachment search is not support
  for the universal claim.

## Imported frontier

- `C004`–`C006` (Carr, 2026): proper-subgraph minimality, cubic domination, and
  at least \(4/7\) cubic vertices in an order-then-size minimal counterexample.
- `C007` (Hegde–Sandeep–Shashank, 2025): every counterexample contains an
  induced \(P_{13}\).
- `C008` (Liu–Montgomery, 2023): sufficiently large absolute average degree
  forces an interval of even cycle lengths and hence a power-of-two cycle.
- `C009` (Biggs, 1998): finite Hamiltonian cubic graphs exist with arbitrarily
  large prescribed girth.
- The May 2026 primary preprint inspected in `S002` reports that the general
  conjecture remains open.

## Open obligations

- `G002` and `G003`: make the 2-connected reduction and a global cycle-length
  mechanism decisive.
- `G004`: inspect the original 1997 article body and original sources for
  reported computational bounds.
- `G007`: turn the new saturation restriction into a power-of-two cycle; its
  separation from the large-girth cubic bundle is now proved.
- `G008`: control the ordered intersections of a full Mersenne-length witness
  with the shortest odd cycle; arbitrary one-ear equations are now ruled
  insufficient.

## Active risks

- Edge-maximal saturation is different from edge minimality; `L008` cannot
  silently reuse `L002` or the spanning-subgraph part of `C004`.
- A Mersenne-length witness for an induced two-edge path can pass through its
  middle vertex, and an external witness initially creates an odd cycle of
  length \(2^k+1\), not a forbidden power.
- `L012` supplies only one ear and says nothing yet about its length or its
  intersections with other witnesses.
- `L014` shows that shortest-cycle minimality plus one ear has infinite
  power-free length patterns.
- For a triangle or \(5\)-cycle, an ear exists but has not been placed inside a
  Mersenne-length witness.
- The Liu–Montgomery theorem operates above a large average-degree threshold,
  while any counterexample is below that threshold.

## Strategy portfolio

- Primary route: `A005`, edge-maximal saturation inside the leaf block from
  `L011`; retain the full `L012` witness and classify its ordered intersections
  with a shortest odd cycle.
- Live alternative: adapt the variable-length path/adjuster mechanism behind
  `C008` directly to the near-minimum-degree 2-connected graph from `L001`.
- Pivot trigger: if the one-component and two-component witness patterns both
  admit unconstrained infinite power-free length families, saturation has lost
  comparative advantage and the variable-path reframing should become primary.

## Best next action

Classify the `L012` Mersenne witness when its vertices outside the shortest odd
cycle form exactly one component, retaining the total length and every cycle
intersection; either force a power-of-two cycle or exhibit an infinite
surviving length family.

## Human-level state

The project now has a genuinely global condition that the previously used
large-girth degree-three examples do not automatically satisfy. In a maximally
filled hypothetical counterexample, every missing edge is certified by a path
whose length is one less than a power of two. Those certificates force odd
cycles throughout the graph and remain available inside the key 2-connected
piece. A shortest odd cycle always has an extra path leaving and returning to
it, and for cycles of length at least seven such a path occurs inside one of
the special certificates. However, the three cycle lengths formed by one
arbitrary extra path can all miss powers of two in infinitely many ways. The
next test must therefore keep the entire certificate, including every place it
meets the shortest odd cycle, rather than treating one extracted subpath in
isolation.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 1%
- Previous estimate: 1%
- Reason for no change: the session found a real global reduction and advanced
  it to a controlled witness-intersection question, but also proved that the
  first one-ear simplification is insufficient. No adjustable even length or
  contradiction has yet been obtained.

## Resume reading

1. `STATEMENT.md`
2. `CLAIMS.md`
3. `OBLIGATIONS.md`
4. `attempts/A005-edge-maximal-power-cycle-saturation.md`
5. `attempts/A004-limits-of-induced-p13-and-cubic-domination.md`
6. `references/source-audit-2026-07-23.md`
7. `sessions/S004-2026-07-23-audit-and-develop-a-global-saturation-route.md`
