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
| C009 | large-girth existence theorem | For every integer \(g\ge3\), there is a finite Hamiltonian cubic graph of girth at least \(g\). | imported | Biggs (1998), Theorem 3.2, taking the prescribed 2-factor to be one cycle; `references/source-audit-2026-07-23.md` | Finite simple graph conventions |
| L007 | separation lemma | The minimal-counterexample conclusions `L002` and `C004`–`C006`, together with the induced-\(P_{13}\) conclusion drawn from `C007` and the absence of \(C_4,C_8\), do not force a \(C_{16}\). | proved | `A004/L007` | `C009` |
| C010 | computational observation | No cubic graph on \(18\) vertices contains an induced \(P_{13}\) while avoiding both \(C_4\) and \(C_8\). | tested | `E003` | Exact reduction and family definition in `E003/README.md` |
| L008 | saturation reduction | If a counterexample exists, one exists which is edge-maximal on its vertex set while remaining power-cycle-free; every nonedge is then joined by a simple path of length \(2^k-1\), and the graph is connected, non-bipartite, and below the average-degree threshold in `C008`. | proved | `A005/L008` | `D001`–`D004`, `C008` |
| L009 | separation lemma | A finite connected bipartite cubic graph of girth at least \(17\) satisfies the prior connected-cubic and induced-\(P_{13}\) bundle while avoiding \(C_4,C_8,C_{16}\), but it fails the Mersenne-path saturation conclusion of `L008`. | proved | `A005/L009` | `C009`, `A004/L007` |
| L010 | structural lemma | In a saturated counterexample supplied by `L008`, the edges which belong to no odd cycle form a matching. | proved | `A005/L010` | `L008` |
| L011 | reduction | If a counterexample exists, there is a non-bipartite 2-connected power-cycle-free block with at most one degree-\(2\) vertex such that every nonedge whose endpoints are not exceptional has an internal simple path of length \(2^k-1\). | proved | `A005/L011` | `L001`, `L008`, `L010` |
| L012 | ear lemma | In the block from `L011`, a shortest odd cycle of length at least \(7\) has an external ear contained in the union with a saturation witness between two nonexceptional cycle vertices. | proved | `A005/L012` | `L011` |
| L013 | ear lemma | Every shortest odd cycle in the block from `L011`, including a triangle or \(5\)-cycle, has an external ear. | proved | `A005/L013` | `L011` |
| L014 | separation lemma | A shortest odd cycle plus one arbitrary external ear does not force a power-of-two cycle: theta path lengths \(2,2r+1,4\) for \(r\ge2\) give only cycle lengths \(2r+3,2r+5,6\). | proved | `A005/L014` | Finite simple graph conventions |
| L015 | separation lemma | A full one-excursion `L012` witness — total length \(2^k-1\), both cycle arcs, both gaps, induced shortest odd cycle, non-Mersenne arc choice — admits infinitely many power-free realizations in every attachment configuration (aligned or crossed, each arc trivial or not, \(d\in\{2,4\}\)), so one-excursion witness data forces no power-of-two cycle. | proved | `A005/L015` | `A005/L012` for the setting; finite simple graph conventions |
| L016 | separation lemma | Full two-excursion witness data also forces no power-of-two cycle: for every \(k\ge4\), the double-theta graph on \(C_7\) with disjoint ears of length \(2^{k-1}-1\) attached at \(\{c_0,c_4\}\) and \(\{c_5,c_2\}\) realizes a witness of length \(2^k-1\) for the distance-\(2\) pair \(c_0,c_2\), and its seven cycle lengths \(7,2^{k-1}+3,2^{k-1}+3,2^{k-1}+2,2^{k-1}+2,2^k+1,2^k+2\) contain no power of two. | proved | `A005/L016` | Finite simple graph conventions |

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
- `C009` is used only for finite cubic large-girth existence. `L007` derives
  the induced \(P_{13}\) and the recorded structural conclusions directly; it
  does not assert that the large-girth graph avoids \(C_{32},C_{64},\ldots\).
- `L007` refutes only the proposed local \(C_{16}\)-forcing route, not `C001`.
  `C010` concerns a much smaller exact family and is not support for `L007`.
- `L008` uses edge-maximality under safe edge addition, not the edge-minimality
  in `L002`. Its minimum-order addendum controls subgraphs which omit vertices;
  it does not import the spanning-subgraph part of `C004`.
- `L009` uses a canonical bipartite double cover when the graph from `C009` is
  non-bipartite. It is a stress test for `L008`, not a counterexample to
  `C001`.
- `L010`–`L012` are consequences of the saturation witnesses. `L013` uses
  2-connectivity and the near-minimum-degree block directly. `L014` is only a
  separation example for one-ear length equations; its internal path vertices
  have degree \(2\), so it is not a counterexample to `C001` or to `L011`.
- `L015` and `L016` delimit the single-witness information content of `L012`:
  their theta and double-theta families satisfy every constraint visible to
  one witness, yet they contain internal degree-\(2\) vertices, so none is a
  counterexample to `C001` or to `L011`. Together they retire every bounded
  single-witness forcing pattern and fire the recorded pivot condition for
  the saturation-only route. They say nothing against saturation as a
  reduction, and `L008`–`L013` remain available as constraints.
