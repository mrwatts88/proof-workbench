# S007 — Frontier sweep: import verified bounds, verify the 24-vertex graphs, and test saturation novelty

- Date: 2026-07-23
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L001`–`L017`; imported `C004`–`C009`;
  the S006 finding that the finite frontier route is cheap and decisive
- Open obligations in scope: `G004` (source correspondence, priority),
  `G011` (saturation novelty, priority); `G007` asymptotically
- Inherited next action: run the frontier sweep from primary sources —
  import the strongest verified finite bounds, obtain and internally
  verify the reported 24-vertex \(\{C_4,C_8\}\)-free cubic graphs, and
  search the literature for edge-maximal power-cycle saturation
- Session goal: execute the sweep; then exploit whatever it exposes
- Falsifiable next move: the sweep itself (each import either matches its
  primary source or does not; the novelty search either finds saturation
  or does not)

## Strategy audit

- Why the inherited route might work: it gates everything downstream —
  whether saturation is novel decides where effort goes, and the true
  frontier numbers decide what counts as passing it.
- Fastest way to falsify it: the sweep is self-falsifying; a source
  contradicting an import, or a published saturation paper, would each
  redirect immediately.
- Mechanistically distinct alternative: jump straight to the
  interval-mechanism theory (`G007`); deferred because it lacked a small
  falsifiable first move and wants the imported extremal graphs as test
  material anyway.
- Selected route and reason: the inherited sweep. Mid-session, two
  evidence-driven extensions were adopted under strategic autonomy: (1)
  probing showed the general \(C_4\)-free minimum-degree-3 classes are
  tiny for modern generation, so the published general bound could be
  passed the same day (`E006`, `A007`); (2) the user's strategic question
  plus the Bensmail inspection led to naming a falsification-side route
  and capping the search layer (see `DECISIONS.md`).
- Pivot criterion: saturation found in the literature (fires the recorded
  pivot to the interval reframing) — it was not found.

## Work performed

- Located and read the primary sources: Markström (2004) in full from the
  author's site; Royle's 2002 page from the Wayback Machine (2002-06-25
  snapshot; the 2003 snapshot is content-identical). Exact quotes and the
  audit trail are in `references/source-audit-2026-07-23-S007.md`.
- Exposed the "at least 17 vertices" figure circulating in Wikipedia and
  Hegde–Sandeep–Shashank as an overread: both primary sources verify only
  orders \(\le 15\). Imported the true bounds as `C012` (general,
  \(\ge16\)) and `C013` (cubic, \(\ge30\)).
- Downloaded the House of Graphs Markström graph (id 51419), verified all
  its reported properties, and discovered `C015`: all \(240\) nonedges
  carry Mersenne witness paths — adding any edge creates a power-of-two
  cycle (`E005` Part 1).
- Built the anchored geng pipeline and reproduced the cubic census:
  connected cubic \(\{C_4,C_8\}\)-free classes are empty at orders
  \(14\)–\(22\) (\(36\), \(269\), \(2761\), \(36101\), \(553227\)
  \(C_4\)-free cubic graphs, all containing \(C_8\)); at order \(24\),
  exactly four survivors among \(9{,}467{,}449\) \(C_4\)-free cubic
  graphs — Markström's Table 3 reproduced — with exactly one planar,
  labelg-isomorphic to HoG 51419, and all four fully
  Mersenne-witness-covered (`E005` Part 2, `C018`).
- Ran the general census `E006` at orders \(14\)–\(17\) with anchors
  A1–A5: the connected \(C_4\)-free minimum-degree-3 classes
  (\(6059\); \(91433\); \(1655659\); \(34758006\)) contain no
  \(C_8\)-free member at all. With the hand-proved connectivity and
  collapse lemmas this gives `L018` in `A007`: every counterexample has
  at least eighteen vertices.
- Ran the recorded `G011` novelty sweep (queries plus full-text checks of
  every EGC source held): no appearance of edge-maximal power-cycle
  saturation anywhere; verdict recorded with a repeat-before-publishing
  caveat, and the saturation line adopted as the frontier-passing asset.
- Read Bensmail (2017) in full and imported `C017` (spectrum-confinement
  constructions; all 1-connected). Recorded the resulting falsification
  route — spectrum-density versus power-gapping inside 2-connected blocks
  — in the portfolio, prompted by the user's mid-session strategic
  question.
- Access attempts for the original Erdős 1997 article failed again
  (ScienceDirect robot wall; Rényi archive scans end at 1989); `G004`
  narrowed to that single remaining item.

## Results

- Proved (computer-assisted): `L018` — every counterexample has at least
  \(18\) vertices, passing the strongest inspectable published general
  bound (\(16\), unmoved since 2002). Corollary: the smallest
  \(\{C_4,C_8\}\)-free minimum-degree-3 graph has \(18\)–\(24\) vertices.
- Tested: `C015` (Markström graph verification and full witness
  coverage); `C016` (the order-14–17 general census); `C018` (the cubic
  census through order 24, matching Markström's Table 3 in count,
  planarity, and the identity of the planar member, and showing all four
  extremal graphs fully witness-covered).
- Imported: `C012`, `C013` (true primary bounds), `C014` (Markström's
  Table 3), `C017` (Bensmail).
- Resolved: `G011` (saturation is absent from the swept literature — the
  project's candidate novel asset is confirmed unclaimed territory).
- Insight (provisional): the Markström graph shows the Mersenne-witness
  half of saturation is realizable by a real extremal graph; only
  power-cycle-freeness separates it from an `L008` object. And Bensmail's
  constructions show bounded-spectrum power dodging is exactly a
  1-connected phenomenon — the counterexample question is whether a
  2-connected minimum-degree-3 spectrum can gap every power of two
  against Bondy–Vince/Sudakov–Verstraëte-type density forcing.

## Failed routes and why

- Obtaining the original 1997 Erdős article body: blocked by access, not
  by mathematics; recorded, low stakes.
- No mathematical route failed this session; the S006 caution that
  saturation cannot prune generation was respected by design (saturation
  ran only as a survivor classifier, and no survivor existed below 18).

## Adversarial check

- Import correspondence: every imported number was matched to a quoted
  primary sentence; the one mismatch found (the circulating "17") was
  documented and excluded rather than imported.
- `L018` logic: the connectivity lemma, the collapse windows (including
  why \(C_{16}\) is irrelevant below order 16 and unused at 16–17), and
  the reduction to connected search were each re-derived; the
  minimum-order argument was checked against `L017`'s coverage of orders
  \(\le13\).
- Pipeline trust: geng is an imported tool — anchored against OEIS
  A002851 (cubic counts) and A006786 (squarefree counts), cross-validated
  end-to-end against the independent `E004` at orders 11–13, with
  per-graph independent re-tests of the degree and \(C_4\) conditions and
  two-sided \(C_8\)-filter controls; the dependency is recorded on the
  claim rather than hidden.
- Novelty verdict: recorded as absence-of-evidence with named queries and
  sources, carrying an explicit repeat-before-publishing caveat; it was
  not upgraded into a positive claim.
- Honest scope: `L018` does not bear on the universal statement; the
  session's structural insights are labeled provisional.
- A live catch demonstrating the value of external cross-checks: the
  first survivor pass misused `planarg` (its `-p` output-format flag
  emits a header even for nonplanar input) and briefly reported all four
  order-24 graphs planar. The contradiction with Markström's "only one
  planar" triggered a direct `planarg -V` re-test, the wrapper was fixed
  in all three scripts, and the corrected result agrees with the paper.
  The defective call never entered any claim or canonical record.

## Canonical records changed

- [ ] `STATEMENT.md`
- [x] `STATE.md`
- [x] `CLAIMS.md`
- [x] `OBLIGATIONS.md`
- [x] `PROOF.md`
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: no counterexample below order \(18\) (`L018`); cubic
  below \(30\) (`C013`, imported); the smallest \(\{C_4,C_8\}\)-free
  minimum-degree-3 graphs live in \([18,24]\), with the order-24 cubic
  ones held and verified internally.
- Remaining blockers: `G002`, `G003`, `G007` (the asymptotic mechanism is
  untouched by everything finite); `G004` only for the 1997 article body.
- Recalibration decision: continued and extended — the sweep completed as
  planned, and two evidence-driven extensions (the `E006` bound, the
  Bensmail route) were adopted under strategic autonomy; the exhaustive
  layer is now explicitly capped (about order 18) rather than perpetual.
- Best live alternative or reframing: the falsification-side
  spectrum-gap program (Bensmail-style confinement versus forced density
  in 2-connected blocks); the interval mechanism remains the proof-side
  alternative.
- Pivot trigger: any \(\{C_4,C_8\}\)-free minimum-degree-3 graph found at
  orders 18–23 (instant new structure, possible counterexample screen);
  or a density lemma/construction attempt on the order-24 graphs that
  decisively favors one side of the gap-versus-density tension.
- Best next action: analyze all four order-24 extremal graphs as test
  material for both deep routes — full even-cycle spectra and witness
  structure, checked against the consecutive-even-lengths and
  cycle-pair-forcing mechanisms — and write the first concrete lemma
  target for the chosen route; deferred alternative: extend the census to
  order 18 with a compiled filter.
- Files a new session should read: `STATE.md`, `CLAIMS.md`,
  `OBLIGATIONS.md`, `A007`, the `E005`/`E006` READMEs,
  `references/source-audit-2026-07-23-S007.md`, this session.

## Plain-language recap

This session went to the original sources for everything this project
leans on. Reading the actual 2004 paper and the 2002 search page (dug out
of the Internet Archive) showed that the number everyone repeats — "a
counterexample needs at least 17 vertices" — was never actually computed:
the real searches stopped at 15. We imported the true numbers, downloaded
and dissected the famous 24-vertex near-miss graph, and reproduced from
scratch the 2004 census of such graphs — finding, as claimed, exactly
four, and catching a bug in our own planarity call because our first
readout disagreed with the paper's "only one is planar." A recorded
literature sweep confirmed that this project's own idea — filling a
hypothetical counterexample with edges until every missing edge carries a
tell-tale path — appears nowhere in print, so it is unclaimed territory.
Then the frontier moved: with a modern generator we exhaustively checked
every graph with 14, 15, 16, and 17 vertices where all vertices have at
least three neighbors, and none avoids both a 4-cycle and an 8-cycle. So
any counterexample now provably needs at least 18 vertices — the first
improvement on the general bound in 24 years. A surprising texture
emerged: all four known smallest cycle-avoiding cubic graphs have the
property that adding any single edge creates a forbidden cycle — they sit
exactly at the boundary this project's saturation idea describes.
Finally, prompted by the user's strategic question, we read Bensmail's
2017 paper and named a concrete falsification program: his constructions
dodge forbidden cycle lengths by hiding all cycles in small pockets
behind cut vertices, which is precisely what a true counterexample cannot
do — so the decisive question is whether a robustly connected sparse
graph can steer its cycle lengths around every power of two. The
conjecture itself remains open, and these finite results do not touch its
general case.

## Proposed next step

Take the four verified 24-vertex extremal graphs and use them as test
material for the two deep routes: map their even cycle lengths and
witness structure in full, and check them against the known theorems that
force many cycle lengths in well-connected sparse graphs. The outcome
should be the first concrete lemma target — either a strengthening of the
saturation structure (proof direction) or a spectrum-gap construction
attempt in 2-connected graphs (disproof direction). The deferred
alternative is extending the exhaustive census to 18 vertices under PyPy,
which would either raise the bound to 19 or exhibit the first
cycle-avoiding graphs below 24 — useful, but capped, support work.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate, if any: 1%
- Reason for change: not the new bound (finite exclusions never touch the
  universal statement) but the improved route inventory: the saturation
  idea is confirmed absent from the literature, meaning unclaimed room to
  work; and the Bensmail reading yielded a concrete, mechanistically
  distinct falsification program (spectrum gapping versus forced density
  in 2-connected blocks) where progress in either direction is meaningful.
- Basis: most promising route — the falsification-side spectrum program,
  because the conjecture's authors expected it false and the enabling and
  blocking mechanisms are now both identified; strongest obstacle — no
  known control of full cycle spectra in 2-connected minimum-degree-3
  families, and the proof-side interval technology remains far above
  degree 3. The estimate stays low because both routes demand tools the
  field does not yet have.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
