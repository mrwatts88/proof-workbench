# S005 — Classify full one-excursion witnesses and recalibrate the saturation route

- Date: 2026-07-23
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: internal `L001`–`L014`, especially the
  saturation reduction `L008`, its leaf-block persistence `L011`, and the
  certified external ear `L012`; imported `C004`–`C009`
- Open obligations in scope: `G008`, the full-witness intersection step;
  `G007`, making the global restriction decisive
- Inherited next action: classify the `L012` Mersenne witness when its
  vertices outside the shortest odd cycle form exactly one component,
  retaining the total length and every cycle intersection; either force a
  power-of-two cycle or exhibit an infinite surviving length family
- Session goal: complete that classification decisively and recalibrate the
  route portfolio on its outcome
- Falsifiable next move: construct, for each attachment configuration, either
  a forced power-of-two cycle or an explicit infinite power-free family

## Strategy audit

- Why the inherited route might work: the coupled system — total length
  \(2^k-1\), both arcs, both gaps, the shortest-odd-cycle bound — might be
  infeasible without a power-of-two cycle, unlike the single extracted ear
  refuted by `L014`.
- Fastest way to falsify it: exhibit one infinite power-free family per
  configuration type; a failure-first construction attempt precedes any
  forcing attempt.
- Mechanistically distinct alternative or reframing: jump directly to the
  variable-length path/adjuster reframing, or jump to a computational search
  exploiting saturation at small orders. Both were deferred until the
  classification, which is cheap and decisive for the recorded pivot trigger,
  was complete.
- Selected route and reason: execute the inherited classification first; its
  outcome either supplies the missing forcing step or fires the recorded
  pivot condition, so its information value is maximal per unit effort.
- Pivot criterion: the recorded trigger — both the one-component and
  two-component witness patterns admit unconstrained infinite power-free
  families.

## Work performed

- Proved the decomposition lemma inside `A005/L015`: a one-excursion witness
  is exactly \(A_1\cdot Q\cdot A_2\) with \(A_1\ni u\), \(A_2\ni w\) disjoint
  arcs of the induced shortest odd cycle \(C\) and \(Q\) an external ear, so
  \(C\cup P\) is a theta graph with exactly three cycles of lengths
  \(q,\ \ell+s,\ \ell+q-s\).
- Reduced the full one-witness data to an exact constraint system: total
  length \(\alpha+\ell+\beta=2^k-1\); the even theta length avoids powers of
  two; the odd theta length is at least \(q\); and the placement relations,
  which fall into types T1 (both arcs trivial), T2 (one trivial; aligned or
  crossed), T3 (both nontrivial; aligned or crossed).
- Constructed six explicit infinite families, one per configuration type,
  covering both \(d=2\) and the \(d=4\) case forced when \(q-2\) is Mersenne:
  theta graphs on \(q\in\{7,9,11\}\) with free parameter \(k\), verified
  against every constraint. This is `L015`.
- Constructed the double-theta family on \(C_7\) with two disjoint ears of
  length \(2^{k-1}-1\): a genuine two-excursion witness of total length
  \(2^k-1\) whose seven cycle lengths
  \(7,2^{k-1}+3,2^{k-1}+3,2^{k-1}+2,2^{k-1}+2,2^k+1,2^k+2\) avoid all powers
  of two for every \(k\ge4\). This is `L016`, proved via the contraction of
  degree-\(2\) vertices onto \(K_4\) and its seven cycles.
- Recorded the sparsity heuristic (labeled intuition, not a claim): every
  even cycle length in these systems is an affine expression with unit
  coefficient in a free segment length, and gaps between consecutive powers
  of two grow without bound, so bounded witness diagrams always admit
  power-free solutions.
- Derived the finite collapse of saturation: at orders \(n\le15\) witness
  lengths are \(3\) or \(7\) exactly, and only \(C_4,C_8\) are excludable
  power cycles; with `L006` and the minimum-order addendum of `L008`, the
  nonexistence of an order-\(11\) saturated counterexample is finitely
  checkable and lifts every counterexample's order to at least \(12\).
- Fired the recorded pivot trigger, resolved `G008` on its obstruction horn,
  opened `G009`, and recalibrated the portfolio in `DECISIONS.md`,
  `STATE.md`, and `problem.json`.

## Results

- Proved `L015`: every attachment configuration of a full one-excursion
  witness admits infinitely many power-free theta realizations.
- Proved `L016`: a full two-excursion pattern admits infinitely many
  power-free double-theta realizations.
- Provisional insight (heuristic only): no bounded witness diagram can force
  a power-of-two cycle; decisive mechanisms must couple unboundedly many
  witnesses or generate an interval of even cycle lengths.
- Provisional insight (exact but not yet exploited): at orders \(\le15\),
  saturation reads "every nonedge has a simple path of length \(3\) or
  \(7\)".
- Computational evidence: none added this session.
- Imported facts: none added this session.

## Failed routes and why

- The hoped-for forcing horn of the classification failed immediately and
  permanently: already the fully degenerate configuration — a single ear of
  length \(2^k-1\) joining the distance-\(2\) pair on \(C_7\) — satisfies
  every one-witness constraint with cycle lengths \(7,2^k+1,2^k+4\). The
  classification still has content: sporadic parameters such as \(k=3\) in
  the T2 crossed type force a \(C_{16}\) and are excluded, but no family is.
- Salvage: the six families plus `L016` define exactly which length patterns
  any multi-witness or interval mechanism must kill, and the sparsity
  heuristic explains why nothing bounded will do it.

## Adversarial check

- Verified the decomposition uses only facts in scope: \(C\) induced comes
  from `L012`'s proof; arcs follow from inducedness; disjointness from path
  simplicity.
- Proved the theta cycle inventory rather than assuming it: three cycles
  exactly, via the two branch vertices of degree \(3\).
- Rechecked every family row arithmetically: totals \(\alpha+\ell+\beta\),
  arc lengths \(s\) from explicit coordinates, parity of the two new theta
  lengths, the odd length at least \(q\), the even length strictly between
  consecutive powers of two in the stated \(k\)-range, \(\ell\ge2\), and the
  non-Mersenne requirement on \(q-d\), including the forced switch to
  \(d=4\) at \(q=9\).
- Confirmed the `L016` cycle count against the \(K_4\) contraction: four
  triangles and three quadrilaterals, seven cycles, lengths checked at
  general \(k\) and numerically at \(k=4\): \(7,11,11,10,10,17,18\).
- Confirmed both lemmas' scope limits: all family members contain
  degree-\(2\) vertices, so they refute proposed implications only and are
  not counterexamples to `C001` or `L011`; recorded this in `CLAIMS.md`.
- Checked the order-\(11\) collapse both ways: a length-\(15\) path needs
  \(16\) vertices, and \(C_{16}\) needs \(16\) vertices, so witness lengths
  \(\{3,7\}\) and excluded cycles \(\{C_4,C_8\}\) are exact at \(n=11\); the
  minimum-order addendum applies at \(11\) precisely because `L006` excludes
  all smaller counterexamples.
- Kept the sparsity argument labeled as heuristic; it is recorded as
  intuition guiding route selection and is barred from proofs.

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

- Current frontier: saturation is fully established as a reduction
  (`L008`–`L013`) and fully delimited as a single-witness forcing mechanism
  (`L014`–`L016`). The live frontier is the finite one: whether an
  order-\(11\) saturated counterexample exists is finitely checkable and
  decisive for the order bound.
- Remaining blockers: `G002`, `G003`, `G007` for the asymptotic mechanism;
  `G009` for the finite frontier; `G004` for provenance.
- Recalibration decision: pivoted. The recorded trigger fired; single-witness
  forcing is retired. The search route replaces it as primary because it is
  immediate, decisive either way, and exploits saturation exactly where it is
  strongest; the trigger's named successor, the variable-length reframing,
  was kept as the alternative because it lacks a small falsifiable first
  move at minimum degree \(3\).
- Best live alternative or reframing: the variable-length/adjuster
  reframing, now sharpened to a concrete demand — an interval of even cycle
  lengths at minimum degree \(3\) — with unbounded multi-witness coupling as
  its second form.
- Pivot trigger: the order-\(11\) search proves intractable after honest
  optimization, or orders \(11\)–\(13\) all clear without accumulating
  structural insight.
- Best next action: run an exhaustive order-\(11\) search for saturated
  counterexamples — minimum degree at least \(3\), no \(C_4\) or \(C_8\),
  and a simple path of length \(3\) or \(7\) across every nonedge; either
  prove none exists, lifting the counterexample lower bound to twelve
  vertices, or record the survivors.
- Files a new session should read: `STATE.md`, `CLAIMS.md`,
  `OBLIGATIONS.md`, `A005`, the source audit, and this session.

## Plain-language recap

A maximally filled hypothetical counterexample certifies every missing edge
with a path whose length is one less than a power of two. The open question
from last session was whether one such certificate, kept whole — its exact
length and every place it touches a shortest odd cycle — must already create
a forbidden cycle. This session settled that question negatively and
completely. In every geometric arrangement of one detour, and also with two
detours, there are infinitely many ways to satisfy every constraint while
dodging all powers of two. The reason is simple and important: powers of two
spread out exponentially, so a bounded diagram with one stretchable segment
always has room to avoid them. Individual certificates, however detailed, will
never finish the job; only many certificates interacting at once, or a
mechanism producing a whole interval of even cycle lengths, could.

The session also found where the certificates are strongest: in small graphs
they have almost no slack, because with at most fifteen vertices every
certificate must have length exactly three or seven. That turns the next
question into a finite computation at eleven vertices, the smallest size not
already ruled out. The conjecture itself remains open; nothing here is a
proof or disproof candidate.

## Proposed next step

Run a complete computer search over graphs with eleven vertices in which
every vertex has at least three neighbors, no cycle of length four or eight
occurs, and every missing edge is joined by a path of exactly three or seven
edges. If no such graph exists, a proved reduction lifts the smallest
possible counterexample from eleven to twelve vertices; if one exists, it is
a revealing near-miss structure worth close study. The alternative considered
and deferred is the variable-length path mechanism aimed at producing many
even cycle lengths at once; it stays live but currently lacks an equally
small, decisive first move.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 1%
- Previous estimate, if any: 1%
- Reason for change: no change. The session removed an entire class of
  candidate mechanisms and opened a tractable finite frontier; the negative
  and positive information roughly balance.
- Basis: the most promising route is the saturated finite frontier, which is
  decisive order by order; the strongest obstacle is unchanged — no known
  mechanism forces a specific power-of-two length at minimum degree \(3\),
  and the sparsity heuristic now explains why bounded local patterns cannot
  supply one.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
