# S024 — The (F) opening probe: power-collision realization tables of the ten named objects

- Date: 2026-07-25
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1 (unchanged).
- Work / claim status: `active` / `open`.
- Strongest established facts: T5 is a theorem (`L049`, audited `R002`
  PASS) with the trunk-identical arc form and prescribed-edge freedom;
  the case-(5b) residual object's spectrum identity is unconditional
  (`L048`(iii): \(\mathrm{Spec}(B)=T_1\cup(S+2)\), every element a
  trunk-split pair value); **(F) ⟺ case (5b) empty below 36** (window
  \([18,35]\)); floors: counterexamples \(\ge22\), tight 1-atoms
  \(\ge22\), \(\mathcal G\)-members \(\ge21\).
- Open obligations in scope: `G015` (exclude case (5b) — the (F)
  program is its entire proof side below 36), `G013`(a).
- Inherited next action: the (F) opening probe — power-collision
  realization tables of the ten named objects, read against the forced
  memberships, under the binding two-object calibration discipline.
- Session goal: build the tables (new experiment, E021 primitives
  imported, anchors re-passed first), read them, and either name a
  candidate (F) mechanism or redirect (F) toward window/order
  arithmetic.
- Falsifiable next move: the tables themselves — pre-registered
  patterns tested mechanically per cycle across all ten objects; the
  mechanism branch dies in-session if no pattern survives both
  calibration objects.
- Background: `E024` (order-21 \(\mathcal G\) rung) is **running**
  (user confirms it will not finish during this session); it is
  excluded from every ledger row and not harvested here.

## Strategy audit

- Tier served: **Tier 1** (`G015`, case (5b), proof side).
- Why the inherited route might work: `L049` just converted the
  object's power-freeness into trunk-split pair arithmetic, so the
  realization tables are the first direct look at the collision
  calculus (F) must force; the ten objects realize the collisions the
  residual object must avoid, and the probe is doubly calibrated
  (Petersen\(-e\), the order-14 exemplar — both realize the forced
  memberships without being power-free, so any pattern surviving them
  consumes power-freeness structurally, exactly the `A021` consumption
  discipline).
- Fastest way to falsify it: the probe carries its own kill — if the
  trunk-split tables show unstructured \((x,y,s)\) scatter with no
  membership tie that survives the calibration pair, the mechanism
  branch is dead and (F) redirects the same day (pre-registered
  outcome (b)).
- Mechanistically distinct alternatives weighed: (i) direct
  construction attack on (F) — build a power-free vertex-taut
  (5b)-profile pair at orders 22–35 by hand; rejected now: three prior
  hand constructions died to the cascade obstruction (`A015`), girth
  arithmetic blocks the cheap high-girth route below order ~58, and
  the ladder (`E024`) is already sweeping the window bottom by
  machine. (ii) The `C038` kill rung at block orders 15–16 — Tier 3
  harvest-only by standing rule, not selectable as primary. (iii)
  Bipartite EGC proof side (Tier 2) — deferred, tier discipline. The
  probe is itself the first falsifiable move of the internal
  tool-building attempt ("name the forcing mechanism from realization
  data, then prove it"), so the no-ceiling rule is satisfied rather
  than deferred.
- Selected route and reason: the inherited probe — cheapest decisive
  move on the only surviving proof-side program, both outcomes
  actionable, minutes of compute on named finite objects.
- Pivot criterion: no membership-patterned regularity surviving both
  calibration objects → take branch (b), redirect (F) to window/order
  arithmetic (recorded in-session, not deferred). A power cycle with
  no trunk-split realization anywhere → **soundness alarm** on
  `L049`/`E023` (critical audit event, not a route pivot).

## Work performed

- Built `E025` (`tables.py`): the complete trunk-split power-collision
  realization tables of the ten named objects. Import chain
  `E021/dissect.py` → `E018 scan/mod4` + `E013 catalogue` (no
  primitive re-implemented); all writes redirected to `E025/data`.
  New code: the trunk-split classifier (a witnessing pair is
  trunk-split iff \(E(P)\setminus E(Q)\) is a single arc; the
  equivalence's claims asserted per pair, not assumed) and the
  pattern evaluator (nine patterns fixed in the docstring **before**
  the first table was built — the pre-registration).
- Anchors first (standing rule): `E021`'s 45-check suite through the
  import + 14 new checks — the \(C_{16}\) cycle graph, the pendant
  tail, the **weave control** (a non-trunk-split witnessing pair the
  classifier must reject), exact reproduction of the recorded `E013`
  Petersen\(-e\) census, the recorded `E021` family-1 per-blocker
  combos for the order-14 exemplar, and cross-engine agreement with
  `E021.dissect_pair`. All pass under PyPy 7.3.23 **and** CPython
  3.14.2.
- Production run (4.3 s PyPy): 604 power cycles, 61,901 witnessing
  pairs, 1,971 trunk-split realizations; every recorded reference
  field of the ten objects re-verified; CPython full-payload
  cross-check identical. Pattern verdicts + exploratory weakest-
  disjunction check + shape distributions extracted.
- Deductions recorded in `A025` (T1 verdict, T2 trunk bound proved,
  T3 saturation, T4 the (F-S)/(F-T) redirect, T5 the S-gap census
  design). `E024` (order-21 rung) ran throughout, untouched,
  excluded from every ledger row (user confirmed at session start it
  would not finish today).

## Results

- **Proved:** `L051`, the trunk bound — every trunk-split realization
  has \(s=t_a+t_b\le n-L\), hence \(x+y\le2n-L\),
  \(\max(x,y)\le s+L-1\) (one paragraph from `L049`'s arc form).
  Computed tight on all ten objects (max \(s=n-L\) exactly).
- **Refuted as a route (pre-registered branch (b)):** the
  membership-collision form of (F). None of the nine patterns is
  universal; 30 cycles across six profile objects are
  membership-blind outright (three shapes: \(\{(5,13,1)\}\),
  \(\{(9,11,2),(10,10,2)\}\), \(\{(5,11,0)\}\)); the calibration
  pair's 100% `has_PP` collapses to 1–8/37–112 at the frontier
  (small-order artifact).
- **Computational evidence (`C045`):** the tables themselves;
  frontier saturation — all eight profile objects have spectrum
  exactly \([3,n]\setminus\{4,8\}\) and \(S\supseteq[6,n-1]\ni6,14\);
  the only known \(\mathbb P-2\) dodges are the calibration pair
  (orders 10/14, both gapping \(S\) exactly at 6); the trunk-split
  skeleton is thin (2.6–4.0 per cycle vs 76–138 witnessing pairs);
  pooled \(C_{16}\) \(s\)-distribution \(\{0{:}111,1{:}403,2{:}763,
  3{:}482,4{:}182\}\); all eight arc splits occur (mode (4,12)); the
  111 "both"-stratum \(C_{16}\)s all have \((u,v)=(a,b)\) forced.
- **Provisional (conjecture strength, labelled):** the (F-S)/(F-T)
  split (`A025` T4) and the saturation/interpolation mechanism
  candidate. Neither is a claim; both are program structure.
- No soundness alarm: every power cycle has a trunk-split realization
  (`L049` corroborated on 604 more cycles).

## Failed routes and why

The membership-collision form of (F) died on its pre-registered kill
(the tables show the forced \(\mathbb P/\mathbb P{-}1/\mathbb P{-}2\)
memberships do not organize the collisions — `A025` T1 preserves the
30 membership-blind witnesses). This is the third
arithmetic-cannot-do-it result (after `C037` and `L045`), and the
reason is now empirical as well as theoretical: at the frontier the
collisions are realized through arithmetically generic length pairs.
Salvage: the tables themselves, the trunk bound, and the saturation
reading that produced the redirect.

## Adversarial check

- The classifier was given a designed negative control (the weave
  pair) and had to reject it; the trunk-split ⟺ single-arc
  equivalence is asserted claim-by-claim per pair (any failure of the
  proof's structure would crash the run).
- The all-pairs layer was asserted equal to two independently
  produced records (`E013` census, `E021` family-1 combos) and to
  `E021.dissect_pair` cross-engine; every recorded reference field of
  the `E022` JSONs was re-verified.
- Full-payload cross-interpreter check (PyPy vs CPython) identical.
- Two pre-registered soundness alarms armed against `L049` (a power
  cycle with no witnessing pair / no trunk-split realization);
  neither fired.
- The failure-count sums quoted in `A025` T1 were recomputed by hand
  from the verdict table (two initial slips caught and fixed: 556 and
  400, not 559/380). The (F)=(F-S)∨(F-T) reduction logic and the
  trunk-bound proof were re-derived before promotion; both
  sub-targets were checked against the `A021` discipline (both fail
  off-window on the calibration pair, as required).

## Canonical records changed

- [ ] `STATEMENT.md` (unchanged — no statement change)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`L051`, `C045` new)
- [x] `OBLIGATIONS.md` (`G015` S024 update)
- [ ] `PROOF.md` (unchanged — integrated argument did not change)
- [x] `DECISIONS.md` (S024 row: the membership-collision form of (F)
  closed as a route; the program re-aimed as (F-S) ∨ (F-T) — a
  disposition change of a major approach; statement unchanged)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: counterexamples \(\ge22\) (window \([22,24]\));
  tight 1-atoms \(\ge22\), \(\mathcal G\)-members \(\ge21\); case
  (5b) below 36 ⟺ (F), now split as (F-S) ∨ (F-T) with the
  membership-collision form dead; `L051` proved; `E024` (order 21)
  still running.
- Remaining blockers: the forcing content of (F-S)/(F-T) (no proof
  step exists); the missing saturation/interpolation tool; no data
  above order 20 (window top 35 untouched).
- Recalibration decision: **continued** on the inherited route — the
  probe was the recorded next action, it produced its pre-registered
  branch-(b) outcome, and the redirect stays inside the (F) program.
- Best live alternative or reframing: (F-T) if (F-S) dies in the
  census; the `C038` kill rung and disjoint long-link descent behind
  it; Tier 2 bipartite EGC as the standing restricted-class theorem.
- Pivot trigger: a vertex-taut member of the 18+ class with
  \(S\cap\{6,14\}=\emptyset\) (kills (F-S), becomes calibration
  object #3); a power-free vertex-taut (5b)-profile pair in-window
  (defeats both forms, disproof-adjacent); `E024` outcomes (an
  \(S\)-satisfying profile hit is a disproof).
- Best next action: the S-gap census at the window bottom (`A025`
  T5), harvesting `E024` first if it has landed.
- Files a new session should read: `STATE.md` resume list (`A025`
  first, then `A024`/`A023`, `E025/README.md`).

## Plain-language recap

The programme's surviving proof route says: the dangerous
configuration's own path system must always collide into a
power-of-two cycle when the graph is small enough. This session took
that question's recorded first step — build, for the ten graphs
closest to the dangerous configuration, the complete table of every
way each power-of-two cycle arises as two overlaid terminal-to-
terminal paths in the reviewed theorem's normal form, and ask whether
the special path lengths the configuration is forced to carry (powers
of two and their neighbours) drive those collisions. The answer is a
clean no: the collisions run through ordinary lengths, thirty of the
cycles involve no special length at all, and the two small graphs
where power lengths did drive everything are size artifacts. That
kills one candidate proof mechanism cheaply — minutes of compute
instead of weeks of proof attempts against an illusion. The same
tables showed what does govern the collisions: room and saturation.
Room: a small newly proved lemma says the shared part of any overlay
must fit entirely outside the cycle, so at these sizes collisions are
squeezed into almost no space — the data meets the bound exactly on
every graph. Saturation: each frontier graph has cycles of every
length except exactly 4 and 8, and paths of every length from 6 up —
including the two "poison" lengths (6 and 14) whose presence dooms a
candidate. So the forcing question sharpens into two alternatives,
either sufficient: prove every candidate in the critical size window
must carry a poison path length, or prove it must carry a 16-cycle.
The overnight order-21 search continues to run and was deliberately
left alone.

## Proposed next step

Run the poison-length census over the already-generated databases of
candidate-shaped graphs at sizes 18–20 (and 21 once the running
search finishes): for every graph, compute its set of
terminal-to-terminal path lengths and check whether any graph escapes
both poison lengths (6 and 14) while keeping the "every vertex
carries traffic" property. If none escapes, the first alternative
survives its cheapest possible test exactly where the dangerous
configuration would have to live, and the way the escapes die out
between sizes 10 and 16 (where escapees exist — the two calibration
graphs among them) measures the mechanism to prove. If one escapes,
it is a genuinely new kind of test object, the first alternative is
dead as stated, and the attack shifts wholly to the 16-cycle
alternative. Deferred alternatives: attacking the forcing lemma
directly without this census (rejected — the census is cheaper and
either shapes or falsifies the lemma first), and the block-order
15/16 kill rung (Tier 3, harvest-only).

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 8%
- Previous estimate, if any: 8% (S023)
- Reason for change: none — held.
- Basis: the session did what a probe should — killed the
  membership-collision mechanism for minutes of compute and replaced
  it with two sharper mutually-covering sub-targets, a proved
  confinement lemma, and a named missing tool. The negative (third
  arithmetic-can't-force-it result in a row) and the positive (the
  saturation phenomenon is real, universal at the frontier, and now
  the explicit target with a cheap first test) roughly cancel. The
  strongest obstacle is unchanged: the forcing content itself is
  unproved and the upper window (22–35) has no data.

This is a subjective research outlook, not mathematical evidence or a
claim-status promotion.
