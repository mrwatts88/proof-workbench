# Status model

Each dossier has two independent axes in `problem.json`.

## Workflow status

| Status | Meaning | Exit criterion |
|---|---|---|
| `intake` | Statement is being normalized. | Scope, definitions, and initial obligations are explicit. |
| `active` | Proof, disproof, or reduction work is underway. | A coherent candidate exists or work is blocked. |
| `candidate` | An integrated argument claims to settle the statement. | Ready for adversarial review. |
| `review` | One or more adversarial audits are underway. | Findings are resolved or the candidate is rejected. |
| `blocked` | No responsible next deduction is available under current constraints. | A named blocker is removed or scope is changed. |
| `complete` | A terminal outcome passed its promotion gate. | Reopen if a critical flaw appears. |
| `archived` | Work is intentionally inactive; outcome may be nonterminal. | Explicit reactivation decision. |

## Claim status

| Status | Meaning |
|---|---|
| `open` | The current statement is unsettled. |
| `proof_candidate` | An integrated proof or disproof candidate exists but is not verified. |
| `proved` | The proof gate passed. |
| `disproved` | A counterexample or contradiction gate passed. |
| `undecidable` | A precisely scoped independence/undecidability result passed review. |
| `withdrawn` | The claim was removed as malformed, duplicate, or no longer intended. |

## Allowed combinations

- `candidate` and `review` require `proof_candidate`.
- `complete` requires `proved`, `disproved`, `undecidable`, or `withdrawn`.
- A terminal claim status normally requires `complete` or `archived`.
- `archived` is not evidence of truth or falsehood.
- `blocked` describes the process, never the truth value.

## Moving backward

Status is not prestige. Move a dossier back to `active` when a critical review
finding opens a gap. Use `blocked` only when the blocker and the condition for
unblocking are recorded. Reopening a completed dossier requires a decision entry
that identifies the new evidence.

