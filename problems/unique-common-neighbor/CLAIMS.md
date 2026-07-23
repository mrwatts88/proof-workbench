# Claim ledger

Use stable IDs and the states in `process/records.md`. Split claims until each row
has one independently checkable assertion.

| ID | Type | Assertion | State | Support | Dependencies |
|---|---|---|---|---|---|
| C001 | main claim | See `STATEMENT.md` version 0.2. | proved | Self-contained derivation in `PROOF.md`, reviewed in `R001` and `R002` | D001–D004, L001–L005 |
| C002 | boundary observation | The one-vertex graph satisfies the normalized statement. | proved | Direct vacuity check in `STATEMENT.md`, “Boundary and degenerate cases” | D001, D004 |
| C003 | boundary observation | No graph on exactly two vertices satisfies the unique-common-neighbor hypothesis. | proved | Direct loopless-graph check in `STATEMENT.md`, “Boundary and degenerate cases” | D001–D003 |
| C004 | example | \(K_3\) satisfies the hypothesis and conclusion. | proved | Direct neighborhood check in `STATEMENT.md`, “Boundary and degenerate cases” | D001–D004 |
| L001 | lemma | Every vertex has even degree. | proved | `A001`, `PROOF.md` Step 2 | D001–D003 |
| L002 | lemma | Any two nonadjacent vertices have equal degree. | proved | `A001`, `PROOF.md` Step 3 | D001–D003, L001 |
| L003 | lemma | If no vertex is universal, then \(\overline G\) is connected. | proved | `A001`, `PROOF.md` Step 4 | D001–D004 |
| L004 | lemma | If no vertex is universal, then \(G\) is regular. | proved | `A001`, `PROOF.md` Step 5 | L002, L003 |
| L005 | lemma | No regular graph satisfying the hypothesis can lack a universal vertex. | proved | `A001`, `PROOF.md` Step 6 | C002, D001–D004, L001, L004 |

## Dependency notes

- `C001` has a self-contained integrated derivation and has passed the required
  distinct adversarial reviews (`R001`, `R002`).
- `C002`–`C004` are boundary checks only and do not materially establish `C001`.
- The main dependency chain is
  \(L001\rightarrow L002\), \(L002+L003\rightarrow L004\), and
  \(L001+L004\rightarrow L005\rightarrow C001\).
