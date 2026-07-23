# Records and stable IDs

## Problem dossier

| Path | Purpose | Editing mode |
|---|---|---|
| `problem.json` | Machine state, dates, tags, dependencies, next action | Rewrite through CLI when possible |
| `STATEMENT.md` | Exact versioned target | Rewrite with decision entry |
| `STATE.md` | Current handoff | Rewrite each substantive session |
| `CLAIMS.md` | Atomic assertion ledger | Maintain in place |
| `OBLIGATIONS.md` | Live gaps and blockers | Maintain in place |
| `PROOF.md` | Integrated candidate | Rewrite carefully |
| `DECISIONS.md` | Consequential decisions | Append |
| `LOG.md` | Short chronology | Append |
| `attempts/` | One coherent approach per record | Preserve failures |
| `reviews/` | Adversarial findings | Append findings/resolutions |
| `experiments/` | Reproducible computation | Preserve code and compact evidence |
| `sessions/` | Detailed resumable checkpoints | Complete, then preserve |
| `references/` | Local citations and source notes | Add with provenance |

## ID namespaces

- `P-###`: problem, allocated by the CLI.
- `D###`: definition local to a problem.
- `C###`: claim or observation.
- `L###`: lemma or proposition.
- `G###`: proof obligation or gap.
- `Q###`: explicit research question.
- `A###`: attempt.
- `E###`: experiment.
- `R###`: review.
- `S###`: session.
- `K-###`: cross-problem knowledge note.

IDs are never reused after deletion or abandonment. Prefix local IDs with the
problem ID when referring across dossiers, for example `P-003/L007`.

## Claim strength

Use one of these states in `CLAIMS.md`:

- `proposed`: plausible but unsupported;
- `tested`: supported by nonexhaustive evidence;
- `proved`: derived in a linked proof;
- `refuted`: contradicted by a linked example or proof;
- `assumed`: explicitly part of the current statement;
- `imported`: external theorem with source and checked hypotheses;
- `obsolete`: no longer used after a recorded decision.

## Obligation state

Use `open`, `in_progress`, `resolved`, `blocked`, or `not_needed`. Never mark an
obligation resolved without linking the exact resolution.

## Session retention

A session record is a distilled research artifact, not a transcript. Preserve:

- goal and starting state;
- deductions and their dependencies;
- counterexamples and failed routes;
- commands/results needed for reproducibility;
- changes to canonical records;
- a concrete next action.

