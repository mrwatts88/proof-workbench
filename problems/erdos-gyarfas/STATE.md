# Current state

- Last updated: 2026-07-24 (S020 — the order-16 \(\mathcal G\)-profile
  scan ran to completion and came back empty; the mod-4 congruence
  hunt died on its own pre-registered kill test)
- Problem: `P-002` — Erdős–Gyárfás Conjecture

## Exact target

Every finite simple undirected graph of minimum degree at least \(3\) contains a
cycle whose length is a power of two. See normalized `STATEMENT.md` version 0.1.

## Established

- `L001`–`L006`: block and edge-minimal reductions; counterexamples have
  \(\ge11\) vertices (hand proofs).
- `L008`–`L016` saturation package with delimitations.
- `L017`/`L018`/`L022` finite exclusions: every counterexample has at
  least **nineteen** vertices; extremal \(\{C_4,C_8\}\)-free window
  \([19,24]\); census capped at order 18.
- `L019`–`L024` the voltage-lift program, closed as a theorem
  (collision wall, reviewed `R001`).
- `L025`–`L030`: atom reduction; rung completeness; lobe decomposition;
  taut rungs \(s_{\min}\le3\) closed \(C_4\)-only; cubic reduction
  modulo 1-atoms.
- `L031`–`L032`: the pendant/block reduction — taut 2-atoms exist iff a
  power-free vertex-taut 2-connected **core** with \(s_{\max}\le2s_{\min}\)
  exists (the block question).
- `L033`: the band-4 pencil dichotomy. With \(d(x,y)=4\), either two
  internally disjoint 4-paths exist (equivalently a \(C_8\) through both
  terminals) or all 4-paths share one internal vertex; no
  \(C_4\)-freeness needed, and under it the pencil is terminal-adjacent
  with a rigid fan.
- `L034`: the generalized ring criterion — a power-free (D)-gadget
  disproves 0.1 whenever **some** \(L\)-fold sumset of \(S\) avoids the
  powers of two (pinch, all-odd, odd-prime gcd, mod-4 channels).
- **New (S016): `L035`, the parity structure theorem and the bipartite
  assembly criterion.** For a vertex-taut two-terminal graph,
  parity-constancy of the through-set is **equivalent** to
  bipartiteness (all-odd = terminals in opposite colour classes). Hence
  (T3) **any** connected bipartite power-free graph with at most two
  sub-cubic vertices disproves 0.1 — no path enumeration, no tautness
  test, no external import — and (T4) bipartite generation is an
  exhaustive instrument for `L034` channels (i) and (iii), modulo the
  standing 1-atom relativization. Not valid for channel (ii): the theta
  graph \(\Theta(3,3,3)\) is vertex-taut, non-bipartite, \(S=\{3\}\).

- **New (S018): `L036`, 1-atom completeness.** A 1-atom in the recorded
  sense (unique sub-cubic vertex, of degree 1 **or** 2) exists iff a
  counterexample exists — attach one pendant vertex to a counterexample.
  So the unrestricted 1-atom question is *conjecture-complete*, `L029`'s
  "cubic reduction modulo 1-atoms" is vacuous as originally stated and
  is restated with **tight** 1-atoms (exceptional degree exactly 2),
  and `A012` Remark T4.1 is withdrawn as unproved.
- **New (S020): `C036`/`C037` — `L041`'s decisive order is empty and
  the congruence route is closed.** The order-16 \(\mathcal G\)-profile
  scan (`E018`): 346,573,602 stream graphs (24-part split, sum
  reproduced by an independent unsplit `geng -u`), 29,713,305 in the
  profile class, **every one blocked by a \(C_8\)** (\(C_{16}\) never
  decisive), zero power-free — so \(\mathcal G\) has no order-16
  member and **every tight 1-atom has order \(\ge18\)** (`C036` with
  `L041`). Proximity datum: the minimum \(C_8\) count over the class
  is **1** (the bipartite class never went below 13). The mod-4
  companion (`A021`, instrument `E018/mod4.py`): the residual object's
  forced-membership profile is *realized* by vertex-taut \(C_4\)-free
  cores from order 10 — one order-10 witness **is Petersen\(-e\)**
  (labelg-verified) — with both admissible residue patterns and no
  invariant (`C037`), and the chain-calculus identity caps
  congruence information at parity (`A021` T1: the
  \(2|E(P)\cap E(Q)|\) leak). **No congruence-type theorem at any
  modulus can exclude case (5b) from the forced hypotheses alone**;
  the surviving proof-side levers are the chain-cancellation tension
  (Minkowski-additive) and mechanisms that make power-freeness itself
  fight (the band-4 pencil is the model — it is exactly the constraint
  Petersen\(-e\) violates). Petersen\(-e\) is the standing calibration
  object: any proposed case-(5b) exclusion must fail on it unless it
  invokes power-freeness or minimality.
- **New (S019): `L037`–`L042`, both `G015` routes advanced in one
  orchestrated parallel run.** R2 side (`L037`/`L038`): the
  **subdivision descent** — the link graph on the degree-\(\ge4\) set of
  a minimal counterexample is power-free (cycles lift doubled) and, by
  order-minimality, 2-degenerate — gives \(3|V_3|\ge2n+3\), strictly
  past Carr's \(4/7\); the 15-vertex certificate S15 (`E017`) shows
  \(2/3\) is the exact ceiling of the non-power hypotheses, so the
  constant route to `G015` is **closed**, with the descent as the
  reusable residue. R1 side (`L039`–`L042`): the closure calculus and
  the (3,3) **bijection** onto the congruence class \(\mathcal G\)
  (through-set avoids \(\{2,6,14,\dots\}\); no \(s_{\max}\) window);
  the **engine + peel** (any counterexample below the minimum atom
  order \(n_0\) yields a *cubic* counterexample — the repair of the
  withdrawn T4.1); the five-case analysis at the defect vertex:
  **the conditional cubic reduction holds modulo excluding case (5b)**
  (defect non-cut, both neighbours cubic, residue vertex-taut), every
  tight 1-atom has order \(\ge17\), and the case-(5b) residual object
  is 2-connected, degree-\(\ge4\)-independent, **non-bipartite** (hand
  proof at every order), with forced power/Mersenne memberships and
  chain cancellation. `C004`–`C006` are upgraded to **verified**
  (line-by-line audit of arXiv:2605.22844v1). The two routes meet: a
  one-defect subgraph of the link graph is exactly a tight 1-atom.

## Imported frontier

- `C004`–`C006` now carried at **verified** strength (S019 line-by-line
  audit and internal reconstruction,
  `references/carr-2026-verification-2026-07-24.md`); `C006` superseded
  internally by `L038`. `C007`–`C009`, `C012`–`C014`, `C017`,
  `C024`–`C026` unchanged; the min-degree-3 literature frontier remains
  Bondy–Vince strength.

## Program status

`G013` has three live objects.

(a) The **tight 1-atom question** — does a power-free graph exist whose
unique sub-cubic vertex has degree exactly 2? Rewritten in S018 (the
unrestricted version is conjecture-complete, `L036`) and **structured in
S019**: every tight 1-atom has order \(\ge17\) (`L041`); a minimum-order
one with both defect-neighbours cubic corresponds bijectively to the
congruence class \(\mathcal G\) (`L039`), and under (R) the *only*
surviving configuration is case (5b) — that closure with a vertex-taut
residue, now heavily constrained (`L042`: 2-connected, non-bipartite,
degree-\(\ge4\)-independent, forced through-set arithmetic, chain
cancellation, band-4 pencil). For `G015` the conditional form suffices
and only case (5b) remains. Empty through order 15 stream-level
(`C027`) **and through order 16 for the exact \(\mathcal G\) profile
(`C036`, S020)** — every tight 1-atom has order \(\ge18\), every
\(\mathcal G\)-member \(\ge17\); no bipartite tight 1-atom through
order 23 (`C034`). The congruence-obstruction leg against the residual
object is retired (`C037`/`A021`); its proof side now rests on the
chain-cancellation tension and on power-freeness-active mechanisms,
its search side on order 17, where the `G014` item-6 generator is the
right instrument (the \(C_8\) filter has been 100% decisive at every
order ever scanned in this profile).

(b′) The **block question** (pinched channel); after `L033` its band-4
case is exactly the **pencil endgame** — prove no vertex-taut
2-connected \(C_4\)-free core with \(d(x,y)=4\), \(s_{\max}\le8\) has a
pencilled 4-path system. Catalogue now through order **16**
(`C030`–`C032`, `C035`/S017): **eight equality blocks** — P10 =
Petersen\(-e\) (band 4), A11/B11/C12 (band 5), D14 (band 6), and from
the order-16 harvest F16 (band 4, terminal degrees (3,3), on a graph
with no sub-cubic vertex), G16 (band 4, (2,4)), H16 (band 6, (2,2),
first block with \(C_{16}\) in spectrum) — every one at exact equality
\(s_{\max}=2\,s_{\min}\); **no strict taut pinched pair exists at
order 16 at all** (strict catalogue complete at seven witnesses
through 16), no power-free closed taut pair at 16, and all three
band-4 core gadgets are disjoint-type, so the pencil endgame's
exhaustive empty base and the 100% two-through-path interference
census both extend through order 16. Hypothesis necessity (`C033`):
\(C_4\)-freeness is essential to both band-4 rungs. Three hand
constructions died to the cascade obstruction (`A015`).

(c) The **congruence channels**, now **split by `L035`**. Channels (i)
(all-odd \(S\)) and (iii) (\(S\subseteq2+4\mathbb Z\)) *are* the
bipartite class, and `E015`/`C034` searched it exhaustively: **no
power-free member at any order \(\le23\)** (\(\le24\) with a pendant),
with every member of the class carrying a \(C_8\) and the minimum
\(C_8\) count never dropping below 13 — so the \(C_{16}\) test is never
even decisive, and this channel is *further* from a witness than the
pinched one (whose equality blocks are blocked by 3–7 \(C_8\)s). What
survives in (c): channel (ii), the odd-prime-gcd channel — not
bipartite-forced, no structure theorem, no reduction, no dedicated
search — plus the missing parity analogue of `L032`'s 2-connected block
extraction. Two by-products of the same run: no bipartite counterexample
and no bipartite **tight** 1-atom at orders \(\le23\), verified
internally.

## Open obligations

- `G015` (**the proof-side deliverable; reduced in S019 to one
  configuration**): exclude case (5b) — no minimum-order tight 1-atom
  is the 2-path closure of a vertex-taut \(\mathcal G\)-member — and
  the cubic reduction follows (`L040`/`L041` supply every other case).
  The constant-density route is closed (`L038` delimitation); the
  order-16 scan is done and empty (`C036`) and the congruence hunt is
  dead (`C037`/`A021`). Live moves: the chain-cancellation tension
  (`L042` W1-T14), the disjoint long-link descent (`A020` W2-T8(c)),
  and the order-17 search rung via the `G014` item-6 generator.
- `G013` (core): tight 1-atoms; the block question (band 4 = pencil
  endgame, bands \(\ge5\) open); the odd-prime-gcd channel and the
  missing parity block-extraction.
- `G014`: source-audit the external memo's literature and census leads.
  Item (2) (bipartite \(\ge32\)) is **de-gated** — `L035` T3 removes the
  need for the Mersenne-window logic and `C034` verifies the range
  internally; items (1), (3)–(6) still gate their threads.
- `G002`, `G003`, `G007`: the global mechanism; `G007` routes through
  `G013`'s conditional transfer.
- `G004`: only the original 1997 Erdős article body remains uninspected.

## Roadmap (S018)

Standing instruction (user, S015): **all threads stay documented and
live**; sessions select by strategy audit, retire only on evidence. S018
adds a second instruction (user): weigh routes by what they would
*deliver* — the full conjecture first, a significant delimited result
second — and keep cheap legs running alongside rather than instead.

The tiers below replace the flat thread list. Threads A–F are all still
here; what changed is that each now says which tier it serves, and no
thread may be selected as a session's primary work on cheapness alone.

**Why the restructure.** Sessions 11–16 all worked inside the assembly
interface, whose proof-side best case is the *cubic reduction*, not 0.1
(`A016` M6). S018 then found that one of that interface's two halves —
the 1-atom question — is conjecture-complete (`L036`), so the recorded
"ceiling" was in fact circular. The dossier's real proof-side
deliverable is `G015`, and it had never been named as a target.

### Tier 0 — settle statement 0.1 (the mission)

No cheap move exists here, and none should be pretended. Two sub-cases:

- **A forcing mechanism at \(\delta\ge3\)** (`G003`, `G007`). The
  literature frontier is Bondy–Vince strength (two cycles differing by 1
  or 2); nothing forces a *specific* length. Every internal theorem so
  far (`L030`, `L033`, `L035`) has run on \(C_4\)-freeness or parity, and
  the power spectrum has never once had to fight — that is the diagnostic
  to keep watching.
- **A counterexample.** Best ticket: cubic, order \(\ge30\) (Thread C),
  because `C013` stops at 28 and `L029` concentrates the risk there.

### Tier 1 — the named deliverable: the cubic reduction (`G015`)

"0.1 holds iff it holds for cubic graphs." **S019 ran both routes in
parallel (audited worker subagents) and the target is now a single
configuration:**

- **R1, reframed to the conditional form** — "a tight 1-atom yields a
  cubic counterexample", which is all the reduction needs (`L040`); the
  unconditional "no tight 1-atom exists" is retired as an R1 target
  (unreachable by minimality: its reducts are counterexamples, not
  atoms). By `L041` the conditional form is proved **except in case
  (5b)**; excluding that case closes `G015`. S020 spent the first two
  recorded moves: the order-16 scan is **empty** (atom bound now
  \(\ge18\), `C036`) and the congruence obstruction is **dead at every
  modulus** (`C037`/`A021` — the forced hypotheses are realized from
  order 10, so they admit no refutation; parity is the ceiling of
  chain-calculus congruence information). Live moves against case
  (5b), in order: (i) the **chain-cancellation tension** (`L042`
  W1-T14): \(S=S_1+S_2\) across any cut of \(H\), each side forced to
  carry a forbidden length while the Minkowski sum avoids
  \(\mathbb P-2\) — quantify the cancellation; first falsifiable
  target: bound the block-chain length or force 2-connectivity of
  \(H\); sanity-check every candidate argument against Petersen\(-e\);
  (ii) the **order-17 \(\mathcal G\) rung** — decisive the same way 16
  was, but the stream is \(\sim\!17\times\) larger
  (\(\sim\!6\times10^9\)), so build the `G014` item-6
  \(\{C_4,C_8\}\)-free generator first (the \(C_8\) filter is 100%
  decisive in this profile at every order ever scanned; min \(C_8\)
  count at 16 is 1, so incremental \(C_8\) rejection prunes nearly
  everything); (iii) the disjoint long-link descent (below), where the
  routes meet.
- **R2, constant route closed** — `C004`–`C006` verified and the bound
  improved to \(3|V_3|\ge2n+3\) (`L037`/`L038`), but S15 certifies
  \(2/3\) as the exact ceiling of the non-power hypotheses and no
  constant \(<1\) delivers the reduction. Surviving extension: the
  internally-disjoint longer-link descent (`A020` W2-T8(c)). The
  descent itself is the reusable mechanism, and the routes meet on the
  link graph (a one-defect subgraph of it is a tight 1-atom).

This remains the highest-value *reachable* target in the dossier: a
theorem about the conjecture rather than about our own gadget
formalism, and it would make Thread C's searches decisive instead of
conditional.

### Tier 2 — restricted-class theorems worth having on their own

- **Bipartite EGC** (Thread E): every bipartite \(\delta\ge3\) graph has
  a power-of-two cycle. `L035` fixes the class (girth \(\ge6\)
  bipartite), `C034` gives an internally verified base through order 23,
  and the naive "\(C_8\) always" form is *false* at large order
  (bipartite double covers of `C009`'s large-girth cubic graphs), so any
  proof must be order-bounded or consume \(C_{16}/C_{32}\). Reported
  externally only as a computation to 31 — a proof would be new.
- **The path-spectrum spread theorem** (Thread B3): under (D), is
  \(\gcd(S)\) always a power of 2? New genre — the literature's mod-\(k\)
  results are about cycle spectra, not two-terminal path spectra. The
  3-connected *cycle* analogue is a four-line Menger argument (`A016`
  M10) and is the proved cousin to start from; \(\Theta(3,3,3)\) shows
  the degree condition, not parity, must do the work.

### Tier 3 — cheap legs: run them, never *select* them

Harvest-only. None of these may be a session's primary work.

- Bipartite hunt (`E015`): **order 23 completed empty in the S019
  follow-up harvest** (PyPy 7.3.23, anchors re-passed first; 928,562
  in class from 260.8M generated in 5,240s, every member with both a
  \(C_8\) and a \(C_{16}\), minimum \(C_8\) count 19; no bipartite
  tight 1-atom, no bipartite counterexample). The class is now clean
  through order 23 (24 with a pendant). Next leg: order 24 — roughly
  \(4\times\) the cost — after which genbg stops being the right
  instrument and the Tier 4 generator is the move.
- The gcd scan over the existing order-\(\le16\) stream (needs path
  enumeration; the bipartite shortcut does not apply).
- Order-17+ legs of the pinched catalogue (Thread A/F).
- Census mining (Thread D), gated by `G014`.

### Tier 4 — infrastructure with cross-thread leverage

- The dedicated \(\{C_4,C_8\}\)-free generator (`G014` item 6): unlocks
  cubic order 30 (Tier 0) *and* bipartite order 31 (Tier 2) at once.
  This is the one build worth doing before more searching.
- `G014` source audits for the imports that gate Tiers 1–3 (Carr's
  argument for R2; census provenance for Thread D).

### Demoted and retired

- **Retired as a target:** the unrestricted 1-atom question
  (conjecture-complete, `L036`). It stays in the record as a
  completeness fact, not as work.
- **Demoted to Tier 3:** the pinched-channel rung ladder, including the
  pencil endgame (Thread A). It is real mathematics and stays live, but
  its best case is one channel of a ceiling-limited interface, so it no
  longer merits primary selection over Tier 1.

### Pivot triggers

A hit in a \(\mathcal G\)-profile scan at order 17+ satisfying the
\(S\)-condition (**immediate disproof** — a tight 1-atom; the order-16
trigger was consumed empty in S020, and the mod-4 kill condition fired
there too, so case (5b)'s proof side now rests on chain cancellation
and power-freeness-active mechanisms); a pencil-type band-4 taut core
at order 17+; a strict block or \(C_8\)-free equality block (disproof
protocol); **any** power-free member of the `E015` class at order 24+
(immediate disproof, `L035` T3); a `G014` audit overturning an assumed
bound; a chain-cancellation theorem bounding the block chain (would
concentrate case (5b) on 2-connected \(H\)); exclusion of case (5b)
(then `G015` is proved and Thread C becomes the whole game).

### Process correction (S018)

Sixteen audits in a row selected the route with the cheapest decisive
computation. That criterion is what buried `G015` and what kept a
conjecture-complete object on the live list for six sessions. From now
on, a session's strategy audit must name the tier its selected route
serves, and must justify any Tier 3 selection as *background*, not as
the session's work.

## Human-level state

The programme's proof-side prize is one named theorem: **the conjecture
holds in general if and only if it holds for 3-regular graphs.** S019
attacked it down both of its routes at once — the first orchestrated
parallel session, one worker per route, everything audited before being
believed — and both routes moved.

The published-density route first: a 2026 paper of Carr proves that in
a smallest possible counterexample, at least 4/7 of the vertices have
degree exactly 3. We verified that paper line by line (it holds up),
then pushed the bound: at least two-thirds, plus a little more. The
push needed a genuinely new trick — the degree-3 vertices wedged
between two high-degree vertices act like markers on invisible edges,
and those invisible edges form their own smaller graph which inherits
the no-power-of-two property with all lengths halved; because the
original graph was the *smallest* offender, the smaller shadow graph
must be sparse. But the same session also proved this route can go no
further: an explicit 15-vertex example meets every hypothesis the
counting uses at exactly two-thirds density, and no percentage short of
100% ever delivers the reduction. So that route ends — honourably, with
a stronger theorem than the literature has and a reusable mechanism.

The internal route is now where the game is. The "single defect" graph
question (one vertex of degree 2, everything else degree 3 or more, no
power-of-two cycle) was analysed at its defect vertex, and of the five
possible local shapes, four are now impossible or lead exactly where we
want: a smaller offender, which a repaired argument converts into a
**3-regular** counterexample — which is the reduction succeeding, not
failing. One shape survives: the defect vertex sits on a triangle-free
"lens" whose two anchor points are both degree 3, with every vertex on
some anchor-to-anchor path. That single surviving configuration now
carries the whole theorem, and it is already known to be at least
17 vertices, two-connected, never two-colourable, and arithmetically
squeezed (its path lengths must hit some exact powers of two and miss
others).

S020 played both of the moves that analysis recommended, and both came
back with definitive answers. The exhaustive size-16 search ran to
completion — thirty million graphs with the right degree pattern, out
of a stream of 346 million — and every single one contains a cycle of
length 8. So the dangerous object cannot exist on 16 + 1 = 17 vertices,
and the "single defect" graph is now known to need at least 18. The
striking detail: some of those thirty million graphs contain exactly
*one* cycle of length 8 — the class comes within a single cycle of
disproving the conjecture, which is precisely why this channel deserves
its dedicated search machinery (a generator that never builds the
8-cycles in the first place) before the next, seventeen-times-larger
order is attempted. The other move — hunting a "remainder modulo 4"
argument to kill the dangerous configuration by pure arithmetic, the
way a parity argument killed its two-colourable version — is dead, and
provably so: the graph obtained by deleting one edge from the famous
Petersen graph satisfies *every* arithmetic condition the dangerous
configuration is forced to satisfy, so no arithmetic of remainders can
ever rule the configuration out. What separates Petersen-minus-an-edge
from an actual counterexample is one concrete cycle of length 8, and
that is the kind of structure — actual cycles interfering with each
other, not remainders — that the surviving proof route (the
"cancellation across links of a chain" tension) has to exploit.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 5%
- Previous estimate: 5% (S019)
- Reason for no change: the session was decisively informative but
  symmetric. Against: one of case (5b)'s two named proof levers (the
  congruence obstruction) is now provably dead — not stalled, dead at
  every modulus — and the decisive search order returned empty, so the
  disproof did not happen. For: the atom bound moved up an order with
  full coverage verified two ways; the kill test produced the
  calibration object (Petersen\(-e\)) that will keep future proof
  attempts honest at essentially zero cost; the min-\(C_8\)=1 datum
  shows this channel is the closest any class in the dossier has come
  to a witness, sharpening the case for the Tier 4 generator; and the
  chain-cancellation lever survived the kill untouched. The programme
  knows strictly more and its reachable deliverable (`G015`) is
  unchanged in difficulty: fewer routes, but the dead one was cheap to
  test and the survivor was always the harder, more structural one.

## Resume reading

1. `STATEMENT.md`
2. the **Roadmap** section above, then `A019` (the case analysis, the
   engine/peel, the residual object — R1's full state) and `A021` (the
   congruence kill: the chain-calculus ceiling, the Petersen\(-e\)
   calibration object, what survives)
3. `A020` (the descent, the density theorem, the sharpness tombstone —
   R2's state) and
   `references/carr-2026-verification-2026-07-24.md` (what
   `C004`–`C006` now rest on)
4. `A018` (1-atom completeness, the `L029` repair, why `G015` is the
   deliverable)
5. `CLAIMS.md` rows `L039`–`L042`, `C036`/`C037`; `OBLIGATIONS.md`
   `G015`/`G013`
6. `E018/README.md` (the order-16 scan, its anchors, and the mod-4
   probe data); `E015/README.md` for the bipartite hunt (order 23
   harvested empty; next leg 24 or the generator)
7. `sessions/S020-…md` (this session) and `S019-…md` (the
   orchestration record behind `L037`–`L042`)
