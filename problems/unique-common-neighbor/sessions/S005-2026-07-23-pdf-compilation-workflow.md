# S005 — PDF compilation workflow

- Date: 2026-07-23
- Problem: `P-001`

## Starting checkpoint

- Statement version: 0.2
- Work / claim status: `complete` / `proved`
- Strongest established facts: reviewed proof and LaTeX source, with no PDF gate
  previously encoded
- Open obligations in scope: none for the theorem
- Session goal: require a reproducible compiled PDF for proved results and
  backfill the current dossier
- Falsifiable next move: compile `papers/unique-common-neighbor.tex` through the
  agent-facing workflow and validate the recorded artifact

## Work performed

- Found Tectonic 0.16.9 already installed at `/opt/homebrew/bin/tectonic`; this is
  the modern single-executable LaTeX system likely intended by the user.
- Added `proofctl.py typeset <slug>`, which invokes Tectonic, writes a PDF to the
  source's `build/` directory, records `pdf_file` and `latex_engine`, and refreshes
  the README dashboard.
- Made `pdf_file` and `latex_engine` manifest fields, added them to new dossiers,
  and made validation reject `proved` status without an existing PDF.
- Compiled `papers/build/unique-common-neighbor.pdf` successfully, retaining the
  PDF as a committed artifact and ignoring only the reproducible build log.

## Results

- The dashboard now links to both the PDF and TeX source for the completed proof.
- The compiler and exact version are recorded in `problem.json` as
  `Tectonic 0.16.9`.
- The initial sandboxed Tectonic run failed while accessing its resource bundle;
  the authorized rerun succeeded and downloaded only required TeX resources.

## Failed routes and why

The first compile attempt failed because the sandbox prevents Tectonic's resource
bundle access; the same command succeeded with the authorized network permission.
This is an environment permission issue, not a TeX or proof failure.

## Adversarial check

Ran `proofctl typeset unique-common-neighbor`, verified the expected PDF exists,
then ran validation. The compiler output confirms TeX and PDF conversion completed.

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

- Current frontier: complete proof with source, compiled PDF, recorded compiler,
  and validator-enforced publication artifacts
- Remaining blockers: none
- Best next action: no research action required
- Files a new session should read: `STATE.md`, `PROOF.md`, the PDF, and
  `process/proof-standard.md`

## Plain-language recap

The proof is now an actual shareable PDF, not just a file that could be compiled
later. Future agents use one normal command to make that PDF and cannot mark a
proof finished if the PDF is missing. The README makes both versions easy to find.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 100%
- Previous estimate, if any: 100%
- Reason for change: this session strengthened the reproducibility and
  publication artifacts without changing the reviewed mathematics.
- Basis: Tectonic compiled the exact reviewed source successfully and validation
  now checks the committed PDF artifact.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
