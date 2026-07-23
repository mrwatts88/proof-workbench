# Review playbook

Use a review record from `templates/review.md`. Lead with findings and severity.

## Pass 1: statement correspondence

- Does the proof conclude the exact current statement?
- Were any quantifiers swapped or domains narrowed?
- Did nonemptiness, finiteness, connectedness, regularity, or choice enter silently?
- Are definitions used consistently?

## Pass 2: dependency and logic audit

- Build or inspect the claim dependency graph.
- Check for circularity and forward references that hide assumptions.
- Verify each case split is exhaustive and mutually sufficient.
- Negate key implications and search for a model satisfying the premises.
- Expand every “without loss of generality” and symmetry reduction.

## Pass 3: edge and adversarial cases

- zero, one, empty, singular, equality, and limiting cases;
- smallest dimensions or cardinalities;
- repeated elements, disconnected objects, nonunique optimizers;
- sign changes, characteristic effects, measurability, and convergence issues;
- alternative conventions in overloaded notation.

## Pass 4: imported results and computation

- Match every theorem hypothesis one by one.
- Verify the citation states the result at the used strength.
- Re-run decisive experiments from recorded commands and inputs.
- Check exact versus floating-point arithmetic, search completeness, integer
  overflow, solver assumptions, and certificate validation.

## Severity

- `critical`: invalidates the main conclusion or counterexample.
- `major`: leaves a substantial gap but likely preserves the strategy.
- `minor`: local omission, ambiguity, or presentation defect.
- `note`: nonblocking improvement or alternative.

Every critical or major finding becomes a `G###` obligation. A review is resolved
only when the resolution is checkable and linked, not when the author disagrees.

