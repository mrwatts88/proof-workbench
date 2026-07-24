# A013 — The taut s_min=3 rung: middle-layer collapse and the three-matchings endgame

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: closed (results promoted)
- Portfolio role: primary (the inherited next action: the taut \(s_{\min}=3\) rung)

## Intended mechanism

The inherited target: prove that no vertex-taut \(C_4\)-free power-free
(D)-gadget with \(S\subseteq\{3,4,5\}\) exists, or exhibit one. The
failure-first opening move was to *build* one: start from the constraints
(tautness pins every vertex to a short \(a\)–\(b\) path, \(C_4\)-freeness
caps every codegree at one, condition (D) forces degree \(\ge3\) off the
terminals) and let the construction show where freedom survives. It never
does: the constraints cascade — the middle layer collapses class by class
until it vanishes, the remaining graph is three perfect matchings on
\(N(a)\cup N(b)\), and the final degree of freedom is a dichotomy in which
one branch is a forced \(C_4\) and the other a forced \(a\)–\(b\) path of
length \(7\). The rung therefore closes **without power-freeness**:
\(C_4\)-freeness alone suffices, as it did for the \(s_{\min}\le2\) rungs
(`L028`), and the expectation recorded at S012 — that the power spectrum
must start carrying the argument at \(s_{\min}=3\) — was wrong. By `C028`'s
five taut pinched \(s_{\min}=6\) witnesses, the \(C_4\)-only regime ends
somewhere in \(s_{\min}\in\{4,5,6\}\).

## Entry assumptions

Statement 0.1 exactly as in `STATEMENT.md`. All graphs finite and simple.
"Power-free": no cycle of length \(2^k\), \(k\ge2\). Definitions D-A1–D-A5
(two-terminal graph, through-set \(S\), condition (D), 2-atom, 1-atom, ring)
from `A011`; D-B1 (essential vertex, taut) and D-B2 (lobe) from `A012`.
`L025`, `L027`, `L028`, `C027`, `C028`, `L022` are consumed at their recorded
strengths. All proofs below are self-contained hand proofs; no conditional
or abstract-strength imports are used.

## Targeted obligations

- `G013`(b): taut 2-atoms with \(s_{\min}\ge3\) — the \(s_{\min}=3\) rung is
  closed here.
- `G007`: the global mechanism — the taut ladder's forcing pattern
  (\(C_4\)-only middle-layer collapse) is quantified exactly.

## Setup and notation

Throughout, \((H,a,b)\) is a vertex-taut \(C_4\)-free (D)-gadget with
\(S=S(H,a,b)\subseteq\{3,4,5\}\), toward a contradiction. Write
\(X=N(a)\), \(Z=N(b)\), \(M=V(H)\setminus(\{a,b\}\cup X\cup Z)\).

Because \(1\notin S\): \(ab\notin E\). Because \(2\notin S\):
\(N(a)\cap N(b)=\emptyset\). Hence \(a,b\notin X\cup Z\), \(X\cap
Z=\emptyset\), \(b\) has no neighbor in \(X\), \(a\) none in \(Z\), and the
five sets \(\{a\},\{b\},X,Z,M\) partition \(V(H)\). Since
\(s_{\min}=d_H(a,b)\), the hypothesis \(S\subseteq\{3,4,5\}\) says exactly:
\(d_H(a,b)\ge3\) and **no simple \(a\)–\(b\) path has length \(\ge6\)**.
Every deduction below exhibits either a \(C_4\) or a simple \(a\)–\(b\) path
of length \(6\) or \(7\); each such exhibit is a contradiction.

Condition (D) gives \(\deg(v)\ge3\) for all \(v\notin\{a,b\}\) and
\(\deg(a),\deg(b)\ge1\), so \(X,Z\ne\emptyset\). (The clause
\(\deg(a)+\deg(b)\ge3\) of (D) is never used.) Tautness: every vertex lies
on a simple \(a\)–\(b\) path, necessarily of length \(3\), \(4\), or \(5\).

## Deductions

### T1 (codegree rules) — proved

**Claim.** In a \(C_4\)-free graph every pair of distinct vertices has at
most one common neighbor. Consequently, in \(H\):

1. every vertex \(v\ne a\) has at most one neighbor in \(X\), and every
   vertex \(v\ne b\) has at most one neighbor in \(Z\);
2. the edges inside \(X\) form a matching, as do the edges inside \(Z\);
3. the \(X\)–\(Z\) edges form a partial matching (each \(x\in X\) on at most
   one, each \(z\in Z\) on at most one).

*Proof.* Two common neighbors \(u\ne u'\) of a pair \(v\ne v'\) give the
4-cycle \(v\,u\,v'\,u'\) (all four distinct: \(u,u'\notin\{v,v'\}\) because
the graph is simple). For (1): if some \(v\ne a\) had two neighbors
\(x\ne x'\) in \(X\), then \(a\) and \(v\) would be two common neighbors of
the pair \((x,x')\), giving the \(C_4\) \(a\,x\,v\,x'\). This applies to
every such \(v\), including \(v\in X\) and \(v\in Z\); and \(b\) has zero
\(X\)-neighbors anyway. (2) is (1) applied to \(v\in X\); (3) is (1) applied
to \(x\in X\) (at most one \(Z\)-neighbor, as \(x\ne b\)) and to \(z\in Z\)
(at most one \(X\)-neighbor, as \(z\ne a\)). ∎

### T2 (middle coverage and the tautness workhorse) — proved

Let \(M_2=\{m\in M:\ m\ \text{has a neighbor in}\ X\}\) and
\(M_3=\{m\in M:\ m\ \text{has a neighbor in}\ Z\}\); set
\(P=M_2\setminus M_3\), \(Q=M_3\setminus M_2\), \(R=M_2\cap M_3\). By T1(1),
each \(m\in M_2\) has a *unique* \(X\)-neighbor \(x_m\), and each
\(m\in M_3\) a unique \(Z\)-neighbor \(z_m\).

**Claim.** (i) \(M=M_2\cup M_3\). (ii) Every \(u\in P\) has a neighbor in
\(M_3\); every \(u\in Q\) has a neighbor in \(M_2\).

*Proof.* (i) By tautness, \(m\in M\) lies on a simple \(a\)–\(b\) path
\(a=v_0,v_1,\dots,v_\ell=b\) with \(\ell\in\{3,4,5\}\). Here \(v_1\in X\)
and \(v_{\ell-1}\in Z\), so \(m=v_i\) for some \(2\le i\le\ell-2\). Every
such position satisfies \(i=2\) or \(i=\ell-2\) (because \(\ell\le5\)); at
\(i=2\), \(m\sim v_1\in X\) gives \(m\in M_2\); at \(i=\ell-2\),
\(m\sim v_{\ell-1}\in Z\) gives \(m\in M_3\).

(ii) Let \(u\in P\) and take its path as in (i). Positions forcing a
\(Z\)-neighbor are impossible for \(u\): \(i=\ell-2\) is such a position,
and for \(\ell=4\), \(i=2=\ell-2\) as well. The only remainder is
\(\ell=5\), \(i=2\): the path is \(a\,v_1\,u\,v_3\,v_4\,b\) with
\(u\sim v_3\), \(v_3\sim v_4\in Z\). Now \(v_3\notin\{a,b\}\) (positions);
\(v_3\in Z\) would make \(v_3\) a \(Z\)-neighbor of \(u\) — excluded for
\(u\in P\); \(v_3\in X\) would give \(u\) the two distinct \(X\)-neighbors
\(v_1,v_3\), contradicting T1(1). So \(v_3\in M\) and \(v_3\sim v_4\in Z\):
\(v_3\in M_3\).

Mirror for \(u\in Q\): only \(\ell=5\), \(i=3\) is possible; the path is
\(a\,v_1\,v_2\,u\,v_4\,b\) with \(u\sim v_2\), \(v_2\sim v_1\in X\). Then
\(v_2\notin\{a,b\}\); \(v_2\in X\) would make \(v_2\) an \(X\)-neighbor of
\(u\) — excluded for \(u\in Q\); \(v_2\in Z\) would give \(u\) the two
distinct \(Z\)-neighbors \(v_2,v_4\), contradicting T1(1). So
\(v_2\in M_2\). ∎

### T3 (degree inventory) — proved

**Claim.** Every \(m\in M\) has all its neighbors in \(X\cup Z\cup M\), at
most one in \(X\) and at most one in \(Z\). Hence every vertex of \(P\) and
of \(Q\) has at least two \(M\)-neighbors, and every vertex of \(R\) at
least one.

*Proof.* \(m\notin X\cup Z\) means \(m\not\sim a\) and \(m\not\sim b\);
T1(1) bounds the \(X\)- and \(Z\)-counts by one. Since \(m\) is
non-terminal, \(\deg(m)\ge3\); subtracting the at most one special neighbor
for \(P,Q\) (which have none on the other side) leaves \(\ge2\), and
subtracting both for \(R\) leaves \(\ge1\). ∎

### T4 (P and Q are empty) — proved

**Claim.** \(P=Q=\emptyset\); hence \(M=R\): every middle vertex has exactly
one \(X\)-neighbor and exactly one \(Z\)-neighbor.

*Proof.* Step 1: *no edge inside \(P\), none inside \(Q\).* Let \(u,w\in P\)
be adjacent. By T2(ii), \(w\) has a neighbor \(t\in M_3\); and \(t\ne u\)
because \(u\notin M_3\). Then
\[a\;x_u\;u\;w\;t\;z_t\;b\]
is a simple \(a\)–\(b\) path of length \(6\): its seven vertices are
pairwise distinct (\(x_u\in X\); \(u,w,t\in M\) pairwise distinct; \(z_t\in
Z\)), and its edges \(ax_u\), \(x_uu\), \(uw\), \(wt\), \(tz_t\), \(z_tb\)
are all present. Contradiction. Mirror for \(Q\) (using T2(ii)'s
\(M_2\)-neighbor and the path \(a\,x_t\,t\,w\,u\,z_u\,b\)).

Step 2: *no \(P\)–\(Q\) edge.* Let \(u\in P\sim w\in Q\). By T3, \(w\) has
\(\ge2\) \(M\)-neighbors; by Step 1 none lies in \(Q\); so some
\(v\in P\cup R\) with \(v\ne u\) is adjacent to \(w\).

- If \(v\in R\): then \(a\;x_u\;u\;w\;v\;z_v\;b\) is a simple path of
  length \(6\) (distinctness: \(v\ne u\) by choice, \(v\ne w\) by
  simplicity of the graph, classes otherwise), contradiction.
- If \(v\in P\): by T3 and Step 1, the \(\ge2\) \(M\)-neighbors of \(u\)
  all lie in \(Q\cup R\subseteq M_3\); pick one \(s\ne w\). Then
  \(a\;x_v\;v\;w\;u\;s\;z_s\;b\) is a simple path of length \(7\):
  \(x_v\) exists (\(v\in P\subseteq M_2\)); the four middles \(v,w,u,s\)
  are pairwise distinct (\(v\ne u\), \(s\ne w\) by choice; \(s\ne v\)
  because \(s\in M_3\) while \(v\in P\); adjacency gives the rest);
  \(z_s\) exists (\(s\in M_3\)); edges \(ax_v\), \(x_vv\), \(vw\), \(wu\),
  \(us\), \(sz_s\), \(z_sb\) all present. Contradiction.

Either way \(w\) has no admissible second \(M\)-neighbor — contradiction.

Step 3: *\(P=Q=\emptyset\).* Let \(u\in P\). Its \(\ge2\) \(M\)-neighbors
(T3) lie in \(R\) by Steps 1–2; pick \(r_1\ne r_2\in R\). Then
\[a\;x_{r_1}\;r_1\;u\;r_2\;z_{r_2}\;b\]
is a simple path of length \(6\) (edges \(ax_{r_1}\), \(x_{r_1}r_1\),
\(r_1u\), \(ur_2\), \(r_2z_{r_2}\), \(z_{r_2}b\); distinctness by classes
and \(r_1\ne r_2\)). Contradiction; so \(P=\emptyset\), and by mirror
\(Q=\emptyset\). ∎

### T5 (the middle is a perfect matching of degree-3 triples) — proved

**Claim.** \(H[M]\) is a perfect matching, and every \(m\in M\) has
\(\deg_H(m)=3\) with \(N(m)=\{x_m,z_m,m'\}\), where \(m'\) is its partner.

*Proof.* By T4, \(M=R\), so each \(m\in M\) has exactly one \(X\)- and one
\(Z\)-neighbor, and by T3 at least one \(M\)-neighbor. If some \(m\) had two
distinct \(M\)-neighbors \(r,r'\), then
\[a\;x_r\;r\;m\;r'\;z_{r'}\;b\]
would be a simple path of length \(6\) (all of \(r,m,r'\in M\) distinct;
\(x_r\), \(z_{r'}\) exist since \(r,r'\in R\); edges present).
Contradiction. So each \(m\) has exactly one \(M\)-neighbor and
\(\deg(m)=3\). ∎

### T6 (X-edges exclude middle contact) — proved

**Claim.** If \(x\sim x'\) with \(x,x'\in X\), then neither \(x\) nor
\(x'\) has a neighbor in \(M\). Mirror statement for edges inside \(Z\).

*Proof.* Suppose \(x'\sim m\in M\) (so \(x'=x_m\) by uniqueness). By T5,
\(m\) has a partner \(m'\) with \(z_{m'}\in Z\). Then
\[a\;x\;x'\;m\;m'\;z_{m'}\;b\]
is a simple path of length \(6\) (distinctness by classes and
\(x\ne x'\), \(m\ne m'\); edges \(ax\), \(xx'\), \(x'm\), \(mm'\),
\(m'z_{m'}\), \(z_{m'}b\)). Contradiction; the argument for \(x\) and the
\(Z\)-mirror are identical. ∎

### T7 (the middle is empty) — proved

**Claim.** \(M=\emptyset\).

*Proof.* Suppose not, and pick a matched pair \(m\sim m'\) (T5).

**Case 1: \(x_m\ne x_{m'}\).** The non-terminal \(x_{m'}\) needs
\(\deg\ge3\). Note \(x_{m'}\not\sim m\) (the unique \(X\)-neighbor of \(m\)
is \(x_m\ne x_{m'}\)). Its candidate neighbors beyond \(a\) and \(m'\):

- another middle \(m''\notin\{m,m'\}\): then
  \(a\;x_m\;m\;m'\;x_{m'}\;m''\;z_{m''}\;b\) is a simple path of length
  \(7\) (distinct: \(x_m\ne x_{m'}\) by the case; \(m,m',m''\) pairwise
  distinct; \(z_{m''}\in Z\) appears once; all seven edges present).
  Contradiction.
- a \(Z\)-neighbor \(z''\): then \(a\;x_m\;m\;m'\;x_{m'}\;z''\;b\) is a
  simple path of length \(6\) (neither \(z_m\) nor \(z_{m'}\) is on the
  path, so no repeat regardless of whether \(z''\) equals one of them).
  Contradiction.
- an \(X\)-neighbor: excluded by T6, since \(x_{m'}\sim m'\in M\).

So \(\deg(x_{m'})\le2\) — contradiction.

**Case 2: \(x_m=x_{m'}=:x\).** First \(z_m\ne z_{m'}\), else
\(m\,x\,m'\,z_m\) is a \(C_4\) (edges \(mx\), \(xm'\), \(m'z_m\), \(z_mm\);
four distinct vertices). The non-terminal \(z_{m'}\) needs \(\deg\ge3\).
Note \(z_{m'}\not\sim m\) (the unique \(Z\)-neighbor of \(m\) is
\(z_m\ne z_{m'}\)). Its candidate neighbors beyond \(b\) and \(m'\):

- another middle \(m''\notin\{m,m'\}\): then
  \(a\;x_{m''}\;m''\;z_{m'}\;m'\;m\;z_m\;b\) is a simple path of length
  \(7\) (distinct: \(x_{m''}\) may or may not equal \(x\) — \(x\) is not on
  the path, so either way no repeat; \(m'',m',m\) pairwise distinct;
  \(z_{m'}\ne z_m\); all seven edges present). Contradiction.
- an \(X\)-neighbor \(x''\): if \(x''=x\), then \(x\,m\,m'\,z_{m'}\) is a
  \(C_4\) (edges \(xm\), \(mm'\), \(m'z_{m'}\), \(z_{m'}x\)); if
  \(x''\ne x\), then \(a\;x''\;z_{m'}\;m'\;m\;z_m\;b\) is a simple path of
  length \(6\). Contradiction either way.
- a \(Z\)-neighbor: excluded by the \(Z\)-mirror of T6, since
  \(z_{m'}\sim m'\in M\).

So \(\deg(z_{m'})\le2\) — contradiction. ∎

### T8 (three-matchings endgame and the theorem) — proved

**Theorem.** No vertex-taut \(C_4\)-free (D)-gadget \((H,a,b)\) has
\(S(H,a,b)\subseteq\{3,4,5\}\).

*Proof.* Continue from T7: \(V(H)=\{a,b\}\cup X\cup Z\). Each \(x\in X\)
has \(N(x)\subseteq\{a\}\cup X\cup Z\) with at most one neighbor in \(X\)
and at most one in \(Z\) (T1); \(\deg(x)\ge3\) forces **exactly one of
each**: write \(\varphi(x)\) for the \(X\)-neighbor and \(\sigma(x)\in Z\)
for the \(Z\)-neighbor. Thus \(\varphi\) is a fixed-point-free involution on
\(X\), and \(\sigma:X\to Z\) is injective (each \(z\) has \(\le1\)
\(X\)-neighbor, T1(3)). Symmetrically each \(z\in Z\) has exactly one
\(Z\)-neighbor \(\psi(z)\) (fixed-point-free involution) and exactly one
\(X\)-neighbor; the latter makes \(\sigma\) surjective, hence a bijection.
(If \(X\)–\(Z\) edges were absent — in particular whenever \(3\notin S\) —
the same inventory gives \(\deg(x)\le2\) at once.)

Fix any \(x_1\in X\ne\emptyset\). Let \(z_s=\sigma(x_1)\) and
\(z_t=\psi(z_s)\ne z_s\).

**Case A: \(\sigma(\varphi(x_1))=z_t\).** Then
\(x_1\,\varphi(x_1)\,z_t\,z_s\) is a \(C_4\): edges \(x_1\varphi(x_1)\)
(\(X\)-matching), \(\varphi(x_1)\,z_t\) (cross, the case assumption),
\(z_t\,z_s\) (\(Z\)-matching), \(z_s\,x_1\) (cross); the four vertices are
distinct (\(x_1\ne\varphi(x_1)\); \(z_s\ne z_t\); \(X\cap Z=\emptyset\)).
Contradiction.

**Case B: \(\sigma(\varphi(x_1))\ne z_t\).** Let \(x_j=\sigma^{-1}(z_t)\):
then \(x_j\ne x_1\) (since \(\sigma(x_1)=z_s\ne z_t\)) and
\(x_j\ne\varphi(x_1)\) (the case assumption). Let
\(x_{j'}=\varphi(x_j)\ne x_j\); also \(x_{j'}\ne x_1\) (else applying
\(\varphi\) gives \(x_j=\varphi(x_1)\)). Let \(z_f=\sigma(x_{j'})\): then
\(z_f\ne z_s\) (injectivity, \(x_{j'}\ne x_1\)) and \(z_f\ne z_t\)
(injectivity, \(x_{j'}\ne x_j\)). Then
\[a\;x_1\;z_s\;z_t\;x_j\;x_{j'}\;z_f\;b\]
is a simple \(a\)–\(b\) path of length \(7\): the \(X\)-vertices
\(x_1,x_j,x_{j'}\) are pairwise distinct, the \(Z\)-vertices
\(z_s,z_t,z_f\) are pairwise distinct, and the edges \(ax_1\); \(x_1z_s\),
\(z_tx_j\), \(x_{j'}z_f\) (cross); \(z_sz_t\) (\(Z\)-matching);
\(x_jx_{j'}\) (\(X\)-matching); \(z_fb\) are all present. Contradiction.

Both cases are impossible; no such gadget exists. ∎

**Remark T8.1 (hypothesis inventory).** The proof uses: tautness (only in
T2), \(C_4\)-freeness (T1 and the forced 4-cycles in T7/T8), non-terminal
degrees \(\ge3\), terminal degrees \(\ge1\), and \(S\subseteq\{3,4,5\}\)
read as "\(d(a,b)\ge3\) and no simple \(a\)–\(b\) path of length \(\ge6\)".
Power-freeness beyond \(C_4\) is not used; neither is (D)'s clause
\(\deg(a)+\deg(b)\ge3\). Equivalent form: **every vertex-taut
\(C_4\)-free two-terminal graph with \(d(a,b)\ge3\), non-terminal degrees
\(\ge3\), and terminal degrees \(\ge1\) has a simple \(a\)–\(b\) path of
length \(\ge6\)** — at \(s_{\min}=3\) this is exactly the taut
spread-doubling inequality \(s_{\max}\ge2\,s_{\min}\) of `L025` R5(b).

**Remark T8.2 (sharpness).** \(K_{3,3}-e\) (terminals the two degree-2
vertices) is vertex-taut, satisfies (D), and has \(S=\{3,5\}\); it is
excluded exactly by its 4-cycles (`E011` anchor A1). So \(C_4\)-freeness
cannot be dropped. Tautness cannot be dropped: by `L026`, unrestricted
pinched gadgets at small \(s_{\min}\) exist iff counterexamples to 0.1
exist, so a tautness-free version of T8 would already prove statement 0.1.
The bound \(5\) cannot be replaced by \(7\) without new ideas — the proof's
exhibits are length-\(6\) and length-\(7\) paths. And by `C028` the
\(C_4\)-only statement is **false** at \(s_{\min}=6\): five taut
\(C_4\)-free pinched witnesses with \(S=\{6,\dots,11\}\) exist at orders
12–13, each containing a \(C_8\). So the \(C_4\)-only regime of the taut
ladder ends within \(s_{\min}\in\{4,5,6\}\).

### Corollaries

**C1 (the rung).** No taut 2-atom has \(s_{\min}=3\); more generally none
has \(s_{\max}\le5\). With `L028`: **every taut 2-atom has
\(s_{\min}\ge4\) and \(s_{\max}\ge6\)**.

*Proof.* A 2-atom is power-free (hence \(C_4\)-free) and satisfies (D). If
taut with \(s_{\min}=3\): pinching gives \(s_{\max}<6\), so
\(S\subseteq\{3,4,5\}\), contradicting T8. If taut with \(s_{\max}\le5\):
\(s_{\min}\le2\) contradicts `L028`, and \(s_{\min}\ge3\) contradicts T8.
So (`L028` + T8) \(s_{\min}\ge4\); then \(d(a,b)\ge3\), and T8 forces
\(s_{\max}\ge6\). ∎

**C2 (non-taut routing and order bound).** Every 2-atom with
\(s_{\min}=3\) is non-taut, hence by `L027` contains a 1-atom or a
power-free graph of minimum degree \(\ge3\); consequently it has order
\(\ge19\).

*Proof.* Non-tautness is C1; `L027` supplies the alternative for the lobe
\(L\), which meets the essential set only in its attachment \(c\). A 1-atom
has order \(\ge16\) (`C027`) and a min-degree-3 power-free graph order
\(\ge19\) (`L022`), so \(|V(L)|\ge16\). The essential set contains the four
distinct vertices \(a,x,z,b\) of a length-3 \(a\)–\(b\) path, and at least
three of them lie outside \(V(L)\). Hence \(|V(H)|\ge16+3=19\). ∎

**C3 (ladder status).** With `L028`, C1, C2: every 2-atom with
\(s_{\min}\le3\) contains a 1-atom or a min-degree-3 power-free graph, so
the assembly disproof channel below \(s_{\min}=4\) routes entirely through
the 1-atom question or an outright counterexample. The live taut rungs are
\(s_{\min}\in\{4,5\}\) (targets empty through order 13, `C028`) and
\(s_{\min}=6\), where \(C_4\)-only closure is impossible (Remark T8.2) and
all five known witnesses contain a \(C_8\) — the first place the power
spectrum itself provably must carry the argument.

## Plan and decisive tests

1. **Failure-first construction attempt (executed; became the proof):**
   build a taut \(C_4\)-free gadget with \(S\subseteq\{3,4,5\}\) from the
   constraint structure. Every degree of freedom closed; the forced moves
   are exactly T1–T8. No construction survives.
2. **Computational falsification (`E012`):** the theorem predicts that no
   terminal pair of any connected \(C_4\)-free graph in the `E010` stream
   class forms a taut (D)-gadget with \(S\subseteq\{3,4,5\}\) — including
   pairs with both terminal degrees \(\ge3\), which `E011`/`C028` never
   examined. Checked exhaustively at orders 6–14; the T8 endgame dichotomy
   checked on all three-matchings structures at \(k\in\{2,4\}\);
   \(K_{3,3}-e\) as positive control for the detector. See `E012`/`C029`.
3. Pivot condition: a construction satisfying all constraints at any stage
   — none materialized; the structure died at T8's dichotomy.

## Failure analysis

None required: the inherited route succeeded, though not in the predicted
shape — S012 expected the power spectrum to carry \(s_{\min}=3\); instead
\(C_4\)-freeness does, and the genuine power-spectrum fight relocates to
\(s_{\min}\in\{4,5,6\}\) with `C028`'s witnesses pinning the upper end.

## Salvageable results

All of T1–T8 and C1–C3 stand and are promoted (`L030`). The middle-layer
collapse pattern (position analysis → class elimination → matching rigidity
→ endgame dichotomy) is the candidate mechanism for the \(s_{\min}=4\)
rung, where middles can sit two steps deep on both sides and the position
analysis gains genuinely new cases.

## Exit state

- Status: closed (results promoted)
- Promoted records: `L030` (T8 + C1–C3), experiment `E012`, observation
  `C029`; `G013` refined.
- Next action: attack the taut \(s_{\min}=4\) rung — prove no taut
  \(C_4\)-free (D)-gadget has \(S\subseteq\{4,5,6,7\}\), or find a
  \(C_4\)-free taut pinched gadget with \(s_{\min}\in\{4,5\}\) at orders
  14–16. Alternatives: direct \(C_8\)-forcing at the \(s_{\min}=6\)
  witnesses; 1-atom structure theory; order-16 census (deferred).
