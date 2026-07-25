# S021 — Orchestrated parallel legs: quantify the chain-cancellation tension (proof side) and build the G014 item-6 C4-C8-free generator (search side)

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L039`–`L042` (the (3,3) bijection onto
  \(\mathcal G\), engine + peel, five-case analysis — the conditional
  cubic reduction holds modulo excluding case (5b)); `C036` (order-16
  \(\mathcal G\)-profile scan empty; every tight 1-atom has order
  \(\ge18\)); `C037`/`A021` (the congruence route is dead at every
  modulus; Petersen\(-e\) is the standing calibration object; chain
  calculus caps congruence information at parity).
- Open obligations in scope: `G015` (exclude case (5b)); `G013`(a);
  `G014` item 6 (the dedicated \(\{C_4,C_8\}\)-free generator).
- Inherited next action: proof side — quantify the chain-cancellation
  tension (`L042`/A019 W1-T14), first falsifiable target: bound the
  block-chain length of \(H\) or prove \(H\) 2-connected; search side —
  build the `G014` item-6 generator before any order-17 scan.
- Session goal: run both legs concurrently under `O011` orchestrated
  mode (one worker subagent per leg, this session holding all ledgers).
- Falsifiable next move: per leg, below.

## Strategy audit

Both inherited legs serve Tier 1 (`G015`, case (5b)); the generator also
serves Tiers 0/2/4 (cubic 30, bipartite 24+, infrastructure).

- Why the inherited route might work: (proof) W1-T14's forced
  memberships come from minimality, so they are allowed to exceed the
  Petersen\(-e\) calibration bar; the recorded `L032` sharpness core
  (two Petersen\(-e\) blocks over a bridge) *fails* the W1-T14 forced
  membership (\(S_1=\{4,5,7,8\}\) avoids \(\mathbb P-2\)), so the chain
  constraints have real bite on real objects. Audit-phase observation
  handed to the worker as an unverified lead: each 2-connected block of
  the chain appears to lie in `C027`'s scanned class and is power-free,
  which would force order \(\ge16\) per block — "either \(H\) is
  2-connected or \(n_0\ge\) ~32" looks reachable. (search) The \(C_8\)
  filter is 100% decisive in this profile at every order ever scanned
  and min \(C_8\) count at 16 is 1, so incremental \(C_8\) rejection
  prunes nearly the whole tree; Markström 2004 is the design precedent
  on weaker hardware.
- Fastest way to falsify it: (proof) exhibit a small vertex-taut
  \(C_4\)-free core **with a cut vertex** realizing every forced chain
  constraint with power-freeness dropped — that would kill
  arithmetic-only chain exclusion (order-bound results would survive);
  (search) anchor mismatch — the generator's counts must equal
  independent geng-plus-filter counts at small orders, and must
  reproduce the profile-class emptiness at 14/15/16 (`C027`/`C036`).
- Mechanistically distinct alternative or reframing: the disjoint
  long-link descent (`A020` W2-T8(c)) — deferred, third in the recorded
  order, needs a fresh A020 re-audit and is not riper than the chain
  tension; raw geng at order 17 (~6e9 stream, est. ~14 CPU-h at E018
  throughput) — deferred as single-use: the generator unlocks three
  targets and all later orders, and raw geng stays the recorded
  fallback; bipartite order 24 — Tier 3 background only, launched at
  close if the machine is clear (S019 precedent), never this session's
  work.
- Selected route and reason: both inherited legs, in parallel — they are
  mechanistically distinct (structural proof vs. instrument build),
  dependency-free (neither consumes the other's output), and touch no
  common claim row; admission rules of `process/concurrency.md` pass.
- Pivot criterion: (proof) the calibration kill above fires → the leg
  pivots to order-bound-only results and records the calibration
  object; (search) anchors fail and cannot be repaired in-session → the
  build is recorded as failed and raw geng order 17 becomes the next
  action. A \(\mathcal G\)-member found at 17 satisfying the
  \(S\)-condition → immediate disproof protocol, everything else stops.

## Worker allocation (declared before launch, per `O011`)

| Worker | Leg | Owned records | Model | Notes |
|---|---|---|---|---|
| W1 | Proof: quantify chain cancellation on the case-(5b) residual object | `A022` (attempt), `E020` (optional calibration compute) | `fable` | The programme's primary proof-side lever; hardest structural reasoning — stronger tier warranted |
| W2 | Search: design, build, verify the \(\{C_4,C_8\}\)-free generator | `E019` (experiment) | `opus` | Engineering + verification discipline; anchor suite is the safeguard |

Ledgers (`STATEMENT.md`, `problem.json`, `STATE.md`, `CLAIMS.md`,
`OBLIGATIONS.md`, `PROOF.md`, `DECISIONS.md`, `LOG.md`,
`PROJECT_STATE.md`, generated index/dashboard) are held by this session
for the whole run; workers write only their owned records above, run no
git commands, and change no status. Worker reports are working input,
not citable records; both are audited before integration.

## Work performed

Both workers launched concurrently after the strategy audit; both
completed and were audited before integration.

- **W1 (proof leg, model `fable`; owned `A022`, `E020`).** Quantified the
  chain-cancellation tension of `A019` W1-T14 on the case-(5b) residual
  object. Deductions W1-T1–W1-T12 in `A022`: the chain frame (including
  \(ab\notin E\) in the chain case and the gateway lemma), the closure
  battery on prefixes (2-/1-/0-closures — every prefix hides the second
  terminal, so every closure lands tight-1-atom-shaped, the [min]
  engine), the assembled per-cut constraint system with localized
  escapes and bridge-row redundancy, the collision table ((ℙ−1,ℙ−1) and
  (ℙ,ℙ−2) at equal exponents are the **only** interactions — the
  cancellation quantified), end blocks non-bipartite, per-block order
  bounds via `C027`/`C036`, and the order dichotomy: **either \(H\) is
  2-connected or \(n_0\ge32\)** (with \(m\le(n_0-9)/8\)). New unforced
  structure: **terminal power saturation** (W1-T4, the \(\mathbb P\)-
  sibling of Mersenne saturation via 0-closure, which `A019` missed).
  `E020`: block/through-set catalogue (orders \(\le13\) all pairs,
  order-14 two-degree-2; 226,619 taut pair instances; 12 anchors), and
  the pre-registered kill search — **zero** candidates at every level
  over all \(m\le3\) chain shapes; single binding mechanism (the forced
  14 in every admissible pairwise Minkowski sum); first abstract
  solutions at block orders 15–16.
- **W2 (search leg, model `opus`; owned `E019`).** Built `G014` item 6 as
  a nauty `PREPRUNE` plugin (`genc48` = geng.c + `prune_c8.c`; nauty
  2.9.3 from the sha256-verified upstream tarball; completeness argument
  written against the vendored source). 146 anchors under CPython and
  PyPy, including 23 `labelg` **set-equality** comparisons against the
  independent `geng | C8-filter` pipeline across five variants, res/mod
  partition checks, and the cubic order-24 **positive control**
  (4 graphs, set-equal to `E005`/Markström Table 3). **Order-17
  \(\mathcal G\)-profile production run: EMPTY** (class 2,580 = unsplit
  count; profile 0). Reproductions of `C027`/`C036` at 14–16 (~75× less
  CPU than `E018`); `C027`'s own class extended to 16 and 17 (empty);
  min-deg-2 \(\le2\)-degree-2 class empty at 16/17 outright; proximity
  statistic: min #degree-2 = 3 at 16/17 and \(C_{16}\) kills every such
  boundary graph — the first decisive \(C_{16}\) in the dossier. Flagged
  (not claimed): min-degree-3 \(\{C_4,C_8\}\)-free empty at 14–19.
- **Orchestrator (this session).** Audits below; source-audit record for
  the user-supplied MathOverflow-512914 quote
  (`references/mathoverflow-512914-audit-2026-07-24.md`: cubic-20
  figures corroborated/recounted; the quoted cubic→min-degree-3
  inference **rejected as unsupported** — its general form is the open
  `G015`); orchestrator audit addendum `E019/audit_mindeg3_n18_parts.py`
  (stream-side slice cross-check at order 18, the first uncrosschecked
  order of the flagged sweep); close-of-session background follow-up
  `E019/followup_s021.py` (MO recount; min-degree-3 order 20; bipartite
  order 24 by the new instrument).

## Results

Proved (hand, audited line-by-line by the orchestrator; conditionality
as labeled):

- The chain-case constraint system and closure battery (`A022`
  W1-T1/T2/T3/T5, ledgered `L043`); terminal power saturation (W1-T4,
  `L044`, filter-not-lever); the collision table and its corollary that
  membership arithmetic alone cannot exclude the chain case (W1-T6,
  `L045`); end blocks non-bipartite (W1-T7, in `L043`); the order
  dichotomy and chain-length bound (W1-T8, `L046`).

Computational evidence (exhaustive, anchored, reproduced):

- `E020` kill search: refuted in its range; the chain floor 15; the
  cut⟺non-taut coincidence at \(\le14\) that retro-explains `C037`'s
  2-connectivity datum (`C038`).
- `E019` order-17 emptiness and the instrument itself (`C039`): every
  tight 1-atom has order \(\ge19\), every \(\mathcal G\)-member
  \(\ge18\); `C027`'s class empty through 17.
- `E019` min-degree-3 sweep 14–19 (`C040`) and the counterexample bound
  \(\ge20\) (`L047`) — integrated only after the orchestrator's slice
  audit at order 18 (below) came back clean; the 18/19 caveat (no full
  stream-side cross-check) is recorded on the row.

Imported facts needing verification:

- MathOverflow 512914 (user-supplied quote): cubic-20 rows corroborated
  (MO-1/MO-3) or recounted (MO-2, stage A); **MO-4 (the min-degree-3
  conclusion at 20) unusable as quoted** — rests on an unread claimed
  reduction whose general form is exactly open `G015`; superseded by the
  internal stage-B follow-up run regardless.

## Failed routes and why

- The pre-registered chain-case kill condition did **not** fire: no
  calibration object exists over the catalogued block range (`E020`).
  The question stays open at block orders 15–16, where the arithmetic
  first admits solutions; named as the kill rung follow-up.
- An absolute (order-free) bound on the chain length is impossible from
  the membership system alone (`L045`'s freeness); the honest bound is
  the linear one in `L046`.
- The MO-512914 route to a free order-20 bound failed audit (MO-4
  above); replaced by the internal stage-B run.

## Adversarial check

- Every W1 hand proof re-derived independently by the orchestrator
  before integration: the collision-table 2-adic case check, the
  dichotomy accounting (\(14k+m+1\); \(k\ge\lceil(m+1)/2\rceil\); the
  32/33/48 thresholds), the closure-battery degree bookkeeping and
  escape localization, and the abstract 15/16 solution
  (\(\{7,8,12,13,14\}+\{8,11,12,13,14,15\}\) dodges all three exponent
  patterns). Citations spot-verified against sources: `A014` T3.3 core
  clauses, `E010`'s stream spec (`-d1`, mine \(=\lceil(3n-4)/2\rceil\)
  implied), `L035` T2's degree-freeness.
- `E020` reproduced by the orchestrator: 12-anchor suite and the full
  kill search re-run (226,619 pairs; 166/176 distinct sets; 0/0/0), and
  the forbidden-set constants checked against the maximum reachable sum
  (39 < 62 — no truncation artifact). `chain_eval`'s bridge handling
  verified to carry the +1 shift through the Minkowski accumulation.
- `E019` audited: the `PREPRUNE` call sites verified in the vendored
  `geng.c` (accept1/accept1b/accept2; the "PRUNE feature" induced-
  subgraph guarantee); `prune_c8.c` read line-by-line (the C8-through-
  newest-vertex decomposition, admissible BFS pruning, correct
  bit-relabelling, sound induction base at \(n<8\)); the 146-anchor
  suite re-run by the orchestrator (passes, CPython); the order-18
  stream-side **slice audit** written and run by the orchestrator
  (`audit_mindeg3_n18_parts.py`, stock geng + the original `E015`
  detector imported from its own file, parts 3/11/19 of 24).
- Worker reports were treated as working input only; all ledger rows
  were written by this session from the records, not the reports.

## Canonical records changed

- [ ] `STATEMENT.md` — unchanged (version 0.1 stands)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`L043`–`L047`, `C038`–`C040`, dependency notes)
- [x] `OBLIGATIONS.md` (`G015`, `G013`(a), `G014` items 6/7)
- [x] `PROOF.md` (bounds; the chain package; the stale `G015` gap
  bullet repaired; `L022`→`L047` supersession)
- [x] `DECISIONS.md` (instrument adoption; chain-branch arithmetic
  retirement; MO-512914 rejection)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

(The last two boxes are checked as part of the closing commit that
contains this file.)

## Ending checkpoint

- Current frontier: tight 1-atoms \(\ge19\); \(\mathcal G\)-members
  \(\ge18\); `C027`'s class empty through 17; every counterexample
  \(\ge20\) (window \([20,24]\)); the case-(5b) chain branch empty
  below \(n_0=36\), so the residual object is 2-connected there; the
  bipartite class clean through 23 with order 24 running.
- Remaining blockers: no mechanism yet makes the power spectrum fight
  on the 2-connected branch (interference is a question, not a
  theorem); the kill question at block orders 15–16 is open; Tier 0
  itself unchanged.
- Recalibration decision: **continued** — both inherited legs were
  run to verdicts and both delivered; no pivot was triggered (the
  chain-case kill condition did not fire; no search hit).
- Best live alternative or reframing: the disjoint long-link descent
  (`A020` W2-T8(c)) on the proof side; the cubic order-26/28/30 ladder
  on the search side (Tier 0's best counterexample ticket, now priced
  at days, not months).
- Pivot trigger: see `STATE.md` (notably: a \(\mathcal G\)-profile hit
  at 18+ = disproof; a realized \(\{7,8,12,13,14\}\)-shaped block
  through-set at 15–16 = the chain-case Petersen\(-e\) exists; a
  non-interference blocker = the pinched-world model breaks).
- Best next action: harvest the follow-up, then the interference
  dissection (proof) + the 18/19 ladder rungs (search) — as recorded
  in `problem.json`.
- Files a new session should read: the `STATE.md` resume list (updated
  this session).

## Plain-language recap

This session ran two workers at once under the orchestration protocol
and both finished their assignments.

The first worker took the one proof idea that survived last session —
the "cancellation across the links of a chain" tension — and settled
exactly what it is worth. If the dangerous configuration (the last
shape standing between us and the theorem "the conjecture holds if and
only if it holds for 3-regular graphs") were chain-shaped, each link
would be forced to contain certain forbidden path lengths while the
whole chain avoids them. The worker proved this forcing is real but
arithmetically weak — the forbidden lengths can always dodge each
other, provably, so no clever arithmetic will ever kill the chain shape
— and then killed the chain shape a different way: each solid link
would itself have to be one of the rare graphs our searches keep
proving nonexistent, so a chain-shaped dangerous configuration needs
at least 36 vertices. Below 36, only one shape remains: a single
two-connected piece. The search for a "chain-shaped near-miss" (an
object that would have calibrated how hard the remaining case is) came
back empty through all small building blocks, with one identified
bottleneck, and the first place such an object could exist is now
precisely named.

The second worker built the search machine the last three sessions
have been asking for: a modified graph generator that never builds an
8-cycle in the first place, instead of generating everything and
filtering. It was verified twenty-three ways against the old pipeline,
plus against an independently published census (it reproduces
Markström's four famous 24-vertex graphs exactly). It is about a
hundred times cheaper than the old approach. On day one it: emptied
size 17 for the dangerous configuration's profile (the object now
needs at least 19 vertices); extended the master emptiness record two
sizes past its old wall; and swept the entire "minimum degree three"
world — where any counterexample must live — through 19 vertices,
finding nothing. That last sweep, after this session's independent
spot-audits against the old instrument, raises the global record:
**any counterexample to the Erdős–Gyárfás conjecture needs at least 20
vertices**, one better than before.

Mid-session the user brought in a MathOverflow thread claiming size 20
was already handled. Auditing it: the thread's cubic computation is
correct — and agrees with our machine's independent run — but its jump
from "no cubic example" to "no example at all" quietly assumes the
very theorem this programme is trying to prove, so we rejected that
step and launched our own size-20 sweep instead (running now in the
background, along with the bipartite size-24 leg on the new machine).

What remains: one two-connected configuration carrying the whole
reduction theorem, a cheap decisive search ladder (sizes 18 and 19
cost minutes now), and the conjecture itself behind them.

## Proposed next step

First, read out the background runs launched at close (the size-20
minimum-degree-3 sweep, the bipartite size-24 leg, and the MathOverflow
recount) — none of it may be cited until read. Then, on the proof
side: dissect the near-miss graphs already on disk — the ones blocked
by a *single* 8-cycle at sizes 14–16, and the boundary graphs at 16–17
that only a 16-cycle kills — and determine whether every blocking
cycle is an "interference pattern" (built from two overlapping
terminal-to-terminal paths, as in every case ever examined in the
neighbouring channel), or whether a blocking cycle of a genuinely
different kind exists. Either answer directs the remaining proof work
on the one surviving configuration. On the search side: run sizes 18
and 19 of the dangerous-configuration profile on the new machine
(minutes each; a hit disproves the conjecture outright, an empty run
pushes the object to 20+). Considered and deferred: the block-level
kill search at size 15 (background rung), the cubic sizes 26/28
reproductions, and the multi-day cubic size-30 run — the first two are
cheap background legs, the last needs a deliberate decision once the
cheaper rungs are spent.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 6%
- Previous estimate, if any: 5% (S020)
- Reason for change: the reachable deliverable (the cubic reduction)
  lost one of its two remaining fronts below order 36 and gained a
  verified instrument that prices every named search rung in
  minutes-to-days; the counterexample floor moved for the first time
  since S009; nothing moved against.
- Basis: the promising route is the case-(5b) endgame — one
  2-connected configuration, attacked by the interference dissection
  (data already on disk) while the decisive ladder runs underneath;
  the strongest obstacle is unchanged — nothing yet forces a specific
  power-of-two length at minimum degree 3, and every emptiness result
  cuts the disproof side's remaining room without making the proof
  side easier. The increment is one point, not more, because the
  deliverable is a reduction, not the conjecture.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
