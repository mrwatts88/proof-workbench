# Agent Operating Contract

These instructions apply to the entire repository.

## Mission

Produce proofs, disproofs, or precisely delimited partial results that can survive
adversarial review. Preserve the reasoning state so another session can resume
efficiently and can distinguish established facts from guesses, experiments, and
open gaps.

## Canonical records

When records conflict, use the most conservative interpretation and repair the
conflict before advancing the status.

- `STATEMENT.md` is the exact current claim, definitions, quantifiers, and scope.
- `problem.json` is the machine-readable workflow state and next action.
- `STATE.md` is the concise operational handoff; it is not a chronological diary.
- `CLAIMS.md` inventories atomic mathematical assertions and their support.
- `OBLIGATIONS.md` is the live list of gaps that block a proof or disproof.
- `PROOF.md` is the current integrated proof or counterexample candidate.
- `DECISIONS.md` records statement changes and consequential research choices.
- `LOG.md` is an append-only chronology.
- `attempts/`, `reviews/`, `experiments/`, and `sessions/` preserve detailed work.

Never let a summary silently upgrade a claim beyond its supporting record.

## Resume protocol

Before substantive work:

1. Run `python3 scripts/proofctl.py validate`.
2. Read `PROJECT_STATE.md` and `problems/INDEX.md`.
3. For the selected problem, read the canonical records above.
4. Read the latest relevant session, active attempt, and unresolved review.
5. Restate privately or in the new session record:
   - the exact target;
   - permitted assumptions;
   - the strongest established facts;
   - the smallest unresolved obligations;
   - the next falsifiable move.
6. Create a session record for any substantive investigation:
   `python3 scripts/proofctl.py add <slug> session "<focus>"`.

Do not begin from a remembered version of a conjecture.

## Research loop

For each meaningful line of attack:

1. Normalize the claim. Expand definitions, expose quantifiers, test boundary and
   degenerate cases, and list hidden assumptions.
2. Search for failure first. Try small cases, extremal constructions, symmetry,
   dimension/counting obstructions, and known theorem hypotheses.
3. Decompose the target into atomic claims and explicit proof obligations.
4. Work in an attempt record. Label intuition, computations, imported theorems,
   and proved deductions distinctly.
5. Stress-test the result from an adversarial role. Check quantifier order,
   domain restrictions, circular dependencies, equality cases, and illicit
   limit/interchange steps.
6. Integrate only supported claims into `PROOF.md`; keep failed approaches with a
   useful postmortem.
7. Update the persistent handoff before ending the session.

A review pass may occur in a later clean-context session. Do not claim reviewer
independence merely because the same reasoning was paraphrased.

## Required end-of-session checkpoint

A substantive session is any investigation that produces or changes a deduction,
counterexample, computation, imported fact, failed approach, proof obligation,
research decision, status, or next action.

Closing a substantive session is part of completing the research task, not an
optional documentation follow-up. Before giving a final response that ends such a
session, complete the checkpoint below. Do not wait for the user to ask whether
important material was recorded.

The user may also say `close session`, `close the session`, `closed session`, or
equivalent wording. Treat that as an instruction to stop investigating, reconcile
the current research state, complete the entire checkpoint, run validation, and
only then report the concise handoff. The user does not need to enumerate the
records to update.

For every substantive session:

- complete the session record with results, failures, evidence, next moves, a
  plain-language recap, and the current success estimate;
- append a dated entry to `LOG.md`;
- update `CLAIMS.md` and `OBLIGATIONS.md`;
- update `PROOF.md` only if the integrated argument changed;
- update `DECISIONS.md` if the statement, assumptions, or strategy changed;
- rewrite `STATE.md` as a concise current handoff, including the human-level state
  and current success estimate;
- update `problem.json` using `set-status` when status or next action changed;
- rebuild the index and run validation;
- update `PROJECT_STATE.md` if repository-wide priorities changed.
- inspect the working tree; commit all and only the session-related canonical
  records, attempts, experiments, and supporting process changes with a
  descriptive commit message; then push the current branch to its configured
  upstream. Do not include unrelated pre-existing changes. If a commit or push
  cannot be completed, say so plainly and do not represent the session as
  closed.

End the closing response with:

1. **Plain-language recap:** explain what the session actually accomplished, why
   it matters, and what remains, in language an interested nonspecialist can
   understand. Minimize internal IDs and advanced nomenclature; when a technical
   term is necessary, explain it.
2. **Estimated chance of resolution:** give a single percentage from 0% to 100%
   for the subjective chance that continued work in this project will eventually
   settle the exact current statement by a valid proof, a valid disproof or
   counterexample, or a valid independence/undecidability result. Give a short
   basis tied to concrete progress, obstacles, and plausible routes. If a prior
   estimate exists, state the change and why.

The estimate is research judgment, not mathematical evidence. It must not upgrade
`claim_status`, resolve an obligation, or be presented as a calibrated fact. Avoid
false precision in the explanation even though the user requested a point
percentage.

Store distilled reasoning, not raw chat transcripts. Preserve exact prompts,
outputs, or code only when they are evidence needed to reproduce a result.

A session is not closed merely because a summary was written. It is closed only
after the canonical records agree, the next action is explicit, the index is
current, validation passes, the session-scoped changes are committed, and that
commit has been pushed to the configured upstream. If validation, commit, or
push fails, repair the issue before reporting the session as closed.

## Epistemic rules

- A finite search does not prove a universal statement unless a proved reduction
  makes the search exhaustive.
- Numerical agreement is not exact equality.
- A computer algebra result is an imported claim until independently justified or
  backed by a checkable certificate.
- Random tests can find counterexamples but cannot establish universality.
- A diagram is intuition unless every used property is formalized.
- An external theorem must include a precise statement, matched hypotheses, and a
  source in `references/`.
- A named claim may be cited only at the strength recorded in `CLAIMS.md`.
- Circular dependencies are prohibited. Record dependencies explicitly.
- Changing a quantifier, domain, convention, or nondegeneracy assumption requires
  a statement-version change and a `DECISIONS.md` entry.
- Failed attempts are research assets. Do not delete or rewrite away the reason
  they failed.

## Status discipline

Use both `work_status` and `claim_status` as defined in
`process/statuses.md`. In particular:

- examples or computational evidence do not justify `proof_candidate`;
- prose that says “clearly” does not resolve an obligation;
- `complete` + `proved` requires no unresolved proof obligations and at least two
  recorded adversarial review passes;
- `complete` + `disproved` requires an explicit counterexample or contradiction
  and at least one independent reproduction review;
- unresolved critical review findings move work back to `active` or `blocked`.

The validator checks record presence, not mathematical truth. Agents remain
responsible for the substance.

## Tool and file discipline

- Prefer exact arithmetic, deterministic seeds, pinned inputs, and small auditable
  programs.
- Put reusable code and its invocation in `experiments/<id>/`; separate generated
  data from conclusions.
- Record tool versions when output is material to an argument.
- Do not fabricate references, theorem names, computations, reviews, or consensus.
- Use stable IDs from `process/records.md` in proofs and cross-references.
- Keep `STATE.md` short enough to read at session start; move history to records.
- Run tests and validation after changing repository process or tooling.
- Do not commit, push, publish, or contact third parties unless the user asks.
  The required end-of-session checkpoint is the standing exception for the
  session-scoped commit and push described above.
