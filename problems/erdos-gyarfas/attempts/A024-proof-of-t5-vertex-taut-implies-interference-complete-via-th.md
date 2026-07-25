# A024 — Proof of T5: vertex-taut implies interference-complete, via the block chain and the trimming construction

- Date opened: 2026-07-25
- Problem: `P-002`
- Status: closed (proof recorded and mechanically verified; delegated
  adversarial review recorded in `reviews/` — see Exit state for the
  verdict)
- Portfolio role: primary (Tier 1, `G015` case (5b), proof side; session
  `S023`)

## Intended mechanism

`A023` T5 records the candidate lemma of the interference program:

> **T5.** Let \((H,a,b)\) be vertex-taut — every vertex of \(H\) lies on
> a simple \(a\)–\(b\) path. Then every cycle of \(H\) is an
> interference cycle: the edge symmetric difference of two distinct
> simple \(a\)–\(b\) paths.

The recorded proof plan (`A023`) was a clean-window reroute plus a
minimal-choice exchange: pick a through-path \(P\) meeting the cycle
\(C\), control the pattern of its contact intervals, and exchange along
\(C\) until the trace is clean, with "weaving" (a path meeting \(C\) in
many disconnected intervals) as the named obstruction and cycle-edge
essentiality as a named sub-obligation.

This attempt proves T5 by a different and shorter mechanism found
during statement normalization, the **trimming construction**: instead
of controlling how a given path meets \(C\), take any \(a\)–\(b\) path
\(R\) through a *prescribed edge* of \(C\) (existence is exactly the
essentiality sub-obligation, proved below from tautness via the block
chain), keep only its prefix up to its **first** contact with
\(V(C)\) and its suffix from its **last** contact, and complete both
fragments through the two \(u\)–\(v\) arcs of \(C\). The discarded
middle of \(R\) is where all weaving lives; nothing about it needs to
be controlled. Both hybrid walks are automatically simple paths, and
their symmetric difference is exactly \(C\).

## Entry assumptions

- Statement 0.1 is not consumed: T5 is a structure theorem about
  arbitrary finite simple graphs with two distinguished vertices. No
  \(C_4\)-freeness, no degree condition, no power-freeness is assumed.
- Definitions match the recorded census semantics exactly (`E013`,
  `E021`, `A023`): a *simple \(a\)–\(b\) path* is a sequence of
  distinct vertices from \(a\) to \(b\) with consecutive vertices
  adjacent, identified with its edge set; a *cycle* is identified with
  its edge set; \(C\) is an **interference cycle** for \((H,a,b)\) iff
  there exist two distinct simple \(a\)–\(b\) paths \(P,Q\) with
  \(E(C)=E(P)\,\triangle\,E(Q)\); \((H,a,b)\) is **vertex-taut** iff
  every vertex of \(H\) lies on at least one simple \(a\)–\(b\) path
  (`E018/mod4.py` essential-mask semantics). Throughout, \(a\ne b\).
- One classical external theorem is imported (precise statement and
  source in `references/textbook-classics-2026-07-25.md`):
  **Menger's theorem, global vertex form, case \(k=2\)** (equivalently
  Whitney's characterization): *a graph on at least three vertices is
  2-connected if and only if any two distinct vertices are joined by
  two internally disjoint paths.* Only the forward direction is used.
- Standard block terminology, with the three standard facts stated as
  **B1–B3** below and proved inline where cheap (sources in the same
  reference note): blocks are the maximal connected subgraphs having no
  cut vertex of their own (each is 2-connected or a bridge \(K_2\) or
  an isolated vertex — the last is impossible here once \(H\) is
  connected with \(\ge2\) vertices);
  **B1** two distinct blocks share at most one vertex, and a shared
  vertex is a cut vertex of \(H\); a vertex lying in two or more blocks
  is a cut vertex;
  **B2** the block–cut tree \(T\) (nodes = blocks and cut vertices; a
  block \(B\) is adjacent to a cut vertex \(c\) iff \(c\in B\)) is a
  tree, and its leaves are blocks; the components of \(H-x\), for a cut
  vertex \(x\), correspond to the subtrees of \(T-x\);
  **B3** every cycle of \(H\) lies inside a single block, and that
  block is 2-connected.

## Targeted obligations

- `G015`: exclude case (5b). T5 is the recorded gate of the T5→(F)
  interference program: under it the case-(5b) residual object's entire
  power-freeness is through-path arithmetic (`L048`(iii)), the genre
  both kill theorems (`C037`, `L045`) left alive.
- `G013`(a): structure theory for tight 1-atoms.

## Plan and decisive tests

1. Cheapest falsification, run **before** this write-up (pre-registered
   in `A023`/`STATE.md`, executed as `E023`): the `smallworld 13`
   exhaustive in-class rung and the sparse general-graph slices at
   orders 8–9. A single non-decomposable cycle in a vertex-taut pair
   refutes the theorem below and locates the error. Outcome: **zero
   failures** (order 13 in-class: 10,853 taut members, 1,614,300
   cycles; orders 8–11 slices: see `E023`), and the tautness
   biconditional is exact at 13 (all 113 non-taut members fail).
2. Mechanical verification of the *proof itself*: the construction in
   T5 below is deterministic given \((H,a,b,C,pq,R)\); `E023
   constructive` re-executes it for **every cycle and every cycle
   edge** of every vertex-taut pair in scope and asserts every step
   (Lemma A witness, first/last-hit trimming invariants, simplicity of
   both hybrids, \(\triangle=C\), and membership of both hybrids in the
   census path list). A failed assertion falsifies the proof step by
   step. Outcome: **zero failures** over every instance run (orders
   4–7 general exhaustive; the sparse slices at orders 8 and 9; the
   eight profile objects at orders 19–20, Petersen\(-e\), and the
   order-14 exemplar); exact scopes and counts in `E023`.
3. Pivot condition: any failed assertion, or a reviewer-confirmed gap
   → T5 returns to conjecture strength and the program reverts to the
   `A023` reroute/exchange plan.

## Deductions

Notation: \(H\) finite simple, \(a\ne b\in V(H)\). For a path or cycle
\(X\), \(V(X)\) and \(E(X)\) are its vertex and edge sets. All paths
are simple.

### T1 (tautness forces the block chain) — proved

**Claim.** Let \((H,a,b)\) be vertex-taut. Then \(H\) is connected, and
its blocks can be enumerated \(B_1,\dots,B_k\) with distinct cut
vertices \(c_1,\dots,c_{k-1}\) such that

1. \(B_i\cap B_{i+1}=\{c_i\}\) and \(B_i\cap B_j=\emptyset\) for
   \(|i-j|\ge2\);
2. \(c_1,\dots,c_{k-1}\) are exactly the cut vertices of \(H\);
3. \(a\in B_1\setminus\{c_1\}\), \(b\in B_k\setminus\{c_{k-1}\}\)
   (for \(k=1\): \(a,b\in B_1=H\)), and neither \(a\) nor \(b\) is a
   cut vertex;
4. every vertex of \(H\) lies in some \(B_i\);
5. (**chain-splice lemma** — standalone, per `R002` F1: its hypothesis
   is only that the blocks of a connected graph \(H\) form a chain as
   in (1) with \(a,b\) placed as in (3); vertex-tautness is **not**
   assumed, and the proof below uses only (1), (3) and B1) if
   \(W_i\) is any \(c_{i-1}\)–\(c_i\) path inside \(B_i\)
   for each \(i\) (writing \(c_0:=a\), \(c_k:=b\)), then
   \(W_1W_2\cdots W_k\) is a simple \(a\)–\(b\) path of \(H\) with edge
   set \(\bigsqcup_i E(W_i)\).

*Proof.* **Connectivity.** Every vertex lies on an \(a\)–\(b\) path and
every such path contains \(a\); so all vertices are in \(a\)'s
component.

**Every cut vertex separates \(a\) from \(b\), into exactly two
parts.** Let \(x\notin\{a,b\}\) be a cut vertex (the next paragraph,
whose proof is independent of this one, shows neither \(a\) nor \(b\)
is a cut vertex, so this covers every cut vertex; `R002` F3) and
suppose \(a,b\) lie in one component \(K\) of \(H-x\). A simple \(a\)–\(b\) path visits \(x\) at
most once, so it decomposes into at most two \(x\)-free segments, each
inside a single component of \(H-x\); its endpoints put those segments
in \(K\). Hence no \(a\)–\(b\) path meets any other component of
\(H-x\), and such a component exists and is nonempty — contradicting
tautness. So \(a,b\) lie in different components \(A_x\ni a\),
\(B_x\ni b\); a third component would again be untouched by every
\(a\)–\(b\) path (a path visits \(x\) once, lies in
\(A_x\cup\{x\}\cup B_x\)), contradicting tautness. So \(H-x\) has
exactly two components.

**\(a\) and \(b\) are not cut vertices.** If \(a\) were one, a simple
\(a\)–\(b\) path starts at \(a\), immediately enters one component of
\(H-a\) and never returns to \(a\); it must end at \(b\), so it stays
in \(b\)'s component. Any other component of \(H-a\) is then untouched
by every \(a\)–\(b\) path, contradicting tautness. Symmetrically for
\(b\).

**The block–cut tree is a path.** Since \(a\) (resp. \(b\)) is not a
cut vertex, it lies in exactly one block \(B_a\) (resp. \(B_b\)) by B1.
Let \(\Pi\) be the tree path in \(T\) from node \(B_a\) to node
\(B_b\). Suppose \(T\ne\Pi\). Then \(T\) has a node off \(\Pi\), hence
(walking away from \(\Pi\)) a **leaf** off \(\Pi\), which by B2 is a
block \(B'\notin\Pi\). Let \(d\) be the first cut-vertex node on the
tree path from \(B'\) to \(\Pi\) — it exists because \(B'\ne B_a,B_b\)
and \(T\) is connected, and \(B'\) lies in a subtree of \(T-d\) that
contains neither \(B_a\) nor \(B_b\). By B2 the vertex set of that
subtree's blocks, minus \(d\), is a union of components of \(H-d\)
containing neither \(a\) nor \(b\). Such a component is nonempty
(\(B'\) has \(\ge2\) vertices, at most one of them \(d\)), so \(H-d\)
has a component containing neither \(a\) nor \(b\) — contradicting the
two-part separation just proved. Hence \(T=\Pi\): the blocks and cut
vertices alternate along a path
\(B_1,c_1,B_2,\dots,c_{k-1},B_k\) with \(B_1=B_a\), \(B_k=B_b\).

Properties (1)–(4) now read off: consecutive blocks share exactly their
common tree-neighbor cut vertex (B1); non-consecutive blocks sharing a
vertex would create a second tree path (B1 makes the shared vertex a
cut-vertex node adjacent to both, closing a cycle in \(T\)) —
impossible; every cut vertex is a node of \(T=\Pi\), i.e. some \(c_i\);
every vertex of a connected graph on \(\ge2\) vertices lies in a block,
and all blocks are among the \(B_i\); \(a\ne c_1\) because \(a\) is not
a cut vertex, and \(a\in B_1\) by definition (similarly \(b\)); the
\(c_i\) are distinct tree nodes, and \(c_{i-1}\ne c_i\) (they are
distinct nodes of \(\Pi\); for \(i=1\), \(c_0=a\ne c_1\) since \(a\) is
no cut vertex, and for \(i=k\), \(c_k=b\ne c_{k-1}\)).

**(5) Chain splice.** (Uses only (1), (3) and B1 — not tautness.)
Each \(W_i\) lives in \(B_i\); by (1) the pieces are
pairwise disjoint except that consecutive pieces share exactly the
junction vertex \(c_i\) (\(W_i\) ends there, \(W_{i+1}\) starts there).
So the concatenation visits distinct vertices, i.e. is a simple
\(a\)–\(b\) path; blocks are edge-disjoint (B1: two blocks share at
most one vertex, so no edge), so its edge set is the disjoint
union. ∎

*Remark (converse, used only in T6(b)).* If the blocks of a connected
\(H\) form a chain satisfying (1) and (3) — no tautness assumed —
then \((H,a,b)\) is vertex-taut: given \(w\in B_i\), take
\(W_i\) a \(c_{i-1}\)–\(c_i\) path of \(B_i\) through \(w\) (T2 below
if \(B_i\) is 2-connected and \(w\notin\{c_{i-1},c_i\}\); trivial if
\(w\in\{c_{i-1},c_i\}\) or \(B_i=K_2\)) and splice with arbitrary
\(W_j\), \(j\ne i\), by the standalone chain-splice lemma (5), whose
hypotheses hold here by assumption.

### T2 (fan corollary of Menger) — proved (classical)

**Claim.** Let \(G\) be 2-connected and \(s,t,w\) three distinct
vertices. Then \(G\) has an \(s\)–\(t\) path through \(w\).

*Proof.* Add a new apex vertex \(z\) adjacent exactly to \(s\) and
\(t\). \(G+z\) is 2-connected: removing \(z\) leaves \(G\); removing
any \(r\in V(G)\) leaves \(G-r\) (connected, \(G\) being 2-connected)
plus \(z\) attached to at least one of \(s,t\). By Menger (\(k=2\),
imported) there are two internally disjoint \(w\)–\(z\) paths. Each
reaches \(z\) through \(s\) or \(t\); they cannot both use \(s\)
(it would be a shared internal vertex), so one arrives via \(s\), the
other via \(t\). Deleting \(z\) leaves a \(w\)–\(s\) path and a
\(w\)–\(t\) path sharing only \(w\); their concatenation is an
\(s\)–\(t\) path through \(w\). ∎

### T3 (subdivision preserves 2-connectivity) — proved (classical)

**Claim.** If \(G\) is 2-connected and \(G'\) arises by subdividing one
edge \(pq\) with a new vertex \(m\), then \(G'\) is 2-connected.

*Proof.* First, \(G-pq\) is connected: a bridge is impossible in a
2-connected graph on \(\ge3\) vertices (one side of a bridge contains a
vertex besides its endpoint; that endpoint is then a cut vertex — if a
side is the endpoint alone, that endpoint has degree 1 and its neighbor
is a cut vertex). Now check \(G'-r\) is connected for each \(r\):
\(r=m\) gives \(G-pq\); \(r=p\) gives \(G-p\) plus \(m\) attached to
\(q\), and \(r=q\) symmetrically (swap \(p\leftrightarrow q\));
\(r\notin\{m,p,q\}\) gives \(G-r\) with \(m\) attached to \(p\)
and \(q\). ∎

### T4 (Lemma A: cycle-edge essentiality in taut pairs) — proved

**Claim.** Let \((H,a,b)\) be vertex-taut and let \(e=pq\) be an edge
of \(H\) lying on some cycle. Then some simple \(a\)–\(b\) path of
\(H\) contains \(e\).

*Proof.* By B3 the cycle, hence \(e\), lies in a 2-connected block; by
T1 that block is some \(B_i\) of the chain, entered and exited by
through-traffic at \(c_{i-1}\ne c_i\) (\(c_0=a\), \(c_k=b\)). Subdivide
\(e\) inside \(B_i\) with a new vertex \(m\): \(B_i'\) is 2-connected
(T3). The vertices \(c_{i-1},c_i,m\) are distinct (\(m\) is new), so by
T2 there is a \(c_{i-1}\)–\(c_i\) path of \(B_i'\) through \(m\). Since
\(m\)'s only neighbors are \(p\) and \(q\), that path traverses
\(p,m,q\) consecutively; contracting \(m\) back yields a
\(c_{i-1}\)–\(c_i\) path \(W_i\) of \(B_i\) containing the edge \(pq\).
For \(j\ne i\) choose any \(c_{j-1}\)–\(c_j\) path \(W_j\) inside
\(B_j\) (\(B_j\) is connected). By T1(5) the splice
\(W_1\cdots W_k\) is a simple \(a\)–\(b\) path of \(H\) containing
\(e\). ∎

*Remark.* Tautness is the exact hypothesis: an inessential-vertex cycle
edge (e.g. the bridge-hung \(C_8\) in `E021`'s negative anchor) lies on
no through-path, and by `L048`(i) (= `A023` T2) its cycle can then
never decompose. Lemma A is also **necessary** for T5 (any witnessing
pair covers every edge of \(C\)).

### T5 (the theorem: vertex-taut ⟹ interference-complete) — proved

**Theorem.** Let \((H,a,b)\) be vertex-taut and let \(C\) be any cycle
of \(H\). Then there exist two distinct simple \(a\)–\(b\) paths
\(P,Q\) with \(E(P)\,\triangle\,E(Q)=E(C)\).

Moreover the witnessing pair can be taken in **trunk-identical arc
form**: there are distinct \(u,v\in V(C)\) and two (possibly trivial)
paths \(T_a\) from \(a\) to \(u\) and \(T_b\) from \(v\) to \(b\), with
\(V(T_a)\cap V(C)=\{u\}\), \(V(T_b)\cap V(C)=\{v\}\),
\(V(T_a)\cap V(T_b)=\emptyset\), such that
\(P=T_a\,A_1\,T_b\) and \(Q=T_a\,A_2\,T_b\), where \(A_1,A_2\) are the
two \(u\)–\(v\) arcs of \(C\). In particular
\(\ell(P)+\ell(Q)-2s=\ell(C)\) with
\(s=|E(T_a)|+|E(T_b)|=|E(P)\cap E(Q)|\), and for any prescribed edge
\(pq\in E(C)\) the pair can be chosen so that \(pq\in E(P)\cup E(Q)\).

*Proof.* Fix any edge \(pq\in E(C)\). By T4 there is a simple
\(a\)–\(b\) path \(R\) containing \(pq\). Order \(R\) from \(a\) to
\(b\); both \(p\) and \(q\) are vertices of \(R\) lying on \(C\), so
\(R\) meets \(V(C)\). Let \(u\) be the **first** vertex of \(V(C)\)
along \(R\) and \(v\) the **last**. In the ordering of \(R\),
\(\mathrm{pos}(u)\le\min(\mathrm{pos}(p),\mathrm{pos}(q))
<\max(\mathrm{pos}(p),\mathrm{pos}(q))\le\mathrm{pos}(v)\), and
distinct positions of a simple path are distinct vertices, so
\(u\ne v\).

Let \(T_a:=R[a..u]\) (the prefix of \(R\) up to \(u\)) and
\(T_b:=R[v..b]\) (the suffix from \(v\)); either may be a single
vertex (if \(a\in V(C)\) then \(u=a\), and if \(b\in V(C)\) then
\(v=b\)). By the choice of \(u\) as first hit,
\(V(T_a)\cap V(C)=\{u\}\); by the choice of \(v\) as last hit,
\(V(T_b)\cap V(C)=\{v\}\). Since every vertex of \(T_a\) precedes every
vertex of \(T_b\) along the simple path \(R\),
\(V(T_a)\cap V(T_b)=\emptyset\).

Since \(u\ne v\) lie on the cycle \(C\), \(C\) splits into two
\(u\)–\(v\) arcs \(A_1,A_2\): edge-disjoint paths with
\(V(A_1)\cap V(A_2)=\{u,v\}\), \(E(A_1)\sqcup E(A_2)=E(C)\), each with
at least one edge. Define
\[P:=T_a\,A_1\,T_b,\qquad Q:=T_a\,A_2\,T_b.\]
Each is a walk from \(a\) to \(b\); it is a **simple path** because its
three pieces are internally disjoint: \(V(T_a)\cap V(A_j)\subseteq
V(T_a)\cap V(C)=\{u\}\), \(V(A_j)\cap V(T_b)\subseteq\{v\}\), and
\(V(T_a)\cap V(T_b)=\emptyset\), with consecutive pieces meeting
exactly at their junction (\(u\), then \(v\)).

Edge sets: an edge of \(T_a\) has at most one endpoint in \(V(C)\)
(namely \(u\)), while every edge of \(A_j\subseteq C\) has both
endpoints in \(V(C)\); so \(E(T_a)\cap E(A_j)=\emptyset\), similarly
for \(T_b\), and \(E(T_a)\cap E(T_b)=\emptyset\) (disjoint vertex
sets). Hence \(E(P)=E(T_a)\sqcup E(A_1)\sqcup E(T_b)\) and
\(E(Q)=E(T_a)\sqcup E(A_2)\sqcup E(T_b)\), so
\[E(P)\,\triangle\,E(Q)=E(A_1)\,\triangle\,E(A_2)
=E(A_1)\sqcup E(A_2)=E(C).\]
\(P\ne Q\) because \(E(A_1)\ne E(A_2)\) (both nonempty and disjoint).
The length identity is immediate from the disjoint unions, and
\(pq\in E(A_1)\sqcup E(A_2)\subseteq E(P)\cup E(Q)\). ∎

**Why the recorded obstruction dissolves.** The `A023` plan tried to
find one path whose trace on \(C\) is clean and reroute *it*; weaving
was the obstruction, and a minimal-choice exchange the proposed
control. The trimming construction never controls the trace: the
middle of \(R\) — the only place weaving occurs — is discarded, and
both witnesses are rebuilt from the two arcs of \(C\) itself. Nothing
remains for weaving to obstruct. (After the fact, one can read the
witness \(P\) as a "clean-window reroute" of \(Q\); the point is that
neither is the path one started from.)

### T6 (consequences) — proved (each a short corollary of T5)

**(a) 2-connected graphs are interference-complete for every pair.**
If \(H\) is 2-connected and \(a\ne b\) arbitrary, then \((H,a,b)\) is
vertex-taut: for \(w\notin\{a,b\}\), T2 gives an \(a\)–\(b\) path
through \(w\); for \(w\in\{a,b\}\), \(w\) lies on every \(a\)–\(b\)
path and one exists since \(H\) is connected (`R002` F5; this is the
classical remark recorded at `A022`, now consumed). So by T5 every
cycle of \(H\) is the symmetric difference of two
\(a\)–\(b\) paths. This subsumes the pinched-world 100% census
(`C031`/`C032`/`C035`, 23/23 at the blocks) and the frontier
dissection verdict (`C041`, 553/553): every dissected object was
vertex-taut, so decomposability was forced, not fortunate.

**(b) The tautness biconditional on min-degree-2 graphs (the `C042`
phenomenon is a theorem).** Let \(H\) be connected with
\(\delta(H)\ge2\) and \(a\ne b\). Then \((H,a,b)\) is
interference-complete **iff** it is vertex-taut.
(⟸ is T5. ⟹: suppose non-taut. If \(H\) is 2-connected, every pair is
taut by T2 — contradiction; so the block–cut tree \(T\) has \(\ge2\)
nodes, and its leaves are blocks (B2). A leaf block \(B'\) with cut
vertex \(c\) has \(B'\setminus\{c\}\) nonempty and free of cut vertices
(a cut vertex in \(B'\) is a \(T\)-neighbor of \(B'\), and a leaf has
only \(c\)); if \(B'=K_2\), its non-cut vertex would have degree 1 in
\(H\), so \(\delta\ge2\) forces every leaf block to be 2-connected,
hence to carry a cycle through any prescribed vertex (T2 with
\(s,t\) two neighbors of it… more simply: 2-connected graphs have
minimum degree 2, and every vertex of a 2-connected graph lies on a
cycle — take two internally disjoint paths between it and any other
vertex, Menger). If some leaf block \(B'\) contains neither \(a\) nor
\(b\) in \(B'\setminus\{c\}\): a simple \(a\)–\(b\) path visiting
\(w\in B'\setminus\{c\}\) would have to pass \(c\) both before and
after \(w\) — impossible; so those vertices lie on no \(a\)–\(b\) path,
and a cycle of \(B'\) through one of them is non-decomposable by
`L048`(i) — interference-incomplete, as claimed. Otherwise every leaf
block contains \(a\) or \(b\) as a non-cut vertex. If \(T\) had
\(\ge3\) leaves this is impossible, so \(T\) is a path; if \(a,b\) sit
in the same end block \(B_1\setminus\{c_1\}\), every \(a\)–\(b\) path
stays in \(B_1\) (leaving and re-entering would revisit \(c_1\)), the
other end block supplies off-path cycle vertices as before —
incomplete. The remaining configuration is exactly the chain of T1(3),
which is taut by the T1 remark — contradiction with non-tautness.)
This proves the exact biconditional observed in `C042` (`smallworld`
10–12, and now 13: all 113 non-taut members fail) on its class — the
profile class is connected with \(\delta\ge2\) — and shows the
empirical law had no exceptions to find.

**(c) The case-(5b) spectrum identity is unconditional.** The
case-(5b) residual object \((H,a,b)\) is vertex-taut (`L042`), so by
T5 and `L048`(ii)/(iii) (= `A023` T4): every cycle of \(H\) is a
\(t=1\), leak-pinned realization,
\[\mathrm{Spec}(H)=T_1(H,a,b),\qquad
\mathrm{Spec}(B)=T_1(H,a,b)\cup(S+2)\]
for the closure \(B=H+u\). The tight 1-atom's entire power-freeness
**is** through-path arithmetic:
\(T_1\cap\{4,8,16,32,\dots\}=\emptyset\) and
\(S\cap(\mathbb P-2)=\emptyset\). The forcing target (F) (`A023` T6)
is now the whole remaining content of case (5b) below order 36, and
the trunk-identical arc form of T5 pins the collision arithmetic: every
cycle length of \(H\) is realized as \(x+y-2s\) with \(x,y\in S\)
realized by paths sharing a split trunk. Conversely every such
\(t=1\) pair value is a cycle length; so
\(\mathrm{Spec}(H)=\{x+y-2s:\) realized trunk-split pairs\(\}\), and
\(C_8/C_{16}/C_{32}\)-freeness of the object is exactly a system of
**non-realization** statements about its own \(S\)-side path system.

**(d) Scope discipline.** T5 does not touch statement 0.1's truth: it
is a completeness theorem for a *representation* (which cycles are
visible to the through-path calculus), not an existence theorem for
cycles. No power-of-two cycle is produced by it; (F) — that the forced
\(S\)-arithmetic makes a power-length realization unavoidable in the
window — remains fully open and is now the exact residual question of
case (5b) below 36.

### T7 (verification, calibration, and literature position) — computed / noted

- **Instance verification of every proof step** (`E023
  constructive`): for every vertex-taut pair of every connected graph
  of orders 4–7 (12,313 pairs), every cycle and **every cycle edge**
  — 723,926 cycle instances, 3,727,132 (cycle, edge) instances — the
  Lemma-A witness exists and the trimming construction succeeds with
  every invariant asserted (trunk hit-sets, simplicity of both
  hybrids, \(\triangle=C\), membership of both hybrids in the census
  path list). Same on the sparse slices at orders 8–9 (25,907 and
  130,842 taut pairs; exact instance counts in `E023`'s data files)
  and on the eight profile objects (orders 19–20: 411 +
  4,250 = 4,661 cycles — the recorded S022 total reproduced object by
  object — 66,038 (cycle, edge) instances), Petersen\(-e\) (29
  cycles), and the order-14 exemplar `M?AA@?WcKWHOWOL??` (64 cycles)
  — the case-(5b)-adjacent world the theorem was built for. Zero
  failures anywhere.
- **Kill-rung outcome** (pre-registered, run first): `smallworld 13`
  exhaustive in-class (10,966 members — the `A021` count reproduced —
  10,853 taut, 1,614,300 cycles, zero failures; all 113 non-taut
  members fail, as T6(b) now predicts) and the general-graph slices
  (orders 8/9/10/11, cyclomatic-bounded; see `E023` for exact scopes)
  — **T5 survived every rung and then stopped being falsifiable by
  them** (it is proved; the scans double as verification of the
  proof's claim set). Per `R002` F2 the dense completion of order 8
  was cited here before it landed; that citation is repaired to the
  landed result: `tautslice 8 13 28` completed in-session with 8,300
  graphs, 192,188 taut pairs, 36,398,537 cycles, zero failures
  (`E023` `n8_dense` subsection), so T5's conclusion is verified
  exhaustively on every graph of order \(\le8\).
- **Literature position.** The theorem's 2-connected specialization —
  in a 2-connected graph every cycle is the symmetric difference of
  two paths between any two prescribed vertices — is elementary and
  may exist as an exercise; no named source was found in the dossier's
  existing audits. It is recorded here as an internal lemma with an
  internal proof; nothing in the program cites it from outside. If a
  published source surfaces, `G014` gains an item and the claim gains
  a provenance note; its internal status is unaffected.

## Failure analysis

No route died. The recorded obstruction inventory of `A023` T5
("weaving control", "minimal-choice exchange", "cycle-edge
essentiality") is resolved as follows: essentiality became Lemma A
(T4, proved from tautness alone via the block chain); weaving control
turned out to be unnecessary — the trimming construction discards the
only path segment where weaving occurs; no exchange argument exists in
the final proof. The residual risk is concentrated in the two named
audit surfaces: the block-chain argument (T1) and the disjointness
bookkeeping in T5; both were mechanically re-executed per instance by
`E023 constructive` and pass everywhere, and both are named audit
targets of the delegated adversarial review opened by `S023`.

## Salvageable results

1. **T5 proved** — the candidate lemma of `A023` at theorem strength,
   with the stronger trunk-identical arc form and the
   prescribed-edge freedom (offered to the ledger as `L049`).
2. **T4 / Lemma A** — cycle-edge essentiality in vertex-taut pairs
   (subsumed in `L049`'s proof; independently useful for (F)).
3. **T1** — the taut block chain with splice (the structural
   characterization of tautness; reusable wherever tautness is a
   hypothesis, e.g. future (F) work on the 2-connected residual
   object).
4. **T6(a)–(c)** — the three corollaries: 2-connected all-pairs
   completeness; the min-degree-2 tautness biconditional (`C042`
   upgraded from empirical law to theorem on its class); the
   unconditional spectrum identity for case (5b) (offered as the
   `L048` upgrade row).
5. The negative information: no minimal-choice exchange is needed
   anywhere in the interference program; proofs downstream of T5
   should consume the trunk-identical normal form, not re-derive
   trace-cleanliness.

## Exit state

- Status: closed — proof recorded, mechanically verified per instance
  (`E023`), and **audited: `R002` PASS at lemma level** (delegated
  fresh-context logic audit, independence mode `delegated-subagent`;
  0 critical, 0 major, 2 minor — F1 the splice rescoping, F2 the
  then-unlanded dense-run citation — and 6 notes F3–F8; all eight
  repaired in place in this file and the references note, each repair
  marked with its finding ID; the reviewer additionally re-ran every
  recorded `E023` command outside the repository and re-verified
  T5/Lemma A/T6(b) with a fully independent implementation — own
  parser and enumerators — on all labelled graphs through order 6,
  3.2M cycle instances, and all ten named objects, zero failures).
- Promoted records: `L049` (T5 + trunk-identical form + Lemma A),
  `L050` (the min-degree-2 tautness biconditional, T6(b)), the
  `L048`(iii) upgrade note, and `C044` (the E023 kill-rung and
  constructive-verification data) — IDs assigned by the session's
  ledger reconciliation (`S023`).
- Next action: the forcing target **(F)** is now the entire proof side
  of case (5b) below order 36 (`A023` T6, consuming `L049` instead of
  conjecture-T5); its first falsifiable move is recorded in `S023` /
  `STATE.md`.
