# Claude Code entry point

The operating contract for this repository is harness-neutral and lives in
`AGENTS.md`. It is imported here so that a Claude Code session loads it
automatically. Do not restate or fork its rules in this file.

@AGENTS.md

Everything below is Claude Code specific. It never overrides `AGENTS.md`; it
states how this harness satisfies that contract. See `process/harness.md` for the
full capability matrix and the Codex equivalents.

## Delegation is available here

`AGENTS.md` and `process/workflow.md` allow a same-context review only when fresh
delegation is genuinely unavailable. In Claude Code it is always available, so
that exemption does not apply. Every required adversarial audit must be delegated
to the `proof-reviewer` subagent defined in `.claude/agents/proof-reviewer.md`.

Delegate with the Task tool after `proofctl.py review` has created the record.
Give the subagent only the problem slug, the review record path, the review type,
and the instruction to start from `STATEMENT.md` and `PROOF.md`. Do not paste
attempt or session reasoning into the prompt; that would destroy the isolation the
subagent exists to provide.

Record the resulting independence mode as `delegated-subagent`.

## Fresh discovery is available here

For a nontrivial strategy audit, the primary agent may delegate independent route
generation to the `proof-explorer` subagent in
`.claude/agents/proof-explorer.md`. This is especially useful after a route is
falsified, when several sessions have inherited the same architecture, or when
the recorded next action appears to be anchoring the work.

Give the explorer only the problem slug, the applicable external-source or
benchmark restriction, and the instruction to follow its isolation rules. Do not
paste the current next action or discovery narrative. Its route memo is
speculative input: compare it with the canonical record, stress-test it, and keep
responsibility for the selected strategy in the primary session. Never count an
explorer memo as an adversarial review or as support for a claim.

## Compaction does not create a fresh context

Claude Code summarizes the conversation when it grows long. A compacted session
still carries the discovery reasoning forward in distilled form, so it is **not** a
fresh context. Never record an audit performed after compaction in the same
session as independent. If a delegated subagent is somehow unavailable, stop and
resume the audit in a genuinely new session rather than downgrading the
independence claim.

## Conversational default

`AGENTS.md` requires that ordinary questions, reactions, brainstorming, and
requests to explain are answered as conversation only, with no commands, record
creation, or status changes. This overrides any default bias toward acting. Read
the repository only when the user has clearly asked for work.

## Tooling notes

- Repository commands are allowlisted in `.claude/settings.json`, including the
  session-closing commit and push that `AGENTS.md` requires. If a needed command
  prompts repeatedly, extend that allowlist as operational work rather than
  working around it.
- Prefer the Read, Glob, and Grep tools over shell equivalents when inspecting the
  repository. Keep any Bash command flat and literal.
- Use extended thinking for statement normalization, integration, and review
  passes. These are the steps where the proof standard demands the most rigor.
- The plan and todo tools are session scratch space. They are not records; only
  the files named in `AGENTS.md` preserve state between sessions.
