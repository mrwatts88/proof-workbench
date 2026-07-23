# S002 — Independent structural attack

- Date: 2026-07-23
- Problem: `P-001`

## Starting checkpoint

- Statement version: 0.2
- Work / claim status: `active` / `open`
- Strongest established facts: normalized target and the one-, two-, and
  three-vertex boundary checks
- Open obligations in scope: `G002`, independent proof or disproof
- Session goal: attack the target structurally without consulting any known
  solution or reference
- Falsifiable next move: test whether neighborhood structure and comparison of
  nonadjacent vertices force useful degree constraints

## Work performed

- Opened `A001` and derived `L001`: each induced neighborhood is 1-regular, so
  every graph degree is even.
- Constructed an injection between neighborhoods to prove `L002`: nonadjacent
  vertices have equal degree.
- Under the counterexample assumption, proved `L003`: the complement is
  connected. Combined this with `L002` to prove regularity (`L004`).
- Translated common-neighbor counts into
  \(A^2=J+(k-1)I\), then used an explicit eigenspace decomposition and the
  zero trace to prove `L005`, ruling out the regular counterexample.
- Integrated the full argument into `PROOF.md`.
- Performed no web search, source inspection, reference comparison, or
  computation.

## Results

- Proved `L001`–`L005` within the attempt record.
- Resolved `G002` with a self-contained integrated proof candidate for `C001`.
- No computational or imported evidence was used.
- The main dossier status advances only to `proof_candidate`; review obligation
  `G003` remains open.

## Failed routes and why

The initial maximum-degree idea was unnecessary. The stronger injection argument
showed that degrees of nonadjacent vertices differ by at most one and hence,
because all degrees are even, are equal. This eliminated the need for an extremal
degree analysis.

## Adversarial check

- Checked that the neighborhood injection cannot identify two domain vertices:
  such an identification creates two distinct common neighbors.
- Checked that “no universal vertex” makes every complement component have at
  least two vertices, which is needed in the disconnected-complement
  contradiction.
- Expanded the matrix argument without invoking a spectral theorem: the
  \(+s/-s\) decomposition is given by an explicit formula.
- Checked the rational-square-root step in lowest terms and the divisibility
  chain \(s\mid k=s^2+1\).
- Rechecked the singleton case separately and confirmed that the empty graph
  remains out of scope.
- This is a discovery-session self-audit, not an independent review.

## Canonical records changed

- [ ] `STATEMENT.md`
- [x] `STATE.md`
- [x] `CLAIMS.md`
- [x] `OBLIGATIONS.md`
- [x] `PROOF.md`
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index

## Ending checkpoint

- Current frontier: a complete self-contained proof candidate using `L001`–`L005`
- Remaining blockers: `G003`, the required adversarial reviews; `G004`, reference
  comparison intentionally deferred
- Best next action: conduct a clean-context statement-correspondence and
  line-by-line logic audit, focusing on `L002`, `L003`, and trace equation (4)
- Files a new session should read: `STATEMENT.md`, `CLAIMS.md`,
  `OBLIGATIONS.md`, `PROOF.md`, `A001`, and this session record

## Plain-language recap

We found a complete independent route. The common-neighbor rule forces strong
local pairing and degree constraints. If no vertex knew every other vertex, those
constraints would make the entire graph regular. Counting two-step walks with a
matrix then leaves only the triangle, where every vertex does know every other
vertex—a contradiction. The argument is now written as a candidate, but separate
review sessions still need to try to break it before the project calls it proved.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 95%
- Previous estimate, if any: 85%
- Reason for change: the session produced a complete self-contained proof
  candidate
- Basis: the route has an explicit dependency chain and uses no unverified
  external theorem or essential computation. The main remaining risk is a hidden
  issue in the injection, complement case split, or trace arithmetic, all of
  which are concrete targets for the required reviews.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
