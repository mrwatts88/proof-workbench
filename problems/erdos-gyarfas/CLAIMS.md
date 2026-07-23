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

## Dependency notes

- `L001`–`L004` are conditional structural consequences of the negation of
  `C001`; none proves `C001`.
- `L003` is independent of `E001`. The computation is retained as a
  reproducibility and implementation check, not as the proof of `L003`.
- No imported theorem or external status claim is used.
