# S019 — G015 route R1: forced local structure of a minimum-order tight 1-atom (parallel with S020 on route R2)

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L022` (counterexamples have ≥19 vertices);
  the assembly programme `L025`–`L036`; `L029` restated with tightness
  (S018); base data `C027` (no tight 1-atom through order 15) and `C034`
  (no bipartite tight 1-atom through order 22).
- Open obligations in scope: `G015` (the cubic reduction — Tier 1, the
  named deliverable), `G013`(a) (tight 1-atoms).
- Inherited next action: Tier 1, route R1 first — forced local structure
  at the degree-2 vertex of a minimum-order tight 1-atom; R2 (Carr 4/7 →
  1) held as the alternative.
- Session goal: orchestrate `G015` routes R1 and R2 as parallel worker
  subagents (orchestrated mode, `process/concurrency.md` as amended by
  `O011`), audit their output, and integrate what survives.
- Falsifiable next move: derive the forced structure at the degree-2
  vertex u (neighbour degrees, cutvertex status, the C4-free
  neighbourhood) under order-minimality, and test whether the
  `L030`/`L033` two-terminal collapse machinery transfers to the
  one-terminal object.

### Worker delegation declarations (orchestrated mode)

- Mode correction mid-setup: this session was first scaffolded in the
  two-interactive-session pattern (worktree `../rh-agent-b`, branch
  `s020-r2-carr`, sibling block S020/A020/E017/R003). The user corrected
  the protocol before any sibling work started: parallel legs are
  orchestrated — one worker subagent per route, launched and audited by
  this session. The scaffolding was removed (worktree and branch
  deleted; nothing was committed on them), the protocol repair is
  `O011` (commit 1965b99), and **no S020 session exists for this run**.
- This session (S019) is the orchestrator: it holds every shared ledger
  throughout, launched the workers after recording this assignment,
  audits their output before integration, and performs the single
  canonical checkpoint at close.
- **Worker W1 — route R1**: forced local structure of a minimum-order
  tight 1-atom, executing the plan in `A019`. Owned records: `A019`
  (fills Deductions onward) and `E016` if a computation is needed.
  Agent type `general-purpose`, model `opus` (the floor per `CLAUDE.md`;
  user directive of 2026-07-24: Opus at a minimum, Fable otherwise).
- **Worker W2 — route R2**: line-by-line verification of Carr's density
  argument (arXiv:2605.22844; imports `C004`–`C006`), then attempt
  4/7 → 1. Owned records: `A020`, `E017` if needed, and
  `references/carr-2026-verification-2026-07-24.md`. Agent type
  `general-purpose`, model `opus`.
- Both workers: write only their owned records in this working tree; no
  ledger edits, no `set-status`/`index`, no git commands; a
  counterexample or proof candidate stops the worker, which reports to
  the orchestrator. Reviews (`R002`/`R003` reserved) are initiated only
  by this session, and only for a candidate that survives its audit.
- Dependency declaration: the legs are mechanistically distinct; neither
  consumes the other's output; worker reports are working input at the
  strength of their recorded support, not citable records, and two
  agreeing workers are not corroboration.
- Machine resources: the Tier 3 order-23 bipartite leg (`E015`) runs in
  background under PyPy 7.3.23 (`pypy3 bipscan.py anchors && pypy3
  bipscan.py run 23`, harness task `be2dzoawp`); its results are
  excluded from every ledger row unless it completes before this
  session's close. Workers were told to check load before launching any
  computation.

## Strategy audit

- Tier served (S018 process rule): **Tier 1** — both R1 (this session)
  and R2 (sibling) serve `G015`, the named proof-side deliverable.
- Why the inherited route might work: the tight 1-atom is a strictly
  smaller object than a counterexample as far as anything proved shows
  (`A018` T3), the analogous two-terminal questions collapsed under
  local structure (`L030` middle-layer collapse, `L033` pencil
  dichotomy), and the base emptiness data is strong (`C027`, `C034`).
  Order-minimality is available against the one-terminal object in a way
  it never was against gadgets (a gadget minus a vertex is another
  gadget only under surgery; a tight 1-atom minus its defect vertex has
  a controlled degree profile).
- Fastest way to falsify it: find a tight 1-atom — the local-structure
  analysis doubles as a targeted search specification (it prunes the
  profile a search must generate), and any hit disproves 0.1 outright
  (`L025` R4). Secondary kill: show the collapse machinery cannot see
  the one-terminal object because both machines anchor on *two*
  terminals (then R1 reduces to search-only and R2 becomes primary).
- Mechanistically distinct alternative or reframing: R2 (Carr 4/7 → 1)
  — density/discharging on minimal counterexamples, no atom formalism.
  Not idle this time: worker W2 works it concurrently, which is exactly
  the productive pairing `process/concurrency.md` names.
  A reframing noted at audit time, to be tested first: for `G015` it
  suffices to prove the *conditional* "no cubic counterexample ⟹ no
  tight 1-atom" — the unconditional form is sufficient but possibly
  stronger than needed, and the conditional form has an extra hypothesis
  to spend exactly where `A012` Remark T4.1 failed.
- Selected route and reason: both Tier 1 routes at once, one Opus worker
  each (R1 needs the dossier's internal machinery, which is all on disk
  in `A011`–`A018`; R2 is self-contained around one external paper).
  Orchestrated parallelization directed by the user this session; this
  context does the launching, auditing, and integration.
- Pivot criterion: if the forced-structure analysis stalls without
  either a proof handle or a search specification within the session,
  fold findings into `A019` and reassess against Tier 2 (bipartite EGC)
  rather than manufacturing progress; if a tight 1-atom is found, jump
  to the disproof protocol immediately.

Keep this comparison compact. Do not invent cosmetic alternatives to fill the
template; record the real strategic choice or explain why the session is exempt
(for example, required review or mechanical closure).

## Work performed

- Orchestration setup as declared above; the superseded two-session
  scaffolding and its replacement are recorded in `O011` (commit 1965b99,
  operational). Workers W1 (R1) and W2 (R2) launched in parallel on
  `opus`; `E015` order-23 leg running in background under PyPy.
- **W2 (route R2) returned; orchestrator audit PASSED.** Audit actions:
  (i) write-set inspected — only owned records touched
  (`references/carr-2026-verification-2026-07-24.md`, `A020`, `E017`);
  (ii) the Carr verification note read in full and all four proof
  reconstructions re-derived by the orchestrator (Lemma 0.1 with the
  order/size case split; Cor 0.1(1) neighbour identification;
  Cor 0.1(2); Thm 0.1 exact counting; the equality-case observation
  that `C005` refutes tightness of 4/7) — verdict agreed: verified,
  statement-correspondence with `C004`–`C006` exact; (iii) `A020` read
  in full and W2-T0 through W2-T7 re-verified line by line, including
  the \(\beta\in\{0,1\}\) cases of W2-T6 via `L003`, the
  \(2\beta-3\) degeneracy bound, the descent's simplicity/lift steps,
  and S15's \(C_4\)-freeness case split and explicit 8-cycle; W2-T8
  confirmed to be labeled as reasoning, with its extremal heuristic
  explicitly not imported; (iv) `E017` reproduced by the orchestrator:
  35/35 checks pass, identical output under CPython 3.14.2 and
  PyPy 7.3.23; (v) claim-row correspondence checked against
  `CLAIMS.md` (`C004` verbatim; `L003` covers the degenerate cases).
  One citation-precision note for integration: `L002`'s recorded row
  is stated for an *edge-minimal* counterexample; for the
  order-then-size minimal object cite the now-verified Cor 0.1(2), or
  add the one-line "order-then-size minimal ⟹ edge-minimal" bridge.
- Integration deferred until W1 lands, for a single coherent ledger
  pass at close. Planned integration from W2: new claim rows for
  W2-T1 (2/3 bound), W2-T3 (apex lemma), W2-T4 (equality
  classification), W2-T5 (subdivision descent), W2-T6 (headline
  \(3|V_3|\ge2n+3\)), with W2-T7/S15 as the sharpness certificate;
  `C004`–`C006` upgraded imported → verified (line-by-line note;
  internally reconstructible); the `G014` item for `C004`–`C006`
  discharged; `G015` route R2 re-scoped — the constant route is capped
  at \(2/3+O(1/n)\) by W2-T7/W2-T8(b), the live extension is the
  internally-disjoint longer-link descent of W2-T8(c), and R1 gains
  the link-graph handle of W2-T8(d).
- **W1 (route R1) returned; orchestrator audit PASSED.** Audit actions:
  (i) write-set inspected — only `A019` and `E016` touched; (ii) `A019`
  read in full (981 lines) and W1-T1 through W1-T14 re-verified line by
  line by the orchestrator: the closure-calculus spectra and the
  recorded \(j=0\) asymmetry; the \(\mathcal A\to\mathcal G\) bijection
  including the edge-bound check for `C027` class membership; the
  engine's two branches (bridge sub-case included) and the load-bearing
  strictness \(<n_0\); the peel; all five cases of W1-T6 with their
  degree lists, order counts, and `L022` bounds; W1-T7's conditional
  logic; W1-T8's unconditional \(\ge17\) against `C027`+`L022`;
  2-connectivity; the size-refined independence (bridgelessness via
  W1-T9); the through-set arithmetic including both closure
  contradictions; the triangle-case suppression arithmetic; Mersenne
  saturation and its count; the parity proof of non-bipartiteness; the
  chain constraints with the terminal-not-cut argument and the
  \(S_1-1\) shift; (iii) the transfer verdict W1-T15 checked against
  the recorded rows — `L030`'s row documents exactly the confinement
  anchors and length-6/7 exhibits the worker identified, and `L033`'s
  dependency row ("`D001`–`D004` only" for T0/T1, \(C_4\)-freeness for
  T2/T3) confirms W1-T15.1 is a verbatim application; `L028`/`L032`
  rows likewise match their uses; (iv) `C027`'s row confirmed to cover
  both the one-degree-2 and two-degree-2 profiles at orders \(\le15\)
  (the load-bearing input to \(|H|\ge16\) and \(n_0\ge17\)); (v)
  `E016` reproduced by the orchestrator: all checks pass (12,109
  graphs / 331,115 pairs closure identities; 67,432-graph case
  dichotomy with counts matching the report; `C027` stream counts
  4/5/36/84/918/4058 reproduced; A6 saturation-kill data reproduced);
  (vi) the demotion of W1-T12 after its pre-registered kill test and
  the explicit warnings (no progress on the unconditional form; (R)
  conditionality; `C027`/`L022` lineage on the \(\ge17\)) checked as
  correctly scoped. One audit note: W1-T16 confirms no Carr import is
  consumed, so R1's results are independent of W2's audit outcome —
  the two legs stayed dependency-free as declared.
- **Ledger integration performed (single pass, this session holding all
  ledgers):** `CLAIMS.md` — `C004`/`C005`/`C006` upgraded to
  `imported (verified)` with the verification note cited, `C006`
  marked superseded by `L038`, new rows `L037`–`L042`; `OBLIGATIONS.md`
  — `G015` rewritten to the case-(5b) state, `G013`(a) updated;
  `PROOF.md` — `L037`–`L042` added to the outline, the imports bullet
  upgraded, the `G015` gap rewritten; `DECISIONS.md` — one entry (the
  orchestrated run, the R1 conditional reframing, the R2 constant-route
  closure); `LOG.md` — S019 entry; `STATE.md` — established facts,
  imported frontier, program status (a), Tier 1 rewrite, Tier 3
  order-23 status, pivot triggers, human-level state, outlook 4% → 5%,
  resume list; `problem.json` — next action = the order-16
  \(\mathcal G\) scan + mod-4 companion; `PROJECT_STATE.md` — P-002
  summary and next action.

## Results

- **Proved claims (all audited by the orchestrator before promotion):**
  `L037` (subdivision descent + apex lemma + equality classification),
  `L038` (cubic-density theorem \(3|V_3|\ge2n+3\), superseding `C006`,
  with the S15 sharpness delimitation), `L039` (closure calculus and
  the (3,3) bijection onto \(\mathcal G\)), `L040` (engine + peel),
  `L041` (five-case analysis; conditional cubic reduction modulo case
  (5b); every tight 1-atom has order \(\ge17\)), `L042` (residual-object
  structure under (R): 2-connected, degree-\(\ge4\)-independent,
  through-set arithmetic, triangle case, saturation (demoted),
  non-bipartite, chain cancellation, band-4 pencil transfer).
- **Verified imports:** `C004`, `C005`, `C006` — all four Carr results
  checked statement-by-statement and proof-by-proof against
  arXiv:2605.22844v1; statement-correspondence exact; internally
  reconstructible (`references/carr-2026-verification-2026-07-24.md`).
  The `G015` R2 verification prerequisite is discharged.
- **Provisional insights (recorded, not claims):** the R2 ceiling
  analysis (`A020` W2-T8: LP cap \(2/3+O(1/n)\); no constant \(<1\)
  suffices; the 2-degenerate-power-free edge question; the
  disjointness gap in the longer-link descent; the link-graph bridge to
  R1); the R1 transfer verdict (`A019` W1-T15: confinement vs
  congruence); the demotion of Mersenne saturation after its
  pre-registered kill test.
- **Computational evidence:** `E016` (closure calculus on 331,115
  pairs; case dichotomy on 67,432 graphs; `C027` stream anchors;
  saturation-kill census) and `E017` (S15 certificate, 35 checks) —
  both reproduced independently by the orchestrator under CPython
  3.14.2 and PyPy 7.3.23.
- **Imported facts needing verification:** none new; `C004`–`C006`
  moved the other way (imported → verified).

## Failed routes and why

- **R2 as constant-grinding: closed by evidence, not abandoned by
  fatigue.** S15 realizes every non-power hypothesis at exactly
  \(2/3\), and the proved constraint set caps at \(2/3+O(1/n)\); no
  density constant \(<1\) was ever logically sufficient for `G015`.
  Salvage: `L037`/`L038` themselves, the descent as a reusable
  mechanism, and the two named reopening questions (the
  2-degenerate-power-free edge maximum; the disjoint longer-link
  descent).
- **R1's unconditional form ("no tight 1-atom exists"): retired as a
  target.** Minimality reducts are counterexamples, not tight 1-atoms,
  so the method structurally cannot reach it; the conditional form is
  what `G015` needs and is now one case from closed.
- **The taut ladder as an R1 engine: retired** (`A019` W1-T15 — the
  collapse machinery anchors on interval confinement; the closure
  channel has no window). The band machinery survives (band-4 pencil).
- **Mersenne saturation as a standalone lever: demoted** by its own
  pre-registered kill test (`E016` A6); its parity corollary (`L042`
  non-bipartiteness) survives.

## Adversarial check

- Every worker deduction was re-derived line-by-line by the
  orchestrator before any ledger write; both machine legs were
  reproduced independently under two interpreters; write-sets were
  inspected after each worker returned.
- The workers' own adversarial artefacts were checked for genuineness:
  W1's E016-A1 falsification of its first draft of the identification
  identity (the recorded asymmetry), W1's pre-registered A6 kill test
  firing against its own strongest lemma, and W2's sharpness search run
  *against* its own bound after proving it.
- Statement-correspondence for the import upgrade was checked verbatim
  on both sides (paper text vs recorded rows), and `C027`'s row was
  re-read to confirm it covers both degree profiles the R1 argument
  consumes.
- Conditionality hygiene: all (R)-conditional statements are flagged in
  `L041`/`L042` and in the A019 warnings; the \(\ge17\) bound's
  `C027`/`L022` computational lineage is recorded on the row; no
  worker result was treated as corroborated by the other worker.
- One citation-precision repair made during integration: `L002`'s row
  is stated for edge-minimal counterexamples, so the independence
  input for the order-then-size object is cited via the verified
  Corollary 0.1(2) (or the one-line bridge), as noted in the audit.

## Canonical records changed

- [x] `STATEMENT.md` (unchanged; statement version stays 0.1)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`C004`–`C006` verified; `L037`–`L042` new)
- [x] `OBLIGATIONS.md` (`G015` rewritten; `G013`(a) updated)
- [x] `PROOF.md`
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: statement 0.1 unchanged (counterexamples \(\ge19\)
  vertices); tight 1-atoms \(\ge17\) (`L041`); minimal-counterexample
  cubic density \(\ge(2n+3)/3n\) (`L038`, past the published 4/7);
  `G015` reduced to excluding case (5b); `C004`–`C006` verified.
- Remaining blockers: case (5b) (the congruence-type residual object —
  no confinement machinery applies); `G013`'s block question and
  gcd channel; `G014` items (1),(3)–(6); the global mechanism
  (`G002`/`G003`/`G007`).
- Recalibration decision: pivoted twice on evidence — R1 to its
  conditional form (the unconditional form is method-unreachable), R2
  off constant-grinding (sharpness tombstone). Both pivots are the
  session's own results, not inherited.
- Best live alternative or reframing: if the mod-4 congruence hunt
  dies by its kill condition, case (5b) reduces to search alone and
  the Tier 4 generator build becomes the critical path; Tier 2
  bipartite EGC remains the standing alternative theorem target.
- Pivot trigger: a hit in the order-16 \(\mathcal G\) scan satisfying
  the \(S\)-condition (immediate disproof protocol); the mod-4 kill
  condition firing; exclusion of case (5b) (then `G015` is proved and
  Thread C is the whole game).
- Best next action: the order-16 \(\mathcal G\)-profile scan with the
  mod-4 congruence hunt alongside (as recorded in `problem.json`).
- Files a new session should read: `STATE.md` (roadmap), `A019`,
  `A020`, the Carr verification note, `CLAIMS.md` `L037`–`L042`,
  `OBLIGATIONS.md` `G015`.
- Background job at close: the `E015` order-23 leg (PyPy, harness task
  `be2dzoawp`) is still running; its results are excluded from every
  ledger row above, and the harvest is a named follow-up (S017
  precedent). Re-run command in `E015/README.md`.

## Plain-language recap

This session ran the project's two roads to its main reachable theorem
— "the conjecture is true in general if and only if it is true for
3-regular graphs" — at the same time, in two independent worker agents,
with this session checking every line of both before believing any of
it.

The first road strengthens a published result. A 2026 paper proves
that in a smallest possible counterexample, at least 4/7 of the
vertices have the minimum degree 3. We verified that paper completely
— it holds up — and then beat the bound: at least two-thirds, plus a
little. The improvement needed a new idea: the degree-3 vertices
wedged between two higher-degree vertices act like midpoints of
invisible edges, and those invisible edges form a smaller "shadow
graph" that inherits the no-power-of-two-cycles property with all
lengths halved; because the original graph was the smallest offender,
the shadow must be sparse. But we also proved this road ends here: an
explicit 15-vertex graph meets every assumption the counting uses at
exactly two-thirds, and no percentage short of 100% ever yields the
theorem. The road closes having produced a result stronger than the
literature's and a new reusable tool.

The second road is now the whole game. The "single defect" object — a
graph with exactly one vertex of degree 2, everything else at least 3,
and no power-of-two cycle — was dissected at its defect vertex. Of the
five possible local shapes there, four are now either impossible or
lead to a *smaller* offender, which a repaired old argument converts
into a 3-regular counterexample — and that is the theorem succeeding,
not failing. Exactly one shape survives, and it is tightly cornered:
at least 17 vertices, robustly connected, never two-colourable, and
forced to hit certain exact path lengths while missing others. The
whole theorem now rests on ruling out that one shape. Two concrete
ways forward: an exhaustive computer search at 16 vertices that either
rules it out at that size or — if it finds the object — disproves the
entire conjecture on the spot; and a divisibility-by-4 argument
modelled on the parity proof that worked this session.

## Proposed next step

Run the decisive 16-vertex search for the surviving shape (connected,
no 4-cycle, exactly two degree-2 vertices, everything else at least 3,
no power-of-two cycle, and the special path-length condition). If it
finds nothing, the smallest possible "single defect" graph moves up to
18 vertices and the corner tightens. If it finds the object, the
conjecture is false and we switch immediately to the disproof
protocol. Alongside it, start the divisibility-by-4 attack on the
surviving shape, using this session's two-colourability proof as the
template. Considered and deferred: grinding the density percentage
further (proved pointless this session), the longer-link version of
the descent (a named open repair), and the background two-colourable
search at 23 vertices (still running; harvest when done).

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 5%
- Previous estimate, if any: 4% (S018)
- Reason for change: the reachable deliverable narrowed from two
  open-ended routes to one named configuration with real structure on
  it, and the session produced the dossier's first mechanism that
  turns minimality into structure on an unbounded object (the
  descent). The density route's closure removes a hoped-for path, and
  the surviving configuration is a congruence-type object the dossier
  has no machinery for — which is why the upgrade is one point, not
  more.
- Basis: most promising routes — excluding case (5b) (order-16 scan +
  mod-4 congruence) for the reduction, then the cubic census at order
  30; strongest obstacle — no forcing mechanism at minimum degree 3,
  and the residual object resists all confinement machinery; evidence
  — `L037`–`L042`, the verified `C004`–`C006`, S15, and the two
  reproduced machine legs.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
