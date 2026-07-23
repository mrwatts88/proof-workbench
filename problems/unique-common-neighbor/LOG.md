# Research log

Append brief dated checkpoints. Detailed reasoning belongs in a linked session,
attempt, experiment, or review record.

## 2026-07-23 — Dossier created

- Created `P-001`.
- Work status: `intake`; claim status: `open`.
- Next: normalize the statement and complete an intake session.

## 2026-07-23 — S001 intake completed

- Normalized the target as `STATEMENT.md` version 0.2, explicitly taking the
  finite vertex set to be nonempty.
- Checked the empty, one-, two-, and three-vertex boundary behavior.
- Recorded the benchmark solution embargo and deferred reference comparison.
- Kept claim status `open`; no proof attempt, external search, or reference
  inspection occurred.
- Next: open `A001` for an independent falsification and structural pass.

## 2026-07-23 — S002 produced first integrated proof candidate

- In `A001`, proved even degree, degree equality across nonedges, complement
  connectivity under the counterexample assumption, and resulting regularity.
- Ruled out the regular counterexample with a self-contained adjacency-matrix
  and trace argument.
- Integrated the dependency chain as a proof candidate in `PROOF.md`.
- No known solution, external source, computation, or imported theorem was used.
- Moved workflow to `candidate` and claim status to `proof_candidate`.
- Next: conduct a clean-context statement-correspondence and line-by-line logic
  review.

## 2026-07-23 — S003 automated and completed adversarial review

- Added the `proofctl review` lifecycle command and made candidate-to-review
  delegation mandatory for agents.
- `R001` passed after a minor explicit symmetry repair in the matrix argument.
- `R002` passed the independent hypotheses and counterexample audit.
- Resolved `G003`; the deferred reference comparison is optional and was not
  performed. The internal result is ready for `complete` / `proved` promotion.

## 2026-07-23 — S004 added LaTeX publication and live status tracking

- Added the standalone reviewed source `papers/unique-common-neighbor.tex`.
- Added provenance-aware dashboard fields and generated the live README table.
- Made LaTeX source mandatory for `proved` dossiers; no local LaTeX compiler was
  available, so no PDF build is represented.
