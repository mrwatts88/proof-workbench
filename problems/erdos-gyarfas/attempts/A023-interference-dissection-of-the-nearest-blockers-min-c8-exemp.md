# A023 — Interference dissection of the nearest blockers: min-C8 exemplars and the C16 boundary

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: active
- Portfolio role: primary (Tier 1, `G015` case (5b), proof side; session
  S022, worker leg W1)

## Intended mechanism

The case-(5b) residual object (`A019`/`L042`) is, below order 36, a
2-connected vertex-taut member of the class \(\mathcal G\) (`L039`:
connected, \(C_4\)-free, exactly two degree-2 vertices \(a,b\), all
other degrees \(\ge3\), power-free, \(S(H,a,b)\cap(\mathbb
P-2)=\emptyset\)). Two proof routes against it are already dead with
recorded reasons: congruence arithmetic (`A021`/`C037` — parity is the
ceiling of chain-calculus information; the forced memberships are
realizable from order 10), and confinement machinery (`A019` W1-T15 —
every taut-ladder lemma consumes an \(s_{\max}\) window the object does
not have). What survives (`STATE.md` S021) is the **interference
structure of the blocking cycles themselves**: in the pinched world the
census is perfect — every \(C_8\) of every equality block and witness
is the symmetric difference of two through-paths (`C031`/`C032`/`C035`,
23/23 at the blocks) — and `A021` T4 states that the discriminating
layer for case (5b) is exactly this \(C_8\)-interference/confinement
structure, never residue arithmetic.

The mechanism this attempt probes: **in the two-degree-2 \(C_4\)-free
vertex-taut world, is every power-blocker an interference cycle** — an
exact two-through-path symmetric difference? If yes at the frontier
(the closest known objects to the target profile), the model "the
power spectrum of the residual object is visible inside its own
through-path system" survives its cheapest kill test, and the
exclusion-shaped lemma it supports converts \(C_8/C_{16}\)-freeness of
\(H\) into a statement **in the same calculus as the forced
\(S\)-arithmetic** — the bridge both dead routes lacked. If no — a
non-interference blocker exists at the boundary — a recorded pivot
trigger fires (`STATE.md`), the pinched-world model breaks at a named
graph, and the proof side must redirect; that outcome is a positive
finding and is analysed at full strength.

The two families dissected (the data was already on disk or one stream
re-run away):

1. the minimum-\(C_8\)-count members of the `E018` profile class at
   orders 14–16 (recorded minima 1/2/1 — one or two \(C_8\)s from
   being tight-1-atom reducts), re-extracted with `E018`'s anchored
   primitives because `E018` recorded only the statistic;
2. the three-degree-2 boundary graphs of the \(\{C_4,C_8\}\)-free
   class at orders 16–17 (`E019` spotcheck data; 4 + 12 graphs, all
   \(C_8\)-free and \(C_{16}\)-blocked — the only place in the dossier
   where \(C_{16}\) is decisive), read against all three terminal-pair
   choices.

## Entry assumptions

Statement 0.1 verbatim; D-A1–D-A5; tightness per `A018` T2. Consumed
at recorded strength: `L039`–`L042` (the class \(\mathcal G\), the
case analysis, the residual object), `L043`–`L046` (chain case:
2-connected branch is the whole case below order 36), `C031`, `C032`,
`C035` (the pinched interference census and its exact predicate),
`C036`/`C039` (class emptiness through 17; the boundary data),
`C037`/`A021` (the Petersen\(-e\) calibration discipline binding every
case-(5b) exclusion argument). The dissection itself drops
power-freeness — its objects are blocked by construction; it measures
the *structure of the blockers*, not the existence of survivors.

## Targeted obligations

- `G015`: exclude case (5b) — the interference lever is the named
  surviving proof-side move (`STATE.md` Tier 1 live move (i)).
- `G013`(a): structure theory for the tight-1-atom question.

## Plan and decisive tests

1. **Anchor the dissection code on the recorded census** before running
   it on anything new: reproduce `E013`'s verdicts on all five equality
   blocks (P10 = Petersen\(-e\), A11, B11, C12, D14) — 23/23
   \(C_8\)s decomposable with the exact recorded length/overlap
   combinations. If the anchors do not reproduce, stop.
2. **The dissection.** Per graph and per blocking cycle, decide the
   E013-semantics predicate (∃ two simple \(a\)–\(b\) paths with edge
   symmetric difference exactly the cycle), stratified by
   terminal-usage (both / exactly one / neither — "both" is trivially
   decomposable via its two arcs, so the informative content is in the
   other two strata). Family (2) is tested for all three degree-2
   pairs; a blocker counts as non-interference only if no pair
   decomposes it.
3. **Decisive outcomes.** (a) All blockers decomposable → the
   interference model survives; record the candidate lemma, what its
   proof needs, its calibration on Petersen\(-e\), and the falsifiable
   next step. (b) A non-interference blocker → pivot trigger fires;
   record the exemplar in full detail and what exactly breaks.
4. Vertex-tautness of every family-(1) exemplar (the `E018`/`mod4.py`
   essential-vertex instrument), because tautness is the hypothesis the
   candidate lemma would consume; it was generic (\(\ge98.9\%\)) in the
   class at orders 10–13 and must be checked at the exemplars.

## Deductions

Deductions carry `A023` T-numbers (worker W1 of `S022`); ledger IDs are
the orchestrator's to assign. Each is labelled **computed** (with its
exhaustive scope), **proved** (with proof), or **conjecture**
(speculation, labelled as such). Notation as in `A019`: \(H\) a graph
with terminals \(a\ne b\); a cycle \(C\) (as an edge set) of \(H\) is an
**interference cycle** for \((H,a,b)\) iff there are two distinct simple
\(a\)–\(b\) paths \(P,Q\) with \(E(C)=E(P)\,\triangle\,E(Q)\) (`E013`'s
recorded census predicate, matched exactly — `E021` reproduces the
`E013` block census, including the combos multiplicity dictionaries,
before touching anything new).

### T1 (the frontier dissection verdict) — computed

**Extraction (exhaustive at orders 14–16).** Over `E018`'s exact stream
(totals 1,706,820 / 20,629,645 / 346,573,602, asserted equal to the
records), the profile class (connected, \(C_4\)-free, exactly two
degree-2 vertices, rest \(\ge3\); sizes 130,461 / 1,826,839 /
29,713,305, asserted) has minimum \(C_8\) count **1 / 2 / 1** (asserted
= `C036`), and the complete lists of members with \(\le3\) \(C_8\)s are
**11 / 20 / 103** graphs (histogram low ends 1:1; 2:3,3:17; 1:3, 2:6,
3:94). No \(C_8\)-free member exists at these orders (re-verified).

**Dissection (descriptive, these 134 + 16 named graphs).**

- Family (1): all **385** blocking \(C_8\)s of all 134 exemplars are
  interference cycles. Strata (both/one/neither terminals): 0/6/25 at
  14, 0/5/52 at 15, 5/71/221 at 16 — 380 of 385 lie in the informative
  strata, so the verdict is not arc-driven. Every exemplar is
  **vertex-taut**; 132/134 are 2-connected; 0/134 bipartite.
- Family (2): all **168** blocking \(C_{16}\)s of the sixteen
  three-degree-2 boundary graphs (orders 16–17, `E019` spotcheck data,
  re-verified spectra) are interference cycles **for every one of the
  three terminal pairs** (504 readings; the 84 informative one-terminal
  readings, all at order 17, each decompose in 7–40 ways; "neither" is
  order-impossible for a \(C_{16}\) at \(n\le17\)). All sixteen graphs
  are vertex-taut for all three pairs.
- Calibration family: the five `E013` blocks reproduce their recorded
  census exactly (23/23; strata 2/15/6).

**No non-interference blocker exists at the frontier.** The recorded
pivot trigger ("a non-interference blocking \(C_8/C_{16}\) among the
boundary exemplars") did **not** fire.

Arithmetic of the decompositions (family 1, all 18,299 decomposing
pair-incidences): every one satisfies \(x+y-2s=8\) exactly
(\(x,y\) the path lengths, \(s\) the shared edge count); \(y-x\in
\{0,2,4,6\}\); \(s\in[0,11]\) with mode 7; only **5** incidences have
\(s=0\). The disjoint-union mechanism (`L033`'s band-4 shape) is a
measure-zero corner of the interference phenomenon; the generic
decomposition is a heavy-overlap **window reroute** (two paths sharing
a long trunk and splitting around the blocker), and pairs with
\(x=y\) — invisible to the length set \(S\) — carry a large share.

### T2 (interference cycles are confined to the essential subgraph) — proved

**Claim.** If \(C=E(P)\triangle E(Q)\) for simple \(a\)–\(b\) paths
\(P,Q\), then every edge of \(C\) lies on a simple \(a\)–\(b\) path,
and hence so does every vertex of \(C\).

*Proof.* Each edge of \(E(P)\triangle E(Q)\) belongs to \(E(P)\) or
\(E(Q)\); \(P\) and \(Q\) are simple \(a\)–\(b\) paths. A vertex of
\(C\) is an endpoint of an edge of \(C\). ∎

**Consequences.** (i) Vertex-tautness (indeed edge-essentiality on
cycles) is **necessary** for interference-completeness whenever some
cycle leaves the essential subgraph — this is why the `E021` control
data behaves as it does (every one of the 20 non-taut profile members
at orders 11–12 has a non-decomposable cycle; 1,148 of their 1,168
cycles fail). (ii) In the 553 dissected frontier blockers, every
blocker edge is essential — a recorded structural fact extending
`C031`'s "no inessential edges in the catalogue" to the frontier
families.

### T3 (the trivial stratum) — proved

**Claim.** A cycle through both terminals is always an interference
cycle: its two \(a\)–\(b\) arcs are internally disjoint simple paths
with symmetric difference the cycle.

*Proof.* A simple cycle visits \(a\) and \(b\) once each, splitting
into two arcs, each a simple \(a\)–\(b\) path with \(\ge1\) edge; they
are edge-disjoint, so their symmetric difference is their union, the
cycle. ∎ (Asserted by the `E021` engine on every stratum-"both"
blocker; this is why the strata are reported separately — the recorded
pinched census convention counts all blockers, and `E021` shows only
2 of the 23 pinched-block \(C_8\)s and 5 of the 385 family-(1)
\(C_8\)s were of this trivial type.)

### T4 (the t = 1 reading: interference is the leak-free case of the chain calculus) — proved

**Claim.** Let \(P,Q\) be distinct simple \(a\)–\(b\) paths of \(H\).
`A021` T1 gives \(E(P)\triangle E(Q)=C_1\sqcup\dots\sqcup C_t\)
(edge-disjoint cycles, \(t\ge1\)) with
\(\ell(P)+\ell(Q)=2|E(P)\cap E(Q)|+\sum_i\ell(C_i)\). Then:

1. each \(C_i\) is a cycle of \(H\), so every single-cycle symmetric
   difference length lies in \(\mathrm{Spec}(H)\): writing
   \(T_1(H,a,b)=\{\ell(C):C\ \text{an interference cycle}\}\), always
   \(T_1(H,a,b)\subseteq\mathrm{Spec}(H)\);
2. an interference cycle is exactly the case \(t=1\), where the
   identity collapses to \(\ell(C)=\ell(P)+\ell(Q)-2|E(P)\cap E(Q)|\)
   with **no residual ambiguity** — the "leak term" of `A021` T1 is
   fully determined by the witnessing pair;
3. if interference-completeness holds for \((H,a,b)\) (every cycle of
   \(H\) is an interference cycle — T5's conjectured conclusion), then
   \(\mathrm{Spec}(H)=T_1(H,a,b)\), and for the case-(5b) closure
   \(B=H+u\) (`A019` W1-T1(1)):
   \[\mathrm{Spec}(B)=T_1(H,a,b)\ \cup\ (S+2),\qquad S=S(H,a,b),\]
   so **the entire power-freeness of the tight 1-atom becomes a
   statement about the through-path system alone**:
   \(T_1\cap\{4,8,16,32,\dots\}=\emptyset\) and
   \(S\cap(\mathbb P-2)=\emptyset\).

*Proof.* (1) A member of an edge-disjoint cycle decomposition of a
subgraph of \(H\) is a cycle of \(H\); the containment follows from the
definition of \(T_1\). (2) is the \(t=1\) case of the displayed
identity. (3) The forward inclusion of
\(\mathrm{Spec}(H)\subseteq T_1\) is the completeness hypothesis; the
reverse is (1); the closure identity is `A019` W1-T1(1). ∎

**Reading — why interference blockers are exactly what vertex-tautness
plus the \(S\)-condition could fight.** The two recorded kill theorems
delimit every surviving case-(5b) route: congruence information caps at
parity because the leak term \(2|E(P)\cap E(Q)|\) is uncontrolled
*modulo anything* (`A021` T1/`C037`), and membership arithmetic alone
can never exclude the chain case (`L045`, whose corollary names
"through-set realizability or \(C_8\)-interference structure" as the
only levers left). The interference calculus uses the same identity the
congruence route died on, but at \(t=1\) **exactly**, as a realization
statement, not a residue statement — the leak is not reduced away, it
is *pinned* by the witnessing pair. Under completeness (T5), the
spectrum side (where power-freeness lives) and the through-set side
(where the forced memberships \(S\cap\mathbb P\ne\emptyset\),
\(S\cap(\mathbb P-1)\ne\emptyset\), \(S\cap(\mathbb P-2)=\emptyset\)
live, `A019` W1-T10 under (R)) become **one calculus on one object**,
the through-path system — which is precisely the object vertex-tautness
constrains (every vertex carries through-traffic) and the object the
\(S\)-condition constrains (its length shadow). A non-interference
blocker would have been a cycle invisible to that object — a phenomenon
the \(S\)-arithmetic could never touch, reopening the category mismatch
of `A019` W1-T15 inside the last surviving route. T1 says no such
blocker exists anywhere we can currently see.

### T5 (candidate lemma: interference-completeness of vertex-taut pairs) — conjecture

> **Candidate lemma (speculation, labelled as such).** Let \((H,a,b)\)
> be vertex-taut: every vertex of \(H\) lies on a simple \(a\)–\(b\)
> path. Then **every cycle of \(H\) is an interference cycle** — the
> symmetric difference of two simple \(a\)–\(b\) paths.

Stated in the general two-terminal setting deliberately: the evidence
supports no side conditions.

**Evidence inventory (all `E021`, exact scopes).**

- Exhaustive over **all connected graphs of orders 4–7 and all
  vertex-taut pairs** (no degree condition, no \(C_4\)-freeness):
  12,313 taut pairs, 723,926 (pair, cycle) instances, **zero
  failures** (`tautgeneral`).
- Exhaustive over the two-degree-2 \(C_4\)-free profile class at
  orders 10–12, power-freeness dropped: all 108,882 cycles of all
  1,266 vertex-taut members decompose; and the biconditional is exact
  on the sample — all 20 non-taut members fail (`smallworld`), with
  the failure direction *proved* by T2.
- The frontier families: 385 + 168 blockers, all vertex-taut objects,
  all decomposable (T1); the five pinched blocks, 23/23 (`C031`
  reproved).

**What a proof would need.** T3 settles cycles through both terminals.
For the rest, the natural mechanism is the **clean-window reroute**:
if some \(a\)–\(b\) path \(P\) meets \(C\) in exactly one arc \(A_1\)
(edge-wise and vertex-wise), then \(Q=P\triangle C\) is again a simple
\(a\)–\(b\) path and \(P\triangle Q=C\); similarly two paths that agree
outside \(C\) and take complementary arcs work. So the lemma reduces
to: *vertex-tautness forces, for every cycle \(C\), a through-path
whose trace on \(C\) is clean* (one arc, or a two-contact detour). The
obstruction a proof must control is **weaving** — every through-path
meeting \(C\) in several disconnected pieces. Two sub-obligations a
proof will have to produce en route: (a) every edge of every cycle is
essential in a taut pair (needed by T2's converse; empirically true in
all scanned instances), and (b) a reroute-selection argument (choose
\(P\) through a fixed edge of \(C\) minimizing \(|E(P)\setminus
E(C)|\) or the number of contact intervals, and show a minimal choice
is clean — an exchange argument in the spirit of the `L033` proofs,
but band-free). Nothing in the dissection proves any step of this;
the lemma is a target, not a result.

**Kill tests (falsifiable, cheap first).** (i) `smallworld 13`
(10,966 members, minutes under PyPy): a single non-decomposable cycle
in a taut member kills the lemma as stated and names the missing
hypothesis. (ii) A sparse-slice general-graph probe at orders 8–9
(dense graphs are path-rich and uninformative; the weaving obstruction,
if realizable, needs sparse structure). (iii) Targeted constructions:
a long cycle attached to the through-traffic at two far-apart contact
vertices with all connecting paths forced to weave.

### T6 (the forcing program this supports, and its calibration) — analysis; the program itself is open

Under (R), the case-(5b) residual object \((H,a,b)\) is vertex-taut,
2-connected below order 36 (`L046`), of order 17–35 in the current
window (`C039`: tight 1-atoms \(\ge19\) give \(|V(H)|\ge18\)), with
forced through-set memberships (`A019` W1-T10) and power-free spectrum
— in particular **no** \(C_4/C_8/C_{16}/C_{32}\). The exclusion
mechanism the dissection supports:

> **(F) (open target, speculation).** For vertex-taut \((H,a,b)\) in
> the (5b) profile with the forced \(S\)-arithmetic, in the order
> window \([18,35]\): the through-path system always realizes a
> \(t=1\) collision at a power length — some pair of through-paths has
> symmetric difference a single cycle of length \(4\), \(8\), \(16\)
> or \(32\).

(F) plus T4(1) contradicts power-freeness of \(H\) and closes case
(5b) below order 36 — `G015` proved there, with `L046` covering the
chain side. Evidence that (F) is the *right* shape: the class data
(`C036`/`C039`: 100% of the profile class is \(C_8\)-blocked at orders
8–16 and the class is empty at 17) **plus T1** (each of those blockers
is \(t=1\)-visible) say the path system *does* always achieve the
8-collision as far as the class exists; and the \(C_{16}\)-decisive
boundary graphs achieve the 16-collision for every terminal reading.
Scope honesty: (F) must be **order-windowed** — at large order the
class contains, e.g., high-girth cubic graphs minus an edge, where no
short cycle exists at all — and the window is exactly where `L046` and
the search ladder have confined the residual object; nothing here
starts a proof of (F).

**Petersen\(-e\) calibration (`A021` discipline, binding).**
Petersen\(-e\) satisfies every hypothesis of (F) except the order
window (taut, (2,2)-profile, \(C_4\)-free, 2-connected,
\(S=\{4,5,7,8\}\) meeting \(\mathbb P\) and \(\mathbb P-1\) and
avoiding \(\mathbb P-2\)) — and (F)'s **conclusion is realized on
it**: its seven \(C_8\)s are all \(t=1\)-visible (30 decomposing pair
incidences; combos include the two disjoint 4-paths, `4+4-2*0`). The
mechanism derives its contradiction from **power-freeness** (the
spectrum side of T4(3)); Petersen\(-e\) is not power-free, so no false
exclusion occurs — exactly the consumption pattern `A021` T4 requires
of any legitimate case-(5b) argument. Minimality/(R) is consumed only
through the forced memberships (inputs to (F)); an unconditional
variant of (F) that drops them must be re-calibrated. The candidate
lemma T5 itself is not exclusion-shaped (it is a structure theorem
whose conclusion *holds* on Petersen\(-e\), 7/7) and needs no
calibration exemption.

### T7 (frontier realization data: the order-14 full-triple exemplar) — computed

Among the 134 exemplars, exactly one satisfies the full forced
membership triple of `L042` while vertex-taut:
`M?AA@?WcKWHOWOL??` (order 14, terminals (6,7), 20 edges,
\(S=\{3,\dots,13\}\setminus\{6\}\) — the through-set dodges precisely
the \(\mathbb P-2\) element in its range — spectrum
\(\{3,5,\dots,14\}\), 2-connected, non-bipartite, 52 through-paths,
exactly 3 \(C_8\)s, all stratum-neither, all interference). This is a
second Petersen\(-e\)-class calibration object, four orders further
and three \(C_8\)s from power-free: any future forcing argument (F)
must produce its collision *on this graph* (it does), and any claimed
exclusion that would also exclude this graph without invoking
power-freeness is wrong. One further exemplar
(`M?AA@AOSbO@WHOF??`, order 14, \(S=\{1,4,8,\dots,13\}\),
\(ab\in E\)) has \(S\cap(\mathbb P-2)=\emptyset\) but misses
\(\mathbb P-1\). The three order-16 minimum exemplars (single
\(C_8\), stratum neither, 30–48 decompositions each) all have
\(S\ni6,14\): at the frontier order the \(S\)-condition and the
spectrum block *simultaneously* — consistent with the unified-calculus
reading of T4.

### T8 (chain-floor corroboration) — computed

The only two exemplars with a cut vertex occur at orders 15 and 16
(both vertex-taut, both 2 \(C_8\)s); none at 14. `C038`'s chain floor
(vertex-taut with a cut vertex \(\Rightarrow\) a chain of blocks of
order \(\ge8\) each, hence order \(\ge15\)) predicts exactly this.
Independent small corroboration of `C038` from a differently-selected
sample; carries no new strength.

## Failure analysis

No route died here: the attempt was a pre-registered two-outcome probe
and the **interference outcome** occurred. The recorded pivot trigger
(non-interference blocker at the boundary) did not fire — that
negative is itself the datum: the pinched-world model survived its
cheapest kill test at the exact frontier, on 553 blockers across two
independent families, having been given every chance to fail in the
informative strata (380 + 84 readings). The residual risks, stated
plainly: T5 is a conjecture whose smallest untested rung (order-13
in-class, order-8 general sparse) could still kill it; (F) is a named
target with no proof step taken; and all frontier evidence is at
orders \(\le17\), while the residual object lives at \(\ge18\).

## Salvageable results

1. **T1** — the frontier dissection verdict and the exhaustive
   exemplar extraction (the complete \(\le3\)-\(C_8\) lists at orders
   14–16 with the count histograms; reusable as search seeds and as
   test objects for any (F)-shaped argument).
2. **T2/T3/T4** — three small proved lemmas fixing the interference
   calculus: confinement to the essential subgraph (the necessity
   direction of the tautness dichotomy), the trivial stratum, and the
   \(t=1\) reading identifying interference as the leak-free case of
   `A021` T1, with the spectrum-unification consequence T4(3).
3. **T5** — the candidate lemma, with its evidence inventory, proof
   obligations (clean-window reroute; edge-essentiality), and ordered
   kill tests. The tautness dichotomy (`E021` `smallworld` +
   `tautgeneral`) is the sharpest single fact this session adds: the
   property is exactly tautness-shaped, with necessity proved.
4. **T6** — the forcing target (F), the precise exclusion shape now on
   the table, calibrated on Petersen\(-e\) per `A021` discipline.
5. **T7** — the order-14 full-triple exemplar as a standing second
   calibration object next to Petersen\(-e\).
6. **T8** — a free corroboration of `C038`'s chain floor.

## Exit state

- Status: active (probe complete; candidate lemma and forcing target
  recorded, neither proved)
- Promoted records: experiment `E021` (extraction + dissection +
  dichotomy data); deduction rows T1–T8 offered to the orchestrator
  for ledger assignment (T1/T7/T8 computational-observation strength,
  T2/T3/T4 proved-lemma strength, T5/T6 conjecture/program strength).
- Next action (recommended, falsifiable, in order):
  1. **T5 kill rung**: `smallworld 13` (exhaustive in-class at order
     13) and a sparse order-8/9 general-graph probe; a failure names
     the missing hypothesis, survival justifies the proof attempt.
  2. **T5 proof attempt**: the clean-window reroute with a
     minimal-choice exchange argument (both sub-obligations named in
     T5).
  3. **(F)** stays the follow-on target after T5, order-windowed
     \([18,35]\); the search ladder (orders 18–20 via `E019`) runs
     unchanged in parallel and remains decisive either way.

