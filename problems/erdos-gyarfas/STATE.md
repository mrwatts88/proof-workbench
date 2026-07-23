# Current state

- Last updated: 2026-07-23
- Problem: `P-002` — Erdős–Gyárfás Conjecture

## Exact target

Every finite simple undirected graph of minimum degree at least \(3\) contains a
cycle whose length is a power of two. See normalized `STATEMENT.md` version 0.1.

## Established

- `L001`–`L006`: block and edge-minimal reductions, a longest-path chord
  restriction, and independent proofs that every counterexample has at least
  eleven vertices.
- `L007`: the retired local bundle — cubic domination, cubic density,
  minimality, an induced \(P_{13}\), no \(C_4,C_8\) — does not force
  \(C_{16}\).
- `L008`: a hypothetical counterexample can be enlarged on its fixed vertex
  set until every nonedge has a simple witness path of length \(2^k-1\); the
  result is connected, non-bipartite, and uniformly sparse.
- `L009`–`L011`: the saturation condition fails on bipartite cubic large-girth
  graphs; edges outside odd cycles form a matching; the witnesses persist
  inside a non-bipartite 2-connected leaf block away from its possible cut
  vertex.
- `L012`–`L013`: every shortest odd cycle in that block has an external ear,
  certified inside a Mersenne witness when the cycle has length at least
  \(7\).
- `L014`–`L016`: separations. One arbitrary ear, a full one-excursion
  witness in every attachment configuration, and a full two-excursion witness
  pattern all admit infinite power-free length families. Bounded
  single-witness data cannot force a power-of-two cycle.

## Evidence, not proof

- `E001`–`E003` provide exact finite checks only. The order-\(11\) lower bound
  has separate hand proofs.
- Sparsity heuristic (intuition only): powers of two are exponentially
  sparse, so any bounded witness diagram with a free segment length admits
  power-free solutions. A decisive mechanism must couple unboundedly many
  witnesses or generate an interval of even cycle lengths.

## Imported frontier

- `C004`–`C006` (Carr, 2026): minimality, cubic domination, and cubic density
  in an order-then-size minimal counterexample.
- `C007` (Hegde–Sandeep–Shashank, 2025): every counterexample contains an
  induced \(P_{13}\).
- `C008` (Liu–Montgomery, 2023): large average degree forces a power-of-two
  cycle.
- `C009` (Biggs, 1998): finite Hamiltonian cubic graphs of arbitrarily large
  girth exist.
- The May 2026 primary preprint inspected in `S002` reports the general
  conjecture open.

## Open obligations

- `G002`, `G003`: make the 2-connected reduction and a global cycle-length
  mechanism decisive.
- `G004`: inspect the original 1997 article body for reported computational
  bounds.
- `G007`: make the saturation restriction decisive; by `L015`–`L016` this
  requires unbounded witness coupling or an interval of even cycle lengths.
- `G009`: settle the order-\(11\) saturated-counterexample search.

## Active risks

- The saturated search must be exhaustive with an auditable completeness
  argument, or it proves nothing; witness checking is per-nonedge exact
  path-length search, not heuristics.
- At order \(11\), saturation legitimately uses witness lengths \(3\) and
  \(7\) only, and power cycles \(C_4,C_8\) only; both restrictions must be
  derived in the experiment record, not assumed.
- The minimum-order addendum of `L008` applies at order \(11\) only because
  `L006` excludes all smaller counterexamples; keep that dependency explicit.
- Survivors of the search would be near-miss structures, not counterexamples;
  they must not be upgraded informally.

## Strategy portfolio

- Primary route: `G009`, the exhaustive order-\(11\) saturated search — the
  point of maximal bite of `L008`, decisive either way at that order.
- Live alternative: the variable-length path/adjuster reframing behind
  `C008`, now sharpened by the sparsity heuristic: the needed output is an
  interval of even cycle lengths at minimum degree \(3\); unbounded
  multi-witness coupling is the second sharpened form.
- Pivot trigger: if the order-\(11\) search proves computationally intractable
  after honest optimization, or if orders \(11\)–\(13\) all clear without any
  structural insight accumulating, promote the variable-length reframing to
  primary.

## Best next action

Run an exhaustive order-\(11\) search for saturated counterexamples: graphs
with minimum degree at least \(3\), no \(C_4\) or \(C_8\), and a simple path
of length \(3\) or \(7\) across every nonedge; either prove none exists,
lifting every counterexample's order to at least \(12\), or record the
survivors.

## Human-level state

The previous session found that in a maximally filled hypothetical
counterexample, every missing edge is certified by a path whose length is one
less than a power of two. This session tested whether one such certificate,
kept in full — its exact length and every place it meets a shortest odd
cycle — must create a forbidden cycle. The answer is no, definitively: in
every geometric arrangement, and even with two detours instead of one, there
are infinitely many ways to satisfy all the constraints while avoiding every
power of two. The deep reason is that powers of two thin out so fast that any
bounded diagram of certificates has enough slack to dodge them.

The positive discovery is that on small graphs the certificates have almost no
slack: with at most fifteen vertices, every certificate must have length
exactly three or seven. So the next step is a complete computer search at
eleven vertices, the smallest order not already excluded. Either no such
maximally filled counterexample exists there — which would push the smallest
possible counterexample to twelve vertices by a proved reduction — or the
search exhibits revealing near-miss structures.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 1%
- Previous estimate: 1%
- Reason for no change: the session removed an entire class of candidate
  mechanisms (bounded witness patterns) and opened a tractable finite
  frontier, but the asymptotic forcing mechanism the conjecture needs is
  still missing; the negative and positive information roughly balance.

## Resume reading

1. `STATEMENT.md`
2. `CLAIMS.md`
3. `OBLIGATIONS.md`
4. `attempts/A005-edge-maximal-power-cycle-saturation.md`
5. `references/source-audit-2026-07-23.md`
6. `sessions/S005-2026-07-23-classify-full-one-excursion-witnesses-and-recalibrate-the-sa.md`
