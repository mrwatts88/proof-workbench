# Mathematical research toolkit

Choose tactics because they expose a falsifiable mechanism, not because they are
on a checklist.

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

