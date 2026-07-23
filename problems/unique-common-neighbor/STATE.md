# Current state

- Last updated: 2026-07-23
- Problem: `P-001` — Unique Common Neighbor

## Exact target

Prove or disprove `STATEMENT.md` version 0.2: every finite, nonempty, simple
undirected graph in which each two distinct vertices have exactly one common
neighbor has a vertex adjacent to every other vertex.

## Established

- The statement, graph conventions, quantifiers, and negation are normalized.
- The one-vertex case satisfies the statement vacuously.
- `L001`: every vertex has even degree.
- `L002`: nonadjacent vertices have equal degree.
- `L003`–`L004`: a graph with no universal vertex would have connected
  complement and would be regular.
- `L005`: the resulting regular case contradicts an exact adjacency-matrix trace
  calculation.
- The integrated proof in `PROOF.md` passed two distinct fresh-context audits:
  `R001` (statement/logic) and `R002` (hypotheses/counterexamples).

## Evidence, not proof

- The user reports that the conjecture is externally solved. This is provenance
  only and supplies no internal mathematical support.

## Resolved review and optional follow-up

- `G003`: resolved by `R001` and `R002`.
- `G004`: reference comparison remains unperformed; it is freely permitted and
  simply optional, and is not needed to establish the internal result.

## Residual risks

- No proof obligation is open. The remaining risk is the ordinary possibility of
  an error missed by two finite human/agent reviews, rather than an identified
  gap.
- As a historical fact, no known solution or external source was consulted
  during development; the internal-only rule behind that has since been retired
  repository-wide (`O008`), and consultation is now freely permitted.

## Best next action

No action is required for the settled internal statement. An optional
provenance task may compare the proof with a reference solution at any time.

## Human-level state

The proof is complete under this repository's standard. Any supposed
counterexample would have to give every vertex the same number of neighbors; an
exact matrix count then says such a graph can only be the triangle, which is not a
counterexample. Two fresh reviewers tried different ways to break that argument;
one found and resolved a minor omitted explanation, and neither found a logical
gap.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 100%
- Previous estimate: 95%
- Reason for change: the internal proof passed all required independent review
  gates and has no unresolved conclusion-blocking obligation.
- Basis: the self-contained argument has two distinct fresh-context reviews, one
  minor clarity issue was repaired, and no imported theorem or computation is
  essential.

## Resume reading

1. `STATEMENT.md`
2. `CLAIMS.md`
3. `OBLIGATIONS.md`
4. `PROOF.md`
5. `PROOF.md`
6. `reviews/R001-statement-correspondence-and-logic-audit.md`
7. `reviews/R002-hypotheses-and-counterexample-audit.md`
