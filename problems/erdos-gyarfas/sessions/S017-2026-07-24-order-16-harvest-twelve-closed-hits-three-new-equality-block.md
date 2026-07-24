# S017 — Order-16 harvest: twelve closed hits, three new equality blocks, no strict hit, pencil endgame and interference census extended

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: as at S015 close (`L033`/`L034`,
  `C032`/`C033`); the S016 session (a different agent) is concurrently
  active in the same working tree (its `L035`/`E015`/`C034` work is
  visible but uncommitted and is not used or touched here).
- Open obligations in scope: `G013` (catalogue frontier data only).
- Inherited task: harvest the `E013` order-16 closed scan launched in
  S015 (per the user's explicit direction at S015 close: a short
  dedicated follow-up session for the harvest alone).
- Session scope: mechanical closure — record and classify the completed
  scan's results. No strategy audit is performed (the contract's
  exemption for mechanical closure work applies); no new route is
  selected; the concurrent S016 session owns the strategic close.

## Work performed

- Read the completed scan (`runclosed 16`, PyPy 7.3.23, 5,986.0s):
  stream 1,006,553,591 (new datum; no `C027` reference at 16),
  eligible 55,213,924, pairs 420,006,891, zero non-taut completions,
  **12 taut closed hits** (bands 4:3, 6:3, 7:6), all at boundary
  \(s_{\max}=2d\), all containing a \(C_8\).
- Classified every hit (terminal degrees, cut vertices): eight
  pendant-type; four core pairs on three new graphs — the two band-4
  pairs on the sub-cubic-free graph proved isomorphic as two-terminal
  gadgets (labelg-cross-anchored engine), so the block catalogue grows
  five → **eight**: F16 (band 4, terminal degrees (3,3), two symmetric
  realizations), G16 (band 4, (2,4)), H16 (band 6, (2,2), the first
  block with \(C_{16}\) in its spectrum). Every block remains at
  exact equality \(s_{\max}=2\,s_{\min}\).
- Pencil-endgame check on the three band-4 core gadgets: all
  **disjoint-type** (4 shortest paths, 4 internally disjoint pairs, 4
  of 6 \(C_8\)s through both terminals each) — no pencil-type band-4
  taut core exists through order 16.
- Interference census: every \(C_8\) of every new core pair is a
  two-through-path symmetric difference (6/6, 6/6, 6/6, 10/10).
- Full details and tables: the S017 addendum in `E013/README.md`;
  raw data `E013/data/catalogue_closed_n16.json` (committed).

## Results

- Computational evidence (order 16, exhaustive for the stream class):
  no strict taut pinched pair (the strict catalogue stands complete at
  seven witnesses through order 16); no power-free closed taut pair;
  three new equality blocks, no strict block; the pencil endgame's
  empty base and the 100% interference census both extend by one
  order. Pair-level only: order 16 has no analogue of `C027`'s
  stream-level \(C_8\) statement, and the `L034` congruence channels
  (unbanded scans) remain unscanned at 16.
- No disproof material; no pivot trigger fired (in particular the
  pencil endgame survives, and the equality phenomenon now covers
  eight blocks across orders 10–16).

## Deferred canonical updates (shared-tree constraint) — APPLIED

While the scan was being classified, the concurrent S016 session held
uncommitted edits to `CLAIMS.md`, `OBLIGATIONS.md`, `PROOF.md`,
`STATE.md`, `DECISIONS.md`, and `LOG.md`, so the first S017 commit
(31db367) carried only harvest-scoped paths plus this punch list.
S016 then closed and pushed (0ed984d) before this session ended, so
the punch list below was applied in-session in a second S017 commit:
the ledger row became `C035`; the frontier phrases in
`OBLIGATIONS.md` (G013), `PROOF.md` (L033 bullet and the G013 gap),
`STATE.md` (program status (b′)) and `PROJECT_STATE.md` now read
"through order 16" with the eight-block catalogue; and one
cross-record conflict in the S016 close was repaired conservatively:
`PROOF.md`'s L035 bullet said the bipartite class was empty "through
order 22 (23 with a pendant)" while its supporting record `C034` and
`STATE.md` say through 21 (22 with a pendant; the order-22 run
explicitly unfinished and excluded) — the summary was aligned to the
supporting record. The original punch list, as recorded at the first
commit:

- The **claim-ledger row** for this harvest is deferred. Proposed row
  (to be added by the next session that holds `CLAIMS.md` cleanly,
  under the next free C-number, state `tested`, support "`E013`
  `runclosed 16` (S017)", dependencies "geng anchored as in
  `E010`–`E013`; `L031`–`L033` supply the predictions tested"):
  "E013 order-16 closed extension (S017): stream 1,006,553,591;
  55,213,924 eligible; 420,006,891 pairs; twelve taut closed hits,
  all at boundary and all containing a \(C_8\) — so no strict taut
  pinched pair and no power-free closed taut pair exists at order 16;
  bands 4:3/6:3/7:6; eight pendant-type; three new equality blocks
  (band-4 F16 with terminal degrees (3,3) in two gadget-isomorphic
  realizations, band-4 G16 (2,4), band-6 H16 (2,2) with \(C_{16}\)
  in spectrum), extending the block catalogue to eight, all at exact
  equality, no strict block through 16; all band-4 cores
  disjoint-type (pencil endgame base extends); interference census
  remains 100% (6/6, 6/6, 6/6, 10/10)."
- The catalogue-frontier phrases "through order 15" in
  `STATE.md`/`OBLIGATIONS.md`/`PROOF.md`/`PROJECT_STATE.md` summaries
  should read "through order 16" for: strict-block emptiness, the
  pencil endgame's empty base, and the block-catalogue coverage (now
  eight blocks); `PROJECT_STATE.md`'s and `STATE.md`'s "order-16 scan
  in flight / untouched" phrasings should point to this harvest
  (mid-write, S016 also took `PROJECT_STATE.md`, so it joined the
  deferred list).
- A `LOG.md` entry with this session's summary was appended directly
  (append-only file; left unstaged so it rides with the S016 close
  commit rather than sweeping that session's other LOG changes).

## Adversarial check

- The scan's own asserts ran (stream simplicity of the pipeline,
  eccentricity/long-path filters proved as necessary conditions in
  `E013`); the L028/L030 boundary assert passed on every hit.
- Classifications used the anchored `E013` primitives (the
  two-terminal isomorphism engine cross-anchored against labelg in
  S014); the disjoint-pair and symmetric-difference counts were
  computed from full path/cycle enumerations per gadget.
- The strict-catalogue completeness claim at 16 rests on the
  boundary-flag subsumption argument recorded in `C032`'s support
  (strict ⊂ closed consistency asserted at every order \(\le15\);
  the identical scanner logic applies at 16).

## Canonical records changed

- [x] `E013/README.md` (S017 addendum) and
  `E013/data/catalogue_closed_n16.json` (committed, 31db367)
- [x] `LOG.md` (S017 entry appended; committed in the second commit)
- [x] `CLAIMS.md` (`C035` + dependency note), `OBLIGATIONS.md` (G013
  frontier), `PROOF.md` (L033/gap frontier + the L035 off-by-one
  repair), `STATE.md` ((b′) rewritten to the order-16 catalogue),
  `PROJECT_STATE.md` — applied post-S016-close in the second commit;
  `DECISIONS.md` untouched (no decision changed); statement unchanged
- [x] Session-scoped changes committed and pushed (both commits)

## Plain-language recap

The one-billion-graph sweep of 16-vertex candidates finished and was
recorded. Nothing dangerous to the conjecture appeared: every
surviving engine configuration still carries an 8-cycle. But the lab
grew substantially: three brand-new "engines at exact spread two"
turned up — the first at the smallest battlefield (shortest connection
4) since the Petersen-graph specimen, one of them living inside a
graph with no low-degree vertices at all, and the first whose cycle
lengths include 16. Every engine known, now eight of them, sits at
exactly the factor-two boundary, and every one of their 8-cycles is
still the overlay of two terminal-to-terminal paths — the pattern the
current proof effort is built on. The bottleneck-impossibility
conjecture from the previous session survived its first genuinely new
test order. Because a parallel session was mid-flight in the same
repository, this session wrote its results into the experiment's own
records and left a precise punch list for the ledger updates, rather
than editing files the other session had open.

## Proposed next step

Unchanged from the S015 close (the concurrent S016 session owns the
strategic close and next action); the only addition from this harvest
is bookkeeping: apply the deferred ledger row and frontier-phrase
updates listed above in the next session that holds the canonical
files cleanly, and treat the three new blocks — especially the
sub-cubic-free band-4 one — as fresh laboratory material for the
pencil-endgame and interference threads.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement:
  4% (unchanged from S015; this session was pure harvest — the
  catalogue extended exactly along predicted lines, with no pivot
  trigger fired in either direction. The concurrent S016 session's
  own findings are not assessed here.)

This is a subjective research outlook, not mathematical evidence or a
claim-status promotion.
