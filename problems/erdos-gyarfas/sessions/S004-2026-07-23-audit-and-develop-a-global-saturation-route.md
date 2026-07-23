# S004 — Audit and develop a global saturation route

- Date: 2026-07-23
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: internal `L001`–`L007`; imported
  minimal-counterexample facts `C004`–`C006`, induced path `C007`,
  high-average-degree forcing `C008`, and large-girth cubic existence `C009`
- Open obligations in scope: `G003`, global cycle forcing; `G007`, a
  restriction not shared by the large-girth cubic obstruction
- Inherited next action: derive a genuinely global minimal-counterexample
  restriction, stress-test it against `L007`, and only then seek a
  variable-length cycle argument
- Session goal: determine whether edge-maximal power-cycle saturation supplies
  such a restriction
- Falsifiable next move: maximize a hypothetical counterexample under safe edge
  addition and test the resulting nonedge certificates against a connected
  bipartite cubic graph of girth at least \(17\)

## Strategy audit

- Why the inherited route might work: absence of every power-of-two cycle can
  make every safe edge addition globally informative, unlike the retired local
  induced-path bundle.
- Fastest way to falsify it: determine whether arbitrary connected cubic
  large-girth graphs already satisfy the proposed restriction; a bipartite
  member of that family is the sharp parity test.
- Mechanistically distinct alternative or reframing: adapt the
  Liu–Montgomery variable-length path construction directly to the
  near-2-connected reduction `L001`; this was deferred because its current
  engine requires average degree far above \(3\).
- Selected route and reason: edge-maximal saturation, because it gives an
  elementary certificate for every nonedge and is immediately testable against
  `L007`.
- Pivot criterion: if the certificates yield no bounded-overlap, density, or
  adjustable-length consequence beyond non-bipartiteness, stop treating
  saturation alone as the primary route.

## Work performed

- Opened `A005` and proved `L008`. Starting with a minimum-order
  counterexample if desired, safe edge additions terminate at a
  power-cycle-free graph in which adding any nonedge creates a power-of-two
  cycle. Removing that new edge gives a simple path of length \(2^k-1\)
  between its endpoints.
- Derived the immediate global consequences: the saturated graph is connected
  and non-bipartite, and `C008` bounds its average degree by an absolute
  constant.
- Re-inspected Liu–Montgomery (2023), Theorem 1.1 and Corollary 1.3. Their
  method gives a long interval of consecutive even cycle lengths above a large
  average-degree threshold, but no direct conclusion at minimum degree \(3\).
- Proved `L009` by applying the canonical bipartite double cover to the graph
  from `C009` when necessary. This gives a connected bipartite cubic graph of
  girth at least \(17\), which satisfies the prior local structural bundle but
  fails the odd Mersenne-path requirement for same-class vertex pairs.
- Analyzed saturation witnesses across induced two-edge paths. This produced
  `L010`: two adjacent edges cannot both lie outside all odd cycles. Hence the
  edges outside odd cycles form a matching.
- Combined `L008` and `L010` with the leaf-block argument from `L001` to prove
  `L011`. A witness between two nonexceptional vertices of a leaf block cannot
  exit and return through the unique cut vertex without ceasing to be simple,
  so the saturation condition persists inside the 2-connected block.
- Took a shortest odd cycle in the block from `L011`. It is induced. For a
  cycle of odd length \(q\ge7\), the odd arcs of lengths \(q-2\) and \(q-4\)
  cannot both be Mersenne numbers, so one saturation witness must leave the
  cycle and contains an external ear. This is `L012`.
- During the adversarial pass, observed that 2-connectivity already supplies
  an external ear for every shortest odd cycle, including a triangle or
  \(5\)-cycle; recorded the exact distinction from the certified ear in
  `L012` as `L013`.
- Tested the proposed one-ear theta mechanism at the level of exact length
  equations. Theta path lengths \(2,2r+1,4\) have only the cycle lengths
  \(2r+3,2r+5,6\), proving `L014` and forcing the route to retain the full
  Mersenne witness rather than one extracted ear.

## Results

- Proved `L008`: the edge-maximal saturation reduction and Mersenne-path
  certificates for every nonedge.
- Proved `L009`: the new restriction is absent from a bipartite connected
  cubic large-girth realization of the bundle in `L007`.
- Proved `L010`: edges outside odd cycles form a matching.
- Proved `L011`: a non-bipartite 2-connected near-minimum-degree leaf block
  inherits the nonedge certificates away from its possible cut vertex.
- Proved `L012`: a shortest odd cycle of length at least \(7\) has an external
  ear.
- Proved `L013`: every shortest odd cycle has an external ear from
  2-connectivity, although the short cases lack the `L012` witness
  certificate.
- Proved `L014`: a shortest odd cycle and one arbitrary ear have infinite
  power-free theta length patterns.
- Provisional mechanism: the total Mersenne length and ordered cycle
  intersections of the full `L012` witness may impose constraints absent from
  an arbitrary ear. No such forcing statement is yet proved.
- Computational evidence: none added in this session.
- Imported facts: no new external theorem. The exact scope of `C008` was
  rechecked and recorded more precisely.

## Failed routes and why

- Saturation plus `C008` does not give a density contradiction: `C008` gives an
  upper bound on the average degree of a counterexample, while no matching
  saturation lower bound was obtained.
- A Mersenne witness for the endpoints of a two-edge path does not directly
  close a forbidden cycle. If it avoids the middle vertex, the resulting cycle
  has length \(2^k+1\); if it contains the middle vertex, its two segments can
  avoid all Mersenne lengths.
- On a shortest triangle there is no internal nonedge, and on a shortest
  \(5\)-cycle every distance-two pair already has the complementary 3-edge
  path. These cases do not produce a *certified* external ear from the first
  saturation test, although `L013` supplies an arbitrary ear.
- The one-ear theta approach was falsified by `L014`; shortest-odd-cycle
  minimality and the three theta lengths alone are insufficient.
- Salvage: the full Mersenne witness in `L012`, including all its intersections
  with the shortest odd cycle, contains information discarded by `L014`.

## Adversarial check

- Checked that every power-of-two cycle newly present after adding a missing
  edge must contain that edge; otherwise it would already occur in the
  saturated graph.
- Kept edge-maximality separate from `L002`'s edge minimality. The
  minimum-order addendum in `L008` was limited to subgraphs omitting vertices
  and was not upgraded to the spanning-subgraph conclusion in `C004`.
- In `L009`, split the bipartite and non-bipartite cases for the graph from
  `C009`; used connectedness of the canonical double cover only in the latter
  case, and checked that covering projection does not decrease girth.
- In `L010`, checked the case where the witness passes through the middle
  vertex: one segment has positive even length and, with its incident edge,
  gives a genuine simple odd cycle.
- Checked that a cycle lies in one block, so `L010` really excludes a
  nontrivial bipartite block rather than only bipartite components.
- In `L011`, restricted internal saturation to endpoints different from the
  possible cut vertex; this is exactly the range in which a simple path cannot
  leave and re-enter the leaf block.
- In `L012`, verified that a shortest odd cycle is induced, that endpoints can
  be chosen away from the one exceptional vertex, and that the triangle and
  \(5\)-cycle cases are not silently included.
- Checked whether the short-cycle ear cases were genuinely open; 2-connectivity
  resolves ear existence directly, leading to `L013`.
- Built the exact infinite theta family in `L014` and limited its logical scope:
  its internal vertices have degree \(2\), so it refutes the one-ear length
  implication but is not a counterexample to `L011`.
- No claim was made that one ear, an odd cycle, or numerical proximity to a
  power of two forces the desired cycle.

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

- Current frontier: `L008`–`L012` replace the falsified local route with a
  global saturation condition, preserve it inside the 2-connected reduction,
  and place an external ear inside a full Mersenne witness when the shortest
  odd cycle has length at least \(7\). `L013` covers ear existence in the short
  cases, while `L014` rules out arbitrary one-ear length equations.
- Remaining blockers: `G002`, `G003`, `G007`, and the new `G008`; witness
  intersections and theta length equations are uncontrolled.
- Recalibration decision: continued. The route passed the `L007` stress test
  and produced more than non-bipartiteness. The one-ear simplification was
  retired, but the full witness retains untested global information.
- Best live alternative or reframing: adapt the variable-length
  path/adjuster mechanism behind `C008` directly to the block in `L001`.
- Pivot trigger: if both the one-component and two-component full-witness
  patterns admit unconstrained infinite power-free length families, saturation
  alone loses comparative advantage.
- Best next action: classify the `L012` Mersenne witness when its vertices
  outside the shortest odd cycle form exactly one component, retaining the
  total length and every cycle intersection; either force a power-of-two cycle
  or exhibit an infinite surviving length family.
- Files a new session should read: `STATE.md`, `CLAIMS.md`, `OBLIGATIONS.md`,
  `A005`, `A004`, the source audit, and this session.

## Plain-language recap

We found a global property that every hypothetical counterexample can be made
to satisfy. Add edges as long as doing so remains safe. At the stopping point,
every still-missing edge has a certificate: its endpoints are already joined
by a path whose length is one less than a power of two, because adding the
missing edge would close a forbidden cycle. This property rules out the
bipartite large-girth examples that defeated the previous local strategy.

The certificates also force odd cycles to be spread throughout the graph and
remain usable inside the crucial 2-connected piece. Every shortest odd cycle
has an extra path leaving and returning to it, and when the cycle has at least
seven vertices one such path lies inside a special certificate. We also found
an important limitation: the three cycle lengths made by one arbitrary extra
path can avoid powers of two in infinitely many ways. The next analysis must
therefore keep the whole certificate and all the places where it meets the
cycle. No power-of-two cycle has yet been forced, so the conjecture remains
open.

## Proposed next step

Classify the `L012` Mersenne witness when its vertices outside the shortest odd
cycle form exactly one component, retaining the total length and every cycle
intersection; either force a power-of-two cycle or exhibit an infinite
surviving length family. The one-ear simplification is already disproved by
`L014`; the high-average-degree variable-path method remains the deferred
alternative.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 1%
- Previous estimate, if any: 1%
- Reason for change: no change. The session found a genuine global reduction
  and isolated the full witness as the relevant object, but also disproved the
  first one-ear simplification.
- Basis: saturation is now the most concrete route and passed the mandatory
  large-girth test. Its strongest obstacle is the uncontrolled intersection
  pattern of a full Mersenne witness; the famous low-degree case remains
  essentially intact.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
