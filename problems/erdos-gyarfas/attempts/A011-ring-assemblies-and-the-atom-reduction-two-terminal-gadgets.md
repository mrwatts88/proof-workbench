# A011 — Ring assemblies and the atom reduction: two-terminal gadgets against the power spectrum

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: active
- Portfolio role: primary (reframing of the walk-to-cycle interface) + live falsification channel

## Intended mechanism

The S010 handoff asked for a walk-to-cycle transfer lemma: convert the
unconditional balanced-walk intervals of `L024` into forced cycle lengths.
Formulation immediately met the recorded kill test. The Bondy–Vince ring
(`C024`; their Figure 1) shows that 2-connected minimum-degree-3 graphs can
have cycle spectra with multiplicative gaps of unbounded ratio, while `L024`
(trivial group) still forces closed nb walks at every admissible length past a
threshold in those same graphs. Hence **no unconditional bounded
walk-to-cycle transfer exists**, and the true question is which transfer
survives the power-freeness hypothesis.

This attempt makes that question exact. Rings of two-terminal gadgets
("atoms") turn out to reduce a *disproof* of statement 0.1 to a finite object:
one power-free gadget whose terminal-to-terminal path lengths are confined to
a window of multiplicative ratio below 2. Contrapositively, if the conjecture
is true, every power-free near-minimum-degree-3 gadget must exhibit
**path-length spread doubling** — the sharp, falsifiable form of
"walk-to-cycle." The mechanism gap against `L024` is clean: closed nb walks
can revisit vertices, so their length spectrum can never be pinched (that is
the collision-wall theorem); simple paths pay geography, and the conjecture is
equivalent to geography being expensive enough.

## Entry assumptions

Statement 0.1 exactly as in `STATEMENT.md`. All graphs finite and simple.
"Power-free" means: no cycle has length \(2^k\), \(k\ge2\). No conditional
claims are consumed; `C024` (Bondy–Vince) is imported at the strength recorded
in `references/source-audit-2026-07-24-S011.md`.

## Targeted obligations

- `G007`: the global mechanism — reformulated here as the spread-doubling
  necessary condition.
- `G013` (opened this session): the atom question.

## Definitions

**D-A1 (two-terminal graph).** A two-terminal graph is a triple \((H,a,b)\)
with \(H\) a finite simple connected graph and \(a\ne b\) distinguished
vertices (terminals). Its through-set is
\(S=S(H,a,b)=\{\,\ell(P): P\ \text{a simple } a\text{–}b\ \text{path}\,\}\)
(lengths in edges). Write \(s_{\min}=\min S\), \(s_{\max}=\max S\) when
\(S\ne\emptyset\) (connectivity gives \(S\ne\emptyset\)).

**D-A2 (degree condition).** \((H,a,b)\) satisfies condition (D) when every
vertex of \(V(H)\setminus\{a,b\}\) has \(\deg_H\ge3\), while
\(\deg_H(a),\deg_H(b)\ge1\) and \(\deg_H(a)+\deg_H(b)\ge3\).

**D-A3 (2-atom).** A 2-atom is a two-terminal graph satisfying (D) whose
cycle spectrum is power-free and whose through-set satisfies
\(s_{\max}<2\,s_{\min}\).

**D-A4 (1-atom).** A 1-atom is a finite simple connected power-free graph
with exactly one vertex of degree less than 3, that vertex having degree 1 or
2 and all others degree \(\ge3\).

**D-A5 (ring).** For a two-terminal graph \((H,a,b)\) and \(L\ge3\), the ring
\(R_L(H,a,b)\) is built from \(L\) disjoint copies \(H_1,\dots,H_L\) by
identifying \(b_i\) with \(a_{i+1}\) (indices mod \(L\)). Call the identified
vertices \(m_1,\dots,m_L\) (gateways, \(m_i=b_i=a_{i+1}\)) and
\(I_i=V(H_i)\setminus\{m_{i-1},m_i\}\) the interiors.

## Deductions

**R1 (ring structure lemma) — proved.** Let \((H,a,b)\) satisfy (D) and let
\(L\ge3\). Then:

1. \(R_L\) is a finite simple graph and \(\delta(R_L)\ge3\).
2. \(\mathrm{Spec}(R_L)=\mathrm{Spec}(H)\cup\Sigma_L\), where
   \(\Sigma_L=\{\,s_1+\dots+s_L:\ s_i\in S\ \text{for all } i\,\}\cap
   \{\text{realizable sums}\}\subseteq[L\,s_{\min},\,L\,s_{\max}]\), and
   \(\Sigma_L\supseteq\{L\,s:\ s\in S\}\ne\emptyset\).

*Proof.* (1) Distinct copies share only gateway vertices, so the only
candidate for a repeated edge is an \(ab\)-edge of \(H\) appearing from two
copies on the same vertex pair; that requires \(m_{i-1}\) and \(m_i\) to
coincide with \(m_{j-1},m_j\) for \(j\ne i\), impossible for \(L\ge3\). So
\(R_L\) is simple. Degrees: an interior vertex keeps its \(H\)-degree
\(\ge3\); a gateway has degree \(\deg_H(b)+\deg_H(a)\ge3\) by (D).

(2) Every edge of \(R_L\) lies inside exactly one copy, and
\(H_i\cap H_j\subseteq\{m_1,\dots,m_L\}\) with
\(H_i\cap H_{i+1}=\{m_i\}\) and \(H_i\cap H_j=\emptyset\) for
\(j\notin\{i-1,i,i+1\}\) (\(L\ge3\)).

\(\supseteq\): a cycle of \(H_i\) is a cycle of \(R_L\); and for any choice
\(s_i\in S\) with witness paths \(P_i\subseteq H_i\), consecutive witnesses
share exactly their common gateway, so \(P_1\cup\dots\cup P_L\) is a cycle of
length \(\sum s_i\); taking all \(s_i\) equal realizes \(Ls\).

\(\subseteq\): let \(C\) be a cycle of \(R_L\). If \(V(C)\) lies in one copy
\(H_i\), then \(C\) is a cycle of \(H\) (possibly through \(a\) or \(b\) or
both), so \(\ell(C)\in\mathrm{Spec}(H)\). Otherwise \(C\) meets two copies.
Walking along \(C\), a maximal segment inside a copy \(H_i\) is a nontrivial
path whose two endpoints are vertices where \(C\) changes copy; a change of
copy can occur only at a vertex lying in two copies, i.e. at a gateway, and
the gateway \(m_i\) is the unique common vertex of \(H_i\) and \(H_{i+1}\).
Since \(C\) is a simple cycle it visits each gateway at most once, so each
transition \(H_i\leftrightarrow H_{i+1}\) occurs at most once. Contracting
each copy to a vertex maps \(C\) to a closed trail in the cycle graph
\(C_L\); the only nonempty closed trail in \(C_L\) is \(C_L\) itself. Hence
\(C\) crosses every gateway exactly once and, for every \(i\), the segment
\(C\cap H_i\) is a simple \(m_{i-1}\)–\(m_i\) path, i.e. a simple \(a\)–\(b\)
path of \(H\) of some length \(s_i\in S\) (an \(ab\)-edge of \(H\), if
present, is the case \(s_i=1\)). Therefore
\(\ell(C)=\sum_{i=1}^{L}s_i\in\Sigma_L\). ∎

**R2 (dyadic placement) — proved.** If \(s_{\max}<2\,s_{\min}\), then for
every \(k\) with \(2^k>\dfrac{s_{\min}\,s_{\max}}{2\,s_{\min}-s_{\max}}\) and
\(2^k\ge3\,s_{\min}\), the integer \(L=\lfloor 2^k/s_{\min}\rfloor+1\)
satisfies \(L\ge3\) and
\[
  2^k \;<\; L\,s_{\min}\;\le\; L\,s_{\max}\;<\;2^{k+1}.
\]

*Proof.* \(L\,s_{\min}\in(2^k,\,2^k+s_{\min}]\) by choice of \(L\), giving the
left inequality and \(L\ge 2^k/s_{\min}\ge3\). For the right inequality,
\(L\,s_{\max}\le(2^k+s_{\min})\dfrac{s_{\max}}{s_{\min}}<2^{k+1}\) is
equivalent to \(s_{\max}\,s_{\min}<2^k(2\,s_{\min}-s_{\max})\), which is the
assumed bound on \(2^k\) (the denominator is positive precisely because
\(s_{\max}<2\,s_{\min}\)). ∎

**R3 (2-atom reduction) — proved.** If a 2-atom exists, statement 0.1 is
false. *Proof.* Take \(k\) as in R2 and \(L\) accordingly. By R1,
\(R_L\) is a finite simple graph with \(\delta\ge3\) and
\(\mathrm{Spec}(R_L)=\mathrm{Spec}(H)\cup\Sigma_L\). \(\mathrm{Spec}(H)\)
contains no power of two by hypothesis, and
\(\Sigma_L\subseteq[L\,s_{\min},L\,s_{\max}]\subseteq(2^k,2^{k+1})\) contains
no power of two by R2. So \(R_L\) is a counterexample. ∎

**R4 (1-atom reduction) — proved.** If a 1-atom \(B\) with exceptional vertex
\(u\) exists, statement 0.1 is false. *Proof.* If \(\deg(u)=2\): take two
disjoint copies of \(B\) and add the edge \(u_1u_2\). Every degree is \(\ge3\)
(\(u_i\) reaches 3, others unchanged). The new edge is a bridge, so it lies on
no cycle, and \(\mathrm{Spec}=\mathrm{Spec}(B)\) is power-free: a
counterexample of order \(2|B|\). If \(\deg(u)=1\): take three disjoint
copies and add the triangle \(u_1u_2,u_2u_3,u_3u_1\). Degrees: \(u_i\) has
\(1+2=3\), others \(\ge3\). A cycle meeting an interior \(V(B_i)\setminus
\{u_i\}\) can leave copy \(i\) only through \(u_i\), and a simple cycle
cannot pass \(u_i\) twice, so every cycle either lies in one copy
(power-free) or has all vertices in \(\{u_1,u_2,u_3\}\) (the new triangle,
length 3). A counterexample of order \(3|B|\). ∎

**R5 (necessary conditions; the sharp walk-to-cycle form) — proved, as the
contrapositive of R3–R4.** If statement 0.1 is true, then:

- (a) no power-free connected graph has exactly one vertex of degree
  less than 3 (of degree 1 or 2), all others of degree \(\ge3\); and
- (b) **spread-doubling:** every two-terminal graph \((H,a,b)\) satisfying
  (D) whose spectrum is power-free has \(s_{\max}\ge2\,s_{\min}\).

Neither implication reverses on its face: a minimal counterexample has no
degree-2 vertex, so deleting an edge from it produces two-terminal graphs but
with no control on the through-ratio. R5 is a *necessary* condition — a test
any proof of 0.1 must pass, and a live disproof channel while unresolved.

**R6 (context facts).** By `C024` (Bondy–Vince Theorem 1), every atom
candidate — having at most two vertices of degree \(<3\) — contains two
cycles whose lengths differ by one or two; so atom spectra always contain a
near-consecutive pair (e.g. \(\{5,6\}\) or \(\{5,7\}\)), which power-freeness
tolerates. The Bondy–Vince gadget \(K_{3,3}-e\) satisfies (D) with
\(S=\{3,5\}\), ratio \(5/3<2\), and fails to be a 2-atom only because its
spectrum \(\{4,6\}\) contains \(C_4\): the entire distance between the 1998
ring and a disproof of 0.1 is the power-freeness of one gadget.

## Relation to L024 and the reframed transfer target

`L024` (trivial group) forces tailless nb closed *walks* at every admissible
length past a per-base threshold — walk-length spread is unlimited,
unconditionally. R5(b) says the conjecture is exactly a *pinching
impossibility* for simple-path lengths: power-freeness must force
\(s_{\max}/s_{\min}\ge2\) at every two-terminal decomposition. The proof-side
program for `G007` is therefore: find the mechanism by which forbidden
\(C_4/C_8/\dots\) forces long detours (ear and saturation structure,
`L011`–`L013`, are the natural levers: an ear on an odd cycle is a rerouting
device that spreads path lengths). The failure-first data is the atom search
`E010`: either an atom appears (disproof protocol starts) or the observed
minimum through-ratio over power-free two-terminal graphs, order by order,
shows how spread grows and what blocks it.

## Plan and decisive tests

1. `E010` search A (decisive, cheap): enumerate connected \(\{C_4,C_8\}\)-free
   graphs with minimum degree \(\ge2\) and at most two sub-cubic vertices,
   orders up to the feasible frontier (\(\approx15\)). Any member with at most
   one degree-2 vertex is a 1-atom or an outright counterexample — statement
   0.1 would be **false** (R4). Expected on current evidence: empty; the empty
   result is itself a new finite exclusion (the class is not covered by
   `E004`/`E006`/`C023`, which all required minimum degree 3).
2. `E010` search B: for survivors with exactly two degree-2 vertices, take
   them as terminals and test the 2-atom ratio \(s_{\max}<2\,s_{\min}\) (R3).
   Record the minimum ratio per order even when \(\ge2\).
3. Anchors: \(K_{3,3}-e\) must report \(S=\{3,5\}\), spectrum \(\{4,6\}\); the
   \(L=3\) Bondy–Vince ring must report spectrum \(\{4,6,9,11,13,15\}\)
   exactly (`C024`'s quoted figure); pipeline re-run with a minimum-degree-3
   filter must reproduce the recorded `E004`/`E006` census counts.
4. Pivot conditions: an atom found → switch the dossier to disproof mode and
   run the counterexample review protocol on the assembled ring. All orders
   empty with ratios bounded well above 2 → the spread-doubling lemma R5(b)
   becomes the primary proof target, with the empirical ratio profile as its
   quantitative guide.

## Failure analysis

(open)

## Salvageable results

R1–R5 stand independently of the search outcome. The naive unconditional
transfer target is retired permanently (Bondy–Vince ring + `L024`), which is
recorded as the reason the walk-to-cycle interface must consume
power-freeness.

## Exit state

- Status: active
- Promoted records: R1–R5 promoted as `L025` (see `CLAIMS.md`); sweep imports
  `C024`–`C026`; new obligation `G013`.
- Next action: run `E010`; then attack R5(b) or the found atom, per the pivot
  conditions above.
