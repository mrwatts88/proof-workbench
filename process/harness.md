# Harness portability

This repository is designed to be worked on by more than one agent harness. The
operating contract in `AGENTS.md` and the documents in `process/` are the single
source of truth and must stay harness-neutral. Harness-specific files exist only
to make a harness satisfy that contract; they never introduce process rules of
their own.

If a rule matters to the research, it belongs in `AGENTS.md` or `process/`. If it
only describes how a particular tool is configured, it belongs here or in that
harness's own configuration.

## Entry points

Each harness loads a different file at session start. Both must reach the same
contract.

| Harness | Auto-loaded file | Role |
|---|---|---|
| Codex | `AGENTS.md` | The contract itself |
| Claude Code | `CLAUDE.md` | Imports `AGENTS.md`, then adds harness notes |

`CLAUDE.md` must remain a thin pointer. Duplicating contract text there creates
two contracts that will silently diverge; `proofctl.py validate` checks that the
import is still present but cannot detect meaning that has drifted.

An unfamiliar harness that loads neither file must be pointed at `AGENTS.md`
before any work begins.

## Fresh-context review

This is the only place where harness capability changes what an agent may do. The
contract requires adversarial audits to be performed by a reviewer that has not
seen the discovery reasoning, and permits a same-context audit only when fresh
delegation is genuinely unavailable.

| Harness | Delegation | Required mode |
|---|---|---|
| Claude Code | Subagents via the Task tool | `delegated-subagent`; the unavailability exemption does not apply |
| Codex | No in-session subagent delegation | `clean-session` in a later session, with the limitation recorded |

Claude Code defines the reviewer in `.claude/agents/proof-reviewer.md`. That file
enforces the isolation rule mechanically: the reviewer starts from `STATEMENT.md`
and `PROOF.md` and may not read `attempts/`, `sessions/`, or prior `reviews/`
before its first verdict. Prefer it over an ad hoc prompt, and do not paste
discovery reasoning into it.

Record how independence was actually obtained with
`proofctl.py review ... --independence <mode>`. The available modes are:

- `delegated-subagent` — a fresh agent with no discovery context;
- `clean-session` — a later session started from the records alone;
- `same-context-limited` — not independent; permitted only as a recorded
  limitation, never as evidence for promotion.

### Context compaction is not a fresh context

Harnesses that summarize a long conversation to continue it, including Claude
Code, carry the discovery reasoning forward in distilled form. A pass performed
after compaction is `same-context-limited`, not `clean-session`. Summarization
removes detail, not influence.

## Permissions and sandboxing

The end-of-session checkpoint requires running validation and tests, sometimes
compiling with Tectonic, and always committing and pushing. Each harness gates
those differently, and a blocked command leaves a session that the contract
considers unclosed.

- Claude Code: allowlisted in `.claude/settings.json`. Extend it as operational
  work rather than routing around it.
- Codex: governed by its own approval and sandbox settings, configured outside
  this repository. Network access is needed for `git push` and for Tectonic's
  first run.

Keep commands recorded in experiment and session records flat and literal —
a single command with explicit paths, no loops or substitutions — so that they
remain reproducible and do not trip a safety analyzer in either harness.

## Skills, slash commands, and other conveniences

Harness-specific shortcuts are permitted only as thin wrappers that point at
`AGENTS.md` or `process/`. Process encoded solely in a slash command or skill is
invisible to the other harness and will be skipped there.

The contract deliberately uses natural-language triggers instead. `Continue
<slug>` and `close session` are defined in `AGENTS.md` and work identically in
every harness, including plain chat.
