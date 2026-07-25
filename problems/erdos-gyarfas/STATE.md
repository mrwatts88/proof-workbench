# Current state

- Last updated: 2026-07-24 (S022 — orchestrated parallel legs: the
  interference model survived its frontier kill test on all 553
  blockers and the calculus is fixed (`L048`); the ladder spent orders
  18–19 — the first-ever profile member appeared at 19, doubly
  blocked — and every tight 1-atom and \(\mathcal G\)-member now has
  order \(\ge20\); follow-up running: the exemplar T5 kill test, the
  order-20 rung, the order-19 unsplit count)
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
  Follow-up running (`E022/followup_s022.py`; nothing citable until
  harvested): the exemplar's full cycle set against T5 (stage A), the
  order-20 rung (stage B), the order-19 unsplit count (stage C).
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
\(\ge20\), every \(\mathcal G\)-member \(\ge20\)** (the 1-bucket is
empty at 18–19, so the atom bound is also direct, without the case
analysis); no bipartite tight 1-atom through order 24 (`C034`, S021
harvest). The congruence-obstruction leg
is retired (`C037`/`A021`) and the chain-cancellation leg is **spent
as a theorem** (S021, `L043`–`L046`): the tension cannot exclude the
chain case by arithmetic alone (`L045`), but per-block order bounds
confine that case to \(n_0\ge36\) (`L046`) — so the case-(5b) frontier
below 36 is exactly the **2-connected** residual object. Its proof
side now runs through the **interference program** (S022): every
blocker at the frontier is a two-through-path symmetric difference
(`C041`), interference-completeness is empirically equivalent to
vertex-tautness (`C042`, necessity proved in `L048`), and under the
candidate lemma T5 the object's power-freeness is through-path
arithmetic (`L048`(iii)) — the forcing target (F) would then close the
case below 36. Its search side is the ladder at order 20+ (the
order-20 rung is running as the S022 follow-up; 21 is \(\approx\)18 h
on 8 workers).

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
  (`C043`). Live moves against case (5b), in order: (i) the **T5
  program** — kill rungs first: the order-19 exemplar's full cycle
  set (S022 follow-up stage A — the exemplar is vertex-taut, so a
  single non-decomposable cycle kills T5 at the most relevant object;
  survival is the strongest cheap evidence yet), then `smallworld 13`
  (\(\approx\)minutes, exhaustive in-class at 13) and a sparse
  general-graph probe at orders 8–9; if T5 survives, the **proof
  attempt**: the clean-window reroute + minimal-choice exchange
  argument, with two named sub-obligations (cycle-edge essentiality
  in taut pairs; weaving control); (ii) the forcing target **(F)**
  (`A023` T6): vertex-taut (5b)-profile pairs with the forced
  \(S\)-arithmetic in the window \([18,35]\) always realize a
  \(t=1\) collision at a power length — with T5/`L048` this closes
  case (5b) below 36; doubly calibrated (Petersen\(-e\), the order-14
  exemplar); (iii) the **ladder at order 20** (follow-up stage B
  running; empty would lift both floors to 21 — direct 1-bucket at
  20 — and 21 costs \(\approx\)18 h on 8 workers); (iv) the `C038`
  **kill rung** at block orders 15–16 and the disjoint long-link
  descent (unchanged).
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
- The min-degree-3 ladder at order 21 (`E019`, ≈5.3 h on 8 workers):
  order 20 landed empty in the S021 harvest (`C040`, `L047` at 21);
  each further empty order lifts the counterexample bound by one.

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

A hit in a \(\mathcal G\)-profile scan at order 20+ satisfying the
\(S\)-condition (**immediate disproof** — a tight 1-atom; 16–19 were
consumed in S020–S022, order 19's sole profile member doubly blocked);
a \(\{C_4,C_8\}\)-free min-degree-3 graph at order 21+ (first at 21
would refute nothing but ends `L047`'s climb; a *power-free* one is a
**counterexample**); a pencil-type band-4 taut core at order 17+; a
strict block or \(C_8\)-free equality block (disproof protocol);
**any** power-free member of the `E015` class at order 25+ (immediate
disproof, `L035` T3; 24 landed empty in the S021 harvest); a `G014`
audit overturning an assumed bound; a realized
\(\{7,8,12,13,14\}\)-shaped block through-set at order 15–16 (kills
arithmetic-only chain exclusion; the chain-case Petersen\(-e\) then
exists at order ~29); a **non-decomposable cycle in any vertex-taut
pair** — in particular in the order-19 exemplar (follow-up stage A),
at `smallworld 13`, or in the sparse 8–9 probe — kills T5 as stated,
names its missing hypothesis, and redirects the proof side (the S022
frontier families gave it every chance and it did not happen, `C041`);
a **proof of T5** (then the case-(5b) object's spectrum equals its
\(T_1\) set, `L048`(iii), and the forcing target (F) becomes the
entire proof side); exclusion of case (5b)'s 2-connected branch below
36 (then `G015` is proved below 36 and the search ladder becomes the
whole case); exclusion of case (5b) outright (then `G015` is proved
and Thread C becomes the whole game).

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
lengths hit two forbidden values. Every "single-defect" seed now needs
at least 20 vertices. The new graph is itself the best test object yet
for the lemma above, and testing it is stage one of the overnight
run launched at close (stages two and three: the size-20 sweep and a
final consistency count for size 19).

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 7%
- Previous estimate: 6% (S021)
- Reason for the change: the last surviving proof-side route survived
  the one test that could have killed it immediately, and came back
  with a mechanism instead of a hope. For: the interference outcome
  was not forced — a single non-interference blocker among 553 would
  have ended the route — and the property landed exactly on the
  hypothesis (vertex-tautness) the case-(5b) object is forced to
  satisfy; the calculus lemma `L048` gives, for the first time, a
  stated pathway by which power-freeness itself fights (the
  requirement both dead routes lacked); the floors moved again
  (atoms/\(\mathcal G\) at 20) and the first profile object exists as
  a concrete test bed. Against, unchanged: T5 is a conjecture (its
  order-19 kill test is running tonight), (F) has no proof step,
  Tier 0's forcing question is untouched, and every emptiness result
  trims the disproof side without paying the proof side. The
  increment is one point again: real structural progress on the
  deliverable, but the deliverable is still the reduction, not the
  conjecture.

## Resume reading

1. `STATEMENT.md`
2. the **Roadmap** section above, then `A023` (the interference
   dissection: the calculus T2–T4, the candidate lemma T5 with its
   kill tests and proof obligations, the forcing target (F), the two
   calibration objects — S022's proof leg) and `A019` (the case
   analysis, the engine/peel, the residual object — R1's foundation)
3. **First action: harvest the S022 follow-up**
   (`E022/data/followup_s022.json` — stage A: the order-19 exemplar's
   full cycle set vs T5; stage B: the order-20 profile rung; stage C:
   the order-19 unsplit count); nothing from it is citable until read
4. `E021/README.md` (the dissection instrument: extraction layer,
   45-anchor suite, the dichotomy probes) and `E022/README.md` (the
   ladder at 18–19: the first profile member, the dual-split check,
   the bucket statements)
5. `A021` (the congruence kill and the Petersen\(-e\) calibration
   discipline — now joined by the order-14 exemplar
   `M?AA@?WcKWHOWOL??` of `C041`; both bind every case-(5b)
   argument) and `A022`/`E020` (the chain package and its 15/16 kill
   rung)
6. `CLAIMS.md` rows `L048`, `C041`–`C043` (and `L039`–`L047`,
   `C036`–`C040` for the frame); `OBLIGATIONS.md` `G015`/`G013`/`G014`
7. `sessions/S022-…md` (this session: worker allocation, audits, the
   independent re-derivations) and `S019`–`S021` for the preceding arc
