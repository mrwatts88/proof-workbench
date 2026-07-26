# Project state

Last reviewed: 2026-07-26

## Mission

Find genuinely open conjectures and settle them — by proof, disproof, or
precisely delimited new partial results. Lean on all existing verified
knowledge to stand at the published frontier immediately; the work that counts
is what passes the frontier and produces information the mathematical
community does not already have. Re-deriving known results for internal
provenance is explicitly not a goal. The repository makes uncertainty visible
and every status promotion auditable.

## Current phase

The first problem, worked before the mission was clarified, has an internally
proved result that passed its adversarial review gates. The active research
dossier targets the Erdős–Gyárfás conjecture, which is open in the literature.

## Active problems

- `P-001` — Unique Common Neighbor: proved internally for statement version
  0.2. It was historically run under a since-retired internal-only rule, so no
  reference comparison has yet been made; that comparison is now freely
  permitted and simply optional.
- `P-002` — Erdős–Gyárfás Conjecture: active and open at statement version 0.1.
  The finite frontier stands at `L022` (every counterexample has at least
  **nineteen** vertices; extremal \(\{C_4,C_8\}\)-free window \([19,24]\);
  census capped at order 18). The voltage-lift falsification program is
  closed as a theorem (`L023`/`L024` collision-wall, reviewed `R001`);
  the walk-to-cycle interface is the **atom question** (`L025`, `G013`),
  taut-relativized (`L026`–`L029`), closed \(C_4\)-only through
  \(s_{\min}=3\) (`L030`), and collapsed onto **blocks** by S014
  (`L031`/`L032`: taut 2-atoms exist iff a power-free vertex-taut
  2-connected core with \(s_{\max}\le2\,s_{\min}\) exists). **S015
  proved the band-4 pencil dichotomy (`L033`)** — in any graph with
  \(d(x,y)=4\), either two internally disjoint 4-paths exist
  (equivalently a \(C_8\) **through both terminals**) or all 4-paths
  share one internal vertex; no \(C_4\)-freeness needed, and under
  \(C_4\)-freeness the pencil is terminal-adjacent with a rigid fan —
  so band 4 of the block question is exactly the **pencil endgame**:
  no vertex-taut 2-connected \(C_4\)-free core with \(d(x,y)=4\),
  \(s_{\max}\le8\) can be pencil-type. Catalogue through order **16**
  (`C032`; `C035`, the S017 harvest of the billion-graph order-16
  scan): **eight equality blocks** — the five known plus F16 (band 4,
  terminal degrees (3,3), on a sub-cubic-free graph), G16 (band 4,
  (2,4)) and H16 (band 6, first block with \(C_{16}\) in spectrum) —
  every one at exact equality; no strict taut pinched pair at 16 at
  all; all band-4 cores disjoint-type, so the pencil endgame's empty
  base and the 100% interference census extend through 16; the
  strict-15 scan = exactly D14's predicted pendant lift. Hypothesis necessity (`C033`): with \(C_4\)s allowed,
  strict blocks exist from order 6 and \(C_8\)-free band-4 equality
  cores from order 9 — \(C_4\)-freeness is essential to both rungs.
  Three hand constructions against the endgame died to the cascade
  obstruction (`A015`). **Mid-session a user-supplied external memo was
  audited (`A016`) and its core confirmed as `L034`:** the ring
  criterion is any-\(L\)-sumset avoidance, not just the pinch — parity
  (all-odd \(S\); bipartite instance), odd-prime gcd, and mod-4
  channels join the pinched one (fatal invisible shapes:
  \(S=\{3,7\}\), \(\{2,6\}\)); all channels are empty through order 15
  because `C027` is profile-agnostic; the "pinch = the criterion"
  glosses are retracted (no proved row false); the program ceiling is
  explicit (assembly closure + 1-atoms = cubic reduction, not 0.1);
  `G014` opened for the memo's unverified literature/census leads.
  **S016 proved `L035`, the parity structure theorem**: for a
  vertex-taut two-terminal graph, parity-constancy of the through-set
  is *equivalent* to bipartiteness, so (a) any connected bipartite
  power-free graph with \(\le2\) sub-cubic vertices disproves 0.1 with
  no path enumeration and no external import, and (b) bipartite
  generation is exhaustive for `L034` channels (i) and (iii) modulo
  1-atoms. `E015`/`C034` then searched that class exhaustively: **no
  power-free member at any order \(\le23\)** (24 with a pendant;
  extended by the S018 order-22 leg and the S019 order-23 harvest) —
  six orders past the general wall — every member blocked by a
  \(C_8\), never fewer than 13 of them; by-products at the same
  orders: no bipartite tight 1-atom and no bipartite counterexample
  (verifying internally the range `G014` item 2 was to supply, which
  is now de-gated). Not covered: `L034` channel (ii), the
  odd-prime-gcd channel (\(\Theta(3,3,3)\) is vertex-taut and
  non-bipartite with \(S=\{3\}\)) — now the only congruence channel
  with no structure theory. **S018 audited the architecture
  itself (`L036`)**: a counterexample plus one pendant vertex is a
  1-atom, so the unrestricted 1-atom question is *conjecture-complete*
  - it was never a sub-question, which is why sixteen audits deferred
  it. `L029`'s "cubic reduction modulo 1-atoms" was therefore vacuous
  and is restated with **tight** 1-atoms (exceptional degree exactly
  2), where it holds; `A012` Remark T4.1 is withdrawn as unproved and
  `A016` M6's ceiling is corrected (it was circular). `G015` opened:
  the **cubic reduction** as the programme's named proof-side
  deliverable, with two non-circular routes (no tight 1-atom; or Carr
  4/7 -> 1). The portfolio is retiered around it in `STATE.md` (Tier 0
  the conjecture, Tier 1 `G015`, Tier 2 restricted-class theorems,
  Tier 3 cheap legs that run but are never selected, Tier 4 the
  generator build), with a new process rule that every strategy audit
  name the tier its route serves. The bipartite hunt's order-22 leg
  completed empty (178,549 in class).
  **S019 (the first orchestrated parallel session, per `O011`: two
  audited Opus workers, one per `G015` route) advanced both routes and
  narrowed the deliverable to one configuration.** R2 side: Carr's
  paper verified line-by-line (`C004`–`C006` now at verified strength,
  the R2 gate discharged), the density bound pushed to
  \(3|V_3|\ge2n+3\) (`L038`) via the new **subdivision descent**
  (`L037` — the link graph on the degree-\(\ge4\) set is power-free
  and 2-degenerate; the dossier's first mechanism converting
  minimality into structure on an unbounded object), and the constant
  route **closed with a tombstone**: S15 (15 vertices, `E017`)
  realizes every non-power hypothesis at density exactly \(2/3\), and
  no constant \(<1\) delivers the reduction. R1 side: the closure
  calculus and (3,3) **bijection** onto the congruence class
  \(\mathcal G\) (`L039`), the **engine + peel** (`L040` — any
  counterexample below the minimum atom order yields a *cubic* one,
  repairing the withdrawn `A012` T4.1), and the five-case analysis
  (`L041`): **the cubic reduction now holds modulo excluding case
  (5b)** — a minimum-order tight 1-atom closing a vertex-taut
  \(\mathcal G\)-member — with every tight 1-atom of order \(\ge17\)
  and the residual object 2-connected, non-bipartite (hand proof,
  `L042`), and arithmetically squeezed. The routes meet on the link
  graph. R1 is reframed to its conditional form (all `G015` needs);
  the unconditional form is retired as a target.
  **S020 spent both Tier 1 legs decisively.** The order-16
  \(\mathcal G\)-profile scan (`E018`, anchored against `E016` A6 and
  `C027` before production) came back **empty** — 346,573,602 stream
  graphs (split-sum reproduced by an independent unsplit `geng -u`),
  29,713,305 in the profile class, **every one blocked by a \(C_8\)**
  (\(C_{16}\) never decisive), zero power-free (`C036`) — so the class
  \(\mathcal G\) has no order-16 member and **every tight 1-atom has
  order \(\ge18\)**; the minimum \(C_8\) count over the class is **1**
  (the closest any scanned class has come to a witness — the case for
  the `G014` item-6 generator). And the mod-4 congruence hunt died on
  its pre-registered kill condition (`C037`/`A021`): the residual
  object's forced membership triple is realized by vertex-taut
  \(C_4\)-free cores from order 10 — one witness is **Petersen minus
  an edge** — with no residue structure, and the chain-calculus
  identity caps congruence information at parity, so **no
  congruence-type theorem at any modulus can exclude case (5b)** from
  the forced hypotheses alone. Petersen\(-e\) is the standing
  calibration object: any future exclusion argument must fail on it
  unless it invokes power-freeness or minimality. Case (5b)'s
  surviving levers: the chain-cancellation tension (proof side) and
  the generator-powered order-17 rung (search side).
  **S021 (second orchestrated parallel session; one `fable` worker on
  the proof leg, one `opus` worker on the instrument leg, both audited
  with reproductions) spent both recorded moves and moved the
  frontier.** Proof side: the chain-cancellation tension is now a
  theorem package (`L043`–`L046`) — the cancellation is *quantified*
  (exactly three equal-exponent collision patterns per cut, so
  membership arithmetic provably cannot exclude the chain case) and
  per-block order bounds confine any chain-shaped residual object to
  order \(\ge36\): **below 36, case (5b) is a single 2-connected
  configuration**; the chain-case analogue of Petersen\(-e\) does not
  exist over blocks of order \(\le14\) (`C038`; the 15/16 rung is
  named). Search side: the dedicated \(\{C_4,C_8\}\)-free generator is
  **built and verified** (`E019`/`C039`: geng + PREPRUNE plugin, 146
  anchors under both interpreters, 23 set-equality checks against the
  old pipeline, cubic-24 positive control = Markström's census);
  **order 17 is empty** — tight 1-atoms \(\ge19\), \(\mathcal
  G\)-members \(\ge18\), `C027`'s class empty through 17 — and the
  min-degree-3 sweep through order 19 (slice-audited at 18 against the
  old instrument) gives `C040`/`L047`: **every counterexample has at
  least 20 vertices** (window \([20,24]\)). A user-supplied
  MathOverflow-512914 claim that order 20 was already settled was
  audited: its cubic-20 computation is right (and matches `E019`
  independently), but its cubic→min-degree-3 step assumes exactly the
  open cubic reduction and was rejected as an import; the internal
  order-20 run (plus bipartite 24 on the new instrument) was launched
  as the close-of-session background follow-up.
  **The same-day follow-up harvest landed all three stages** (fresh
  reconciliation commit): stage A reproduced both MO cubic-20 figures
  exactly (510,489 = A002851; 36,101 \(C_4\)-free — MO-1/MO-2
  corroborated; the rejected inference stays rejected and is now
  moot); stage B (min-degree-3 order 20, `genc48 -d3`, 16/16 parts)
  came back **empty**, extending `C040` to 14–20 and lifting `L047`
  to **every counterexample has \(\ge21\) vertices** (extremal window
  \([21,24]\), four orders wide); stage C (bipartite order 24,
  `genc48 -b`, 16/16 parts) came back **empty**, extending `C034`
  through 24 (25 with a pendant). The order-18 audit slice completed
  clean — all three sampled slices (38.7M graphs, ~24% of the stream)
  agree with the generator.
  **S022 (third orchestrated parallel session; W1 `fable` on the
  dissection, W2 `opus` on the ladder, both audited with independent
  re-derivations) ran both recorded moves to verdicts.** Proof side:
  the interference dissection landed the **interference outcome** —
  all 553 blocking \(C_8/C_{16}\)s of the closest known objects (the
  min-\(C_8\) exemplars at 14–16, exhaustively re-extracted, and the
  three-degree-2 \(C_{16}\) boundary at 16–17) are two-through-path
  symmetric differences (`C041`); the non-interference pivot trigger
  did **not** fire; the property is empirically **exactly
  vertex-tautness-shaped** (`C042`: biconditional at 10–12; zero
  failures over all taut pairs, orders 4–7), with the calculus proved
  (`L048`: interference = the \(t=1\), leak-pinned case of the chain
  identity; under completeness \(\mathrm{Spec}(B)=T_1\cup(S+2)\) —
  power-freeness becomes through-path arithmetic, the genre surviving
  both kill theorems). Candidate lemma **T5** and forcing target
  **(F)** recorded with ordered kill tests; a second calibration
  object (order 14, full membership triple) joins Petersen\(-e\).
  Search side (`C043`): order 18 profile-empty; order 19 the
  **first-ever nonempty profile rung** — its unique member
  vertex-taut, 2-connected, non-bipartite, and blocked twice
  independently (46 \(C_{16}\)s; \(S\ni6,14\)).
  **The same-conversation follow-up harvest (2026-07-25) landed:**
  stage A — **T5 survived the exemplar**, 411/411 cycles decompose
  (determined-partner algorithm, independent of `E021`'s); stage C —
  the order-19 unsplit count 74,589 **exact**; stage B — **order 20
  spent** (class 2,569,481; profile 7, all \(C_{16}\)-blocked, none
  power-free; 0-/1-buckets empty), and the three on-disk profile
  members all pass verification and T5 (1,890/1,890; all with the
  same \(S\ni6,14\) double blocking) — so **every \(\mathcal
  G\)-member has order \(\ge21\) and every tight 1-atom \(\ge22\)**
  (`L041` cases (4)/(5) propagating `L047`; direct generation gives
  21). **The second harvest closed the run (2026-07-25):** the
  part-14 recollection recovered the four remaining order-20 profile
  members (stream 439,745 reproduced exactly; all vertex-taut,
  2-connected, \(S\ni6,14\)) and **T5 survives on all four** — so
  **all eight profile objects in existence survive T5, 4,661/4,661
  cycles, every one \(S\ni\{6,14\}\)-double-blocked** — and the
  stage-D min-degree-3 order-21 sweep came back **empty**: `C040`
  runs 14–21 and **every counterexample has \(\ge22\) vertices**
  (`L047`, extremal window \([22,24]\), three orders wide).
  **S023 (2026-07-25) closed the T5 program: T5 IS A THEOREM.** The
  two remaining pre-registered kill rungs ran **first** and survived
  (`C044`: `smallworld 13` exhaustive in-class with the tautness
  biconditional exact — all 10,853 taut members pass on 1,614,300
  cycles, all 113 non-taut members fail; the general probes clean
  with order \(\le8\) **exhaustive** — every graph, every vertex-taut
  pair, every cycle — and cyclomatic-bounded slices at 9–11). Then
  the proof landed (`A024`, promoted `L049`): every vertex-taut pair
  is interference-complete, in trunk-identical arc form with
  prescribed-edge freedom, by the **trimming construction** — the
  recorded weaving obstruction is discarded with the trimmed middle,
  never controlled; **Lemma A** (cycle-edge essentiality in taut
  pairs) proved en route. Delegated fresh-context audit `R002`:
  **PASS at lemma level** (0 critical / 0 major; 2 minor + 6 notes,
  all repaired in place), with the reviewer independently re-running
  every `E023` command and re-verifying the claim set with its own
  implementation. Mechanically verified per instance (17.4M
  (cycle, edge) instances incl. all eight profile objects).
  Consequences: interference-complete ⟺ vertex-taut on connected
  \(\delta\ge2\) graphs (`L050`); the case-(5b) residual object's
  spectrum identity is **unconditional** (`L048`(iii):
  \(\mathrm{Spec}(B)=T_1\cup(S+2)\), every element a trunk-split
  pair value) — **the forcing target (F) is now the entire proof
  side of case (5b) below order 36**, and (F) ⟺ that case's
  emptiness there. Floors unchanged (counterexamples \(\ge22\),
  window \([22,24]\); atoms 22/21). At close, the order-21
  \(\mathcal G\)-profile rung was launched as `E024`
  (\(\approx\)21 h on 8 workers; **running, not citable**).
  **S024 (2026-07-25) spent the (F) opening probe — pre-registered
  branch (b).** The complete trunk-split realization tables of the
  ten named objects (`E025`/`C045`: 604 power cycles, 61,901
  witnessing pairs, 1,971 trunk-split realizations, every `L049`
  invariant asserted, anchors 45+14 both interpreters, CPython
  payload identical, no soundness alarm) show **no
  membership-patterned regularity** — none of the nine pre-registered
  patterns is universal, 30 cycles are membership-blind outright, and
  the calibration pair's 100% power-participant structure is a
  small-order artifact — so the **membership-collision form of (F)
  is dead** (`A025` T1; the empirical third leg beside
  `C037`/`L045`). Proved en route: **`L051`, the trunk bound**
  (\(s\le n-L\), hence \(x+y\le2n-L\); **tight on all ten objects** —
  the case-(5b) collision system is order-confined). Saturation
  recorded: all eight profile objects have spectrum exactly
  \([3,n]\setminus\{4,8\}\) and \(S\supseteq[6,n-1]\ni6,14\); the
  only known \(\mathbb P-2\) dodges are the calibration pair (orders
  10/14, both gapping \(S\) exactly at 6). **(F) is re-aimed as
  (F-S) ∨ (F-T)** (`A025` T4, both order-windowed, both correctly
  failing off-window on the calibration pair): the window forces
  \(S\cap\{6,14\}\ne\emptyset\) (closure blocked), or forces
  \(16\in\mathrm{Spec}\) (\(H\) blocked) — either closes case (5b)
  below 36. First move: the **S-gap census** over the on-disk 18–20
  classes (+21 when `E024` lands). `E024` ran throughout, untouched,
  **still running**.
  **S025 (2026-07-25) spent the census — pre-registered outcome (i)
  with a decisive mechanism recalibration.** Over **18,754,354**
  degree-2 pairs of the on-disk classes (`E026`/`C046`; orders 10–19
  complete, order 20 the 572,519-graph 11/16-part sample — the S022
  "572,530" figure had counted 11 file headers — plus the four
  recorded part-14 profile members; anchors 45+57 both interpreters;
  two production runs, identical tallies): **zero (F-S) kill
  candidates** — no exactly-two member is gapped, the eight profile
  objects re-verified saturated — so **(F-S) survives its first kill
  test where the residual object lives**. The other half: **9,061
  vertex-taut gapped pairs off the profile** (2,727/167/5,756 at
  18/19/20, no decay; 6,934 full \(\mathbb P{-}2\) dodges; 5,419 on
  power-free members, most 2-connected; min degree-2 count 5/6/4,
  never \(\le3\)) — **tautness + class + window order force
  nothing**: any interpolation lemma proving (F-S) must consume the
  exactly-two profile (min degree \(\ge3\) off the terminals), and
  the (F-T) double blocking is likewise profile-specific. The stored
  near-miss corpus is simultaneously the mechanism's raw material
  and the refutation set for any overclaiming draft. `E024` ran
  throughout, untouched, **still running**.
  **S026 (2026-07-25) spent the dissection sub-move — the mechanism
  is extracted and the lemma splits.** The corpus dissection
  (`E027`/`C047`, attempt `A026`; anchors 35 checks both
  interpreters; every row re-validated, the `L035` parity alarm
  never firing): the dodge economy has exactly **three rigid
  shapes** — A (short: \(\max S=13\) *exactly* on every minimal
  full dodge at 16–20), A′ (distance: \(\min S=7\) exactly), B
  (long-range: holes exactly \(\{6,10,14\}\), even part
  \(\subseteq4\mathbb Z\), needing \(\ge7\) degree-2 vertices) —
  the dodge is **pair-local** (frontier members carry five
  saturated sibling pairs; member-level lemmas dead) with the
  frontier at **ndeg2 = 4 at order 20** (profile load-bearing by
  two subdivision vertices), and **99.1% of dodge rows smooth to
  class-violating reduced graphs** (near-misses are subdivisions
  escaping the class constraint; the profile is the
  subdivision-free stratum). Proved en route: the **span law** (no
  path chord of span 3 or 7 in a \(\{C_4,C_8\}\)-free graph). The
  **first-order chord-exchange calculus** (disjoint-chord surgery
  on one Hamiltonian path) generates the entire top of \(S\) down
  to 10 — including 14 — on **all eight** profile objects while
  filling no interval on any of the 36 Hamiltonian dodgers (their
  spans \(\equiv1,2\bmod4\) make the poison-hitting savings class
  \(\equiv3\bmod4\) unreachable). **(F-S) ⟸ (L-A) ∧ (L-B)**: (L-A)
  short-range exclusion (thin margin, no engine); (L-B) long-range
  poison forcing (engine validated — the span/savings combinatorics
  of longest-path chord systems, the sharpened missing tool).
  Killed: member-level lemmas, odd-cycle-supply discrimination.
  `E024` ran throughout, untouched, **still running**.
  **S027 (2026-07-25) turned (F) into a decision procedure — and it
  comes back empty on the Hamiltonian stratum.** Instead of proving
  the (L-B) savings lemma by hand, `A027` proves two reductions
  (`L052`): the **chord-minimal descent** (on a pair with a
  Hamiltonian \(a\)–\(b\) path the chords cover every path position,
  0 and \(M\) exactly once, and every inclusion-minimal subcover
  inherits the degree profile, the Hamiltonian path,
  cycle-length-freedom and the through-set — so the search may be
  restricted to chord-minimal systems) and the **monotone reroute**
  (interval-disjoint chord families are genuine \(a\)–\(b\) paths of
  length \(M-\sum(\sigma_k-1)\), with a left-to-right DP whose
  *prefixes* already certify a poison length). Two aims sharpened
  inside `A025` T4's frame, both strictly in our favour: decide the
  **disjunction** (F) directly rather than (F-S)/(F-T) separately —
  which supplies \(C_{16}\)-freeness as a **free** hypothesis, and
  that is exactly what cuts the enumeration's growth from
  \(\approx\times3.5\) to \(\approx\times1.9\) per order and brings
  the window \([18,35]\) into computational range — and use the whole
  poison set \(\{2,6,14,30\}\) (\(30+2=32\)). Verdict
  (`E028`/`C048`): **empty at every order 16–29** — the last completed
  rung — so case (5b) is closed there for every residual object carrying
  a Hamiltonian through-path. **Audited `R003`** (delegated fresh
  reviewer): PASS at lemma-and-instrument level, 0 critical / 4 major /
  4 minor / 3 notes, with the reviewer reproducing both runs' node counts
  to the last digit and re-deriving the run-B emptiness from its own
  from-scratch enumerator; all four majors repaired in place. Two of its
  corrections are load-bearing: the ladder is an **open-ended
  computation**, not a window closure (wall-clock growth 1.8–2.4 per rung,
  so orders 30–35 are days of single-core computing), and **above order 26
  the poison prune stops firing**, so orders 27–29 prove the *stronger*
  poison-free class-emptiness statement while exercising none of (F)'s
  forcing mechanism. The anchor repair matters too: before it, none of the
  three loss-capable prunes was ever exercised on a positive or nonempty
  instance. En route the \(\{C_4,C_8\}\)-only run exhibited the
  **first \(\mathcal G\)-profile objects at orders 21 and 22** (10 and
  43 chord-minimal ones, 3 and 16 isomorphism classes, all
  2-connected, girth 3, 91–186 \(C_{16}\)s), every one killed twice
  (\(14\in S\) on all 53, \(6\in S\) on 40, a \(C_{16}\) on all 53) —
  and **13 of the order-22 objects have \(S\) *not* a full interval**
  (8 with \([5,21]\setminus\{6\}\); 5 adjacent-terminal with
  \(\{1,5\}\cup[8,21]\)): the first in-window exactly-two objects to
  break the `A025` T3 saturation pattern while keeping the double
  blocking, so **saturation is not the mechanism** and any future
  argument must explain 14 and 16 specifically. Independent
  cross-check of the recorded ladder from a different generation
  principle (poison prune off: 0 covers at orders 12–18, 6 and 65 at
  19 and 20, only recorded signatures). Corrected en route (`A027`
  T6): interior-disjoint chords close **no** extra cycle with the
  path — a hand-table entry that was wrong, caught by the
  instrument's own anchors, nothing downstream affected. Adversarial
  audit `R003` delegated to a fresh reviewer. Named residue: the
  **non-Hamiltonian stratum** (`A027` T5), with a first purchase — a
  zero-savings two-attachment off-path component forces an
  all-equal-length, hence bipartite, interior-degree-\(\ge3\) gadget,
  exactly the class `L035`/`C034` empties. `E024` still running,
  untouched, excluded from every ledger row.
  **S030 (2026-07-26) spent the recorded next action, killed the
  deferred alternative, and named the programme's ceiling — all
  proof-side, with one read of data already on disk.** (i) `L053`: for
  every \(N\) there is a 2-connected exactly-two-profile pair of order
  \(\ge N\) with girth \(\ge17\) — hence no \(C_4\), \(C_8\),
  \(C_{16}\) — and **no Hamiltonian through-path** (a cubic
  non-Hamiltonian graph of large girth minus an edge; Haythorpe,
  independently Kochol's snarks plus the three-line proof that a
  Hamiltonian cubic graph is 3-edge-colourable). So `C049`'s 27/27 is a
  small-order **pattern, not a lemma**, the non-Hamiltonian stratum is
  unavoidable, and **calibration object #3** joins Petersen\(-e\).
  Asymptotic — nothing exhibited in \([18,35]\), no floor moves.
  (ii) `L055`, the **positive-savings theorem**: every off-path
  component of a longest through-path admits a bridge with savings
  \(\ge1\), and \(\ge2\) with three or more attachments (the
  Y-identity \(\sigma(i,k)=\sigma(i,j)+\sigma(j,k)+2\beta\),
  maximality alone); the two-attachment case runs through the new
  `L054` **bipartite exclusion dichotomy** with its power-freeness
  hypothesis finally matched. `A027` T5's zero-savings obstruction is
  **gone** and `L052`(iii)'s reroute machinery transports from chords to
  bridges — but the stratum is cleared at **no** order (`A028` T8: no
  component-atomic minimality; savings per component, not per position).
  (iii) **The ceiling.** `L046` supplies the 2-connectivity the whole
  (F) frame assumes only below order 36, so the (F) programme — complete
  on both strata — closes case (5b) for \(n_0\le35\) and **cannot
  prove `G015`**; with `R003` F4 and `L053` its top rungs prove
  something that must stop being true. The `E028` ladder is **demoted to
  a source of floors**. (iv) The successor is order-unbounded:
  **(INT) ∧ (L-A)** (`A028` T9) — (INT) says
  \(S\supseteq[8,\max S]\) for a vertex-taut \(\{C_4,C_8\}\)-free
  exactly-two-profile pair; with \(\max S\ge14\) it forces
  \(14\in S\), poison, hence (F-S) **at every order**, no window and no
  \(C_{16}\) hypothesis. `C050`/`E029` kill-tested it with **no
  generation**: 24 recorded profile objects, **zero violations**, every
  hole in \(\{4,5,6\}\); over the 9,061-row near-miss corpus the
  minimum degree-2 count admitting a hole is 4 for every value
  \(\le7\) and **5** at 8 (the constant is pinned from both sides),
  while a hole at **14** needs \(\ge7\) — five above the profile. New
  en route: a second non-interval profile object, at order 20. (INT) is
  a **conjecture**; 1,920 corpus rows refute it the moment the profile
  hypothesis is dropped, and they are its standing sanity check.
  Portfolio (all threads carried, per standing user instruction): the
  case-(5b) endgame (the **(F) program**, Tier 1, now the
  (F-S)/(F-T) pair with the **profile-consuming interpolation
  attempt** as its first move, fed by `E026`'s corpus; + the
  ladder at order 21+, `E024` running); the `C038`
  kill rung at block orders 15–16; the pencil endgame + band-2 rung
  (pinched channel); the bipartite hunt at order 26 (order 24
  harvested empty on the new instrument) and the gcd-channel theory
  question; the cubic census at orders 26/28/30 (~15 min/3.5 h/2.3
  days on 8 workers); census mining; bipartite EGC (proof side); the
  disjoint longer-link descent (R2's surviving extension);
  3-connectivity leverage; order-17+ pinched catalogue legs.  **S031 (2026-07-26) ran the kill test the recorded route had skipped, and
  the route is dead.** `A028` T9 had adopted **(INT)** — \(S\supseteq[8,\max
  S]\) for a vertex-taut \(\{C_4,C_8\}\)-free exactly-two-profile pair —
  as the order-unbounded successor architecture, on the strength of `C050`'s
  24/24. `C050` tested it against every profile object *on disk*; it was never
  tested against Calibration object #3, which the **same attempt** had
  constructed eight theorems earlier. **`L056`:** that object satisfies every
  hypothesis of (INT) and has \(\min S\ge16\), so **(INT) and (INT-14) are
  both false**. The delegated audit `R004` then made it far worse for the
  conjecture: the attempt had claimed no such object exists below order 70,
  and F4 refuted that with the **truncated Petersen graph** (every vertex
  blown up to a triangle; cubic, 3-connected, \(\{C_4,C_8\}\)-free) minus a
  link edge — order **30**, \(S=[9,26]\), so \(8\notin S\) — with a
  two-copy chain at order **59** giving \(S=[18,52]\) and \(14\notin S\).
  **(INT) is false inside the case-(5b) window**, not merely asymptotically,
  with no import at all (verified, `E030`). `C050` could not have caught it:
  nothing with \(\min S>8\) has ever been *generated*, because the ladders
  stop at order 21. **`L057`:** the natural repair fails too — the
  **triangle expansion** of a bipartite cubic 3-connected graph of girth
  \(\ge10\) and large order, minus an edge far from the triangle, is a
  *non-bipartite* class member whose through-set has a parity hole at
  \(\min S+1\ge10\) (verified end to end on an explicit 106-vertex graph,
  `E030`) — this half **failed** its audit twice and is **not
  established**: `R004` F3′ is still open (`X004`'s 3-connectivity clause has
  no source), so it is recorded at `proposed` and may not be cited. The genre
  conclusion does not depend on it — `L056` kills the absolute form and the
  bipartite one-liner kills the relativized form against a bipartite
  defender. **The interpolation genre is empty — the third dead genre** after
  congruence (`C037`) and membership (`L045`/`C045`), and all three fail for
  one reason (`A029` T3(a)): every class-level hypothesis is **local and
  hereditary**, hence inherited by large-girth cubic graphs minus an edge, and
  the two hypotheses the residual object has that those do not — power-freeness
  **above the girth**, and minimum-order minimality — have never been consumed
  by an (F)-side lemma. **`L058`** re-derives `A022` W1-T8 from the current
  block-order floor of 21: **either \(H\) is 2-connected or \(n_0\ge42\)**,
  so the case-(5b) window is \(n_0\in[23,41]\) (\(H\)-orders
  \([22,40]\)) and the stopped `E028` ladder is **ten** rungs short of it,
  not four — sharpening S030's ceiling finding rather than softening it.
  Conditional residue: an interpolation lemma would have pinned \(S\) into
  one dyadic band, \(\max S<2\min S+O(1)\) — `L031`/`L032`'s
  block-question constraint. No floor, status or statement changed; every
  refuting object contains \(C_{16}\). **Audited `R004`: FAIL at lemma
  level** (2 critical, 2 major, 4 minor, 2 notes) — T1 passed and was
  *strengthened* by F4, T2 failed and is repaired but unaudited, T3(b) passed
  up to side conditions now carried; all ten findings answered.

- See the generated [problem index](problems/INDEX.md).

## Repository-wide decisions

- Each problem is a self-contained dossier under `problems/<slug>/`.
- Workflow maturity and mathematical outcome are tracked separately.
- Atomic claims and unresolved obligations are first-class records.
- A proof is not complete until adversarial reviews and promotion gates pass.
- Agents initiate and delegate those reviews automatically when a candidate
  appears; humans do not schedule the review lifecycle. Delegation to a fresh
  reviewer is mandatory wherever the harness supports it, and how independence was
  obtained is recorded on the review.
- The operating contract is harness-neutral and works in either Codex or Claude
  Code; harness-specific files configure a harness but never hold process rules.
- Every internally proved result has a standalone LaTeX source, and the generated
  README dashboard displays both current status and prior-proof provenance.
- A proved result also has a committed PDF compiled by Tectonic, with the source,
  PDF, and compiler version recorded in its dossier.
- Repository process and tooling work is recorded separately under `operations/`;
  it does not count as progress on a mathematical dossier.
- Session continuity comes from concise handoffs plus detailed append-oriented
  records, not retained chat history.
- A recorded next action is the previous session's best proposal, not a command.
  Each nontrivial exploration session audits it against a fast falsification move
  and a mechanistically distinct alternative or reframing before committing.
- External knowledge is leaned on, never avoided: published theorems, bounds,
  computations, and examples are imported at their verified strength so work
  starts at the frontier. There is no internal-first or no-consultation rule;
  the retired benchmark-era rule on `P-001` must not be reintroduced. Novelty
  relative to the literature is checked deliberately, because producing new
  information is the point.
- `STATE.md` and session records preserve a compact strategy portfolio: primary
  route, live alternative, and pivot trigger. Fresh discovery agents may reduce
  anchoring where the harness supports them, but their suggestions remain
  speculative until checked by the primary agent.
- Missing tools are internal research targets: when the obstacle is "no known
  technique applies," strategy audits weigh a tool-building attempt with a
  falsifiable first move and kill condition; capability-based deference is not
  a valid route-selection reason, and estimates stay calibrated regardless.
- Closing a substantive session includes a mandatory canonical-record checkpoint;
  the human shorthand `close session` invokes the whole checkpoint.
- Each closure preserves a plain-language recap, a subjective percentage estimate
  of the chance of eventually settling the exact current statement, and a
  plain-language statement of the proposed next step.
- Two agents may work one dossier concurrently only under the record
  partition of `AGENTS.md` (Parallel sessions): owned records parallelize,
  shared ledgers are written one session at a time, record IDs are allocated
  in advance, and a sibling session is never a reviewer. Where the harness
  supports delegation, parallel legs run as worker subagents of a single
  orchestrating session that holds the ledgers throughout; two interactive
  sessions are the fallback, not the default.
- Computational work must be reproducible and its logical scope must be stated.

## Next action

**S032 (2026-07-26) supersedes everything below in this section.** The dossier now
has a **proved case of statement 0.1** — `L061`: every planar graph with
minimum degree \(\ge4\) contains a cycle of length 4 or 8 (also
projective-planar, and 2-connected toroidal/Klein), via `L060` and a discharging
bound \(m\le2n-2\chi(S)\) colliding with \(m\ge2n\); prior art swept in both the
Erdős–Gyárfás and planar-Turán literatures and not found. It also has a closed
channel (`L064` resolves `G013`(c), the odd-prime-gcd channel open since S016,
and every modulus with it) and **three barrier theorems that retire the
inherited programme**: `L059` (no subdivision-closed hypothesis can imply 0.1's
conclusion — which covers the whole (F) programme, `L048`–`L052` included),
`L062` (no additive surgery on a minimum counterexample can contradict
anything), `L063` (girth does not localize the spectrum). The new primary
obligation is `G016`: extend `L061` below \(\delta\ge4\) toward all planar graphs
with \(\delta\ge3\), closing the gap to Heckman–Krakovski's 3-connected cubic
planar case. See `problem.json`, `DECISIONS.md` and `sessions/S032`.

The paragraph below is the S031 state, retained for provenance:

For `P-002`, keep working **Tier 1: exclude case (5b)** — but by closing the
**non-Hamiltonian stratum**, not by any interpolation lemma. S031 refuted the
recorded successor architecture outright. `L056`: **(INT) and (INT-14) are false**,
with explicit witnesses of orders **30** and **59** — truncated Petersen minus
a link edge, and its two-copy chain — so the failure is *inside* the
case-(5b) window, not asymptotic. `L057`: the relativized repair fails too, on a
non-bipartite object. **The interpolation genre is empty**, the third after
congruence (`C037`) and membership (`L045`/`C045`).

**First action: close `A028` T8's two gaps**, using `L055`'s positive-savings
engine. They are named exactly: (1) there is no component-atomic minimal-cover
notion with a bound on the number of components — a component cannot be
thinned bridge by bridge, and dropping it destroys the degree profile at all
its attachments at once; (2) the savings are per component, while the
monotone-reroute DP needs an *interval-disjoint family* of positive-savings
bridges, and different components' good bridges may nest or cross. Closing
both makes the window's interior fully decided rather than half-decided, which
is the most any finite-window route can deliver. Kill condition: a power-free
2-connected profile pair whose off-path components provably cannot be thinned
to a bounded family — that is a named obstruction, and the route re-aims.

**Alternative considered and deferred:** build the first (F)-side lemma that
*consumes* power-freeness **above the girth** or minimum-order minimality —
the only shape of statement the three dead genres leave open, and the only
shape that can be order-unbounded. Deferred because no proof step exists for
it yet, while the non-Hamiltonian stratum has a proved engine and a bounded
objective.

**Binding kill discipline, strengthened by S031: Calibration object #3 is now
the primary calibration object for the (F) side**, ahead of Petersen\(-e\),
because it satisfies every class-level hypothesis simultaneously at
arbitrarily large order. Check every drafted lemma against it *before* working
on it; the check is mechanical — if the lemma's hypotheses are girth-monotone
and its conclusion names a specific value below the girth, it is false.

**Window, corrected (`L058`):** the case-(5b) window is \(n_0\in[23,41]\),
i.e. \(H\)-orders \([22,40]\). The `E028` ladder is **stopped** at
\(H\)-order 30 and is ten rungs short of that top; do **not** restart it,
and do not re-run `E024` (harvested, `C049`). Tier 3 stays harvest-only (the
`C038` kill rung at block orders 15–16; cubic 26/28; min-degree-3 at 22;
bipartite 26). Do **not** reopen congruence obstructions (`C037`),
membership-only chain exclusion (`L045`), the density constant (`L038`), the
membership-collision form of (F) (`C045`), the Hamiltonian-forcing route
(`L053`), or **interpolation in any form** (`L056`/`L057`). Live pivot
triggers: a power-free vertex-taut profile pair anywhere in \(H\)-orders
\([22,40]\) (disproof-adjacent, report immediately); and
any non-Hamiltonian-stratum lemma that **holds** on Calibration object #3 (a
soundness alarm on the draft). A non-decomposable cycle in a vertex-taut pair
remains a **soundness alarm** against the reviewed `L049`, not a route pivot.
No required action remains for `P-001`; its reference comparison is optional
and freely permitted.

## Known process risks

- A structurally valid dossier can still contain invalid mathematics.
- Independent review is a reasoning discipline, not something filenames can
  guarantee.
- Handoffs become misleading if agents omit the end-of-session checkpoint.
- Strategy audits can become empty ceremony if agents list cosmetic variants
  instead of comparing distinct mechanisms and acting on negative evidence.
- Imported results are only as good as their statement correspondence: a
  miscopied hypothesis or an overread bound silently corrupts everything built
  on it. Precise statements, matched hypotheses, and sources are mandatory.
- Effort can silently drift into re-deriving known results; route selection
  must ask what the work adds beyond the published frontier.
