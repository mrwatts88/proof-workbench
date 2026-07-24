# A020 — Beyond 4/7: the subdivision descent and the density of cubic vertices in a minimal counterexample

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: complete for its stated scope
- Session: `S019` (worker W2)
- Portfolio role: primary (route `R2` of `G015`)

## Intended mechanism

`G015` route `R2` asks whether Carr's density bound `C006` — at least \(4/7\) of
the vertices of an order-then-size minimal counterexample have degree exactly
\(3\) — can be pushed to \(1\), which is exactly the cubic reduction.

The line-by-line audit of the source (`references/carr-2026-verification-2026-07-24.md`,
this session, all four results verified) exposes the opening. Carr's Theorem 0.1
uses Corollary 0.1(**2**) — the degree-\(\ge4\) vertices are independent
(internally `L002`) — and nothing else. It does **not** use Corollary 0.1(**1**)
= `C005`, that every vertex has a neighbour of degree exactly \(3\). And the
equality case \(4|V_{\ge4}|=3|V_3|\) demands that every degree-\(3\) vertex send
all three of its edges into \(V_{\ge4}\), which `C005` forbids outright. So the
\(4/7\) bound is not even attainable, and the two corollaries have never been
used together.

Two mechanisms are tried here:

1. **Use `C005` in the count.** `C005` plus the degree partition says the
   degree-\(3\) vertices induce a subgraph with no isolated vertex; that alone
   converts \(4/7\) into \(2/3\).
2. **A descent, not a count.** The degree-\(3\) vertices with exactly two
   neighbours of degree \(\ge4\) behave like *subdivision vertices* of edges
   between degree-\(\ge4\) vertices. The resulting "link graph" on the
   degree-\(\ge4\) vertices has the property that each of its cycles of length
   \(\ell\) lifts to a cycle of length \(2\ell\) in \(G\) — so the link graph is
   itself **power-free**, and by order-minimality it can have no subgraph of
   minimum degree \(\ge3\). This is a genuinely new mechanism in this dossier:
   it manufactures a *smaller* power-free object out of a minimal
   counterexample, rather than counting inside it.

Preferable to the live alternatives for this leg because it is unconditional,
uses only already-proved material, and its failure mode is informative: if the
constant cannot be moved, the *reason* localises the obstruction for `G015`.

## Entry assumptions

Statement 0.1 exactly as in `STATEMENT.md` (version 0.1), with `D001`–`D004`.
Throughout, \(G\) is a **counterexample minimizing order and then size**
(order-then-size minimal counterexample): finite, simple, undirected,
\(\delta(G)\ge3\), no cycle of length \(2^k\) with \(k\ge2\), of least order and,
among those, least size. Everything below is conditional on such a \(G\)
existing; if none exists, statement 0.1 holds and every deduction is vacuous.

Facts consumed, at exactly their recorded strength:

- `C004` (Carr, Lemma 0.1; **verified line by line this session**, and
  reproduced internally in §1 of the verification note): every proper subgraph
  of \(G\) with defined minimum degree has a vertex of degree \(\le2\).
- `C005` (Carr, Corollary 0.1(1); **verified this session**): every vertex of
  \(G\) has a neighbour of degree exactly \(3\).
- `L002` (**internally proved**, `A001`): the degree-\(\ge4\) vertices of \(G\)
  are independent. Carr's Corollary 0.1(2) is the same statement and is also
  verified; the internal proof makes the import dispensable.
- `L003` (**internally proved**, `A001`): every counterexample has \(\ge9\)
  vertices. Used only to dispose of two degenerate cases.
- `A012` T4 second branch and `L029`/`L036` are read for context; **no step
  below cites them**, and `A012` Remark T4.1 (withdrawn per `A018`) is not used.

Notation, fixed for the whole record:

- \(n=|V(G)|\); \(A=V_3=\{v:d(v)=3\}\); \(B=V_{\ge4}=\{v:d(v)\ge4\}\);
  \(\beta=|B|\).
- For \(a\in A\), \(\deg_A(a)=|N(a)\cap A|\); \(A_j=\{a\in A:\deg_A(a)=j\}\) and
  \(p=|A_1|,\ q=|A_2|,\ r=|A_3|\).
- \(e(A,B)\) = number of edges with one end in \(A\) and one in \(B\).
- "Power-free" = no cycle of length \(2^k\), \(k\ge2\).
- Deductions are numbered `W2-Tk`. Claim IDs are the orchestrator's to assign;
  none is asserted here.

## Targeted obligations

- `G015`: the cubic reduction — route `R2` (strengthen `C006`).
- `G014`: audit the unverified imports — discharged for `C004`/`C005`/`C006` by
  `references/carr-2026-verification-2026-07-24.md`.

## Plan and decisive tests

1. **Gating test (executed first, passed):** verify Carr's four results line by
   line. If Lemma 0.1, Corollary 0.1(1) or Theorem 0.1 had failed, `R2` would
   have had no base. All four verified; written up separately.
2. **Cheapest falsification of the improvement:** exhibit a graph satisfying
   every hypothesis the argument uses and having cubic density exactly at the
   claimed bound. This was run *after* proving \(2/3\) and it **succeeded** for
   the non-power hypotheses (W2-T7, graph S15), which is why the record
   contains both an improvement and an exact statement of the method's ceiling.
3. **Pivot condition, declared in advance:** if a witness satisfies
   \(\delta\ge3\) + Lemma 0.1 + \(C_4\)-freeness + full power-freeness at
   density \(2/3+o(1)\), route `R2` is dead as a path to `G015` and only the
   improved constant survives. The witness found (S15) satisfies everything
   except power-freeness, so the pivot fired only partially: power-freeness
   still buys something (W2-T6), but provably only an additive constant from
   this constraint set (W2-T8).

## Deductions

### W2-T0 (bookkeeping) — proved

**Claim.** In \(G\):

1. \(V(G)=A\sqcup B\), and \(A\neq\emptyset\).
2. \(B\) is independent, so every edge at a vertex of \(B\) has its other end in
   \(A\), and \(\sum_{b\in B}d(b)=e(A,B)\).
3. Every \(a\in A\) has \(\deg_A(a)\ge1\); hence \(A=A_1\sqcup A_2\sqcup A_3\)
   and \(G[A]\) has no isolated vertex.
4. \(e(A,B)=2p+q\).
5. \(\sum_{b\in B}d(b)\ge4\beta\), hence \(2p+q\ge4\beta\).

*Proof.* (1) \(\delta(G)\ge3\) means every degree is \(3\) or \(\ge4\), and the
two conditions are mutually exclusive, so \(A\) and \(B\) partition \(V(G)\).
\(V(G)\neq\emptyset\), and by `C005` any vertex has a neighbour of degree
exactly \(3\), so \(A\neq\emptyset\).

(2) `L002`. A neighbour of \(b\in B\) lies in \(A\cup B\) and independence
excludes \(B\); summing \(d(b)\) over \(b\in B\) therefore counts each
\(A\)–\(B\) edge exactly once (the two sets are disjoint and no edge has both
ends in \(B\)).

(3) By `C005` each \(a\in A\) has a neighbour of degree exactly \(3\), i.e. a
neighbour in \(A\). Since \(d(a)=3\), \(\deg_A(a)\in\{1,2,3\}\).

(4) \(e(A,B)=\sum_{a\in A}|N(a)\cap B|=\sum_{a\in A}\bigl(3-\deg_A(a)\bigr)
=2|A_1|+1\cdot|A_2|+0\cdot|A_3|=2p+q\), using (1) so that every neighbour of
\(a\) is in \(A\) or \(B\).

(5) Each \(b\in B\) has \(d(b)\ge4\); combine with (2) and (4). ∎

### W2-T1 (the 2/3 bound) — proved

**Claim.** \(\displaystyle |V_{\ge4}|\le\tfrac12|V_3|\), and hence
\(\displaystyle |V_3|\ge\tfrac23 n\).

*Proof.* By W2-T0(1) and (3), \(|A|=p+q+r\) and \(2p+q\ge4\beta\). Also
\(2p+q\le 2(p+q+r)=2|A|\). Therefore \(4\beta\le2|A|\), i.e.
\(\beta\le\frac12|A|\). Then \(n=|A|+\beta\le\frac32|A|\), i.e.
\(|A|\ge\frac23n\). ∎

*Remark (what changed relative to `C006`).* Carr's proof bounds
\(e(A,B)\le 3|A|\), because it does not know that \(A\)-vertices must spend an
edge inside \(A\). `C005` upgrades that to \(e(A,B)\le 2|A|\) (each \(a\in A\)
sends at least one of its three edges to \(A\)). Equivalently: \(G[A]\) has no
isolated vertex, so \(e(G[A])\ge|A|/2\) and
\(e(A,B)=3|A|-2e(G[A])\le2|A|\). \(2/3>4/7\).

*Integrality refinement.* If \(|A|\) is odd then \(e(G[A])\ge(|A|+1)/2\) and
\(4\beta\le e(A,B)\le2|A|-1\), so \(\beta\le\lfloor(2|A|-1)/4\rfloor\).

### W2-T2 (Lemma 0.1 is a degeneracy statement) — proved

**Claim.** For a finite simple graph \(G\), the following are equivalent:
(i) every nonempty proper subgraph \(H\subsetneq G\) has \(\delta(H)\le2\);
(ii) \(G\) has no nonempty proper subgraph of minimum degree \(\ge3\);
(iii) \(G-v\) is 2-degenerate for every \(v\in V(G)\), and \(G-e\) is
2-degenerate for every \(e\in E(G)\).

(Here 2-degenerate means: repeatedly deleting a vertex of current degree \(\le2\)
empties the graph; equivalently, no nonempty subgraph has minimum degree
\(\ge3\).)

*Proof.* (i)\(\Leftrightarrow\)(ii) is a restatement. (ii)\(\Rightarrow\)(iii):
a nonempty subgraph of \(G-v\) or of \(G-e\) of minimum degree \(\ge3\) is a
proper subgraph of \(G\) of minimum degree \(\ge3\). (iii)\(\Rightarrow\)(ii):
let \(H\subsetneq G\) be nonempty and proper. If \(V(H)\subsetneq V(G)\), pick
\(v\in V(G)\setminus V(H)\); then \(H\subseteq G-v\). Otherwise
\(E(H)\subsetneq E(G)\); pick \(e\in E(G)\setminus E(H)\); then \(H\subseteq
G-e\). Degeneracy is inherited by subgraphs, so \(H\) is 2-degenerate and
\(\delta(H)\le2\). ∎

This is the form used by the machine check in `E017`; it reduces an infinite
quantifier to \(n+m\) finite peelings.

### W2-T3 (component deletion; the apex lemma) — proved

**Claim.** Assume \(B\ne\emptyset\). Let \(S\) be the vertex set of a connected
component of \(G[A]\). Then there is \(b\in B\) with
\[
  |N(b)\cap S|\ \ge\ d(b)-2\ \ge\ 2 .
\]
In particular, if \(S=\{a_1,a_2\}\) is a \(K_2\)-component of \(G[A]\) (both
ends in \(A_1\), matched to each other), then such a \(b\) satisfies
\(d(b)=4\) and \(N(b)\supseteq\{a_1,a_2\}\); it is **unique**; and
\(\{a_1,a_2,b\}\) induces a triangle.

*Proof.* \(V(G)\setminus S\supseteq B\ne\emptyset\), so \(H=G-S\) is a nonempty
proper subgraph and `C004` gives \(\delta(H)\le2\): there is
\(u\in V(G)\setminus S\) with \(d_G(u)-|N(u)\cap S|\le2\).

If \(u\in A\setminus S\), then every neighbour of \(u\) inside \(A\) lies in
\(u\)'s own component of \(G[A]\), which is disjoint from \(S\); and no
neighbour of \(u\) in \(B\) lies in \(S\subseteq A\). So \(N(u)\cap S=\emptyset\)
and \(d_H(u)=d_G(u)=3>2\) — impossible. Hence \(u\in B\), and
\(|N(u)\cap S|\ge d_G(u)-2\ge4-2=2\). Take \(b=u\).

Now let \(S=\{a_1,a_2\}\). Then \(|N(b)\cap S|\le2\), so \(d(b)-2\le2\), i.e.
\(d(b)\le4\); with \(d(b)\ge4\) this forces \(d(b)=4\) and
\(|N(b)\cap S|=2\), i.e. \(N(b)\supseteq\{a_1,a_2\}\). If two distinct
\(b,b'\in B\) were both adjacent to \(a_1\) and \(a_2\), then
\(a_1\,b\,a_2\,b'\,a_1\) would be a \(4\)-cycle (four distinct vertices, since
\(A\cap B=\emptyset\)), contradicting power-freeness; so \(b\) is unique.
Finally \(a_1a_2\in E(G)\), so \(a_1,a_2,b\) is a triangle. ∎

### W2-T4 (classification of the equality case in W2-T1) — proved

**Claim.** Suppose \(|V_3|=\frac23 n\) (equivalently \(\beta=\frac12|A|\)). Then:

1. \(q=r=0\): \(G[A]\) is a **perfect matching** (in particular \(|A|\) is even);
2. every \(b\in B\) has degree **exactly** \(4\);
3. \(G\cong S(H)+\mathcal P\), where \(H\) is a **simple 4-regular** graph on the
   \(\beta=n/3\) vertices of \(B\), \(S(H)\) is its subdivision (each edge \(e\)
   of \(H\) replaced by a path \(u-a_e-w\)), and \(\mathcal P\) is a
   \(P_3\)-decomposition of \(H\) — a partition of \(E(H)\) into \(\beta\) pairs
   of **adjacent** edges — contributing one extra edge \(a_ea_f\) for each pair
   \(\{e,f\}\in\mathcal P\).

*Proof.* By W2-T0, \(4\beta\le2p+q\le2(p+q+r)=2|A|\). Equality
\(\beta=\frac12|A|\) forces both inequalities to be equalities. The second gives
\(q=r=0\), so \(A=A_1\): every \(a\in A\) has exactly one neighbour in \(A\), so
\(G[A]\) is a perfect matching. The first gives \(\sum_{b\in B}d(b)=4\beta\)
with each \(d(b)\ge4\), so \(d(b)=4\) for all \(b\).

For (3): each \(a\in A=A_1\) has exactly two neighbours in \(B\); let \(\eta(a)\)
be that pair. If \(\eta(a)=\eta(a')\) for \(a\ne a'\), the four vertices form a
\(4\)-cycle — excluded. So \(\eta\) is injective, and \(H:=(B,\{\eta(a):a\in A\})\)
is a simple loopless graph with \(|E(H)|=|A|=2\beta\) and
\(\deg_H(b)=|N_G(b)\cap A|=d(b)=4\): 4-regular. \(S(H)\) has vertex set
\(B\cup\{a_e\}_{e\in E(H)}\) with \(a_e\) adjacent to the two ends of \(e\),
which is exactly the \(A\)–\(B\) part of \(G\) under \(a\mapsto a_{\eta(a)}\);
\(B\) is independent in \(G\) (W2-T0) and in \(S(H)\); the remaining edges of
\(G\) are exactly the perfect matching \(G[A]\). By W2-T3 each matched pair
\(\{a,a'\}\) has a common \(B\)-neighbour, i.e. \(\eta(a)\cap\eta(a')\ne\emptyset\),
i.e. the edges \(\eta(a),\eta(a')\) of \(H\) are adjacent (they are distinct, so
they meet in exactly one vertex). Hence \(G[A]\) transports to a partition of
\(E(H)\) into \(\beta\) adjacent pairs — a \(P_3\)-decomposition. ∎

*Converse numerics.* For any simple 4-regular \(H\) on \(m\) vertices and any
\(P_3\)-decomposition \(\mathcal P\) (one always exists: a connected graph has a
\(P_3\)-decomposition iff it has evenly many edges, and \(|E(H)|=2m\)), the graph
\(S(H)+\mathcal P\) has \(3m\) vertices, \(2m\) of degree \(3\) and \(m\) of
degree \(4\), density exactly \(2/3\). So the shape in (3) is the exact shape of
the equality case, and it is realizable as a graph — the question is only
whether it can be a minimal counterexample. W2-T5 answers: never.

### W2-T5 (the subdivision descent) — proved

**Definition.** The **link graph** of \(G\) is the graph \(H_1\) with vertex set
\(B\) and one edge \(\eta(a)=N(a)\cap B\) for each \(a\in A_1\).
(By W2-T0(3) every \(a\in A_1\) has exactly two neighbours in \(B\), so
\(\eta(a)\) is a genuine pair of distinct vertices.)

**Claim.**

1. \(H_1\) is a simple loopless graph on \(\beta\) vertices with exactly
   \(p=|A_1|\) edges; the map \(a\mapsto\eta(a)\) is a bijection
   \(A_1\to E(H_1)\).
2. Every cycle of length \(\ell\) in \(H_1\) lifts to a cycle of length
   \(2\ell\) in \(G\). Consequently \(H_1\) is **power-free**.
3. Every subgraph \(K\subseteq H_1\) with \(\delta(K)\ge3\) would be a
   counterexample of order \(\le\beta<n\). Hence **no such \(K\) exists**:
   \(H_1\) is **2-degenerate**.
4. Therefore \(p\le2\beta-3\) whenever \(\beta\ge2\).

*Proof.* (1) Loopless because the two \(B\)-neighbours of \(a\) are distinct
vertices. Simple: if \(\eta(a)=\eta(a')=\{b,b'\}\) with \(a\ne a'\), then
\(a\,b\,a'\,b'\,a\) is a \(4\)-cycle on four distinct vertices (\(a,a'\in A\),
\(b,b'\in B\), \(A\cap B=\emptyset\)), contradicting power-freeness. So \(\eta\)
is injective and \(|E(H_1)|=p\).

(2) Let \(b_1e_1b_2e_2\cdots b_\ell e_\ell b_1\) be a cycle of \(H_1\), with the
\(b_i\in B\) distinct and the \(e_i\in E(H_1)\) distinct, \(e_i=\{b_i,b_{i+1}\}\)
(indices mod \(\ell\)). Put \(a_i=\eta^{-1}(e_i)\in A_1\); these are distinct by
(1). Each \(a_i\) is adjacent in \(G\) to both \(b_i\) and \(b_{i+1}\). Then
\[
  b_1\,a_1\,b_2\,a_2\,\cdots\,b_\ell\,a_\ell\,b_1
\]
is a cycle of \(G\) on \(2\ell\) vertices, all distinct (the \(b_i\) are
distinct, the \(a_i\) are distinct, and \(A\cap B=\emptyset\)). \(G\) is
power-free, so \(2\ell\ne2^k\) for every \(k\ge2\), i.e. \(\ell\notin\{2,4,8,16,\dots\}\).
Since \(H_1\) is simple, \(\ell\ge3\), so \(\ell\notin\{4,8,16,\dots\}\): \(H_1\)
has no cycle of length a power of two, i.e. \(H_1\) is power-free.

(3) Let \(K\subseteq H_1\) be nonempty with \(\delta(K)\ge3\). \(K\) is finite,
simple and undirected; every cycle of \(K\) is a cycle of \(H_1\), so \(K\) is
power-free by (2); and \(\delta(K)\ge3\). So \(K\) is a counterexample to
statement 0.1. Its order is at most \(\beta=n-|A|<n\), because \(A\ne\emptyset\)
(W2-T0(1)). This contradicts the order-minimality of \(G\). So no such \(K\)
exists, which is exactly 2-degeneracy of \(H_1\).

(4) A 2-degenerate graph on \(\beta\ge2\) vertices has at most \(2\beta-3\)
edges: order its vertices \(v_1,\dots,v_\beta\) as the reverse of a peeling
order, so that each \(v_i\) has at most \(2\) neighbours among
\(v_1,\dots,v_{i-1}\); then \(|E|\le 0+1+2(\beta-2)=2\beta-3\). ∎

*Why this is not a counting argument.* (3) uses order-minimality of \(G\)
against a graph that is not a subgraph of \(G\) — it is a *minor-like*
contraction of the subdivision structure. Nothing in `C004`/`C005`/`L002`
supplies it, and it is invisible to any argument phrased only in degrees of
\(G\). It is the first place in this dossier where power-freeness at *all* even
lengths, not just \(C_4\), is converted into a structural restriction on the
degree-\(\ge4\) set.

*Immediate corollary (equality is impossible).* In the equality case of W2-T4,
\(A=A_1\) and \(H_1=H\) is 4-regular, so \(\delta(H_1)=4\ge3\), contradicting
(3). Hence \(|V_3|>\frac23n\) always. W2-T6 quantifies this.

### W2-T6 (the improved density bound) — proved

**Claim.** For every order-then-size minimal counterexample \(G\) of order \(n\):
\[
  3\,|V_3|\ \ge\ 2n+3,
  \qquad\text{i.e.}\qquad
  \frac{|V_3|}{n}\ \ge\ \frac23+\frac1n,
  \qquad\text{and}\qquad
  |V_{\ge4}|\ \le\ \frac{n-3}{3}.
\]
Moreover, if \(\beta\ge2\) then \(|A_2|\ge6\): at least six degree-\(3\) vertices
have exactly two degree-\(3\) neighbours.

*Proof.* By `L003`, \(n\ge9\).

*Case \(\beta=0\).* \(|V_3|=n\) and \(3n\ge2n+3\) since \(n\ge3\).

*Case \(\beta=1\).* \(|V_3|=n-1\) and \(3(n-1)\ge2n+3\) iff \(n\ge6\).

*Case \(\beta\ge2\).* By W2-T5(4), \(p\le2\beta-3\). By W2-T0(5),
\(q\ge4\beta-2p\); and \(4\beta-2p\ge4\beta-2(2\beta-3)=6>0\), so this is a
positive lower bound and \(q\ge6\). Hence
\[
  |A|=p+q+r\ \ge\ p+q\ \ge\ p+(4\beta-2p)=4\beta-p\ \ge\ 4\beta-(2\beta-3)=2\beta+3 .
\]
Substituting \(\beta=n-|A|\) gives \(|A|\ge2(n-|A|)+3\), i.e.
\(3|A|\ge2n+3\). The bound on \(|V_{\ge4}|\) follows from
\(|V_{\ge4}|=n-|V_3|\). ∎

*Comparison.* `C006` gives \(|V_3|\ge\frac47n\approx0.5714\,n\) and
\(|V_{\ge4}|\le\frac37n\approx0.4286\,n\). This gives
\(|V_3|\ge\frac23n+1\approx0.6667\,n\) and \(|V_{\ge4}|\le\frac13n-1\). Both are
strict improvements, unconditionally, for the same object. As integers,
\(|V_3|\ge\lceil 2n/3\rceil+1\) when \(3\mid n\), and \(\ge\lceil(2n+3)/3\rceil\)
in general.

### W2-T7 (exact sharpness of the non-power hypotheses) — proved; machine-assisted in one clause

**Claim.** Let \(\mathcal H\) be the hypothesis set

- \(\delta\ge3\);
- no proper subgraph of minimum degree \(\ge3\) (= `C004`, the full strength of
  Carr's Lemma 0.1, which by W2-T2 is a finite condition);
- no \(4\)-cycle.

(Note that `L002` and `C005` are *consequences* of \(\mathcal H\), by exactly
Carr's Corollary 0.1 arguments, so \(\mathcal H\) is at least as strong as
everything W2-T1 uses.) Then **no argument from \(\mathcal H\) alone can prove a
cubic-density constant better than \(2/3\)**: the following graph S15 satisfies
every condition in \(\mathcal H\) and has exactly \(\frac23\) of its vertices of
degree \(3\).

**S15.** Vertices \(a_i,a'_i,b_i\) for \(i\in\mathbb{Z}_5\) (15 vertices);
edges (25 in total), for each \(i\in\mathbb{Z}_5\):
\[
  a_ia'_i,\qquad a_ib_i,\qquad a'_ib_i,\qquad a_ib_{i+1},\qquad a'_ib_{i+2}.
\]

*Verification.*

- *Degrees.* \(N(a_i)=\{a'_i,b_i,b_{i+1}\}\) and \(N(a'_i)=\{a_i,b_i,b_{i+2}\}\),
  both of size 3. \(b_j\) is adjacent to \(a_j,a'_j\) (apex edges), to
  \(a_{j-1}\) (from \(a_ib_{i+1}\) with \(i=j-1\)) and to \(a'_{j-2}\) (from
  \(a'_ib_{i+2}\) with \(i=j-2\)): degree 4. So \(\delta=3\), \(V_3=\{a_i,a'_i\}\)
  with \(|V_3|=10\), \(V_{\ge4}=\{b_i\}\) with \(|V_{\ge4}|=5\), and
  \(|V_3|/n=10/15=2/3\) exactly.
- *\(V_{\ge4}\) independent, and `C005` holds.* No edge joins two \(b\)'s by
  construction. Each \(b_j\) has all four neighbours in \(V_3\); each \(a_i\) has
  the neighbour \(a'_i\in V_3\) and vice versa.
- *No \(4\)-cycle.* \(G[V_3]\) is the perfect matching \(\{a_ia'_i\}\), so each
  \(V_3\)-vertex has exactly one \(V_3\)-neighbour and exactly two
  \(V_{\ge4}\)-neighbours. A \(4\)-cycle cannot use a \(V_3\)–\(V_3\) edge: from
  \(a_ia'_i\) it would need a common neighbour path of length 3 through vertices
  \(z,w\); \(z,w\) cannot both be in \(V_{\ge4}\) (independent) and cannot be in
  \(V_3\) (each \(V_3\)-vertex has only one \(V_3\)-neighbour, already used).
  Two \(V_3\)–\(V_3\) edges cannot both appear (matching edges are pairwise
  non-adjacent). So every \(4\)-cycle alternates \(V_3,V_{\ge4}\), i.e. two
  \(V_3\)-vertices share both their \(V_{\ge4}\)-neighbours. But
  \(\eta(a_i)=\{b_i,b_{i+1}\}\) and \(\eta(a'_i)=\{b_i,b_{i+2}\}\): the five sets
  of the first kind are the five \(\mathbb{Z}_5\)-pairs of difference \(\pm1\),
  the five of the second kind those of difference \(\pm2\), and \(1\not\equiv\pm2
  \pmod 5\), so all ten sets are distinct. No \(4\)-cycle.
- *No proper subgraph of minimum degree \(\ge3\).* By W2-T2 this is the
  2-degeneracy of the 15 graphs \(G-v\) and the 25 graphs \(G-e\). The map
  \(a_i\mapsto a_{i+1},\ a'_i\mapsto a'_{i+1},\ b_i\mapsto b_{i+1}\) is an
  automorphism, so there are only **3 vertex orbits and 5 edge orbits**: eight
  peelings settle it. Machine-verified exhaustively (all 15 + 25 cases) in
  `E017`, under two interpreters.
- *What S15 is not.* S15 is **not** power-free and **not** a counterexample: an
  explicit \(8\)-cycle is
  \[
    b_1\,a_1\,b_2\,a_2\,b_3\,a'_3\,b_5\,a_5\,b_1
  \]
  (check: \(a_1\sim b_1,b_2\); \(a_2\sim b_2,b_3\); \(a'_3\sim b_3,b_5\);
  \(a_5\sim b_5,b_1\)). `E017` computes its full cycle census: lengths
  \(3,5,6,7,8,\dots,15\) with fifty \(8\)-cycles, and \(8\) is the only
  power-of-two length present. ∎

*Reading.* S15 is the \(H_1=K_5\) instance of W2-T4's classification:
\(K_5\) is simple and 4-regular, and \(\{a_i,a'_i\}\) is a \(P_3\)-decomposition
of it. \(K_5\) contains \(4\)-cycles, which lift to \(8\)-cycles of S15 —
exactly the failure that W2-T5 forbids. So the descent is precisely the
ingredient that separates W2-T6 from W2-T1, and S15 shows nothing weaker can.

### W2-T8 (the ceiling of route R2) — recorded reasoning, not a theorem

Two obstructions, stated separately because they have different status.

**(a) A density constant below \(1\) cannot deliver `G015`.** `G015` is
"\(V_{\ge4}=\emptyset\) for a minimal counterexample". Any bound of the form
\(|V_3|\ge c\,n\) with \(c<1\) is compatible with \(V_{\ge4}\ne\emptyset\); and
\(c=1\) is not a density statement at all — it asserts the emptiness directly.
So `R2` phrased as "improve the constant" can approach `G015` but can never
reach it by improving a constant: the final step is necessarily structural. This
is a definitional observation, not a mathematical obstruction, but it re-scopes
the route.

**(b) The available constraint set caps out at \(2/3\) asymptotically.**
The constraints actually proved above are
\[
  2p+q\ \ge\ 4\beta,\qquad p\ \le\ 2\beta-3,\qquad
  |V_3|=p+q+r,\qquad n=|V_3|+\beta .
\]
Their linear-programming optimum is attained at \(r=0\), \(p=2\beta-3\),
\(q=6\), giving \(|V_3|=2\beta+3\) and \(n=3\beta+3\), so
\(|V_3|/n=(2\beta+3)/(3\beta+3)\to 2/3\). Hence **no strengthening of the
counting alone can beat \(2/3+O(1/n)\)**; the additive \(+1\) of W2-T6 is the
whole gain available from this constraint set. To improve the *constant* one
must improve the edge bound \(p\le2\beta-3\), i.e. prove that a power-free
2-degenerate graph has average degree bounded away from \(4\). That is
**provisionally judged false**, on the following heuristic — used here as
intuition for a research judgment and **not** as a proof step, and not imported
as a claim: the classical extremal numbers for the relevant even cycles
(Kővári–Sós–Turán / Erdős–Rényi–Sós for \(C_4\); Bondy–Simonovits for \(C_8\))
grow strictly faster than linearly, so forbidding \(C_4,C_8,C_{16},\dots\) is not
expected to hold average degree below \(4\) at large order, while maximal
2-degenerate graphs can plausibly be built greedily keeping all codegrees
\(\le1\). Neither a proof nor a counterexample is offered. Deciding this is the
natural first target if someone wants to reopen the counting; it is a finite
search at small orders and a construction question at large ones.

**(c) Where the descent could still be pushed (open, with the gap named).** The
descent used only links of length 2 — a single \(A_1\)-vertex between two
\(B\)-vertices — and the reason it works cleanly is that the internal vertex
*is* the edge label: distinct edges of \(H_1\) have distinct internal vertices
automatically, so a cycle of \(H_1\) lifts to a cycle of \(G\) with no vertex
repetitions. The length multiplier is \(2\), and \(2\ell=2^k\iff\ell=2^{k-1}\),
so power-freeness transfers exactly.

The same arithmetic works for links of length \(4\) (\(4\ell=2^k\iff
\ell=2^{k-2}\)) and, more generally, for links whose common length is a power of
two. **The obstruction to using them is not arithmetic but disjointness.** A
length-4 link is a path \(b-x-y-z-b'\) with \(x,y,z\notin B\); two distinct such
links may share internal vertices, so a cycle in the length-4 link multigraph
need not lift to a *cycle* of \(G\). Repairing this needs either a definition of
the link graph that enforces pairwise internal disjointness along every cycle
(and then the 2-degeneracy conclusion must be re-derived for that object), or an
argument that shared internal vertices themselves force a power-of-two cycle.
Two facts do survive unconditionally and may be useful: a length-4 link with
both endpoints equal is a \(4\)-cycle, hence does not exist; and two
*internally disjoint* length-4 links with the same endpoints form an
\(8\)-cycle, hence do not exist. What is definitely *not* available is mixing
link lengths: a cycle using \(i\) links of length \(2\) and \(j\) of length
\(4\) has length \(2i+4j\), which is unconstrained by power-freeness.

Making the length-4 (or mixed) case work — or ruling it out — is the open end of
this mechanism, and is the only visible way to push past \(2/3\) by descent.

**(d) A bridge to route R1 (observation).** A connected subgraph \(K\subseteq
H_1\) with exactly one vertex of degree \(<3\), that vertex of degree exactly
\(2\), is precisely a **tight 1-atom** (`A018` T2's object: connected,
power-free by W2-T5(2), one sub-cubic vertex of degree 2). So `R1`'s hypothesis
"no tight 1-atom exists" applies verbatim to the link graph, and under it every
component of the 2-core of \(H_1\) has at least two vertices of degree exactly
\(2\). The two routes of `G015` therefore meet on the same object. No
quantitative gain is extracted from this here.

## Failure analysis

Not a failed route, but the route's ceiling is now located precisely, and it is
below the target.

- The improvement \(4/7\to 2/3\) is real, unconditional, and cheap: it is the
  first joint use of Carr's two corollaries.
- The improvement \(2/3\to 2/3+1/n\) required a new mechanism (the descent) and
  yields only an additive constant.
- The exact obstruction to more is W2-T8(b): 2-degeneracy of the link graph
  permits average degree \(4-6/\beta\), which is exactly the density the
  \(B\)-side needs. The two constraints meet asymptotically with no slack.
- The obstruction is *not* an artefact of weak hypotheses: W2-T7 exhibits a
  concrete 15-vertex graph on which every non-power hypothesis is tight
  simultaneously.

## Salvageable results

- **W2-T6** (the headline): \(3|V_3|\ge2n+3\) and \(|V_{\ge4}|\le(n-3)/3\) for an
  order-then-size minimal counterexample — strictly stronger than `C006`, with a
  complete internal proof depending only on `C004`, `C005`, `L002`, `L003` and
  power-freeness.
- **W2-T1** (\(|V_3|\ge\frac23n\)) as the version that needs no power-freeness
  beyond \(C_4\), and **W2-T7** as its exact sharpness certificate.
- **W2-T5** (the subdivision descent) as a *reusable mechanism*: it converts a
  minimal counterexample into a smaller power-free graph and is not tied to the
  density question. Any future argument that wants to exploit the degree-\(\ge4\)
  set structurally can use "the link graph is power-free and 2-degenerate".
- **W2-T3** (apex lemma) and **W2-T4** (equality classification: subdivision of a
  simple 4-regular graph plus a \(P_3\)-decomposition) as structure theorems for
  the degree-\(\ge4\) set.
- **W2-T2** as the finite reformulation of `C004` — it is what makes `C004`
  machine-checkable on a candidate graph, and `E017` uses it.
- The warning in **W2-T8(a)**: no constant \(<1\) reaches `G015`.
- `references/carr-2026-verification-2026-07-24.md`: all of `C004`, `C005`,
  `C006` verified line by line against arXiv:2605.22844v1, and all three shown
  to be internally reconstructible.

## Exit state

- Status: complete for its stated scope
- Machine support: `E017` (single-graph certificate; CPython 3.14.2 and
  PyPy 7.3.23; 35 checks including 11 anchors, all passed under both)
- Promoted records: none by this worker — W2-T1, W2-T3, W2-T4, W2-T5, W2-T6,
  W2-T7 are offered to the orchestrator for claim IDs, together with the
  verification note discharging the `G014` item for `C004`–`C006`.
- Next action proposed: **do not** continue to grind the constant. Either
  (i) settle W2-T8(b) — decide whether a power-free 2-degenerate graph can have
  \(2\beta-o(\beta)\) edges, which would close the counting route for good; or
  (ii) take the descent (W2-T5) into the mixed-link regime of W2-T8(c), which is
  the only visible route by which it could reach `G015`; or
  (iii) redirect `G015` to route `R1` (no tight 1-atom), to which W2-T8(d)
  supplies a new handle on the link graph.
