# A015 — The band-4 pencil dichotomy: disjoint 4-paths or a common vertex; consequences for the block rungs

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: active
- Portfolio role: primary route (the band-4 block rungs of `A014`)

## Intended mechanism

`A014` left two band-4 block rungs: (i) no vertex-taut \(C_4\)-free
2-connected core has \(S\subseteq\{4,5,6,7\}\) (strict), and (ii) every such
core with \(S\subseteq\{4,\dots,8\}\) contains a \(C_8\) (equality power).
The candidate mechanism was the disjoint/intersecting dichotomy on the
4-path system: two internally disjoint shortest paths close into a \(C_8\)
outright, and pairwise-intersecting systems were expected to be "rigid"
under \(C_4\)-freeness. This attempt settles the rigidity half completely
and in a stronger form than hoped: **pairwise-intersecting 4-path systems
are pencils** (all paths share one internal vertex) — and the dichotomy
needs no \(C_4\)-freeness at all. \(C_4\)-freeness then pins the pencil to
a terminal's neighborhood and rigidifies the resulting fan. Rung (ii) is
thereby reformulated as a **pencil endgame**: prove that no vertex-taut
2-connected \(C_4\)-free core at band 4 with \(s_{\max}\le8\) can have a
pencilled 4-path system. The reformulated conclusion is stronger than (ii):
a \(C_8\) **through both terminals**, with no \(C_{16}\) caveat at any
order.

## Entry assumptions

Definitions D-A1–D-A5 of `A011`, vertex-tautness (`A012`), core/excess
(`A014` D-P1). Everything below is unconditional finite graph theory;
statement 0.1 never enters. Throughout, \(G\) is a finite simple graph with
two distinguished vertices \(x\ne y\) at distance \(d(x,y)=4\), and a
**4-path** is a simple \(x\)–\(y\) path of length 4. A 4-path is a shortest
path, so its \(i\)-th internal vertex \(p_i\) has \(d(x,p_i)=i\) and
\(d(p_i,y)=4-i\); internal vertices of two 4-paths can therefore coincide
only within the same "layer" \(i\in\{1,2,3\}\).

## Targeted obligations

- `G013` (b′), the block question, band 4: both `A014` rungs.

## Definitions

**D-Q1 (middle set).** \(M=\{v: d(x,v)=2 \text{ and } d(v,y)=2\}\). For
\(m\in M\): \(A(m)=N(m)\cap N(x)\), \(B(m)=N(m)\cap N(y)\).

**D-Q2 (pencil / fan).** A nonempty family of 4-paths is a **pencil at
\(c\)** if every member contains \(c\) as an internal vertex. When the
pencil vertex is adjacent to a terminal and there are \(t\ge2\) paths, the
configuration is a **fan**; its **strands** are the (middle, exit) pairs
of its members.

## Deductions

**T0 (middles are exactly \(M\)) — proved, no hypotheses.** The middle
vertices of 4-paths are exactly the elements of \(M\), and for \(m\in M\)
the 4-paths with middle \(m\) are exactly
\(\{x\,u\,m\,w\,y : u\in A(m),\, w\in B(m)\}\), with
\(A(m)\ne\emptyset\ne B(m)\).

*Proof.* A middle \(p_2\) lies in \(M\) by the layer remark. Conversely let
\(m\in M\). A shortest \(x\)–\(m\) path \(x\,u\,m\) has
\(u\in N(x)\cap N(m)=A(m)\); a shortest \(m\)–\(y\) path \(m\,w\,y\) gives
\(w\in B(m)\). For any \(u\in A(m)\), \(w\in B(m)\):
\(d(u,y)\ge d(x,y)-1=3\) and \(d(u,y)\le 1+d(m,y)=3\); likewise
\(d(x,w)\ge 4-d(w,y)=3\) and \(\le d(x,m)+1=3\). So \(x,u,m,w,y\) have
distances \(0,1,2,3,4\) from \(x\), hence are five distinct vertices, and
the edges \(xu,um,mw,wy\) make \(x\,u\,m\,w\,y\) a 4-path with middle
\(m\). ∎

**T1 (pencil dichotomy — general graphs) — proved.** Either \(G\) has two
internally disjoint 4-paths, or all 4-paths of \(G\) form a pencil.

*Proof.* Assume no two 4-paths are internally disjoint. If \(|M|=1\), the
unique middle lies on every 4-path (T0): a pencil. Let \(|M|\ge2\) and
\(m\ne m'\in M\). Two paths \((u,m,w)\), \((u',m',w')\) through distinct
middles are internally disjoint iff \(u\ne u'\) and \(w\ne w'\) (all other
coincidences are barred by layers). Since the \(u\)- and \(w\)-choices in
T0's product are independent, "no disjoint pair between \(m\) and \(m'\)"
is equivalent to: \(A(m)\cup A(m')\) is a singleton (the pair is
**A-tied**), or \(B(m)\cup B(m')\) is a singleton (**B-tied**); all four
sets are nonempty by T0, so a tied union forces both sets equal to the
same singleton.

*Case 1: every pair of distinct middles is B-tied.* Fix any \(m_0\); for
every \(m\ne m_0\), \(B(m)=B(m_0)\) is one singleton \(\{b\}\); every
4-path ends \(b\,y\): pencil at \(b\).

*Case 2: some pair \((m_1,m_2)\) is not B-tied,* hence A-tied:
\(A(m_1)=A(m_2)=\{a\}\). For any other \(m\in M\): if \((m,m_1)\) and
\((m,m_2)\) were both B-tied, then \(B(m_1)=B(m)=B(m_2)\) as singletons,
making \((m_1,m_2)\) B-tied — contradiction. So \((m,m_1)\) or
\((m,m_2)\) is A-tied, forcing \(A(m)=\{a\}\). Every 4-path starts
\(x\,a\): pencil at \(a\). ∎

**T1′ (\(C_8\) equivalence — general graphs) — proved.** \(G\) has an
8-cycle through both \(x\) and \(y\) iff \(G\) has two internally disjoint
4-paths.

*Proof.* (⇐) The union of two internally disjoint \(x\)–\(y\) paths of
length 4 is a cycle on \(2+3+3=8\) distinct vertices through \(x\) and
\(y\). (⇒) An 8-cycle through \(x\) and \(y\) splits at \(x,y\) into two
internally disjoint simple \(x\)–\(y\) paths with lengths summing to 8,
each of length \(\ge d(x,y)=4\), hence both exactly 4. ∎

**T2 (\(C_4\)-free refinements) — proved.** Let \(G\) additionally be
\(C_4\)-free; equivalently, every two distinct vertices have at most one
common neighbor.

1. **(Single overlap.)** Two distinct 4-paths share at most one internal
   vertex. [If they share the vertices of two layers, they differ in the
   third, and the two differing vertices are distinct common neighbors of
   the shared flanking pair: shared layers \(\{1,2\}\) give
   \(p_3\ne q_3\in N(p_2)\cap N(y)\); \(\{2,3\}\) give
   \(p_1\ne q_1\in N(x)\cap N(p_2)\); \(\{1,3\}\) give
   \(p_2\ne q_2\in N(p_1)\cap N(p_3)\) — each a \(C_4\). Sharing all
   three layers makes the paths equal.]
2. **(Terminal pencil.)** If there are \(\ge2\) 4-paths and no two are
   internally disjoint, the pencil vertex \(c\) is unique and adjacent to
   a terminal. [Uniqueness: two common vertices would put two shared
   internal vertices on some pair, violating (1). If \(c\in M\): every
   4-path would have middle \(c\) (\(c\) can occupy only layer 2), so all
   4-paths lie in \(A(c)\times\{c\}\times B(c)\); but \(A(c)\) is a set of
   common neighbors of \(x\) and \(c\), so \(|A(c)|\le1\), similarly
   \(|B(c)|\le1\) — exactly one 4-path, contradicting \(\ge2\). Hence
   \(d(x,c)=1\) or \(d(c,y)=1\).]
3. **(Fan rigidity.)** Let the pencil sit at \(c\in N(x)\) with \(t\ge2\)
   paths (the case \(c\in N(y)\) is symmetric under swapping \(x,y\)).
   Then:
   - every \(m\in M\) has \(A(m)=\{c\}\) and \(|B(m)|=1\) [the 4-path
     through \(m\) supplied by T0 contains \(c\), and \(c\) can only be
     its layer-1 vertex, so \(c\in A(m)\); \(|A(m)|\le1\), \(|B(m)|\le1\)
     as common-neighbor sets]. Writing \(B(m_i)=\{b_i\}\), the 4-paths
     are exactly the \(t=|M|\) strands \(x\,c\,m_i\,b_i\,y\);
   - the middles are pairwise distinct, the exits are pairwise distinct,
     and there are **no cross chords**: \(m_ib_j\in E\) iff \(i=j\) [a
     cross chord would make \(x\,c\,m_i\,b_j\,y\) a 4-path sharing
     \(\{c,m_i\}\) with strand \(i\), violating (1)];
   - distinct middles have exactly \(c\) as common neighbor; distinct
     exits have exactly \(y\); each strand pair spans the hexagon
     \(c\,m_i\,b_i\,y\,b_j\,m_j\), so \(6\in\mathrm{Spec}(G)\) whenever
     \(t\ge2\).
4. **(Unique-path case.)** If \(G\) has exactly one 4-path
   \(x\,a\,m\,b\,y\), then \(M=\{m\}\) [any other middle would carry a
   second 4-path by T0].

**T3 (far-neighbor lemma) — proved.** Suppose \(C_4\)-free \(G\) has no
two internally disjoint 4-paths, with 4-paths pencilled at \(c\in N(x)\)
and strands \((m_i,b_i)_{i\le t}\), \(t\ge1\) (for \(t=1\) read \(c=a\),
the unique path's first vertex; the \(N(y)\)-side pencil is symmetric).
Then:

- every \(u\in N(x)\setminus\{c\}\) has \(d(u,y)\ge4\);
- every \(w\in N(y)\setminus\{b_1,\dots,b_t\}\) has \(d(x,w)\ge4\); in
  particular the vertices at coordinates
  \((d(x,\cdot),d(\cdot,y))=(3,1)\) are exactly the exits.

*Proof.* Let \(u\in N(x)\) with \(d(u,y)=3\) (\(\ge3\) always, since
\(d(x,y)=4\)). A shortest \(u\)–\(y\) path \(u\,\alpha\,\beta\,y\) has
\(d(x,\alpha)\le d(x,u)+1=2\) and \(d(x,\alpha)\ge4-d(\alpha,y)=2\), so
\(\alpha\in M\), and \(u\in N(x)\cap N(\alpha)=A(\alpha)=\{c\}\) (T2(3);
in the \(t=1\) case \(A(m)=\{a\}\) directly since \(|A(m)|\le1\ni a\)).
So \(u=c\). Let \(w\in N(y)\) with \(d(x,w)=3\). A shortest \(x\)–\(w\)
path \(x\,\alpha\,\beta\,w\) has \(d(\beta,y)\le d(\beta,w)+d(w,y)=2\)
and \(\ge4-d(x,\beta)=2\), so \(\beta\in M\) and
\(w\in N(\beta)\cap N(y)=B(\beta)\): an exit. ∎

**T4 (the band-4 pencil endgame — reduction proved; endgame open).**
Let \((T,x,y)\) be a vertex-taut 2-connected \(C_4\)-free core with
\(d(x,y)=4\) and \(s_{\max}\le8\) (the band-4 objects of the block
question, strict or equality). Exactly one of:

- \(T\) has two internally disjoint 4-paths — equivalently (T1′) a
  \(C_8\) **through both terminals**; or
- the 4-path system of \(T\) is a pencil: a fan at a terminal's neighbor
  (\(t\ge2\)) or a unique 4-path (\(t=1\)), with the T2/T3 structure.

Consequently the band-4 case of the block question closes — in the
strengthened form "every vertex-taut 2-connected \(C_4\)-free core with
\(d(x,y)=4\), \(s_{\max}\le8\) has a \(C_8\) through its terminals" —
**iff the pencil endgame holds**: no such core has a pencilled 4-path
system. Structural inventory available for the endgame (proved above,
plus the core axioms):

- far/near partition of both terminal neighborhoods (T3); with
  \(\deg(x)\ge2\), \(N(x)\setminus\{c\}\ne\emptyset\) in the fan case,
  and every through-path through a far vertex has length \(\ge5\);
- 2-connectivity gives an \(x\)–\(y\) path avoiding \(c\), necessarily
  of length in \(\{5,\dots,8\}\) (no 4-path avoids \(c\));
- tautness with \(s_{\max}\le8\) confines every vertex to
  \(d(x,v)+d(v,y)\le8\);
- \(N(c)\) inventory (fan case): \(N(c)\subseteq\{x\}\cup Z\cup
  \{m_1,\dots,m_t\}\cup W\) where \(|Z|\le1\) (\(Z\subseteq N(x)\), a
  common neighbor of \(x,c\), necessarily far) and \(W\) is the set of
  \(c\)-neighbors at coordinates \((2,3)\) [\(c\)'s \(L_2\)-neighbors
  with \(d(\cdot,y)=2\) are middles, hence strands];
- third-neighbor confinement: a middle's neighbors beyond \(c,b_i\) lie
  at coordinates \((2,3),(3,2),(3,3)\) or are other middles [neighbors
  in \(N(x)\) would be a second common neighbor of \(x,m_i\) beside
  \(c\); neighbors in \(N(y)\) would be a second exit for \(m_i\),
  i.e. \(|B(m_i)|\ge2\)]; an exit's neighbors beyond \(m_i,y\) lie at
  \((3,1)\) (other exits), \((3,2)\), \((4,1)\), \((4,2)\) [a neighbor
  at \((2,2)\) would be a cross chord or a second strand at \(m_i\)].

Status: **empty through order 15.** The exhaustive `E013` closed
catalogue shows the only vertex-taut band-4 core with \(s_{\max}\le8\)
at orders \(\le15\) is Petersen\(-e\), which is disjoint-type (two
internally disjoint shortest pairs; 7 \(C_8\)s). The pencil-type taut
band-4 (D)-objects at orders \(\le15\) all have a degree-1 terminal
(orders 9 and 15 — pendant lifts pencil at their attachment by
construction), so the endgame's obstruction must genuinely consume the
core axioms (both terminal degrees \(\ge2\)) and/or 2-connectivity,
consistent with `A014` T5.

## Corollaries

**C1 (rung reformulation).** The band-4 equality power rung (`A014` plan
item 2) is implied by the pencil endgame in strengthened form: a \(C_8\)
through both terminals, no \(C_{16}\) alternative needed at any order.
The band-4 case of block question (b′) then closes: no power-free
vertex-taut 2-connected core with \(s_{\min}=4\), \(s_{\max}\le8\)
exists. (Both band-4 rung targets have \(s_{\max}\le8\), so the endgame
also delivers the strict rung's power-freeness violation, though not its
\(C_4\)-only nonexistence claim.)

**C2 (hypothesis necessity — computational, `E014`).** \(C_4\)-freeness
is essential to both rungs and cannot be discharged:

- strict blocks exist with \(C_4\)s from order 6 (\(K_{3,3}-e\), band 3,
  \(S=\{3,5\}\) — the dossier's standing `L030` sharpness example,
  recast in block language); strict band-4 blocks with the exact rung
  shape \(S=\{4,5,6,7\}\) exist with \(C_4\)s at order 8;
- band-4 equality cores with \(S=\{4,\dots,8\}\) and **no \(C_8\)**
  exist with \(C_4\)s at order 9 (e.g. spectrum \(\{4,5,7,9\}\));
- the dichotomy T1/T1′ is general, but T2's refinements fail without
  \(C_4\)-freeness: two 4-paths can share two internal vertices, and
  middle pencils with \(\ge2\) paths occur (`E014` anchors 1–2; 946
  middle pencils in the general stream, none in the \(C_4\)-free
  stream).

**C3 (instance verification — computational, `E014`).** T0/T1/T1′
verified exhaustively on all connected graphs of orders 5–9 (43,419
distance-4 pairs) and T0–T3 consequences on all connected \(C_4\)-free
graphs of orders 5–11 (116,187 distance-4 pairs; zero middle pencils;
fan sizes 2/3/4 realized 22,332/885/10 times; disjoint-pair ⟺
\(C_8\)-through-terminals in every single case).

**C4 (catalogue status — computational, `E013` order-15 extension).**
Through order 15: no strict block; the `C031` five equality blocks are
the whole block world; the strict-15 scan found exactly one taut pinched
pair, machine-identified as D14's pendant lift (confirming the `C031`
swap-symmetry prediction of exactly one strict band-7 witness at order
15); the closed-15 scan found 20 hits, all pendant-type. No closed hit
at any band \(\le3\) exists through order 15: the equality-block ladder
genuinely starts at band 4. That emptiness is empirical, not a lemma;
the band-2 closed rung (\(S\subseteq\{2,3,4\}\), \(4\in S\)) is the
smallest open closed-block question below the band-4 fight. An
order-16 closed scan was launched and was still running at S015's
close; its harvest is reserved for a short follow-up session.

## Plan and decisive tests

1. **The pencil endgame** (the new primary target): prove that a
   vertex-taut 2-connected \(C_4\)-free core with \(d(x,y)=4\),
   \(s_{\max}\le8\) cannot have a pencilled 4-path system. Split into
   the fan case (\(t\ge2\)) — which owns hexagons, strand rigidity and
   the \(N(c)\) inventory — and the unique-path case (\(t=1\)). Killed
   by: any pencil-type band-4 taut core at order \(\ge16\) (the order-16
   closed scan tests 16 directly; through 15 the case is exhaustively
   empty).
2. **Strict rung (i)** — unchanged statement, now known to need
   \(C_4\)-freeness essentially (C2). Deferred behind the endgame.
3. Search legs: order-16 closed catalogue (running; the first order
   where a hit could be \(C_8\)-free, since `C027` stops at 15);
   order 17+ deferred.

## Construction attempts against the endgame (failure data, provisional)

Three hand attempts to BUILD a fan-type band-4 taut core (t = 2 strands,
middle matching \(m_1m_2\)), each C4-free with all degrees correct at the
point of death:

1. **Exit-matching version** (\(b_1b_2\in E\), far web \(u,w,v\) with
   \(v\sim b_1\)): dies to the 8-cycle
   \(x\,c\,m_2\,b_2\,b_1\,v\,w\,u\) — a \(C_8\) through \(x\) only, so
   T1′ does not see it; exit matchings splice the far web into the
   strand web at length exactly 8.
2. **Hub-splice version** (far vertex \(u\sim c\) to reach degree 3):
   dies to the 9-path
   \(x\,u\,c\,m_1\,m_2\,b_2\,v_2\,v\,b_1\,y\) — the \(u\sim c\) edge
   lets far-side and strand-side segments concatenate past
   \(s_{\max}=8\).
3. **FarY version** (exits supported by \((4,1)\)-vertices
   \(g_i\sim y\), far web \(u,w,h\)): every attempted closing edge from
   the \((3,2)\)-vertex \(h\) into the existing web creates a \(C_4\)
   (\(h m_1\), \(h b_1\), \(h b_2\), \(h g_2\) all die this way), and
   every neighbor near \(y\) would make a new middle whose 4-path is
   disjoint from strand 1, hence a \(C_8\) through both terminals.

The recurring obstruction ("the cascade"): internal degree \(\ge3\)
forces each support vertex to acquire neighbors, but neighbors at
\(d(\cdot,y)\le2\) create new middles with \(A(m)\ne\{c\}\) — disjoint
4-paths — hence \(C_8\); neighbors back toward \(x\) or \(c\) splice
\(\ge9\)-paths; and lateral closures inside the support web hit
\(C_4\)-freeness. Unexplored escape: the deep coordinate classes
\((3,3),(3,4),(4,3),(4,4)\) (tautness allows \(d(x,v)+d(v,y)=8\)), where
a large C4-free web could live if every vertex still finds an exactly-
length-8 through-path; the hand attempts never closed there, and the
order-16 scan is the first systematic probe of that territory. These are
construction failures, not proofs; they map the pressure points for the
impossibility argument.

Two provisional endgame micro-lemmas (proof sketches only, not ledger
material yet):

- middles induce a matching, exits induce a matching [a 2-edge path
  among middles closes a \(C_4\) through \(c\); dually through \(y\)];
- with \(t\ge3\) strands and no \(C_8\): no \((2,3)\)-vertex
  \(z\in N(c)\) is adjacent to a matched middle — if \(z\sim m_l\) and
  \(m_l\sim m_j\), pick a third strand \(i\notin\{l,j\}\) and
  \(c\,m_i\,b_i\,y\,b_j\,m_j\,m_l\,z\) is an 8-cycle.

Unique-path case inventory (t = 1, path \(x\,a\,m\,b\,y\), \(M=\{m\}\)),
for the second endgame branch:

- far lemmas hold verbatim (T3 with \(c=a\)): \(N(x)\setminus\{a\}\)
  and \(N(y)\setminus\{b\}\) are far, and both are nonempty by the
  terminal-degree axiom;
- \(m\)'s third neighbor lies at \((2,3)\), \((3,2)\) or \((3,3)\)
  [neighbors in \(N(x)\) would be a second common neighbor of \(x,m\)
  beside \(a\); dually for \(N(y)\); \((2,2)\) is exhausted by
  \(M=\{m\}\)];
- \(a\)'s neighbors beyond \(x,m\): at most one triangle-mate in
  \(N(x)\) (necessarily far), the rest at \((2,3)\) or \((2,4)\); dual
  for \(b\);
- no \(C_8\) through both terminals exists (that IS the pencil), and
  two internally disjoint through-paths have length sum in
  \(\{9,\dots,16\}\) with \((8,8)\) the only \(C_{16}\) shape;
- empirical: no taut unique-path band-4 object exists anywhere in the
  data — the two pendant-type closed band-4 pairs are fans (t = 2 at
  order 9, t = 4 at order 15) and P10 is disjoint-type — so BOTH
  endgame branches are empty in all known instances.

## Failure analysis

Not abandoned; one planned sub-claim died productively. The first hand
analysis derived the pencil via a \(C_4\)-forced "triangle exclusion"
and treated \(C_4\)-freeness as essential to the dichotomy itself; the
planned machine anchor — realize the triangle configuration (three
pairwise-intersecting 4-paths, no common vertex) in a \(C_4\)-carrying
graph — **failed to build**: edge-closure kept generating extra 4-paths
containing an internally disjoint pair. Chasing that failure produced
the product structure (T0) and the two-tie argument (T1), removing the
\(C_4\)-hypothesis from the dichotomy entirely and revealing that the
triangle configuration is impossible in every graph. The failed anchor
was replaced by the two correct sharpness anchors now in `E014`.

## Salvageable results

T0–T3 are unconditional lemmas (ledger row `L033`); T4's reduction is
proved and its endgame is the sharpest open question of the band-4
program; C2's specimens (strict-with-\(C_4\) blocks from order 6,
\(C_8\)-free equality cores from order 9) delimit every future rung
statement.

## Exit state

- Status: active
- Promoted records: `L033` (T0–T3 and T4's reduction), `C032`
  (order-15/16 catalogue extension), `C033` (`E014` verification and
  hypothesis necessity).
- Next action: the pencil endgame, fan case first, with the order-16
  scan as the live falsification leg.
