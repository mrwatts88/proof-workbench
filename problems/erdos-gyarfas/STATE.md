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

## Evidence, not proof

- `E001` exhaustively found no counterexample among all labelled eligible graphs
  through order \(7\), or among labelled cubic graphs through order \(8\). This
  is consistent with, but logically unnecessary for, `L003`.

## Open obligations

- `G002`: make the 2-connected near-minimum-degree reduction decisive.
- `G003`: force an \(8\)-, \(16\)-, or longer power-of-two cycle from the local
  restrictions.
- `G004`: verify source correspondence and audit the literature.
- `G005`: extend exact \(C_4\)-free enumeration from order \(9\).

## Active risks

- No current lemma controls cycle lengths globally; all progress is local or
  small-order.
- Edge minimality does not imply cubicity, and the leaf-block reduction may
  introduce one degree-\(2\) vertex.
- External provenance and known partial results have not been checked.
- Finite enumeration cannot establish the universal statement.

## Best next action

Build an exact backtracking generator for \(C_4\)-free minimum-degree-\(3\)
graphs starting at order \(9\), retain auditable survivors that also avoid an
\(8\)-cycle, and use them to test a sharpened block or longest-path lemma.

## Human-level state

The project has begun with a precise target and several verified reductions.
We now know that a counterexample cannot be tiny and that a minimal one has
strong local restrictions. These facts do not yet approach a full proof: the
missing step is to turn local sparsity into a cycle whose length is exactly a
power of two.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 3%
- Basis: there is now a clean reduction frontier and a falsifiable computational
  next move, but the established lemmas are elementary local constraints and no
  mechanism yet reaches arbitrary cycle lengths. The estimate is especially
  provisional because the literature has not been audited.

## Resume reading

1. `STATEMENT.md`
2. `CLAIMS.md`
3. `OBLIGATIONS.md`
4. `attempts/A001-minimal-counterexample-and-block-reductions.md`
5. `experiments/E001-small-cubic-graph-census/README.md`
6. `sessions/S001-2026-07-23-initial-normalization-and-structural-attack.md`
