# A022 — The chain-case constraint system: full closure arithmetic at every cut, block order bounds, and the glued-witness kill test

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: closed (targets reached; kill condition did not fire in range;
  order-bound theorem delivered)
- Portfolio role: primary (proof side of case (5b), `G015` route R1;
  session `S021`, worker leg W1 — the "chain-cancellation tension" item
  recorded as next action in `problem.json` after S020)

## Intended mechanism

`A019` W1-T14 (ledgered in `L042`) showed that a cut vertex in the
case-(5b) residual object forces each side's local through-set to meet a
forbidden set while the total avoids one — a cancellation tension across
the Minkowski sum \(S=S_1+S_2\) (`L032`/`L035` T0). This leg runs that
tension to a verdict, in three coordinated moves:

1. **Complete the constraint system.** W1-T14 used only the 2-closure at
   each cut. The same minimality engine admits 1-closures and
   0-closures (merges) at every prefix/suffix pair — a battery of forced
   memberships far denser than W1-T14: every prefix must meet
   \(\mathbb P-2\), \((\mathbb P-1)\cup\{1\}\), **and**
   \(\mathbb P\cup\{1,2\}\), with saturation versions at the cut vertex
   and (when the attachment degree is \(\ge3\)) at every prefix pair.
2. **Quantify the cancellation.** Determine exactly which pairs of
   forced memberships can collide into \(\mathbb P-2\) (the arithmetic
   of \(2^p+2^q\) mod small powers), i.e. state the tension as a finite
   list of exponent-disjointness conditions — the honest content of
   "the forbidden lengths must cancel across the chain".
3. **Bound or kill.** Per-block order bounds via `C027`/`C036` turn the
   chain case into an order dichotomy (the recorded falsifiable target:
   bound the chain length or prove 2-connectivity). In parallel, run the
   pre-registered kill test: try to *realize* the full constraint system
   by gluing catalogued small blocks (power-freeness dropped) — the
   chain-case analogue of Petersen\(-e\) (`C037`). Either the witness
   exists (arithmetic-only exclusion is dead, order bounds survive) or
   the realized through-set arithmetic obstructs it in range (recorded
   with its mechanism).

Distinctive vs. the alternatives: this is the only live proof-side lever
against case (5b) that `A021`/`C037` did not kill — it is set-sum
structure, not residue structure, so the parity ceiling (`A021` T1) does
not apply to it; and it is the branch of case (5b) where minimality
yields *strictly more* than in the 2-connected branch, because proper
subgraphs (prefixes) hide the second terminal.

## Entry assumptions

Statement 0.1 verbatim; D-A1–D-A5 (`A011`); tightness per `A018` T2.
Consumed at recorded strength: `L027` (lobe dichotomy), `L032` (chain
decomposition, core clauses), `L035` T0 (degree-free chain
decomposition) and T2 (parity structure theorem), `L039` (closure
calculus and the \(\mathcal G\)-correspondence; its W1-T1 pair and merge
forms are used for arbitrary vertex pairs, as recorded), `L040`,
`L041` (case analysis; only (5b) survives under (R)), `L042` (residual
structure, including `A019` W1-T10/T12/T14), `C027` (atom-class
emptiness through 15; tested), `C036` (order-16 emptiness for the
exactly-two-degree-2 profile; tested). Nothing from `C004`–`C006`.
Per `A021`/`C037`: no congruence-type argument beyond parity is
attempted anywhere below.

**Standing setting (the chain case).** \((B,u,a,b,H)\) is the case-(5b)
residual object: \(B\) a minimum-order tight 1-atom (\(n_0=|V(B)|\ge18\)
by `C036`), \(u\) its degree-2 vertex, \(N_B(u)=\{a,b\}\),
\(\deg_B(a)=\deg_B(b)=3\), \(H=B-u\) connected, \((H,a,b)\in\mathcal G\)
vertex-taut, \(S=S(H,a,b)\), \(|V(H)|=n_0-1\ge17\). This configuration
is what (R) forces via `L041`; every deduction below assumes it.
Additionally in this attempt: **\(H\) is not 2-connected**, i.e. has a
cut vertex (except W1-T4, which holds for every residual object).

**Conditionality labels.** Each deduction is marked
- **[min]** — its proof uses only \(n_0\)-minimality of \(B\) over the
  class of tight 1-atoms (a power-free reduct that is
  tight-1-atom-shaped of order \(<n_0\) is a direct contradiction), or
- **[R]** — it additionally needs (R) ("no counterexample of order
  \(<n_0\)": the reduct is only \(\delta\ge3\)-shaped).

Both live inside the (R)-framed configuration; the label records which
engine the proof consumes, as `A019` did.

Notation as in `A019`: \(\mathbb P=\{4,8,16,\dots\}\),
\(\mathbb P-1=\{3,7,15,\dots\}\), \(\mathbb P-2=\{2,6,14,30,\dots\}\);
\(P_G(x,y)\) the set of simple \(x\)–\(y\) path lengths of \(G\);
Minkowski sum \(X+Y=\{x+y\}\); \(X+c=\{x+c\}\).

## Targeted obligations

- `G015`: the cubic reduction, route R1 — the case-(5b) chain branch.
- `G013`(a): structure theory of the tight-1-atom question.

## Plan and decisive tests

1. Prove the chain frame and the extended closure battery; assemble the
   per-cut constraint system with exact side conditions.
2. Quantify the cancellation (the collision table). Decisive question:
   does the forced system self-contradict at some chain length? (It does
   not — W1-T6/W1-T11.)
3. Order bounds per block via `C027`/`C036`; the dichotomy theorem.
4. **Pre-registered kill condition (from the S021 brief, carried from
   S020's checkpoint):** if a vertex-taut \(C_4\)-free two-terminal
   graph with a cut vertex, exactly two degree-2 vertices (the
   terminals), power-freeness dropped, realizes the full forced
   system (every W1-T14-pattern membership, total avoiding
   \(\mathbb P-2\), total meeting \(\mathbb P\) and \(\mathbb P-1\)),
   then arithmetic-only exclusion of the chain case is dead and the
   surviving product is the order-bound theorem. Instrument: `E020`
   (block catalogue + glued witnesses). Pivot triggers: kill fires →
   record witness, retire arithmetic-only exclusion; kill refuted in
   range → record the mechanism and the next falsifiable rung.

## Deductions

Deduction numbers W1-T1–W1-T12 are this worker's; references to
`A019`'s deductions always carry the prefix "`A019`".

---

### W1-T1 (the chain frame) — proved [min for (c),(d); the rest is inherited structure]

**Claim.** In the standing setting with \(H\) not 2-connected:

1. Every cut vertex of \(H\) separates \(a\) from \(b\); the block–cut
   tree of \(H\) is a path. Writing the blocks \(L_1,\dots,L_m\)
   (\(m\ge2\)) with cut vertices \(c_1,\dots,c_{m-1}\),
   \(c_0:=a\in L_1\) only, \(c_m:=b\in L_m\) only, and
   \(T_i=S(L_i,c_{i-1},c_i)\): each \((L_i,c_{i-1},c_i)\) is
   vertex-taut, \(S=T_1+\dots+T_m\), and
   \(\mathrm{Spec}(H)=\bigcup_i\mathrm{Spec}(L_i)\); every block is
   power-free and \(C_4\)-free.
2. Neither \(a\) nor \(b\) is a cut vertex of \(H\), and
   \(ab\notin E(H)\). Consequently the full `A019` W1-T10(2)
   memberships apply to \(S\) under (R).
3. The end blocks \(L_1,L_m\) are 2-connected; every bridge block is
   interior and no two bridges are adjacent; with \(k\) the number of
   2-connected (non-bridge) blocks, \(m-k\le k-1\), i.e.
   \(k\ge\lceil(m+1)/2\rceil\).
4. \(\deg_{L_1}(a)=2=\deg_{L_m}(b)\); every non-attachment,
   non-terminal vertex of a block has block-degree \(=\) its
   \(H\)-degree \(\ge3\); each attachment vertex has degree \(\ge2\) in
   each adjacent 2-connected block and degree 1 in an adjacent bridge.
   Hence, as a standalone graph, every non-bridge block is 2-connected,
   \(C_4\)-free, power-free, of minimum degree \(\ge2\), with at most
   two vertices of degree 2, all of them among its two terminals.
5. *(Gateway lemma.)* For every \(i\), write
   \(H_1^{(i)}=L_1\cup\dots\cup L_i\) and
   \(H_2^{(i)}=L_{i+1}\cup\dots\cup L_m\) (union along the shared cut
   vertices), so \(V(H_1^{(i)})\cap V(H_2^{(i)})=\{c_i\}\). Then for
   all \(x,y\in V(H_1^{(i)})\):
   \(P_H(x,y)=P_{H_1^{(i)}}(x,y)\); for all \(x,y\in V(L_j)\):
   \(P_H(x,y)=P_{L_j}(x,y)\). In particular
   \(A_i:=S(H_1^{(i)},a,c_i)=P_H(a,c_i)=T_1+\dots+T_i\) and
   \(Z_i:=S(H_2^{(i)},c_i,b)=P_H(c_i,b)=T_{i+1}+\dots+T_m\), and
   \(S=A_i+Z_i\) for every \(i\).

*Proof.* (1) \((H,a,b)\) is vertex-taut with non-terminal degrees
\(\ge3\) and terminal degrees \(2\ge1\), so `L032` (A014 T3) applies —
its parts T3.1/T3.2/T3.4 give the separation, the path-shaped block–cut
tree with \(a\in B_1\) only and \(b\in B_m\) only (D-P3), the block
tautness, the Minkowski identity, and the spectrum union (`L035` T0 is
the degree-free form of the same statements). Power-freeness and
\(C_4\)-freeness of blocks: subgraphs of \(H\), whose spectrum is
power-free by \((H,a,b)\in\mathcal G\) (`L039`).

(2) If \(a\) were a cut vertex: \(\deg_H(a)=2\), so \(H-a\) has at most
two components; a component avoiding \(b\) contains a vertex on no
simple \(a\)–\(b\) path (leaving that component is possible only
through \(a\)), contradicting tautness (this is the first paragraph of
`A019` W1-T14's proof; repeated for self-containment). Symmetrically for
\(b\). For \(ab\notin E\): an edge lies in exactly one block; \(a\) lies
only in \(L_1\) and \(b\) only in \(L_m\) with \(m\ge2\), so no block
contains both, hence no edge \(ab\). (Direct alternative: any cut vertex
\(c\) satisfies \(c\notin\{a,b\}\), and if \(ab\in E\) then \(a,b\) lie
in one component of \(H-c\) — contradicting the separation in (1).)
Then `A019` W1-T10(2) [R] gives \(S\cap\mathbb P\ne\emptyset\) and
\(S\cap(\mathbb P-1)\ne\emptyset\), while \(S\cap(\mathbb P-2)
=\emptyset\) holds absolutely (\((H,a,b)\in\mathcal G\)).

(3) \((H,a,b)\) is a core (terminal degrees \(2\ge2\)), so `L032` T3.3
applies verbatim: no bridge is an end block, no two bridges are
adjacent, \(\#\text{bridges}\le\#\{2\text{-connected blocks}\}-1\);
rearranged, \(k\ge(m+1)/2\), and \(k\) is an integer.

(4) The degree statements are `L032` T3.3 plus: all edges of \(H\) at
\(a\) lie in \(L_1\) (\(a\) is in no other block), so
\(\deg_{L_1}(a)=\deg_H(a)=2\); likewise at \(b\). A 2-connected block
has minimum degree \(\ge2\), giving the attachment clause. Standalone
profile: the only vertices of \(L_i\) that can have block-degree \(<3\)
are its two terminals (interior vertices keep their \(H\)-degree
\(\ge3\)); in a 2-connected block the minimum degree is \(\ge2\); so at
most two vertices of degree exactly 2, all terminals.

(5) Let \(x,y\in V(H_1^{(i)})\) and let \(Q\) be a simple \(x\)–\(y\)
path of \(H\) using a vertex \(w\in V(H_2^{(i)})\setminus\{c_i\}\).
Every walk between \(V(H_1^{(i)})\setminus\{c_i\}\) and
\(V(H_2^{(i)})\setminus\{c_i\}\) passes \(c_i\) (the two vertex sets
meet only in \(c_i\) and there is no edge between their
\(c_i\)-complements, since an edge lies in one block). If
\(x,y\ne c_i\), then \(Q\) passes \(c_i\) before \(w\) and again after
\(w\) — twice, impossible in a simple path. If \(y=c_i\), then \(Q\)
reaches \(c_i\) strictly before \(w\), but \(c_i\) is its endpoint —
again impossible. So \(Q\) stays in \(H_1^{(i)}\); the converse
inclusion is trivial. The block version is the same argument applied
twice (leaving \(L_j\) through one attachment is terminal: re-entry
would revisit it, and the other side of the chain is unreachable
without it). The identities for \(A_i,Z_i\) then follow from (1)
applied to the sub-chains \(L_1,\dots,L_i\) and \(L_{i+1},\dots,L_m\),
and \(S=A_i+Z_i\) by grouping the Minkowski sum. ∎

**Remark (2-connectivity gives tautness for free).** The standard 2-fan
consequence of Menger's theorem implies that *every* 2-connected
two-terminal graph is vertex-taut w.r.t. every terminal pair (fan from
\(v\) to \(\{a,b\}\): two paths disjoint except at \(v\), ending at
\(a\) and \(b\); their union is a simple \(a\)–\(b\) path through
\(v\)). This external classical fact is **not consumed** by any
deduction here (block tautness comes from `L032`); it is recorded
because `E020` corroborated it on all 226,619 catalogued
block/terminal-pair instances (zero exceptions) and because it makes
tautness filters free for future generators on 2-connected candidates.

---

### W1-T2 (the prefix profile) — proved [structure only]

**Claim.** For \(1\le i\le m-1\), the prefix \(W=H_1^{(i)}\) is
connected, power-free, \(C_4\)-free, of order
\(|V(W)|\le n_0-2\), with degree profile
\[\deg_W(a)=2,\qquad \deg_W(c_i)=d_i:=\deg_{L_i}(c_i),\qquad
\deg_W(v)=\deg_H(v)\ge3\ \ (v\ne a,c_i),\]
and \(d_i=1\) iff \(L_i\) is a bridge, else \(d_i\ge2\). The mirror
statements hold for the suffix \(H_2^{(i)}\) with terminals
\((c_i,b)\) and \(d_i':=\deg_{L_{i+1}}(c_i)\).

*Proof.* Connectivity: a union of blocks along the path of cut
vertices. Power-/\(C_4\)-freeness: subgraph of \(H\). Order:
\(|V(H_1^{(i)})|+|V(H_2^{(i)})|=|V(H)|+1=n_0\), and
\(|V(H_2^{(i)})|\ge2\) (it contains \(c_i\ne b\)). Degrees: every
\(H\)-edge at a vertex of \(V(W)\setminus\{c_i\}\) lies in \(W\)
(edges leaving \(W\) pass \(c_i\), W1-T1(5) argument), so those degrees
are the \(H\)-degrees: \(2\) at \(a\), \(\ge3\) elsewhere
(non-terminal vertices of \(H\); note \(b\notin V(W)\)); at \(c_i\)
exactly the \(L_i\)-edges of \(c_i\) lie in \(W\), giving \(d_i\).
Bridge iff \(d_i=1\) is the definition of a bridge block. ∎

---

### W1-T3 (the closure battery on prefixes) — proved [min]

**Claim.** Let \(W=H_1^{(i)}\), \(d=d_i\), and suppose \(L_i\) is
**not** a bridge (\(d\ge2\)). Write \(P(x,y)=P_W(x,y)\)
(\(=P_H(x,y)\) by W1-T1(5)). Then:

1. *(2-closure at \((a,c_i)\); this is `A019` W1-T14(1), cited not
   reproved.)* \(A_i\cap(\mathbb P-2)\ne\emptyset\).
2. *(1-closures into the cut vertex — cut-vertex Mersenne
   saturation; NEW.)* For every \(x\in V(W)\setminus\{a\}\) with
   \(xc_i\notin E\): \(P(x,c_i)\cap(\mathbb P-1)\ne\emptyset\).
3. *(1-closures at general pairs; NEW.)* If \(d\ge3\): for every pair
   \(x,y\in V(W)\setminus\{a\}\), \(xy\notin E\):
   \(P(x,y)\cap(\mathbb P-1)\ne\emptyset\). (For pairs containing
   \(c_i\), item 2 already gives this at \(d\ge2\).)
4. *(2-closures from \(a\); NEW.)* If \(d\ge3\): for every
   \(x\in V(W)\setminus\{a\}\):
   \(P(a,x)\cap(\mathbb P-2)\ne\emptyset\). (For \(x=c_i\) this is
   item 1, at \(d\ge2\).)
5. *(0-closures (merges) at pairs avoiding \(a\); NEW.)* For every
   pair \(x,y\in V(W)\setminus\{a\}\) with \(xy\notin E\),
   \(N_W(x)\cap N_W(y)=\emptyset\), and (\(c_i\in\{x,y\}\) or
   \(d\ge3\)): \(P(x,y)\cap\mathbb P\ne\emptyset\).

The mirror statements hold on suffixes (with \(b,d_i'\) in place of
\(a,d\)). At a bridge cut (\(d_i=1\)), `A019` W1-T14(2) applies
instead: \(A_i\cap(\mathbb P-1)\ne\emptyset\).

*Proof.* Each item modifies \(W\) into a graph \(G\) that is connected,
simple, of order \(<n_0\), whose degree list has \(u\)-shape "unique
sub-cubic vertex, of degree 2"; \(\mathrm{Spec}(W)\subseteq
\mathrm{Spec}(H)\) is power-free, so by the closure calculus (`L039`,
i.e. `A019` W1-T1 applied to the relevant pair) \(G\) is power-free iff
the named path set misses the named forbidden set; power-freeness would
make \(G\) a tight 1-atom of order \(<n_0\), contradicting the
minimality of \(n_0\) [min]. The bookkeeping per item:

(2) \(G=W+xc_i\). Simple (non-adjacent pair), connected, order
\(\le n_0-2\). Degrees: \(a\): 2; \(c_i\): \(d+1\ge3\); \(x\):
\(\deg_W(x)+1\ge4\) (as \(x\ne a,c_i\), so \(\deg_W(x)\ge3\) by
W1-T2); others unchanged \(\ge3\). Unique sub-cubic: \(a\), degree 2.
By `L039`'s pair form,
\(\mathrm{Spec}(G)=\mathrm{Spec}(W)\cup(P(x,c_i)+1)\); if
\(P(x,c_i)\cap(\mathbb P-1)=\emptyset\), \(G\) is power-free. ∎(2)

(3) \(G=W+xy\), \(x,y\ne a\). Degrees: \(x,y\) rise to \(\ge4\) (or
\(c_i\in\{x,y\}\) rises to \(d+1\ge3\)); \(c_i\) keeps \(d\ge3\) if
\(c_i\notin\{x,y\}\) — this is where \(d\ge3\) is consumed; \(a\)
keeps 2. Unique sub-cubic \(a\). Spectrum as in (2) with
\(P(x,y)+1\). ∎(3)

(4) \(G=W+u'\), \(u'\) new, \(N(u')=\{a,x\}\) (legal for any \(x\ne a\),
adjacent or not). Order \(\le n_0-1\). Degrees: \(u'\): 2; \(a\): 3;
\(x\): \(\ge4\) if \(x\ne c_i\) (needs \(d\ge3\) at \(c_i\) to keep
\(c_i\) non-sub-cubic), or \(d+1\ge3\) if \(x=c_i\). Unique sub-cubic:
\(u'\). \(\mathrm{Spec}(G)=\mathrm{Spec}(W)\cup(P(a,x)+2)\)
(`L039` 2-closure at the pair \((a,x)\)); power-free iff
\(P(a,x)\cap(\mathbb P-2)=\emptyset\). ∎(4)

(5) \(G=W/(x{=}y)\). Legality (simplicity) is exactly \(xy\notin E\)
and no common neighbour in \(W\). Connected; order \(\le n_0-3\).
Degrees: merged vertex \(\deg_W(x)+\deg_W(y)\ge3+2=5\) (at least one
of \(x,y\) is not \(c_i\)); \(a\): 2; \(c_i\): absorbed if
\(c_i\in\{x,y\}\), else keeps \(d\ge3\) — the side condition; others
\(\ge3\). Unique sub-cubic: \(a\). By `L039`'s merge inclusion,
\(\mathrm{Spec}(G)\subseteq\mathrm{Spec}(W)\cup P(x,y)\); if
\(P(x,y)\cap\mathbb P=\emptyset\), \(G\) is power-free (only the
inclusion direction is used, per the recorded asymmetry). ∎(5) ∎

**Reading.** The prefix hides \(b\); that is why every one of these
closures lands on a *tight-1-atom-shaped* reduct — the [min] engine —
where the same closure applied to \(H\) itself would leave \(b\)
sub-cubic and yield only a 2-atom shape (no lever). Item 2 says every
non-bridge block is Mersenne-saturated **at its attachment vertices**
as a standalone graph (apply it to \(x\in V(L_i)\) and use the block
gateway); `A019` W1-T12 said this at the terminals \(a,b\). Items 3–5
say that a prefix whose attachment degree is \(\ge3\) is saturated at
*every* pair — a rigidity budget that grows with the chain.

---

### W1-T4 (terminal power saturation in \(H\)) — proved [min]; holds for EVERY residual object, 2-connected or not

**Claim.** Let \((B,u,a,b,H)\) be any case-(5b) residual object (no cut
vertex assumed). For every \(x\in V(H)\setminus\{a,b\}\) with
\(ax\notin E(H)\) and \(N_H(a)\cap N_H(x)=\emptyset\):
\[P_H(a,x)\cap\mathbb P\ne\emptyset.\]
The mirror holds at \(b\). (At \(x=b\) the statement is `A019`
W1-T10(2)'s first clause, which is [R]; the interior case above is
[min].)

*Proof.* Let \(G=H/(a{=}x)\): simple by the two legality hypotheses,
connected, of order \(n_0-2<n_0\). Degrees: merged vertex
\(\deg_H(a)+\deg_H(x)=2+\deg_H(x)\ge5\); \(b\): 2; all others \(\ge3\).
Unique sub-cubic: \(b\), of degree 2 — tight-1-atom-shaped. By `L039`'s
merge inclusion,
\(\mathrm{Spec}(G)\subseteq\mathrm{Spec}(H)\cup P_H(a,x)\) with
\(\mathrm{Spec}(H)\) power-free; if \(P_H(a,x)\cap\mathbb P=\emptyset\)
then \(G\) is power-free, a tight 1-atom of order \(<n_0\) —
contradiction [min]. ∎

**Reading and discipline.** This is the \(\mathbb P\)-channel sibling
of `A019` W1-T12 (which used 1-closures for the
\(\mathbb P-1\)-channel): order-minimality forces, at each terminal,
*power-of-two* path lengths to every non-neighbour at distance
\(\ge3\). `A019` did not record it. Two cautions: (i) on Petersen\(-e\)
the hypothesis set is empty (diameter 2: every non-adjacent pair has a
common neighbour), so the lemma is vacuously calibrated there — it
consumes minimality, which the calibration bar allows; (ii) by the
`E016` A6 precedent, such saturation conditions are expected to be
generically satisfied in the ambient class once distances grow;
W1-T4 is therefore recorded as **forced structure and a search filter,
not a standalone exclusion lever**, and any future promotion to a
primary lever must first run an A6-style genericity kill test
(named follow-up; not run here).

---

### W1-T5 (the assembled chain system) — proved [labels per row]

**Claim.** In the chain case, for every cut index \(1\le i\le m-1\),
with \(A_i,Z_i\) as in W1-T1(5):

| # | constraint | condition | label |
|---|---|---|---|
| (C1) | \(A_i\cap(\mathbb P-2)\ne\emptyset\) | \(L_i\) non-bridge | [min] (`A019` W1-T14(1)) |
| (C1′) | \(A_i\cap(\mathbb P-1)\ne\emptyset\) | \(L_i\) bridge | [min] (`A019` W1-T14(2); side condition \(c'\ne a\) automatic, bridges are interior) |
| (C2) | \(A_i\cap(\mathbb P-1)\ne\emptyset\) **or** \(1\in A_i\) | always | [min] (`A019` W1-T12 at \(z=c_i\), legal since \(c_i\ne b\)) |
| (C3) | \(A_i\cap\mathbb P\ne\emptyset\) **or** \(1\in A_i\) **or** \(2\in A_i\) | always | [min] (W1-T4 at \(x=c_i\); the escapes are exactly its legality conditions) |
| (C4–C6) | mirrors of C1–C3 for \(Z_i\) (with \(L_{i+1}\), \(b\)) | — | [min] |
| (C7) | \(S=A_i+Z_i\) avoids \(\mathbb P-2\) | always | absolute (\(\mathcal G\)-membership) |
| (C8) | \(S\cap\mathbb P\ne\emptyset\) and \(S\cap(\mathbb P-1)\ne\emptyset\) | always | [R] (`A019` W1-T10(2); \(ab\notin E\) by W1-T1(2)) |

Escapes are localized: \(1\in A_i\) iff \(i=1\) and \(ac_1\in E(L_1)\);
\(2\in A_i\) iff (\(i=1\) and \(a,c_1\) have a common neighbour in
\(L_1\)) or (\(i=2\) and \(1\in T_1\) and \(1\in T_2\)). In particular
for \(i\ge2\), (C2) reads \(A_i\cap(\mathbb P-1)\ne\emptyset\)
outright, and for \(i\ge3\), (C3) reads \(A_i\cap\mathbb
P\ne\emptyset\) outright. Mirrors at \(m-1,m-2\) for \(Z_i\).

Moreover *(redundancy of bridge rows)*: (C1′) at a bridge cut follows
from (C1) at the neighbouring cut — if \(L_i\) is a bridge then
\(i\ge2\), \(L_{i-1}\) is non-bridge, and
\(A_i=A_{i-1}+1\), so \(A_{i-1}\cap(\mathbb P-2)\ne\emptyset\) gives
\(A_i\cap(\mathbb P-1)\ne\emptyset\); mirror on suffixes.

*Proof.* (C1)/(C1′): `L042`'s recorded W1-T14, whose prefix graph is
exactly \(W=H_1^{(i)}\) (W1-T2 supplies the degree profile its proof
uses). (C2): `A019` W1-T12 applied to the pair \((a,z)\), \(z=c_i\ne
b\), which is [min] in that case; \(P_H(a,c_i)=A_i\) by W1-T1(5); the
lemma requires \(ac_i\notin E\), i.e. \(1\notin A_i\), else the escape.
(C3): W1-T4 at \(x=c_i\) (an interior vertex, \(c_i\ne b\)); its
legality conditions \(ac_i\notin E\), \(N(a)\cap N(c_i)=\emptyset\) are
precisely \(1\notin A_i\), \(2\notin A_i\) (a common neighbour is a
length-2 path and conversely). (C7): \((H,a,b)\in\mathcal G\); the
factorization over any cut is W1-T1(5). (C8): W1-T1(2). Escapes:
\(1\in A_i\) means \(ac_i\in E(H)\); \(N(a)\subseteq V(L_1)\) and
\(c_i\in V(L_1)\) forces \(i=1\) (distinct cuts; blocks meet only
consecutively). \(2\in A_i\) means a common neighbour \(w\) of
\(a,c_i\): \(w\in N(a)\subseteq V(L_1)\) and
\(w\in N(c_i)\subseteq V(L_i)\cup V(L_{i+1})\); for \(i\ge3\) those
vertex sets are disjoint; for \(i=2\), \(w=c_1\), forcing the edges
\(ac_1\) (\(1\in T_1\)) and \(c_1c_2\) (\(1\in T_2\)); for \(i=1\),
\(w\) is a common neighbour inside \(L_1\). Redundancy: no two bridges
adjacent and no bridge end block (W1-T1(3)) make \(L_{i-1}\)
non-bridge; \(T_i=\{1\}\) for a bridge gives \(A_i=A_{i-1}+1\), and
\(x\in A_{i-1}\cap(\mathbb P-2)\) gives
\(x+1\in A_i\cap(\mathbb P-1)\). ∎

**Reading.** Every proper prefix and suffix of the chain is forced to
behave like a full W1-T10 object — meeting \(\mathbb P-2\),
\(\mathbb P-1\), **and** \(\mathbb P\) (mod localized escapes) — and
all of that is [min], strictly cheaper than the [R]-conditional
memberships of the total. The chain case is thus *more* constrained
than the 2-connected case at every epistemic level.

---

### W1-T6 (the collision table: the cancellation quantified) — proved [arithmetic]

**Claim.** Let \(x=2^p+\varepsilon_1\), \(y=2^q+\varepsilon_2\) with
\(p,q\ge2\), \(\varepsilon_1,\varepsilon_2\in\{0,-1,-2\}\). Then
\(x+y\in\mathbb P-2\) **iff** \(p=q\) and
\(\{\varepsilon_1,\varepsilon_2\}\in\bigl\{\{-1,-1\},\{0,-2\}\bigr\}\)
(in both cases \(x+y=2^{p+1}-2\)). In particular:

- \((\mathbb P-2)+(\mathbb P-2)\), \(\mathbb P+\mathbb P\),
  \(\mathbb P+(\mathbb P-1)\), and \((\mathbb P-1)+(\mathbb P-2)\)
  never meet \(\mathbb P-2\) (the orchestrator-suggested lead (c) is
  verified as the first of these);
- \((\mathbb P-1)+(\mathbb P-1)\) and \(\mathbb P+(\mathbb P-2)\) meet
  \(\mathbb P-2\) exactly at equal exponents.

**Corollary (exponent dodging at every cut).** Write
\(M(X)=\{t:2^t-1\in X\}\), \(E_0(X)=\{t:2^t\in X\}\),
\(E_2(X)=\{t:2^t-2\in X\}\). In the chain case, (C7) forces, at every
cut \(i\):
\[M(A_i)\cap M(Z_i)=\emptyset,\qquad E_0(A_i)\cap E_2(Z_i)=\emptyset,
\qquad E_2(A_i)\cap E_0(Z_i)=\emptyset,\]
while W1-T5 forces \(M,E_2\) nonempty on both sides and \(E_0\)
nonempty modulo the localized escapes. These three disjointnesses are
the **only** interactions among the six forced membership classes;
every other forced-pair sum lies outside \(\mathbb P-2\) automatically.

*Proof.* Case check on \((\varepsilon_1,\varepsilon_2)\), using
\(2^p\equiv2^q\equiv0\pmod4\) and \(2^s-2\equiv2\pmod4\) for
\(p,q,s\ge2\):
\((0,0)\): \(2^p+2^q\equiv0\not\equiv2\pmod4\).
\((0,-1)\) and \((-1,-2)\): odd \(\ne\) even.
\((0,-2)\) and \((-1,-1)\): \(x+y=2^p+2^q-2=2^s-2\iff2^p+2^q=2^s
\iff p=q\), \(s=p+1\).
\((-2,-2)\): \(2^p+2^q=2^s+2\equiv2\pmod4\), impossible.
The corollary reads the two colliding patterns across the split
\((A_i,Z_i)\); disjointness is forced because a collision puts
\(2^{t+1}-2\in A_i+Z_i=S\). ∎

**Reading — the tension has exactly this much content.** "The
forbidden lengths must cancel across the chain" (`A019`'s reading of
W1-T14) is now quantified: the cancellation requirement on the *forced*
elements is three exponent-disjointness conditions and nothing more —
e.g. neighbouring near-intervals such as \(T_1\supseteq\{3,\dots,6\}\),
\(T_2\supseteq\{4,\dots,7\}\) satisfy all of them naturally (Mersenne
exponents 2 vs 3, power/\(\mathbb P-2\) crossings 2 vs 3). The residual
force of (C7) falls on the *unforced* bulk of the sets, which no
membership constraint controls. This is why the system does not
self-contradict at any chain length (confirmed at the realized level by
W1-T11's abstract solutions), and it sharpens `A019`'s category
diagnosis: even the set-sum channel carries only finitely much forced
arithmetic per cut. Any exclusion of the chain case must therefore
consume the *realizability* of through-sets (what `E020` measures) or
power-freeness structure beyond the through-set — not the memberships
alone.

---

### W1-T7 (both end blocks are non-bipartite; every prefix and suffix is) — proved [min]

**Claim.** In the chain case, \(L_1\) and \(L_m\) are non-bipartite;
more generally every prefix \(H_1^{(i)}\) and every suffix
\(H_2^{(i)}\) is non-bipartite.

*Proof.* \(A_i\) contains an even element (C1/C1′ if \(L_i\) is
non-bridge gives \(x\in\mathbb P-2\), even; if bridge, the redundancy
proof shows \(A_i\ni x+1\) with... — argue uniformly: by (C1) or (C1′),
\(A_i\) meets \(\mathbb P-2\) (even) or \(\mathbb P-1\) (odd); by (C2),
\(A_i\) contains an odd element (a Mersenne number, or \(1\)). If
\(A_i\) meets \(\mathbb P-2\) we have both parities directly. If
\(L_i\) is a bridge, apply (C1) at \(i-1\): \(A_{i-1}\) meets
\(\mathbb P-2\), and \(A_i=A_{i-1}+1\) contains the corresponding odd
element **and**, by (C2) at \(i-1\) (odd element of \(A_{i-1}\)), an
even element. Either way \(A_i\) contains both parities, so
\(A_i\) is not parity-constant. The prefix \((H_1^{(i)},a,c_i)\) is
vertex-taut (its blocks \(L_1,\dots,L_i\) are the blocks of a taut
chain; equivalently, the \(a\)-to-\(c_i\) segment of the taut
decomposition of any \(a\)–\(b\) path through a given vertex of the
prefix witnesses tautness). By `L035` T2 (parity structure theorem:
taut + parity-constant \(\iff\) bipartite, used in the contrapositive),
\(H_1^{(i)}\) is non-bipartite. For \(i=1\) this is \(L_1\); mirrors
give the suffixes and \(L_m\). ∎

**Reading.** `A019` W1-T13 proved \(H\) non-bipartite; in the chain
case the odd cycles are pinned into **both end blocks**
simultaneously, at [min] strength. (Middle blocks can still be
bipartite — a bipartite middle block shifts all path lengths by a
parity-constant set, which no constraint above forbids.)

---

### W1-T8 (block order bounds; the order dichotomy; the chain-length bound) — proved [min + `C027`/`C036` at tested strength]

**Claim.**

1. Every non-bridge block of the chain has order \(\ge16\); if both its
   terminals have block-degree exactly 2, order \(\ge17\).
2. \(|V(H)|\ge14k+m+1\ge14\lceil(m+1)/2\rceil+m+1\), hence
   \[n_0\ \ge\ 14\left\lceil\tfrac{m+1}2\right\rceil+m+2
   \qquad\text{and}\qquad m\ \le\ \frac{n_0-9}8 .\]
3. **(Order dichotomy.)** Either \(H\) is 2-connected, or
   \(n_0\ge32\); with \(m=3\), \(n_0\ge33\); with \(m\ge4\),
   \(n_0\ge48\). Contrapositive: for \(18\le n_0\le31\), the residual
   object's \(H\) **is 2-connected** — the chain case is empty below
   order 32.

*Proof.* (1) By W1-T1(4), a non-bridge block \(L\) is connected,
\(C_4\)-free, of minimum degree \(\ge2\ge1\), with at most two
sub-cubic vertices (its degree-2 vertices are among the two
terminals); its degree sum is \(\ge2+2+3(|V(L)|-2)=3|V(L)|-2
\ge3|V(L)|-4\), so it satisfies the edge bound of `C027`'s class
(`E010`: `geng -c -f -d1 n mine:0` with
\(\texttt{mine}=\lceil(3n-4)/2\rceil\) *implied by the degree
profile*, i.e. no additional restriction). \(L\) is power-free
(W1-T1(1)). `C027`: no power-free member of that class has order
\(\le15\). So \(|V(L)|\ge16\). If both terminals of \(L\) have
block-degree exactly 2, then \(L\) has exactly two degree-2 vertices
and all others \(\ge3\) — the profile of `C036`'s order-16 scan, which
found no power-free member; so \(|V(L)|\ge17\) in that case.

(2) Blocks intersect pairwise in at most one vertex and consecutively
in exactly one, along a path (W1-T1(1)), so
\(|V(H)|=\sum_i|V(L_i)|-(m-1)\). With \(k\) non-bridges of order
\(\ge16\) and \(m-k\) bridges of order 2:
\(|V(H)|\ge16k+2(m-k)-(m-1)=14k+m+1\). W1-T1(3) gives
\(k\ge\lceil(m+1)/2\rceil\). For the linear bound:
\(n_0-1=|V(H)|\ge14\cdot\frac{m+1}2+m+1=8m+8\).

(3) \(m=2\): \(k=2\), \(n_0\ge14\cdot2+2+2=32\). \(m=3\): \(k\ge2\),
\(n_0\ge28+3+2=33\). \(m\ge4\): \(k\ge3\),
\(n_0\ge42+m+2\ge48\). Every chain has \(m\ge2\), so a cut vertex
forces \(n_0\ge32\); `C036` gives \(n_0\ge18\) unconditionally, so in
the window \([18,31]\) only the 2-connected branch survives. ∎

**Conditionality.** The chain frame is (R)-framed as everything here;
the order inputs `C027`/`C036` are computational rows consumed at
"tested" strength with their recorded geng lineage. The dichotomy is
the leg's recorded falsifiable target delivered: "bound the block-chain
length \(m\), or prove \(H\) is 2-connected" — \(m\) is bounded
linearly in \(n_0\) (no absolute bound is available from memberships
alone, by W1-T6/W1-T11), and 2-connectivity is proved outright below
order 32.

**Remark (refinement not taken).** If additionally
\(\deg_{L_1}(c_1)=\deg_{L_2}(c_1)=2\) in an \(m=2\) chain, part 1's
second clause gives \(16+17\) or \(17+17\), i.e. \(n_0\ge34\); the
attachment degrees are not forced, so the clean statement stays
\(n_0\ge32\).

---

### W1-T9 (calibration: the known strict core fails the system) — proved; machine-verified (`E020` anchors A5–A8)

**Claim.** The `A014` T5 sharpness composite (two Petersen\(-e\) blocks
joined by a bridge; order 20; \(T_1=T_3=\{4,5,7,8\}\), \(T_2=\{1\}\);
\(S=\{9,\dots,17\}\)) violates the chain system at **seven** of its
rows: (C1) at both cuts (\(\{4,5,7,8\}\) avoids \(\mathbb P-2\)),
(C1′)-content at both cuts (\(\{5,6,8,9\}\) avoids \(\mathbb P-1\);
counted twice more as the coinciding (C2)-rows, whose \(\{1\}\)-escape
is vacuous since \(1\notin T+1\)), and (C7)
(\(14\in S\)). It satisfies (C8) (\(16,15\in S\)) and every (C3)-row.

*Proof.* Direct evaluation; machine-verified in `E020` (anchor A6 at
the set level, anchor A7 independently from the glued graph, anchor A8
for the Minkowski identities \(S=A_i+Z_i\) at both cuts). ∎

**Reading (lead (d) verified and sharpened).** The only strict
vertex-taut core the dossier possesses is excluded by the chain
system *five ways at the pre-registered level alone* — the
W1-T14-pattern constraints genuinely bite on known objects even with
power-freeness dropped. Note what fails is precisely the
\(\mathbb P-2\)/\(\mathbb P-1\) *memberships* (Petersen\(-e\)'s
through-set avoids the forbidden sets — the very property that made it
the 2-connected calibration object makes it an illegal chain block),
plus the total avoidance.

---

### W1-T10 (the chain floor at order 15; the `C037` 2-connectivity datum explained) — proved [structure] + computational (`E020`)

**Claim.**

1. The block class (2-connected, \(C_4\)-free, at most two degree-2
   vertices, all others \(\ge3\)) is empty at orders \(\le7\) and has
   exactly one member at order 8 (`E020`: geng streams
   `-c -f -d2 n` with the implied edge floor are empty for
   \(n=4,\dots,7\); the order-8 member is `GCpdag`, terminals its two
   degree-2 vertices, \(T=\{3,4,5,6,7\}\)). [computational]
2. Hence every **vertex-taut** member of the (5b) terminal profile
   class (connected, \(C_4\)-free, exactly two degree-2 vertices, rest
   \(\ge3\); power-freeness dropped) that has a cut vertex is a chain
   of \(m\ge2\) blocks of order \(\ge8\) and so has order
   \(\ge8+8-1=15\). [proved from W1-T1's frame, whose only inputs are
   tautness and the degree profile]
3. In that profile class at orders \(\le14\): a member has a cut vertex
   **iff** it is not vertex-taut. (Taut + cut needs order \(\ge15\) by
   2; conversely a non-taut connected (D)-gadget has a lobe (`L027`)
   whose attachment vertex \(c\) is a cut vertex: the lobe keeps all
   non-\(c\) edges internal, \(V(L)\setminus\{c\}\ne\emptyset\), and at
   least one terminal lies outside the lobe, so deleting \(c\)
   separates them.)
   This *predicts exactly* the `E018`/mod4 data: cut-vertex members
   number \(0/1/19/113\) at orders 10–13 — equal, order by order, to
   class minus taut (\(22-22\), \(125-124\), \(1139-1120\),
   \(10966-10853\)) — and `E020`'s order-14 run continues the pattern
   (all 129,654 2-connected exactly-two-degree-2 members taut).
   [proved + corroborated]

**Reading.** `C037` recorded that all sixty membership-triple witnesses
at orders 10–13 are 2-connected and inferred that a chain-case
calibration object "lives higher or must be built from pieces". Part 2
shows the observation is *forced by order alone* — chains in this class
cannot exist below 15 — so it carried no evidence about the chain
case's realizability. The kill test below is the first instrument that
actually probes it.

---

### W1-T11 (the kill test: refuted in range, mechanism identified, question open) — computational (`E020`), with the scope stated exactly

**Setup.** `E020` catalogued every block (with all admissible terminal
pairs and exact through-sets) at orders \(\le13\), and every
exactly-two-degree-2 block at order 14: 226,619 taut block/pair
instances; 166 distinct end-usable through-sets (a terminal of block
degree 2), 176 distinct mid-usable ones. It then searched all chains
of \(m\le3\) catalogued blocks — [end,end], [end,bridge,end],
[end,mid,end] — against the system, at three levels: **L1** = the
pre-registered kill system ((C1)/(C1′) pattern + (C7) + (C8) + the
structural frame), **L2** = plus (C2)/(C3) and mirrors, **L3** = plus
the saturation batteries (W1-T3(2)–(5), W1-T4 pattern at both
terminals).

**Result.** *Zero* candidates pass L1 (a fortiori L2/L3): all 9,045
unordered pairs of \(\mathbb P-2\)-meeting realized end through-sets
have \(14=2^4-2\) in their Minkowski sum — a single binding site (6 is
also hit in 6,710 pairs, 2 in 1,378, 30 in none: the maximum reachable
sum is \(13+13=26<30\)); the (C8) memberships never engage. The
realized through-sets are fat near-intervals reaching \(\max T=n-1\)
(the sole order-14 set meeting \(\mathbb P-2\) while avoiding both 7
and 8 is \(\{1,5,6,9,10,11,12,13\}\), and its 1 pairs with its
13 into 14).

**Verdict on the pre-registered kill condition: it did not fire**, and
in the searched range it is *refuted*: no vertex-taut \(C_4\)-free
two-degree-2 chain witness with \(m\le3\) blocks exists over blocks of
order \(\le13\) (any profile) plus order-14 exactly-two-degree-2
blocks. Scope holes, stated exactly: order-14 blocks with \(\le1\)
degree-2 vertex; all blocks of order \(\ge15\); chains with \(m\ge4\)
blocks (minimum order 29; no realized sub-pattern seeds them, but that
is not an emptiness proof).

**The question stays open above the range — with a named target.** The
safe zone \([15,29]\) between consecutive forbidden sums has width 15,
and machine-verified set arithmetic (`E020`) shows the system is
satisfiable just past the catalogue: \(T_1=\{7,8,12,13,14\}\) (block
order \(\ge15\)) with \(T_2=\{8,11,12,13,14,15\}\) (order \(\ge16\))
passes L1 **and** L2 abstractly, with exactly the W1-T6
exponent-dodging pattern (Mersenne exponents 3 vs 4, crossings 3 vs 4);
\(T=\{6,9,10,11,12,13\}\) against itself passes L1. Whether such
gapped through-sets are *realized* by taut \(C_4\)-free blocks at
orders 15–16 is precisely the next falsifiable rung (PyPy-scale, not
run here). Note where the frontier sits: the first arithmetic solutions
appear at exactly the block orders (\(\ge16\)) where the real residual
object's blocks live (W1-T8) — the toy range's obstruction (the
14-window) says nothing about the real range, whose safe zones widen
exponentially.

---

### W1-T12 (what the leg establishes about the real object) — reading, proved parts as cited

Under (R), for the case-(5b) residual object:

1. **The chain branch is dead below order 32** (W1-T8): any tight
   1-atom of order \(\le31\) in case (5b) has \(H\) 2-connected. All
   search legs through the current frontier (`E018` at 16; the `G014`
   item-6 generator from 17 up) therefore need no chain-case handling
   for a long way — and if the generator route reaches its targets
   order by order, the chain case stays empty forever below 32.
2. If the chain branch is ever alive (\(n_0\ge32\)), it is *more*
   constrained than the 2-connected branch: every prefix/suffix meets
   all three forbidden-set families ([min], W1-T5), both end blocks are
   non-bipartite ([min], W1-T7), every non-bridge block is a power-free
   vertex-taut 2-connected core of order \(\ge16\) that is
   Mersenne-saturated at its attachments (W1-T3(2)), and the
   \(\mathbb P-2\)-elements of the sides must dodge each other only in
   the three exponent patterns of W1-T6.
3. The arithmetic memberships alone cannot close the branch (W1-T6's
   freeness + W1-T11's abstract solutions); closure must come from
   realizability (through-set structure of power-free blocks — the
   `E020` successor at 15–16 probes its toy version) or from
   \(C_8\)-interference structure, consistent with `C037`'s diagnosis
   for the 2-connected branch.
4. Independently of the chain case, **W1-T4 is new forced structure on
   every residual object** and joins `L042`'s filter stack for future
   scans (checkable at generation time: for each terminal, every
   non-neighbour at distance \(\ge3\) needs a power-of-two path
   length).

## Failure analysis

No deduction failed; the leg's two targets were both reached (the
dichotomy theorem and a verdict on the kill test in its feasible
range). What did *not* materialize, and why, recorded to prevent
re-spending:

- **An absolute bound on \(m\)** (independent of \(n_0\)): impossible
  from the membership system alone — W1-T6 shows the per-cut forced
  content is three finite disjointness conditions, which long chains
  satisfy with room to spare (W1-T11's abstract families extend to any
  \(m\) by inserting bridges/middles with shifted intervals). The
  honest bound is the linear one, \(m\le(n_0-9)/8\).
- **A chain-case exclusion by pure arithmetic**: blocked in principle
  by the same freeness; blocked in the searched range only by
  realizability (the 14-window), which is order-local and evaporates
  at block orders \(\ge15\).
- The pre-registered kill **did not fire** — the opposite outcome from
  `A021`'s congruence hunt (whose kill fired at the first possible
  order). The asymmetry is informative: residue structure was already
  realizable at order 10, but *chain* structure compatible with the
  forced memberships is obstructed at least through the order-14
  block catalogue; the chain case is the harder side of (5b) for a
  counterexample to inhabit.

## Salvageable results

In expected order of reuse:

1. **W1-T8 (order dichotomy)** — "2-connected or \(n_0\ge32\)", with
   the per-block \(\ge16\)/\(\ge17\) bounds and \(m\le(n_0-9)/8\). The
   leg's headline; ledger-ready ((R)-conditional, `C027`/`C036`
   lineage).
2. **W1-T4 (terminal power saturation)** — new [min] structure on
   *every* residual object; a generation-time filter; must pass an
   A6-style genericity test before any promotion beyond filter status.
3. **W1-T5 + W1-T3 (the full closure battery)** — the chain case's
   constraint stack, all [min]; W1-T3(2) (cut-vertex Mersenne
   saturation) and the \(d\ge3\) total-saturation batteries are the
   reusable general pattern: *prefixes hide the second terminal, so
   every closure lands tight-1-atom-shaped*.
4. **W1-T6 (collision table)** — the cancellation tension quantified
   once and for all; also the formal reason no congruence-free
   arithmetic exclusion exists. Any future "chain-cancellation"
   proposal must name which unforced structure it consumes.
5. **W1-T11's frontier** — the kill question's exact state: refuted
   through the 13/14 catalogue for \(m\le3\); first abstract solutions
   at block orders 15–16 (\(\{7,8,12,13,14\}\)-family); named rung for
   the successor experiment.
6. **W1-T10** — the chain floor 15 and the cut\(\iff\)non-taut
   coincidence at \(\le14\); retro-explains the `C037` 2-connectivity
   datum (it carried no chain-case evidence).
7. **W1-T7 (end blocks non-bipartite)** and **W1-T9 (the composite
   fails seven rows)** — structure and calibration for any future
   chain-case work.
8. The **fan remark** (2-connected \(\Rightarrow\) taut, corroborated
   on 226,619 instances) — makes tautness free for 2-connected
   generation; external classical fact, kept out of the load-bearing
   chain.

**Warnings.**

- Everything in the chain frame is (R)-framed via `L041`; the [min]
  labels record the engine inside that frame, not freedom from (R).
  Do not quote W1-T8's dichotomy without its (R) conditionality and
  the `C027`/`C036` computational lineage.
- W1-T11's negative result is scoped to its catalogue (block orders
  \(\le13\) full, 14 two-degree-2-only, \(m\le3\)); it is not an
  emptiness theorem for the kill object.
- The saturation lemmas (W1-T3(2)–(5), W1-T4) are filters, not levers,
  until a genericity kill test says otherwise — the `E016` A6
  precedent applies to them squarely.

## Exit state

- Status: closed. Both targets delivered: the recorded falsifiable
  target ("bound the block-chain length m, or prove H is 2-connected")
  is met as W1-T8's dichotomy + linear bound; the pre-registered kill
  condition was run to a verdict in its feasible range (refuted there;
  open above, with a named next rung).
- Promoted records offered to the orchestrator (IDs are the
  orchestrator's): W1-T1 (chain frame incl. \(ab\notin E\) and the
  gateway lemma), W1-T3, W1-T4, W1-T5, W1-T6, W1-T7, W1-T8, W1-T10;
  experiment `E020`; W1-T9/W1-T11 as computational rows citing `E020`.
- Recommended next actions for this branch, falsifiable form:
  1. *(kill rung)* Catalogue (2,2)-profile blocks at order 15 under
     PyPy (`E020` machinery unchanged; the stream is the order-15
     analogue of `E018`'s calibrate) and test whether any realized
     through-set is \(\{7,8,12,13,14\}\)-shaped (equivalently: meets
     \(\mathbb P-2\), avoids \(\{1,\dots,6\}\cup\{9,10,11\}\)-enough to
     pair); a hit likely completes the chain-case Petersen\(-e\) at
     order \(\sim29\), killing arithmetic-only exclusion outright; a
     miss extends W1-T11's refutation range.
  2. *(proof rung)* The 2-connected branch is now the whole case-(5b)
     frontier below \(n_0=32\); the live levers there remain the
     \(C_8\)-interference structure (`C037`'s diagnosis) and the
     search ladder — this leg adds W1-T4 to the filter stack for the
     `G014` item-6 generator at order 17+.
  3. *(deferred)* \(m\ge4\) set-level search; order-14 one-degree-2
     blocks; the A6-style genericity measurement for W1-T4 —
     prerequisite to ever promoting saturation beyond filter status.
