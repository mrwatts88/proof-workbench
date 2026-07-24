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
| C011 | computational observation | The exhaustive labelled search found no graph of order \(11\), \(12\), or \(13\) with minimum degree at least \(3\) avoiding both \(C_4\) and \(C_8\); five validation anchors reproduced the independent `E001`/`E002` counts, an exact symmetry quotient, and a nonzero \(C_8\)-free positive control. | tested | `E004` | Coverage layers proved in `A006/L017` |
| L017 | finite exclusion | Every counterexample has at least fourteen vertices. | proved | `A006/L017`, computer-assisted via the exhaustive search `E004` | `L006`, `E004` |
| C012 | reported computation | Royle's 2002 search — all graphs on at most \(15\) vertices with minimum degree \(3\), the degree-\(\ge4\) vertices independent, and no \(C_4\) — found every such graph to contain a \(C_8\); via the minimal-counterexample degree structure this gives: every counterexample has at least \(16\) vertices. The circulating "at least 17" has no primary-source support. | imported | Royle (2002 archived page) and Markström (2004), quoted in `references/source-audit-2026-07-23-S007.md`; external computation, not reproduced | The degree-structure reduction (internally `L002`'s independence conclusion plus order-minimality); `D001`–`D004` |
| C013 | reported computation | Markström's search of all cubic graphs on at most \(28\) vertices found each to contain a \(C_4\), \(C_8\), or \(C_{16}\); since cubic graphs have even order, every cubic counterexample has at least \(30\) vertices. | imported | Markström (2004), quoted in `references/source-audit-2026-07-23-S007.md`; external computation, not reproduced beyond order \(24\) | `D001`–`D004`; parity of cubic order |
| C017 | spectrum-confinement theorem | For every \(q\ge3\) there exist arbitrarily large planar cubic graphs with no \(q\)-power cycles; for \(q=2\) there exist arbitrarily large planar cubic graphs whose 2-power cycles all have length \(4\) only, or all length \(8\) only. All these constructions are 1-connected: cycles are confined to bounded gadgets around an internally cubic tree, so the cycle spectrum is a fixed finite set and the powers of \(q\ge3\) can be dodged; the paper states the tools do not apply at \(q=2\). | imported | Bensmail (2017), read in full; `references/source-audit-2026-07-23-S007.md` | Finite simple graph conventions |
| C014 | reported census | The smallest cubic graphs avoiding both \(C_4\) and \(C_8\) have \(24\) vertices; the counts of connected cubic \(\{C_4,C_8\}\)-free graphs are \(4\), \(23\), \(251\) at orders \(24\), \(26\), \(28\), each such graph found containing a \(C_{16}\); exactly one of the four at order \(24\) is planar. | imported | Markström (2004), Table 3 and Section 4; `references/source-audit-2026-07-23-S007.md`; the order-\(\le24\) part is reproduced internally as `C018` | `D001`–`D004` |
| C015 | computational observation | The Markström graph (House of Graphs 51419) is cubic, planar, connected, non-bipartite, of order \(24\), with cycle spectrum exactly \(\{3,5,6,7\}\cup\{9,\dots,24\}\); every one of its \(240\) nonedges carries a simple path of length \(15\) (and \(225\) of length \(7\), \(105\) of length \(3\)), so adding any single edge creates a \(C_4\), \(C_8\), or \(C_{16}\). | tested | `E005` Part 1 (`verify_markstrom.py`), all checks passed | Graph data from House of Graphs entry 51419; detectors from `E004` |
| C016 | computational observation | The exhaustive anchored census found no graph of order \(14\)–\(17\) with minimum degree at least \(3\) avoiding both \(C_4\) and \(C_8\): the connected \(C_4\)-free minimum-degree-\(3\) classes have sizes \(6059\), \(91433\), \(1655659\), \(34758006\) at orders \(14\)–\(17\), and every member contains a \(C_8\). | tested | `E006` (geng-generated, anchors A1–A5 passed, independent per-graph re-verification) | geng (nauty 2.9.3) correctness for the delegated class, anchored as recorded in `E006` |
| L018 | finite exclusion | Every counterexample has at least eighteen vertices; consequently the smallest \(\{C_4,C_8\}\)-free graph of minimum degree at least \(3\) has between \(18\) and \(24\) vertices. | proved | `A007/L018`, computer-assisted via `E006`/`C016` (generation layer delegated to anchored geng, unlike the fully internal `E004`) | `L017`, `C016`, connectivity and collapse lemmas in `A007` |
| C018 | computational reproduction | The connected cubic \(\{C_4,C_8\}\)-free census through order \(24\): empty at orders \(14\)–\(22\) (the \(C_4\)-free cubic classes of sizes \(36\), \(269\), \(2761\), \(36101\), \(553227\) all contain \(C_8\)), and at order \(24\) exactly four graphs among \(9{,}467{,}449\) \(C_4\)-free cubic graphs — matching Markström's Table 3 — of which exactly one is planar and labelg-isomorphic to House of Graphs 51419; all four contain \(C_{16}\), and each of the four is fully Mersenne-witness-covered: every one of its \(240\) nonedges carries a simple path of length \(3\), \(7\), or \(15\) (all \(240\) carry length \(15\)). | tested | `E005` Part 2 (`generate24.py`), planarity by nauty `planarg`, isomorphism by nauty `labelg` | geng anchored as in `E005`/`E006`; detectors from `E004`; upgrades the order-\(\le24\) part of `C014` from reported to reproduced |
| L019 | projection lemma | For every \(\mathbb{Z}_m\)-voltage assignment on a base multigraph satisfying the simplicity conditions, every cycle of length \(L\ge3\) in the derived graph projects to a tailless non-backtracking closed walk of length \(L\) in the base with net voltage \(\equiv0\pmod m\); hence if no such walk exists at any power length \(\le\) the lift's order (with lengths \(1,2\) encoding simplicity), the lift is a simple minimum-degree-\(\ge3\) graph with no power-of-two cycle. | proved | `A008/L019` | `D001`–`D004`; finite group conventions |
| L020 | gauge lemma | Voltage assignments differing by a coboundary yield isomorphic derived graphs; on a connected base every assignment is equivalent to one vanishing on a fixed spanning tree, so the assignment space is \((\mathbb{Z}_m)^\mu\) (\(\mu\) = cycle rank) and the net voltage of a closed walk is the pairing \(\nu\cdot x\) of its cycle-space vector with the free voltages. Unit scaling of assignments also preserves the isomorphism type. | proved | `A008/L020` | Finite group conventions |
| L021 | commutator obstruction | If \(W_1,W_2\) are non-backtracking closed walks at a common vertex of a multigraph satisfying the four arc conditions of `A008`, then \(W_1W_2\overline{W_1}\overline{W_2}\) is a tailless non-backtracking closed walk of length \(2(\lvert W_1\rvert+\lvert W_2\rvert)\) whose net voltage is zero under every abelian voltage assignment. Realizations: length \(8\) on the dumbbell, \(16\) on theta3 and \(K_4\), hence abelian lifts of these bases of sufficient order can never satisfy the L019 certificate at those power lengths. | proved | `A008/L021`; DP-independent witnesses in `E007/data/zero-vector-witnesses.txt` (also length 16 on the prism, 32 on \(K_{3,3}\), 4 on the bouquet, computed) | `L019` for the certificate reading |
| C019 | computational observation | The four verified order-24 extremal graphs contain exactly \(315\), \(330\), \(207\), \(228\) sixteen-cycles respectively; every edge lies on at least \(70\) of them and no edge lies on all of them (a fortiori no vertex), so the \(C_{16}\) obstruction at the extremal boundary is massively redundant and cannot be removed by local surgery. | tested | `E007` `calibrate`, `data/calibration-order24-c16.txt` | `C018` graph data; `E004` detectors |
| C020 | computational observation | Certificate verdict: for each of the six bases — the complete list of cycle-rank-2 minimum-degree-\(3\) multigraph bases (bouquet, theta3, dumbbell) plus \(K_4\), \(K_{3,3}\), prism — and every modulus \(m\ge2\), no \(\mathbb{Z}_m\) voltage assignment admits the L019 walk certificate of power-of-two-freeness: the exhaustive hyperplane sieve (both parities of \(m\)) leaves zero survivors below each base's first integer-zero-vector power length, and the integer zero vector kills every larger \(m\) outright. | tested | `E007` sieve outputs in `data/` | `L019`–`L021`; walk-class DP anchored A1–A8 |
| C021 | computational observation | Truth census: for every base and every \(m\) with lift order in \([12,30]\), over all voltage assignments of both parities, every simple derived graph contains a \(C_4\), \(C_8\), or \(C_{16}\); since these are the only power lengths \(\le30\), no counterexample to `C001` exists anywhere in the \(\mathbb{Z}_m\)-lift families of the six bases through order \(30\). In particular every simple circulant \(C_m(a,b)\) with \(m\le30\) contains a \(C_4\), and the \(48\) \(K_4\)-lifts of order \(28\) avoiding \(C_4\) and \(C_8\) all contain \(C_{16}\). | tested | `E007` `truth`, `data/truth-census-orders-12-30.txt` | `E004` detectors (independent of `L019`); consistent with `L017`, `L018`, `C013` |
| C022 | computational observation | Non-abelian certificate verdict: over \(\mathbb{Z}_7\rtimes\mathbb{Z}_3\) (order 21, metabelian), the Heisenberg group mod 3 and \(\mathbb{Z}_9\rtimes\mathbb{Z}_3\) (both order 27), and the perfect group \(A_5\) (order 60), every voltage assignment on the cycle-rank-2 bases (theta3, dumbbell, bouquet2) — and on \(K_4\) for the three solvable groups — is L019-certificate-dead by length \(16\): some tailless non-backtracking closed walk of length \(4\), \(8\), or \(16\) has identity net voltage. Zero survivors among all assignments (e.g. all \(3600\) per base over \(A_5\), certificate lengths through \(64\)). The pre-registered solvable-cascade predictions of `A009` are confirmed at or before their bounds; the \(A_5\) deaths match the collision-wall prediction \(2^k\approx2\log_2\lvert\Gamma\rvert\), and the wall mechanism (not yet a proved lemma) is recorded in `A009`/`E008`. | tested | `E008` `probe`, `data/probes-mu2-bases.txt`, `data/probes-k4-solvable.txt`; anchors incl. bidirectional agreement with the `E007` engine on cyclic groups | Group tables axiom-checked at runtime; `L019`/`L020` in their group-agnostic form (`A009`); certificate-level only — no statement about actual cycle spectra of the lifts |
| C023 | computational observation | The exhaustive anchored census at order \(18\): the connected \(C_4\)-free minimum-degree-\(3\) class has \(834{,}711{,}846\) members and every one contains a \(C_8\); no \(\{C_4,C_8\}\)-free graph of minimum degree at least \(3\) exists on \(18\) vertices. | tested | `E006` order-18 extension (S009: 48 geng parts, 8 PyPy workers; anchors A1–A5 re-passed under PyPy 7.3.23; empty survivor files `data/survivors_n18.*`) | geng (nauty 2.9.3) correctness for the delegated class, anchored as recorded in `E006`; same caveats as `C016` |
| L022 | finite exclusion | Every counterexample has at least nineteen vertices; consequently the smallest \(\{C_4,C_8\}\)-free graph of minimum degree at least \(3\) has between \(19\) and \(24\) vertices. | proved | `A007` addendum (S009), computer-assisted via the order-18 census `C023` | `L018`, `C023`, connectivity and collapse lemmas in `A007` |
| L023 | structure lemma | Arc-digraph structure of a finite connected multigraph \(B\) with \(\delta\ge3\): (i) no nonempty continuation-closed arc set is reverse-free; (ii) the non-backtracking arc digraph is strongly connected; (iii) its period is \(1\) or \(2\), equal to \(2\) exactly when \(B\) is bipartite, with class = tail side; (iv) there is a finite \(R_B\) such that every ordered arc pair is joined by an nb walk of every sufficiently large admissible exact length. (`A010` W2–W5.) | proved | `A010` (hand proofs, incl. inline numerical-semigroup sub-lemma); verified on six bases in `E009`; audited in `R001` (pass) | Finite multigraph conventions; no voltage content |
| L024 | collision-wall theorem | For every finite connected multigraph base \(B\) with \(\delta(B)\ge3\) (\(m\) edges), every finite group \(\Gamma\), and every voltage assignment: \(B\) has a tailless non-backtracking closed walk with identity net voltage of every length \(L\equiv0\pmod4\) with \(L\ge4\ell^*+4R_B+8\) (every even such \(L\) if \(B\) is non-bipartite), where \(\ell^*=\lfloor\log_2(2m\lvert\Gamma\rvert)\rfloor+2\); in particular of length \(2^k\) for every \(2^k\ge4\log_2\lvert\Gamma\rvert+C_B\) with \(C_B=4\lceil\log_2m\rceil+4R_B+24\). Corollary (scoped per `R001` F3): for each base there is \(\Gamma_0(B)\) such that for all \(\lvert\Gamma\rvert\ge\Gamma_0(B)\) the walk certificate fails at some power \(2^k\le n\lvert\Gamma\rvert\) — per-base effective closure of the certificate program; the small-group/large-base regime is not covered by this corollary. | proved | `A010` W7–W8 (hand proof); construction verified exhaustively in scope by `E009` (9,606,333 assertions) and by the independent R001 probe (108 cases, 3,136 lengths); audited in `R001` (pass, minor findings repaired) | `L023`; the group-agnostic form of `L019` (`A009`) for the certificate reading only |

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
- `L017` is computer-assisted, unlike the hand-proved `L005`–`L006`: its
  proof combines the proved small-order collapse and coverage arguments in
  `A006` with the exhaustive search `C011`/`E004`. At orders \(11\)–\(13\)
  the full \(\{C_4,C_8\}\)-free class was empty, so `L017` does not depend
  on `L008`. The cleared orders are below reported prior computational
  bounds in the literature; no novelty is claimed, and those prior
  computations were not reproduced or relied on here.
- `C012` and `C013` are external computations imported at reported
  strength; neither was reproduced here in full. `C012`'s reduction to the
  restricted degree structure is the elementary minimal-counterexample
  argument (the independence conclusion of `L002` plus order-minimality),
  so its search class covers all minimum counterexamples. The
  widely-circulated "at least 17 vertices" strengthening of `C012` is an
  overread with no primary-source support and must not be cited
  (`references/source-audit-2026-07-23-S007.md`). Orders \(11\)–\(16\) of
  the range covered by `C012` are independently confirmed internally
  (`E004`, `E006`); orders \(\le 24\) of `C013`'s range by `E005`.
- `C017` is a strategic import: its graphs satisfy the conjecture (or
  concern \(q\ge3\)) and none is 2-connected, so it does not intersect the
  block reduction `L011`; its value is the spectrum-confinement mechanism
  and the demonstration that 1-connectivity is what makes bounded cycle
  spectra — and hence power dodging — possible at minimum degree \(3\).
- `C015` records witness coverage, not `L008` saturation: the Markström
  graph contains a \(C_{16}\), so it is not power-cycle-free and not an
  `L008` object; the observation is that the Mersenne-witness half of the
  saturation condition is realizable by an actual extremal cubic planar
  graph at order \(24\).
- `L018` is computer-assisted like `L017`, but with a weaker internality:
  `E004`'s generation layer was internal and hand-proved, while `E006`
  delegates generation to nauty's geng, an imported tool anchored against
  OEIS A002851/A006786 counts, cross-validated against `E004` at orders
  \(11\)–\(13\), and re-checked per graph for the degree and \(C_4\)
  conditions. The connectivity and collapse lemmas of `A007` are hand
  proofs. `L018` strictly strengthens `L017`'s bound; `L017` remains the
  strongest bound with an internal generation layer.
- `L019`–`L021` are unconditional lemmas about voltage lifts (tools for
  the falsification program of `A008`), not reductions of `C001`; none
  bears on the truth of `C001` directly. `L019`'s certificate direction
  is one-sided: absence of zero-voltage walks proves absence of the
  corresponding cycle lengths, but a zero-voltage walk does not prove a
  cycle exists. `L021` is abelianization-specific: over a non-abelian
  voltage group the commutator word's net voltage is a genuine group
  commutator, generally nontrivial, so `L021` says nothing there.
- `C020` is a statement about the L019 *certificate*, not about the
  lifts' actual cycle spectra: it proves the cyclic-lift sieve can never
  output a counterexample candidate from the six bases, and nothing
  more. `C021` is truth-level (validated detectors on the explicit
  graphs) but finite: orders \(12\)–\(30\) only, six bases only. Neither
  claim covers non-abelian groups, other bases, or unbounded orders; the
  general-base effective version of the `L021` obstruction is open as
  `G012`.
- `C019` uses the `C018` graphs verbatim and the `E004` detectors plus an
  exact canonical cycle counter; it is calibration data for route
  selection, with no bearing on `C001`'s truth.
- `L022` extends `L018` by one order with an identical support
  structure: the `A007` connectivity and collapse lemmas are hand
  proofs, the computational leg is the same anchored pipeline at order
  \(18\) (`C023`), and every internality caveat recorded for `L018`
  applies verbatim. `L017` remains the strongest bound with a fully
  internal generation layer.
- `L023` and `L024` are voltage-lift program results, not reductions of
  `C001`; neither bears on the truth of `C001` directly. `L024`'s
  certificate corollary cites `L019` at its group-agnostic strength as
  proved in `A009` (the ledger row `L019` itself is stated for
  \(\mathbb Z_m\); `C022` already cites the group-agnostic form the same
  way). The corollary is per-base effective closure for
  \(\lvert\Gamma\rvert\ge\Gamma_0(B)\) plus the finite verdicts
  `C020`/`C022`; it does not cover a small fixed group on bases with
  large reach constant \(R_B\) (see `R001` F3 for a concrete such
  family). For bipartite bases the forced lengths are \(\equiv0\bmod4\)
  only (`R001` F4); powers of two are unaffected. `E009` and the `R001`
  probe verify the construction on finitely many instances; the
  universal claims rest on the `A010` proofs. Unlike `L017`–`L022`,
  `L023`/`L024` carry a delegated adversarial logic audit (`R001`,
  delegated-subagent, pass).
