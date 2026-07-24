# A014 — The pendant reduction: strict-pinched taut gadgets are lifts of ratio-2 cores; the four cores and the C8 interference mechanism

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: active
- Portfolio role: reframing that became the primary route

## Intended mechanism

The six concrete taut pinched gadgets (the five `C028` witnesses plus the
band-5 witness found by `E013`) all share one anatomy: a single cut vertex,
terminal degrees \(\{1,2\}\), and a degree-1 terminal whose deletion leaves a
two-terminal graph at through-ratio exactly \(2\). Formalizing that anatomy
(pendant reduction and lift, then series-chain decomposition at cut vertices)
collapses the entire taut half of the 2-atom question onto one object: a
**power-free vertex-taut 2-connected core with \(s_{\max}\le2\,s_{\min}\)**.
The concrete enemy catalogue for that object is small (five blocks through
order 14, all at exact equality \(s_{\max}=2\,s_{\min}\)), and in every one of
them the \(C_8\) obstruction is produced by one mechanism: two through-paths
whose symmetric difference is the 8-cycle.

## Entry assumptions

Definitions D-A1–D-A5 of `A011` (two-terminal graph, condition (D), 2-atom,
1-atom, ring); vertex-tautness from `A012`; statement version 0.1 only enters
through the power-free condition of D-A3. Everything below is unconditional
graph theory about finite simple graphs.

## Definitions

**D-P1 (core).** A **core** is a two-terminal graph \((T,x,y)\) (D-A1: finite,
simple, connected, \(x\ne y\)) in which every non-terminal vertex has degree
\(\ge3\) and *both* terminals have degree \(\ge2\). Every core is a
(D)-gadget. The **excess** of a two-terminal graph with nonempty through-set
is \(e=s_{\max}-2\,s_{\min}\). A core is **strict** if \(e\le-1\) (i.e.
pinched, ratio \(<2\)), **at equality** if \(e=0\).

**D-P2 (pendant lift).** For a two-terminal graph \((T,x,y)\) and the terminal
\(x\), the pendant lift at \(x\) is \((T+a,\,a,\,y)\), where \(a\) is one new
vertex adjacent exactly to \(x\).

**D-P3 (chain).** A **chain decomposition** of a two-terminal graph
\((T,x,y)\) is the block–cut decomposition read from \(x\) to \(y\): blocks
\(B_1,\dots,B_m\) with \(B_i\cap B_{i+1}\) a single cut vertex, \(x\in B_1\)
only, \(y\in B_m\) only, each \(B_i\) carrying the two attachment vertices
\(c_{i-1},c_i\) as its terminals (\(c_0=x\), \(c_m=y\)). A block is either an
edge (**bridge**) or 2-connected.

## Deductions

**T1 (pendant reduction) — proved.** Let \((H,a,b)\) be a vertex-taut
(D)-gadget with \(\deg_H(a)=1\), and let \(x\) be the unique neighbor of
\(a\). Then:

1. \(x\ne b\). If \(x=b\), the only simple \(a\)–\(b\) path is the edge
   \(ab\); by (D), \(\deg(b)\ge2\), so \(b\) has a neighbor \(z\ne a\), and
   \(z\) lies on no simple \(a\)–\(b\) path, contradicting tautness.
2. Every simple \(a\)–\(b\) path starts with the edge \(ax\) and never
   returns to \(a\); stripping/prepending that edge is a bijection between
   simple \(a\)–\(b\) paths of \(H\) and simple \(x\)–\(b\) paths of
   \(H-a\). Hence \(S(H,a,b)=1+S(H-a,x,b)\).
3. \((H-a,\,x,\,b)\) is a **core**: \(x\) is a non-terminal of \(H\), so
   \(\deg_{H-a}(x)=\deg_H(x)-1\ge2\); \(\deg(b)\ge2\) by (D) with
   \(\deg(a)=1\); all other degrees are unchanged \(\ge3\). It is connected
   and vertex-taut: every vertex of \(H-a\) lies on a simple \(a\)–\(b\)
   path of \(H\) (tautness of \(H\)), hence on its \(x\)–\(b\) tail.
4. \(a\) lies on no cycle, so \(\mathrm{Spec}(H)=\mathrm{Spec}(H-a)\):
   \(C_4\)-freeness and power-freeness transfer both ways.
5. Ratio arithmetic: \(s_{\max}(H)\le2\,s_{\min}(H)-1\) **iff**
   \(s_{\max}(H-a)\le2\,s_{\min}(H-a)\). (Shift by 1:
   \(s'+1\le2(s'_{\min}+1)-1\Leftrightarrow s'\le2s'_{\min}\).) So strict
   pinch upstairs is *closed* ratio (\(e\le0\)) downstairs, with strict
   downstairs corresponding to \(s_{\max}(H)\le2\,s_{\min}(H)-2\).

**T2 (pendant lift) — proved.** Conversely, if \((T,x,y)\) is a vertex-taut
core, its pendant lift at \(x\) is a vertex-taut (D)-gadget with a degree-1
terminal, \(S=1+S(T)\), \(\mathrm{Spec}\) unchanged, and it is strictly
pinched iff \(e(T)\le0\). ((D): the attachment \(x\) becomes internal with
degree \(\deg_T(x)+1\ge3\); terminal degrees are \(1\) and
\(\deg_T(y)\ge2\), sum \(\ge3\). Tautness and the path bijection as in T1.)
*Remark (lift matching).* The lifts at \(x\) and at \(y\) are isomorphic as
two-terminal gadgets iff \(T\) has a terminal-swapping automorphism: an
isomorphism must send pendant to pendant (the unique degree-1 terminal),
hence attachment to attachment, and terminal to terminal.

**T3 (chain decomposition of taut two-terminal graphs) — proved.** Let
\((T,x,y)\) be vertex-taut with every non-terminal degree \(\ge3\) and
terminal degrees \(\ge1\). Then:

1. Every cut vertex of \(T\) separates \(x\) from \(y\), and the block–cut
   tree is a path from the block containing \(x\) to the block containing
   \(y\). (If some component \(K\) of \(T-c\) contains neither \(x\) nor
   \(y\), a simple \(x\)–\(y\) path meeting \(K\) would have to pass \(c\)
   twice; so \(K\)'s vertices lie on no such path, contradicting tautness.
   The same argument bars leaf blocks not containing a terminal.)
2. With blocks \(B_1,\dots,B_m\) as in D-P3, every simple \(x\)–\(y\) path
   is the concatenation of independent simple \(c_{i-1}\)–\(c_i\) paths, one
   in each block; hence the Minkowski sum
   \(S(T)=S(B_1)+\dots+S(B_m)\), and each \((B_i,c_{i-1},c_i)\) is
   vertex-taut.
3. Degrees inside blocks: a non-attachment, non-terminal vertex of \(B_i\)
   keeps degree \(\ge3\); an attachment vertex \(c_i\) has degree \(\ge1\)
   in each adjacent block. If \((T,x,y)\) is a **core**, then no bridge is
   an end block (\(B_1\) a bridge would give \(\deg(x)=1\)), and no two
   bridges are adjacent (their shared attachment would be a non-terminal of
   degree 2). Hence \(\#\text{bridges}\le\#\{2\text{-connected blocks}\}-1\),
   and every 2-connected block, with its attachments as terminals, is
   itself a vertex-taut **core** (attachment degrees \(\ge2\) inside a
   2-connected block).
4. Every cycle of \(T\) lies in one block, so
   \(\mathrm{Spec}(T)=\bigcup_i\mathrm{Spec}(B_i)\): \(T\) is power-free iff
   every block is.

**T4 (block extraction; the taut interface theorem) — proved.** Taut 2-atoms
exist **iff** power-free vertex-taut 2-connected cores with
\(s_{\max}\le2\,s_{\min}\) (excess \(e\le0\)) exist.

*Proof.* (⇒) Let \((H,a,b)\) be a taut 2-atom. If some terminal has
degree 1 (by (D) at most one does), apply T1: the core \((T,x,b)\) is
vertex-taut, power-free, with \(e(T)\le0\). If both terminal degrees are
\(\ge2\), take \(T=H\) itself: a power-free taut core with \(e\le-1\).
Apply T3 to \(T\): blocks \(B_1,\dots,B_m\), \(b^*\) of them bridges and
\(k=m-b^*\) of them 2-connected, each 2-connected block a power-free
vertex-taut core. A bridge has \(S=\{1\}\), excess \(-1\); the Minkowski sum
gives \(e(T)=\sum_i e(B_i)\ge\sum_{2\text{-conn}}e(B_i)-b^*\). Since
\(e(T)\le0\) and \(b^*\le k-1\) (T3.3; \(k\ge1\), and \(k=0\) is impossible
since a bare bridge is not a core), if every 2-connected block had
\(e\ge1\) we would get \(e(T)\ge k-b^*\ge1\), a contradiction. So some
2-connected block \(B\) has \(e(B)\le0\); it is power-free, vertex-taut,
2-connected, with terminal degrees \(\ge2\).

(⇐) Let \((B,x,y)\) be power-free, vertex-taut, 2-connected, terminal
degrees \(\ge2\), \(e(B)\le0\). If \(e(B)\le-1\), \(B\) is itself a taut
2-atom (it satisfies (D) with both terminal degrees \(\ge2\ge\) the required
sums, and is strictly pinched). If \(e(B)=0\), its pendant lift at \(x\)
(T2) is a vertex-taut strictly pinched (D)-gadget with unchanged power-free
spectrum: a taut 2-atom. ∎

**T5 (strict cores exist: the bridge composite) — proved by construction,
machine-verified.** Take two disjoint copies of Petersen\(-e\) (see C-facts
below; terminals its two degree-2 vertices, \(S=\{4,5,7,8\}\), spectrum
\(\{5,6,8,9\}\)) and join terminal \(y_1\) of the first to terminal \(x_2\)
of the second by a bridge. The result \((T,x_1,y_2)\) is a vertex-taut
**core** of order 20 with \(S=\{4,5,7,8\}+1+\{4,5,7,8\}=\{9,\dots,17\}\),
\(s_{\max}=17\le2\cdot9-1\): **strictly pinched**, excess \(-1\), and
spectrum \(\{5,6,8,9\}\) (blocked from power-freeness only by its \(C_8\)s).
Verified by the `E013` machinery (anchor A9: taut, band 9, exact \(S\),
2 cut vertices = the bridge ends). Consequences:

- "Taut core \(\Rightarrow s_{\max}\ge2\,s_{\min}\)" is **false**: naive
  core-level spread-doubling dies at once. T4's restriction to 2-connected
  blocks is not cosmetic; blocks are the correct level.
- Strict pinch is buildable from equality blocks and bridges; only the
  *power* obstruction (each block drags its \(C_8\) along) stops the
  composite from disproving 0.1.

## Corollaries

**C1 (interface restatement).** With `L027` (non-taut gadgets contain lobes:
1-atoms or min-degree-3 power-free graphs) and T4, obligation `G013`
becomes exactly: **(a)** the 1-atom question, and **(b′)** does a
power-free vertex-taut 2-connected core with \(s_{\max}\le2\,s_{\min}\)
exist? Both directions of (b′) are constructive (T2/T4).

**C2 (rung transfer).** Blocks are (D)-gadgets, so `L028`/`L030` apply
verbatim: a vertex-taut \(C_4\)-free core has no \(S=\{1\}\), no
\(s_{\min}=2\) with \(S\subseteq\{2,3\}\), and at \(d(x,y)=3\) has a path of
length \(\ge6\). In excess language, \(C_4\)-freeness alone forces
\(e\ge0\) for 2-connected blocks with \(s_{\min}\le3\) (the \(s_{\min}\le2\)
cases even force more). The open **block rungs** are \(s_{\min}=4,5,\dots\):
strict blocks (\(e\le-1\)) are excluded through order 14 by the `E013`
closed catalogue; equality blocks exist from \(s_{\min}=4\) on.

**C3 (the block catalogue through order 14) — computational, `E013`.**
Exactly five 2-connected vertex-taut cores with \(e\le0\) exist among all
admissible terminal pairs of all connected \(C_4\)-free graphs with at most
two sub-cubic vertices at orders \(\le14\) — all five at **exact equality**
\(s_{\max}=2\,s_{\min}\):

| block | order | band \(s_{\min}\) | \(S\) | spectrum | \(C_8\)s |
|---|---|---|---|---|---|
| P10 = Petersen\(-e\) | 10 | 4 | \(\{4,5,7,8\}\) | \(\{5,6,8,9\}\) | 7 |
| A11 | 11 | 5 | \(\{5,\dots,10\}\) | \(\{3,5,\dots,11\}\) | 3 |
| B11 | 11 | 5 | \(\{5,\dots,10\}\) | \(\{3,5,\dots,11\}\) | 3 |
| C12 | 12 | 5 | \(\{5,\dots,10\}\) | \(\{3,5,\dots,11\}\) | 5 |
| D14 | 14 | 6 | \(\{6,\dots,12\}\) | \(\{3,5,\dots,13\}\) | 5 |

The strict taut-pinched (D)-catalogue at orders \(\le14\) is exactly the six
pendant lifts of P10, A11, B11, C12 (T1/T2 bijection, machine-verified: the
asymmetric A11 and C12 have two non-isomorphic lifts each, the
swap-symmetric P10 and B11 one each; D14 is swap-symmetric and predicts
exactly one strict band-7 witness at order 15). Petersen\(-e\) is identified
by nauty `labelg` canonical comparison; its \(S=\{4,5,7,8\}\) is the
cycle-through-edge spectrum of Petersen shifted by \(-1\), and its 7
\(C_8\)s are Petersen's 15 minus the 8 through the deleted edge
(edge-transitivity).

**C4 (mechanism observations, all machine-checked).**

- In every block and every witness, **every \(C_8\) is the symmetric
  difference of two through-paths** (5/5, 3/3, 3/3, 5/5, 7/7 realized).
- Every block has at least one pair of internally disjoint shortest
  through-paths. At band 4 that alone forces \(C_8\)
  (\(4+4-2\cdot0=8\): realized twice in P10); at bands 5–6 the disjoint
  shortest pairs give \(C_{10}/C_{12}\), and the \(C_8\)s come from
  overlapping pairs (\(5+5-2\cdot1\), \(6+6-2\cdot2\), \(5+7-2\cdot2\),
  \(6+8-2\cdot3\), ...).
- Every edge of every block/witness lies on some through-path (no
  inessential edges), so the path-interference mechanism has no blind
  spots in the known catalogue.

## Plan and decisive tests

The two block rungs at \(s_{\min}=4\) are now the sharpest targets, each
with a clean kill:

1. **Strict band-4 block rung** (the \(e\ge0\) side): prove that no
   vertex-taut \(C_4\)-free 2-connected core has
   \(S\subseteq\{4,5,6,7\}\). Empty through order 14 (`E013` closed
   catalogue, strict subset); killed by any strict block found at order
   \(\ge15\).
2. **Band-4 equality power rung** (the power side): prove that every
   vertex-taut \(C_4\)-free 2-connected core with \(S\subseteq\{4,\dots,8\}\)
   contains a \(C_8\) (at orders \(\ge16\), a \(C_8\) or \(C_{16}\)).
   Guided by P10; the candidate proof shape is the disjoint/intersecting
   dichotomy on the 4-path system: two internally disjoint 4-paths give
   \(C_8\) outright; a pairwise internally intersecting 4-path system under
   \(C_4\)-freeness is rigid (two 4-paths can share only specific
   patterns), and tautness plus degree \(\ge3\) must route the whole graph
   through it. Killed by a \(C_8\)-free equality block at order \(\le15\)
   (which `C027` already excludes) or at 16+ (which would be disproof
   material, subject to the \(C_{16}\) check).
3. Search leg: extend the closed catalogue to order 15 under PyPy. Any new
   block extends the lab; a strict block kills rung 1; a \(C_8\)-free block
   kills rung 2.

## Failure analysis

Not abandoned. One candidate formulation was refuted in-session and the
refutation is retained as T5: core-level spread-doubling (without
2-connectedness) is false, by the bridge composite. This is why T4 extracts
a 2-connected block rather than working with cores directly.

## Salvageable results

T1–T4 are unconditional lemmas (candidate ledger rows `L031`, `L032`); T5 is
a permanent separation example; C3–C4 are the concrete enemy catalogue and
mechanism data (`C030`, `C031`). The bridge composite also shows how close
the boundary sits: its only power violation is the \(C_8\) each Petersen
\(-e\) block carries.

## Exit state

- Status: active
- Promoted records: `L031` (T1+T2), `L032` (T3+T4, with T5 as the
  sharpness example), `C030` (strict catalogue), `C031` (closed
  catalogue, blocks, dissection) — see `CLAIMS.md`.
- Next action: the band-4 block rungs (strict impossibility, equality
  \(C_8\)-forcing), with the order-15 closed catalogue as the search leg.
