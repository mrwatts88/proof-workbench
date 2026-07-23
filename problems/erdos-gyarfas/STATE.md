# Current state

- Last updated: 2026-07-23
- Problem: `P-002` — Erdős–Gyárfás Conjecture

## Exact target

Every finite simple undirected graph of minimum degree at least \(3\) contains a
cycle whose length is a power of two. See normalized `STATEMENT.md` version 0.1.

## Established

- `L001`: any counterexample contains a 2-connected power-cycle-free block with
  at most one vertex of internal degree \(2\), all others having internal degree
  at least \(3\).
- `L002`: in an edge-minimal counterexample, every edge has a degree-\(3\)
  endpoint; high-degree vertices are independent.
- `L003`: exact counting and an order-eight case analysis prove that every
  counterexample has at least nine vertices.
- `L004`: chords from an endpoint of a longest path avoid positions
  \(3,7,15,\ldots\).
- `L005` and `L006`: exact degree/codegree arguments and a complete structural
  classification prove that every counterexample has at least eleven vertices.
- These internal finite bounds are weaker than previously reported
  computational bounds and are not claimed as novel.

## Evidence, not proof

- `E001` exhaustively found no counterexample among all labelled eligible graphs
  through order \(7\), or among labelled cubic graphs through order \(8\). This
  is consistent with, but logically unnecessary for, `L003`.
- `E002` exhaustively generated the necessary edge-minimal degree patterns at
  orders \(9\) and \(10\); it found no order-\(9\) \(C_4\)-free completion and
  found that every order-\(10\) completion has an \(8\)-cycle. `L005` and `L006`
  have independent hand proofs.

## Imported frontier

- `C004`–`C006` (Carr, 2026): in an order-then-size minimal counterexample,
  every proper subgraph has a vertex of degree at most \(2\), every vertex has
  a cubic neighbor, and at least \(4/7\) of all vertices are cubic.
- `C007` (Hegde–Sandeep–Shashank, 2025): every counterexample contains an
  induced \(P_{13}\).
- `C008` (Liu–Montgomery, 2023): a sufficiently large absolute
  average-degree threshold forces a power-of-two cycle.
- The inspected May 2026 primary preprint reports that the general conjecture
  remains open. See `references/source-audit-2026-07-23.md`.

## Open obligations

- `G002`: make the 2-connected near-minimum-degree reduction decisive.
- `G003`: force an \(8\)-, \(16\)-, or longer power-of-two cycle from the local
  restrictions.
- `G004`: inspect the original 1997 article body and original sources for
  reported computational bounds.
- `G006`: make the induced-\(P_{13}\)/cubic-domination route decisive.

## Active risks

- No current lemma controls cycle lengths globally; all progress is local or
  small-order.
- Edge minimality does not imply cubicity, and the leaf-block reduction may
  introduce one degree-\(2\) vertex.
- The internal order-\(11\) bound is below reported prior computational
  frontiers, so continuing by order alone is not competitive.
- The \(P_{13}\)-free result is computer-assisted and its external computation
  was inspected but not reproduced here.
- Imported high-average-degree methods do not directly apply at minimum degree
  \(3\).

## Best next action

Fix an induced path \(P=v_1\ldots v_{13}\) in a minimal counterexample, encode
the attachment of the cubic dominating set to \(P\), and test the precise
claim that every attachment pattern consistent with no \(C_4\) and no \(C_8\)
already forces a \(C_{16}\). A surviving finite pattern would falsify this
route before attempting a general proof.

## Human-level state

The project now has a fully checked proof that a counterexample needs at least
eleven vertices, but the literature already reaches farther computationally.
The more important gain is a better global target: any minimal counterexample
is mostly cubic, every vertex touches a cubic vertex, and it must contain a long
induced path. The next attack will test whether those two facts together force
a \(16\)-cycle.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Basis: the session added two correct finite exclusions and identified a
  scalable induced-path route, but the literature audit shows that stronger
  finite computation and substantial special-class results already exist
  without resolving the general problem. No new global mechanism is yet in
  hand.

## Resume reading

1. `STATEMENT.md`
2. `CLAIMS.md`
3. `OBLIGATIONS.md`
4. `attempts/A002-order-nine-exclusion-via-degree-and-codegree-budgets.md`
5. `attempts/A003-order-ten-structural-classification.md`
6. `experiments/E002-c4-free-degree-sequence-frontier/README.md`
7. `references/source-audit-2026-07-23.md`
8. `sessions/S002-2026-07-23-exact-c4-free-frontier-and-survivor-analysis.md`
