# S025 — the S-gap census at the window bottom: poison-length gaps and tautness over the on-disk C4-C8-free classes

- Date: 2026-07-25
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1 (unchanged).
- Work / claim status: `active` / `open`.
- Strongest established facts: T5/`L049` (theorem, audited `R002`) with
  the unconditional spectrum identity `L048`(iii); **(F) ⟺ case (5b)
  empty below 36**, re-aimed by S024 as **(F-S) ∨ (F-T)** with the
  membership-collision form dead (`C045`); the trunk bound `L051`;
  floors: counterexamples \(\ge22\), tight 1-atoms \(\ge22\),
  \(\mathcal G\)-members \(\ge21\).
- Open obligations in scope: `G015` (exclude case (5b)), `G013`(a).
- Inherited next action: the S-gap census at the window bottom
  (`A025` T5) over the on-disk \(\{C_4,C_8\}\)-free classes at 18–20,
  with the gap-vs-order curve against 10–16 as the mechanism
  measurement; order 21 excluded until `E024` lands.
- Session goal: run the census with pre-registered outcomes (i)/(ii)/
  (iii), read the curve, and leave (F-S) either surviving its first
  kill test or dead with calibration object #3 named.
- Falsifiable next move: the census itself — a vertex-taut exactly-two
  member with \(S\cap\{6,14\}=\emptyset\) at 18–20 kills (F-S) as
  stated in-session.
- Background: `E024` (order-21 rung) **running throughout** (parts 0–7
  of 16 in flight at session start, confirmed via `pgrep`; status file
  says stage B running); untouched, excluded from every ledger row,
  not harvested here (user confirmed at session start it would not
  land during this session). The census is throttled around it: at
  most 3 workers at `nice -n 15` against `E024`'s 8.

## Strategy audit

- Tier served: **Tier 1** (`G015`, case (5b), proof side — the (F)
  program's first move after the S024 re-aim).
- Why the inherited route might work: the census is itself the
  failure-first move — it searches the exact stratum where the
  residual object must live (the window bottom) for the object that
  would kill (F-S), and both outcomes are decisive and pre-registered
  (`A025` T5): survival where the residual object lives, or
  calibration object #3 and a forced re-aim onto (F-T).
- Fastest way to falsify it: not applicable in the usual sense — the
  census **is** the kill test; its cost was estimated at hours and
  measured in minutes (the membership-bit design replaces full path
  enumeration).
- Mechanistically distinct alternatives weighed: (i) start the
  saturation/interpolation proof attempt directly (through-set lower
  bounds in taut windowed pairs) — rejected first: the census either
  falsifies its target or shapes it, at ~1000× less cost, and the
  design discipline says run the kill test before the proof attempt;
  (ii) attack (F-T) (cycle-space compression for
  \(16\in\mathrm{Spec}\)) — deferred: the census re-reads the class
  \(C_{16}\) status for free (outcome (iii)), so (F-T) data arrives
  anyway; (iii) Tier 3 legs (`C038` 15/16 rung, cubic 26/28) —
  harvest-only by standing rule, not selectable as primary.
- Design refinement recorded (not a scope change): `A025` T5 says
  "per member compute \(S\)"; the exactly-two stratum at 18–20 is
  already fully decided on disk (the eight profile objects, all
  \(S\ni6,14\)), so a member-only census would be vacuous. The
  faithful nonvacuous form quantifies over **every unordered pair of
  degree-2 vertices** of every class member (the exactly-two stratum
  is then the (F-S) hypothesis class proper, and the wider pair
  census is the mechanism curve the redirect asked for). Gap bits are
  computed by an exact-length existence search (new code, anchored
  against two independent full enumerators); tautness and full \(S\)
  are computed for every gapped pair and every exactly-two member by
  the anchored `E018` enumerator, per the T5 design ("tautness for
  the members with a gap").
- Selected route and reason: the inherited census, with the pair-level
  refinement above — cheapest decisive move on the only surviving
  proof-side program.
- Pivot criterion: a vertex-taut **exactly-two** member with
  \(S\cap\{6,14\}=\emptyset\) at 18–20 → (F-S) dead as stated,
  calibration object #3 named, attack shifts to (F-T) (recorded
  in-session, not deferred). A vertex-taut gapped pair on a
  **non**-exactly-two member does not kill (F-S) but recalibrates the
  mechanism target (the interpolation lemma must then consume the
  exactly-two profile, not just tautness). Soundness alarms armed:
  any census disagreement with the recorded reference data of the
  ten named objects (anchor layer) halts production.

## Work performed

- Built `E026` (`census.py` + `anchors.sh` + `run_census.sh`): the
  S-gap census. Import chain: `E019/scan.py` by `E022`'s `load_scan`
  pattern (DATA rebound, E019 asserted untouched, generator binaries
  never invoked) + `E021/dissect.py` → `E018/mod4.py`
  `paths_with_essential` by `E025`'s pattern. New code only: the
  exact-length existence DFS (admissible BFS-distance pruning; parity
  shortcut — which never fired, the censused classes contain zero
  bipartite members) and the tally/harvest/analyze layer.
- Anchor gate before production: `E021`'s 45-check suite through the
  import + 57 new checks, under CPython 3.14.2 **and** PyPy 7.3.23 —
  named-object checks (the calibration pair must be *found*
  gapped+taut; the eight profile objects matched field-for-field
  against `t5_n20_profile.json`/`collect_n20_part14.json`/
  `exemplars_n19` values), exact-length DFS controls, a
  three-enumerator cross-algorithm sweep (20,554 pairs), and
  inventory ties (class files vs the authoritative scan tallies).
  The gate caught a records discrepancy: the S022 caveat's "572,530
  saved" at order 20 counted the 11 class-file header lines; the true
  sample is **572,519** graphs (scan tallies also re-summed to
  2,569,481 over all 16 parts). Corrected in `E026`'s constants and
  README; recorded here.
- Production: orders 10–17 in one process; orders 18/19/20 as
  16+16+11 part jobs on **3 workers at nice 15** (machine-resource
  rule: `E024` held 8 cores at nice 0 throughout and was never
  touched); the supp14 stratum; harvest with identity assertions;
  the `analyze` secondary cuts. Run twice: the first run stored all
  540,127 gapped rows (~350 MB); storage was trimmed to taut-only
  rows and the entire production re-run — **identical tallies**
  (`run1_tallies.json` vs the final `census_summary.json`,
  asserted).
- `E024` ran throughout, untouched, excluded from every ledger row
  (user confirmed at session start it would not land today; `pgrep`
  and its status file checked read-only at session start).

## Results

- **Computational evidence (`C046`, the census verdict):**
  - **(F-S) survives its first kill test** (pre-registered outcome
    (i)): zero exactly-two members of any censused class are gapped;
    the hypothesis class of (F-S) has exactly eight known
    realizations (order 19: 1; order 20: 3 in the sample + 4
    recollected), every one with \(6,14\in S\), re-verified.
  - **The tautness-only saturation mechanism is refuted**: 9,061
    vertex-taut gapped pairs in the same classes (8/8/371/24 at
    orders 12/14/16/17, **2,727/167/5,756** at 18/19/20 — rate
    0.01–0.2% of pairs, no monotone decay), 6,934 of them full
    \(\mathbb P{-}2\) dodges (\(2,6,14\notin S\)). Tautness +
    \(\{C_4,C_8\}\)-freeness + window order do **not** force the
    poisons.
  - **The dodge reaches every residual-object hypothesis except the
    profile**: 5,419 taut gapped rows sit on power-free
    (\(C_{16}\)-free) members, most 2-connected — so at orders 18–20
    there are 2-connected \(\{C_4,C_8,C_{16}\}\)-free vertex-taut
    pairs with \(S\cap\{2,6,14\}=\emptyset\) and 4–11 degree-2
    vertices. The (F-T) double blocking is likewise profile-specific.
  - **The gradient**: minimum degree-2 count of a dodge-carrying
    member is 5/6/**4** at 18/19/20 (order-20 histogram
    \(4{:}6,\dots,11{:}8\)); no taut gapped pair on a \(\le3\)-bucket
    member at any order (thin strata, recorded as data not
    mechanism).
- **Provisional (labelled, program structure):** the interpolation
  lemma's sharpened specification — it must consume min degree
  \(\ge3\) off the terminals; target form
  \(S\supseteq[c,n-1]\), \(c\le14\), on the window. Not a claim;
  the next attempt's target.
- **Records correction:** the order-20 on-disk sample is 572,519
  graphs, not 572,530 (header-line miscount in the S022 caveat; the
  class-level figure 2,569,481 and all profile conclusions
  unaffected — they were built on scan tallies, not class files).

## Failed routes and why

No route died: the census was a pre-registered two-outcome
instrument and outcome (i) occurred. What it *refuted* is a
mechanism hypothesis inside `A025` T4's frame: "tautness + class +
order force the poisons" is false 9,061 times over, so the weakest
viable interpolation lemma is the profile-consuming one. The
near-miss corpus (all rows stored with full \(S\), tautness,
\(C_{16}\) status) is the salvage — it is simultaneously the raw
material for extracting the mechanism and the standing refutation
set for any draft lemma that overclaims.

## Adversarial check

- The census had to *find* the known dodges, not merely avoid false
  alarms: the calibration pair (Petersen\(-e\), the order-14
  exemplar) is asserted found as gapped+taut in the anchors, and the
  eight profile objects asserted saturated with \(S\), tautness, and
  \(C_{16}\) counts equal to three prior experiments' records.
- Every gapped pair and every exactly-two member was recomputed in
  full by the independent `E018` enumerator with the 6/14 verdicts
  asserted against the bit search (540,135 agreements per run);
  a deterministic stride sample (3,867 pairs, 2,642 of them taut)
  cross-checked the non-gapped majority; three independently written
  enumerators agreed on the 20,554-pair anchor sweep.
- Per-line integrity asserted on every member (degree-2 count and
  edge count recomputed); the `power_free` flag re-verified by
  `has_cycle_len` on every 500th member (1,510 rechecks) and on
  every gapped row; class-file totals asserted against the
  authoritative scan tallies (which exposed the 572,519 correction).
- The whole production was run twice (before/after the storage trim)
  with identical tallies; anchors passed under both interpreters.
- Scope discipline: order-20 statements are sample statements (11/16
  parts + the four recorded part-14 members); nothing is claimed
  about the five uncensused parts or orders 21+.

## Canonical records changed

- [ ] `STATEMENT.md` (unchanged — no statement change)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`C046` new)
- [x] `OBLIGATIONS.md` (`G015` S025 update)
- [ ] `PROOF.md` (unchanged — integrated argument did not change)
- [ ] `DECISIONS.md` (unchanged — no statement or architecture
  change: the census refined the candidate mechanism *inside*
  `A025` T4's frame, which already listed the profile degrees among
  the hypotheses; (F-S)/(F-T) stand verbatim)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: counterexamples \(\ge22\) (window \([22,24]\));
  tight 1-atoms \(\ge22\), \(\mathcal G\)-members \(\ge21\); case
  (5b) below 36 ⟺ (F) = (F-S) ∨ (F-T); **(F-S) past its first kill
  test** with the interpolation lemma's spec sharpened to
  profile-consuming; the 9,061-row near-miss corpus on disk;
  `E024` (order 21) still running.
- Remaining blockers: no proof step exists for (F-S) or (F-T); no
  recorded technique converts "min degree \(\ge3\) off the
  terminals" into path-length lower bounds; no exactly-two data
  above order 20 beyond the eight objects (until `E024` lands).
- Recalibration decision: **continued** — the inherited census was
  run as designed, produced its pre-registered outcome (i), and the
  redirect stays inside the (F) program with a sharper target.
- Best live alternative or reframing: (F-T) via cycle-space
  compression if the interpolation attempt stalls; the `C038` kill
  rung and disjoint long-link descent behind it; Tier 2 bipartite
  EGC as the standing restricted-class theorem.
- Pivot trigger: a gapped vertex-taut **exactly-two** member at
  order 21+ (kills (F-S), calibration object #3 — check each new
  ladder rung); a power-free vertex-taut (5b)-profile pair in-window
  (defeats both forms, disproof-adjacent); a draft interpolation
  lemma that *holds* on the near-miss corpus (unsound by
  construction — the corpus is the refutation set); `E024` outcomes.
- Best next action: the profile-consuming interpolation attempt
  (open the attempt record; dissect the corpus against the eight
  profile objects; extract and calibrate the candidate reroute
  mechanism), harvesting `E024` first if it has landed.
- Files a new session should read: `STATE.md` resume list (`A025`
  and `E026/README.md` first).

## Plain-language recap

The surviving proof route says: a graph shaped like the dangerous
configuration — every vertex carrying terminal-to-terminal traffic,
no forbidden cycles, and exactly two low-degree vertices — must
always contain a path of one of the two "poison" lengths (6 or 14)
if it is small enough, which would put the whole dangerous case out
of existence below 36 vertices. This session ran that claim's
cheapest possible kill test: a complete census of every candidate
pair in every graph database the project has generated — nearly
nineteen million pairs across three-quarters of a million graphs,
sizes 10 through 20, the search code triple-checked against older
independent programs and the entire run performed twice with
identical counts. Two findings. First, the claim survived exactly
where it must: among graphs with the dangerous configuration's
precise shape, there are only eight in existence (sizes 19–20), and
every one carries both poison lengths — no shape-matching escape
exists anywhere on disk. Second, the census revealed what the claim
actually runs on: graphs *near* the shape (three or more low-degree
vertices instead of exactly two) escape the poisons over nine
thousand times, on graphs otherwise indistinguishable from the
dangerous configuration — so the escape phenomenon is real, abundant,
and stops precisely at the shape itself. The "every vertex carries
traffic" property alone forces nothing; the two-low-degree-vertex
shape is what does the work. That converts a vague hope ("saturation
happens at these sizes") into a concrete mathematical question with
a built-in test bed: prove that demanding degree three everywhere
except the two terminals forces paths of every length, and check any
proposed proof against the nine thousand stored near-misses (it must
fail on them) and the two known small escapes (it must fail on those
sizes too). A small bookkeeping error from two sessions ago was also
caught and fixed: the size-20 database holds 572,519 graphs, eleven
fewer than recorded — file headers had been counted as graphs;
nothing built on the wrong figure.

## Proposed next step

Open the proof attempt against the sharpened target: why does
"degree at least three everywhere except the two terminals" force a
terminal-to-terminal path of every length from some small threshold
up? Concretely: dissect the census's nine thousand near-miss escapes
against the eight shape-matching graphs — where do the extra
low-degree vertices sit, and which length-adjusting detours do
degree-three vertices enable that the near-misses lack — extract the
candidate mechanism, and calibrate it (it must fail on the
near-misses, fail at sizes 10 and 14 on the two known escapes, and
succeed on the eight). This would either produce the missing lemma —
closing the dangerous case below 36 vertices, the programme's
centerpiece — or show concretely which extra ingredient the lemma
needs. Deferred alternative: attacking the 16-cycle variant of the
forcing claim first (the census showed it is equally profile-bound,
so the same dissection feeds it). The overnight size-21 search keeps
running and is harvested first once it lands.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 8%
- Previous estimate, if any: 8% (S024)
- Reason for change: none — held.
- Basis: the census's halves cancel. For: (F-S) survived its
  cheapest kill test where the residual object lives, and the
  missing tool's specification is now empirically forced (consume
  the profile; nothing weaker is true — 9,061 witnesses). Against:
  the dodge grows right up to the profile wall (four degree-2
  vertices at order 20, on otherwise residual-shaped power-free
  2-connected graphs), the hypothesis class has eight data points
  total, and no recorded technique yet converts the profile
  hypothesis into path-length lower bounds. The route is better
  aimed but not easier.

This is a subjective research outlook, not mathematical evidence or a
claim-status promotion.
