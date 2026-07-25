# Current state

- Last updated: 2026-07-25 (S026 — **the corpus dissection is spent:
  the dodge mechanism is extracted, two candidate mechanisms are
  killed, and the interpolation lemma splits into (L-A) ∧ (L-B) with
  a validated formal engine for the long-range half.** Over the
  9,061-row `E026` corpus vs the eight profile objects + a 556-member
  control (`E027`/`C047`, attempt `A026`): the dodge economy has
  exactly **three rigid shapes** (A: short, \(\max S=13\) walls; A′:
  distance exactly 7; B: long-range, even part \(\subseteq4\mathbb
  Z\), holes at \(\{6,10,14\}\)); the dodge is **pair-local**
  (frontier members carry five saturated sibling pairs — member-level
  lemmas dead) with the frontier at **ndeg2 = 4 at order 20** (the
  profile load-bearing by two subdivision vertices); **99.1% of dodge
  rows smooth to class-violating reduced graphs** (near-misses are
  subdivisions escaping the class constraint; the profile is the
  subdivision-free stratum). The **span law** is proved (no chord of
  span 3 or 7 on any path in a \(\{C_4,C_8\}\)-free graph) and the
  **first-order chord-exchange calculus** generates the entire top of
  \(S\) down to 10 — including 14 — on all eight profile objects
  while respecting every dodger hole: the missing tool sharpens to
  **span/savings combinatorics of longest-path chord systems**.
  Floors unchanged; `E024` (order-21 rung) still **running**,
  excluded from every ledger)
- Problem: `P-002` — Erdős–Gyárfás Conjecture

## Exact target

Every finite simple undirected graph of minimum degree at least \(3\) contains a
cycle whose length is a power of two. See normalized `STATEMENT.md` version 0.1.

## Established

- `L001`–`L006`: block and edge-minimal reductions; counterexamples have
  \(\ge11\) vertices (hand proofs).
- `L008`–`L016` saturation package with delimitations.
- `L017`/`L018`/`L022` finite exclusions: every counterexample has at
  least **nineteen** vertices; extremal \(\{C_4,C_8\}\)-free window
  \([19,24]\); census capped at order 18.
- `L019`–`L024` the voltage-lift program, closed as a theorem
  (collision wall, reviewed `R001`).
- `L025`–`L030`: atom reduction; rung completeness; lobe decomposition;
  taut rungs \(s_{\min}\le3\) closed \(C_4\)-only; cubic reduction
  modulo 1-atoms.
- `L031`–`L032`: the pendant/block reduction — taut 2-atoms exist iff a
  power-free vertex-taut 2-connected **core** with \(s_{\max}\le2s_{\min}\)
  exists (the block question).
- `L033`: the band-4 pencil dichotomy. With \(d(x,y)=4\), either two
  internally disjoint 4-paths exist (equivalently a \(C_8\) through both
  terminals) or all 4-paths share one internal vertex; no
  \(C_4\)-freeness needed, and under it the pencil is terminal-adjacent
  with a rigid fan.
- `L034`: the generalized ring criterion — a power-free (D)-gadget
  disproves 0.1 whenever **some** \(L\)-fold sumset of \(S\) avoids the
  powers of two (pinch, all-odd, odd-prime gcd, mod-4 channels).
- **New (S016): `L035`, the parity structure theorem and the bipartite
  assembly criterion.** For a vertex-taut two-terminal graph,
  parity-constancy of the through-set is **equivalent** to
  bipartiteness (all-odd = terminals in opposite colour classes). Hence
  (T3) **any** connected bipartite power-free graph with at most two
  sub-cubic vertices disproves 0.1 — no path enumeration, no tautness
  test, no external import — and (T4) bipartite generation is an
  exhaustive instrument for `L034` channels (i) and (iii), modulo the
  standing 1-atom relativization. Not valid for channel (ii): the theta
  graph \(\Theta(3,3,3)\) is vertex-taut, non-bipartite, \(S=\{3\}\).

- **New (S018): `L036`, 1-atom completeness.** A 1-atom in the recorded
  sense (unique sub-cubic vertex, of degree 1 **or** 2) exists iff a
  counterexample exists — attach one pendant vertex to a counterexample.
  So the unrestricted 1-atom question is *conjecture-complete*, `L029`'s
  "cubic reduction modulo 1-atoms" is vacuous as originally stated and
  is restated with **tight** 1-atoms (exceptional degree exactly 2),
  and `A012` Remark T4.1 is withdrawn as unproved.
- **New (S020): `C036`/`C037` — `L041`'s decisive order is empty and
  the congruence route is closed.** The order-16 \(\mathcal G\)-profile
  scan (`E018`): 346,573,602 stream graphs (24-part split, sum
  reproduced by an independent unsplit `geng -u`), 29,713,305 in the
  profile class, **every one blocked by a \(C_8\)** (\(C_{16}\) never
  decisive), zero power-free — so \(\mathcal G\) has no order-16
  member and **every tight 1-atom has order \(\ge18\)** (`C036` with
  `L041`). Proximity datum: the minimum \(C_8\) count over the class
  is **1** (the bipartite class never went below 13). The mod-4
  companion (`A021`, instrument `E018/mod4.py`): the residual object's
  forced-membership profile is *realized* by vertex-taut \(C_4\)-free
  cores from order 10 — one order-10 witness **is Petersen\(-e\)**
  (labelg-verified) — with both admissible residue patterns and no
  invariant (`C037`), and the chain-calculus identity caps
  congruence information at parity (`A021` T1: the
  \(2|E(P)\cap E(Q)|\) leak). **No congruence-type theorem at any
  modulus can exclude case (5b) from the forced hypotheses alone**;
  the surviving proof-side levers are the chain-cancellation tension
  (Minkowski-additive) and mechanisms that make power-freeness itself
  fight (the band-4 pencil is the model — it is exactly the constraint
  Petersen\(-e\) violates). Petersen\(-e\) is the standing calibration
  object: any proposed case-(5b) exclusion must fail on it unless it
  invokes power-freeness or minimality.
- **New (S021): `L043`–`L047`, `C038`–`C040` — the chain case spent,
  the instrument built, the frontier moved.** Proof side: if the
  residual object's \(H\) has a cut vertex, every prefix and suffix of
  its block chain is forced by [min]-closures to meet all three
  forbidden families and to be non-bipartite (`L043`), the cancellation
  is quantified once and for all (`L045`: three exponent-disjointness
  conditions per cut — and therefore memberships alone can **never**
  exclude the chain case), and per-block `C027`-class order bounds give
  the dichotomy: **either \(H\) is 2-connected or \(n_0\ge36\)**
  (`L046`; 32 on the `C027`+`C036`-only lineage). The chain-case
  analogue of Petersen\(-e\) does not exist over blocks of order
  \(\le14\) (`C038` — kill refuted in range, single mechanism, named
  15/16 rung open). New forced structure on every residual object:
  terminal **power** saturation (`L044`, filter strength). Search side:
  `G014` item 6 is **discharged** — `E019`'s `genc48` (geng + PREPRUNE
  \(C_8\) plugin, 146 anchors both interpreters, 23 set-equality
  checks, cubic-24 external positive control) replaces
  filter-the-stream from order 17 up (~75× cheaper at 16, ~45,000×
  smaller output). **Order 17 is empty** (`C039`): tight 1-atoms
  \(\ge19\), \(\mathcal G\)-members \(\ge18\), `C027`'s whole class
  empty through 17; at the boundary (three degree-2 vertices, orders
  16–17) \(C_{16}\) is decisive — the first time in the dossier.
  Flagged min-degree-3 sweep audited (orchestrator slice checks at 18,
  three parts, 38.7M stream graphs, all clean) and extended by the
  same-day follow-up harvest to order 20: **no
  \(\{C_4,C_8\}\)-free \(\delta\ge3\) graph through order 20**
  (`C040`), so **every counterexample has \(\ge21\) vertices**
  (`L047`, extremal window now \([21,24]\) — four orders wide). The
  same harvest emptied the bipartite class at order 24 on the new
  instrument (`C034` extended; clean through 24, 25 with a pendant).
  External input: the MathOverflow-512914 quote (user-supplied) —
  cubic-20 figures now reproduced *exactly* (510,489 / 36,101, stage
  A), its cubic→min-degree-3 step **rejected** (that inference is the
  open `G015`) and superseded by the internal stage-B run.
- **New (S022): `L048`, `C041`–`C043` — the interference lever run to
  its verdict, and the atom floors at 20.** The dissection of the
  closest known objects (the min-\(C_8\) exemplars at orders 14–16,
  exhaustively re-extracted — 11/20/103 graphs with \(\le3\)
  \(C_8\)s — and the three-degree-2 \(C_{16}\) boundary at 16–17)
  landed the **interference outcome**: all **553** blocking cycles are
  two-through-path symmetric differences, for every admissible
  terminal reading; the recorded non-interference pivot trigger did
  **not** fire (`C041`). The property is empirically **exactly
  vertex-tautness-shaped** — a complete biconditional on the profile
  class at orders 10–12, zero failures over all 12,313 vertex-taut
  pairs of all connected graphs of orders 4–7 (`C042`) — with the
  necessity direction proved: interference cycles are confined to the
  essential subgraph (`L048`(i)). `L048` fixes the calculus:
  interference is the \(t=1\), leak-**pinned** case of `A021` T1's
  identity (a realization statement — the genre that survives both
  kill theorems `C037`/`L045`), and under interference-completeness
  \(\mathrm{Spec}(B)=T_1(H,a,b)\cup(S+2)\): the tight 1-atom's entire
  power-freeness becomes through-path-system arithmetic. On the table,
  labelled: candidate lemma **T5** ("vertex-taut \(\Rightarrow\)
  interference-complete", `A023`) with ordered kill tests, and the
  order-windowed forcing target **(F)**, calibrated on Petersen\(-e\)
  **and** the new order-14 exemplar `M?AA@?WcKWHOWOL??` (full
  membership triple, 3 interference \(C_8\)s). Search side (`C043`):
  order 18 profile-empty (class 108,447); order 19 carries the
  **first-ever profile member** (class 74,589) —
  `R???C@?GC_B?@_aAA_aP?W_?BO@Gc?`, vertex-taut, 2-connected,
  non-bipartite, blocked **twice independently** (46 \(C_{16}\)s;
  \(S=\{5..18\}\ni6,14\)) — and the 0-/1-buckets are empty at both
  orders, so **every tight 1-atom and every \(\mathcal G\)-member has
  order \(\ge20\)** (direct 1-bucket route and `L041` route agree);
  \(C_{16}\) is decisive on the whole \(\le4\)-degree-2 stratum at 19.
  **Follow-up harvest (same conversation, 2026-07-25):** stage A — the
  exemplar's **full cycle set decomposes**, 411/411 across every
  length, zero failures (determined-partner algorithm, independent of
  `E021`'s pairwise) — **T5 survived the sharpest available kill
  test**; stage C — the order-19 unsplit count = 74,589 **exactly**
  (the partition follow-up is closed); stage B — **order 20 spent**:
  class 2,569,481, profile **7** (all \(C_{16}\)-blocked, none
  power-free; 0-/1-buckets empty), so **every \(\mathcal G\)-member
  has order \(\ge21\) and every tight 1-atom \(\ge22\)** (`L041`
  cases (4)/(5) propagate `L047` and the \(\mathcal G\) floor; direct
  generation certifies \(\ge21\)); the three on-disk order-20 profile
  members were fully verified and T5-tested by the orchestrator —
  **all survive** (1,890/1,890 cycles; 254 \(C_{16}\) verdicts
  re-verified pairwise), and all three repeat the \(S\ni6,14\) double
  blocking. SAVE_LIMIT caveat recorded: order-20 class files are
  per-part 200k samples (18/19 were complete). **Second harvest
  (both residual legs landed):** the part-14 recollection recovered
  the four remaining order-20 profile members (stream total 439,745
  reproduced exactly; identities in `profile_n20_part14.g6`; all
  vertex-taut, 2-connected, 65–80 \(C_{16}\)s, \(S\ni6,14\)) and
  **T5 survives on all four** (2,360/2,360) — so **all eight profile
  objects in existence survive T5** (`C042`(e), 4,661/4,661 cycles),
  every one carrying the same double blocking; and stage D
  (`followup_s022b.py`) came back **empty at order 21** — `C040`
  runs 14–21 and **`L047` lifts to 22** (window \([22,24]\), three
  orders wide; atom floors unchanged at 22/21, case (5) still
  binding).
- **New (S023): `L049`/`L050`/`C044` — T5 is a theorem; the
  interference program's gate is passed.** The two remaining
  pre-registered kill rungs ran first and survived (`C044`:
  `smallworld 13` exhaustive in-class, class 10,966 = `A021`'s count,
  all 10,853 taut members pass on 1,614,300 cycles and **all 113
  non-taut members fail** — the biconditional exact at 13; order
  \(\le8\) **exhaustive** over every graph, every vertex-taut pair,
  every cycle — 36.8M cycles at order 8 alone; cyclomatic-bounded
  slices at 9–11 clean). Then the proof (`A024`, promoted `L049`):
  **every vertex-taut pair is interference-complete** — for every
  cycle \(C\) and every prescribed edge of \(C\) there are two
  distinct through-paths in **trunk-identical arc form** with
  symmetric difference exactly \(C\) — by the **trimming
  construction**: tautness forces the block chain (block–cut tree a
  path, terminals non-cut in the end blocks); Menger's fan corollary
  plus subdivision put a through-path through any prescribed cycle
  edge (**Lemma A**: cycle-edge essentiality in taut pairs, proved);
  trimming that path at its first/last \(V(C)\)-contacts and
  completing through **both** arcs yields the pair. The recorded
  weaving obstruction never arises — the woven middle is discarded,
  not controlled. Audited `R002` (delegated fresh context): **PASS at
  lemma level**, 0 critical / 0 major, 2 minor + 6 notes, all
  repaired in place; the reviewer re-ran every `E023` command
  independently and re-verified the claim set with its own
  implementation (all labelled graphs \(\le6\); the ten named
  objects). Mechanically verified per instance (`E023
  constructive`): every step asserted on 17.4M (cycle, edge)
  instances including **all eight profile objects** (the recorded
  4,661 cycles reproduced object by object). Consequences: `L050` —
  on connected \(\delta\ge2\) graphs, interference-complete ⟺
  vertex-taut (the `C042` law is a theorem; the pinched census and
  `C041`'s 553/553 are instances); `L048`(iii) **unconditional** for
  the case-(5b) residual object (vertex-taut by `L042`):
  \(\mathrm{Spec}(H)=T_1(H,a,b)\),
  \(\mathrm{Spec}(B)=T_1(H,a,b)\cup(S+2)\) — its entire
  power-freeness is through-path arithmetic, every spectrum element
  realized by a trunk-split pair. **(F) ⟺ case (5b) empty below 36**;
  (F) is now the whole proof side there. Imports: Menger
  \(k=2\)/Whitney and block facts B1–B3, precise statements in
  `references/textbook-classics-2026-07-25.md`.
- **New (S024): `L051`/`C045` — the (F) opening probe spent, branch
  (b) taken, (F) re-aimed.** The complete trunk-split power-collision
  realization tables of the ten named objects (`E025`, anchors 45+14
  both interpreters, every recorded reference field re-verified, the
  weave control separating trunk-split from weaving pairs): none of
  the nine pre-registered membership patterns is universal; **30
  cycles across six profile objects are membership-blind outright**
  (trunk-split sets \(\{(5,13,1)\}\), \(\{(9,11,2),(10,10,2)\}\), or
  \(\{(5,11,0)\}\)); the calibration pair's 100% `has_PP` structure
  (every calibration \(C_8\) realized by two power-length paths)
  collapses to 1–8/37–112 at the frontier. **The membership-collision
  form of (F) is dead** — the empirical third leg beside `C037`
  (congruence caps at parity) and `L045` (memberships cannot exclude
  the chain case). Proved en route: **`L051`, the trunk bound** —
  every trunk-split realization has \(s=t_a+t_b\le n-L\), hence
  \(x+y\le2n-L\) (trunks live on off-cycle vertices; one paragraph
  from `L049`'s arc form) — **tight on all ten objects** (max \(s\) =
  \(n-L\) exactly: 2/6/3/4 at orders 10/14/19/20); with `L048`(iii)
  the residual object's entire collision system is order-confined
  (\(C_{32}\) at order \(\le33\): \(s\le1\)). Frontier saturation
  recorded (`A025` T3): spectra exactly \([3,n]\setminus\{4,8\}\) and
  \(S\supseteq[6,n-1]\) with \(6,14\in S\) on **all eight** profile
  objects (the double blocking, now seen as saturation); the only
  known \(\mathbb P-2\) dodges (\(S\cap\{6,14\}=\emptyset\)) are the
  calibration pair at orders 10 and 14, both gapping \(S\) exactly at
  6. **(F) = (F-S) ∨ (F-T)** (`A025` T4, both order-windowed, both
  failing off-window on the calibration pair as the discipline
  requires): (F-S) — vertex-taut (5b)-profile pairs with
  \(4,8\notin\mathrm{Spec}\) in the window force
  \(S\cap\{6,14\}\ne\emptyset\) (closure blocked via
  \(\mathrm{Spec}(B)\supseteq S+2\)); (F-T) — they force
  \(16\in\mathrm{Spec}\). Either, proved on \([18,35]\), closes case
  (5b) there (`L046` covers the chain side). Candidate mechanism:
  **saturation/interpolation** — a lower-bound theory for through-path
  length sets of taut windowed pairs (missing tool, named; `L049`'s
  block chain + `L051` are the raw material). First falsifiable move:
  the **S-gap census at the window bottom** (`A025` T5) — the
  \(\{C_4,C_8\}\)-free two-degree-2 classes are on disk at 18–20
  (`E022/data`, order 20 SAVE_LIMIT-sampled) with 21 generating
  (`E024`): per member, the \(S\)-gap structure at \(\{2,6,14\}\) and
  tautness; no taut gapped member ⟹ (F-S) survives where the residual
  object lives; a taut gapped member kills (F-S) as stated and is
  calibration object #3; the gap-vs-order curve against 10–16
  measures the mechanism either way.
- **New (S025): `C046` — the S-gap census spent; (F-S) survives; the
  saturation mechanism is profile-bound.** Over every unordered
  degree-2 pair of every on-disk class member (orders 10–19 complete;
  order 20 the per-part-complete 11/16 sample, **572,519** graphs —
  the S022 "572,530" figure counted the 11 file headers, corrected
  against the scan tallies — plus the four part-14 profile members):
  18,754,354 pairs, 767,004 members, anchors 45+57 under both
  interpreters (the calibration pair must be *found* gapped+taut, and
  is; the eight profile objects matched field-for-field). **(a)**
  Zero exactly-two members are gapped — (F-S)'s hypothesis class has
  exactly eight known realizations, all with \(6,14\in S\); outcome
  (i) of the pre-registration. **(b)** The wider class realizes the
  dodge freely: 9,061 vertex-taut gapped pairs (8/8/371/24 at
  12/14/16/17; 2,727/167/5,756 at 18/19/20 — no decay), 6,934 full
  \(\mathbb P{-}2\) dodges (\(2,6,14\notin S\)), on members with
  4–11 degree-2 vertices (min 5/6/4 at 18/19/20, never \(\le3\);
  thin-strata caveat). **(c)** 5,419 taut gapped rows sit on
  **power-free** members, most 2-connected: at window orders, every
  residual-object hypothesis *except the exactly-two profile* is
  realized simultaneously with the full dodge — the (F-T) double
  blocking is likewise profile-specific. Consequence for the missing
  tool: the interpolation lemma must consume min degree \(\ge3\) off
  the terminals; nothing weaker is true. Verification: every gapped
  pair recomputed by the independent full enumerator (540,135
  agreements per run) + stride sample; per-line integrity on all
  members; two production runs, identical tallies; zero bipartite
  members in the classes.
- **New (S026): `C047` — the near-miss dissection; the dodge taxonomy,
  the subdivision frame, and the chord-exchange validation.** Against
  the eight profile objects and a stride control: **(a)** every corpus
  dodge is shape A (short + 6-hole; minimal full dodges have
  \(\max S=13\) *exactly* at orders 16–20), A′ (\(\min S=7\) exactly),
  or B (long-range; holes exactly \(\{6,10,14\}\); even part
  \(\subseteq4\mathbb Z\) — the `L034` channel-(iii) pattern in-window
  on non-bipartite members; needs \(\ge7\) degree-2 vertices);
  **(b)** the dodge is pair-local — the order-20 frontier members
  (ndeg2 4; one adjacent-terminals full dodge \(S=\{1\}\cup[8,13]\))
  carry five fully saturated sibling pairs, so no member-level
  hypothesis works, and the profile hypothesis is load-bearing by
  exactly two subdivision vertices; **(c)** corridors are short
  (weights 2–3) and 99.1% of dodge rows reduce (suppressing
  non-terminal degree-2 vertices) to graphs carrying a \(C_4\)/
  \(C_8\) — subdivision is the escape from the class constraint;
  **(d)** killed: member-level lemmas, odd-cycle-supply
  discrimination (100% of dodge members have triangles); **(e)**
  control base rates: ordinary taut pairs break the upper-interval
  property at 12–17% (holes at 7–9, nearly gone by 13), Hamiltonian
  pairs 22–29% — the profile-8's joint saturation is far outside
  both; **(f)** the **span law** (proved, `A026` T5: no span-3/7
  chords) plus the first-order disjoint-chord calculus reproduce the
  profile saturation from 10 up (14 on all eight; misses confined to
  \([4,9]\)) and exactly explain the dodgers' holes (two span-2
  chords + spans \(\equiv1,2\bmod4\) ⟹ savings never \(\equiv3\bmod
  4\)). Consequence (`A026` T7): **(F-S) ⟸ (L-A) ∧ (L-B)** — (L-A)
  short-range exclusion (\(\max S\ge14\) in-window on the profile, or
  \(6\in S\) when short); (L-B) long-range poison forcing
  (\(\max S\ge14\Rightarrow14\in S\) or \(6\in S\)) — with the
  chord-savings combinatorics as (L-B)'s engine and ear-overload as
  (L-A)'s candidate.
- **New (S019): `L037`–`L042`, both `G015` routes advanced in one
  orchestrated parallel run.** R2 side (`L037`/`L038`): the
  **subdivision descent** — the link graph on the degree-\(\ge4\) set of
  a minimal counterexample is power-free (cycles lift doubled) and, by
  order-minimality, 2-degenerate — gives \(3|V_3|\ge2n+3\), strictly
  past Carr's \(4/7\); the 15-vertex certificate S15 (`E017`) shows
  \(2/3\) is the exact ceiling of the non-power hypotheses, so the
  constant route to `G015` is **closed**, with the descent as the
  reusable residue. R1 side (`L039`–`L042`): the closure calculus and
  the (3,3) **bijection** onto the congruence class \(\mathcal G\)
  (through-set avoids \(\{2,6,14,\dots\}\); no \(s_{\max}\) window);
  the **engine + peel** (any counterexample below the minimum atom
  order \(n_0\) yields a *cubic* counterexample — the repair of the
  withdrawn T4.1); the five-case analysis at the defect vertex:
  **the conditional cubic reduction holds modulo excluding case (5b)**
  (defect non-cut, both neighbours cubic, residue vertex-taut), every
  tight 1-atom has order \(\ge17\), and the case-(5b) residual object
  is 2-connected, degree-\(\ge4\)-independent, **non-bipartite** (hand
  proof at every order), with forced power/Mersenne memberships and
  chain cancellation. `C004`–`C006` are upgraded to **verified**
  (line-by-line audit of arXiv:2605.22844v1). The two routes meet: a
  one-defect subgraph of the link graph is exactly a tight 1-atom.

## Imported frontier

- `C004`–`C006` now carried at **verified** strength (S019 line-by-line
  audit and internal reconstruction,
  `references/carr-2026-verification-2026-07-24.md`); `C006` superseded
  internally by `L038`. `C007`–`C009`, `C012`–`C014`, `C017`,
  `C024`–`C026` unchanged; the min-degree-3 literature frontier remains
  Bondy–Vince strength.

## Program status

`G013` has three live objects.

(a) The **tight 1-atom question** — does a power-free graph exist whose
unique sub-cubic vertex has degree exactly 2? Rewritten in S018 (the
unrestricted version is conjecture-complete, `L036`) and **structured in
S019**: every tight 1-atom has order \(\ge17\) (`L041`); a minimum-order
one with both defect-neighbours cubic corresponds bijectively to the
congruence class \(\mathcal G\) (`L039`), and under (R) the *only*
surviving configuration is case (5b) — that closure with a vertex-taut
residue, now heavily constrained (`L042`: 2-connected, non-bipartite,
degree-\(\ge4\)-independent, forced through-set arithmetic, chain
cancellation, band-4 pencil). For `G015` the conditional form suffices
and only case (5b) remains. Empty through order 15 stream-level
(`C027`) **and through order 16 for the exact \(\mathcal G\) profile
(`C036`, S020), through order 17 for `C027`'s **entire class** by
the dedicated generator (`C039`, S021), and through order 19 for the
profile ladder (`C043`, S022 — order 18 empty; order 19's unique and
first-ever profile member is vertex-taut but \(C_{16}\)-blocked and
\(S\)-violating, doubly excluded)** — **every tight 1-atom has order
\(\ge22\), every \(\mathcal G\)-member \(\ge21\)** (S022 harvest:
order 20 also spent — profile 7, all \(C_{16}\)-blocked, none
power-free; the 1-bucket is empty at 18–20, so \(\ge21\) holds
directly by generation, and `L041`'s cases (4)/(5) with `L047` give
\(\ge22\)); no bipartite tight 1-atom through order 24 (`C034`, S021
harvest). The congruence-obstruction leg
is retired (`C037`/`A021`) and the chain-cancellation leg is **spent
as a theorem** (S021, `L043`–`L046`): the tension cannot exclude the
chain case by arithmetic alone (`L045`), but per-block order bounds
confine that case to \(n_0\ge36\) (`L046`) — so the case-(5b) frontier
below 36 is exactly the **2-connected** residual object. Its proof
side now runs through the **interference program**, whose gate is
passed (S023): interference-completeness holds for **every**
vertex-taut pair (`L049`, theorem, audited `R002`), so the object's
power-freeness **is** through-path arithmetic unconditionally
(`L048`(iii): \(\mathrm{Spec}(B)=T_1\cup(S+2)\), every element a
trunk-split pair value) — and the forcing target **(F)** is now the
entire proof side below 36: (F) says the forced \(S\)-arithmetic
makes a power-length trunk-split collision unavoidable in the window
\([18,35]\), which is *equivalent* to case (5b)'s emptiness there.
**S024 spent (F)'s opening move**: the realization tables came back
with no membership pattern (branch (b), `C045`), so (F) is re-aimed
as **(F-S) ∨ (F-T)** — the window forces \(S\cap\{6,14\}\ne\emptyset\)
or \(16\in\mathrm{Spec}\) — with the trunk bound `L051` proved and
the S-gap census as the next move. **S025 spent the census**
(`E026`/`C046`): (F-S) survives its first kill test (zero gapped
exactly-two members on all of 10–20's disk classes), and the
mechanism is recalibrated — 9,061 vertex-taut gapped pairs off the
profile prove that tautness + class + order force nothing; the
interpolation lemma must consume the exactly-two profile itself.
**S026 spent the dissection** (`E027`/`C047`, attempt `A026`): the
dodge taxonomy is rigid (shapes A/A′/B), the dodge is pair-local
with the frontier two subdivisions from the profile, near-misses are
subdivisions of class-violating graphs, and the interpolation target
splits into **(L-A) ∧ (L-B) ⟹ (F-S)** with the span law proved and
the chord-exchange calculus validated as (L-B)'s engine (top-of-S
saturation from 10 up reproduced on all eight profile objects).
Next: harvest `E024` (census the order-21 rung on landing), then the
(L-B) chord-savings attempt (prove in-window profile chord systems
realize savings \(M-14\) or \(M-6\)), with (L-A) ear-overload behind
it.

(b′) The **block question** (pinched channel); after `L033` its band-4
case is exactly the **pencil endgame** — prove no vertex-taut
2-connected \(C_4\)-free core with \(d(x,y)=4\), \(s_{\max}\le8\) has a
pencilled 4-path system. Catalogue now through order **16**
(`C030`–`C032`, `C035`/S017): **eight equality blocks** — P10 =
Petersen\(-e\) (band 4), A11/B11/C12 (band 5), D14 (band 6), and from
the order-16 harvest F16 (band 4, terminal degrees (3,3), on a graph
with no sub-cubic vertex), G16 (band 4, (2,4)), H16 (band 6, (2,2),
first block with \(C_{16}\) in spectrum) — every one at exact equality
\(s_{\max}=2\,s_{\min}\); **no strict taut pinched pair exists at
order 16 at all** (strict catalogue complete at seven witnesses
through 16), no power-free closed taut pair at 16, and all three
band-4 core gadgets are disjoint-type, so the pencil endgame's
exhaustive empty base and the 100% two-through-path interference
census both extend through order 16. Hypothesis necessity (`C033`):
\(C_4\)-freeness is essential to both band-4 rungs. Three hand
constructions died to the cascade obstruction (`A015`).

(c) The **congruence channels**, now **split by `L035`**. Channels (i)
(all-odd \(S\)) and (iii) (\(S\subseteq2+4\mathbb Z\)) *are* the
bipartite class, and `E015`/`C034` searched it exhaustively: **no
power-free member at any order \(\le24\)** (\(\le25\) with a pendant),
with every member of the class carrying a \(C_8\) and the minimum
\(C_8\) count never dropping below 13 — so the \(C_{16}\) test is never
even decisive, and this channel is *further* from a witness than the
pinched one (whose equality blocks are blocked by 3–7 \(C_8\)s). What
survives in (c): channel (ii), the odd-prime-gcd channel — not
bipartite-forced, no structure theorem, no reduction, no dedicated
search — plus the missing parity analogue of `L032`'s 2-connected block
extraction. Two by-products of the same run: no bipartite counterexample
and no bipartite **tight** 1-atom at orders \(\le23\), verified
internally.

## Open obligations

- `G015` (**the proof-side deliverable; reduced in S019 to one
  configuration**): exclude case (5b) — no minimum-order tight 1-atom
  is the 2-path closure of a vertex-taut \(\mathcal G\)-member — and
  the cubic reduction follows (`L040`/`L041` supply every other case).
  The constant-density route is closed (`L038` delimitation); the
  order-16 scan is done and empty (`C036`) and the congruence hunt is
  dead (`C037`/`A021`). Live moves: the chain-cancellation tension
  (`L042` W1-T14), the disjoint long-link descent (`A020` W2-T8(c)),
  and the order-17 search rung via the `G014` item-6 generator.
- `G013` (core): tight 1-atoms; the block question (band 4 = pencil
  endgame, bands \(\ge5\) open); the odd-prime-gcd channel and the
  missing parity block-extraction.
- `G014`: source-audit the external memo's literature and census leads.
  Item (2) (bipartite \(\ge32\)) is **de-gated** — `L035` T3 removes the
  need for the Mersenne-window logic and `C034` verifies the range
  internally; items (1), (3)–(6) still gate their threads.
- `G002`, `G003`, `G007`: the global mechanism; `G007` routes through
  `G013`'s conditional transfer.
- `G004`: only the original 1997 Erdős article body remains uninspected.

## Roadmap (S018)

Standing instruction (user, S015): **all threads stay documented and
live**; sessions select by strategy audit, retire only on evidence. S018
adds a second instruction (user): weigh routes by what they would
*deliver* — the full conjecture first, a significant delimited result
second — and keep cheap legs running alongside rather than instead.

The tiers below replace the flat thread list. Threads A–F are all still
here; what changed is that each now says which tier it serves, and no
thread may be selected as a session's primary work on cheapness alone.

**Why the restructure.** Sessions 11–16 all worked inside the assembly
interface, whose proof-side best case is the *cubic reduction*, not 0.1
(`A016` M6). S018 then found that one of that interface's two halves —
the 1-atom question — is conjecture-complete (`L036`), so the recorded
"ceiling" was in fact circular. The dossier's real proof-side
deliverable is `G015`, and it had never been named as a target.

### Tier 0 — settle statement 0.1 (the mission)

No cheap move exists here, and none should be pretended. Two sub-cases:

- **A forcing mechanism at \(\delta\ge3\)** (`G003`, `G007`). The
  literature frontier is Bondy–Vince strength (two cycles differing by 1
  or 2); nothing forces a *specific* length. Every internal theorem so
  far (`L030`, `L033`, `L035`) has run on \(C_4\)-freeness or parity, and
  the power spectrum has never once had to fight — that is the diagnostic
  to keep watching.
- **A counterexample.** Best ticket: cubic, order \(\ge30\) (Thread C),
  because `C013` stops at 28 and `L029` concentrates the risk there.

### Tier 1 — the named deliverable: the cubic reduction (`G015`)

"0.1 holds iff it holds for cubic graphs." **S019 ran both routes in
parallel (audited worker subagents) and the target is now a single
configuration:**

- **R1, reframed to the conditional form** — "a tight 1-atom yields a
  cubic counterexample", which is all the reduction needs (`L040`); the
  unconditional "no tight 1-atom exists" is retired as an R1 target
  (unreachable by minimality: its reducts are counterexamples, not
  atoms). By `L041` the conditional form is proved **except in case
  (5b)**; excluding that case closes `G015`. S020 spent the first two
  recorded moves: the order-16 scan is **empty** (atom bound now
  \(\ge18\), `C036`) and the congruence obstruction is **dead at every
  modulus** (`C037`/`A021` — the forced hypotheses are realized from
  order 10, so they admit no refutation; parity is the ceiling of
  chain-calculus congruence information). **S021 spent the next two moves in one
  orchestrated run:** the chain-cancellation tension is now the theorem
  package `L043`–`L046` — quantified (`L045`: three exponent-
  disjointness conditions per cut are the whole forced content, so
  membership arithmetic alone can never exclude the chain case), with
  every prefix/suffix forced non-bipartite (`L043`) and the order
  dichotomy `L046` confining the chain case to \(n_0\ge36\) — **only
  the 2-connected configuration remains below 36**; and the order-17
  rung is **spent empty** by the new generator (`C039`: tight 1-atoms
  \(\ge19\); the chain-case kill test refuted through the order-14
  block catalogue, `C038`, named 15/16 rung open). **S022 ran moves (i) and (ii) to
  verdicts** (orchestrated: W1 `fable` on the dissection, W2 `opus` on
  the ladder, both audited with independent re-derivations): the
  dissection landed the **interference outcome** — no
  non-interference blocker exists at the frontier (`C041`, 553/553),
  the property is exactly tautness-shaped (`C042`), the calculus is
  proved (`L048`), and the ladder moved the floors to 20 with the
  **first-ever profile member** at order 19, doubly blocked
  (`C043`). **S023 closed the T5 program**: the remaining kill
  rungs ran first and survived (`C044`), then **T5 was proved
  outright** (`L049`, the trimming construction — no exchange
  argument exists in the final proof; audited `R002` PASS) with the
  spectrum identity unconditional (`L048`(iii) upgrade) and the
  biconditional a theorem on \(\delta\ge2\) (`L050`). Live moves
  against case (5b), in order — **S024 spent move (i)'s opening probe
  (branch (b)) and re-aimed the program**: (i) **the (F) program,
  now (F-S) ∨ (F-T)** (`A025` T4): the membership-collision form is
  dead (`C045` — no pattern survives the ten objects; 30
  membership-blind cycles), and (F) splits into (F-S) — in the window
  \([18,35]\), vertex-taut (5b)-profile pairs with
  \(4,8\notin\mathrm{Spec}\) force \(S\cap\{6,14\}\ne\emptyset\)
  (closure blocked) — and (F-T) — they force \(16\in\mathrm{Spec}\)
  (\(H\) blocked); either closes case (5b) below 36. Supporting
  structure proved: the trunk bound `L051` (\(s\le n-L\), tight on
  all ten objects — the collision system is order-confined).
  Candidate mechanism: **saturation/interpolation** (all eight
  profile objects have \(S\supseteq[6,n-1]\) and spectrum
  \([3,n]\setminus\{4,8\}\); the missing tool is a lower-bound theory
  for through-path length sets). **S025 spent the census** (`E026`/
  `C046`, outcome (i)): **(F-S) survives** — zero gapped exactly-two
  members anywhere on disk at 10–20 — and the tool's spec is
  sharpened: 9,061 vertex-taut gapped pairs off the profile (down to
  4 degree-2 vertices at order 20, most on power-free 2-connected
  members) prove the lemma must consume the **exactly-two profile**,
  not just tautness. **S026 spent the dissection sub-move**
  (`E027`/`C047`, attempt `A026`): the taxonomy (A/A′/B), the
  pair-locality warning, the ndeg2-4 frontier, the subdivision frame
  (99.1% class-violating reductions), the span law (proved), and the
  chord-exchange validation — the target lemma is now the split
  **(L-A) ∧ (L-B)** with the chord-savings combinatorics as (L-B)'s
  engine. Next falsifiable moves, in order: **harvest `E024`** when
  it lands (census the order-21 rung; a gapped exactly-two member
  kills (F-S); an \(S\)-satisfying hit is a disproof), then the
  **(L-B) chord-savings attempt** (build the \(C_4/C_8\) chord-pair
  exclusion table over a longest path; prove in-window profile chord
  systems realize savings \(M-14\) or \(M-6\); any draft must fail
  on the 36 Hamiltonian dodgers and respect the corpus), then the
  **(L-A) ear-overload attempt** (short-range exclusion; the
  adjacent-case recursion of `A026` T2); behind them min-degree-3 at
  22 (\(\approx\)38 h) and the `C038` **kill rung** at block orders
  15–16 + the disjoint long-link descent (unchanged).
- **R2, constant route closed** — `C004`–`C006` verified and the bound
  improved to \(3|V_3|\ge2n+3\) (`L037`/`L038`), but S15 certifies
  \(2/3\) as the exact ceiling of the non-power hypotheses and no
  constant \(<1\) delivers the reduction. Surviving extension: the
  internally-disjoint longer-link descent (`A020` W2-T8(c)). The
  descent itself is the reusable mechanism, and the routes meet on the
  link graph (a one-defect subgraph of it is a tight 1-atom).

This remains the highest-value *reachable* target in the dossier: a
theorem about the conjecture rather than about our own gadget
formalism, and it would make Thread C's searches decisive instead of
conditional.

### Tier 2 — restricted-class theorems worth having on their own

- **Bipartite EGC** (Thread E): every bipartite \(\delta\ge3\) graph has
  a power-of-two cycle. `L035` fixes the class (girth \(\ge6\)
  bipartite), `C034` gives an internally verified base through order 24,
  and the naive "\(C_8\) always" form is *false* at large order
  (bipartite double covers of `C009`'s large-girth cubic graphs), so any
  proof must be order-bounded or consume \(C_{16}/C_{32}\). Reported
  externally only as a computation to 31 — a proof would be new.
- **The path-spectrum spread theorem** (Thread B3): under (D), is
  \(\gcd(S)\) always a power of 2? New genre — the literature's mod-\(k\)
  results are about cycle spectra, not two-terminal path spectra. The
  3-connected *cycle* analogue is a four-line Menger argument (`A016`
  M10) and is the proved cousin to start from; \(\Theta(3,3,3)\) shows
  the degree condition, not parity, must do the work.

### Tier 3 — cheap legs: run them, never *select* them

Harvest-only. None of these may be a session's primary work.

- Bipartite hunt (`E015`/`E019`): clean through order 24 (25 with a
  pendant) — the order-24 leg landed empty in the S021 same-day
  harvest, the first order covered by generation rather than genbg.
  Next leg: order 26 on the `-b` instrument (even orders; the
  unfinished odd-order-23 probe remains the recorded warning against
  interpolating even-order growth).
- The gcd scan over the existing order-\(\le16\) stream (needs path
  enumeration; the bipartite shortcut does not apply).
- Order-17+ legs of the pinched catalogue (Thread A/F).
- Census mining (Thread D), gated by `G014`.
- The min-degree-3 ladder at order 22 (≈38 h on 8 workers at the
  measured ×7.2 growth — a deliberate decision, no longer a cheap
  leg): orders 20 and 21 landed empty in the S021/S022 harvests
  (`C040` runs 14–21, `L047` at 22); order 22 is the window's bottom,
  so the next empty rung meets Markström's order-24 ceiling two away.

### Tier 4 — infrastructure with cross-thread leverage

- ~~The dedicated \(\{C_4,C_8\}\)-free generator~~ **Built (S021,
  `E019`/`C039`; `G014` item 6 discharged).** What it unlocked on day
  one: the order-17 \(\mathcal G\) rung (40 s wall), `C027`'s class to
  17, the min-degree-3 sweep to 19 (`C040`/`L047`). What it prices in:
  \(\mathcal G\) orders 18/19/20 at ≈4 min/25 min/2.8 h; cubic orders
  26/28 at ≈15 min/3.5 h (reproducing the remaining `C013`/`C014`
  lines) and **cubic order 30 — Tier 0's best counterexample ticket —
  at ≈2.3 days on 8 workers**; bipartite 24–26 in minutes-to-hours.
  Remaining instrument work if order 24+ \(\mathcal G\)-rungs are ever
  needed: port the same 60-line prune into a cubic-specialized host
  (genreg/minibaum) — recorded in `E019`'s design analysis, not needed
  through order 21.
- `G014` source audits for the imports that gate Tiers 1–3 (census
  provenance for Thread D; items (1),(3)–(5); new item (7), the
  MO-512914 thread body).

### Demoted and retired

- **Retired as a target:** the unrestricted 1-atom question
  (conjecture-complete, `L036`). It stays in the record as a
  completeness fact, not as work.
- **Demoted to Tier 3:** the pinched-channel rung ladder, including the
  pencil endgame (Thread A). It is real mathematics and stays live, but
  its best case is one channel of a ceiling-limited interface, so it no
  longer merits primary selection over Tier 1.

### Pivot triggers

A hit in a \(\mathcal G\)-profile scan at order 21+ satisfying the
\(S\)-condition (**immediate disproof** — a tight 1-atom; 16–20 were
consumed in S020–S022, the eight profile members at 19–20 all
\(C_{16}\)-blocked);
a \(\{C_4,C_8\}\)-free min-degree-3 graph at order 22+ (first at 22
would refute nothing but ends `L047`'s climb at the window's bottom;
a *power-free* one is a **counterexample**; 14–21 are all empty); a pencil-type band-4 taut core at order 17+; a
strict block or \(C_8\)-free equality block (disproof protocol);
**any** power-free member of the `E015` class at order 25+ (immediate
disproof, `L035` T3; 24 landed empty in the S021 harvest); a `G014`
audit overturning an assumed bound; a realized
\(\{7,8,12,13,14\}\)-shaped block through-set at order 15–16 (kills
arithmetic-only chain exclusion; the chain-case Petersen\(-e\) then
exists at order ~29); a non-decomposable cycle in a vertex-taut
pair would now **contradict the reviewed theorem `L049`** (the S023
rungs gave it 12.7M further chances and it never happened) — any such
find is a soundness alarm on `A024`/`R002`/the census predicate, to be
treated as a critical audit event, not a route pivot;
~~a membership-patterned regularity in the (F) realization tables~~
(**spent, S024**: the tables came back with no pattern — branch (b)
taken, the membership-collision form of (F) is dead, `C045`/`A025`);
~~a vertex-taut member of the 18+ class with
\(S\cap\{6,14\}=\emptyset\) in the S-gap census~~ (**spent, S025**:
the census found none on any exactly-two member — (F-S) survives —
while the wider class realizes the dodge freely, so the trigger's
surviving form is a **gapped vertex-taut exactly-two member at order
21+**, checked when each new ladder rung is censused; a wider-class
dodge is no longer a trigger, it is the recorded norm);
a **profile-consuming interpolation lemma that also holds on the
census's near-miss corpus** (would be false — 9,061 counterexamples
on disk — so any draft proof matching the corpus is unsound: use it
as the standing sanity check beside the calibration pair; after
S026, the sharp instances are the **36 Hamiltonian dodgers** for
(L-B) — any savings-forcing draft must fail on their chord systems —
and the **ndeg2-4/5 frontier members** for (L-A)); a **short-range
or gapped exactly-two member at order 21+** (a \(\max S\le13\)
profile pair kills (L-A) as stated; a gapped one kills (F-S) —
check each new ladder rung); a **power-free vertex-taut (5b)-profile pair anywhere in
the window** (defeats (F) in both forms and is one 2-path closure
away from a tight 1-atom — disproof-adjacent); a **proof of (F-S) or
(F-T) on the window** (then case (5b) is closed below 36, `G015` is
proved below 36, and the search ladder becomes the whole case);
exclusion of case (5b) outright (then `G015` is proved and Thread C
becomes the whole game).

### Process correction (S018)

Sixteen audits in a row selected the route with the cheapest decisive
computation. That criterion is what buried `G015` and what kept a
conjecture-complete object on the live list for six sessions. From now
on, a session's strategy audit must name the tier its selected route
serves, and must justify any Tier 3 selection as *background*, not as
the session's work.

## Human-level state

The programme's proof-side prize is one named theorem: **the conjecture
holds in general if and only if it holds for 3-regular graphs.** S019
attacked it down both of its routes at once — the first orchestrated
parallel session, one worker per route, everything audited before being
believed — and both routes moved.

The published-density route first: a 2026 paper of Carr proves that in
a smallest possible counterexample, at least 4/7 of the vertices have
degree exactly 3. We verified that paper line by line (it holds up),
then pushed the bound: at least two-thirds, plus a little more. The
push needed a genuinely new trick — the degree-3 vertices wedged
between two high-degree vertices act like markers on invisible edges,
and those invisible edges form their own smaller graph which inherits
the no-power-of-two property with all lengths halved; because the
original graph was the *smallest* offender, the smaller shadow graph
must be sparse. But the same session also proved this route can go no
further: an explicit 15-vertex example meets every hypothesis the
counting uses at exactly two-thirds density, and no percentage short of
100% ever delivers the reduction. So that route ends — honourably, with
a stronger theorem than the literature has and a reusable mechanism.

The internal route is now where the game is. The "single defect" graph
question (one vertex of degree 2, everything else degree 3 or more, no
power-of-two cycle) was analysed at its defect vertex, and of the five
possible local shapes, four are now impossible or lead exactly where we
want: a smaller offender, which a repaired argument converts into a
**3-regular** counterexample — which is the reduction succeeding, not
failing. One shape survives: the defect vertex sits on a triangle-free
"lens" whose two anchor points are both degree 3, with every vertex on
some anchor-to-anchor path. That single surviving configuration now
carries the whole theorem, and it is already known to be at least
17 vertices, two-connected, never two-colourable, and arithmetically
squeezed (its path lengths must hit some exact powers of two and miss
others).

S020 spent the order-16 search (empty — the dangerous object needs at
least 18 vertices) and killed the "remainders" proof route for good
(Petersen minus an edge satisfies every arithmetic condition the
dangerous configuration must satisfy, so no remainder argument can
ever exclude it).

S021 ran the two surviving moves in parallel — one worker on the
remaining proof idea, one building the search machine — and both
delivered.

The proof idea was the "cancellation across links of a chain" tension:
if the dangerous configuration were built like a chain of beads, each
bead is forced to contain certain forbidden path lengths while the
whole chain must avoid them — a tension that looked exploitable. The
session settled exactly what that tension is worth. On its own,
provably nothing: the forbidden lengths can always dodge each other
(the collision arithmetic is now a small closed table). But combined
with the search data the picture flips: each solid bead of such a
chain would itself have to be one of the rare graphs our searches have
been proving nonexistent, so **any chain-like dangerous configuration
needs at least 36 vertices**. Below that, the dangerous configuration
must be a single solid two-connected piece — one shape left, and the
cycles-interfering-with-each-other structure is now provably the only
kind of argument that can kill it.

The search machine got built the same afternoon: a modified version of
the standard graph generator that refuses ever to build an 8-cycle,
verified twenty-three ways against the old pipeline and against an
independently published census it reproduces exactly. It is roughly a
hundred times cheaper than the old filter-everything approach. Its
first production run emptied size 17 in forty seconds of wall clock
(the dangerous object now needs at least 19 vertices), and as a
by-product it swept the "minimum degree three" world — where any
counterexample to the whole conjecture must live — up through 19
vertices: empty, with the first unchecked orders independently
spot-audited against the old instrument (three slices, 38.7 million
graphs, all agreeing). A reader-supplied MathOverflow thread claimed
size 20 was already settled; auditing it showed its cubic computation
is right (and matches ours) but its leap from "no cubic example" to
"no example at all" silently assumes the very theorem this programme
is trying to prove — so we rejected that step and ran our own size-20
sweep, which needs no such assumption. It landed the same evening,
empty: **every counterexample to the conjecture now needs at least 21
vertices**, two better than the previous record, and the extremal
window is down to four sizes, 21 through 24. The same evening's runs
also emptied bipartite size 24 on the new machine (that class is now
clean through 24) and reproduced the thread's two cubic counts to the
digit — their computation was right, their inference was the only gap,
and nothing now rests on it.

S022 ran the two named moves in parallel — one worker dissecting the
near-miss graphs, one running the search ladder — and both delivered.

The dissection asked the one question the surviving proof route hangs
on: in the graphs closest to the dangerous configuration, is every
"blocking" cycle (the 8-cycle or 16-cycle that stops the graph from
being a counterexample seed) built by overlaying two terminal-to-
terminal paths — an *interference pattern* — or can a blocker exist
that the path system cannot see? The answer, across all 553 blocking
cycles of every closest object on record: **interference, every single
time**, and the trait tracks exactly the property ("every vertex
carries terminal-to-terminal traffic", vertex-tautness) that the
dangerous configuration is forced to have. Three small lemmas now pin
the mechanism down: under the conjectured completeness, the dangerous
object's entire "no power-of-two cycle" property becomes arithmetic of
its own path system — the one kind of argument the two earlier
impossibility theorems left alive. The lemma to prove next ("in a
vertex-taut graph, every cycle is such an overlay") is stated, its
evidence is strong (over 800,000 verified instances, zero failures),
its proof obstacles are named, and its kill tests are ordered and
cheap.

The search ladder swept sizes 18 and 19. Size 18: nothing. Size 19
produced a genuine first — the very first graph ever found with the
dangerous configuration's exact degree pattern — and it is killed
twice over, independently: a 16-cycle sits inside it, and its path
lengths hit two forbidden values. The new graph is itself the best
test object yet for the lemma above, and the overnight run launched
at close delivered: the lemma **survived** on it (all 411 of its
cycles are path overlays, zero exceptions); the size-20 sweep found
seven more graphs with the dangerous degree pattern — every one
killed by a 16-cycle, with each recovered one *also* hitting the two
forbidden path lengths, the same double death as size 19 — and the
size-19 consistency count came back exact. The lemma then survived on
all three of the size-20 graphs recoverable from disk (1,890 more
cycles, zero exceptions). Net: every single-defect seed now needs at
least 22 vertices, and the candidate lemma has passed its sharpest
cheap tests. The four size-20 graphs that fell outside a
data-retention window were regenerated (the stream recount matched
the original tally to the digit) and the lemma survived on them too —
so **all eight graphs in existence with the dangerous degree pattern
pass the lemma, on every one of their 4,661 cycles**, and every one
of the eight is killed by the same double mechanism (a 16-cycle plus
the two forbidden path lengths). And the size-21 sweep of the
minimum-degree-three world came back empty: **every counterexample
to the conjecture now needs at least 22 vertices**, and the extremal
window is down to three sizes, 22 through 24.

S023 finished what the overnight tests began. The two remaining cheap
attempts to kill the key lemma were run first — every candidate graph
with the right shape on 13 vertices, and every graph whatsoever up
through 8 vertices — and the lemma survived all of them, tens of
millions of cycles with not one exception. Then, instead of the
planned delicate argument about controlling how paths wind through a
cycle, a much simpler idea landed the proof outright: route a path
through any chosen edge of the cycle, throw away everything between
its first and last touches of the cycle, and complete the two kept
ends around both sides of the cycle. The two hybrid routes so built
are the desired pair, and all the winding one feared lives entirely
in the part that was thrown away. A fresh, isolated referee — given
only the claim and the proof, none of the discovery reasoning —
attacked it, re-ran every computation independently, rebuilt the
whole verification from scratch in its own code, and passed it with
only cosmetic repairs, each now applied. So the pattern spotted two
sessions ago ("every blocking cycle is an interference pattern of two
terminal-to-terminal paths") is now a theorem wherever the dangerous
configuration can live, and that configuration's defining
no-power-of-two property is now, provably and unconditionally, a
statement about the arithmetic of its own path system. What remains
of this branch of the programme is exactly one named question — the
forcing question: do the path lengths that configuration is *forced*
to have always collide into a power-of-two cycle when the graph is
small enough? Answer yes below 36 vertices, and the programme's
centerpiece theorem (the cubic reduction) is proved there.

S024 took that question's first step: it built the complete
"collision tables" of all ten graphs closest to the dangerous
configuration — for every power-of-two cycle in each graph, every way
that cycle arises as two terminal-to-terminal paths overlaid in the
theorem's normal form. The question the tables were built to answer:
do the special path lengths the dangerous configuration is forced to
carry (powers of two and their neighbours) drive the collisions? The
answer is a clean no — the collisions run through ordinary lengths,
thirty of the cycles involve no special length at all, and the two
small graphs where power lengths did drive everything turn out to be
small-size artifacts. That kills one candidate proof mechanism early
and cheaply, and the same tables revealed what actually governs the
collisions: geometry and size, not length arithmetic. Two facts stand
out. First, a newly proved (small) lemma: the shared part of any such
overlay must fit entirely outside the cycle, so at the sizes in
question the collisions have almost no room — a bound the data meets
exactly on every one of the ten graphs. Second, saturation: each of
the eight frontier graphs has cycles of *every* length except exactly
4 and 8, and terminal-to-terminal paths of *every* length from 6 up —
in particular the two "poison" lengths (6 and 14) whose presence
dooms a candidate seed. So the forcing question sharpens into two
concrete alternatives, either of which suffices below 36 vertices:
prove that in the critical size window every candidate is forced to
carry a poison path length, or prove it is forced to carry a
16-cycle. The next move is a direct census over the already-generated
databases: does any graph in the window escape both poison lengths?
If none does, the first alternative survives its cheapest test; if
one does, it is a named new test object and the attack shifts to the
second alternative.

S025 ran that census — every pair of degree-2 vertices of every
graph in the databases, three-quarters of a million graphs, nearly
nineteen million pairs, with the search code cross-checked against
two older independent programs on every interesting case and the
whole run executed twice with identical counts. The answer has two
halves, both sharp. First: no graph with the dangerous
configuration's exact shape (exactly two degree-2 vertices) escapes
the poison lengths — the eight known such graphs all carry both
poisons, and no ninth shape-matching graph exists in any database —
so the "poison is forced" alternative survives its cheapest kill
test exactly where the dangerous configuration would have to live.
Second, and just as important: graphs that are *near* the shape but
not exactly on it (three or more low-degree vertices instead of two)
escape the poisons freely — over nine thousand escapes, many on
graphs that also avoid all the forbidden cycles, growing rather than
dying out as size increases. So the escape phenomenon is real and
abundant right up to the wall, and it stops exactly at the shape
itself.

S026 dissected those nine thousand escapes against the eight
shape-matching graphs, and the anatomy came out cleaner than hoped.
Every escape works one of three ways, each rigid: keep all paths
short (the longest terminal-to-terminal path is *always* exactly 13
— one below the poison), start too far apart (distance exactly 7,
never more), or run a striking arithmetic pattern where the
even-length paths come only in multiples of four (killing lengths 6,
10 and 14 together). Three structural facts explain the escapes.
The escape belongs to the *pair*, not the graph — the frontier
graphs carry one escaping pair alongside five fully saturated ones,
so no whole-graph explanation can work. Every escape rides on
"corridor" vertices — degree-2 vertices that would be forbidden in
the exact shape — and 99% of escapes, when those corridors are
contracted away, reveal a graph that violates the forbidden-cycle
rules: the escapes are stretched-out versions of illegal graphs,
and the exact shape is precisely the class that cannot stretch.
And the escape frontier now stands two corridor vertices from the
exact shape. On the positive side, a concrete engine emerged: on
each of the eight shape-matching graphs, take one longest
terminal-to-terminal path and reroute it along its shortcut edges
(a one-line rule says shortcuts spanning 3 or 7 steps cannot exist,
because they would close a forbidden cycle) — and those reroutes
alone already produce every path length from 10 up to the maximum,
including both poisons, on all eight graphs, while provably
producing none of the escapees' missing lengths. The proof problem
is now two named lemmas: show that the exact shape in the critical
size range cannot keep all paths short (the thin-margin half), and
show that its shortcut structure always reaches down to a poison
length (the half the new engine covers).

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 8%
- Previous estimate: 8% (S025)
- Reason for no change: the dissection's findings again roughly
  cancel. For: the mechanism extraction succeeded beyond expectation —
  the dodge taxonomy is rigid, the exchange calculus is a *validated*
  engine (it already reproduces the entire poison-relevant part of
  the saturation on all eight profile objects, with the span law
  proved), and (L-B) now has a concrete combinatorial proof target
  where none existed. Against: (L-A) — the short-range half — has a
  two-subdivision empirical margin, no engine, and the frontier trend
  (dodges at ndeg2 4 by order 20, hi = 13 walls) is compatible with
  (F-S) simply failing at some order 21–35; the exactly-two class
  still has eight data points; and even (L-B)'s target (savings
  reachability) is an unproved combinatorial statement about a chord
  structure nobody has axiomatized. The route is sharper and better
  instrumented but not yet easier.

## Resume reading

1. `STATEMENT.md`
2. **`A026`** (the dissection deductions T1–T6, the (L-A)/(L-B)
   split T7, the sharpened tool spec and kill discipline) and
   **`A025`** (the (F-S)/(F-T) redirect frame it serves); then
   `A024`/`A023` (the T5 theorem and interference frame) and `A019`
   (the case analysis, the engine/peel, the residual object)
3. **`E024` is running** (order-21 \(\mathcal G\) rung, launched at
   S023 close; not citable until harvested — **harvest it first when
   it finishes**: floors move if empty, each profile member is a new
   (F) data point to census + exchange-test, an \(S\)-satisfying hit
   is a disproof, a gapped or short-range exactly-two member kills
   (F-S)/(L-A)). **Then: the (L-B) chord-savings attempt** — build
   the \(C_4/C_8\) chord-pair exclusion table over a longest path
   and prove in-window profile chord systems realize savings
   \(M-14\) or \(M-6\); any draft must fail on the 36 Hamiltonian
   dodgers (`E027/data/exchange_test.json`) and hold on the eight
   profile objects. Behind it: the (L-A) ear-overload attempt.
4. `E027/README.md` (the dissection: taxonomy, frontier, subdivision
   frame, control rates, the exchange validation) with
   `corpus_rows_compact.json` as the per-row refutation set; then
   `E026/README.md` (the census) and the `E021`/`E022` READMEs for
   the imported instruments
5. `A021` (the congruence kill and the two-object calibration
   discipline — Petersen\(-e\) shows \(C_8\)-freeness is necessary
   for (L-A)) and `A022`/`E020` (the chain package and its 15/16
   kill rung)
6. `CLAIMS.md` rows `C047` (new, S026), `C046` (S025), `L051`/`C045`
   (S024), `L049`/`L050`/`C044` (S023) (and `L039`–`L048`,
   `C036`–`C043` for the frame); `OBLIGATIONS.md` `G015`/`G013`
7. `sessions/S026-…md` (this session: the dissection, the split, the
   engine) and `S019`–`S025` for the preceding arc
