# Source audit — 2026-07-23, session S007 (frontier sweep)

Scope: the computational frontier from primary sources, the 24-vertex
extremal graphs, and the deliberate novelty sweep for the edge-maximal
power-cycle saturation reduction (`L008`–`L016`), per obligations `G004` and
`G011`. Only sources actually inspected are recorded as support; search
snippets located sources but are never themselves mathematical support.

## Primary source: Markström (2004), inspected in full

- K. Markström, “Extremal graphs for some problems on cycles in graphs,”
  *Congressus Numerantium* 171 (2004), 179–192. PDF obtained from the
  author's university page and read in full (15 pages):
  <http://abel.math.umu.se/~klasm/Uppsatser/cycex.pdf> (downloaded
  2026-07-23).
- Section 4 states Conjecture 4.1 exactly as `STATEMENT.md` version 0.1:
  “Every graph with minimum degree at least 3 contains a cycle whose length
  is a power of 2,” attributed to Erdős and Gyárfás, 1995, with the
  \$100/\$50 prizes.
- On Royle's general search, the paper says: Royle “used a modified version
  of Brendan McKay's graph generator makeg … to generate graphs without
  \(C_4\)'s and the described degree structure. Royle generated all
  relevant graphs on **less than 16 vertices** and found no
  counterexamples.” The described structure — an independent set of
  degree-\(\ge4\) vertices, all other vertices of degree \(3\) — is valid
  for an order-then-size minimal counterexample (removing an edge between
  two degree-\(\ge4\) vertices preserves the hypotheses), so emptiness
  below \(16\) excludes all counterexamples below \(16\).
- On the cubic search: “We used Gunnar Brinkman's cubic graph generator
  minibaum to generate all cubic graphs on **less than 29 vertices** and a
  simple fortran program to check for the existence of cycles of length
  4, 8 and 16. No counterexamples to the conjecture was found.” Since a
  cubic graph has even order, exhausting orders \(\le 28\) gives: every
  cubic counterexample has at least \(30\) vertices. (For \(n\le 28<32\),
  the only power-of-two lengths are \(4,8,16\), so the three checks are
  exhaustive.)
- On the extremal graphs: “However on 24 vertices we found the smallest
  cubic graphs without cycles of lengths 4 and 8. These graphs are
  displayed in Fig. 14. We note that the lower right of the four graphs can
  be constructed from \(K_4\) by repeatedly expanding vertices into
  triangles, it is also the only planar graph among the four.” Table 3
  gives the counts of cubic graphs with no \(C_4\) and no \(C_8\):
  \(4\) at order \(24\), \(23\) at order \(26\), \(251\) at order \(28\).
  The four graphs appear only as drawings; no adjacency data is printed.
- The paper contains no occurrence of saturation, edge-maximality, or
  edge-addition arguments for this conjecture.

## Primary source: Royle's search page (2002), inspected via archive

- G. Royle, “The \(2^n\) conjecture,” formerly at
  `http://www.cs.uwa.edu.au/~gordon/remote/erdosconj.html`; the live page is
  gone. Wayback Machine snapshots of 2000-09-29, 2002-06-25, and 2003-07-13
  exist; the 2002-06-25 snapshot was downloaded and read in full, and the
  2003 snapshot has the same content digest.
- Exact statements: “I have checked this conjecture for graphs on **up to 15
  vertices**.” The generator was McKay's `makeg`, modified to construct
  graphs with minimum degree \(3\), “no edges join two vertices of degree
  greater than three,” and no \(4\)-cycles; “the graphs so constructed are
  then examined for 8-cycles.” His table reports the counts of such graphs
  at orders \(9\)–\(15\) (\(0, 4, 5, 27, 138, 775, 5369\)) and states “All
  contain an abundance of 8-cycles.” A relaxed class allowing one
  degree-\(2\) vertex is also tabulated (used to rule out gluing
  constructions).
- Provenance note on the page: Bert Randerath informed Royle that the
  conjecture is due to Erdős and Gyárfás and “was presented by Erdős at the
  1995 South-Eastern conference at Boca Raton. Erdős offered \$100 for a
  proof and \$50 for a counterexample.”

## Discrepancy: the circulating “at least 17” is not supported

- Wikipedia (“Erdős–Gyárfás conjecture,” read 2026-07-23) asserts “any
  counterexample must have at least 17 vertices,” citing Markström (2004).
- Hegde–Sandeep–Shashank (arXiv:2410.22842v2) assert “a counterexample has
  at least 17 vertices, a cubic counterexample has at least 30 vertices
  [10],” citing Markström (a 2002 Umeå report version).
- Both primary sources actually verify only orders \(\le 15\) (“up to 15” /
  “less than 16”). Neither states a search of order \(16\). The correct
  imported bound is therefore: **every counterexample has at least 16
  vertices** (`C012`). The “17” appears to be an overread propagated
  between secondary accounts; it must not be imported. (If the unpublished
  2002 Umeå report version of Markström's paper checked one order more,
  no inspectable evidence of that survives; the Congressus version and
  Royle's own page agree on 15.)
- Consequence for this dossier: the published general-order frontier is
  \(16\), only two orders above the internally proved `L017` (\(\ge 14\)),
  and it has not moved since 2002.

## The Markström graph (House of Graphs 51419), obtained and verified

- House of Graphs entry 51419 “Markstroem Graph,” JSON API payload
  downloaded 2026-07-23 and stored verbatim as `E005/hog51419.json`
  (adjacency list, adjacency matrix, canonical graph6 form
  `Ws??W?@@?P?aA_?O?GG?a?@_?gA??a?@CO?CG?A@???a??D`).
- MathWorld's “Markström Graph” page describes it as the cubic planar
  24-vertex graph lacking \(C_4\) and \(C_8\) but containing \(C_{16}\),
  the only planar member of Markström's four, with cycle lengths
  \(3,5,6,7,9\)–\(24\); it cites the House of Graphs entry.
- Internal verification (`E005/verify_markstrom.py`, all checks passed):
  order \(24\), cubic, connected, non-bipartite, planar (nauty `planarg`),
  no \(C_4\), no \(C_8\) (codegree criterion plus the `E004` whole-graph
  detector), cycle spectrum exactly
  \(\{3,5,6,7\}\cup\{9,\dots,24\}\), and the adjacency-list graph is
  isomorphic to the stored canonical form (nauty `labelg`).
- New internal observation (`C015`): every one of its \(240\) nonedges
  carries a Mersenne witness path — lengths \(3\) (\(105\) nonedges),
  \(7\) (\(225\)), \(15\) (all \(240\)) — so adding **any** edge creates a
  \(C_4\), \(C_8\), or \(C_{16}\). It fails the `L008` saturation package
  only by already containing \(C_{16}\).

## Pirzada–Shah–Baskoro (2022), inspected pp. 337–340

- S. Pirzada, M. A. Shah, E. T. Baskoro, “On 2-power unicyclic cubic
  graphs,” *Electronic Journal of Graph Theory and Applications* 10 (1)
  (2022), 337–344, DOI 10.5614/ejgta.2022.10.1.24.
- Constructs, for each admissible size, cubic graphs containing exactly one
  power-of-two cycle (Theorem 2.1; a 94-vertex example has no
  \(C_4,C_8,C_{16}\) but a \(C_{32}\)). The constructions contain bridges,
  so they do not meet the 2-connected reductions here. The abstract's
  closing remark that the observation “impl[ies] that there does not exist
  a counter example” is a loose comment about their bridge family, not a
  proof of the conjecture; Carr (2026) confirms the conjecture remains
  open. Nothing is imported from this paper as support.
- It repeats the “at least 17” figure (secondary, not evidence) and cites
  Bensmail for arbitrarily large cubic graphs with no \(q\)-power cycle
  (\(q\ge3\); tangential here).

## Bensmail (2017), inspected in full

- J. Bensmail, “On \(q\)-power cycles in cubic graphs,” *Discussiones
  Mathematicae Graph Theory* 37 (1) (2017), 211–220, DOI
  10.7151/dmgt.1926; HAL open-access copy hal-01629942 read in full
  (7 content pages).
- Results, at exactly this strength: for every \(q\ge3\) there exist
  arbitrarily large **planar cubic** graphs with no \(q\)-power cycles
  (Theorems 1–4, split by cases \(q\ge6\), \(q=5\), \(q=4\), \(q=3\));
  and, for \(q=2\), arbitrarily large planar cubic graphs whose 2-power
  cycles all have length \(4\) only, or all have length \(8\) only
  (Discussion, via the two edge-gadgets of its Figure 8). The paper poses
  as open whether, for any \(2^k>8\), there are infinite cubic families
  whose only 2-power cycles have length exactly \(2^k\).
- Mechanism (relevant to route selection here): start from an internally
  cubic tree and raise leaf degrees with edge/vertex gadgets so that every
  leaf remains a cut vertex; all cycles are then confined to gadget
  regions, so the entire cycle spectrum is a fixed finite set independent
  of the order (e.g. \(\{3,\dots,2k+2\}\cup\{3k+9,\dots,14k+21\}\) in the
  \(q\ge6\) case), and the parameter is chosen so no power of \(q\) lies
  in the set. For \(q=2\) the powers are too dense for these bounded
  windows — the paper states its tools “do not apply for the case
  \(q=2\)”, confirming it as the hardest case.
- Consequence recorded for the portfolio: every Bensmail graph is
  1-connected by construction, so the confinement trick is exactly what
  the 2-connected block reduction (`L001`/`L011`) forbids for genuine
  counterexamples. The falsification-side question is whether a
  **2-connected** minimum-degree-\(3\) graph can gap its cycle spectrum at
  every power of \(2\) up to its order, against forced spectrum-density
  results (Bondy–Vince-type differ-by-\(\le2\) pairs; Sudakov–Verstraëte
  consecutive even lengths at given girth). Imported as `C017`.

## Reported but not inspected

- P. Salehi Nowbandegani, H. Esfandiari, “An Experimental Result on the
  Erdős-Gyárfás Conjecture in Bipartite Graphs” (14th Workshop on Graph
  Theory CID, 2011): reported by Hegde–Sandeep–Shashank as giving a
  \(30\)-vertex lower bound for bipartite counterexamples. The paper body
  was not obtained; no claim is imported. Saturated counterexamples are
  non-bipartite by `L008`, so this bound is peripheral to the current
  route.
- Gao–Shan (2022): the conjecture holds for \(P_8\)-free graphs; subsumed
  by the imported \(P_{13}\)-free theorem `C007`. Noted for completeness.
- P. Erdős, “Some old and new problems in various branches of
  combinatorics,” *Discrete Mathematics* 165/166 (1997), 227–231: body
  still inaccessible (ScienceDirect serves a robot challenge; the Rényi
  Erdős archive scans end at 1989; the 1979 Congressus paper of the same
  title is a different text). Statement correspondence continues to rest
  on the three primary papers plus Royle's page, which independently
  records the 1995 Boca Raton presentation.

## G011 novelty sweep for the saturation reduction

Question: does the edge-maximal power-cycle saturation reduction — pass to
an edge-maximal power-cycle-free counterexample so that every nonedge
carries a simple path of length \(2^k-1\) (`L008`), with the derived
structure `L009`–`L016` — appear anywhere in the literature?

Queries run 2026-07-23 (web search over indexed literature, including
arXiv):

1. “Erdős-Gyárfás conjecture saturated edge-maximal power of two cycles”
2. “saturation number / saturated graphs, cycles, power of 2, C4 C8 C16
   family”
3. “arXiv Erdős-Gyárfás / power of two cycle, saturated / saturation /
   edge maximal, 2024–2026”
4. “Mersenne path/cycle graph power of two 2^k−1 conjecture minimum degree
   witness”
5. Earlier session queries that located the EGC corpus (Markström, Royle,
   Carr, HSS, Hu–Shen, Daniel–Shauger, Shauger, Heckman–Krakovski,
   Liu–Montgomery, Sudakov–Verstraëte, Verstraëte, Pirzada et al.).

Full-text or targeted inspection for saturation language:

- Markström (2004): none (full read).
- Royle (2002 page): none (full read).
- Carr (arXiv:2605.22844): searched for “saturated / saturation /
  edge-maximal / maximal / adding edges” — none; deletion arguments only.
- Hegde–Sandeep–Shashank (arXiv:2410.22842v2): the only edge-adding is
  their generator's algorithmic extension of partial \(P_k\)-free graphs;
  no saturation of counterexamples.
- Hu–Shen and Liu–Montgomery: inspected during S004; interval/adjuster
  methods, no counterexample-saturation formalism.
- Pirzada–Shah–Baskoro (2022): none (pp. 337–340 read).
- Cycle-saturation literature (sat\((n,C_m)\), \(C_{2k}\)-saturated
  graphs, rainbow/game variants located by query 2): concerns single fixed
  cycles or generic families; no appearance of the power-of-two cycle
  family \(\{C_4,C_8,C_{16},\dots\}\) as a saturation target and no
  connection to Erdős–Gyárfás.

Verdict recorded for `G011`: **no appearance found.** The saturation
reduction and its Mersenne-witness structure remain, as far as this sweep
reaches, an internal asset of this project. Standing caveat: absence of
evidence from one indexed sweep is not proof of absence; any external
write-up must restate this check and the sweep should be repeated
skeptically before major investment or any novelty claim in a manuscript.

## Import consequences

- `C012` (new import): every counterexample has at least \(16\) vertices
  (Royle 2002 / Markström 2004, as above) — not \(17\).
- `C013` (new import): no cubic counterexample on fewer than \(29\)
  vertices (Markström 2004); with even cubic order, every cubic
  counterexample has at least \(30\) vertices.
- `C014` (new import): Markström's Table 3 counts (\(4/23/251\) at orders
  \(24/26/28\)), smallest at \(24\), exactly one planar at \(24\); the
  order-\(24\) line is being reproduced internally in `E005`.
- `C015` (internal, tested): the verified properties and full
  Mersenne-witness coverage of the Markström graph, as above.
