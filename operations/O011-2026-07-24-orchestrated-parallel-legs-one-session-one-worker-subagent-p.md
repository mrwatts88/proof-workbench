# O011 — orchestrated parallel legs: one session, one worker subagent per route

- Date: 2026-07-24
- Classification: repository operation (not mathematical research)

## Scope

Correct the parallel-work protocol. `O010` wrote `process/concurrency.md`
around two interactive sessions as the primary model; the user directed
(2026-07-24, during S019 setup) that where the harness supports delegation the
correct model is **orchestration**: one session orchestrates and each parallel
leg runs in its own worker subagent, so there is one session record, one
ledger holder, and one canonical checkpoint. Affected files: `AGENTS.md`
(Parallel sessions), `process/concurrency.md`, `process/harness.md`
(capability matrix), `CLAUDE.md` (harness note), `PROJECT_STATE.md` (one
decision bullet). No problem dossier's mathematical content is touched; the
concurrent research session S019 records its own use of the new mode
separately.

## Work performed

- `AGENTS.md`: added the orchestrated-mode paragraph to *Parallel sessions* —
  workers are not sessions, write only assigned owned records, never ledgers
  or statuses or commits, leave no `S###` record, and their reports are
  working input, not citable records; two interactive sessions demoted to
  fallback (delegation unavailable, or a human deliberately runs the second).
- `process/concurrency.md`: new *Two modes* and *Orchestrated mode* sections
  (orchestrator duties: resume protocol, ID-block allocation before launch,
  ledger hold, per-worker scope/epistemic rules, audit-before-integration,
  single checkpoint, worker-death handling, explicit per-worker model
  choice); scoped the ID-allocation/isolation/ledger/declaration sections to
  the two-session fallback; split the checklist by mode.
- `process/harness.md`: parallel-mode capability matrix per harness — Claude
  Code default is orchestrated via the Agent tool with no worktree needed;
  two sessions with worktrees as fallback; Codex orchestrates when
  collaboration subagents are exposed.
- `CLAUDE.md`: harness note *Parallel legs are orchestrated here* — launch
  one `general-purpose` worker per leg with the Agent tool, pass the `--id`
  block, reading list, file ownership, and ledger prohibition verbatim;
  worker model floor (user directive 2026-07-24): Opus at a minimum
  (`model: "opus"`), Fable when the leg warrants it, never below Opus; the
  GPT-harness equivalent floor (GPT-5.6 Soul) is recorded in
  `process/harness.md`.
- `PROJECT_STATE.md`: appended the orchestrated-mode sentence to the
  parallel-work decision bullet.
- Cleanup of the superseded two-session setup created earlier in S019 before
  the user's correction: worktree `../rh-agent-b` removed, branch
  `s020-r2-carr` deleted (never used, no commits). The S020/A020/E017/R003
  sibling ID block is reassigned by S019 under the new mode.

Design choice: orchestrated mode is written harness-neutrally in `AGENTS.md`
and `process/concurrency.md` ("when the harness supports delegation"), with
harness mechanics (Agent tool, model parameter) confined to `CLAUDE.md` and
`process/harness.md`, preserving the O006/O010 layering rule.

## Verification

- `python3 -m unittest discover -s tests -q` — 12 tests, OK (pytest is not
  installed for the system Python; the suite is unittest-based).
- `python3 scripts/proofctl.py validate` — pass (2 problem dossiers).
- `git worktree list` shows only the main tree; `git branch` shows no
  `s020-r2-carr`.
- Inspection: `CLAUDE.md` still imports `AGENTS.md` and restates no contract
  rule; the two-session fallback text in `process/concurrency.md` is intact
  under its scoping note.

## Dossier impact

None mathematically. No statement, claim, obligation, proof, review, or
status changed. Research session S019 (P-002), which runs concurrently,
declares its worker allocation in its own record; that is research bookkeeping
outside this operation.

## Handoff

- Result: parallel legs are orchestrated by a single session wherever
  delegation exists; two interactive sessions are now an explicit fallback
  with the same partition rules as before.
- Remaining operational follow-up: optional — a dedicated
  `.claude/agents/proof-worker.md` definition baking the file-discipline into
  a worker agent type (deferred: agent definitions load at session start, so
  it could not serve the currently running session; inline prompts carry the
  discipline meanwhile).
- Files a later operator should read: `process/concurrency.md` (*Two modes*,
  *Orchestrated mode*), `CLAUDE.md` (*Parallel legs are orchestrated here*).
- Commit and push status: committed and pushed as the operational commit for
  O011 (see repository history).
