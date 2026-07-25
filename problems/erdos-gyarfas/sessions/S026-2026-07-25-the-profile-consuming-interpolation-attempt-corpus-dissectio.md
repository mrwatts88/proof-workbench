# S026 — the profile-consuming interpolation attempt: corpus dissection against the eight profile objects and the reroute mechanism

- Date: 2026-07-25
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1 (unchanged).
- Work / claim status: `active` / `open`.
- Strongest established facts: T5/`L049` (theorem, audited `R002`) with the
  unconditional spectrum identity `L048`(iii); **(F) ⟺ case (5b) empty below
  36**, (F) = (F-S) ∨ (F-T) (`A025` T4); the trunk bound `L051`; the census
  verdict `C046` — (F-S) past its first kill test, zero gapped exactly-two
  members on disk at 10–20, and 9,061 vertex-taut gapped pairs off the
  profile (the tautness-only mechanism refuted); floors: counterexamples
  \(\ge22\), tight 1-atoms \(\ge22\), \(\mathcal G\)-members \(\ge21\).
- Open obligations in scope: `G015` (exclude case (5b)), `G013`(a).
- Inherited next action: the **profile-consuming interpolation attempt** —
  target lemma: vertex-taut \(\{C_4,C_8\}\)-free pairs with all non-terminal
  degrees \(\ge3\) at orders 18–35 have \(S\supseteq[c,n-1]\) for some
  \(c\le14\) (implies (F-S)); first sub-move: dissect `E026`'s stored
  near-miss corpus against the eight profile objects and extract the
  candidate reroute mechanism.
- Session goal: open the attempt record (`A026`), run the dissection, and
  leave either a named candidate mechanism (with its calibration status) or
  a recorded reason the local form is dead.
- Falsifiable next move: the dissection itself — if no structural feature
  separates the eight profile objects from the 9,061 near-miss rows at the
  gap lengths, the local-reroute form of the lemma dies in-session.
- Background: `E024` (order-21 rung) **running throughout** (launched at
  S023 close, relaunched 09:55 today per its status file; parts 0–7 of 16
  in flight, confirmed via `pgrep` read-only at session start; ~21 h wall,
  so it will not land today). Untouched, excluded from every ledger row.
  Analysis compute here is corpus-scale (thousands of rows), throttled and
  nice'd per the `E026` pattern.

## Strategy audit

- Tier served: **Tier 1** (`G015`, case (5b), proof side — the (F) program's
  named missing tool).
- Why the inherited route might work: the census left exactly one viable
  hypothesis set (the exactly-two profile) and delivered an unusually sharp
  contrastive corpus — 8 positive objects vs 9,061 stored negatives at the
  same orders in the same class — so mechanism extraction has real data to
  bite on; and the profile hypothesis is unburned (no recorded technique has
  ever consumed "min degree \(\ge3\) off the terminals" for length lower
  bounds), so the space is genuinely unexplored rather than known-hard.
- Fastest way to falsify it: the dissection is failure-first by design — it
  can show in one pass that the profile/near-miss contrast is **not**
  localizable (extra degree-2 vertices unrelated to where the gaps form; no
  reroute feature separating the classes), killing the local form of the
  lemma before any proof effort is spent.
- Mechanistically distinct alternatives weighed: (i) attack (F-T) first
  (cycle-space compression for \(16\in\mathrm{Spec}\)) — deferred: the
  census showed it equally profile-bound, and this same dissection feeds it
  (the corpus stores per-row \(C_{16}\) status); (ii) draft the lemma by
  pure thought and only then test — rejected: a draft that holds on any
  corpus row is unsound by construction (standing trigger), so the corpus
  contrast must come first; (iii) harvest `E024` — unavailable (still
  running, lands tomorrow); (iv) Tier 3 legs — harvest-only by standing
  rule. The tool-building weighing of `AGENTS.md` is satisfied identically:
  this attempt *is* the internal tool-building move, with the corpus as its
  kill condition.
- Target-strength caution (recorded up front): the interval form
  \(S\supseteq[c,n-1]\) includes \(n-1\in S\) (a Hamiltonian \(a\)–\(b\)
  path) — far stronger than (F-S) needs (\(6\in S\) or \(14\in S\)). The
  attempt treats the interval as the observed phenomenon and keeps the
  weaker poison-forcing forms as fallback targets; overclaiming the interval
  when only the poisons are needed would be self-inflicted difficulty.
- Selected route and reason: the inherited dissection-first attempt
  (`A026`/`E027`) — cheapest decisive move on the only surviving proof-side
  program, with the kill discipline built in.
- Pivot criterion: dissection shows no localizable contrast → drop the
  local-reroute form, escalate to global arguments (block-chain arithmetic /
  (F-T) compression); any draft lemma holding on a corpus row → unsound,
  kill immediately; a soundness alarm against `E026`'s recorded fields →
  halt and audit before proceeding.

## Work performed

- Opened attempt `A026` (the profile-consuming interpolation lemma) with
  the kill discipline and target family (interval / poison / step forms)
  fixed before any data was touched, including the recorded
  target-strength caution (the interval form implies Hamiltonian
  connectivity — treat as phenomenon, not target).
- Built and ran `E027` (`dissect.py`): pre-registered questions Q1–Q4 +
  control fixed in the docstring before production; anchors 35 checks
  under CPython 3.14.2 **and** PyPy 7.3.23 (classifier micro-tests;
  Petersen\(-e\) by edge list; the order-14 exemplar; hand graphs for
  chains/smoothing/triangles; corpus and profile loading identities);
  then `corpus` (9,061 rows + 8 profile objects, 0.8 s), `control` (556
  stride members, 14,098 full enumerations, 0.7 s), and — added after
  the first tables were read, pre-registered before it ran — `exchange`
  (the first-order disjoint-chord calculus on one Hamiltonian path per
  profile object and per Hamiltonian corpus row).
- Scratchpad analyses (frontier cross-tabs, mod-4 patterns, exemplar
  dissections, the full-dodge re-cut) drove three instrument
  extensions; all conclusions were then recomputed inside `E027` or
  recorded from its data files.
- `E024` ran throughout, untouched (8 workers on parts 0–7 of 16 at
  session start, per `pgrep` read-only; launched 09:55 today, ~21 h
  wall — confirmed it cannot land in-session). All `E027` compute ran
  single-process at `nice -n 15`.

## Results

- **Computational evidence (`C047`, the dissection verdict):**
  - **Taxonomy (Q1/Q2):** every corpus dodge is shape A (short +
    6-hole: \(\max S\le13\); the minimal full dodges have \(\max S=13\)
    *exactly* at every order 16–20), A′ (distance: \(\min S=7\)
    exactly, never \(\ge8\)), or B (long-range: holes exactly at
    \(\{6,10,14\}\), even part \(\subseteq4\mathbb Z\) on 395/419
    order-20 rows — the `L034` channel-(iii) pattern in-window on
    non-bipartite members; needs ndeg2 \(\ge7\)). The 14-dodge is
    never by distance; the 6-dodge never by shortness.
  - **Pair-locality + frontier (T2):** full-dodge frontier min ndeg2 =
    5/7/5/6/5/6/**4** at 12–20; the ndeg2-4 realization is
    adjacent-terminals (\(S=\{1\}\cup[8,13]\)), reducing recursively
    to an off-terminal distance dodge; frontier members carry five
    fully saturated sibling pairs — member-level lemmas are dead; the
    profile hypothesis is load-bearing by two subdivision vertices.
  - **Subdivision frame (Q3):** corridor weights {2: 47,662, 3: 2,006,
    4: 10}; 99.1% of dodge rows smooth to class-violating reduced
    graphs (all 83 exceptions theta-hubs, all shape A; shape B 100%).
  - **Control:** ordinary taut pairs break the upper-interval property
    at 12–17% (holes at 7–9, ~0.1% at \(\ge13\)); Hamiltonian pairs
    22–29%; the profile-8's joint saturation is far outside both.
  - **Exchange validation (T6):** on all eight profile objects the
    first-order calculus generates the entire top of \(S\) down to 10
    (misses \(\subseteq[4,9]\)), **14 on all eight**; on the 36
    Hamiltonian dodgers it fills no interval — their chord geometry
    (two span-2 chords, spans \(\equiv1,2\bmod4\)) makes savings
    \(\equiv3\bmod4\) unreachable; soundness asserted throughout.
- **Proved:** the span law (`A026` T5, one line): no path in a
  \(\{C_4,C_8\}\)-free graph has a chord of span 3 or span 7; verified
  by assertion on all eight objects and all 36 dodgers.
- **Refuted mechanism candidates:** member-level hypotheses (T2);
  odd-cycle-supply discrimination (T4: 100% of dodge members carry
  triangles).
- **Program structure (provisional, `A026` T7):** (L-A) ∧ (L-B) ⟹
  (F-S) — (L-A) short-range exclusion (\(\max S\ge14\) in-window on
  the profile, or \(6\in S\) when short); (L-B) long-range poison
  forcing (\(\max S\ge14\Rightarrow14\in S\) or \(6\in S\)). The
  missing tool sharpens to the span/savings combinatorics of
  longest-path chord systems ((L-B) engine, validated) and
  ear-overload ((L-A) candidate, no engine yet). Labelled speculation;
  no ledger row at lemma strength.

## Failed routes and why

Two candidate mechanisms were killed cheaply, as intended: member-level
lemmas (the frontier members' saturated sibling pairs are the
counterexample) and odd-cycle-supply discrimination (dodge members are
triangle-rich). The naive upper-interval decomposition ("interval
theorem class-wide + range theorem profile-specific") died on the
control data (12–17% violations). The pivot criterion ("no localizable
contrast → drop the local form") half-fired — the contrast is not
terminal-local — but the taxonomy's rigidity and the exchange engine's
validation kept the attempt inside the (F) program with sharper
targets instead of pivoting to (F-T).

## Adversarial check

- Anchors under both interpreters before production, with named-object
  ties to three prior experiments' recorded values; the calibration
  objects re-found with their exact recorded \(S\)-sets and correctly
  classified by the new code.
- Every corpus row's stored fields structurally re-validated; \(\min
  S=d(a,b)\) asserted on all 9,061 rows; every 250th row fully
  re-enumerated by the independent `E018` enumerator (37 rows,
  identical); the `L035` parity soundness alarm armed on every corpus
  row and every control taut pair — zero violations.
- The exchange calculus carries a per-length soundness assert (every
  generated length must be in the recorded \(S\)) — it fired never,
  on 8 + 36 objects.
- The smoothing construction is verified per row by an edge-count
  identity and anchored on a hand-checkable subdivided \(K_4\).
- Scope honesty: the corpus is a *selected* set (gapped rows only);
  order 20 samples 11/16 parts; the exchange test is one deterministic
  path per object (a lower bound on the calculus, not on \(S\));
  nothing claimed at orders 21+; the frontier trend is explicitly
  recorded as compatible with (F-S) failing at higher orders.

## Canonical records changed

- [ ] `STATEMENT.md` (unchanged — no statement change)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`C047` new)
- [x] `OBLIGATIONS.md` (`G015` S026 update)
- [ ] `PROOF.md` (unchanged — integrated argument did not change)
- [ ] `DECISIONS.md` (unchanged — no statement or architecture change:
  the dissection split the candidate lemma *inside* `A025` T4's frame;
  (F-S)/(F-T) stand verbatim)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: counterexamples \(\ge22\) (window \([22,24]\));
  tight 1-atoms \(\ge22\), \(\mathcal G\)-members \(\ge21\); case (5b)
  below 36 ⟺ (F) = (F-S) ∨ (F-T); (F-S) ⟸ (L-A) ∧ (L-B) with the
  chord-savings engine validated for (L-B); the dodge frontier two
  subdivisions from the profile at order 20; `E024` (order 21) still
  running.
- Remaining blockers: no proof step for (L-A) (thin margin, no
  engine) or (L-B) (engine validated but the savings-reachability
  statement unproved and unaxiomatized); the exactly-two class still
  has eight data points; no exactly-two data above order 20 until
  `E024` lands.
- Recalibration decision: **continued** — the inherited dissection
  sub-move ran as designed, extracted a mechanism sharper than the
  redirect anticipated, and the attempt stays inside the (F) program
  with the split targets.
- Best live alternative or reframing: (F-T) via cycle-space
  compression if both halves stall; the `C038` kill rung and the
  disjoint long-link descent behind it; Tier 2 bipartite EGC.
- Pivot trigger: `E024` outcomes (a gapped or short-range exactly-two
  member at 21 kills (F-S)/(L-A); an \(S\)-satisfying hit is a
  disproof); a chord-savings draft that holds on any of the 36
  Hamiltonian dodgers (unsound by construction); a short-range
  exactly-two pair anywhere in-window (kills (L-A) as stated).
- Best next action: harvest `E024` (census + exchange-test the
  order-21 rung), then the (L-B) chord-savings attempt (build the
  \(C_4/C_8\) chord-pair exclusion table over a longest path; prove
  savings \(M-14\) or \(M-6\) reachable in-window on the profile),
  then (L-A) ear-overload.
- Files a new session should read: `STATE.md` resume list (`A026` and
  `E027/README.md` first).

## Plain-language recap

Last session ended with a puzzle: over nine thousand graphs escape the
two "poison" path lengths while sitting right next to the dangerous
configuration's exact shape, and whatever forces the poisons on the
exact shape had to be hiding in the difference. This session took the
nine thousand escapes apart. Three findings. First, every escape works
in one of exactly three rigid ways: keep every terminal-to-terminal
path short (the longest is always exactly 13 — one below the poison at
14), start the two terminals too far apart (distance exactly 7, never
more), or run a striking arithmetic pattern in which even-length paths
come only in multiples of four, killing lengths 6, 10 and 14 together.
Second, the escapes are structurally parasitic: they all ride on
"corridor" vertices that the exact shape forbids, and when those
corridors are contracted away, 99% of the escapes reveal a graph that
violates the forbidden-cycle rules — the escapes are stretched-out
illegal graphs, and the exact shape is precisely the class that cannot
stretch. The escape frontier now stands two corridor vertices from the
exact shape, and the escape belongs to a specific terminal pair, not
to the graph — the frontier graphs each carry one escaping pair
alongside five fully saturated ones, which rules out whole classes of
would-be proofs. Third, and most constructively, a concrete engine
fell out: take a longest terminal-to-terminal path and reroute it
along its shortcut edges. A one-line fact (proved) says shortcuts
spanning 3 or 7 steps can never exist — they would close a forbidden
cycle — and on all eight known exact-shape graphs, the rerouting rule
alone already produces every path length from 10 up to the maximum,
both poisons included, while provably producing none of the escapees'
missing lengths. The proof problem is now two named lemmas instead of
one vague one: show the exact shape cannot keep all its paths short
(the half with the thin safety margin), and show its shortcut
structure always reaches a poison length (the half the new engine
covers). The overnight size-21 search kept running untouched
throughout and is harvested first next session.

## Proposed next step

Harvest the size-21 search when it lands (it ran all day; each new
exact-shape graph found there gets the full poison census and the new
shortcut-engine test; a shape-matching graph that escapes the poisons
would kill the current approach, and one that also avoids all
forbidden cycles would disprove the conjecture outright). Then open
the first of the two named lemmas — the shortcut half: catalogue
exactly which shortcut patterns the forbidden cycles allow on a
longest path, and try to prove that the exact shape always has enough
shortcuts to walk the path length down to a poison. Any draft must
fail on the thirty-six stored escapees (their shortcut patterns are
the exact obstruction) and succeed on the eight known graphs.
Deferred alternative: attacking the short-path half first — it has
the thinner empirical margin and no engine yet, so the shortcut half
goes first.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 8%
- Previous estimate, if any: 8% (S025)
- Reason for change: none — held.
- Basis: the dissection delivered more than expected — a rigid
  taxonomy, a proved micro-lemma (the span law), and a validated
  engine for one of the two halves — but the other half ((L-A),
  short-range exclusion) has a two-subdivision empirical margin, no
  engine, and a frontier trend compatible with the whole forcing
  target failing at sizes 21–35. Eight data points still carry the
  positive side. Sharper instruments, unchanged distance to a proof.

This is a subjective research outlook, not mathematical evidence or a
claim-status promotion.
