# O010 — Concurrency protocol for parallel sessions on one dossier

- Date: 2026-07-24
- Classification: repository operation (not mathematical research)

## Scope

Process documentation and one tooling change, motivated by an unplanned live
test: on 2026-07-24 sessions `S016` and `S017` ran concurrently on `P-002` in a
single working tree. The partition held everywhere except the shared ledgers,
where `S017` had to notice `S016` mid-edit, defer its claim row, and apply the
bookkeeping in a follow-up commit. That worked because the second agent was
careful, not because anything enforced it. The user intends to run two agents in
the next session, so the protocol is written before rather than after the next
collision.

Affected systems: `AGENTS.md` (new *Parallel sessions* section),
`process/concurrency.md` (new), `process/harness.md` (isolation mechanisms per
harness), `PROJECT_STATE.md` (one repository-wide decision bullet),
`scripts/proofctl.py` (`add --id`), `tests/test_proofctl.py` (one new test).

No problem dossier is touched: `P-002`'s records, claims, obligations, proof,
status, and next action are exactly as `S018` left them, and no `S###` record was
created for this work.

## Work performed

- **`AGENTS.md`, new section *Parallel sessions*.** States the rule that makes
  concurrency survivable: the dossier splits into *owned records*
  (`attempts/`, `experiments/`, `sessions/`, `reviews/` — one session each) and
  *shared ledgers* (`STATEMENT.md`, `problem.json`, `STATE.md`, `CLAIMS.md`,
  `OBLIGATIONS.md`, `PROOF.md`, `DECISIONS.md`, `LOG.md`, `PROJECT_STATE.md`,
  generated index and dashboard). Owned records parallelize; ledgers are written
  one session at a time. Also fixed in the contract: advance ID allocation, the
  stale-state re-read requirement for whoever finishes second, the punch-list
  closure path, the rule that a sibling session is never a fresh reviewer, and
  the rule that an unfinished background job's results may not be claimed.
- **`process/concurrency.md`, new.** The operational detail: when parallel work
  is allowed and when it is not (including the negative case — two agents on one
  proof attempt, where the bottleneck is insight rather than hands), worktree
  isolation, ID allocation, ledger serialization, the punch-list convention,
  conflict handling, the cross-session declarations each session must record,
  independence, machine-resource discipline, and a two-part checklist.
- **`process/harness.md`, new section.** Isolation mechanism per harness
  (Claude Code: `git worktree` or worktree-isolated subagents; Codex: a worktree
  per session), plus the explicit note that no isolation mechanism converts a
  sibling session into a reviewer.
- **`scripts/proofctl.py`: `add --id`.** The one failure mode discipline cannot
  fix. `next_record_number` scans the tree it can see, so two agents in separate
  worktrees both receive the same next free number and only discover it at merge
  time. `--id A019` (or `--id 019`) pins the record ID; `requested_record_number`
  validates the format and refuses a number already used in that tree. Automatic
  allocation is unchanged when `--id` is omitted.
- **`PROJECT_STATE.md`:** one bullet under repository-wide decisions.
- Design choices: the rule lives in `AGENTS.md` as the single source of truth
  with `process/concurrency.md` carrying only operational detail, per the
  no-restatement rule; `--id` deliberately does *not* try to detect sibling-tree
  allocations, since a tool cannot see another worktree — the launching session
  owns that responsibility and records the blocks it handed out; and the
  punch-list convention codifies what `S017` improvised rather than inventing a
  new mechanism.

## Verification

- `python3 -m unittest tests.test_proofctl` — 12 tests, OK (was 11; the new
  `test_explicit_record_id_allocation_for_parallel_sessions` covers explicit
  allocation, the prefixed and bare spellings, refusal of a used ID, refusal of a
  malformed ID, and that automatic allocation still continues past the explicit
  ones).
- `python3 scripts/proofctl.py validate` — passed (2 problem dossiers).
- Inspection: `AGENTS.md` gains a section and no existing rule was reworded;
  `process/concurrency.md` and `process/harness.md` carry only detail and
  harness mechanics, no new rules; the `proofctl.py` change is additive with the
  default path unchanged.

## Dossier impact

None. No statement, claim, obligation, proof, review, status, or research
session changed. The protocol is written from the `S016`/`S017` experience but
records no mathematics, and the parallel run it is intended for has deliberately
**not** been launched — the user will start it in a later session.

## Handoff

- Result: concurrency is contract law rather than improvisation. Two agents may
  share a dossier when their owned records are disjoint and their routes are
  mechanistically independent; ledger writes serialize; IDs are handed out in
  advance and the tool now enforces the allocation.
- Remaining operational follow-up: none required. Optional, if parallel runs
  become routine: a `proofctl.py` check that warns when a session record
  declares a sibling but the ledgers show no punch list.
- Files a later operator should read: `AGENTS.md` (Parallel sessions),
  `process/concurrency.md`, `process/harness.md` (Parallel sessions).
- Recommended first parallel pairing, recorded here as context rather than as a
  research decision: the two independent routes to `G015` — R1 (no tight
  1-atom, internal structure work) and R2 (verify and strengthen the imported
  \(4/7\) cubic-density bound, literature-facing) — which share no machinery,
  or R1 paired with the Tier 4 generator build, which is pure tooling.
- Commit and push status: committed and pushed as the operational commit for
  O010, separate from the `S018` research commit.
