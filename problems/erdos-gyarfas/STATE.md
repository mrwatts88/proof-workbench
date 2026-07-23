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
- `G004`: inspect the original 1997 article body for reported bounds.
- `G007`: make the saturation restriction decisive; requires unbounded
  witness coupling or an interval of even cycle lengths.
- `G010`: extend the exhaustive search through orders \(14\)–\(15\), the
  rest of the small-order collapse range.

## Active risks

- `L017` is computer-assisted; its exhaustiveness rests on the coverage
  arguments in `A006` and the five validation anchors in `E004`, not on an
  independent hand proof as with `L005`–`L006`.
- Order \(13\) already cost \(44{,}397{,}061\) nodes in one process; order
  \(14\) will likely need intra-sequence parallel decomposition or a
  compiled port, and any such change must re-run the validation anchors.
- At order \(16\) the collapse ends: \(C_{16}\) and witness length \(15\)
  enter, and the searched class stops being the counterexample class.
- Survivors at order \(14\) or \(15\) would be actual counterexamples;
  treat any survivor first as a probable bug and verify independently.

## Strategy portfolio

- Primary route: `G010`, the finite frontier through order \(15\), one
  exhaustive order at a time with the validated `E004` tooling.
- Live alternative: the variable-length/adjuster reframing — an interval of
  even cycle lengths at minimum degree \(3\) — with unbounded multi-witness
  coupling as its second form; both target the asymptotic mechanism `G007`.
- Pivot trigger: if order \(14\) is intractable after honest optimization,
  or when order \(15\) closes the collapse range, shift primary effort to
  the asymptotic mechanism; also pivot immediately to survivor analysis if
  any survivor is verified.

## Best next action

Extend the exhaustive \(\{C_4,C_8\}\)-free search to order \(14\), adding
parallel decomposition across degree sequences and subtrees and re-running
the validation anchors after the change; either prove the class empty,
lifting every counterexample's order to at least fifteen, or record and
independently verify the first survivors.

## Human-level state

Two sessions ago the project found that a hypothetical minimal counterexample
can be maximally filled with edges so that every missing edge carries an
exact-length certificate path. Last session showed one certificate can never
force the forbidden cycle. This session turned to brute force where brute
force is exact: for graphs with at most fifteen vertices, being a
counterexample just means having every vertex with three neighbors while
avoiding cycles of length four and eight, a finitely checkable condition. A
new exhaustive program — validated against two earlier independent
computations, an exact symmetry identity, and a positive control — proved
that no such graph exists with eleven, twelve, or thirteen vertices. So any
counterexample needs at least fourteen vertices. The searches stayed cheap
because avoiding both cycle lengths at once is extremely restrictive;
fourteen and fifteen vertices are the natural continuation, after which
cycle length sixteen becomes possible and the simple equivalence ends.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 1%
- Previous estimate: 1%
- Reason for no change: the finite frontier advanced two orders with a
  reusable validated tool, but finite exclusions cannot settle the universal
  statement, and the missing asymptotic mechanism is unchanged.

## Resume reading

1. `STATEMENT.md`
2. `CLAIMS.md`
3. `OBLIGATIONS.md`
4. `attempts/A006-saturated-finite-frontier-at-order-eleven.md`
5. `experiments/E004-order-11-saturated-search/README.md`
6. `sessions/S006-2026-07-23-exhaustive-order-11-saturated-counterexample-search.md`
