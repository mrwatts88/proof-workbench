# Research workflow

## 0. Classify the request

Conversational questions and feedback are not work requests: answer them without
opening records or running repository commands. Only after a clear request to act
should the agent classify the requested work. Before opening a dossier, decide
whether that work bears on a mathematical result.
Research about a statement, proof, counterexample, evidence, obligation, or review
uses this workflow and a dossier session. Repository process, tooling, dashboard,
LaTeX build, documentation, or template work that does not change mathematical
support is operational work: create an `O###` record with `proofctl.py operation`,
run relevant checks, and do not update a problem session or resolution outlook.

If a task has both kinds of work, split its records. A process change must not be
recorded as progress on a theorem merely because it was performed near that work.

## 1. Intake and normalization

Create a dossier, then rewrite the conjecture into a statement whose truth value is
well-defined.

- Specify every domain, quantifier, dependency, and convention.
- Separate hypotheses from notation and from the desired conclusion.
- Define degenerate objects and boundary cases.
- Give the statement a version. Any material change creates a new version and a
  decision record.
- Record provenance without treating the source's wording as authoritative.
- Set `prior_proof_status` in `problem.json`: `unknown`, `reported`, or
  `verified`. This status is for the live dashboard and never imports a proof.

Deliverable: `STATEMENT.md` version 0.1 or later, with initial claims and
obligations.

## 2. Triage

Before investing in a proof:

- test the smallest and most pathological cases;
- search for counterexamples and missing hypotheses;
- compare with known results, recording exact theorem hypotheses;
- identify invariances, normal forms, monotone quantities, and likely obstructions;
- classify computational tests as exploratory, exhaustive, or certificate-based.

Deliverable: an intake session and an initial `STATE.md` naming the best next
move, the fastest way to falsify it, and at least one live alternative or
reframing.

## 3. Decomposition

Break the target into stable, referenceable units:

- definitions (`D###`);
- claims, lemmas, and propositions (`C###`, `L###`);
- proof gaps or obligations (`G###`);
- questions (`Q###`);
- attempts (`A###`);
- experiments (`E###`);
- reviews (`R###`);
- sessions (`S###`).

The claim ledger records assertion strength and dependencies. The obligation ledger
records what remains to be shown and what it blocks.

## 4. Exploration

### Strategy audit before committing to a route

The inherited `next_action` is a resumability device, not a command. At the start
of a nontrivial exploration session, briefly compare:

- **exploitation:** the strongest current route and why it might work;
- **falsification:** the cheapest decisive test of that route or its hidden
  premise;
- **alternative or reframing:** a mechanistically different proof architecture,
  representation, or counterexample route.

Generate before pruning: give plausible mechanisms enough room to become
specific, then evaluate them for information gain, leverage, falsifiability, and
unsupported dependencies. Select one primary move and one pivot trigger. This
comparison should be compact and substantive, not a quota of superficial ideas.

The agent may retire or replace the inherited move without human approval when
the audit or later evidence warrants it. A material change of proof architecture
goes in `DECISIONS.md`; the session and `STATE.md` retain the primary route, the
best live alternative, and the reason other routes were deferred or retired.

Where discovery delegation is available, a fresh agent can be asked for
independent mechanisms before it sees the inherited route or discovery narrative.
Its output is exploratory material, not a review verdict or mathematical support;
the primary agent remains responsible for comparison and verification.

### Working an attempt

Create one attempt record per coherent approach. An attempt should state:

- its role in the strategy portfolio: primary, falsification, alternative, or
  reframing;
- the mechanism that might make the approach work;
- required intermediate claims;
- decisive tests and a kill or pivot criterion;
- actual deductions;
- failures and salvageable results.

Run inexpensive falsification tests early. When using computation, create an
experiment record before treating its output as evidence.

## 5. Integration

Promote supported pieces into `PROOF.md` in dependency order. Each nontrivial step
should cite a claim ID, a proved inline derivation, or an imported theorem with
matched hypotheses.

An attractive attempt is not the integrated proof. `PROOF.md` should contain the
strongest coherent candidate and openly label unresolved gaps.

## 6. Challenge

The moment an integrated proof or counterexample candidate exists, stop treating
the task as ordinary exploration. The agent must set the dossier to `candidate`
with claim status `proof_candidate`, then immediately start review itself:

1. run `python3 scripts/proofctl.py review <slug> "<audit title>" --type <type>`;
2. assign that audit to a fresh agent, delegating whenever the harness allows it
   and falling back to a later clean context only when it does not;
3. give the reviewer `STATEMENT.md` and the candidate, but not discovery attempts,
   sessions, or prior reviews before its first verdict;
4. record critical and major findings as obligations and repair or reject the
   candidate before seeking promotion.

The human does not need to request, schedule, or choose these reviews. The agent
owns the transition and must tell the human when review starts and what its verdict
is. A useful review attempts to break the candidate, not summarize it.

For a proof or undecidability result, the agent must obtain two meaningfully
distinct fresh-context audits (normally logic plus hypotheses/counterexample). For
a disproof, it must obtain one fresh-context reproduction audit from the statement.
Delegation is mandatory in a harness that supports it; `process/harness.md` states
what each one provides and which independence mode to record. Only where fresh
delegation is genuinely unavailable may the agent record that limitation and use a
later clean-context pass. It must never label a same-context paraphrase as
independent, and a context that was summarized or compacted to continue the same
session does not become fresh by that summarization.

## 7. Consolidation and handoff

At the end of a substantive session:

1. record what changed and what failed;
2. reconcile the claim and obligation ledgers;
3. update the integrated proof if warranted;
4. make decisions and statement versions explicit;
5. rewrite `STATE.md` around the current frontier;
6. recalibrate the compact strategy portfolio: primary route, live alternative
   or reframing, and pivot trigger;
7. set one concrete next action selected from that portfolio;
8. rebuild the index and validate.

For a `complete` + `proved` result, also create the standalone LaTeX source in
`papers/`, set `latex_file` in `problem.json`, and run `proofctl.py typeset
<slug>` to produce a committed PDF using Tectonic. The resulting `pdf_file` and
`latex_engine` are required promotion evidence. `proofctl.py index` updates both
`problems/INDEX.md` and the live dashboard table in `README.md` after every status
or dossier change.

The next action should be falsifiable and small, such as “prove L004 without
compactness” or “search orders 8–12 for a counterexample to C007,” not “continue
working.” It records the current selection, not an instruction exempting the next
session from strategic reevaluation.

## 8. Closing a session

Session closure is a workflow operation, not a request for a conversational
summary. A substantive session includes work that changes any mathematical
conclusion, evidence, attempted route, obligation, decision, status, or next
action.

An agent must run the consolidation and handoff steps before its final response
when that response ends a substantive session. The user need not remind the agent
to document the work.

The human shorthand `close session` (or equivalent wording such as `close the
session` or `closed session`) means:

1. stop opening new lines of investigation;
2. finish the active session and attempt records with exact results and failures;
3. reconcile all canonical records listed in `AGENTS.md`;
4. recalibrate the route portfolio and set a small, falsifiable next action;
5. rebuild `problems/INDEX.md` and run `proofctl.py validate`;
6. repair any inconsistency found by validation;
7. inspect the working tree, commit all and only the session-related records and
   supporting work with a descriptive message, and push that commit to the
   current branch's configured upstream; do not commit unrelated pre-existing
   changes;
8. report what is established, what remains open, and where the next session
   should resume;
9. end with a plain-language explanation of what was accomplished and why it
   matters;
10. give a single subjective percentage for the chance that continued work will
   eventually settle the exact current statement;
11. state the proposed next step in plain language: the concrete move, what it
    would establish or rule out, and any alternative deferred. It must match the
    next action stored in `problem.json` and `STATE.md`, while remaining a
    proposal for the next session to audit rather than obey blindly.

Do not ask the user which records to update. The current dossier and the required
checkpoint determine that.

The success estimate counts a valid proof, counterexample or other disproof, or
independence/undecidability result as success. It is an outlook estimate, not
evidence about the conjecture's truth. Support it with the concrete routes and
obstacles visible at closure, and record any change from the preceding estimate.
Persist both the plain-language recap and the estimate in the session record and
`STATE.md` so a later session can understand and revise them.

## 9. Closing an operation

Operational work closes through `operations/O###`, not a dossier session. Record
the non-mathematical scope, implementation, verification, and exact dossier
impact; do not give a proof-resolution estimate. Validate, commit, and push the
operation and report its outcome separately from the research workflow.

A session is not closed if its required commit or push fails. The closing report
must name the failure and preserve the reconciled working state for recovery.
