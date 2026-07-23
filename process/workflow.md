# Research workflow

## 1. Intake and normalization

Create a dossier, then rewrite the conjecture into a statement whose truth value is
well-defined.

- Specify every domain, quantifier, dependency, and convention.
- Separate hypotheses from notation and from the desired conclusion.
- Define degenerate objects and boundary cases.
- Give the statement a version. Any material change creates a new version and a
  decision record.
- Record provenance without treating the source's wording as authoritative.

Deliverable: `STATEMENT.md` version 0.1 or later, with initial claims and
obligations.

## 2. Triage

Before investing in a proof:

- test the smallest and most pathological cases;
- search for counterexamples and missing hypotheses;
- compare with known results, recording exact theorem hypotheses;
- identify invariances, normal forms, monotone quantities, and likely obstructions;
- classify computational tests as exploratory, exhaustive, or certificate-based.

Deliverable: an intake session and an initial `STATE.md` naming the best next move.

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

Create one attempt record per coherent approach. An attempt should state:

- the mechanism that might make the approach work;
- required intermediate claims;
- decisive tests;
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

Create a review record using `review-playbook.md`. A useful review attempts to
break the proof, not summarize it. Critical findings become obligations and move
the work status backward when necessary.

For final promotion, conduct clean-context review passes from the statement and
proof, revealing prior heuristics only after the first audit when feasible.

## 7. Consolidation and handoff

At the end of a substantive session:

1. record what changed and what failed;
2. reconcile the claim and obligation ledgers;
3. update the integrated proof if warranted;
4. make decisions and statement versions explicit;
5. rewrite `STATE.md` around the current frontier;
6. set one concrete next action;
7. rebuild the index and validate.

The next action should be falsifiable and small, such as “prove L004 without
compactness” or “search orders 8–12 for a counterexample to C007,” not “continue
working.”

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
4. set a small, falsifiable next action;
5. rebuild `problems/INDEX.md` and run `proofctl.py validate`;
6. repair any inconsistency found by validation;
7. report what is established, what remains open, and where the next session
   should resume;
8. end with a plain-language explanation of what was accomplished and why it
   matters;
9. give a single subjective percentage for the chance that continued work will
   eventually settle the exact current statement.

Do not ask the user which records to update. The current dossier and the required
checkpoint determine that.

The success estimate counts a valid proof, counterexample or other disproof, or
independence/undecidability result as success. It is an outlook estimate, not
evidence about the conjecture's truth. Support it with the concrete routes and
obstacles visible at closure, and record any change from the preceding estimate.
Persist both the plain-language recap and the estimate in the session record and
`STATE.md` so a later session can understand and revise them.
