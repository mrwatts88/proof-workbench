# S015 — The band-4 block rungs: pencil structure of the 4-path system, the interference mechanism, and the order-15 core catalogue

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L022` (counterexamples \(\ge19\)
  vertices); `L025`–`L032` atom/rung/lobe/block program; `C030`/`C031`
  exact catalogue through order 14 (five equality blocks, no strict
  block, every \(C_8\) a two-through-path symmetric difference).
- Open obligations in scope: `G013` (1-atoms; the block question),
  `G007`, `G003`.
- Inherited next action: the band-4 block rungs — (i) strict
  (\(S\subseteq\{4,\dots,7\}\) impossible) and (ii) equality power
  (\(S\subseteq\{4,\dots,8\}\Rightarrow C_8\)), candidate mechanism the
  disjoint/intersecting dichotomy on 4-paths; order-15 closed catalogue
  under PyPy as search leg.
- Session goal: settle the mechanism half (rigidity of intersecting
  4-path systems), extend the catalogue to order 15, and convert the
  results into the sharpest provable rung statement.
- Falsifiable next move: the order-15 scan — a strict block kills (i),
  a \(C_8\)-free equality block kills (ii) and enters the disproof
  protocol.
- User input mid-session: a strategy memo from a different AI agent,
  supplied verbatim with the instructions to fold it into the records
  without acting on it yet, and — standing — that all research threads
  be documented and carried in parallel, none dropped by a choice of
  direction. Integrated via `A016` (audit), `L034`, `G014`, and the
  Thread A–F portfolio in `STATE.md`; memo preserved in
  `references/external-agent-strategy-memo-2026-07-24.md`.

## Strategy audit

- Why the inherited route might work: band 4 is the smallest open case,
  Petersen\(-e\) is a concrete guide, and the two-path interference
  census (23/23) makes the disjoint/intersecting dichotomy the visible
  mechanism; the search leg is cheap (PyPy) and decisive in both
  directions.
- Fastest way to falsify it: the order-15 scan itself (either a strict
  block or a \(C_8\)-free equality block ends the rungs as stated); for
  the proof half, an exhaustive small-order check of the claimed
  rigidity statements before investing in write-up.
- Mechanistically distinct alternative or reframing: 1-atom structure
  theory (deferred again — still no new lever); the band-5 equality
  analogue (dominated by band 4); order-16 census (cost previously
  deferred, revisited below once order 15 ran in minutes).
- Selected route and reason: the inherited route, mechanism half first —
  it is exactly where a lemma-sized theorem could exist, and the search
  legs run in the background at no attention cost. Within the mechanism,
  verification-before-recording was enforced: every claimed lemma was
  machine-checked exhaustively at small orders before entering the
  ledger.
- Pivot criterion: any order-15/16 hit of the two kill types (strict
  block → disproof-side reweighting; \(C_8\)-free equality block →
  disproof protocol); or the rigidity claims failing verification.

## Work performed

- Proved the **band-4 pencil dichotomy** (`A015` T0–T3, ledger `L033`):
  in any graph with \(d(x,y)=4\), the (2,2)-vertices are exactly the
  4-path middles with a product structure per middle; either two
  internally disjoint 4-paths exist — equivalently a \(C_8\) through
  both terminals — or all 4-paths share one internal vertex. The
  dichotomy needs **no** \(C_4\)-freeness: the planned anchor realizing
  the "triangle" configuration with a \(C_4\) failed to build (its
  assert fired), and chasing the failure produced the product/two-tie
  argument that removed the hypothesis. Under \(C_4\)-freeness: single
  overlap, unique terminal-adjacent pencil vertex (middle pencils force
  a unique 4-path), fan rigidity (strands biject with middles, unique
  exits, no cross chords, hexagons per strand pair), far-neighbor
  separation of both terminal neighborhoods (T3).
- Reformulated rung (ii) as the **pencil endgame**: no vertex-taut
  2-connected \(C_4\)-free core with \(d(x,y)=4\), \(s_{\max}\le8\) has
  a pencilled 4-path system — equivalent to closing band 4 of the block
  question in the strengthened form "\(C_8\) through both terminals".
- Built `E014`: exhaustive verification of `L033` (116,187 \(C_4\)-free
  distance-4 pairs at orders 5–11; 43,419 general pairs at orders 5–9;
  zero failures; two sharpness anchors) and the \(C_4\)-allowed block
  probe (orders 6–9): strict blocks from order 6 (\(K_{3,3}-e\)),
  strict band-4 blocks with \(S=\{4,5,6,7\}\) at order 8, band-4
  equality cores with no \(C_8\) at order 9 — so \(C_4\)-freeness is
  essential to both rungs (`C033`).
- Extended `E013` to order 15 under PyPy 7.3.23 (anchors re-passed;
  61,813,970 stream graphs, 22,022,137 pairs per mode, ~5 min per
  mode): strict scan = exactly one hit, machine-identified as D14's
  pendant lift (the `C031` swap-symmetry prediction confirmed); closed
  scan = 20 hits, all pendant-type; block catalogue unchanged through
  15; no closed hit at any band \(\le3\); the closed band-4 world is
  three objects, only Petersen\(-e\) a core, disjoint-type (`C032`).
  The `cores` command's two hardcoded counts were updated (6→7
  witnesses) for the extension; `cores`/`dissect` re-run: five distinct
  cores, interference census extends (every \(C_8\) in every witness
  and core a two-path symmetric difference).
- Launched the order-16 closed scan (the first order where a hit could
  be \(C_8\)-free, `C027` ending at 15); still running at session
  close — per the user's mid-session direction, the session closes now
  and the harvest is reserved for a short dedicated follow-up session,
  so `C032` deliberately covers order 15 only.
- Three hand construction attempts against the pencil endgame (fan,
  t = 2), each dying to a specific violation (a \(C_8\) through one
  terminal via exit-matching; a 9-path via the hub splice \(u\sim c\);
  \(C_4\)s at every web closure): the "cascade" obstruction, recorded
  in `A015` with the deep-territory caveat ((3,3)–(4,4) coordinates
  unexplored by hand).
- **External memo integration (second half of session).** Audited the
  user-supplied memo claim by claim (`A016`, memo verbatim in
  `references/`): its core is correct and was independently re-derived
  — `A011` R1's ring spectrum formula never used the pinch, so the
  ring disproof criterion is any-\(L\)-sumset avoidance (`L034`), with
  parity (all-odd \(S\), odd \(L\)), odd-prime gcd, and mod-4 channels
  beside the pinched one; fatal shapes invisible to the 2-atom frame:
  \(S=\{3,7\}\), \(S=\{2,6\}\). Verified mitigations the memo lacked:
  `C027` is stream-level and profile-agnostic, so every channel is
  empty through order 15 (18 for degree-\(\ge3\) terminal pairs); the
  all-odd ladder lives at odd bands only, disjoint from the band-4
  pencil battlefield; `L030` already forces the \(\{3,7\}\)-shape on
  the taut band-3 parity rung. Corrections recorded: the three
  "pinch = the criterion" glosses retracted (framing error, no proved
  row false; `L031`/`L032` are pinch-specific — pendant shifts flip
  parity — so the parity channel needs its own reduction theory); the
  program ceiling made explicit (assembly closure + 1-atoms = the
  cubic reduction, not 0.1). The memo's literature/census leads are
  unverified: `G014` opened. Its six paths entered the portfolio as
  Threads B–E beside all pre-existing threads; nothing was executed on
  them this session per the user's instruction.

## Results

- Proved claims: `L033` (T0 product structure; T1 general pencil
  dichotomy; T1′ \(C_8\)-through-terminals equivalence; T2 \(C_4\)-free
  refinements; T3 far-neighbor lemma; T4 endgame reduction); `L034`
  (generalized ring criterion with the parity/gcd/mod-4 instances and
  the corrected necessary conditions — corollary of `A011` R1,
  independently re-derived during the `A016` audit).
- Refuted in-session: the expectation that the dichotomy needs
  \(C_4\)-freeness (machine-refuted anchor became a stronger theorem);
  the hope that either band-4 rung could be proved without
  \(C_4\)-freeness (`C033` specimens at orders 6–9); the framing that
  the pinch is *the* ring criterion (three glosses retracted — the
  memo's headline, confirmed; no proved row false).
- Computational evidence: `C032` (order-15 extension: D14-lift
  prediction confirmed; block catalogue stable; band distribution 4–7),
  `C033` (`E014` verification + necessity).
- Provisional insights (not lemmas): the cascade obstruction against
  fan-type cores; the band-2 closed rung (\(S\subseteq\{2,3,4\}\),
  \(4\in S\)) identified as the last \(C_4\)-only gap below band 4;
  pendant-type closed boundary hits reduce to excess-\(+1\) cores
  (the \(e(H)=e(\text{core})-1\) bookkeeping), so they are not block
  material; the all-odd ladder lives at odd bands only; the
  3-connectivity mod-\(m\) exclusion sketch (`A016` M10); the memo's
  Mersenne-window logic for bipartite gadgets at orders \(\le31\)
  (conditional on the `G014` \(\ge32\) import).
- Imported facts needing verification: the `G014` list (Chen–Saito;
  bipartite \(\ge32\) and bipartite-EGC-to-31; Heckman–Krakovski;
  Shauger and Daniel–Shauger; census provenance items) — none usable
  until audited.

## Failed routes and why

No route abandoned. One planned sub-claim (the \(C_4\)-dependent
triangle anchor) was refuted by its own verification assert and replaced
by the stronger hypothesis-free theorem — recorded in `A015` as the
productive failure. The three endgame construction attempts failed as
constructions (that is the desired direction) and are preserved as
pressure-point data.

## Adversarial check

- Every lemma was machine-verified exhaustively at small orders before
  ledger entry (`E014`: 159,606 distance-4 pairs across both streams,
  zero failures); the verification caught a real error — the planned
  anchor encoding the session's initial belief about where
  \(C_4\)-freeness enters.
- The two sharpness anchors confirm the refinements genuinely consume
  \(C_4\)-freeness (double-middle overlap; product fan at a middle).
- The order-15 run cross-checks: stream totals against `C027`, strict ⊂
  closed consistency, `C028` witnesses re-found, `cores` lift bijection
  re-verified with the seventh witness, D14 identification by
  terminal-respecting isomorphism (the engine that was itself
  labelg-cross-anchored in S014), plus a direct terminal-respecting
  isomorphism check of the extracted core against the recorded
  closed-14 D14 hit.
- The construction attempts actively tried to falsify the session's own
  endgame conjecture before it was recorded as the next target.
- The external memo was treated as untrusted input: every mathematical
  claim re-derived or bounded in `A016` (R1 re-read at source; sumset
  arithmetic by hand; the "wrong class" and "never looked" claims
  corrected against `C027`'s actual coverage; literature claims
  quarantined behind `G014`); its provenance and unaudited status are
  recorded on the reference file itself.

## Canonical records changed

- [ ] `STATEMENT.md` (unchanged; statement version stays 0.1)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`L033`, `C032`, `C033` + dependency notes)
- [x] `OBLIGATIONS.md` (`G013` refined to the pencil endgame at band 4)
- [x] `PROOF.md` (outline: pencil dichotomy added; `G013` gap rescoped)
- [x] `DECISIONS.md` (pencil-endgame reformulation)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: finite exclusions unchanged (`L022`); block
  catalogue stable through order 15 (five equality blocks, no strict
  block); band 4 of the pinched channel = the pencil endgame, empty
  through 15, with the order-16 scan running at close (harvest in the
  follow-up session); both band-4 rungs proven to require
  \(C_4\)-freeness; the assembly interface widened to the `L034`
  sumset criterion — parity/gcd/mod-4 channels open, empty through 15,
  shape-unscanned, no reduction theory.
- Remaining blockers: `G013` (1-atoms; the pencil endgame and higher
  pinched rungs; the congruence channels), `G014` (import audits),
  `G007`, `G002`, `G003`.
- Recalibration decision: continued on the inherited route for the
  session's first half (mechanism half became `L033`); mid-session the
  interface itself was corrected (`L034`) on audited external input —
  recorded as a widening, not a pivot: every prior thread stays live
  per the user's standing instruction, and the new channels entered
  the portfolio without displacing the pencil endgame.
- Best live alternative or reframing: Thread B (parity calibration +
  bipartite gadget hunt) — cheap and decisive; the band-2 closed rung
  warm-up; 1-atom structure theory.
- Pivot trigger: a pencil-type band-4 taut core at order 16+ (kills
  the endgame as stated); a strict block or \(C_8\)-free equality
  block at 16 (disproof protocol); an all-odd taut core found by the
  calibration scan (re-weights toward the parity channel); a `G014`
  audit overturning an assumed bound.
- Best next action: strategy-audit the expanded portfolio; proposed
  first moves are the odd-\(S\) calibration scan (orders \(\le15\))
  and the `G014` source audits, with the pencil endgame co-primary on
  the pinched channel.
- Files a new session should read: `STATE.md`, `A016` + the memo
  reference file, `A015`, `E014/README.md`, `E013/README.md`
  (extension section), `A014`, `CLAIMS.md` `L031`–`L034`/
  `C030`–`C033`, `OBLIGATIONS.md` `G013`/`G014`, this session.

## Plain-language recap

The disproof strategy builds counterexamples by chaining copies of a
two-terminal "engine" into a ring; the ring's cycle lengths are sums
of the engine's path lengths, so the engine wins if those sums can
dodge every power of two. The session had two halves. First half: for
engines whose path lengths squeeze inside a factor-of-two window (the
program's target class until now), the smallest open battlefield is
engines with shortest connection 4, and this session proved a clean
structure theorem there: either two shortest paths avoid each other
entirely — instantly creating an 8-cycle, the very thing the engine
must avoid — or every shortest path threads one bottleneck vertex next
to a terminal, in a rigid, fully mapped "fan". The session's own
verification machinery caught that the theorem needs no assumptions at
all (a planned test case was impossible to build, which is how an
assumption fell away). Machine searches show no bottleneck engine
exists up to 15 vertices; three hand attempts to build one collapsed
for three different structural reasons; the 16-vertex search ran
during the session. Second half: the user brought in an outside
review, and its central point survived a line-by-line audit — the sums
can dodge the powers of two by *arithmetic*, not just by squeezing:
if all path lengths are odd, sums of an odd number of them are odd and
never a power of two, and similar tricks work with common factors. So
the hunt has several parallel grounds, not one. Everything proved so
far stands (the factor-of-two ground really is closed as recorded, and
prior searches incidentally show the new grounds are also empty
through 15 vertices), but three summary claims that had presented the
factor-of-two condition as the whole criterion were retracted, one
honest ceiling was made explicit (even total success on the engine
program only reduces the conjecture to 3-regular graphs), and the new
grounds — including a bipartite engine hunt with cheap decisive
searches, a 3-regular census extension where any hit is instantly a
counterexample, and two new proof-side theorem targets — entered the
research portfolio alongside every existing thread, per the user's
instruction that no thread be dropped.

## Proposed next step

Open the next session with a strategy audit over the expanded
portfolio; the proposed first moves are the two cheap decisive ones.
(1) The parity calibration scan: rerun the engine catalogue machinery
at up to 15 vertices hunting engines whose path lengths are all odd
(the new arithmetic channel) instead of factor-of-two-squeezed — it
either exhibits the first "shape specimens" of the new channel or
shows it is as empty as the old one. (2) Source-audit the outside
review's literature claims (a divisibility theorem, a bipartite
lower bound that gates the bipartite hunt's window, two partial-case
proofs, and several public graph censuses), since none may be used
until verified. The bottleneck-impossibility fight from the first half
stays co-primary, and all other threads remain live. Considered and
deferred: executing any of the new searches immediately (excluded by
the user's instruction this session), the band-2 warm-up rung, 1-atom
structure theory, and the 17-vertex search leg.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 4%
- Previous estimate, if any: 3% (S014)
- Reason for change: the disproof interface genuinely widened — the
  audited outside review exposed ring channels (parity, common-factor,
  mod-4) that the program's definition had excluded, several with
  cheap decisive searches (bipartite engines at 16–31 vertices; the
  3-regular census at 30 vertices, where any hit is a counterexample
  outright), and the proof side gained two frontier-adjacent targets
  (the bipartite case as a theorem; pushing the published 4/7 cubic
  density to 1). The increase is small because every new channel is
  still empty through 15 vertices, the key literature imports are
  unverified, the ceiling correction reduced the proof-side yield of
  the engine program, and the 1-atom question remains untouched.
- Basis: most promising routes — the parity/bipartite channel and the
  cubic census extension on the disproof side, the pencil endgame and
  bipartite EGC on the proof side; strongest obstacles — nothing yet
  forces spread or power cycles at any generality, the new channels
  have no reduction theory, and the program ceiling; evidence —
  `L033`/`L034`, the `C032` catalogue stability, `C033`'s necessity
  specimens, and the audit trail in `A016`.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
