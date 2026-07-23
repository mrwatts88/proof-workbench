# Proof obligations

An obligation is resolved only when the resolution column links to an exact proof,
counterexample, decision, or certificate.

| ID | Obligation | Status | Blocks | Resolution |
|---|---|---|---|---|
| G001 | Normalize the statement, definitions, quantifiers, negation, and boundary conventions. | resolved | All research | `STATEMENT.md` version 0.2 and `S001` |
| G002 | Produce a self-contained proof or disproof of `C001` without consulting or intentionally reproducing a known solution. | resolved | Internal settlement of `C001` | `A001` and the integrated candidate in `PROOF.md` |
| G003 | Subject any eventual integrated candidate to the required adversarial reviews, including checks of the nonempty convention and quantifier order. | resolved | Promotion beyond `proof_candidate` | `R001` (logic and statement correspondence) and `R002` (hypotheses and counterexample audit) |
| G004 | Compare the internally developed and reviewed result with a reference solution. | not_needed | Optional comparison, not the exact mathematical claim | No reference was inspected before completion; `D003` records that comparison is outside completion of the internal result. The internal-only rule was later retired repository-wide (`O008`), so comparison is now freely permitted and simply optional. |
