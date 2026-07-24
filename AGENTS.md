# Agent Operating Contract

These instructions apply to the entire repository and to every agent harness. They
are the single source of truth; harness-specific configuration may explain how a
harness satisfies this contract but may never restate, weaken, or extend it. See
`process/harness.md`.

## Mission

Settle genuinely open conjectures: produce proofs, disproofs, or precisely
delimited partial results that can survive adversarial review and that add
information the mathematical community does not already have. Lean on all
existing verified knowledge — published theorems, computations, and explicit
examples — through the import rules to reach the current frontier as fast as
possible; effort belongs past the frontier, never on re-deriving known results
for their own sake. Preserve the reasoning state so another session can resume
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

## Conversational default

Treat ordinary questions, reactions, feedback, brainstorming, confirmations, and
requests to explain or discuss as conversation only. Do not run commands, inspect
the repository, create records, update status, test, commit, push, or start a
workflow merely because the topic concerns this repository or its process.

Act only when the user clearly asks to inspect, change, build, record, test,
commit, deploy, or otherwise perform work. If the wording is genuinely ambiguous,
answer the question first and ask before taking action. A conversational request
such as “can we do this?” is not by itself authorization to do it.

## Classify work before choosing a protocol

First decide whether the request is mathematical research or a repository
operation. Do not use a problem dossier merely because one happens to exist.

- **Mathematical research** changes or evaluates a particular statement, proof,
  counterexample, claim, obligation, experiment, review, or problem status. Use
  the full dossier resume protocol, create an `S###` session, and close it with
  the research checkpoint and resolution outlook.
- **Repository operation** changes process, tooling, commands, templates,
  dashboards, build/publication infrastructure, documentation, or other support
  systems without advancing a mathematical result. Do not select a problem,
  create an `S###` record, update problem canonical records, change a claim/status,
  or report a chance of mathematical resolution. Create an `O###` record with
  `python3 scripts/proofctl.py operation "<focus>"` when the work is material.
- **Mixed work** must be split. Record the mathematical portion in the affected
  dossier and the supporting/tooling portion in an operation record. Do not use a
  research session as a diary for process work.

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

## Strategic autonomy

The `next_action` in `problem.json` and `STATE.md` is the best proposal from the
previous checkpoint, not an instruction whose premises must be accepted. Its
purpose is to make work resumable, not to turn the next agent into an implementer
of a stale plan.

Before committing a substantive exploration session to the inherited route, the
agent must perform a brief strategy audit:

1. state why the inherited route might work and the fastest evidence that would
   kill it;
2. compare it with a failure-first move and at least one mechanistically distinct
   alternative or reframing;
3. allow a short generative phase before rejecting ideas, then select the route
   with the best expected research value—information gain, leverage on the main
   claim, falsifiability, and dependence on unproved assumptions;
4. name the pivot condition that will trigger reevaluation.

This is a reasoning discipline, not a quota or brainstorming performance. A
sentence per route is enough when the comparison is simple. Do not manufacture
cosmetic variants merely to fill a template, and do not interrupt intake,
candidate review, required reproduction, or mechanical closure work with an
irrelevant strategy exercise.

The agent is authorized to replace, postpone, or retire the inherited next action
without asking the human when mathematical evidence supports the change. When a
route is falsified or loses its comparative advantage, pivot rather than finishing
it for compliance. Record the decisive reason in the session and attempt, update
`DECISIONS.md` when the proof architecture materially changes, preserve a compact
strategy portfolio in `STATE.md`, and make the selected next move the new
`next_action`.

Protect creativity without weakening epistemic standards. Speculative mechanisms,
analogies, and reframings belong in the strategy audit or an attempt record and
must be labeled as such. They enter `CLAIMS.md` or `PROOF.md` only at their
supported strength.

Missing tools are research targets, not exogenous events. When the recorded
obstacle is that no known technique applies, the strategy audit must weigh at
least one internal tool-building attempt — a new mechanism, construction, or
lemma with a falsifiable first move and an explicit kill condition — against
importing or awaiting external progress. Capability-based deference is never a
selection reason: routes are chosen on expected research value, not on
assumptions about who is entitled to build the missing piece. Ambition does not
license inflation; estimates and claim strengths stay calibrated to evidence.

When the harness supports delegation, a fresh discovery agent may be used to
counter anchoring or generate independent mechanisms. Give it the exact statement,
definitions, established claims, and open obligations, but initially withhold the
inherited next action, attempts, and session narrative. External literature is
available to it by default; its isolation targets this repository's inherited
framing, not the world's knowledge. This is optional discovery, not an adversarial review and not
evidence by itself. The primary agent must compare, stress-test, and synthesize
its suggestions. See `process/harness.md`.

## Research loop

For each meaningful line of attack:

1. Audit the current strategy—beginning with the inherited next action at session
   start—and choose the route under the strategic autonomy rules above.
2. Normalize the claim. Expand definitions, expose quantifiers, test boundary and
   degenerate cases, and list hidden assumptions.
3. Search for failure first. Try small cases, extremal constructions, symmetry,
   dimension/counting obstructions, and known theorem hypotheses.
4. Decompose the target into atomic claims and explicit proof obligations.
5. Work in an attempt record. Label intuition, computations, imported theorems,
   and proved deductions distinctly.
6. Stress-test the result from an adversarial role. Check quantifier order,
   domain restrictions, circular dependencies, equality cases, and illicit
   limit/interchange steps.
7. Integrate only supported claims into `PROOF.md`; keep failed approaches with a
   useful postmortem.
8. Recalibrate the route portfolio and persistent handoff before ending the
   session.

A review pass may occur in a delegated fresh agent or a later clean-context
session. Do not claim reviewer independence merely because the same reasoning was
paraphrased, or because a long context was compacted before the audit.

## Mandatory candidate-to-review transition

When an integrated argument appears to prove or disprove the current statement,
the agent must initiate adversarial review without waiting for the human to ask.
This is a workflow transition, not an optional suggestion:

1. integrate the exact candidate in `PROOF.md`, keep every unresolved gap visible,
   and set `work_status` to `candidate` with `claim_status` `proof_candidate`;
2. immediately run `python3 scripts/proofctl.py review <slug> "<audit title>"
   --type <logic|hypotheses|counterexample|computation|exposition>`;
3. assign the review to a fresh agent that has not participated in discovery. When
   the harness supports delegation, that is mandatory, not preferred; see
   `process/harness.md` for what each harness provides. Only when delegation is
   genuinely unavailable may the audit wait for a later clean context, and that
   limitation must be recorded. A context that was summarized or compacted to
   continue the same session is not a fresh context;
4. give the reviewer the exact statement and candidate first. Do not provide
   attempts, session narratives, or prior reviews until its initial verdict;
5. announce to the human that review has begun, report its verdict, turn every
   critical or major finding into an obligation, and either repair the candidate or
   return the dossier to active work.

For a proof or undecidability candidate, initiate two distinct audits before
promotion: one logic/dependency audit and one hypotheses/counterexample audit. For
a counterexample, initiate a fresh reproduction audit from the statement. The
agent chooses and performs these steps; never ask the human to remember commands
or decide whether review is due.

## LaTeX and live dashboard at completion

When a claim is ready for `complete` + `proved`, the agent must create or update a
standalone LaTeX source in the root-level `papers/` directory. It must state the
exact statement version, give the reviewed proof (not merely a link or outline),
and name the supporting review records. Set `latex_file` in `problem.json` to its
repository-relative path before promotion. Run `python3 scripts/proofctl.py
typeset <slug>` to compile with Tectonic, record `pdf_file` and `latex_engine` in
the manifest, and include the generated PDF in the session commit. A proof cannot
be promoted to `proved` without both source and PDF. If Tectonic is absent, the
agent must install or repair the approved toolchain before attempting promotion.

At intake, record `prior_proof_status` as `unknown`, `reported`, or `verified`.
Its purpose is target selection: the mission is to settle open problems, so a
statement with a verified external proof is not a research target, and a merely
reported proof should be verified or refuted, not re-derived blind. External
results of any strength are usable through the import rules; internal claim
promotions still pass this repository's review gates.
After every dossier creation, status update, or completion, run `proofctl.py
index`; it regenerates the live table in `README.md`. The agent owns these updates
and must not ask the human to maintain them.

## Parallel sessions

Two agents may work the same problem concurrently, but only under a partition
that the records can survive. The dossier separates **owned records**
(`attempts/`, `experiments/`, `sessions/`, `reviews/`), which belong to exactly
one session, from **shared ledgers** (`STATEMENT.md`, `problem.json`,
`STATE.md`, `CLAIMS.md`, `OBLIGATIONS.md`, `PROOF.md`, `DECISIONS.md`,
`LOG.md`, `PROJECT_STATE.md`, and the generated index and dashboard). Owned
records parallelize; ledgers do not.

When the harness supports delegation, parallel legs run as **worker subagents
of a single orchestrating session**, not as two interactive sessions. The
orchestrator allocates each worker a disjoint block of owned-record IDs, holds
every shared ledger for the whole run, audits the workers' output before
integrating any of it, and performs the one canonical checkpoint. A worker is
not a session: it writes only its assigned owned records — never a ledger,
never a status change, never a commit — it leaves no `S###` record, and its
report is working input to the orchestrator, not a citable record or
corroborating evidence. Two interactive sessions under the partition below are
the fallback, legitimate only when delegation is genuinely unavailable or when
a human deliberately runs the second session.

- Parallel work requires disjoint owned records and no dependency on the
  sibling's uncommitted results. A sibling's in-progress reasoning is not
  citable.
- Record IDs must be allocated in advance by the launching session and passed
  explicitly (`proofctl.py add ... --id A019`); each agent otherwise scans its
  own tree and picks the same number.
- Ledger writes are serialized: one session at a time performs the canonical
  checkpoint. A session finishing second re-reads every ledger it changes, because
  its starting state is stale by construction.
- A session that must close while the ledgers are held records its pending
  ledger edits as a punch list in its own session record and reports the dossier
  as not yet reconciled. It is closed only once that punch list is applied.
- A sibling session is never a fresh reviewer and never corroborating evidence;
  review independence is unchanged.
- An unfinished background job's results may not be claimed. Exclude the leg
  from every ledger row and name the harvest as follow-up.

See `process/concurrency.md` for the two modes, isolation, conflict handling,
cross-session declarations, and the machine-resource rules.

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

For every substantive mathematical session:

- complete the session record with results, failures, evidence, next moves, a
  plain-language recap, and the current success estimate;
- append a dated entry to `LOG.md`;
- update `CLAIMS.md` and `OBLIGATIONS.md`;
- update `PROOF.md` only if the integrated argument changed;
- update `DECISIONS.md` if the statement, assumptions, or strategy changed;
- rewrite `STATE.md` as a concise current handoff, including the human-level state
  and current success estimate, plus the primary route, a live alternative or
  reframing, and the condition that would trigger a pivot;
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
3. **Proposed next step:** state what the next session should actually do, in the
   same plain language as the recap. Give the concrete move, say what it would
   establish or rule out, and name any alternative that was considered and
   deferred. This must be the same next action recorded in `problem.json` and
   `STATE.md`; if they disagree, repair the records rather than the message. It
   must be small and falsifiable — "search orders 12–14 for a counterexample to
   C007," not "continue working." If the dossier is complete, say that no further
   step is required and name any optional follow-up. This selection is the next
   session's inherited proposal, not a command that bypasses its strategy audit.

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

## Operational-work checkpoint

For a material repository operation, create and complete an `operations/O###`
record; state scope, verification, and dossier impact. Run relevant tests and
`proofctl.py validate`, update `PROJECT_STATE.md` only if repository-wide
priorities changed, then commit and push only the operational changes. Do not
rewrite a problem's `STATE.md`, `CLAIMS.md`, `OBLIGATIONS.md`, `PROOF.md`,
`DECISIONS.md`, `LOG.md`, or `sessions/` unless the task separately has a genuine
mathematical component. The final report describes the operational outcome and
verification only; it has no required research recap or resolution percentage.

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
