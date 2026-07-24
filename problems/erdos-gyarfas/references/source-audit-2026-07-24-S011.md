# Source audit — S011 (2026-07-24): cycle-length intervals, mod-k results, and ring constructions at minimum degree 3

Purpose: the deliberate literature sweep required by the S010 handoff before
formulating the walk-to-cycle transfer target. Each entry states exactly what
was inspected and at what strength the fact may be cited. Imported rows are
mirrored in `CLAIMS.md`.

## Inspected in the primary source (PDF pages read)

### Bondy–Vince 1998 — imported as `C024`

J. A. Bondy and A. Vince, "Cycles in a graph whose lengths differ by one or
two," *Journal of Graph Theory* 27 (1998) 11–15. Pages 11–13 of the published
PDF were read directly (via the copy at
`people.clas.ufl.edu/avince/files/Cycles.pdf`).

Exact statements, quoted:

- **Theorem 1.** "With the exception of \(K_1\) and \(K_2\), every simple
  graph having at most two vertices of degree less than three contains two
  cycles whose lengths differ by one or two."
- **Theorem 2.** "Every nonbipartite 3-connected graph has two cycles whose
  lengths differ by one."
- Extension stated in prose: with exactly twelve exceptions (\(K_1\), \(K_2\),
  \(C_3\), \(P_3\), \(K_{2,3}\), and the seven graphs obtained from
  \(C_3, P_3, K_{2,3}\) by attaching a single pendant edge to one or more
  vertices of degree two), every simple graph having at most **three** vertices
  of degree less than three contains two cycles whose lengths differ by one or
  two.
- **The ring remark (page 12), quoted:** "Concerning Theorem 2, the
  3-connectedness requirement is necessary. If it is assumed instead that
  \(G\) is 2-connected and, in addition, that every vertex has degree at least
  \(d\), the corresponding statement is false. The counterexample (for
  \(d=3\)) in Figure 1 has only cycles of lengths 4, 6, 9, 11, 13 and 15. This
  example can easily be generalized to an infinite family of counterexamples
  by attaching a sufficiently large odd number of copies of \(K_{d,d}-e\) in a
  ring, as in the figure."

Reading of the ring remark (our reconstruction, checked against the reported
spectrum): copies of \(K_{3,3}-e\) have the two ex-endpoints of the deleted
edge as degree-2 terminals in opposite parts; all terminal-to-terminal simple
path lengths are 3 or 5; identifying terminals of consecutive copies around a
ring of \(L\) copies gives a 2-connected graph of minimum degree 3 whose
cycles are the gadget-internal cycles (lengths 4 and 6) plus the global cycles
(one through-path per copy, lengths \(\sum s_i\), \(s_i\in\{3,5\}\); for
\(L=3\): 9, 11, 13, 15 — matching the quoted spectrum exactly). This is the
**ring-of-gadgets mechanism**: 2-connected minimum-degree-3 graphs with large
multiplicative gaps in the cycle spectrum. Bondy–Vince use it against
"lengths differ by one"; its gadget contains \(C_4\), so it says nothing
directly about power-of-two cycles.

## Inspected at abstract strength only (full text not read)

### Gao–Huo–Liu–Ma — imported as `C025`

J. Gao, Q. Huo, C.-H. Liu, J. Ma, "A unified proof of conjectures on cycle
lengths in graphs," *International Mathematics Research Notices* 2022 (10),
7615–7653; arXiv:1904.08126. Statements taken from the arXiv abstract:

- Every graph with minimum degree at least \(k+1\) contains cycles of all
  even lengths modulo \(k\); if in addition 2-connected and non-bipartite,
  cycles of all lengths modulo \(k\).
- For all \(k\ge3\), every \(k\)-connected graph contains a cycle of length
  \(\equiv0\pmod k\).
- Every 3-connected non-bipartite graph with minimum degree at least \(k+1\)
  contains \(k\) cycles of consecutive lengths.
- Every graph with chromatic number at least \(k+2\) contains \(k\) cycles of
  consecutive lengths.
- They also prove a tight minimum degree condition for paths between two
  *given* endpoints whose lengths form a long arithmetic progression with
  common difference one or two (exact threshold not visible in the abstract).

At minimum degree exactly 3 these specialize to: 3-connected non-bipartite
graphs have two cycles of consecutive lengths (\(k=2\)); every 3-connected
graph has a cycle of length divisible by 3. The mod-\(k\) and long-AP
machinery all require minimum degree \(\ge k+1\), so they add nothing at
degree 3 beyond `C024`.

### Carr 2025 (diameter 2) — imported as `C026`

A. Carr, "Cycles of Length 4 or 8 in Graphs with Diameter 2 and Minimum
Degree at Least 3," arXiv:2508.19302 (August 2025). Abstract statement: every
graph of diameter 2 and minimum degree at least 3 contains a cycle of length
4 or 8; the note confirms the Erdős–Gyárfás conjecture for diameter-2 graphs.
Preprint; external proof not verified here.

### Carr 2026 (minimal counterexamples predominantly cubic)

A. Carr, "Every Minimal Counterexample to the Erdős–Gyárfás Conjecture is
Predominantly Cubic," arXiv:2605.22844 (May 2026). Abstract content: every
vertex of a minimal counterexample is adjacent to a vertex of degree exactly
3; at least \(4/7\) of the vertices have degree exactly 3; every regular
minimal counterexample is cubic. This matches the strengths already imported
as `C004`–`C006` (recorded in `references/source-audit-2026-07-23.md`); the
arXiv identifier is now on record. No new import needed.

## Context inspected, deliberately not imported

- **Sudakov–Verstraëte,** "Cycle lengths in sparse graphs," *Combinatorica*
  28 (2008); arXiv:0707.2117 (abstract). Number of cycle lengths
  \(\Omega(d^{\lfloor(g-1)/2\rfloor})\) for average degree \(d\) and girth
  \(g\); their consecutive-even-lengths theorem requires average degree of
  order \(192(k+1)\) (secondary reports); for EGC they bound the average
  degree of power-cycle-free \(n\)-vertex graphs by \(e^{O(\log^* n)}\),
  which is superseded by the constant bound of Liu–Montgomery (imported as
  `C008`). Nothing applicable at average degree 3; **in particular the swept
  literature does not settle EGC for minimum degree 3 with large girth.**
- **Bai–Grzesik–Li–Prorok,** "Cycle lengths in graphs of given minimum
  degree," *JCTB* 180 (2026); arXiv:2511.03085 (abstract). For 2-connected
  graphs with minimum degree \(k\ge4\): \(k\) cycles in arithmetic
  progression with difference one or two, and mod-\(k\) statements, with
  listed exceptions. Hypotheses start at \(k\ge4\); nothing at degree 3.
- **D. West's open-problem page** on the conjecture
  (`dwest.web.illinois.edu/openp/2powcyc.html`): partial results recorded
  there (Daniel–Shauger planar claw-free; Shauger \(K_{1,m}\)-free) are
  already imported; no reductions, constructions, or ring-type remarks
  appear. Caro's weaker question (cycle of perfect-power length) is noted
  there.
- **Bensmail** (`C017`, read in full during S007): his \(q\)-power spectrum
  confinement uses bounded gadgets on an internally cubic **tree** —
  1-connected assemblies with bounded total spectrum; he states the tools do
  not apply at \(q=2\). The Bondy–Vince **ring** is the 2-connected assembly
  shape with unbounded (but gapped) spectrum.

## Targeted novelty check

A direct search for ring/gadget/two-terminal constructions against
Erdős–Gyárfás ("ring gadget", "cycle spectrum", "two-terminal", counterexample
construction) found no treatment in the indexed literature beyond the
Bondy–Vince figure itself. The atom reduction recorded in `A011` is therefore
not known to appear elsewhere, with the standing caveat that this sweep, like
`G011`'s, must be repeated skeptically before any external novelty claim.
