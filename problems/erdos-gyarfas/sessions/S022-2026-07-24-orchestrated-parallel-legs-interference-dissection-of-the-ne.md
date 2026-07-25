# S022 — Orchestrated parallel legs: interference dissection of the nearest blockers (proof side) and the G-profile ladder at orders 18-19 (search side)

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L039`–`L047` (the conditional cubic
  reduction holds modulo excluding case (5b); the chain branch is
  confined to \(n_0\ge36\), so below 36 the residual object is
  2-connected; every counterexample has \(\ge21\) vertices, window
  \([21,24]\)); `C036`/`C039` (tight 1-atoms \(\ge19\), \(\mathcal
  G\)-members \(\ge18\), `C027`'s class empty through 17); `C037`/`A021`
  (congruence route dead; Petersen\(-e\) calibration discipline);
  `C031`/`C032`/`C035` (the pinched-world interference census: every
  \(C_8\) in every catalogued block/witness is a two-through-path
  symmetric difference, 100% at every order through 16); `C038` (chain
  kill test refuted through block order 14); `E019`/`C039` (the
  verified \(\{C_4,C_8\}\)-free generator, anchors 146/146 both
  interpreters).
- Open obligations in scope: `G015` (exclude case (5b)); `G013`(a).
- Inherited next action: primary (proof side) — the interference
  dissection of the closest known objects (min-\(C_8\)-count exemplars
  at orders 14–16 from the `E018` stream; three-degree-2
  \(C_{16}\)-blocked boundary graphs at 16–17 from `E019`); search
  side — the \(\mathcal G\)-profile ladder at orders 18–19 via `E019`.
- Session goal: run both legs concurrently under orchestrated mode
  (`process/concurrency.md`; one worker subagent per leg, this session
  holding all ledgers), audit, integrate, and reconcile.
- Falsifiable next move: per leg, below.
- Record repair on entry (user-requested): `PROJECT_STATE.md` still
  carried the pre-harvest "First action: harvest the S021 follow-up"
  sentence and the pre-harvest P-002 bullet tail, although the S021
  addendum records the harvest as landed and `problem.json`/`STATE.md`
  are post-harvest. Repaired before launch (harvest paragraph appended
  to the bullet; portfolio bipartite line moved to 25+; next-action
  paragraph now matches `problem.json`). No mathematical content
  changed.

## Strategy audit

Both legs serve Tier 1 (`G015`, case (5b)). The user endorsed the
inherited pair conditional on parallelizability; the audit below is the
session's own check, not a formality.

- Why the inherited route might work: (proof) after `C037` killed
  congruence obstructions and `L045` killed membership-only chain
  exclusion, the interference structure of the blocking cycles is the
  only recorded structural lever against the 2-connected case-(5b)
  branch — and it has a perfect precedent: the pinched-world census is
  100% interference at every catalogued order (`C031`/`C032`/`C035`).
  Either verdict moves the proof side: universal interference among the
  nearest objects names the candidate lemma the branch needs ("every
  power-blocker in the profile class is a two-through-path
  interference cycle" — which vertex-tautness plus the \(S\)-condition
  could then fight arithmetically); a non-interference blocker fires a
  recorded pivot trigger and redirects the proof side before more work
  is sunk into the pinched-world model. (search) Each rung is decisive:
  a profile hit passing the \(S\)-condition disproves 0.1 outright, an
  empty rung lifts the atom floor; the instrument is verified and the
  rungs cost minutes.
- Fastest way to falsify it: (proof) the dissection IS the
  falsification test — a single non-interference blocker among ~20
  boundary graphs and the min-\(C_8\) exemplars settles it negatively;
  (search) the anchor suite failing to re-pass would invalidate the
  instrument and abort the rung.
- Mechanistically distinct alternative or reframing: the disjoint
  long-link descent (`A020` W2-T8(c)) — deferred again: it needs a
  fresh re-audit of `A020`, has no data waiting on disk, and is not
  riper than a dissection whose inputs already exist; the `C038` kill
  rung at block order 15 — Tier 3 background by standing rule (run,
  never select), candidate for a close-of-session background launch;
  cubic order 30 (Tier 0's counterexample ticket, ~2.3 days) — a
  deliberate multi-day decision the roadmap defers until the cheap
  rungs are spent.
- Selected route and reason: both inherited legs in parallel. They are
  mechanistically distinct (structural dissection of existing data vs.
  generator production runs), dependency-free (neither consumes the
  other's output), and touch no common claim row; the admission rules
  of `process/concurrency.md` pass. Machine check at launch: load 1.92
  on 12 cores, no competing jobs.
- Pivot criterion: a \(\mathcal G\)-profile hit at 18/19 satisfying the
  \(S\)-condition → immediate disproof protocol, everything else
  stops; a non-interference blocker → the pinched-world model breaks
  and the proof side redirects (this is the dissection's own verdict,
  not a failure); anchors fail → the ladder aborts and the instrument
  regression becomes the finding.

## Worker allocation (declared before launch, per `process/concurrency.md`)

| Worker | Leg | Owned records | Model | Notes |
|---|---|---|---|---|
| W1 | Proof: interference dissection of the min-\(C_8\)-count exemplars (orders 14–16, re-extracted from the `E018`-style stream) and the three-degree-2 \(C_{16}\)-blocked boundary graphs (orders 16–17, on disk in `E019` spotcheck data) | `A023` (attempt), `E021` (experiment) | `fable` | The programme's primary proof-side lever; the predicate must match the recorded `E013` census semantics exactly — stronger tier warranted |
| W2 | Search: the \(\mathcal G\)-profile ladder at orders 18 and 19 via the `E019` generator, anchors re-passed first under both interpreters | `E022` (experiment) | `opus` | Production runs on a verified instrument; the anchor suite is the safeguard |

Orchestrator correction handed to W1: the recorded next action says the
min-\(C_8\) exemplars are "`E018` data", but `E018`'s JSON records only
the min statistic (1/2/1 at 14/15/16), not the exemplar graphs — W1
re-extracts them from the same `geng` stream into `E021`, asserting
consistency with `E018`'s recorded class sizes and minima.

Ledgers (`STATEMENT.md`, `problem.json`, `STATE.md`, `CLAIMS.md`,
`OBLIGATIONS.md`, `PROOF.md`, `DECISIONS.md`, `LOG.md`,
`PROJECT_STATE.md`, generated index/dashboard) are held by this session
for the whole run; workers write only their owned records above, run no
git commands, and change no status. Worker reports are working input,
not citable records; both are audited before integration. Machine
budget: W2 up to 8 concurrent generator workers; W1 at most 4 for its
one heavy extraction (order 16); contention noted in both records.

## Work performed

Both workers launched concurrently after the strategy audit; both
completed and were audited before integration.

- **W1 (proof leg, model `fable`; owned `A023`, `E021`).** Extracted the
  min-\(C_8\) exemplar families exhaustively from `E018`'s exact stream
  at orders 14–16 (stream totals, class sizes, and minima asserted
  equal to the records; 11/20/103 graphs with \(\le3\) \(C_8\)s) and
  dissected them plus the sixteen three-degree-2 \(C_{16}\)-blocked
  boundary graphs (16–17, `E019` spotcheck data) against the `E013`
  census predicate, anchored first on the five recorded blocks (23/23
  reproduced with exact combos multiplicities; a genuine negative
  control included after W1 corrected its own first, mathematically
  wrong control). Verdict: **all 553 blockers decompose; the
  non-interference pivot trigger did not fire**. Supplementary probes:
  the tautness dichotomy (`smallworld` 10–12 exact biconditional;
  `tautgeneral` orders 4–7, all taut pairs, zero failures in 723,926
  instances). `A023` records the calculus lemmas T2/T3/T4 (proved),
  candidate lemma T5 and forcing target (F) (labelled conjecture and
  program), the order-14 calibration exemplar (T7), and a `C038`
  corroboration (T8). Disclosed deviations: two supplementary probes
  beyond the brief; a momentary 5th process; three bytecode-cache files
  written into `E018/__pycache__` and removed, with a
  `dont_write_bytecode` guard added and anchors re-passed.
- **W2 (search leg, model `opus`; owned `E022`).** Re-passed the
  146-anchor suite under both interpreters **before production**
  (output byte-identical to `E019`'s), then ran the ladder: order 18
  (16 parts, `--verify-all`; class 108,447, profile 0; independent
  unsplit count 108,447 exact) and order 19 (class 74,589, **profile
  1** — the first nonempty rung; the member \(C_{16}\)-blocked and
  \(S\)-violating; dual-split 16-vs-24 partition check labelg
  set-equal; the unsplit count deliberately left to the orchestrator).
  Spotchecked all 2,233 near-boundary members with the brute-force
  enumerator; recorded the empty 0-/1-buckets, histograms, growth
  rates, and the order-20 projection. Wrote nothing into `E019`
  (asserted programmatically on every invocation).
- **Orchestrator (this session).** Entry record repair
  (`PROJECT_STATE.md`, user-requested); worker briefs with the
  ledger prohibition verbatim; the audits below; the exemplar's
  vertex-tautness (computed here — it is taut, making it a genuine T5
  kill object); ledger integration (`L048`, `C041`–`C043`, `G015`,
  `G013`(a), `PROOF.md`, `DECISIONS.md`, `STATE.md`); the follow-up
  launch (`E022/followup_s022.py`, background: anchors gate → exemplar
  T5 test → order-20 rung ∥ order-19 unsplit count) with
  `exemplar_t5.py` written by this session on a deliberately different
  algorithm (determined-partner) so its harvest doubles as an
  independent-algorithm check.

## Results

Proved (hand, audited line-by-line by the orchestrator):

- `L048` — the interference calculus (`A023` T2/T3/T4): interference
  cycles are confined to the essential subgraph (necessity of
  tautness-side hypotheses); the both-terminals stratum is trivially
  decomposable; interference is the \(t=1\), leak-pinned case of
  `A021` T1, and under interference-completeness
  \(\mathrm{Spec}(B)=T_1(H,a,b)\cup(S+2)\) — the tight 1-atom's
  power-freeness becomes through-path arithmetic. Consistency anchor:
  the recorded 2-closure of Petersen\(-e\).

Computational evidence (exhaustive scopes stated per row):

- `C041` — the frontier dissection: 553/553 blockers are two-through-
  path symmetric differences (family 1: 385 \(C_8\)s, strata
  0/6/25–5/71/221; family 2: 168 \(C_{16}\)s × all three pairs);
  extraction exhaustive at 14–16; decomposition arithmetic (only 5 of
  18,299 incidences disjoint-type — `L033`'s shape is a corner case);
  134/134 exemplars vertex-taut; the two cut-vertex exemplars at 15/16
  (`C038` corroborated); the order-14 full-triple calibration object.
- `C042` — the tautness dichotomy: exact biconditional at orders
  10–12; zero failures over all taut pairs of all connected graphs of
  orders 4–7 (723,926 instances).
- `C043` — the ladder: order 18 profile-empty; order 19's unique,
  first-ever profile member doubly blocked (46 \(C_{16}\)s;
  \(S\ni6,14\)), vertex-taut (orchestrator-verified); 0-/1-buckets
  empty at both orders; **every tight 1-atom and every \(\mathcal
  G\)-member has order \(\ge20\)** (direct route + `L041` route);
  `C040`'s flagged orders 18–19 corroborated from a different tree
  (same binary — caveat retained).

Conjecture/program (labelled, not claims): `A023` T5
(vertex-taut \(\Rightarrow\) interference-complete; ordered kill tests)
and T6/(F) (the order-windowed forcing target, doubly calibrated).

## Failed routes and why

No route died: the dissection was a pre-registered two-outcome probe
and the interference outcome occurred; the ladder rungs were decisive
in the expected direction. Two forward-looking risks recorded rather
than hidden: T5's smallest untested rungs (the order-19 exemplar —
running tonight — then in-class 13, sparse general 8–9) could still
kill it; and all frontier interference evidence sits at orders
\(\le17\)+the exemplar, while the residual object lives at \(\ge18\).
W1's first negative control was mathematically wrong (a C8-with-tail
that actually decomposes); W1 caught and replaced it itself — recorded
as a reminder that controls need proofs too.

## Adversarial check

- Both worker reports treated as working input only; every ledger row
  written by this session from the records after audit.
- W1 audit: the 45-anchor suite re-run by the orchestrator under both
  interpreters; extraction agreements re-verified directly against
  `E018`'s stored JSONs; three sample claims re-derived with
  **independently written code sharing nothing with E013/E018/E021**
  (the T7 exemplar in full; an order-17 boundary graph × all three
  pairs; the three order-16 single-\(C_8\) minima); `smallworld` and
  `tautgeneral` re-run with exact agreement; the T2/T3/T4 proofs
  re-derived by hand; the `A021` T1 citation checked verbatim; T4(3)
  checked against the recorded 2-closure anchor.
- W2 audit: anchor output byte-compared to `E019`'s (identical);
  harvest/count/splitcheck JSONs re-read directly; the order-19
  exemplar re-derived in full with independent code (order, degrees,
  distance, spectrum, 46 \(C_{16}\)s, \(S=\{5..18\}\), 2-connectivity,
  non-bipartiteness) plus vertex-tautness computed fresh; class-file
  membership grepped in both splits; the `proofctl add` side effect
  (regenerated `problem.json`/index) verified content-identical via
  `git diff`.
- Scope discipline enforced: bound-lifting arithmetic done only by the
  orchestrator; W2's records state the finite exclusions only.

## Canonical records changed

## Canonical records changed

- [ ] `STATEMENT.md` — unchanged (version 0.1 stands)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`L048`, `C041`–`C043`)
- [x] `OBLIGATIONS.md` (`G015`, `G013`(a))
- [x] `PROOF.md` (the atom floors; the S022 lever bullet; the `G015`
  gap rewritten around the T5 program)
- [x] `DECISIONS.md` (the interference program adopted as the primary
  case-(5b) route)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream
- [x] `PROJECT_STATE.md` (entry repair of the stale pre-harvest text,
  user-requested; end-of-session update of the P-002 bullet and next
  action)

(The commit boxes are checked as part of the closing commit that
contains this file.)

## Ending checkpoint

- Current frontier: every tight 1-atom and every \(\mathcal G\)-member
  has order \(\ge20\); every counterexample \(\ge21\) (window
  \([21,24]\)); the case-(5b) chain branch empty below 36; **the
  interference model survived its frontier kill test in full** (553/553
  blockers decompose; the property exactly tautness-shaped; the
  calculus `L048` proved); the first-ever profile object exists at
  order 19, doubly blocked, vertex-taut — the sharpest T5 test object.
- Remaining blockers: T5 is a conjecture (its order-19 kill test is
  stage A of the running follow-up); (F) has no proof step; Tier 0's
  forcing question untouched.
- Recalibration decision: **continued** — both inherited legs ran to
  verdicts and both delivered; no pivot trigger fired. Within the
  route, the proof side sharpened from "interference structure" to the
  named T5 → (F) program (recorded in `DECISIONS.md`).
- Best live alternative or reframing: the disjoint long-link descent
  (`A020` W2-T8(c)) on the proof side; cubic order 26/28/30 on the
  search side (Tier 0's counterexample ticket).
- Pivot trigger: see `STATE.md` (notably: a non-decomposable cycle in
  any vertex-taut pair — the exemplar, `smallworld 13`, or sparse
  8–9 — kills T5 and redirects; a \(\mathcal G\)-profile hit at 20+
  passing the \(S\)-condition = disproof; a proof of T5 makes (F) the
  whole proof side).
- Best next action: harvest the follow-up
  (`E022/data/followup_s022.json`: the exemplar T5 verdict, the
  order-20 rung, the order-19 unsplit count), then run the T5 kill
  rungs that remain (`smallworld 13`, sparse general 8–9) and, if T5
  survives everything, open the proof attempt (clean-window reroute +
  minimal-choice exchange). As recorded in `problem.json`.
- Files a new session should read: the `STATE.md` resume list (updated
  this session).

## Plain-language recap

This session ran two workers at once under the orchestration protocol,
audited both, and both delivered.

The proof-side worker answered the one question the surviving route
hinged on. The dangerous configuration — the last shape standing
between us and the theorem "the conjecture holds if and only if it
holds for 3-regular graphs" — is always stopped, in every near-miss we
know, by a "blocking" cycle of length 8 or 16. The question: is every
such blocker built by overlaying two terminal-to-terminal paths (an
"interference pattern" the object's own path arithmetic can see), or
can a blocker exist that the path system is blind to? The answer,
across all 553 blocking cycles of every closest known object:
interference, every single time — and the trait tracks exactly the
"every vertex carries terminal traffic" property the dangerous
configuration is forced to have (over 800,000 verified instances
behind that correspondence, zero exceptions, with the easy direction
now a proved lemma). Three small proved lemmas turn this into a
calculus: if the conjectured completeness holds, the dangerous
object's entire "no power-of-two cycle" property becomes arithmetic of
its own path system — precisely the kind of argument the two earlier
impossibility theorems left as the only survivor. The lemma to prove
is stated, its obstacles are named, and its kill tests are ordered.

The search-side worker swept sizes 18 and 19 with the generator built
last session (after re-passing all 146 instrument checks under both
interpreters). Size 18: empty. Size 19 produced a first — the only
graph ever found with the dangerous configuration's exact degree
pattern — and it is dead twice over, independently: a 16-cycle sits
inside it, and its path lengths hit two forbidden values. Every
single-defect seed now needs at least 20 vertices, and the strange
new graph is itself the best test object yet for the candidate lemma:
it was launched against it tonight as stage one of the overnight run
(stages two and three: the size-20 sweep and a final consistency count
for size 19).

## Proposed next step

First, read out the overnight run: the candidate lemma's verdict on
the new size-19 graph (a single failing cycle kills the lemma at the
most relevant object; survival is the strongest cheap evidence yet),
the size-20 sweep (a hit with the right arithmetic disproves the
conjecture outright; empty pushes the dangerous object to 21+), and
the size-19 consistency count. Then finish the lemma's cheap kill
tests (the exhaustive size-13 in-class scan, minutes; a sparse
general-graph probe at sizes 8–9). If the lemma survives everything,
open the proof attempt — the "clean window reroute" argument, whose
two sub-steps are already named. Considered and deferred: the
block-level kill search at size 15–16 (background rung), the cubic
26/28 reproductions, and the multi-day cubic size-30 run (the
deliberate decision it deserves comes after the cheap rungs are
spent).

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 7%
- Previous estimate, if any: 6% (S021)
- Reason for change: the last surviving proof-side route survived the
  one test that could have killed it immediately — and came back with
  a stated mechanism (a candidate lemma plus a forcing target) rather
  than a hope; the floors moved again; the first profile object
  exists as a concrete test bed.
- Basis: the promising route is the T5 → (F) interference program —
  either T5 dies cheaply this week (redirect with a named missing
  hypothesis) or the case-(5b) endgame becomes a two-step theorem
  target with the search ladder decisive underneath. The strongest
  obstacle is unchanged: nothing yet forces a specific power length at
  minimum degree 3, and (F) is order-windowed evidence, not an
  argument. One point of increment, as in S021: real structural
  progress on the deliverable, but the deliverable is the reduction,
  not the conjecture.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.

## Follow-up harvest addendum (same conversation, 2026-07-25)

The close-of-session background run completed and was harvested in the
same conversation (fresh reconciliation commit; the S019/S021
precedent):

- **Stage 0/A:** anchors re-passed (146, PyPy); the order-19
  exemplar's full cycle set against T5 — **411/411 decompose, zero
  failures** across every length. T5 survived the sharpest available
  kill test, on the determined-partner algorithm (deliberately
  different from `E021`'s pairwise search).
- **Stage C:** the order-19 independent unsplit count = **74,589
  exactly**; `C043`'s named partition follow-up is closed.
- **Stage B:** order 20 spent — class 2,569,481, **profile 7**, all
  \(C_{16}\)-blocked, zero power-free, 0-/1-buckets empty, 4,436
  near-boundary graphs spot-checked. Floors: **\(\mathcal G\)-members
  \(\ge21\); tight 1-atoms \(\ge22\)** (`L041` cases (4)/(5)
  propagating `L047` and the \(\mathcal G\) floor — the case-(4)
  constant in the `L041` row text predates `L047`; the direct
  1-bucket route certifies \(\ge21\)).
- **Orchestrator additions at harvest:** the three on-disk order-20
  profile members extracted, verified, and T5-tested
  (`t5_n20_profile.py`; **1,890/1,890 decompose**; 254 \(C_{16}\)
  verdicts re-verified by the independent pairwise algorithm; all
  three vertex-taut, 2-connected, \(S\ni6,14\)). Two of my own
  tooling errors were caught and fixed during this audit: a
  first-draft degree filter that over-restricted the third-smallest
  degree, and a class-file-format assumption (lines carry metadata
  columns after the graph6 field); extraction re-run clean both
  times. **SAVE_LIMIT finding:** `scan.py` caps saved class rows at
  200k/part, so the order-20 class files are samples (572,530 of
  2,569,481) — unlike 18/19, which this addendum re-confirms as
  complete; part 14's four profile members fell outside its window
  and their dedicated recollection (`collect_n20_part14.py`, with a
  stream-total assertion against the 439,745 tally) is running.
- **Chained mid-wait (recorded in-conversation, per the standing
  Tier 3 rule and the user's utilization request):** stage D
  (`followup_s022b.py`) — the min-degree-3 order-21 sweep, launched
  as a waiter that started when stages B/C finished, after re-passing
  the anchor gate. Empty would lift `L047` to 22. Running.

Ledger deltas in the harvest commit: `C042`/`C043` extended (T5 rungs
1–2 survived; order 20; floors 21/22), `OBLIGATIONS.md`
(`G015`/`G013`(a)), `PROOF.md` floors, `STATE.md`,
`PROJECT_STATE.md`, `problem.json` next action (harvest-first now
points at the two still-running legs; then the remaining T5 kill
rungs; then the proof attempt). Resolution outlook unchanged at 7% —
the harvest landed inside the S022 call (T5 survived what it was
given; every emptiness moved the floors as projected).

## Second follow-up harvest addendum (2026-07-25, closing the run)

Both residual legs landed and were audited:

- **Part-14 recollection** (`collect_n20_part14.py`; two runs with
  identical aggregates — the first run's per-graph reports were
  computed but not persisted, a script bug disclosed in `LOG.md`;
  fixed, re-run with a raw g6 dump written during the stream pass):
  stream total **439,745 = the stage-B tally exactly**; the four
  remaining order-20 profile members recovered and identified
  (`profile_n20_part14.g6`) — all vertex-taut, 2-connected, 65–80
  \(C_{16}\)s, \(S\ni6,14\) — and **T5 survives on all four**
  (2,360/2,360 cycles). The orchestrator independently re-audited the
  first member (spectrum, 69 \(C_{16}\)s, \(S\)-set, cycle count)
  with the from-scratch primitives. Cumulative, now on `C042`(e):
  **all eight profile objects in existence survive T5 — 4,661/4,661
  cycles — and every one carries the \(S\ni\{6,14\}\) double
  blocking**, the (F)-shaped pattern.
- **Stage D** (`followup_s022b.py`): the min-degree-3
  \(\{C_4,C_8\}\)-free sweep at order 21 is **empty** — 16/16 parts,
  zero output (16 empty files verified on disk), all return codes 0,
  the 146-anchor gate re-passed under PyPy immediately before
  generation, 20,288 s wall on 8 workers. `C040` extends to 14–21
  and **`L047` lifts to \(\ge22\)**: every counterexample has at
  least twenty-two vertices; the extremal window is \([22,24]\),
  three orders wide. Atom floors unchanged (22/21; `L041` case (5)
  still binds).

Ledger deltas in this commit: `C040` (order 21; the 18–21 caveat),
`L047` (22; window \([22,24]\); constant history), `C042`(e) (the
four members; the cumulative eight-object statement), `C043` (the
recollection landed), `OBLIGATIONS.md` `G015`, `PROOF.md` (`L022`
supersession note and floors), `STATE.md`, `PROJECT_STATE.md`,
`problem.json` (next action: the two remaining cheap T5 kill rungs —
`smallworld 13`, sparse general 8–9 — then the T5 proof attempt).
Nothing is left running; the dossier is reconciled. Resolution
outlook unchanged at 7% (both results landed inside the S022 call).
