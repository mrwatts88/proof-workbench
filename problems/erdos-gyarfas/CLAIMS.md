# Claim ledger

Use stable IDs and the states in `process/records.md`. Split claims until each row
has one independently checkable assertion.

| ID | Type | Assertion | State | Support | Dependencies |
|---|---|---|---|---|---|
| C001 | main claim | Every finite simple undirected graph of minimum degree at least \(3\) contains a cycle of length \(2^k\) for some \(k\ge2\); see `STATEMENT.md` version 0.1. | proposed | — | `D001`–`D004` |
| L001 | reduction | Every counterexample contains a 2-connected power-cycle-free subgraph in which all but possibly one vertex have internal degree at least \(3\), and the possible exception has internal degree at least \(2\). | proved | `A001/L001` | `D001`–`D004` |
| L002 | structural lemma | An edge-minimal counterexample is connected, every edge has a degree-\(3\) endpoint, and hence its degree-\(\ge4\) vertices are independent. | proved | `A001/L002` | `D001`–`D004` |
| L003 | finite exclusion | Every counterexample has at least nine vertices. | proved | `A001/L003` | `D001`–`D004` |
| L004 | path lemma | At an endpoint \(v_0\) of a longest path \(v_0\ldots v_\ell\) in a counterexample, every neighbor is on the path and no chord \(v_0v_i\) has \(i=2^k-1\) for \(k\ge2\). | proved | `A001/L004` | `D001`–`D004` |
| C002 | computational observation | The exact labelled census found no counterexample among all graphs of minimum degree at least \(3\) through order \(7\) or among all cubic graphs through order \(8\). | tested | `E001` | `D001`–`D004` |
| L005 | finite exclusion | Every counterexample has at least ten vertices. | proved | `A002/L005` | `L002`, `L003` |
| L006 | finite exclusion | Every counterexample has at least eleven vertices. | proved | `A003/L006` | `L002`, `L005` |
| C003 | computational observation | Exhaustive degree-sequence backtracking found no edge-minimal counterexample of order \(9\) or \(10\). | tested | `E002` | `L002`, `L003` |
| C004 | minimality theorem | In a counterexample minimizing order and then size, every proper subgraph with defined minimum degree has a vertex of degree at most \(2\). | imported | Carr (2026), Lemma 0.1; `references/source-audit-2026-07-23.md` | `C001` negation and stated minimality |
| C005 | domination theorem | Every vertex of an order-then-size minimal counterexample has a neighbor of degree exactly \(3\). | imported | Carr (2026), Corollary 0.1(1); `references/source-audit-2026-07-23.md` | `C004` |
| C006 | density theorem | At least \(4/7\) of the vertices of an order-then-size minimal counterexample have degree exactly \(3\). | imported | Carr (2026), Theorem 0.1; `references/source-audit-2026-07-23.md` | `L002` |
| C007 | induced-path theorem | Every \(P_{13}\)-free graph of minimum degree at least \(3\) has a \(4\)- or \(8\)-cycle; consequently every counterexample contains an induced \(P_{13}\). | imported | Hegde–Sandeep–Shashank (2025), Theorem 0.2; `references/source-audit-2026-07-23.md` | `D001`–`D004` |
| C008 | high-average-degree theorem | There exists an absolute constant \(d\) such that every graph of average degree at least \(d\) contains a power-of-two cycle. | imported | Liu–Montgomery (2023); `references/source-audit-2026-07-23.md` | Their finite simple graph hypotheses |

## Dependency notes

- `L001`–`L004` are conditional structural consequences of the negation of
  `C001`; none proves `C001`.
- `L003` is independent of `E001`. The computation is retained as a
  reproducibility and implementation check, not as the proof of `L003`.
- `L005` and `L006` are independent of `E002`; the experiment located the
  structural cases, while `A002` and `A003` prove them.
- `L002` was proved internally before source inspection. Carr (2026) identifies
  its high-degree-independence conclusion as an earlier observation of
  Markström; no novelty is claimed here.
- `C004`–`C008` are imported at exactly the strength stated. They do not imply
  `C001`, and the external computations behind `C007` were not reproduced in
  this repository.
