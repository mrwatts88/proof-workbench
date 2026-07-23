# S004 — LaTeX publication and live dashboard

- Date: 2026-07-23
- Problem: `P-001`

## Starting checkpoint

- Statement version: 0.2
- Work / claim status: `complete` / `proved`
- Strongest established facts: self-contained reviewed proof in `PROOF.md`, with
  completed fresh-context audits `R001` and `R002`
- Open obligations in scope: none for the exact statement; reference comparison
  remains optional and unperformed
- Session goal: make LaTeX and a live, provenance-aware README dashboard part of
  normal agent workflow, then backfill the completed dossier
- Falsifiable next move: run validation and tests after enforcing an existing
  LaTeX source for every `proved` manifest

## Work performed

- Added `prior_proof_status` and `latex_file` to every dossier manifest and the
  new-dossier template.
- `proofctl.py index` now regenerates both `problems/INDEX.md` and the live table
  in `README.md`; validation rejects a stale README dashboard.
- Validation now requires a `proved` dossier to name an existing `.tex` source.
- Added `papers/unique-common-neighbor.tex`, a standalone rendering of the exact
  statement version 0.2 and its reviewed proof.
- Updated agent and process instructions so agents record provenance at intake,
  produce LaTeX at proof completion, and keep the dashboard current themselves.

## Results

- The README now reports the current work and claim status, whether a prior proof
  is unknown, reported, or verified, and links to a LaTeX source when available.
- The current theorem is backfilled as “Reported (not inspected),” preserving the
  distinction between user-reported external provenance and the internal proof.
- `pdflatex` is not installed in this environment, so no PDF build was claimed.
  The source is present and validator-enforced.

## Failed routes and why

No mathematical approach failed. The environment lacks a local LaTeX compiler;
the process therefore retains and validates source files while requiring a build
only when a toolchain is available.

## Adversarial check

Validation checked the manifest-to-source link and stale-dashboard detection.
The complete test suite checked creation, status, review, and index behavior.

## Canonical records changed

- [ ] `STATEMENT.md`
- [x] `STATE.md`
- [ ] `CLAIMS.md`
- [ ] `OBLIGATIONS.md`
- [ ] `PROOF.md`
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: a complete reviewed proof with a standalone LaTeX source and
  automatically maintained live dashboard
- Remaining blockers: none for the exact theorem; PDF compilation awaits only a
  future environment with a LaTeX toolchain
- Best next action: no research action required
- Files a new session should read: `STATE.md`, `PROOF.md`, `R001`, `R002`, and
  `../../papers/unique-common-neighbor.tex`

## Plain-language recap

The proof is now available in two useful forms: the detailed research record and
a clean LaTeX document that can be shared or compiled later. The main README also
acts as a live scoreboard: it shows what is being worked on, what is settled, and
whether an earlier proof is merely reported or actually verified. Agents update
that scoreboard as part of their normal process, so it is not another task for a
human to remember.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 100%
- Previous estimate, if any: 100%
- Reason for change: documentation and publication artifacts were added; the
  reviewed mathematical status did not change.
- Basis: the theorem remains complete with its two distinct reviews; LaTeX source
  and dashboard tracking improve accessibility and continuity, not proof strength.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
