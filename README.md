# Research Harness

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

## Common commands

```sh
python3 scripts/proofctl.py validate
python3 scripts/proofctl.py status
python3 scripts/proofctl.py new compactness-example --title "A compactness example"
python3 scripts/proofctl.py add compactness-example session "Initial normalization"
python3 scripts/proofctl.py add compactness-example attempt "Minimal counterexample"
python3 scripts/proofctl.py add compactness-example review "Quantifier audit"
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
current handoff. To end the current research session, the human can simply say:

```text
Close session.
```

That phrase invokes the complete checkpoint in `AGENTS.md`: the agent reconciles
the session, claims, obligations, proof, decisions, log, handoff, status, and next
action; rebuilds the index; and validates the repository. The human does not need
to list those bookkeeping steps. Agents also perform the checkpoint automatically
before ending any substantive mathematical session.

The closing response ends with a plain-language account of what was accomplished
and a subjective percentage estimate for the chance that continued work will
eventually settle the conjecture. A valid proof, counterexample or other
disproof, or independence/undecidability result counts as success. The percentage
is an outlook judgment and never substitutes for proof or changes the formal
claim status.

## Repository map

```text
AGENTS.md              operating contract for agents
PROJECT_STATE.md       concise repository-wide handoff
process/                workflow, proof standards, review, and tool guidance
problems/INDEX.md       generated problem dashboard
problems/<slug>/        one self-contained research dossier
knowledge/              reusable results and methods across problems
templates/              records created during research
scripts/proofctl.py     create, index, update, and validate dossiers
tests/                  structural regression tests
```

The `problems/_template/` directory is a browsable specimen. New dossiers should
normally be created with `proofctl.py new`, which assigns a stable problem ID and
rebuilds the index.
