# S003 — Review lifecycle automation

- Date: 2026-07-23
- Problem: `P-001`

## Starting checkpoint

- Statement version: 0.2
- Work / claim status: `candidate` / `proof_candidate`
- Strongest established facts: the self-contained `L001`–`L005` argument in
  `PROOF.md`, not yet independently reviewed
- Open obligations in scope: `G003` (required reviews); `G004` (separate,
  optional reference comparison)
- Session goal: make adversarial review agent-owned rather than a human-operated
  checklist, then apply that lifecycle to the current candidate
- Falsifiable next move: have a fresh reviewer find a statement, logic, or
  counterexample defect in the candidate

## Work performed

- Added `proofctl review <slug> <title> --type <type>`. It accepts only a
  `proof_candidate`, creates a fresh-context review record, moves work to
  `review`, and sets an explicit next action.
- Added a validation gate preventing the `review` work state without a review
  record, plus tests for the new command and gate.
- Added mandatory lifecycle instructions to `AGENTS.md` and `process/workflow.md`:
  when a candidate appears, the agent—not the human—must start and delegate the
  appropriate fresh-context audits.
- Applied the lifecycle to `P-001`: `R001` audited statement correspondence and
  logic; `R002` audited hypotheses and counterexamples. Each reviewer initially
  received only `STATEMENT.md` and `PROOF.md`.

## Results

- `R001` found no critical or major flaw. It found one minor omission: the
  invariance calculation in Step 6 used adjacency-matrix symmetry without saying
  that it follows from undirectedness. `PROOF.md` now states this explicitly.
- `R002` found no critical, major, or minor flaw; its two clarity suggestions are
  nonblocking notes.
- The exact statement now has a self-contained proof that meets the repository's
  two-distinct-review promotion requirement. No source, computation, or imported
  theorem was used.

## Failed routes and why

No mathematical route failed in this session. The original test fixture assumed a
repository with no dossiers; it was isolated from the live fixture so its `P-001`
assertion remains deterministic.

## Adversarial check

The logic reviewer and hypotheses/counterexample reviewer were fresh contexts and
were instructed not to read discovery records or each other's material before
their verdicts. Their findings are recorded in `R001` and `R002`.

## Canonical records changed

- [ ] `STATEMENT.md`
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

- Current frontier: proved internal result, with two distinct completed
  fresh-context reviews
- Remaining blockers: none for the exact internal statement; reference comparison
  remains optional and separately authorized
- Best next action: none required; retain the dossier for optional future
  provenance comparison
- Files a new session should read: `STATE.md`, `PROOF.md`, `R001`, and `R002`

## Plain-language recap

The process now treats a proof candidate as the start of a review job, not as a
signal for the human to remember what to do next. When the current graph proof
reached that point, the agent created two independent checks automatically. One
reviewer noticed a small omitted explanation and it was fixed; neither found a
substantive error. The result is now supported by both the proof itself and two
separate attempts to break it.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 100%
- Previous estimate, if any: 95%
- Reason for change: the self-contained candidate passed two distinct
  fresh-context adversarial reviews, with its only minor finding repaired.
- Basis: no conclusion-blocking obligation, imported result, or essential
  computation remains. This is a research judgment about the completed dossier,
  not additional mathematical evidence.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
