# A008 — Cyclic voltage lifts against the power spectrum

- Date opened: 2026-07-23
- Problem: `P-002`
- Status: active
- Portfolio role: falsification-side tool-building (the internal attempt
  opened under the `O009` rule; selected by the S008 amendment and the
  S009 strategy audit)

## Intended mechanism

Bensmail's confinement graphs (`C017`) dodge sparse power sets by keeping
the whole cycle spectrum a fixed finite set, at the price of cut vertices,
which `L001`/`L011` make useless against the conjecture. The missing tool
is *spectrum control under 2-connectivity*. Voltage lifts are the standard
machine for building large graphs whose cycle structure is governed by a
small quotient: take a small base multigraph \(B\) of minimum degree at
least \(3\), assign each edge a voltage in \(\mathbb{Z}_m\), and pass to
the derived graph on \(V(B)\times\mathbb{Z}_m\). The derived graph keeps
minimum degree, grows linearly in \(m\), and — this is the leverage —
**every cycle upstairs projects to a closed walk downstairs of the same
length with net voltage zero** (Lemma L019 below). Power-of-two freeness
of an order-\(nm\) graph therefore reduces to finitely many linear
conditions "\(\nu\cdot x\not\equiv 0 \pmod m\)" indexed by the base's
tailless non-backtracking closed walks of length \(4,8,16,\dots\le nm\).
The infinite-looking target becomes an exact finite sieve over the voltage
space \((\mathbb{Z}_m)^{\mu}\), \(\mu\) the cycle rank of \(B\), and every
sieve survivor is *guaranteed* power-cycle-free — a counterexample to
`C001` if it is simple with minimum degree \(\ge3\). Verdicts are
machine-checkable instantly against the validated `E004`/`E005` detectors.

Distinctive against the live alternatives: this is the only route on the
board where the object sought is produced by a parametrized algebraic
family with exact, cheap certificates, rather than found by census
(capped) or forced by an unavailable interval lemma (proof side).

## Entry assumptions

Only `D001`–`D004` and standard finite group/graph conventions. Nothing
here assumes the negation of `C001`; the attempt tries to *construct* a
witness for the negation. No unproved external result is used. (Prior-art
caveat recorded: lifts of the theta and dumbbell bases are known families
— cyclic Haar graphs, I-graphs/generalized Petersen graphs — so any
surviving object must be literature-checked before a novelty claim; the
S007 sweep found no lift-based construction in the EGC literature.)

## Targeted obligations

- The negation of `C001` directly (a survivor of the full sieve is a
  counterexample).
- `G012` (opened this session): prove the cyclic-lift obstruction or
  exhibit a surviving lift; either outcome closes the question whether
  this tool can decide the conjecture's falsification side.
- Failure data feeds `G007`: the walk classes that kill every assignment
  are precisely the forcing patterns a proof-side interval lemma should
  formalize.

## Definitions

A *base* is a finite connected multigraph \(B\) (loops and parallel edges
allowed) with \(\delta(B)\ge3\), a loop adding \(2\) to its vertex's
degree. Each non-loop edge yields two mutually reverse *arcs* \(u\to v\),
\(v\to u\); each loop at \(u\) yields two mutually reverse arcs \(u\to
u\). Reversal \(a\mapsto\bar a\) is a fixed-point-free involution. A
*voltage assignment* over \(\mathbb{Z}_m\) is \(\alpha\) on arcs with
\(\alpha(\bar a)=-\alpha(a)\). The *derived graph* \(B^\alpha\) has vertex
set \(V(B)\times\mathbb{Z}_m\) and, for each edge \(e\) with chosen arc
\(a:u\to v\), the edges \(\{(u,g),(v,g+\alpha(a))\}\) for all
\(g\in\mathbb{Z}_m\) (independent of the arc choice).

A *walk* of length \(L\) is an arc sequence \(a_1\cdots a_L\) with
\(\mathrm{head}(a_i)=\mathrm{tail}(a_{i+1})\); *closed* if
\(\mathrm{head}(a_L)=\mathrm{tail}(a_1)\); *non-backtracking* (nb) if
\(a_{i+1}\ne\bar a_i\) for \(i<L\); *tailless* if moreover \(a_1\ne\bar
a_L\). Its *net voltage* is \(\sum_i\alpha(a_i)\).

**Simplicity conditions.** \(B^\alpha\) is a simple graph iff (i) every
loop arc \(a\) has \(\alpha(a)\ne0\) and \(2\alpha(a)\ne0\); (ii) parallel
arcs \(a\ne a'\) with the same tail and head have
\(\alpha(a)\ne\alpha(a')\). (Loops upstairs come exactly from
\(\alpha(a)=0\) on a loop; parallel edges upstairs come exactly from a
loop with \(2\alpha(a)=0\) or from parallel base edges with equal
voltages.) Under (i)–(ii), \(\deg_{B^\alpha}(u,g)=\deg_B(u)\), so
\(\delta(B^\alpha)=\delta(B)\ge3\).

## Deductions

**L019 (projection lemma; proved by hand below).** Let \(\alpha\) be a
\(\mathbb{Z}_m\)-voltage assignment on a base \(B\) satisfying the
simplicity conditions, and let \(L\ge3\). If \(B^\alpha\) contains a cycle
of length \(L\), then \(B\) contains a tailless non-backtracking closed
walk of length \(L\) with net voltage \(\equiv0\pmod m\).

*Proof.* Let \((x_0,\dots,x_{L-1})\) be a cycle in \(B^\alpha\), indices
mod \(L\), with \(x_i=(u_i,g_i)\). Fix \(i\). The edge \(\{x_i,x_{i+1}\}\)
is the lift of a unique base edge \(e_i\): lifts of distinct base edges
coincide only if the base edges are parallel with equal voltages, which
(ii) excludes. Choose the arc \(a_i\) of \(e_i\) as follows. If \(e_i\) is
a non-loop with chosen arc \(a:u\to v\) and lift edges
\(\{(u,g),(v,g+\alpha(a))\}\): if \(u_i=u\) put \(a_i=a\), giving
\(g_{i+1}=g_i+\alpha(a_i)\); if \(u_i=v\) put \(a_i=\bar a\), giving
\(g_{i+1}=g_i-\alpha(a)=g_i+\alpha(a_i)\). If \(e_i\) is a loop at \(u\)
with arc \(a\), its lifts are \(\{(u,g),(u,g+\alpha(a))\}\); according as
\(g_{i+1}=g_i+\alpha(a)\) or \(g_i=g_{i+1}+\alpha(a)\), put \(a_i=a\) or
\(a_i=\bar a\); in all cases
\[
  \mathrm{tail}(a_i)=u_i,\quad \mathrm{head}(a_i)=u_{i+1},\quad
  g_{i+1}=g_i+\alpha(a_i).
\]
Then \(W=a_0a_1\cdots a_{L-1}\) is a closed walk in \(B\) of length \(L\),
and its net voltage telescopes: \(\sum_i\alpha(a_i)=\sum_i(g_{i+1}-g_i)
= 0\) in \(\mathbb{Z}_m\).

Non-backtracking and taillessness are the single claim
\(a_{i+1}\ne\bar a_i\) for all \(i\) mod \(L\). Suppose \(a_{i+1}=\bar
a_i\); then \(e_{i+1}=e_i=:e\), and the cycle edges \(\{x_i,x_{i+1}\}\ne
\{x_{i+1},x_{i+2}\}\) (consecutive edges of a cycle of length \(\ge3\) are
distinct) are both lifts of \(e\) at \(x_{i+1}\). If \(e=uv\) is a
non-loop, exactly one lift of \(e\) is incident to any fixed vertex of the
fibre of \(u\) or \(v\) — contradiction. If \(e\) is a loop at \(u\) with
arc voltage \(\alpha(a)=c\), the lifts of \(e\) at \(x_{i+1}=(u,h)\) are
\(\{(u,h),(u,h+c)\}\) and \(\{(u,h-c),(u,h)\}\), so
\(\{x_i,x_{i+2}\}=\{(u,h-c),(u,h+c)\}\) with \(x_i\ne x_{i+2}\) (using
\(2c\ne0\), condition (i)). Reading the two steps: from
\(x_i=(u,h\mp c)\) to \(x_{i+1}=(u,h)\) to \(x_{i+2}=(u,h\pm c)\), both
steps traverse the loop in the *same* group direction \(\pm c\), so
\(a_{i+1}=a_i\). But \(a_{i+1}=\bar a_i\) then forces \(a_i=\bar a_i\),
impossible for a fixed-point-free involution. ∎

**Contrapositive (sieve soundness).** If for some \(L\) no tailless nb
closed walk of length \(L\) in \(B\) has net voltage \(\equiv0\pmod m\),
then \(B^\alpha\) has no \(L\)-cycle. If this holds for every
\(L\in\{2^k:k\ge2,\ 2^k\le m\,|V(B)|\}\), then \(B^\alpha\) is a simple
graph of minimum degree \(\ge3\) with no power-of-two cycle — a
counterexample to `C001`. The sieve is thus *sound* for constructing
counterexamples; it is merely not complete (a voltage-zero walk need not
lift to a cycle, so a sieve hit does not prove a power cycle exists).

**L020 (gauge reduction; proved by hand below).** If
\(\beta(a)=\alpha(a)+f(\mathrm{head}(a))-f(\mathrm{tail}(a))\) for some
\(f:V(B)\to\mathbb{Z}_m\), then \(B^\alpha\cong B^\beta\). Consequently,
for connected \(B\) every assignment is equivalent to one vanishing on a
fixed spanning tree \(T\), and the search space is
\((\mathbb{Z}_m)^{\mu}\) on the non-tree edges, \(\mu=|E|-|V|+1\).
Moreover the net voltage of any closed walk is then \(\nu\cdot x\), where
\(x\in(\mathbb{Z}_m)^\mu\) lists the non-tree voltages and
\(\nu\in\mathbb{Z}^{\mu}\) is the walk's vector of signed non-tree
traversal counts.

*Proof.* The map \((u,g)\mapsto(u,g+f(u))\) sends the \(\alpha\)-lift edge
\(\{(u,g),(v,g+\alpha(a))\}\) (arc \(a:u\to v\)) to
\(\{(u,g+f(u)),(v,g+\alpha(a)+f(v))\}\), and the \(\beta\)-lift edge at
\((u,g+f(u))\) along \(a\) ends at
\((v,g+f(u)+\beta(a))=(v,g+\alpha(a)+f(v))\); so the map is an
isomorphism. For the tree gauge take \(f(v)=-\)(\(\alpha\)-sum along the
\(T\)-path from a root to \(v\)); every tree arc then carries \(\beta=0\).
The closed-walk formula is immediate since tree arcs contribute \(0\) and
the non-tree arc for coordinate \(i\) contributes \(\pm x_i\) per signed
traversal. ∎

**Scaling symmetry (recorded, used only for reporting).** For a unit \(c\)
of \(\mathbb{Z}_m\), \((u,g)\mapsto(u,cg)\) is an isomorphism
\(B^{\alpha}\to B^{c\alpha}\); assignments \(x\) and \(cx\) give
isomorphic lifts.

**Walk classes are base-intrinsic.** In tree gauge, let
\(V_L(B)\subset\mathbb{Z}^\mu\) be the set of vectors \(\nu\) of tailless
nb closed walks of length exactly \(L\). \(V_L(B)\) is finite
(\(\lVert\nu\rVert_1\le L\)), independent of \(m\) and \(x\), and
computable by exact dynamic programming over states (arc, partial
vector). The sieve then reads: **assignment \(x\) over \(\mathbb{Z}_m\)
is certified free of \(L\)-cycles iff no \(\nu\in V_L(B)\) has
\(\nu\cdot x\equiv0\pmod m\).** Simplicity folds in uniformly: the
tailless nb closed walks of lengths \(1\) and \(2\) are exactly the loop
and parallel-edge patterns, so including \(L\in\{1,2\}\) in the sieve
enforces conditions (i)–(ii). (Walks of length \(1\) or \(2\) exist only
at loops and parallel edges; a tailless nb closed walk cannot live in the
spanning tree, so every such walk meets a non-tree edge and every
\(\nu\in V_L\) with \(L\in\{1,2\}\) is nonzero.)

**Counting-wall expectation (provisional, labeled intuition).** Tailless
nb closed walks of length \(L\) number \(\sim\Lambda^L\) with
\(\Lambda\ge\delta-1=2\), while distinct vectors number at most
\(O(L^\mu)\); a random-hyperplane heuristic then predicts that for
\(\mu=2\) all assignments die once some power \(2^k\gtrsim\sqrt{m}\) must
be dodged, i.e., cyclic lifts of \(\mu=2\) bases should fail for large
\(m\) unless \(V_{2^k}(B)\) is *structured* (confined to sublattices or
short vectors). The attempt's live hope is exactly that structure; the
kill condition is its absence. This paragraph is intuition, not a claim.

**L021 (abelian commutator obstruction; proved by hand below).** Let
\(B\) be a multigraph, \(u\) a vertex, and \(W_1,W_2\) non-backtracking
closed walks at \(u\) (lengths \(\ge1\); taillessness of the \(W_i\)
themselves is not required) satisfying the four arc conditions

1. \(\mathrm{first}(W_2)\ne\overline{\mathrm{last}(W_1)}\);
2. \(\mathrm{last}(W_2)\ne\mathrm{last}(W_1)\);
3. \(\overline{\mathrm{last}(W_2)}\ne\mathrm{first}(W_1)\);
4. \(\mathrm{first}(W_2)\ne\mathrm{first}(W_1)\).

Then the commutator concatenation \(W_1W_2\overline{W_1}\,\overline{W_2}\)
is a tailless non-backtracking closed walk at \(u\) of length
\(2(|W_1|+|W_2|)\) whose net voltage vanishes under **every** abelian
voltage assignment on \(B\); equivalently its cycle-space vector is zero.

*Proof.* Each factor is closed at \(u\), so the concatenation is a closed
walk of the stated length. The reverse of a non-backtracking walk is
non-backtracking (apply \(\bar{\cdot}\) to \(a_{i+1}\ne\bar a_i\)), so
all four factors are internally non-backtracking. Four junctions remain;
writing the condition "successor \(\ne\) reverse of predecessor":
at \(W_1|W_2\) it is exactly (1); at \(W_2|\overline{W_1}\) the successor
is \(\overline{\mathrm{last}(W_1)}\) and the condition is
\(\overline{\mathrm{last}(W_1)}\ne\overline{\mathrm{last}(W_2)}\), i.e.
(2); at \(\overline{W_1}|\overline{W_2}\) the predecessor is
\(\overline{\mathrm{first}(W_1)}\) and the successor
\(\overline{\mathrm{last}(W_2)}\), giving
\(\overline{\mathrm{last}(W_2)}\ne\mathrm{first}(W_1)\), i.e. (3); at the
wraparound \(\overline{W_2}|W_1\) the predecessor is
\(\overline{\mathrm{first}(W_2)}\) and the condition
\(\mathrm{first}(W_1)\ne\mathrm{first}(W_2)\), i.e. (4) — which is
precisely taillessness of the whole walk. Reversal negates each arc's
voltage, so the net voltage is
\(\alpha(W_1)+\alpha(W_2)-\alpha(W_1)-\alpha(W_2)=0\), an identity with
integer coefficients, hence the zero cycle-space vector. ∎

**Concrete corollaries (each cross-checked by the E007 dynamic program
and its reconstructed witness walks).** Write \(b\) for a bridge arc,
\(l_i\) for loop arcs, \(e_i^{\pm}\) for the parallel arcs of the theta
base, and \(u,a,b,v\) for the vertices of \(K_4\).

- **Dumbbell, length 8:** \(W_1=l_0\) (length 1),
  \(W_2=b\,l_1\,\bar b\) (length 3). Conditions (1)–(4) hold by
  inspection, so the dumbbell has a zero-vector walk of length
  \(2(1+3)=8\): no abelian voltage lift of the dumbbell of order \(\ge8\)
  — the entire I-graph/generalized-Petersen-type family — can be
  walk-certified \(C_8\)-free.
- **\(K_4\), length 16:** \(W_1=(u\to a,\ a\to b,\ b\to u)\) (a
  triangle), \(W_2=(u\to v,\ v\to a,\ a\to b,\ b\to v,\ v\to u)\)
  (length 5, not tailless — allowed). Conditions (1)–(4) hold, giving a
  zero-vector walk of length \(2(3+5)=16\).
- **theta3, length 16:** \(W_1=(e_1^+,e_0^-)\) (length 2),
  \(W_2=(e_2^+,e_0^-,e_1^+,e_2^-,e_1^+,e_2^-)\) (length 6). Conditions
  (1)–(4) hold, giving a zero-vector walk of length \(2(2+6)=16\).

**General expectation (provisional, labeled intuition, target of
`G012`).** Taking \(W_1\) a cycle of length \(\ell_1\) and
\(W_2=P\,C_2\,\bar P\) a cycle of length \(\ell_2\) conjugated through a
connecting walk of length \(d\), L021 produces zero-vector walks of
length \(2(\ell_1+\ell_2+2d)\); at minimum degree \(3\) the slot
conditions are generically satisfiable and \(d\) ranges over rich sets,
so these lengths should sweep arithmetic progressions that contain
powers of two for every base — an effective general obstruction lemma
("every abelian lift of every min-degree-3 base is certificate-dead
beyond an explicit order") looks provable and is the first target of
`G012`. Not claimed today; today's claims are the six explicit bases.

## Plan and decisive tests

1. Cheapest falsification: run the exact sieve on the \(\mu=2\) bases —
   theta (\(2\) vertices, \(3\) parallel edges; lifts are bipartite cubic
   Haar-type graphs) and dumbbell (two looped vertices joined by an edge;
   lifts are I-graphs/generalized-Petersen-type) — for all \(m\) up to
   the exact-DP horizon, powers up to \(128\). Zero survivors past
   trivially small orders on every \(\mu=2\) and \(\mu=3\) base is the
   kill datum for the cyclic-abelian version of the tool.
2. Pivot triggers (named before running, per S008): **(a)** a proved
   obstruction — e.g. the zero vector lies in \(V_{2^k}(B)\) for every
   admissible base at some \(2^k\) (kills all abelian voltages at once),
   or a proved covering statement for the hyperplane union at power
   lengths; **(b)** empirical loss of control — every tested \((B,m)\)
   dies at \(16\) or \(32\) with no sublattice structure in the vector
   sets to exploit. Either trigger ends the cyclic-abelian attempt and
   routes its failure pattern to the proof-side interval lemma; nonabelian
   voltage groups become the successor tool question.
3. Success trigger: any full-sieve survivor (automatically a
   counterexample candidate) — then immediately: independent detector
   verification, reproduction record, and the mandatory counterexample
   review path. A survivor with \(30\le N\le63\) would contradict `C013`
   (cubic case) or the reported bipartite bound, so any such finding is
   treated first as a probable bug.

## Failure analysis

**Kill condition (a) fired for the abelian version of the tool, in a
stronger and cleaner form than anticipated.** The proved obstruction is
not a covering statement about hyperplane unions but the abelianization
itself: by L021, commutator words are tailless non-backtracking closed
walks with zero net voltage over *every* abelian group, and they occur at
power-of-two lengths already on the smallest bases (length 8 on the
dumbbell, 16 on theta3/\(K_4\)/prism, 32 on \(K_{3,3}\), 4 on the
bouquet). The E007 computation made the verdict exhaustive:

- certificate level (`C020`): for all six bases — the complete list of
  cycle-rank-2 bases plus \(K_4\), \(K_{3,3}\), prism — and **every**
  \(m\ge2\), no \(\mathbb{Z}_m\) assignment can be walk-certified
  power-free (explicit sieve below each base's zero-vector threshold,
  the integer zero vector above it);
- truth level (`C021`): at every lift order in \([12,30]\), all
  assignments, both parities, every simple lift actually contains a
  \(C_4\), \(C_8\), or \(C_{16}\) — the cyclic-lift universe of these
  bases contains no counterexample through order 30.

The first invalid step of the route, in hindsight: cyclic groups were
chosen for the clean no-wrap correspondence, but cyclicity is
abelianness, and abelianness is exactly what converts the fundamental
group's commutators into voltage-invisible walks. The route's algebraic
leverage and its fatal obstruction are the same fact seen from two sides.

## Salvageable results

- L019 and L020 are permanent, group-agnostic tools (proved for
  \(\mathbb{Z}_m\); the proofs use only reversal-antisymmetry and so
  transfer to any voltage group with \(\alpha(\bar a)=\alpha(a)^{-1}\));
  the \(V_L\) walk-class DP and hyperplane sieve are reusable for
  successor group families (classes replaced by group elements).
- L021 identifies the obstruction structurally, which is what makes the
  successor precise: over a non-abelian voltage group the commutator
  word's net voltage is a genuine commutator \([g_1,g_2]\ne e\) in
  general, so the L021 kill vanishes at its root. The successor tool is
  the same sieve over small non-abelian groups (odd order kills wrapped
  power cycles by the same divisibility argument; smallest candidates
  \(\mathbb{Z}_7\rtimes\mathbb{Z}_3\) of order 21, the Heisenberg group
  of order 27), with walk classes valued in the group.
- The zero-vector length sets and the L021 length formula
  \(2(\ell_1+\ell_2+2d)\) are exactly the "forcing patterns" the
  proof-side interval lemma should formalize (`G007` input): they say
  *which* even lengths a min-degree-3 graph cannot help generating from
  two cycles and a connector.
- The E007 truth census doubles as an independent reproduction of the
  known small-order landscape (consistency with `L017`, `L018`, `C013`)
  and as a structured probe of the open window \([18,30]\).

## Exit state

- Status: closed (kill condition (a) fired for the cyclic/abelian
  version; the attempt's machinery and verdicts are recorded in `E007`)
- Promoted records: L019, L020, L021 to `CLAIMS.md` (hand proofs above);
  `C019`–`C021` (calibration, certificate verdict, truth census) to
  `CLAIMS.md` via `E007`; obligation `G012` opened for the successor
  question
- Next action: the successor tool decision is a fresh strategy choice,
  not this attempt's continuation — either the non-abelian sieve
  (falsification side, machinery ready) or the proof-side interval lemma
  fed by the L021 length formula; recorded as the session's proposed
  next step
