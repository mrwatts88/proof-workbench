# A010 — The collision-wall lemma: identity-voltage tailless walks at all power lengths past the log threshold

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: active
- Portfolio role: primary (inherited); closing theorem of the voltage-lift
  program (`G012`) and quantitative input to the proof-side route (`G007`)

## Intended mechanism

Prove the collision-wall lemma refined in `G012`: for every finite group
\(\Gamma\), every finite connected multigraph base \(B\) with
\(\delta(B)\ge3\), and every voltage assignment \(\alpha\), the base admits a
tailless non-backtracking closed walk of length exactly \(2^k\) with identity
net voltage, for every \(2^k\ge C\log_2\lvert\Gamma\rvert+C_B\) with \(C\)
absolute and \(C_B\) depending only on \(B\).

The mechanism inherited from `A009`: non-backtracking walks multiply like
\(2^L\) against only \(\lvert\Gamma\rvert\) voltage values, so same-voltage
walk pairs are forced at logarithmic length, and \(W\cdot\mathrm{rev}(W')\)
is an identity-voltage closed walk. The open part was the first/last-arc
diversity bookkeeping at the two junctions, plus exact length control (naive
pigeonhole pairs must be trimmed of common prefixes/suffixes, which destroys
the exact target length). The solution found here: trim the pigeonhole pair
once into a **seed pair** (distinct first arcs, shared last arc, equal
voltages), then **branch** the seed along two different continuations and
**steer** both branches to a common terminal vertex with two different final
arcs, using exact-length reachability in the arc digraph. A four-piece
assembly of the branched extensions then satisfies all four junction
conditions structurally, has exactly the target length, and its voltage
telescopes to the identity in any group.

## Entry assumptions

`D001`–`D004` for ambient conventions; standard finite group theory;
elementary graph theory. The lemma is about the base multigraph and is
independent of the truth of `C001`. All supporting lemmas below are proved
internally; no external theorem is imported.

## Targeted obligations

- `G012`: this attempt proves its statement (Theorem W7, Corollary W8).
- `G007` (indirectly): the proof-side reading at the end.

## Plan and decisive tests

1. Cheapest falsification: a value-confinement family — an assignment whose
   same-voltage walk pairs all share first or last arcs at some target
   length. The proof must rule this out structurally; while drafting, the
   candidate obstruction was checked against the dichotomy argument (a
   fiber whose pairs all share first or last arc is all-same-first or
   all-same-last), and the final construction avoids fibers entirely by
   steering. Residual test: `E009` runs the construction on adversarial
   assignments (all-distinct arc voltages, coset-structured, and the E008
   group tables) and fails loudly if any junction check is violated.
2. Pivot trigger: an unfixable gap in exact-length steering (Lemma W5) or
   in the junction verification; or `E009` producing a counterexample to
   any lemma. None fired.

## Deductions

All labeled deductions below are proved in this record and promoted as
`L023` (W2–W5) and `L024` (W7, W8).

### Conventions

\(B\) is a finite connected multigraph, loops and parallel edges allowed,
with \(n\) vertices and \(m\) edges. Each edge \(\{u,v\}\) carries two
**arcs** \((u\to v)\) and \((v\to u)\), mutual reverses \(a\mapsto\bar a\);
a loop at \(v\) carries two arcs at \(v\), mutual reverses. \(\deg(v)\) is
the number of arcs with tail \(v\) (a loop contributes \(2\)); minimum
degree \(\ge3\) means every vertex has at least three out-arcs,
equivalently at least three in-arcs (in-arcs are reverses of out-arcs).
The **transition** \(a\to b\) is legal iff
\(\mathrm{head}(a)=\mathrm{tail}(b)\) and \(b\ne\bar a\). A
**non-backtracking (nb) walk** of length \(L\) is a sequence of \(L\) arcs
with all \(L-1\) consecutive transitions legal. It is **closed** if
\(\mathrm{tail}(a_1)=\mathrm{head}(a_L)\) and **tailless** if in addition
the wrap transition \(a_L\to a_1\) is legal (\(a_1\ne\bar a_L\)). The
**arc digraph** \(\mathcal A(B)\) has the \(2m\) arcs as states and the
legal transitions as directed edges; an nb walk of length \(L\) is a walk
through \(L\) states of \(\mathcal A(B)\) (\(L-1\) transitions).

A voltage assignment is \(\alpha:\text{arcs}\to\Gamma\) with
\(\alpha(\bar a)=\alpha(a)^{-1}\). The net voltage of \(W=a_1\cdots a_L\)
is \(\omega(W)=\alpha(a_1)\cdots\alpha(a_L)\), and for the reversed walk
\(\mathrm{rev}(W)=\bar a_L\cdots\bar a_1\),
\[
\omega(\mathrm{rev}(W))
 =\alpha(a_L)^{-1}\cdots\alpha(a_1)^{-1}
 =\omega(W)^{-1}. \tag{R}
\]
The reverse of an nb walk is nb: legality of \(a\to b\) equals legality of
\(\bar b\to\bar a\), since both say \(\mathrm{head}(a)=\mathrm{tail}(b)\)
and \(b\ne\bar a\). Two nb walks concatenate to an nb walk provided the
single junction transition is legal; nb-ness is a local condition on
consecutive pairs.

### W1 (branching bound)

Every arc \(a\) has at least \(\deg(\mathrm{head}(a))-1\ge2\) legal
continuations: exactly one out-arc of \(\mathrm{head}(a)\), namely
\(\bar a\), is excluded. Hence for every arc \(a\) and every \(L\ge1\)
there are at least \(2^{L-1}\) distinct nb walks of length \(L\) with
first arc \(a\).

### W2 (no reverse-free forward-closed arc set)

Call an arc set \(C\) **continuation-closed** if \(a\in C\) implies every
legal continuation of \(a\) is in \(C\), and **reverse-free** if no edge
has both of its arcs in \(C\).

**Lemma W2.** If \(\delta(B)\ge3\), a nonempty continuation-closed arc set
is never reverse-free.

*Proof.* Suppose \(C\) is nonempty, continuation-closed, and reverse-free.
Let \(S\) be the set of heads of arcs of \(C\); \(S\ne\emptyset\). Write
\(\mathrm{out}_C(v)\), \(\mathrm{in}_C(v)\) for the numbers of \(C\)-arcs
with tail (resp. head) \(v\).

Fix \(v\in S\) and \(a\in C\) with head \(v\). The legal continuations of
\(a\) are all \(\deg(v)\) out-arcs of \(v\) except \(\bar a\), and all lie
in \(C\); hence \(\mathrm{out}_C(v)\ge\deg(v)-1\). Also
\(\mathrm{in}_C(v)\ge1\).

Reverse-freeness gives \(\mathrm{out}_C(v)+\mathrm{in}_C(v)\le\deg(v)\):
each non-loop edge at \(v\) has one arc-end at \(v\) and contributes at
most one arc to \(C\), hence at most \(1\) to the sum; each loop at \(v\)
has two arc-ends at \(v\) and contributes at most one of its two arcs to
\(C\), and that single arc contributes \(1\) to \(\mathrm{out}_C(v)\) and
\(1\) to \(\mathrm{in}_C(v)\), total \(2\), matching its two ends. Summing
arc-ends at \(v\) proves the bound.

Combining, \(1+(\deg(v)-1)\le\mathrm{in}_C(v)+\mathrm{out}_C(v)\le\deg(v)\),
so equality holds: \(\mathrm{in}_C(v)=1\) and
\(\mathrm{out}_C(v)=\deg(v)-1\) for every \(v\in S\).

Every arc of \(C\) has its head in \(S\), so
\(\lvert C\rvert=\sum_{v\in S}\mathrm{in}_C(v)=\lvert S\rvert\). The arcs
of \(C\) with tail in \(S\) number
\(\sum_{v\in S}\mathrm{out}_C(v)=\sum_{v\in S}(\deg(v)-1)\ge2\lvert
S\rvert\) using \(\deg\ge3\), and they are pairwise distinct arcs of
\(C\), so \(2\lvert S\rvert\le\lvert C\rvert=\lvert S\rvert\), forcing
\(S=\emptyset\): contradiction. \(\square\)

### W3 (strong connectivity of the arc digraph)

**Lemma W3.** If \(B\) is connected with \(\delta(B)\ge3\), then
\(\mathcal A(B)\) is strongly connected: for any arcs \(a,b\) there is an
nb walk with first arc \(a\) and last arc \(b\).

*Proof.* First, \(\mathcal A(B)\) is weakly connected. (a) For arcs
\(p\ne q\) out of a common vertex \(h\): among the \(\ge3\) in-arcs of
\(h\), choose \(c\) with \(\bar c\notin\{p,q\}\); then \(c\to p\) and
\(c\to q\) are both legal, giving the undirected path
\(p\leftarrow c\rightarrow q\) in \(\mathcal A(B)\). (b) For adjacent
vertices \(h,h'\) joined by an edge with arc \(y:h\to h'\): every arc out
of \(h\) is weakly connected to \(y\) by (a); every arc \(q'\) out of
\(h'\) with \(q'\ne\bar y\) receives the legal transition \(y\to q'\), and
\(q'=\bar y\) is weakly connected to the other out-arcs of \(h'\) by (a).
Every arc is an out-arc of its tail, and \(B\) is connected, so chaining
(a)–(b) along paths of \(B\) weakly connects all arcs.

The reversal map \(a\mapsto\bar a\) is an anti-automorphism of
\(\mathcal A(B)\): \(a\to b\) is legal iff \(\bar b\to\bar a\) is legal.
Hence it maps strongly connected components to strongly connected
components and reverses all condensation edges; in particular it maps sink
components to source components.

Let \(T\) be the arc set of a sink component of the (finite, nonempty)
condensation. No transition leaves \(T\), and every state has out-degree
\(\ge2\) (W1), so \(T\) is continuation-closed and nonempty. By W2, \(T\)
contains both arcs \(x,\bar x\) of some edge. Then \(\bar T:=\{\bar t:t\in
T\}\) is a source component, and \(x\in T\cap\bar T\), so \(T=\bar T\)
(components partition the arcs). Thus \(T\) is simultaneously a sink and a
source: an isolated node of the condensation. Weak connectivity forces the
condensation to be a single node, so \(T\) is everything and
\(\mathcal A(B)\) is strongly connected. \(\square\)

### W4 (period at most two)

Let \(p\) be the gcd of the lengths of all closed walks of
\(\mathcal A(B)\); a closed walk through \(L\) states (counting the
closing transition) is exactly a tailless nb closed walk of length \(L\)
in \(B\).

**Lemma W4.** If \(B\) is connected with \(\delta(B)\ge3\), then
\(p\in\{1,2\}\), and \(p=2\) exactly when \(B\) is bipartite. When
\(p=2\), the class of an arc under the canonical partition is the side of
its tail, and every transition advances the class by one.

*Proof.* If \(B\) has a loop with arc \(l\): the one-arc sequence \((l)\)
is closed and its wrap transition \(l\to l\) is legal (\(\bar l\ne l\)); a
tailless nb closed walk of length \(1\), so \(p=1\), and \(B\) is
non-bipartite. If \(B\) is loopless with parallel edges \(e\ne f\) joining
\(u,v\): the sequence \((e:u\to v,\ f:v\to u)\) is nb (distinct edges),
closed, and tailless, so \(p\mid2\). If \(B\) is simple: take a longest
path \(v_0v_1\cdots v_t\). All neighbors of \(v_0\) lie on the path
(maximality) and there are at least three: \(v_1,v_i,v_j\) with
\(1<i<j\le t\). The three cycles \(v_0v_1\cdots v_iv_0\),
\(v_0v_1\cdots v_jv_0\), \(v_0v_iv_{i+1}\cdots v_jv_0\) have lengths
\(i+1\), \(j+1\), \(j-i+2\); each cycle, traversed once, is a tailless nb
closed walk (consecutive arcs, and the wrap pair, use distinct edges).
Since \((i+1)+(j-i+2)-(j+1)=2\), any common divisor of the three lengths
divides \(2\), so \(p\mid2\).

If \(p=2\): every cycle is even and there are no loops, so \(B\) is
bipartite, and each transition moves the tail along one edge, switching
sides. If \(B\) is bipartite: every closed walk has even length, so \(p\)
is even, hence \(p=2\). If \(B\) is non-bipartite: an odd cycle is a
tailless nb closed walk of odd length, so \(p\) is odd, hence \(p=1\).
\(\square\)

### W5 (uniform exact-length reachability)

Fix the class function \(\chi\) on arcs: constant \(0\) if \(p=1\); the
side of the tail if \(p=2\).

**Lemma W5.** There is a finite constant \(R_B\) such that for all arcs
\(\sigma,\tau\) and every integer \(T\ge R_B\) with
\(T\equiv\chi(\tau)-\chi(\sigma)\pmod p\), there is an nb walk with first
arc \(\sigma\), last arc \(\tau\), and exactly \(T\) transitions (i.e.
\(T+1\) arcs).

*Proof.* Work in the finite strongly connected digraph \(\mathcal A(B)\)
(W3). Any two walk lengths \(\ell_1,\ell_2\) from \(\sigma\) to \(\tau\)
are congruent mod \(p\): append a return walk \(\tau\to\sigma\) of length
\(r\) (strong connectivity); \(p\) divides both closed lengths
\(\ell_i+r\). So length mod \(p\) is a well-defined function of the
ordered pair, additive along concatenation, and for \(p=2\) it agrees with
\(\chi(\tau)-\chi(\sigma)\) because each transition switches tail-sides
(W4).

Let \(S\) be the set of lengths of closed walks at a fixed state
\(\sigma_0\). \(S\) is closed under addition (concatenation), and
\(\gcd(S)=p\): for a closed walk of length \(\lambda\) at any state
\(\tau\), connect \(\sigma_0\to\tau\) (length \(r_1\)) and
\(\tau\to\sigma_0\) (length \(r_2\)); then \(r_1+r_2\in S\) and
\(r_1+\lambda+r_2\in S\), so \(\gcd(S)\mid\lambda\), and conversely \(p\)
divides every element of \(S\).

*Sub-lemma (numerical semigroup; proved inline, per R001 finding F1).*
A set \(S\) of positive integers closed under addition with
\(\gcd(S)=p\) contains every sufficiently large multiple of \(p\).
*Proof.* The gcd of an increasing chain of finite subsets of \(S\)
stabilizes, so finitely many elements \(g_1,\dots,g_k\in S\) already
have \(\gcd(g_1,\dots,g_k)=p\), and by Bézout there are integers
\(u_i\) with \(\sum_iu_ig_i=p\). Let \(P:=\sum_{u_i>0}u_ig_i\) and
\(N:=-\sum_{u_i<0}u_ig_i\), so \(P-N=p\), \(N\ge0\), and \(P=N+p>0\).
As nonnegative integer combinations of elements of \(S\), \(P\in S\)
and \(N\in S\cup\{0\}\). Since \(p\mid g_1\), write \(q:=g_1/p\). For
\(0\le b<q\) set
\[
x_b:=b\,P+(q-b)\,N=qN+bp\ \in\ S\cup\{0\},
\]
with \(x_b=0\) only when \(b=0\) and \(N=0\). The \(x_b\) are \(q\)
consecutive multiples of \(p\) starting at \(qN\), so they realize
every residue of a multiple of \(p\) modulo \(g_1=qp\). Given a
multiple \(\mu\) of \(p\) with \(\mu\ge qN+g_1\), choose
\(b:=\bigl((\mu-qN)/p\bigr)\bmod q\). Then \(\mu-x_b=p\cdot
\bigl((\mu-qN)/p-b\bigr)\) with the bracket a nonnegative multiple of
\(q\) (nonnegative because \(x_b\le qN+g_1-p<\mu\)), so
\(\mu=x_b+cg_1\) with \(c\ge0\), a nonnegative combination of elements
of \(S\) that is positive — hence \(\mu\in S\) (when \(x_b=0\),
\(\mu=cg_1\) with \(c\ge1\)). Take \(\Lambda:=qN+g_1\); then
\(S\supseteq\{\,\mu\equiv0\bmod p:\ \mu\ge\Lambda\,\}\). \(\dashv\)

Given \(\sigma,\tau\): fix walks \(\sigma\to\sigma_0\) of length \(d_1\)
and \(\sigma_0\to\tau\) of length \(d_2\). For every
\(T\ge d_1+d_2+\Lambda\) with \(T\equiv d_1+d_2\pmod p\) — and
\(d_1+d_2\equiv\chi(\tau)-\chi(\sigma)\pmod p\) — insert a closed walk of
length \(T-d_1-d_2\in S\) at \(\sigma_0\). Take
\(R_B:=\Lambda+\max_{\sigma,\tau}(d_1+d_2)\), a finite maximum over the
\((2m)^2\) ordered state pairs. \(\square\)

### W6 (seed pair)

Define
\[
\ell^*:=\lfloor\log_2(2m\lvert\Gamma\rvert)\rfloor+2,
\qquad\text{so}\qquad 2^{\ell^*-1}>2m\lvert\Gamma\rvert .
\]

**Lemma W6.** For every voltage assignment \(\alpha\) over any finite
group \(\Gamma\) there exist a vertex \(u_1\), an integer
\(\lambda_1\in[2,\ell^*-1]\), and nb walks \(W\ne W'\) of length
\(\lambda_1\), both from \(u_1\) to a common vertex \(w_1\), with
\[
\omega(W)=\omega(W'),\qquad
\mathrm{first}(W)\ne\mathrm{first}(W'),\qquad
\mathrm{last}(W)=\mathrm{last}(W')=:d .
\]

*Proof.* Fix any arc \(a\). By W1 there are at least
\(2^{\ell^*-1}>2m\lvert\Gamma\rvert\) distinct nb walks of length
\(\ell^*\) with first arc \(a\). The map
\(X\mapsto(\mathrm{last}(X),\omega(X))\) takes at most
\(2m\lvert\Gamma\rvert\) values, so two such walks \(X\ne X'\) share their
last arc and voltage (and the first arc \(a\)). Let \(P\) be their maximal
common prefix, of length \(\pi\); \(1\le\pi\le\ell^*-1\) since both start
with \(a\) and \(X\ne X'\). Write \(X=PW\), \(X'=PW'\),
\(\lambda_1:=\ell^*-\pi\). Then \(W\ne W'\) have distinct first arcs
(maximality of \(P\)), equal last arcs (\(=\mathrm{last}(X)\)), common
start \(u_1:=\mathrm{head}(\mathrm{last}(P))\), common end
\(w_1:=\mathrm{head}(\mathrm{last}(X))\), and
\(\omega(P)\,\omega(W)=\omega(X)=\omega(X')=\omega(P)\,\omega(W')\) gives
\(\omega(W)=\omega(W')\). If \(\lambda_1=1\), a walk of length one is its
own first and last arc, contradicting distinct firsts with equal lasts; so
\(\lambda_1\ge2\). \(\square\)

### W7 (main theorem: the collision wall)

**Theorem W7.** Let \(B\) be a finite connected multigraph with
\(\delta(B)\ge3\) and \(m\) edges, with period \(p\in\{1,2\}\) (W4) and
reach constant \(R_B\) (W5). Let \(\Gamma\) be a finite group and
\(\alpha\) any voltage assignment on \(B\). Then \(B\) has a tailless nb
closed walk of length exactly \(L\) with identity net voltage:

- for every \(L\equiv0\pmod4\) with \(L\ge4\ell^*+4R_B+8\); and
- if \(B\) is non-bipartite, for every even \(L\ge4\ell^*+4R_B+8\).

In particular, with \(C_B:=4\lceil\log_2 m\rceil+4R_B+24\): for every
integer \(k\) with
\(2^k\ge4\log_2\lvert\Gamma\rvert+C_B\), there is a tailless nb closed
walk of length exactly \(2^k\) with identity net voltage. The absolute
constant is \(C=4\).

*Proof.* Let \((W,W')\) be a seed pair from W6: common length
\(\lambda_1\in[2,\ell^*-1]\), from \(u_1\) to \(w_1\), equal voltages,
distinct first arcs, shared last arc \(d\).

**Branch.** \(w_1\) has \(\deg(w_1)\ge3\) out-arcs, of which only
\(\bar d\) is an illegal continuation of \(d\); choose two distinct legal
continuations \(x\ne x'\). (Per R001 finding F6: the distinctness
\(x\ne x'\) carries no load — no junction check below involves \(x\)
against \(x'\), and the construction is equally valid with \(x=x'\); two
branches are kept for exposition only.)

**Steer.** Choose any vertex \(z\) and two distinct in-arcs \(e\ne f\) of
\(z\) (at least three exist). If \(p=2\), then \(\chi(x)=\chi(x')\)
(common tail \(w_1\)) and \(\chi(e)=\chi(f)\) (their tails are neighbors
of \(z\), hence on one side), so the required residues
\(\tau:=\chi(e)-\chi(x)=\chi(f)-\chi(x')\pmod 2\) coincide. Given the
target \(L\), set
\[
N_0:=\tfrac{L}{2}-2\lambda_1-2 .
\]
If \(p=2\): \(L\equiv0\pmod4\) makes \(N_0\) even; choose
\(T_1\in\{R_B,R_B+1\}\) with \(T_1\equiv\tau\pmod2\) and
\(T_2:=N_0-T_1\equiv\tau\pmod2\); \(T_2\ge N_0-R_B-1\ge R_B\) holds when
\(N_0\ge2R_B+1\), which follows from \(L\ge4\ell^*+4R_B+8\) and
\(\lambda_1\le\ell^*-1\):
\(N_0=\tfrac L2-2\lambda_1-2\ge2\ell^*+2R_B+4-2(\ell^*-1)-2=2R_B+4\).
If \(p=1\): take \(T_1:=R_B\), \(T_2:=N_0-R_B\ge R_B\), needing only
\(N_0\ge2R_B\); any even \(L\ge4\ell^*+4R_B+8\) suffices (evenness of
\(L\) makes \(N_0\) an integer).

By W5 pick nb walks \(xA\) (first arc \(x\), last arc \(e\), \(T_1\)
transitions, hence length \(T_1+1\)) and \(x'B'\) (first arc \(x'\), last
arc \(f\), length \(T_2+1\)).

**Assemble.** Define
\[
U:=W\cdot xA,\quad U':=W'\cdot xA,\quad
Y:=W\cdot x'B',\quad Y':=W'\cdot x'B',
\]
all legal concatenations: \(W\) and \(W'\) both end with \(d\), and
\(x,x'\ne\bar d\). Lengths: \(t_1:=\lambda_1+T_1+1\) for \(U,U'\) and
\(t_2:=\lambda_1+T_2+1\) for \(Y,Y'\). Last arcs: \(e,e,f,f\)
respectively. Voltages:
\(\omega(U)=\omega(W)\,\omega(xA)=\omega(W')\,\omega(xA)=\omega(U')=:h_1\)
and likewise \(\omega(Y)=\omega(Y')=:h_2\).

Consider the closed walk based at \(u_1\):
\[
\Omega:=U\cdot\mathrm{rev}(Y)\cdot Y'\cdot\mathrm{rev}(U') .
\]

*Length.* \(\lvert\Omega\rvert=2(t_1+t_2)=4\lambda_1+2(T_1+T_2)+4
=4\lambda_1+2N_0+4=L\).

*Voltage.* By (R),
\(\omega(\Omega)=h_1h_2^{-1}h_2h_1^{-1}=\mathrm{id}\) — in any group; no
commutativity is used.

*Closure.* \(\Omega\) starts at \(\mathrm{tail}(\mathrm{first}(W))=u_1\)
and ends at
\(\mathrm{head}(\overline{\mathrm{first}(W')})
=\mathrm{tail}(\mathrm{first}(W'))=u_1\).

*Non-backtracking and taillessness.* Each of the four pieces is nb
(reverses of nb walks are nb), so only four junctions need checking:

1. \(U\mid\mathrm{rev}(Y)\): arcs \(e\) then
   \(\overline{\mathrm{last}(Y)}=\bar f\), both at \(z\); legal iff
   \(\bar f\ne\bar e\), i.e. \(e\ne f\). ✓
2. \(\mathrm{rev}(Y)\mid Y'\): arcs
   \(\overline{\mathrm{first}(Y)}=\overline{\mathrm{first}(W)}\) then
   \(\mathrm{first}(Y')=\mathrm{first}(W')\), both at \(u_1\); legal iff
   \(\mathrm{first}(W')\ne\mathrm{first}(W)\). ✓ (seed)
3. \(Y'\mid\mathrm{rev}(U')\): arcs \(f\) then
   \(\overline{\mathrm{last}(U')}=\bar e\), both at \(z\); legal iff
   \(\bar e\ne\bar f\). ✓
4. Wrap \(\mathrm{rev}(U')\mid U\): arcs
   \(\overline{\mathrm{first}(W')}\) then \(\mathrm{first}(W)\), both at
   \(u_1\); legal iff \(\mathrm{first}(W)\ne\mathrm{first}(W')\). ✓ (seed)

So \(\Omega\) is a tailless nb closed identity-voltage walk of length
exactly \(L\), based at \(u_1\).

*Threshold arithmetic.* \(\ell^*\le\log_2\lvert\Gamma\rvert+\log_2(2m)+2
\le\log_2\lvert\Gamma\rvert+\lceil\log_2m\rceil+3\), so
\(4\ell^*+4R_B+8\le4\log_2\lvert\Gamma\rvert+4\lceil\log_2m\rceil+4R_B+20
<4\log_2\lvert\Gamma\rvert+C_B\). A power \(2^k\) above the threshold
satisfies \(2^k\ge8\), hence \(2^k\equiv0\pmod4\), so the first bullet
applies. \(\square\)

**Remark (walks, not cycles).** \(\Omega\) traverses arcs repeatedly
(the seed region four times); it is a closed walk, exactly the object the
`L019` certificate quantifies over. Nothing here asserts a cycle of length
\(L\) in any lift.

**Remark (location).** The walk is based at the seed vertex \(u_1\), which
the construction does not control; `G012` requires no prescribed basepoint.

**Remark (constant).** The theorem is an upper bound on certificate
survival; the E008 deaths at length \(16\) for
\(\lvert\Gamma\rvert\in\{21,27,60\}\) are earlier than this threshold,
consistent with a proved constant \(C=4\) versus the heuristic \(2\),
traded for full generality and taillessness.

### W8 (corollary: the certificate program closes, effectively)

For every base \(B\) (connected, \(\delta\ge3\), \(n\) vertices) there is
\(\Gamma_0(B)\) such that for every finite group with
\(\lvert\Gamma\rvert\ge\Gamma_0(B)\) and every assignment, the walk
certificate of power-of-two-freeness — `L019` in its group-agnostic form,
proved in `A009` and cited at that strength by `C022` (R001 finding
F2) — fails at some power length \(2^k\le n\lvert\Gamma\rvert\): it
suffices that
\([\,4\log_2\lvert\Gamma\rvert+C_B,\ n\lvert\Gamma\rvert\,]\) contain a
power of two, which holds for all large \(\lvert\Gamma\rvert\) because a
power of two lies in \([x,2x)\) for every \(x\ge1\) and the interval's
ratio grows without bound.

Scope (per R001 finding F3): this closes the certificate route
**per base**, for every \(\Gamma\) with
\(\lvert\Gamma\rvert\ge\Gamma_0(B)\); together with the exhaustive
finite verdicts `C020` (all \(\mathbb Z_m\), six bases) and `C022`
(orders 21, 27, 60, four bases), it is the closing theorem `G012` asked
for. It is **not** a blanket claim over all \((B,\Gamma)\)
simultaneously: for a small fixed group on a base with large \(R_B\)
(e.g. \(\mathbb Z_2\) on a long chain of triple-edge blocks, where
\(R_B\) grows with the diameter), the certificate window
\([\,4\log_2\lvert\Gamma\rvert+C_B,\ n\lvert\Gamma\rvert\,]\) can be
empty and W7 says nothing about those certificates; in the abelian case
`L021` still applies there, but that is a separate mechanism and is not
invoked here.

### Proof-side reading (input to `G007`)

Applied with any \(\Gamma\) (including the trivial group), W7 says: a
connected multigraph of minimum degree \(\ge3\) has tailless nb closed
walks of **every** length \(\equiv0\bmod4\) (every even length if
non-bipartite) past a constant threshold, and these walks can be forced to
be voltage-balanced in any prescribed finite quotient at only logarithmic
cost in the threshold. The conjecture's hard core, seen from here, is
walk-to-cycle: which forced balanced round trips can be realized with
distinct vertices. Recorded as raw material for the interval-forcing
route, not as progress on `C001` itself.

## Failure analysis

Not applicable — the attempt succeeded. Two dead ends met while drafting
are worth recording: (i) pigeonhole at the target length with trimming
gives identity walks of *uncontrolled* shorter even length, and no
fiber-degeneracy dichotomy was needed once steering replaced fibers;
(ii) pumping one short identity walk through powers gives only multiples
of its length, and combining two incommensurable identity walks runs into
Frobenius bounds of size \(\Theta(\lvert\Gamma\rvert\log\lvert\Gamma\rvert)\)
— both approaches cannot reach exact powers at logarithmic thresholds.

## Salvageable results

- `L023`: the arc-digraph structure package (W2, W3, W4, W5) — reusable
  for any future nb-walk argument on min-degree-3 bases, independent of
  voltages.
- `L024`: the collision-wall theorem (W7) with corollary W8.
- The even-length interval reading for `G007` (above).

## Exit state

- Status: closed (theorem proved; mechanical verification `E009` passed;
  delegated logic audit `R001` returned pass with three minor findings,
  all repaired in place — see session `S010`)
- Promoted records: `L023`, `L024` to `CLAIMS.md` (scoped per R001
  F2/F3); `G012` resolved with the mod-4 caveat of R001 F4
- Next action: fold W7 into the publishable note; the proof-side
  interval route inherits the walk-interval reading as its quantitative
  input
