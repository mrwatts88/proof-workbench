# Textbook classics imported by A024 (S023)

Recorded per the epistemic rule that every external theorem carries a
precise statement, matched hypotheses, and a source. These are
foundational textbook results, imported at verified strength; no
research-level claim is imported here.

## Menger's theorem, global vertex form, case k = 2 (Whitney's characterization)

**Statement imported.** A graph \(G\) with \(|V(G)|\ge3\) is
2-connected if and only if every two distinct vertices of \(G\) are
joined by at least two internally disjoint paths (paths sharing no
vertex except their common endpoints).

**Use.** Only the forward direction (2-connected ⟹ two internally
disjoint paths between any two distinct vertices) is consumed, in
`A024` T2 (the fan corollary: an \(s\)–\(t\) path through any third
prescribed vertex \(w\), obtained by applying the statement to \(w\)
and an apex vertex \(z\) adjacent exactly to \(s,t\)).

**Sources.** K. Menger, *Zur allgemeinen Kurventheorie*, Fund. Math.
10 (1927), 96–115 (general form); H. Whitney, *Non-separable and
planar graphs*, Trans. Amer. Math. Soc. 34 (1932), 339–362 (the
2-connected characterization). Modern exposition: R. Diestel, *Graph
Theory*, 5th ed., Springer GTM 173 (2017), Theorem 3.3.6 (Menger,
global version) and Section 3.1; J. A. Bondy and U. S. R. Murty,
*Graph Theory*, Springer GTM 244 (2008), Theorem 5.1 and Section 9.1.

**Hypothesis match.** `A024` T2 applies the statement to \(G+z\),
which is verified 2-connected inline (removal of any single vertex
leaves a connected graph) and has \(\ge4\ge3\) vertices; the two
vertices joined are \(w\ne z\). No other part of Menger's theorem
(higher \(k\), edge forms, set-to-set forms) is used.

## Block structure (facts B1–B3 of A024)

**Statements imported.** For a finite connected graph \(H\): the
blocks of \(H\) are its maximal connected subgraphs having no cut
vertex of their own (each is 2-connected or a single edge); (B1) two
distinct blocks share at most one vertex, and any shared vertex is a
cut vertex of \(H\), so a vertex in two or more blocks is a cut
vertex; (B2) the block–cut tree (nodes = blocks and cut vertices,
block \(B\) adjacent to cut vertex \(c\) iff \(c\in B\)) is a tree
whose leaves are blocks, and for a cut vertex \(x\) the components of
\(H-x\) correspond to the subtrees of \(T-x\); (B3) every cycle lies
inside a single block, necessarily 2-connected.

**Sources.** Diestel, *Graph Theory*, 5th ed., Section 3.1 (blocks and
the block graph, Lemma 3.1.1, Lemma 3.1.4); Bondy–Murty, *Graph
Theory*, GTM 244, Section 5.2 (Proposition 5.2, Theorem 5.2, the
block tree). B3 follows from B1 because a cycle is a connected
subgraph without a cut vertex of its own, hence contained in one
block, and a single edge carries no cycle. Two immediate consequences
also consumed by `A024` T1 (itemized per `R002` F8): every vertex of a
connected graph on \(\ge2\) vertices lies in at least one block (it
has an edge, and every edge lies in a block), and distinct blocks are
edge-disjoint (an edge's two endpoints lie in any block containing it,
and two blocks share at most one vertex by B1).

**Use.** `A024` T1 (the taut block chain) and T4 (Lemma A). The fan
consequence "every 2-connected two-terminal graph is vertex-taut" was
already recorded as a classical remark in `A022` (there explicitly
*not consumed*); `A024` T6(a) now consumes it through T2's inline
proof, so no additional import is created by that step.
