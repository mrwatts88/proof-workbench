# A012 — Rung completeness, the lobe decomposition, and taut bottom rungs

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: closed (results promoted)
- Portfolio role: primary (audit and repair of the inherited bottom-rung route)

## Intended mechanism

The inherited next action asked for hand proofs that no power-free pinched
gadget exists with \(s_{\min}\in\{1,2\}\) — the "bottom rungs" of the
spread-doubling lemma `L025` R5(b). The failure-first opening move of this
attempt was to test the premise that these rungs are lemma-sized: to try to
*build* pinched power-free gadgets at \(s_{\min}\le2\) from strong hypothetical
ingredients. That construction succeeds from a counterexample (T1 below), so
each unrestricted rung is equivalent to the full conjecture and the inherited
plan, read literally, was hollow. The repair: the equivalence constructions all
hide their content behind cut vertices, in parts of the gadget that no
terminal-to-terminal path visits. Relativizing the rungs to **taut** gadgets
(every vertex on some \(a\)–\(b\) path) removes exactly that hiding room. The
lobe decomposition (T2) shows the hidden parts are always 1-atom-like objects,
and the taut rungs \(s_{\min}\le2\) then fall by hand (T3), using only
\(C_4\)-freeness. A byproduct of the same analysis (T4): modulo the 1-atom
question, the conjecture reduces to cubic graphs.

## Entry assumptions

Statement 0.1 exactly as in `STATEMENT.md`. All graphs finite and simple.
"Power-free": no cycle of length \(2^k\), \(k\ge2\). "Counterexample": a
counterexample to statement 0.1, i.e. a finite simple graph with
\(\delta\ge3\) and power-free cycle spectrum. Definitions D-A1–D-A5 (gadget,
condition (D), 2-atom, 1-atom, ring) from `A011`. `L025` (R1–R5) is consumed
at its recorded strength. No conditional or abstract-strength imports are
used; all proofs below are self-contained.

## Targeted obligations

- `G013`: the atom / spread-doubling question — refined here.
- `G007`: the global mechanism — the taut relativization is the corrected
  form of its bottom-rung program.

## Definitions

**D-B1 (essential vertex, taut gadget).** Let \((H,a,b)\) be a two-terminal
graph. A vertex \(v\in V(H)\) is *essential* if some simple \(a\)–\(b\) path
contains \(v\) (so \(a,b\) are essential whenever \(H\) is connected). Write
\(\mathrm{Ess}(H,a,b)\) for the set of essential vertices. \((H,a,b)\) is
**(vertex-)taut** if \(\mathrm{Ess}=V(H)\).

**D-B2 (lobe).** A *lobe* of \((H,a,b)\) at a vertex \(c\) is a connected
subgraph \(L\subseteq H\) with \(|V(L)|\ge2\), \(V(L)\cap\mathrm{Ess}=\{c\}\),
such that every edge of \(H\) incident to a vertex of \(V(L)\setminus\{c\}\)
lies in \(L\).

Throughout, \(X=N(a)\setminus\{w\}\), \(Z=N(b)\setminus\{w\}\) in the
\(s_{\min}=2\) analysis, where \(w\) is the common neighbor of the terminals.

## Deductions

### T1 (rung completeness) — proved

**Claim.** (i) A 2-atom with \(S=\{1\}\) exists **iff** a counterexample
exists. (ii) A 2-atom with \(s_{\min}=2\) exists **iff** a counterexample
exists. Consequently each unrestricted "bottom rung" of the spread-doubling
program — nonexistence of pinched power-free (D)-gadgets at a fixed
\(s_{\min}\in\{1,2\}\) — is equivalent to statement 0.1 itself, and clause
(b) of `L025` R5 alone (spread-doubling for all (D)-gadgets) is equivalent to
statement 0.1.

*Proof.* (⇒) in both cases is `L025` R3: any 2-atom yields a counterexample.

(⇐) (i). Let \(G\) be a counterexample; take two disjoint copies \(G_1,G_2\),
choose \(u_i\in V(G_i)\), and set \(H=G_1\sqcup G_2\) plus the edge
\(u_1u_2\), with terminals \(a=u_1\), \(b=u_2\). Condition (D): non-terminal
degrees are \(\ge3\) (inherited), terminal degrees are \(\ge4\). The edge
\(ab\) is a bridge, so every simple \(a\)–\(b\) path uses it; since it already
joins the terminals, the unique simple \(a\)–\(b\) path is the edge itself:
\(S=\{1\}\), pinched. A bridge lies on no cycle, so
\(\mathrm{Spec}(H)=\mathrm{Spec}(G_1)\cup\mathrm{Spec}(G_2)\) is power-free.
So \((H,a,b)\) is a 2-atom with \(S=\{1\}\).

(⇐) (ii). Let \(G,G'\) be disjoint counterexamples (two copies of one). Add
three new vertices \(a,w,b\) and the edges \(aw\), \(wb\), \(ax\) for one
chosen \(x\in V(G)\), and \(wy\) for one chosen \(y\in V(G')\). Degrees:
\(\deg(a)=2\), \(\deg(b)=1\) (sum \(3\)), \(\deg(w)=3\), \(x\) and \(y\) gain
one, everyone else unchanged — (D) holds. Simple \(a\)–\(b\) paths: \(b\) has
the single neighbor \(w\), so every path ends \(w\,b\); a simple \(a\)–\(w\)
path is either the edge \(aw\) or would have to leave \(\{a\}\cup V(G)\)
through a vertex adjacent to it — but the only edges leaving \(V(G)\) go to
\(a\), and the only edges leaving \(V(G')\) go to \(w\), so a path entering
\(G\) via \(x\) can never reach \(w\). Hence \(S=\{2\}\): pinched,
\(s_{\min}=2\). Cycles: \(b\) has degree \(1\), so no cycle contains \(b\); a
cycle through \(a\) would need a \(w\)–\(x\) path avoiding \(a\), but from
\(w\) the non-\(a\) neighbors are \(b\) (degree 1, no through-traffic) and
\(y\in V(G')\), and \(G'\) has no exit except back to \(w\); the same
argument shows no cycle through \(w\). So
\(\mathrm{Spec}(H)=\mathrm{Spec}(G)\cup\mathrm{Spec}(G')\), power-free.
\((H,a,b)\) is a 2-atom with \(s_{\min}=2\).

Final clause: statement 0.1 ⇒ (b) is `L025` R5(b). Conversely ¬(0.1) gives a
counterexample, and (⇐)(i) turns it into a (D)-gadget with
\(s_{\max}=1<2=2s_{\min}\), violating (b). ∎

**Reading.** The \(s_{\min}\)-stratification of spread-doubling has no
lemma-sized unrestricted rungs: every rung is conjecture-complete. Any
meaningful rung program must first outlaw the hiding mechanism the two
constructions share — content invisible to every \(a\)–\(b\) path, propped up
behind cut vertices. That is exactly tautness.

### T2 (lobe decomposition) — proved

**Claim.** Let \((H,a,b)\) be a (D)-gadget (connected, per D-A2). Then either
\((H,a,b)\) is taut, or \(H\) contains a lobe \(L\) at some vertex \(c\), and
any lobe satisfies: every vertex of \(V(L)\setminus\{c\}\) has
\(\deg_L\ge3\), and \(\deg_L(c)\ge1\). Consequently, if \(H\) is power-free
and not taut, then \(H\) contains a **1-atom** (if \(\deg_L(c)\le2\)) **or a
power-free graph of minimum degree \(\ge3\)** (if \(\deg_L(c)\ge3\)) as a
subgraph.

*Proof.* Recall the block-cut tree \(T\) of the connected graph \(H\): its
nodes are the blocks (maximal connected subgraphs without a cut vertex) and
the cut vertices, with a block adjacent to the cut vertices it contains;
\(T\) is a tree, and two distinct blocks share at most one vertex of \(H\).

Fix a shortest path in \(T\) between a block containing \(a\) and a block
containing \(b\); write its blocks in order \(B_1,\dots,B_t\) (the *chain*),
with consecutive blocks \(B_i,B_{i+1}\) sharing the cut vertex \(c_i\), and
set \(c_0=a\in B_1\), \(c_t=b\in B_t\). (If some block contains both \(a\)
and \(b\), the chain is that single block. Minimality of the path gives
\(c_{i-1}\neq c_i\) for each \(i\).)

**Step 1: every vertex of \(U=V(B_1)\cup\dots\cup V(B_t)\) is essential.**
First, inside one block: if \(B\) is 2-connected and \(p\ne q\in V(B)\), then
every \(v\in V(B)\) lies on some simple \(p\)–\(q\) path in \(B\). (For
\(v\in\{p,q\}\) take any \(p\)–\(q\) path. Otherwise the fan lemma in the
2-connected \(B\) gives two paths from \(v\) to \(\{p,q\}\), vertex-disjoint
except at \(v\); if both ended at the same terminal, say \(p\), 2-connectivity
of \(B-p\)… — more directly: by Menger applied to \(v\) and the pair
\(\{p,q\}\) after adding a virtual vertex joined to \(p,q\), there are two
paths from \(v\) to \(p\) and to \(q\) respectively, sharing only \(v\); their
union is a \(p\)–\(q\) path through \(v\).) If \(B\) is a bridge block
\(K_2\), its two vertices are \(p,q\) themselves and the claim is trivial.
Now compose: given \(v\in V(B_i)\), pick inside each \(B_j\) a simple
\(c_{j-1}\)–\(c_j\) path \(P_j\) (through \(v\) when \(j=i\)). Distinct chain
blocks share at most the connecting cut vertex (\(B_j\cap B_{j+1}=\{c_j\}\);
non-consecutive chain blocks are disjoint, else \(T\) would contain a cycle
or the \(T\)-path would not be shortest), so \(P_1\cdots P_t\) is a simple
\(a\)–\(b\) path through \(v\).

**Step 2: every simple \(a\)–\(b\) path stays inside \(U\).** Let \(P\) be a
simple \(a\)–\(b\) path and \(v\in V(P)\). In \(T\), the blocks traversed by
\(P\) form a walk from a block containing \(a\) to a block containing \(b\);
since \(T\) is a tree, every such walk contains the \(T\)-path, and
conversely, if \(P\) visited a block \(B\notin\{B_1,\dots,B_t\}\), then \(P\)
would have to enter and leave the branch of \(T\) hanging off the chain that
contains \(B\) through the single cut vertex attaching that branch to the
chain — visiting it twice, contradicting simplicity. (In detail: let \(c\) be
the attachment cut vertex of that branch; removing \(c\) from \(H\)
disconnects all non-\(c\) vertices of the branch's blocks from \(a\) and from
\(b\), because every \(T\)-walk from the branch to \(B_1\) or \(B_t\) passes
the node \(c\). A simple path visits \(c\) at most once, so it cannot enter
the branch and return.) Hence \(\mathrm{Ess}=U\) exactly.

**Step 3: components outside the chain are lobes.** Suppose \(H\) is not
taut, i.e. \(W=V(H)\setminus U\neq\emptyset\). Let \(K\) be a connected
component of \(H[W]\), and let \(L'\) be the union of all blocks of \(H\)
that contain a vertex of \(K\). Every such block lies in one branch of \(T\)
hanging off the chain (blocks not on the chain, since \(K\cap U=\emptyset\)),
and all of them lie in the *same* branch (a path in \(K\) between vertices of
two different branches would have to pass through the chain, through the
attachment vertices — but \(K\) avoids \(U\)). Let \(c\) be the attachment
cut vertex of that branch (\(c\in U\); possibly \(c\in\{a,b\}\)). By Step 2's
detail, every vertex of the branch other than \(c\) is separated from \(a\)
and \(b\) by \(c\), so the branch's blocks contain no essential vertex except
\(c\). Take \(L\) = the union of the blocks of the branch. Then \(V(L)\cap
\mathrm{Ess}=\{c\}\), \(|V(L)|\ge2\), \(L\) is connected (a branch of \(T\)
is a subtree; consecutive blocks share cut vertices), and every edge of \(H\)
at a vertex \(v\in V(L)\setminus\{c\}\) lies in a block containing \(v\),
hence in the branch, hence in \(L\): \(L\) is a lobe at \(c\).

**Step 4: lobe degrees.** Let \(L\) be any lobe at \(c\). For
\(v\in V(L)\setminus\{c\}\): \(v\notin\mathrm{Ess}\supseteq\{a,b\}\), so
\(v\) is non-terminal and \(\deg_H(v)\ge3\) by (D); by D-B2 all edges of
\(H\) at \(v\) lie in \(L\), so \(\deg_L(v)=\deg_H(v)\ge3\). And
\(\deg_L(c)\ge1\) since \(L\) is connected with \(|V(L)|\ge2\).

Final clause: \(L\) is connected, and power-free as a subgraph of the
power-free \(H\). If \(\deg_L(c)\ge3\), then \(\delta(L)\ge3\). If
\(\deg_L(c)\in\{1,2\}\), then \(L\) is connected and power-free with exactly
one vertex of degree \(<3\), of degree 1 or 2 — a 1-atom (D-A4). ∎

### T3 (taut bottom rungs) — proved

**Claim.** (i) No taut (D)-gadget has \(S=\{1\}\). (ii) No taut (D)-gadget
with \(s_{\min}=2\), \(S\subseteq\{2,3\}\), and no 4-cycle exists.
(Power-freeness beyond \(C_4\)-freeness is not needed. The case
\(S=\{3\}\) has \(s_{\min}=3\) and belongs to the next rung; it is **not**
covered here.)

*Proof.* (i) \(S=\{1\}\) means the unique simple \(a\)–\(b\) path is the edge
\(ab\), so \(\mathrm{Ess}=\{a,b\}\); tautness forces \(V(H)=\{a,b\}\), and
then \(\deg(a)+\deg(b)=2<3\) violates (D).

(ii) Suppose \((H,a,b)\) is such a gadget. Since \(2=s_{\min}\), \(ab\notin
E\) and the terminals have a common neighbor; since \(H\) has no \(C_4\), the
common neighbor \(w\) is unique (two common neighbors \(w,w'\) give the
4-cycle \(a\,w\,b\,w'\)). Set \(X=N(a)\setminus\{w\}\),
\(Z=N(b)\setminus\{w\}\); then \(X\cap Z=\emptyset\) (a member of both would
be a second common neighbor), \(a,b,w\notin X\cup Z\), and \(X\cap N(b)=
\emptyset=Z\cap N(a)\).

*Vertex inventory.* Simple \(a\)–\(b\) paths have length 2 or 3. The unique
length-2 path is \(a\,w\,b\). A length-3 path is \(a\,p\,q\,b\) with \(p\in
N(a)\), \(q\in N(b)\), \(pq\in E\). By tautness every vertex lies on such a
path, so \(V(H)=\{a,b,w\}\cup X\cup Z\).

*The tautness workhorse.* Every \(x\in X\) lies on some simple \(a\)–\(b\)
path; the length-2 path does not contain \(x\), so \(x\) lies on a length-3
path \(a\,p\,q\,b\). Since \(q\in N(b)\) and \(x\notin N(b)\), necessarily
\(x=p\), so \(x\) has a neighbor \(q\in N(b)=\{w\}\cup Z\): **every \(x\in
X\) is adjacent to \(w\) or to a vertex of \(Z\)** (symmetrically for
\(Z\)).

*Local constraints.*
1. Each \(x\in X\) has at most one neighbor in \(Z\): two neighbors
   \(z\ne z'\in Z\) give the 4-cycle \(x\,z\,b\,z'\). (Symmetrically each
   \(z\in Z\) has at most one neighbor in \(X\).)
2. At most one vertex of \(X\) is adjacent to \(w\): \(x\ne x'\) both
   adjacent to \(w\) give the 4-cycle \(a\,x\,w\,x'\). (Symmetrically at most
   one \(z\in Z\) is adjacent to \(w\).)
3. No edge inside \(X\): suppose \(xx'\in E\) with \(x,x'\in X\). If \(x\)
   had a neighbor \(z\in Z\), then \(a\,x'\,x\,z\,b\) would be a simple
   \(a\)–\(b\) path of length 4 (its five vertices are pairwise distinct
   since \(a,b\notin X\cup Z\), \(X\cap Z=\emptyset\)), contradicting
   \(S\subseteq\{2,3\}\). So \(x\) — and symmetrically \(x'\) — has no
   neighbor in \(Z\), and the workhorse forces both adjacent to \(w\),
   contradicting 2. (Symmetrically no edge inside \(Z\).)
4. Possible neighbors of \(x\in X\) are therefore: \(a\), \(w\) (for at most
   one \(x\)), and at most one \(z\in Z\) — the inventory excludes anything
   else, and \(xb\notin E\).

*Forcing.* By (D), \(\deg(x)\ge3\) for every \(x\in X\). By constraint 4, a
vertex of \(X\) not adjacent to \(w\) has degree at most \(2\) (\(a\) plus
one \(z\)). So every \(x\in X\) is adjacent to \(w\), whence \(|X|\le1\) by
constraint 2; symmetrically \(|Z|\le1\).

If \(X=\{x\}\): \(\deg(x)\ge3\) forces \(x\sim a,w\) and \(x\sim z\) for a
(unique) \(z\in Z\), so \(Z=\{z\}\); then \(\deg(z)\ge3\) with options
\(b,w,x\) forces \(z\sim w\). Now \(a\,x\,z\,w\,a\) is a 4-cycle (edges
\(ax\), \(xz\), \(zw\), \(wa\); vertices distinct) — contradiction. So
\(X=\emptyset\). Then any \(z\in Z\) has options only \(b\) and \(w\), degree
\(\le2<3\) — so \(Z=\emptyset\). But then \(\deg(a)=\deg(b)=1\) (only \(w\)),
violating \(\deg(a)+\deg(b)\ge3\). ∎

**Corollary T3.1.** Every 2-atom with \(s_{\min}\le2\) contains a 1-atom or a
power-free graph of minimum degree \(\ge3\).

*Proof.* \(s_{\min}=1\) and pinched means \(S=\{1\}\): by T3(i) the gadget is
not taut; \(s_{\min}=2\) and pinched means \(S\subseteq\{2,3\}\), and a
2-atom is power-free, in particular \(C_4\)-free: by T3(ii) not taut. Either
way T2 supplies the subgraph. ∎

**Corollary T3.2 (finite bound).** Every 2-atom with \(s_{\min}\le2\) has
order \(\ge17\), and \(\ge18\) when \(s_{\min}=2\).

*Proof.* By T3.1 and `C027` (no power-free graph with \(\le2\) sub-cubic
vertices through order 15, so 1-atoms have order \(\ge16\)) and `L022`
(min-degree-3 power-free graphs have order \(\ge19\)): the lobe (with its
attachment vertex) has \(\ge16\) vertices. For \(s_{\min}=1\) the second
bridge side contributes at least one further vertex (the other terminal). For
\(s_{\min}=2\): the lobe meets \(\mathrm{Ess}\) only in its attachment \(c\),
while \(a,b,w\) are three distinct essential vertices, so at least two of
them lie outside the lobe. ∎

### T4 (cubic reduction modulo 1-atoms) — proved

**Claim.** If no 1-atom exists, then every counterexample of minimum order
(then minimum size) is cubic. Hence statement 0.1 is true **iff** no cubic
counterexample and no 1-atom exist.

*Proof.* Let \(G\) be a counterexample minimizing \(|V|\), then \(|E|\).
\(G\) is connected (a component is a counterexample; a proper one would beat
minimality). Suppose \(G\) is not cubic; pick \(x\) with \(\deg(x)\ge4\).

If some neighbor \(y\) of \(x\) has \(\deg(y)=3\): in \(G-xy\), the vertex
\(y\) has degree 2, \(x\) has degree \(\ge3\), all others are unchanged, and
the spectrum only shrinks, so \(G-xy\) is power-free. If \(G-xy\) is
connected it is a 1-atom (exactly one sub-cubic vertex, of degree 2) —
contradiction. If not, \(xy\) was a bridge; the component of \(y\) in
\(G-xy\) is connected, power-free, with \(y\) of degree 2 and all other
degrees \(\ge3\): a 1-atom — contradiction.

Otherwise every neighbor of \(x\) has degree \(\ge4\): for any edge \(xy\),
\(G-xy\) has minimum degree \(\ge3\) and is power-free — if connected it is a
counterexample with fewer edges, contradicting size-minimality; if
disconnected, each component is a counterexample of smaller order,
contradicting order-minimality. ∎

**Remark T4.1.** In a 1-atom of minimum order the sub-cubic vertex \(u\) has
degree 2: if \(\deg(u)=1\), then \(B-u\) is connected (u is a leaf),
power-free, and has at most one sub-cubic vertex (\(u\)'s neighbor, which had
degree \(\ge3\) and drops to \(\ge2\)); so \(B-u\) is a smaller 1-atom or a
min-degree-3 power-free graph, the latter yielding (by deleting one further
edge as in T4, or directly as a counterexample) a contradiction with
statement scope — in either case \(B\) was not minimal. So the 1-atom
question concentrates on degree-2 exceptional vertices, matching D-A4's
doubling assembly (`L025` R4, degree-2 case).

**Reading.** The 1-atom question now sits at the center of three channels:
it is the sole content of the unrestricted bottom rungs (T1 via T2/T3.1), the
sole obstruction to a clean cubic reduction of statement 0.1 (T4), and the
lobe half of every non-taut 2-atom (T2). The known searches make it a
strictly-order-\(\ge16\) phenomenon (`C027`).

## Plan and decisive tests

1. **Premise test (executed first, fired):** try to build unrestricted
   pinched gadgets at \(s_{\min}\le2\) from a hypothetical counterexample.
   Success = T1 = the inherited rung program is conjecture-complete as
   stated. This fired at formulation time, before any computation.
2. **Repair test (executed, passed):** relativize to taut gadgets and attack
   \(s_{\min}\le2\) by hand. T3 closes both rungs using \(C_4\)-freeness
   only.
3. **Computational check (E011):** T3(ii) predicts that every \(C_4\)-free
   (D)-gadget with \(S\subseteq\{2,3\}\) in the E010 profile class is
   non-taut. Verified at orders 12–13 against a re-derived profile stream
   (anchored to the E010 counts), plus construction anchors for T1 scaffolds
   and a tautness anchor on \(K_{3,3}-e\). See `E011`.
4. Pivot conditions: none fired against the repaired route; the next rung
   (taut \(s_{\min}=3\), where \(K_{3,3}-e\) shows the shape is realizable
   with 4-cycles) is genuinely open and becomes the proposed next action.

## Failure analysis

The *inherited* route failed at its premise: the unrestricted bottom rungs
are not lemmas but restatements of the conjecture (T1). The failure mechanism
— counterexample content hidden behind cut vertices, invisible to every
\(a\)–\(b\) path — is itself the key structural fact; naming it produced the
taut relativization under which the rungs become true lemmas (T3). This is
recorded as a premise correction, not a dead end.

## Salvageable results

All of T1–T4 and the two corollaries stand and are promoted (`L026`–`L029`).
The rung program survives only in taut-relativized form; its meaningful
ladder starts at taut \(s_{\min}=3\). The 1-atom question is elevated to the
central open object of the disproof interface.

## Exit state

- Status: closed (results promoted)
- Promoted records: `L026` (T1), `L027` (T2), `L028` (T3 + corollaries),
  `L029` (T4 + remark); experiment `E011`; `G013` refined.
- Next action: attack the taut \(s_{\min}=3\) rung — no taut power-free
  \(C_4\)-free (D)-gadget with \(S\subseteq\{3,4,5\}\) — or exhibit one
  (disproof by `L025` R3). Alternatives: minimal 1-atom structure theory;
  order-16 atom census (deferred).
