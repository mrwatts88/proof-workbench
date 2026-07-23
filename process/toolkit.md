# Mathematical research toolkit

Choose tactics because they expose a falsifiable mechanism, not because they are
on a checklist.

## Strategy generation and recalibration

Separate the generative and critical phases:

1. **Generate mechanisms.** Seek explanations that would make the statement true
   or false: a conserved quantity, obstruction, extremal object, transformation,
   dual formulation, or source of counterexamples. Prefer mechanistic diversity
   over several cosmetic variants of one proof.
2. **Make them concrete.** For each serious route, name the first new claim it
   needs and the cheapest test that could distinguish it from wishful thinking.
3. **Compare research value.** Favor routes with high information gain and
   leverage on the main claim, not merely the shortest task or the easiest record
   to complete.
4. **Recalibrate.** Continue while the mechanism survives its tests; pivot when a
   hidden premise fails, the route reduces to the original claim, or a distinct
   route becomes clearly more informative.

Useful route roles are:

- **primary:** the best current route to a proof or disproof;
- **falsification:** a direct attack on the primary route's weakest premise;
- **alternative:** a different mechanism pursuing the same target;
- **reframing:** a change of representation that may expose a new invariant or
  obstruction.

Do not confuse novelty with randomness. A mature route that continues to gain
support may deserve exploitation; a fashionable new representation with no
decisive test does not. Conversely, do not keep an inherited route alive merely
because it is already documented.

## Normalize and negate

- Write the logical form with explicit quantifiers.
- Write the exact negation; it often reveals a counterexample search.
- Separate local, global, existential, and uniform claims.
- Check whether the conclusion is invariant under the proposed normalization.

## Counterexample search

- smallest parameter values and dimensions;
- empty, singleton, repeated, singular, disconnected, or extremal objects;
- equality cases of invoked inequalities;
- random search followed by exact reconstruction;
- constraint solving or exhaustive enumeration on a proved finite reduction;
- perturbation of assumptions and limiting examples.

Record the search space, pruning argument, seed, and completeness claim.

## Proof mechanisms

- direct deduction and contrapositive;
- contradiction or minimal counterexample;
- induction on the parameter that genuinely decreases;
- invariants, monovariants, potentials, and conservation laws;
- extremal principles and exchange arguments;
- compactness, diagonalization, and limiting arguments;
- algebraic normalization, factorization, and basis changes;
- probabilistic method and expectation bounds;
- double counting, generating functions, and bijections;
- decomposition into local lemmas with an acyclic dependency graph.

## Computation

Prefer, in order:

1. exact hand-checkable derivation;
2. exact arithmetic program;
3. solver output with a checkable certificate;
4. interval or formally bounded numerical computation;
5. floating-point exploration;
6. unrecorded interactive output.

The lower items are useful for discovery but require more work before they can
support a proof. Keep essential programs small, deterministic, and runnable from a
documented command. Record tool and dependency versions.

## External knowledge

For each imported theorem, record:

- a precise statement or a narrow paraphrase;
- source and location;
- required hypotheses;
- the mapping from current objects to the theorem;
- whether the source was inspected directly.

Search-result snippets and remembered theorem names are leads, not sources.

## Escalation choices

When stuck, prefer a precise change of representation:

- prove a smaller lemma;
- seek the weakest counterexample;
- strengthen the induction hypothesis;
- identify the first unjustified implication;
- isolate where a named assumption is used;
- translate the problem into an equivalent algebraic, combinatorial, geometric, or
  computational form;
- record a conditional theorem if a single difficult lemma is the true frontier.
