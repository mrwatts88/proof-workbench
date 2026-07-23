# Source audit — 2026-07-23

This note records only sources actually inspected during `S002` or `S003`.
Search-result snippets and secondary problem pages were used to locate sources
but are not treated as mathematical support.

## Exact statement and original attribution

- P. Erdős, “Some old and new problems in various branches of combinatorics,”
  *Discrete Mathematics* 165/166 (1997), 227–231,
  DOI: <https://doi.org/10.1016/S0012-365X(96)00173-2>.
- The publisher bibliographic page was inspected, but the article body was not
  accessible. The original source is therefore identified but not directly
  verified.
- Three later primary research papers below state the same target as
  `STATEMENT.md` version 0.1: finite simple graphs of minimum degree at least
  \(3\), with a cycle whose length is a power of \(2\). Hegde–Sandeep–Shashank
  date the conjecture to 1994 and explain that the wording appeared in the 1997
  paper.

## Current general status and minimal counterexamples

- A. Carr, “Every Minimal Counterexample to the Erdős–Gyárfás Conjecture is
  Predominantly Cubic,” arXiv:2605.22844v1 (13 May 2026),
  <https://arxiv.org/abs/2605.22844>.
- Scope inspected: abstract, definitions, Lemma 0.1, Corollaries 0.1–0.2,
  Theorem 0.1, proofs, and references.
- The paper explicitly reports that the general conjecture remains open as of
  its submission.
- Its “minimal counterexample” minimizes order and then size, matching the
  convention relevant here. It proves:
  1. every proper subgraph has minimum degree at most \(2\);
  2. every vertex has a neighbor of degree exactly \(3\);
  3. vertices of degree at least \(4\) form an independent set;
  4. at least \(4/7\) of all vertices have degree exactly \(3\).
- Item 3 was independently proved in `A001/L002` before this source was
  inspected. Carr attributes that observation to Markström. Items 1, 2, and 4
  are imported as `C004`, `C005`, and `C006`; their hypotheses exactly match
  an order-then-size minimal counterexample to `C001`.

## Induced-path frontier

- A. S. Hegde, R. B. Sandeep, and P. Shashank, “Erdős–Gyárfás conjecture on
  graphs without long induced paths,” arXiv:2410.22842v2 (11 February 2025),
  <https://arxiv.org/abs/2410.22842>.
- Scope inspected: full HTML paper, algorithm statement, correctness lemma,
  Theorems 0.1–0.2, implementation discussion, and correctness-testing
  appendix.
- Theorem 0.2 is computer-assisted: every \(P_{13}\)-free graph of minimum
  degree at least \(3\) contains a \(4\)- or \(8\)-cycle. Thus any
  counterexample to `C001` contains an induced \(P_{13}\). This is imported as
  `C007`; the present repository did not reproduce their C++ computation.
- The paper reports earlier exact-search bounds, including at least \(30\)
  vertices for a cubic counterexample, and exhibits four cubic graphs on
  \(24\) vertices with no \(4\)- or \(8\)-cycle but with a \(16\)-cycle.
  These reported computations were not reproduced here.

## Earlier induced-path and high-average-degree results

- Z. Hu and C. Shen, “Erdős–Gyárfás Conjecture for \(P_{10}\)-free Graphs,”
  arXiv:2308.05675v2 (12 August 2023), published in *Discrete Mathematics*
  347 (2024), 114175, <https://arxiv.org/abs/2308.05675>.
- Scope inspected: abstract, introduction, stated theorem, and literature
  summary. The paper proves that every \(P_{10}\)-free graph of minimum degree
  at least \(3\) has a \(4\)- or \(8\)-cycle. The stronger \(P_{13}\)-free
  result above subsumes it for the present route.
- H. Liu and R. Montgomery, “A solution to Erdős and Hajnal’s odd cycle
  problem,” arXiv:2010.15802v2 (19 September 2022), published in *JAMS* 36
  (2023), 1191–1234, <https://arxiv.org/abs/2010.15802>.
- Scope inspected: abstract and the proof overview relevant to even path
  lengths. The authors prove that some absolute average-degree threshold
  forces a power-of-two cycle. This is imported as `C008`; the threshold is not
  specialized to minimum degree \(3\).
- During `S004`, Theorem 1.1, Corollary 1.3, and the proof outline were
  re-inspected. Theorem 1.1 produces an interval of consecutive even cycle
  lengths \([\log^8\ell,\ell]\) once the average degree exceeds an absolute
  threshold, and Corollary 1.3 specializes the method to powers of two. This
  confirms the exact strength of `C008` but supplies no low-degree conclusion
  applicable directly at minimum degree \(3\).

## Cubic graphs of large girth

- N. Biggs, “Constructions for cubic graphs with large girth,” *Electronic
  Journal of Combinatorics* 5 (1998), #A1,
  <https://doi.org/10.37236/1386>.
- Scope inspected during `S003`: abstract, Sections 1–3, and especially
  Theorem 3.2 and its proof.
- Theorem 3.2 starts from a disjoint union of cycles of total order \(2^g\)
  and girth at least \(g\), and adds a matching to produce a cubic graph of
  girth at least \(g\). Taking the initial 2-factor to be one cycle produces a
  finite Hamiltonian cubic graph of girth at least \(g\).
- This existence theorem is imported as `C009`. Applied with \(g=17\), it is
  the external input to the internally proved separation result `A004/L007`.

## Consequences for this dossier

- The statement correspondence is strongly corroborated, but the original
  1997 article body remains uninspected.
- `L005` and `L006` are valid internal small-order results but are weaker than
  reported prior computational bounds. They must not be described as new or
  state of the art.
- Continuing one order at a time is not the best main strategy. `A004/L007`
  shows that the induced path forced by `C007` plus the cubic conclusions
  `C004`–`C006` cannot, even with the absence of \(C_4,C_8\), force
  \(C_{16}\). A scalable route needs an additional genuinely global
  restriction, potentially involving variable-length path/ear constructions
  suggested by the Liu–Montgomery method.
