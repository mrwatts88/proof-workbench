# Project state

Last reviewed: 2026-07-24

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
  (`L047`, extremal window \([22,24]\), three orders wide). Nothing
  is left running.
  Portfolio (all threads carried, per standing user instruction): the
  case-(5b) endgame (the **T5 → (F) interference program** + the
  ladder at order 20+, Tier 1); the `C038` kill rung at
  block orders 15–16; the pencil endgame + band-2 rung (pinched
  channel); the bipartite hunt at order 26 (order 24 harvested empty on the
  new instrument) and the gcd-channel theory question; the cubic census at
  orders 26/28/30 (now ~15 min/3.5 h/2.3 days on 8 workers); census
  mining; bipartite EGC (proof side); the disjoint longer-link descent
  (R2's surviving extension); 3-connectivity leverage; order-17+
  pinched catalogue legs.
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

For `P-002`, keep working **Tier 1: exclude case (5b)** via the **T5 →
(F) interference program** (S022, fully harvested): T5 has survived
every kill rung run so far — all eight profile objects in existence
(orders 19–20), 4,661/4,661 cycles — the atom/\(\mathcal G\) floors
are at 22/21, and the counterexample floor at 22 (`C043`/`C042`,
`L047`; extremal window \([22,24]\), three orders wide). **First
action: the two remaining cheap T5 kill rungs** — `smallworld 13`
(minutes, exhaustive in-class at order 13, via `E021/dissect.py`) and
a sparse general-graph probe at orders 8–9 — then, if T5 survives,
the **T5 proof attempt** (clean-window reroute + minimal-choice
exchange; named sub-obligations: cycle-edge essentiality in taut
pairs, weaving control). The forcing target (F) follows T5,
order-windowed \([18,35]\), doubly calibrated (Petersen\(-e\) and the
order-14 exemplar of `C041`) and backed by eight profile-member data
points realizing the 16-collision and the \(S\)-violation
simultaneously. Tier 3 stays harvest-only (the `C038` kill rung at
block orders 15–16; cubic 26/28; the \(\mathcal G\) rung at order 21,
\(\approx\)18 h, and min-degree-3 at 22, \(\approx\)38 h — both
deliberate decisions; bipartite 26). Do **not** reopen congruence
obstructions (`C037`), membership-only chain exclusion (`L045`), or
the density constant (`L038`); any case-(5b) exclusion argument must
fail on **both** calibration objects unless it consumes
power-freeness or minimality.
No required action remains for `P-001`; its reference comparison is
optional and freely permitted.

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
