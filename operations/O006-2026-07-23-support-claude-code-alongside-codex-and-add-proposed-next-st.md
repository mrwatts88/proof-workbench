# O006 — Support Claude Code alongside Codex and add proposed-next-step to closings

- Date: 2026-07-23
- Classification: repository operation (not mathematical research)

## Scope

Two unrelated process changes.

1. Make the framework workable from either Codex or Claude Code. The contract was
   already almost entirely harness-neutral in wording, but nothing loaded it in
   Claude Code and nothing said how a harness with real delegation should satisfy
   the fresh-context review requirement.
2. Add a third required element to the closing response of a substantive research
   session: the proposed next step, in plain language.

No problem dossier was opened, and no mathematical statement, claim, obligation,
proof, review, or status changed.

## Work performed

### Harness portability

- Added `CLAUDE.md` as the Claude Code entry point. It imports the contract with
  `@AGENTS.md` and holds only harness-specific notes. The contract stays in
  `AGENTS.md`; the alternative of copying it into `CLAUDE.md` was rejected because
  two copies drift silently and the validator cannot detect drifted meaning.
- Added `process/harness.md` with the capability matrix: entry points, delegation
  and independence modes per harness, permission and sandbox notes, and the rule
  that harness-specific shortcuts may only be thin wrappers over `process/`.
- Added `.claude/agents/proof-reviewer.md`. This turns the reviewer-isolation rule
  from honor-system prose into a real context boundary: the subagent starts from
  `STATEMENT.md` and `PROOF.md` and is instructed not to read `attempts/`,
  `sessions/`, or prior `reviews/` before its first verdict. It cannot edit
  canonical records.
- Added `.claude/settings.json` allowlisting the commands the mandatory
  end-of-session checkpoint requires, including the commit and push. Without it a
  denied prompt leaves a session the contract considers unclosed. Force-push and
  hard reset are denied. `.claude/settings.local.json` is now git-ignored.
- Tightened the four places that hedged on delegation (`AGENTS.md`,
  `process/workflow.md` twice, `PROJECT_STATE.md`). Delegation is now mandatory
  where the harness supports it; the "when available" exemption survives only for
  harnesses that genuinely lack it.
- Recorded that a summarized or compacted context is **not** a fresh context, in
  `AGENTS.md`, `process/workflow.md`, `templates/review.md`, and `CLAUDE.md`. This
  gap was previously unstated and would have let a compacted session claim
  independence.
- Replaced the review record's fixed independence string with a recorded mode:
  `proofctl.py review --independence <delegated-subagent|clean-session|
  same-context-limited>`, defaulting to delegation. Choosing
  `same-context-limited` prints a warning that the audit cannot support promotion.
- `validate` now requires `CLAUDE.md` and `process/harness.md` to exist, and
  requires `CLAUDE.md` to still contain the `@AGENTS.md` import.

### Proposed next step in closings

- `AGENTS.md` closing response now requires a third element after the recap and
  the resolution estimate: the concrete next move, what it would establish or rule
  out, and any alternative deferred. It must match the next action already stored
  in `problem.json` and `STATE.md`; on disagreement the records are repaired
  rather than the message.
- Mirrored in `process/workflow.md` step 11, `templates/session.md` (new
  "Proposed next step" section), `PROJECT_STATE.md`, and `README.md`.

The next action already existed in the records and in the session template's
ending checkpoint. This change surfaces it in the closing message, in the same
plain language as the recap.

## Verification

- `python3 -m unittest discover -s tests` passes, including two new tests:
  `CLAUDE.md` losing its import fails validation, and a review records the
  independence mode it was given.
- `python3 scripts/proofctl.py validate` passes.
- `python3 scripts/proofctl.py index` leaves the dashboard unchanged, as expected
  for operational work.

Not verified by automation: whether a delegated subagent actually honors the
isolation instruction in practice. That remains a reasoning discipline, as
`PROJECT_STATE.md` already notes for independent review generally. The subagent
narrows the opportunity for contamination; it does not eliminate it.

## Dossier impact

None. Both existing dossiers are untouched. The next closing of a substantive
session in either one will include the proposed next step, and any future
adversarial review will record its independence mode.

## Handoff

- Result: the framework is now loadable and workable from either harness, with
  fresh-context review strengthened rather than merely permitted, and closings
  report what is coming next.
- Remaining operational follow-up: none required. Optional — if Codex later gains
  project-level prompt support, add thin wrappers there mirroring the natural
  language triggers, without moving any process into them.
- Files a later operator should read: `AGENTS.md`, `CLAUDE.md`,
  `process/harness.md`, and `.claude/agents/proof-reviewer.md`.
- Commit and push status: included in this operation's closure commit and push.
