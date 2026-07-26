# S032 — nine-agent breakthrough sweep: planar δ≥4 theorem, modular-channel closure, three barrier theorems

- Date: 2026-07-26
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1 (unchanged throughout)
- Work / claim status: `active` / `open`
- Strongest established facts: `L047` (every counterexample has ≥22 vertices),
  `L049` (interference-completeness, audited `R002`), `L058` (case-(5b) window
  \(n_0\in[23,41]\)), `L056` (interpolation genre empty).
- Open obligations in scope: `G015` (cubic reduction), `G013` (atom question,
  including channel (ii) — the odd-prime-gcd channel, open with **no structure
  theorem, no reduction and no dedicated search** since S016), `G003`/`G007`.
- Inherited next action: close `A028` T8's two gaps in the non-Hamiltonian
  stratum, using `L055`'s positive-savings engine.
- Session goal (user directive): a genuine breakthrough on statement 0.1 —
  proof, disproof, or a breakthrough reduction. Framework constraints explicitly
  relaxed where they would hinder that. Orchestration permitted; Opus floor.
- Falsifiable next move: nine independent attacks on 0.1 itself, each with a
  stated deliverable and kill condition.

## Strategy audit

- **Why the inherited route might work:** `L055` removes the zero-savings
  obstruction, and closing `A028` T8's two gaps would make the case-(5b)
  window's interior fully decided.
- **Fastest way to falsify it:** none needed — it was already falsified as a
  route to 0.1. **`S030` proved the (F) programme cannot prove `G015`** (`L046`
  supplies 2-connectivity only below order 36), and `G015` is itself only a
  *reduction* of 0.1. The inherited action's best case is therefore a delimited
  sub-result of a sub-result with a proved ceiling.
- **Mechanistically distinct alternative:** aim every leg at 0.1 directly —
  new proved classes, a counterexample construction, and (decisively) attempts
  to prove that whole *genres* of argument cannot work.
- **Selected route and reason:** the latter, on expected research value. A final
  session spent one rung further inside a programme with a proved ceiling has
  near-zero chance of adding information the community lacks.
- **Pivot criterion:** none needed; the session was structured as nine parallel
  legs, so a dead leg costs one leg, not the session.

**Retrospective vindication:** `L059` proves that the genre the entire (F)
programme belongs to is *incapable* of proving 0.1. The audit that the inherited
route deserved had never been run at genre level.

## Work performed

Nine delegated `opus` workers, each given a self-contained brief and **no access
to the dossier narrative** (isolation from inherited framing); the orchestrator
independently re-verified every load-bearing computation with its own code.

| leg | verdict |
|---|---|
| literature frontier | frontier mapped; three novelty verdicts; one orchestrator claim refuted as known |
| restricted classes | **new theorem: 0.1 for planar \(\delta\ge4\)** (`L060`, `L061`) |
| closure calculus | **`L059` subdivision barrier**; exact truncation spectrum theorem |
| minimality surgeries | still running at close — **excluded from every ledger row** |
| large girth | **`L063` girth does not localize**; (G1) reframed as Conjecture SF |
| odd-gcd channel | **`L064` modular channel closed** — `G013`(c) resolved |
| Hamiltonian stratum | structure theorem; \(n\le42\) verified; depth exactly 4 |
| counterexample hunt | none found; Exoo frontier imported; substitution barrier measured |
| adversarial audit | **`L062` lift-safety barrier**; orchestrator's own two lemmas ruled **vacuous** |

Orchestrator-side verification, all with independently written code:
`L060` exhaustive over all 143,038 connected \(C_4\)-free graphs at orders
5–11 (0 violations, 1,366 non-vacuous instances at order 11); `L061`'s planar
case exhaustive over the \(\{C_4,C_8\}\)-free \(\delta\ge2\) planar class at
orders 4–11 (0 violations, max \(m-2n=-7\) against the bound \(-4\)); the
\(K_5\)/\(K_{3,3}\) mod-4 check (\(4^{10}+4^{9}\) weightings, 0 exceptions);
`L064`'s conclusion over all cubic \(F\) and all edges \(ab\), orders 4–16
(97,440 pairs — the only mod-3 hits have \(|S|=1\)); the truncated Petersen
decoy test for the vacuity finding.

## Results

### Proved (new)

- **`L059` — subdivision barrier.** For any class \(\mathcal C\) closed under
  subdivision and any \(S\) with \(S\cap t\mathbb N=\emptyset\) for some
  \(t\ge2\), "\(G\in\mathcal C\Rightarrow L(G)\cap S\ne\emptyset\)" is false:
  \(L(G^{(t)})=t\,L(G)\). With \(S=\mathbb P\), \(t=3\): **no
  subdivision-closed hypothesis implies 0.1's conclusion.** Every law of the
  through-set / ear / theta / exchange / interference family is
  subdivision-covariant, so **no conjunction of them can prove 0.1** — this
  includes the whole (F) programme and `L048`–`L052`. Smallest defeater:
  \(K_4^{(3)}\), 16 vertices, \(L=\{9,12\}\), power-free, satisfying every
  recorded closure law. `L049` is unaffected as a theorem; what is delimited is
  what it can be used *for*.
- **`L060` — the triangle-detour lemma.** In a \(C_4\)-free graph, a 5-cycle
  with three edges in triangles forces a \(C_8\). (Apexes are off the cycle and
  pairwise distinct by \(C_4\)-freeness; \(5-3+6=8\).) No planarity, no
  connectivity, no degree hypothesis.
- **`L061` — surface density theorem and the planar \(\delta\ge4\) case.**
  Connected, \(\delta\ge2\), \(n\ge4\), \(\{C_4,C_8\}\)-free, 2-cell embedded in
  \(S\) ⟹ \(m\le 2n-2\chi(S)\), by discharging (\(\mu(v)=d(v)-4\),
  \(\mu(f)=\ell(f)-4\), triangles fed \(\tfrac13\) per edge, pentagons unable to
  donate three times by `L060`). Since \(\delta\ge4\) forces \(m\ge2n\) on an
  endblock: **every planar graph with \(\delta\ge4\) contains a cycle of length
  4 or 8**; likewise projective-planar; likewise 2-connected toroidal /
  Klein-bottle (there \(\chi=0\), the bound is tight, and the case rests on a
  separate equality analysis — the weakest point of the package).
  By-products: \(\mathrm{ex}_P(n,\{C_4,C_8\})\le2n-4\) (\(2n-5\) if
  2-connected); planar \(\delta\ge4\) \(C_4\)-free forces \(n\ge30\), sharp at
  the icosidodecahedron.
- **`L062` — lift-safety barrier.** \(\mathbb P\) is closed under doubling but
  has no additive self-similarity, so an order-reducing reduction yields a
  contradiction **only** if it is length-preserving (\(H\subseteq G\), already
  Markström/Carr) or length-multiplying by a power of two (2-group quotient).
  Every additive surgery returns "\(G\) has a cycle of length \(2^k+c\)", which
  is consistent with power-freeness; six were worked out explicitly (edge
  contraction, identification, \(Y\to\Delta\), triangle contraction, path
  contraction, delete-and-suppress) and all six are vacuous.
- **`L063` — girth does not localize.** For every \(g\) and \(M\) there is a
  connected cubic graph of girth exactly \(g\) with \(L(G)\cap[g+1,M]=\emptyset\)
  (attach a \(g\)-cycle to a girth-\(>M\) cubic graph through \(g\) subdivision
  vertices pairwise at distance \(\ge M\)); explicit 768-vertex witness, girth 6,
  nothing of length 7–11. Kills every argument anchored at a shortest cycle.
- **`L064` — the modular channel is empty (`G013`(c) resolved).** If a
  power-free gadget's through-set lies in a single residue class mod \(m\ge3\),
  then 0.1 is already false via a graph built from a proper subgraph of the
  gadget. Equivalently: if 0.1 holds, \(d(S)=\gcd\{s-s'\}\in\{1,2\}\) for every
  gadget. Route: pendant-branch lemma ⟹ the block tree of a gadget is a path
  with every block matching Fan's hypotheses ⟹ Fan (JCTB 84 (2002);
  Gao–Huo–Liu–Ma Thm 1.2 at \(k=2\)) gives two through-paths differing by 1 or 2.
  This closes the odd-prime-gcd channel **and every modulus**, and it covers the
  strictly larger target "one residue class mod 3 with \(3\mid L\)" (which does
  not require \(3\mid\gcd S\)).
- **`L065` — a minimum-order counterexample is non-bipartite.** Contract an edge
  lying in no triangle; the lift is a \(2^k\)-cycle (contradiction) or a
  \((2^k+1)\)-cycle, which is odd. Not found in the literature.

### Computational evidence

- Hamiltonian stratum: exact structure theorem for \(L(C_n+M)\) (the cycles with
  chord set \(F\) are the two connected alternating gap classes); **every cubic
  Hamiltonian graph with \(n\le42\) has a power cycle with a \(\le4\)-chord
  certificate**, exhaustive up to rotation. Depth 4 is necessary: explicit
  \(n=20,24,28\) matchings with no \(\le3\)-chord power cycle, all with every
  chord span even, so a parity theorem forbids odd-chord families. No shallow
  proof of the Hamiltonian case exists.
- Substitution barrier, measured: every 3-terminal gadget whose own cycles miss
  \(4,8,16\) has \(\rho=(1+t_{\max})/(1+t_{\min})\ge7/3>2\), so the top band of
  the inflated spectrum is forced to contain a power of two. 300 H7-inflations
  over five girth-\(\ge6\) bases: **all** miss exactly \(\{4,8,16\}\), **all**
  contain 32 and 64. Powers still to dodge strictly increase per iteration.
- \(f(k)/2^{k+1}\) = 1.25, 1.5, \(\ge\)1.69 — **widening**; the strongest
  quantitative evidence in the file, pointing toward 0.1 being **true**.
- Leaf-gadget (bridge) census exhaustive to order 23: 22,455,873 graphs, zero
  survivors ⟹ that family needs a gadget of order \(\ge25\). Noted: this family
  is genuinely **not** covered by the standard 2-connectivity reduction, because
  suppressing a degree-2 cut vertex shifts lengths by 1 and \(\mathbb P\) is not
  shift-invariant. Smallest \(\{C_4,C_8\}\)-free \(\delta\ge3\) graph: order
  \(\ge23\).
- New object: a cubic order-98 \(\{C_4,C_8,C_{16}\}\)-free graph (H7-inflation
  of Heawood), triple-verified. Not a record — Exoo's is 78.

### Imported facts (previously missing from this dossier)

- **Exoo, arXiv:1403.5636** — the true state of the art: \(G_{78}\) cubic, no
  \(C_4,C_8,C_{16}\); \(G_{450}\) cubic, no \(C_4,C_8,C_{16},C_{32}\)
  (Tutte–Coxeter with every vertex replaced by a 15-vertex gadget);
  \(G_{420}\) 3-connected cubic **planar**, no \(2^m\) for \(m\le4\).
  \(f(2)=10\), \(f(3)=24\), \(f(4)\in[54,78]\), \(f(5)\le450\); the
  \(f(4)\ge54\) lower bound is unpublished (Markström) and unverified.
  **These are the correct calibration objects for every future lemma**, far
  stronger than the order-24 graphs used until now.
- **Heckman–Krakovski** conclude "a \(2^m\)-cycle, \(2\le m\le7\)", not "4 or 8".
  The truncated icosahedron is 3-connected cubic planar with no \(C_4\) and no
  \(C_8\) (verified here), so the 4-or-8 form is false; Exoo's \(G_{420}\)
  refutes their suggested \(m\le4\), leaving \(5\le m\le7\) open.
- **Liu–Montgomery, JAMS 36 (2023)**: average degree \(\ge d_0\) forces every
  even length in \([\log^8\ell,\ell]\), hence a power of two ⟹ **0.1 is
  entirely a bounded-degree question**.
- **Dean–Lesniak–Saito (1993)**: \(\delta\ge3\) with \(\le2\) degree-2 vertices
  forces a cycle \(\equiv0\bmod4\); and \(\delta\ge3\) forces a cycle
  \(\equiv0\bmod k\) iff \(k\le4\) (\(K_4\) has spectrum \(\{3,4\}\)). The
  mod-\(k\) route is capped permanently.
- **Erdős's own position** (Discrete Math. 165/166 (1997)): "We are convinced now
  that this is false … but we never found a counterexample even for \(r=3\)."
- Markström's exhaustive cubic census reaches \(n\le28\); Royle's \(n\le15\).
  The widely-quoted "17" is folklore. erdosproblems.com #64: open, \$1000, zero
  claimed proofs.

### Refuted en route (orchestrator claim, withdrawn)

"Every non-planar graph has a cycle of length divisible by 4" was derived and
verified here (\(4^{10}\) and \(4^9\) weightings, zero exceptions) and is
**already in print**: Győri–Li–Salia–Tompkins–Varga–Zhu, JCTB 176 (2026),
Lemma 2, same reduction; its cubic corollary is weaker than
Dean–Lesniak–Saito. Withdrawn as a novelty claim; retained as a verified fact.

## Failed routes and why

- **Power-Path Saturation** (orchestrator's own contraction/identification
  lemmas): correct after two repairs — the degree bookkeeping needs
  \(C_4\)-freeness, and the cubic clause as first stated was wrong — but
  **vacuous**. Satisfied by 15/15 edges of the truncated Petersen graph, by all
  four Markström order-24 graphs and all 23 at order 26, and by adversarial
  search designed to break it (2 failures in 1,720 random \(C_4\)-free cubic
  graphs, both at order 14). Explained structurally by `L062` and by the fact
  that "cycle lengths through an edge" is nearly a full interval. Residue:
  `L065`.
- **Lemma C** (2-group covers): correct, and it reproves the known 2-group
  Cayley cases by descent, but selects a measure-zero family (0 of 27
  near-counterexamples, 0 of 900 random cubic graphs at \(n\ge20\) admit a free
  involution with simple quotient).
- **(G1), "large girth forces a power cycle"**: reframed, not proved. `L063`
  shows the girth-anchored form is unprovable; the scale-free replacement is
  Conjecture SF.
- **Bipartite double cover as a proof device**: the orchestrator's cycle
  classification for \(G\times K_2\) was **false** (Desargues has 14, 16, 20,
  which the classification misses). Corrected: the projection is a closed
  non-backtracking walk visiting vertices at most twice with several doubled
  paths. No information flows from the cover back to \(G\).

## Adversarial check

- A dedicated hostile-referee leg was run against the orchestrator's own two
  lemmas, with an explicit instruction not to defend them. It found one
  substantive gap, one false clause, and — via measurement on 27 near-
  counterexamples plus adversarial annealing — the vacuity verdict. It also
  corrected the double-cover claim above.
- Every load-bearing computation from a worker was re-run by the orchestrator
  with independently written code (`L060`, `L061`, `L064`, mod-4, decoy test).
- The one novelty claim that survived internal enthusiasm but not the literature
  (`mod 4`) was withdrawn.
- The `L064` worker corrected the orchestrator's own framing: the ring's junction
  vertices are **not** cut vertices; the cycle classification holds by an
  edge-partition/parity argument instead.

## Canonical records changed

- [ ] `STATEMENT.md` — unchanged (statement 0.1 untouched)
- [x] `STATE.md`
- [x] `CLAIMS.md`
- [x] `OBLIGATIONS.md`
- [ ] `PROOF.md` — no candidate; preliminary-reduction list unchanged
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- **Current frontier:** 0.1 is proved for planar \(\delta\ge4\) (`L061`) and, by
  import, for average degree \(\ge d_0\) (Liu–Montgomery). Counterexample floor
  unchanged at 22 vertices (\(\ge23\) for the \(\{C_4,C_8\}\)-free class);
  cubic floor 30. The real frontier object is Exoo's \(G_{450}\).
- **Remaining blockers:** no technique locates an exact cycle length at
  \(\delta=3\); `L059`, `L062`, `L063` now say *why* three whole genres cannot.
- **Recalibration decision: pivoted, decisively.** The `G015`/case-(5b)/(F)
  programme is retired as a route to 0.1 — not because it is hard, but because
  `L059` proves its genre cannot reach 0.1 even if completed. It may still be
  finished as a delimited result about the cubic reduction; that is a different,
  smaller deliverable and should be labelled as such.
- **Best live alternative:** extend `L061` downward in degree — the discharging
  has real slack, and the target "planar, \(\delta\ge3\), few cubic vertices
  ⟹ \(C_4\), \(C_8\) or \(C_{16}\)" is reachable; the obstruction is the vertex
  type \((3,6,6)\).
- **Pivot trigger:** any lemma that holds on Exoo's \(G_{78}\) or \(G_{450}\) is
  a soundness alarm — those are now the primary calibration objects, ahead of
  Petersen\(-e\) and calibration object #3.
- **Best next action:** see `problem.json`.
- **Files a new session should read:** this record; `L059`–`L065` in `CLAIMS.md`;
  `STATE.md`'s new header.

## Plain-language recap

The conjecture says: if every point of a network has at least three connections,
you can always find a loop whose length is exactly a power of two — 4, 8, 16, 32,
and so on. It has been open since 1994 and carries a \$1000 prize.

This project had spent thirty-one sessions on a *reduction*: an attempt to show
the conjecture only needs checking on the simplest networks, where every point
has exactly three connections. That reduction was never the conjecture itself,
and a previous session had already proved the current machinery could not even
finish the reduction. So this session abandoned it and attacked the conjecture
directly, using nine independent research agents working in parallel on
deliberately different ideas, with every important computation re-checked
independently.

Three things came out. First, a genuinely new theorem: **the conjecture is true
for every flat (planar) network in which each point has at least four
connections** — and in that case the loop can always be taken to have length 4
or 8. A careful literature check found nothing like it; it also yields a new
bound in a separate, active area (planar extremal graph theory) that is stronger
than anything published, including a paper posted nine days ago.

Second, the project's own last untested escape route for *dis*proving the
conjecture — a construction based on making all path lengths agree modulo an odd
number — was closed by a theorem, not by a search. It had been sitting open
since session 16.

Third, and most important, we now know *why* the last thirty-one sessions did
not work, and it is not for want of effort. Three separate proofs show that
entire families of argument are incapable of settling this problem: any argument
that only sees the network's "topological shape" fails, because stretching every
connection into a path of three triples all loop lengths and three never divides
a power of two; any argument that shrinks a smallest counterexample fails,
because powers of two are not preserved by shifting a length by one or two; and
any argument that starts from the shortest loop fails, because a network's
shortest loop tells you nothing about where its other loops are. The dossier's
main machinery falls into the first family.

We also found that the published state of the art was missing from this project
entirely: Exoo has explicit networks that dodge four consecutive powers of two,
far better than anything recorded here, and measuring how his method behaves
shows it gets *harder*, not easier, to dodge the next power — which is the
strongest evidence yet that the conjecture is true, despite Erdős himself having
believed it false.

## Proposed next step

Extend the new planar theorem downward. It currently needs every point to have
at least four connections; the natural next target is flat networks where a
limited number of points have only three. The proof has measurable slack, and
the obstruction is a single identified local configuration. This would establish
the conjecture for a much larger and more natural class, and would fail
visibly — the discharging accounts simply will not balance — if the slack is not
really there.

Deferred alternative: finish the old cubic-reduction programme as a delimited
result. Deferred because a theorem proved this session shows that programme
cannot reach the conjecture, so it is now a smaller deliverable than it looked.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: **7%**
- Previous estimate: 12%
- Reason for change: **down**, and the reason is information, not discouragement.
  Three genres of argument are now *proved* incapable, including the one this
  dossier was built on; the only unconditional general theorem in the area
  (Liu–Montgomery) explicitly does not reach bounded degree; the mod-\(k\) route
  is capped at \(k=4\) permanently; and the best construction method in existence
  gets measurably worse per power. The problem is not close on either side.
- Basis: most promising route — extending `L061`'s discharging to lower degree on
  surfaces, plus Conjecture SF as the scale-free reformulation. Strongest
  obstacle — nothing anywhere forces an *exact* cycle length at \(\delta=3\), and
  `L059`/`L062`/`L063` now show three natural ways of trying cannot. Evidence —
  the widening margin \(f(k)/2^{k+1}\) says a counterexample is unlikely, so the
  answer is probably "true" and probably out of reach.
