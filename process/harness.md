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

Review independence is the one place where harness capability changes the
promotion path. The contract requires adversarial audits to be performed by a
reviewer that has not seen the discovery reasoning, and permits a same-context
audit only when fresh delegation is genuinely unavailable.

| Harness | Delegation | Required mode |
|---|---|---|
| Claude Code | Subagents via the Task tool | `delegated-subagent`; the unavailability exemption does not apply |
| Codex | Collaboration subagents when exposed by the session; otherwise unavailable | `delegated-subagent` when exposed; `clean-session` later only when genuinely unavailable |

Claude Code defines the reviewer in `.claude/agents/proof-reviewer.md`. That file
enforces the isolation rule mechanically: the reviewer starts from `STATEMENT.md`
and `PROOF.md` and may not read `attempts/`, `sessions/`, or prior `reviews/`
before its first verdict. Prefer it over an ad hoc prompt, and do not paste
discovery reasoning into it.

In Codex, capability is detected per session. If collaboration/subagent tools are
present, the unavailability exemption does not apply: start a subagent without
forking the discovery conversation and give it the same isolated reviewer brief.
If those tools are absent, record `clean-session` and perform the audit in a
genuinely later context.

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

## Fresh-context discovery

Strategic exploration may also use a fresh agent to reduce anchoring, but this is
different from mandatory candidate review:

- discovery delegation is optional and produces speculative routes, not a
  verdict or mathematical evidence;
- initially give the explorer the statement, definitions, established claims,
  and open obligations, while withholding `next_action`, `STATE.md`, attempts,
  sessions, and prior reviews; external literature is available to it by
  default, since its isolation targets inherited framing, not the world's
  knowledge;
- ask for mechanistically distinct proof, disproof, and reframing routes with
  explicit kill tests;
- after the independent route memo is returned, the primary agent compares it
  with the inherited portfolio, checks it against known failures, and records
  only distilled useful reasoning.

Claude Code provides `.claude/agents/proof-explorer.md` for this role. A harness
Codex may use a no-history collaboration subagent with the same isolation brief
when that capability is exposed. A harness without discovery delegation performs
the same strategy audit in the primary context; that does not weaken any
review-independence requirement.

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
