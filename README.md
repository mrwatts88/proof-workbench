# Proof Workbench

This repository is a durable workspace for investigating mathematical hypotheses,
constructing proofs or counterexamples, and preserving enough context for a later
session to continue without relying on chat history.

The repository treats a proof as a collection of auditable claims and obligations,
not as a persuasive narrative. Computation, examples, and intuition are evidence;
they become proof only when their logical role is made explicit.

## Start here

1. Read [PROJECT_STATE.md](PROJECT_STATE.md) for the repository-wide handoff.
2. Read [problems/INDEX.md](problems/INDEX.md) and choose a problem.
3. In that problem, read `problem.json`, `STATEMENT.md`, `STATE.md`,
   `CLAIMS.md`, and `OBLIGATIONS.md`.
4. Read the most recent relevant session, attempt, and review records.
5. Follow [AGENTS.md](AGENTS.md) and the process documents in `process/`.

[AGENTS.md](AGENTS.md) is the operating contract for every agent harness. Codex
loads it directly; Claude Code loads [CLAUDE.md](CLAUDE.md), which imports it and
adds only harness-specific notes. [process/harness.md](process/harness.md)
describes how each harness satisfies the contract, most importantly for delegated
adversarial review.

## Common commands

```sh
python3 scripts/proofctl.py validate
python3 scripts/proofctl.py status
python3 scripts/proofctl.py new compactness-example --title "A compactness example"
python3 scripts/proofctl.py add compactness-example session "Initial normalization"
python3 scripts/proofctl.py operation "Refresh process tooling"
python3 scripts/proofctl.py add compactness-example attempt "Minimal counterexample"
python3 scripts/proofctl.py add compactness-example review "Quantifier audit"
python3 scripts/proofctl.py typeset unique-common-neighbor
python3 scripts/proofctl.py set-status compactness-example active --claim open \
  --next "Resolve G001 or record why it is blocked"
```

Run `python3 scripts/proofctl.py --help` for all options. The CLI uses only the
Python standard library.

## Continuing and closing research

In a later agent session, a human can resume without restating prior work:

```text
Continue compactness-example.
```

The agent follows the resume protocol in `AGENTS.md` and reads the dossier's
current handoff. The stored next action is treated as the previous session's best
proposal, not an order: before nontrivial exploration the agent compares it with
the quickest way to falsify it and with a genuinely different route or reframing.
The selected route, live alternative, and pivot trigger are preserved in the
session and handoff.

Where a harness supports fresh discovery agents, one may generate independent
routes before seeing the inherited plan. Those suggestions are speculative inputs,
not reviews or proof evidence; the primary agent remains responsible for checking
and selecting them.

To end the current research session, the human can simply say:

```text
Close session.
```

That phrase invokes the complete checkpoint in `AGENTS.md`: the agent reconciles
the session, claims, obligations, proof, decisions, log, handoff, status, and next
action; rebuilds the index; and validates the repository. The human does not need
to list those bookkeeping steps. Agents also perform the checkpoint automatically
before ending any substantive mathematical session.

Before reporting closure, the agent also commits all and only the session-related
changes with a descriptive message and pushes that commit to the current branch's
configured upstream. Unrelated pre-existing working-tree changes must be left
out. A failed commit or push means the session remains open until it is repaired.

The closing response ends with three things: a plain-language account of what was
accomplished, a subjective percentage estimate for the chance that continued work
will eventually settle the conjecture, and the proposed next step. A valid proof,
counterexample or other disproof, or independence/undecidability result counts as
success. The percentage is an outlook judgment and never substitutes for proof or
changes the formal claim status.

The proposed next step says in plain language what the following session should
do and what that move would establish or rule out, so the direction of the work is
visible without opening the dossier. It always matches the next action stored in
`problem.json` and `STATE.md`.

## Repository map

```text
AGENTS.md              operating contract for agents, harness-neutral
CLAUDE.md              Claude Code entry point; imports AGENTS.md
.claude/               Claude Code subagents and permissions
PROJECT_STATE.md       concise repository-wide handoff
process/                workflow, proof standards, review, and tool guidance
problems/INDEX.md       generated problem dashboard
problems/<slug>/        one self-contained research dossier
operations/              repository-only process and tooling records
knowledge/              reusable results and methods across problems
templates/              records created during research
scripts/proofctl.py     create, index, update, and validate dossiers
tests/                  structural regression tests
```

The `problems/_template/` directory is a browsable specimen. New dossiers should
normally be created with `proofctl.py new`, which assigns a stable problem ID and
rebuilds the index.

<!-- BEGIN GENERATED PROBLEM DASHBOARD -->
## Live research status

| ID | Problem | Work | Claim | Previously proven? | LaTeX |
|---|---|---|---|---|---|
| P-001 | Unique Common Neighbor ([details](problems/unique-common-neighbor/STATE.md)) | `complete` | `proved` | Reported (not inspected) | [PDF](papers/build/unique-common-neighbor.pdf) · [TeX](papers/unique-common-neighbor.tex) |
| P-002 | Erdős–Gyárfás Conjecture ([details](problems/erdos-gyarfas/STATE.md)) | `active` | `open` | Unknown | — |

<!-- END GENERATED PROBLEM DASHBOARD -->
