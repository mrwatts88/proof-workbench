# S001 — Initial intake and benchmark constraints

- Date: 2026-07-23
- Problem: `P-001`

## Starting checkpoint

- Statement version: 0.1, unnormalized intake wording
- Work / claim status: `intake` / `open`
- Strongest established facts: only the user-supplied hypotheses and target;
  the user reports an external solution, but it was not inspected and is not
  internal evidence
- Open obligations in scope: `G001`, statement normalization
- Session goal: create a precise benchmark dossier and record the independent
  investigation constraints
- Falsifiable next move: expand the graph definitions and test whether the exact
  wording survives the empty and smallest-order cases

## Work performed

- Expanded “finite simple undirected graph,” “common neighbor,” and “adjacent to
  every other vertex” in `STATEMENT.md` version 0.2.
- Wrote the hypothesis, conclusion, and logical negation with explicit
  quantifiers.
- Tested the empty, one-, two-, and three-vertex boundary cases directly from
  the definitions.
- Recorded that the empty graph would be a counterexample if admitted, so `D001`
  explicitly requires a nonempty vertex set.
- Recorded the user-mandated embargo on searching for, citing, or intentionally
  reproducing known solutions. No external search, source inspection, or
  reference comparison occurred.

## Results

- Proved boundary checks: the singleton graph satisfies the statement
  vacuously; no two-vertex graph meets the hypothesis; \(K_3\) meets both the
  hypothesis and conclusion.
- Resolved `G001` through `STATEMENT.md` version 0.2.
- Created `G002` for the independent proof or disproof, `G003` for later
  adversarial review, and `G004` for the deliberately deferred reference
  comparison.
- No general mathematical inference, computation, or imported theorem was used.
- The main claim `C001` remains `proposed`, and the dossier claim status remains
  `open`.

## Failed routes and why

No proof route was opened. The literal empty-graph reading failed immediately:
its universal hypothesis is vacuous while its existential conclusion is false.
The residue is the explicit nonempty convention in `D001`, recorded as a scope
decision rather than hidden in prose.

## Adversarial check

Checked the logical negation and all graph orders below the first nonvacuous
example. In particular, verified that neither endpoint of a pair can count as its
own common neighbor in a simple loopless graph, and that “adjacent to every other
vertex” is vacuous for a singleton. Also checked that the external-solution report
was not entered as support for any claim.

## Canonical records changed

- [x] `STATEMENT.md`
- [x] `STATE.md`
- [x] `CLAIMS.md`
- [x] `OBLIGATIONS.md`
- [x] `PROOF.md`
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index

## Ending checkpoint

- Current frontier: a normalized, internally open graph-theory benchmark with no
  proof attempt yet
- Remaining blockers: `G002` (independent settlement), `G003` (future review),
  and `G004` (reference comparison deliberately blocked until the later phase)
- Best next action: create `A001` and perform an independent small-order and
  structural falsification pass without consulting known solutions
- Files a new session should read: `STATEMENT.md`, `STATE.md`, `CLAIMS.md`,
  `OBLIGATIONS.md`, `DECISIONS.md`, and this session record

## Plain-language recap

The conjecture now has a precise target and a clean benchmark boundary. We made
explicit that the graph must contain at least one vertex, because otherwise the
empty graph would defeat the wording for a purely logical reason. We checked the
smallest cases and sealed off known solutions and reference comparisons so the
next phase can develop an independent argument. Nothing in this intake proves the
general conjecture.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 85%
- Previous estimate, if any: none
- Reason for change: this is the first recorded estimate
- Basis: the statement is a concrete finite-graph problem and is reported to be
  externally solved, making independent resolution plausible. The main obstacle
  is that no structural mechanism has yet been derived, and the solution embargo
  intentionally prevents using the known route as a fallback.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
