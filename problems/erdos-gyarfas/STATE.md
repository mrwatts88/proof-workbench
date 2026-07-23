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
- `L007`: the current induced-\(P_{13}\)/cubic-domination bundle cannot force a
  \(16\)-cycle, even after assuming no \(4\)- or \(8\)-cycle.
- The finite bounds `L003`, `L005`, and `L006` are weaker than previously
  reported computational bounds and are not claimed as novel.

## Evidence, not proof

- `E001` exhaustively found no counterexample among all labelled eligible graphs
  through order \(7\), or among labelled cubic graphs through order \(8\). This
  is consistent with, but logically unnecessary for, `L003`.
- `E002` exhaustively generated the necessary edge-minimal degree patterns at
  orders \(9\) and \(10\); it found no order-\(9\) \(C_4\)-free completion and
  found that every order-\(10\) completion has an \(8\)-cycle. `L005` and `L006`
  have independent hand proofs.
- `E003` exhaustively ruled out the smallest 18-vertex completion made from an
  induced \(P_{13}\) and five independent cubic hubs. This narrow computation
  is not the proof of `L007`.

## Imported frontier

- `C004`–`C006` (Carr, 2026): in an order-then-size minimal counterexample,
  every proper subgraph has a vertex of degree at most \(2\), every vertex has
  a cubic neighbor, and at least \(4/7\) of all vertices are cubic.
- `C007` (Hegde–Sandeep–Shashank, 2025): every counterexample contains an
  induced \(P_{13}\).
- `C008` (Liu–Montgomery, 2023): a sufficiently large absolute
  average-degree threshold forces a power-of-two cycle.
- `C009` (Biggs, 1998): finite Hamiltonian cubic graphs exist with arbitrarily
  large prescribed girth.
- The inspected May 2026 primary preprint reports that the general conjecture
  remains open. See `references/source-audit-2026-07-23.md`.

## Open obligations

- `G002`: make the 2-connected near-minimum-degree reduction decisive.
- `G003`: force an \(8\)-, \(16\)-, or longer power-of-two cycle from the local
  restrictions.
- `G004`: inspect the original 1997 article body and original sources for
  reported computational bounds.
- `G007`: find a global restriction on a minimal counterexample that is not
  shared by arbitrary connected cubic graphs of girth at least \(17\).

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
- Cubic domination, cubic density, and proper-subgraph minimality place no
  extra restriction on connected cubic graphs; large-girth cubic graphs show
  that these facts plus an induced \(P_{13}\) do not force \(C_{16}\).

## Best next action

Derive a genuinely global consequence of counterexample minimality or of the
absence of all power-of-two cycles, beyond `C004`–`C007`, and test it first on
the Hamiltonian cubic girth-\(17\) family from `L007`. Only a restriction that
excludes that family without assuming the desired conclusion should be used
in a new cycle-length forcing argument.

## Human-level state

The proposed next attack has been decisively stress-tested and rejected. Being
mostly cubic and containing a long shortcut-free path sounded restrictive, but
ordinary cubic graphs with no short cycles already have all of those features
and can avoid cycles of lengths \(4\), \(8\), and \(16\). The project must now
find a truly global property of a hypothetical counterexample rather than
classify attachments around one path.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 1%
- Basis: the session eliminated the best concrete local route by a rigorous
  large-girth obstruction. This prevents wasted work and clarifies the need for
  a global mechanism, but no replacement mechanism is yet in hand and the
  cubic case remains essentially untouched.

## Resume reading

1. `STATEMENT.md`
2. `CLAIMS.md`
3. `OBLIGATIONS.md`
4. `attempts/A004-limits-of-induced-p13-and-cubic-domination.md`
5. `experiments/E003-cubic-survivor-for-the-local-p13-route/README.md`
6. `references/source-audit-2026-07-23.md`
7. `sessions/S003-2026-07-23-falsify-the-induced-p13-and-cubic-domination-forcing-route.md`
