# S003 — Falsify the induced-P13 and cubic-domination forcing route

- Date: 2026-07-23
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: internal reductions `L001`–`L006`; imported
  cubic domination and density `C004`–`C006`; imported induced-\(P_{13}\)
  theorem `C007`
- Open obligations in scope: `G003`, global cycle forcing; `G006`,
  induced-\(P_{13}\) attachment classification
- Session goal: determine whether the imported induced-path and cubic
  conclusions can force a \(16\)-cycle after \(C_4\) and \(C_8\) are excluded
- Falsifiable next move: seek a complete cubic graph with an induced
  \(P_{13}\), all recorded minimality conclusions, and no
  \(C_4,C_8,C_{16}\)

## Work performed

- Opened `A004` and observed that `C004`–`C006` impose no additional
  restriction on a connected cubic graph:
  - every proper nonempty subgraph loses an incident edge at some vertex and
    therefore has a vertex of degree at most \(2\);
  - every vertex has a cubic neighbor;
  - all vertices are cubic.
- Built `E003`, an exact backtracker for the smallest 18-vertex cubic family
  consisting of an induced \(P_{13}\) and five independent outside hubs.
- Exhausted that family. Every branch creates a \(4\)- or \(8\)-cycle before
  completion; there is no survivor in this narrow family.
- Inspected Biggs (1998), especially Theorem 3.2 and its proof. Imported as
  `C009` the existence, for every \(g\ge3\), of a finite Hamiltonian cubic
  graph of girth at least \(g\).
- Applied `C009` with \(g=17\) to prove `A004/L007`: the resulting connected
  cubic graph has no \(C_4,C_8,C_{16}\), satisfies all conclusions of `L002`
  and `C004`–`C006`, and contains an induced \(P_{13}\).
- Repaired stale claim-number references in the existing source audit before
  adding the Biggs source.

## Results

- Imported `C009` at the exact strength used: finite Hamiltonian cubic graphs
  exist with arbitrarily large girth.
- Proved `L007`: the recorded minimality conclusions, cubic domination and
  density, induced \(P_{13}\), and absence of \(C_4,C_8\) do not force
  \(C_{16}\).
- Resolved `G006` by refuting the proposed route, not by proving the main
  conjecture.
- Added `G007`: a replacement route must use a genuinely global restriction
  that is not shared by arbitrary connected cubic graphs of girth at least
  \(17\).
- Recorded `C010` as tested finite evidence: the 18-vertex independent-hub
  completion family has no \(C_4,C_8\)-free member.
- No proof or disproof candidate for `C001` exists.

## Failed routes and why

- The decisive failure is not a rare attachment pattern. Cubic domination can
  be witnessed entirely along the path, and every connected cubic graph
  already satisfies the imported minimality conclusions.
- Large-girth cubic graphs turn that observation into a complete obstruction:
  the whole structural bundle can hold while \(C_4,C_8,C_{16}\) are all
  absent.
- Assuming absence of every longer power-of-two cycle would reintroduce the
  full counterexample hypothesis, so it is not yet a noncircular repair.
- `E003` remains useful only as a sharply delimited finite exclusion.

## Adversarial check

- Checked the exact quantifiers of `C004`–`C007`; no claim was strengthened to
  say that a cubic witness must lie outside the induced path.
- Verified the proper-subgraph assertion separately when a proper subgraph
  omits an edge and when it omits vertices.
- Used the Hamiltonian conclusion of the inspected Biggs construction, not an
  unproved assumption that an arbitrary cubic graph has a long path.
- Checked that a chord of thirteen consecutive Hamiltonian-cycle vertices
  would create a cycle of length at most \(13\), contradicting girth at least
  \(17\).
- Explicitly retained the possibility of \(C_{32},C_{64},\ldots\); `L007` is
  not represented as a counterexample to `C001`.
- Added cycle-detector self-tests to `E003` and audited why lexicographically
  sorting the five outside-neighbor triples removes only vertex-label
  symmetry.
- Re-ran the exact search after adding the self-tests.

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

- Current frontier: `L007` closes the proposed local \(C_{16}\)-forcing route
  by a full large-girth cubic obstruction; the main claim remains open.
- Remaining blockers: `G002` and `G003`, the global forcing step; `G004`,
  original-source completion; `G007`, a nonlocal replacement mechanism.
- Best next action: derive a consequence of minimality or of the absence of all
  power-of-two cycles that fails on the girth-\(17\) cubic family without
  assuming the desired conclusion, then use it in a variable-length
  path/ear argument.
- Files a new session should read: `STATE.md`, `CLAIMS.md`, `OBLIGATIONS.md`,
  `A004`, `E003/README.md`, `references/source-audit-2026-07-23.md`, and this
  session.

## Plain-language recap

We tested the most promising proposed route at its weakest point and found a
decisive obstruction. The known facts say that a hypothetical smallest
counterexample is mostly degree three and contains a long path with no
shortcuts. But ordinary degree-three graphs with no cycles shorter than
seventeen already have all of those properties, and they have no cycles of
length \(4\), \(8\), or \(16\). So classifying the immediate connections around
one long path cannot, by itself, force a \(16\)-cycle. A small exact search also
ruled out the tightest 18-vertex version of that picture, but the general
failure comes from the large-girth construction. This does not settle the
conjecture; it tells us that the next successful idea must use information
spread across the graph and must control longer power-of-two lengths.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 1%
- Previous estimate, if any: 2%
- Reason for change: the induced-\(P_{13}\)/cubic-domination route was the only
  concrete scalable attack, and `L007` shows that its proposed local forcing
  step is false
- Basis: the session removed a misleading direction and produced a reusable
  stress test, but no replacement global mechanism is known; the remaining
  cubic case contains the central difficulty of the open conjecture.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
