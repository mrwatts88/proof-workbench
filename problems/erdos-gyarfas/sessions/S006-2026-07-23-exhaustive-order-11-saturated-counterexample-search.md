# S006 — Exhaustive order-11 saturated-counterexample search

- Date: 2026-07-23
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L001`–`L016`; the S005 pivot retiring
  single-witness saturation forcing; the small-order collapse observation
- Open obligations in scope: `G009`, the order-\(11\) search; `G007`
  asymptotically
- Inherited next action: run an exhaustive order-\(11\) search for saturated
  counterexamples — minimum degree \(3\), no \(C_4\) or \(C_8\), a path of
  length \(3\) or \(7\) across every nonedge — and either prove none exists
  or record survivors
- Session goal: execute that search with proof-grade coverage and
  validation, and extend upward while cheap
- Falsifiable next move: the search itself; it is decisive either way at
  each order

## Strategy audit

- Why the inherited route might work: the collapse at orders \(\le15\) makes
  the frontier exactly finitely checkable, and each cleared order is a
  proved lemma rather than evidence.
- Fastest way to falsify it: run the search; intractability or survivors
  would each end the route quickly.
- Mechanistically distinct alternative or reframing: the variable-length
  reframing toward an interval of even cycle lengths; deferred again because
  it still lacks a small falsifiable first move, while the search is
  immediate and decisive.
- Selected route and reason: the inherited search, with one design deviation
  discovered during planning: saturation cannot prune a generation tree,
  because edge-maximality constrains only completed graphs, so the search
  was implemented as a plain exhaustive \(\{C_4,C_8\}\)-free enumeration
  with saturation kept as a survivor classifier. At orders \(\le15\) that
  class is exactly the counterexample class, so this is also logically
  stronger.
- Pivot criterion: intractability after honest optimization, verified
  survivors, or closing the collapse range at order \(15\).

## Work performed

- Built `E004` (`saturated.py`): degree-sequence enumeration under the
  proved codegree bound; least-unfinished-vertex labelled completion as in
  `E002`; incremental rejection of any edge closing a path of length \(3\)
  or \(7\); canonical restriction of vertex \(0\)'s neighbourhood to
  per-degree-block prefixes; per-leaf independent re-verification and
  saturation classification; always-on self-checks including the `L016`
  double-theta graph and the hand-derived order-\(11\) sequence list.
- Validated against five anchors: `E001`'s independent \(19{,}355\)
  labelled cubic graphs at order \(8\); `E002`'s independent \(937{,}440\)
  labelled \(C_4\)-free cubic graphs at order \(10\), all containing
  \(C_8\); the exact symmetry quotient \(937{,}440/\binom93=11{,}160\);
  incremental-vs-independent \(C_8\) consistency at order \(10\); and the
  positive control at order \(8\) where incremental \(C_8\) rejection and
  independent classification agree at exactly the \(35\) labelled copies of
  \(K_4\sqcup K_4\), ruling out over-rejection on a nonzero class.
- Ran order \(11\): \(12\) degree sequences, \(231{,}646\) nodes, zero
  \(\{C_4,C_8\}\)-free graphs. Order \(12\): \(29\) sequences,
  \(6{,}535{,}800\) nodes, zero. Order \(13\): \(59\) sequences,
  \(44{,}397{,}061\) nodes, zero. All three sequence counts were re-derived
  by hand; the order-\(13\) hand count initially missed the budget-exact
  sequence \((7,7,4,3^{10})\) before agreeing at \(59\).
- Proved `L017` in `A006`: the small-order collapse (at \(n\le15\),
  counterexample \(=\) \(\{\delta\ge3\), no \(C_4\), no \(C_8\}\); witness
  lengths collapse to \(\{3,7\}\)), the two coverage layers of the search,
  and the conclusion that every counterexample has at least fourteen
  vertices, from `L006` plus the three empty orders.
- Resolved `G009` in the stronger form; opened `G010` for orders
  \(14\)–\(15\); recorded in `DECISIONS.md` that the saturation-accelerator
  premise was wrong generatively and that `L008` was not needed for `L017`.

## Results

- Proved `L017` (computer-assisted): every counterexample has at least
  fourteen vertices.
- Tested `C011`: the exhaustive computation behind it, with its five
  validation anchors.
- Provisional insight: incremental \(C_8\) rejection collapses the search
  tree (order \(11\) needed \(231{,}646\) nodes against \(4{,}252{,}251\)
  for order \(10\) with \(C_4\) rejection alone in `E002`); the pair
  \(\{C_4,C_8\}\) binds very strongly at small orders.
- Provisional insight: the smallest \(\{C_4,C_8\}\)-free graph of minimum
  degree \(3\) has between \(14\) and \(24\) vertices, the upper end from
  the literature's reported cubic examples; locating the threshold is now a
  concrete subgoal with direct conjecture consequences through order
  \(15\).
- Imported facts: none added.

## Failed routes and why

- Saturation as a generative search accelerator failed conceptually before
  running: edge-maximality constrains completed graphs only, so it cannot
  prune partial graphs. It survives as a survivor classifier, and no
  survivor has yet existed for it to classify. The route's actual engine is
  incremental \(C_8\) rejection.

## Adversarial check

- Coverage: re-derived all three degree-sequence lists by hand (\(12\),
  \(29\), \(59\)); verified the codegree-bound argument; confirmed the
  completion scheme generates each labelled graph exactly once, including
  that a vertex's unrealized neighbours always have larger index when it
  becomes least unfinished.
- Rejection exactness both directions: a closed path of length \(3\)/\(7\)
  persists into every completion, so rejection loses no valid leaf; any
  \(C_4\)/\(C_8\) in a leaf would have been caught at its last-added edge,
  so no forbidden leaf survives.
- Over-rejection was additionally excluded empirically by the V5 positive
  control on a class with nonzero truth, \(35\) being also the hand count
  of labelled \(K_4\sqcup K_4\) copies.
- Symmetry restriction: proved the block-prefix relabelling argument and
  confirmed the exact uniform quotient \(937{,}440/84=11{,}160\) at order
  \(10\).
- Noted honestly that the per-leaf independent re-checks were vacuous at
  orders \(11\)–\(13\) because no leaf existed; correctness rests on the
  five anchors, which include nonzero classes on both the \(C_4\) and
  \(C_8\) sides.
- Checked the collapse boundary: the program refuses orders outside
  \(4\)–\(15\), where the constants \(\{3,7\}\)/\(\{4,8\}\) would be wrong.
- Confirmed no novelty claim: reported literature computations exceed these
  orders; they were neither reproduced nor relied on.

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

- Current frontier: orders \(11\)–\(13\) are excluded outright; the finite
  frontier stands at order \(14\), with the collapse range ending at
  \(15\). The asymptotic mechanism (`G007`) is untouched.
- Remaining blockers: `G002`, `G003`, `G007` asymptotically; `G010` on the
  frontier; `G004` provenance.
- Recalibration decision: continued, with the recorded internal correction
  that saturation is a classifier, not an accelerator; the frontier route
  performed exactly as selected and cleared three orders in one session.
- Best live alternative or reframing: the variable-length/interval
  reframing; unchanged.
- Pivot trigger: order-\(14\) intractability, a verified survivor, or
  closing order \(15\).
- Best next action: extend the exhaustive search to order \(14\) with
  parallel decomposition and re-validated anchors; either prove emptiness,
  lifting the bound to fifteen, or independently verify and analyze the
  first survivors.
- Files a new session should read: `STATE.md`, `CLAIMS.md`,
  `OBLIGATIONS.md`, `A006`, the `E004` README, and this session.

## Plain-language recap

For graphs small enough — up to fifteen vertices — being a counterexample to
this conjecture means exactly one checkable thing: every vertex has at least
three neighbors, and the graph has no cycle of length four and none of
length eight. This session built a careful exhaustive program for that
condition, validated it five separate ways against earlier independent
computations and hand-countable cases, and proved that no such graph exists
with eleven, twelve, or thirteen vertices. Consequently any counterexample
must have at least fourteen vertices. The searches stayed fast because
avoiding both cycle lengths simultaneously is very restrictive. An honest
side finding: the certificate structure from the previous sessions, while
logically sound, contributed nothing computational here — the exclusions
held for the plain class before certificates even entered. The conjecture
itself remains open, and these finite steps, while solid, do not by
themselves approach the general statement.

## Proposed next step

Run the same validated exhaustive search at fourteen vertices, after adding
a parallel work-splitting layer and re-running the five validation anchors,
since fourteen will be several times larger than thirteen's forty-four
million search nodes. If no graph passes, every counterexample needs at
least fifteen vertices; if one passes, it would be an actual counterexample
candidate and must first be independently verified, then studied closely.
The deferred alternative remains the theoretical mechanism aimed at
producing many even cycle lengths at once; the frontier search stays primary
while it remains cheap and decisive.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 1%
- Previous estimate, if any: 1%
- Reason for change: no change. Three orders were excluded with a reusable
  validated tool, but finite exclusions do not touch the universal
  statement, and the asymptotic gap is what the estimate prices.
- Basis: the frontier route is cheap, decisive, and cumulative through order
  fifteen; the strongest obstacle is unchanged — no mechanism forces a
  specific power-of-two cycle length at minimum degree three, and
  `L015`–`L016` proved the bounded local versions of the best current idea
  cannot work.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
