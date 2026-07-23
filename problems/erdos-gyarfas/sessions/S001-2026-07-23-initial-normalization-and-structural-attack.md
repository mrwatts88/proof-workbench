# S001 — Initial normalization and structural attack

- Date: 2026-07-23
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1 intake wording
- Work / claim status: `intake` / `open`
- Strongest established facts: none beyond the supplied informal statement
- Open obligations in scope: `G001`, statement normalization
- Session goal: fix an exact target, search first for boundary failures, and
  derive the first reusable counterexample constraints
- Falsifiable next move: test whether the absence of the required \(4\)-cycle,
  together with minimum degree \(3\), rules out all sufficiently small orders

## Work performed

- Normalized the graph category, cycle convention, quantifiers, negation, and
  boundary cases in `STATEMENT.md`.
- Opened `A001` and proved:
  - `L001`, a leaf-block reduction to a 2-connected graph with at most one
    internal degree-\(2\) vertex;
  - `L002`, the independent-high-degree-vertices structure of an edge-minimal
    counterexample;
  - `L003`, the exact lower bound \(|V(G)|\ge9\) for any counterexample;
  - `L004`, the forbidden Mersenne-index chords at longest-path endpoints.
- Created `E001`, a dependency-free deterministic census. It enumerated all
  labelled simple graphs of minimum degree at least \(3\) through order \(7\)
  and all labelled cubic graphs through order \(8\).
- Performed no web search, source inspection, claimed-solution comparison, or
  imported-theorem use.

## Results

- Proved `L001`–`L004` in `A001`.
- Resolved intake obligation `G001`.
- Exact computation `E001` found no counterexample in either finite search
  space; this is recorded only as tested evidence `C002`.
- The hand proof of `L003` independently excludes every eligible graph through
  order \(8\), so it is not contingent on the program.
- No proof or disproof candidate for `C001` exists.
- Attribution, current external status, and known partial results remain
  unverified (`G004`).

## Failed routes and why

- Edge minimality initially looked capable of forcing a cubic counterexample,
  but the valid conclusion is weaker: each edge has a cubic endpoint, while
  vertices of degree at least \(4\) may persist as an independent set.
- A leaf block is nearly suitable for recursive application, but its unique cut
  vertex can have degree only \(2\) inside the block.
- Longest-path endpoints create several cycles, but their neighbor positions
  need not hit \(2^k-1\).
- The common-neighbor double count is decisive through order \(8\) and then
  loses enough slack that it does not by itself address arbitrary order.

## Adversarial check

- Removed a vacuous-quantifier ambiguity at order \(0\) by defining minimum
  degree only for nonempty graphs and quantifying over nonempty vertex sets.
- Checked the bridge-block edge case in `L001`: a leaf bridge would force a
  degree-\(1\) non-cut endpoint.
- Checked that deleting an edge in `L002` preserves minimum degree only when
  both endpoints originally have degree at least \(4\).
- Recounted `L003` as incidences \((v,\{x,y\})\), ensuring each unordered
  vertex pair has at most one common neighbor exactly because \(C_4\) is absent.
- Audited the order-eight parity step and both possible induced graphs on a
  three-vertex neighborhood.
- Cross-checked the cubic generator against the general graph enumerator at
  orders \(4\) and \(6\), where both found respectively \(1\) and \(70\)
  labelled cubic graphs.
- Added detector assertions on \(C_4,C_6,C_8\).
- This was a discovery-session self-audit, not an independent adversarial
  review and not evidence that the main conjecture is solved.

## Canonical records changed

- [x] `STATEMENT.md`
- [x] `STATE.md`
- [x] `CLAIMS.md`
- [x] `OBLIGATIONS.md`
- [x] `PROOF.md`
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: any counterexample has order at least \(9\), admits the
  2-connected near-minimum-degree reduction `L001`, and in an edge-minimal form
  has the local structure `L002`.
- Remaining blockers: `G002` and `G003`, the missing global cycle-forcing step;
  `G004`, source/literature audit; `G005`, a larger auditable census.
- Best next action: generate exactly the \(C_4\)-free minimum-degree-\(3\)
  graphs starting at order \(9\), retain those also avoiding an \(8\)-cycle,
  and test sharpenings of the block and longest-path lemmas against them.
- Files a new session should read: `STATEMENT.md`, `STATE.md`, `CLAIMS.md`,
  `OBLIGATIONS.md`, `A001`, `E001/README.md`, and this session.

## Plain-language recap

The conjecture now has an exact target and the first verified footholds. If a
counterexample exists, it can be narrowed to a highly connected piece where
almost every vertex still has at least three neighbors. A smallest
counterexample cannot place two high-degree vertices next to each other, and a
direct counting argument proves it needs at least nine vertices. An exhaustive
small computation agrees with that hand proof. What remains is the hard part:
none of these local restrictions yet forces a cycle whose length is exactly
\(8,16,\) or another power of two in an arbitrarily large graph.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 3%
- Previous estimate, if any: none
- Reason for change: this is the first estimate after intake
- Basis: the project has a clean lower boundary, exact reductions, and a
  falsifiable next experiment, but no global mechanism yet controls the sparse
  target set of cycle lengths. The literature has also not yet been audited, so
  both the available routes and the true novelty of these lemmas remain
  uncertain.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
