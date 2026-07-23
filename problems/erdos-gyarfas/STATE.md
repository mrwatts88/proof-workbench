# Current state

- Last updated: 2026-07-23
- Problem: `P-002` — Erdős–Gyárfás Conjecture

## Exact target

Every finite simple undirected graph of minimum degree at least \(3\) contains a
cycle whose length is a power of two. See normalized `STATEMENT.md` version 0.1.

## Established

- `L001`–`L006`: block and edge-minimal reductions, a longest-path chord
  restriction, and hand proofs that every counterexample has at least eleven
  vertices.
- `L007`: the retired local bundle does not force \(C_{16}\).
- `L008`–`L013`: the saturation reduction — Mersenne witnesses across every
  nonedge — with its parity separation, odd-cycle matching structure,
  leaf-block persistence, and external ears of shortest odd cycles.
- `L014`–`L016`: separations. One arbitrary ear, a full one-excursion
  witness in every configuration, and a full two-excursion pattern all admit
  infinite power-free families; bounded single-witness data cannot force.
- `L017` (computer-assisted): every counterexample has at least fourteen
  vertices. At orders \(11\)–\(13\) no minimum-degree-\(3\) graph avoids
  both \(C_4\) and \(C_8\) at all, by the exhaustive validated search
  `E004`; at orders \(\le15\) such a graph would be exactly a
  counterexample, so the exclusion needed neither `L008` nor saturation.

## Evidence, not proof

- `E001`–`E003` are exact finite checks; `E004` is exhaustive per order and
  carries `L017` as its proved consequence (`C011` records the computation).
- Sparsity heuristic (intuition only): bounded witness diagrams always admit
  power-free solutions; a decisive mechanism must couple unboundedly many
  witnesses or generate an interval of even cycle lengths.

## Imported frontier

- `C004`–`C006` (Carr, 2026): minimality, cubic domination, cubic density.
- `C007` (Hegde–Sandeep–Shashank, 2025): induced \(P_{13}\) in every
  counterexample.
- `C008` (Liu–Montgomery, 2023): large average degree forces a power-of-two
  cycle.
- `C009` (Biggs, 1998): finite Hamiltonian cubic graphs of arbitrarily large
  girth.
- Reported prior computations exceed the internal orders; the literature
  also exhibits cubic graphs on \(24\) vertices with no \(C_4\) or \(C_8\)
  (but with \(C_{16}\)), so the internal \(\{C_4,C_8\}\)-free frontier ends
  somewhere in \([14,24]\).

## Open obligations

- `G002`, `G003`: make the 2-connected reduction and a global cycle-length
  mechanism decisive.
- `G004` (priority): pin down the published computational and structural
  frontier from primary sources and import it at full verified strength.
- `G007`: make the saturation restriction decisive; requires unbounded
  witness coupling or an interval of even cycle lengths.
- `G011` (priority): settle whether edge-maximal saturation (`L008`) is new
  to the literature; it is the project's candidate novel asset.

## Active risks

- `L017` is computer-assisted; its exhaustiveness rests on the coverage
  arguments in `A006` and the five validation anchors in `E004`, not on an
  independent hand proof as with `L005`–`L006`.
- Import correspondence: a miscopied hypothesis or overread bound from the
  literature would silently corrupt the route; exact statements and sources
  are mandatory.
- A missed source in the `G011` novelty sweep would waste effort on a known
  result; the sweep must be recorded with the databases and queries used, and
  repeated skeptically before any novelty-based investment.
- The mission is new information: work that only re-derives reported results
  must be recognized and stopped at route-selection time.

## Strategy portfolio

- Primary route: the frontier sweep `G004` + `G011` — import the strongest
  verified bounds, obtain and internally verify the reported \(24\)-vertex
  \(\{C_4,C_8\}\)-free cubic graphs, and determine whether the saturation
  reduction `L008`–`L016` is already known. If it is new, strengthen the
  saturation line toward a publishable partial result past the frontier.
- Live alternative: the variable-length/adjuster reframing — an interval of
  even cycle lengths at minimum degree \(3\) — with unbounded multi-witness
  coupling as its second form; both target the asymptotic mechanism `G007`,
  and both would use the imported extremal graphs as test cases.
- Pivot trigger: if the sweep finds saturation already published in a form
  subsuming `L008`–`L016`, import it, take what is strongest, and promote
  the interval reframing to primary.

## Best next action

Run the frontier sweep from primary sources: import the strongest verified
finite bounds with exact statements; obtain the reported \(24\)-vertex
\(\{C_4,C_8\}\)-free cubic graphs and verify their properties internally
with the `E004` detectors; and search the literature deliberately for any
appearance of edge-maximal power-cycle saturation, recording the queries.
The sweep either establishes the saturation line as new — making it the
frontier-passing target — or upgrades the dossier with the published form.

## Human-level state

The mission has been clarified by the user: settle open conjectures by
standing on everything already known and spending effort only past the
published frontier. Under that lens the project's position is this. The
internal work proved solid but mostly non-novel results — structural
reductions and a verified bound that any counterexample needs at least
fourteen vertices, below what the literature already reports. The one idea
not found in any audited source is the saturation certificate: a
hypothetical counterexample can be maximally filled with edges so that
every missing edge carries a path certificate of exact length one less
than a power of two, a condition with proved consequences and proved
limits. The immediate task is a deliberate literature check: if this idea
is genuinely absent, it is the project's beachhead past the frontier and
the work becomes strengthening it into a publishable new partial result;
if it is known, the strongest published form gets imported and the effort
moves to the harder mechanism question with imported extremal graphs as
test material.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 1%
- Previous estimate: 1%
- Reason for no change: the finite frontier advanced three orders with a
  reusable validated tool, but finite exclusions cannot settle the universal
  statement, and the missing asymptotic mechanism is unchanged. This estimate
  was set at the S006 research close; the O008 mission realignment changes
  route selection, not the mathematical outlook.

## Resume reading

1. `STATEMENT.md`
2. `CLAIMS.md`
3. `OBLIGATIONS.md`
4. `attempts/A006-saturated-finite-frontier-at-order-eleven.md`
5. `experiments/E004-order-11-saturated-search/README.md`
6. `sessions/S006-2026-07-23-exhaustive-order-11-saturated-counterexample-search.md`
