# Current state

- Last updated: 2026-07-24 (S018; order-16 block data from the concurrent S017)
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

## Imported frontier

- `C004`–`C009`, `C012`–`C014`, `C017`, `C024`–`C026` unchanged; the
  min-degree-3 literature frontier remains Bondy–Vince strength.

## Program status

`G013` has three live objects.

(a) The **tight 1-atom question** — does a power-free graph exist whose
unique sub-cubic vertex has degree exactly 2? Rewritten in S018: the
unrestricted version is conjecture-complete (`L036`) and is retired as a
target; the tight version is what `A012` T4 consumes, is strictly weaker
as far as anything proved shows, and is route R1 of `G015`. Empty
through order 15 (`C027`); no bipartite tight 1-atom through order 22
(`C034`).

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
power-free member at any order \(\le22\)** (\(\le23\) with a pendant),
with every member of the class carrying a \(C_8\) and the minimum
\(C_8\) count never dropping below 13 — so the \(C_{16}\) test is never
even decisive, and this channel is *further* from a witness than the
pinched one (whose equality blocks are blocked by 3–7 \(C_8\)s). What
survives in (c): channel (ii), the odd-prime-gcd channel — not
bipartite-forced, no structure theorem, no reduction, no dedicated
search — plus the missing parity analogue of `L032`'s 2-connected block
extraction. Two by-products of the same run: no bipartite counterexample
and no bipartite **tight** 1-atom at orders \(\le22\), verified
internally.

## Open obligations

- `G015` (**new, the proof-side deliverable**): prove the cubic
  reduction unconditionally, by R1 (no tight 1-atom) or R2 (Carr
  \(4/7\to1\)).
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

"0.1 holds iff it holds for cubic graphs." Two independent, non-circular
routes:

- **R1** — prove no *tight* 1-atom exists (unique sub-cubic vertex, of
  degree exactly 2); `L029` then gives the reduction. Empty through
  order 15 (`C027`), and bipartite-empty through 22 (`C034`).
- **R2** — strengthen the imported density bound `C006` (\(\ge4/7\) of a
  minimal counterexample is cubic) to 1. Bypasses the atom formalism
  entirely; ingredients on hand are `C005` and `A012` T4's unconditional
  branch (every degree-\(\ge4\) vertex of a minimal counterexample has a
  degree-3 neighbour). Verifying Carr's argument is a prerequisite.

This is the highest-value *reachable* target in the dossier: a theorem
about the conjecture rather than about our own gadget formalism, and it
would make Thread C's searches decisive instead of conditional.

### Tier 2 — restricted-class theorems worth having on their own

- **Bipartite EGC** (Thread E): every bipartite \(\delta\ge3\) graph has
  a power-of-two cycle. `L035` fixes the class (girth \(\ge6\)
  bipartite), `C034` gives an internally verified base through order 22,
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

- Order-23 bipartite hunt (`E015`; order 22 completed during S018 — 178,549 in class, all with a \(C_8\); 23 is splits \((11,12)\), \((10,13)\) and costs a few hours at the order-22 rate of 47 min).
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

A pencil-type band-4 taut core at order 17+; a strict block or
\(C_8\)-free equality block (disproof protocol); **any** power-free
member of the `E015` class at order 23+ (immediate disproof, `L035` T3);
a `G014` audit overturning an assumed bound; a proof of either `G015`
route (then Thread C becomes the whole game).

### Process correction (S018)

Sixteen audits in a row selected the route with the cheapest decisive
computation. That criterion is what buried `G015` and what kept a
conjecture-complete object on the live list for six sessions. From now
on, a session's strategy audit must name the tier its selected route
serves, and must justify any Tier 3 selection as *background*, not as
the session's work.

## Human-level state

The programme's disproof engine chains copies of a small two-terminal
"engine" into a ring; the proof side hoped that ruling out every kind of
engine would reduce the conjecture to 3-regular graphs. S018 audited that
architecture at the user's prompting — why had sixteen sessions kept
deferring the "single defect" object? — and found the answer is
mathematical, not psychological. A "single defect" graph is a power-free
graph with exactly one vertex of too-low degree. If a counterexample to
the conjecture exists, you can hang one extra dangling vertex on it and
you have a single-defect graph; conversely a single-defect graph can be
assembled into a counterexample. So the two questions are the *same
question*, and every session that deferred it was, without saying so,
declining to prove the conjecture that afternoon. The dossier had been
listing it as a sub-problem with special proof-side value.

The repair is small and the payoff is a clearer map. The recorded
reduction survives if the defect vertex is required to have degree
exactly two — that stricter version is a genuine, strictly smaller
question, and it is exactly what the original proof of the reduction
actually used. With that fixed, the honest proof-side prize of the whole
programme becomes a single named theorem: **the conjecture holds in
general if and only if it holds for 3-regular graphs.** That is now a
target with two independent routes, one internal and one strengthening a
published density result, and it is the first thing in this dossier that
would be a theorem *about the conjecture* rather than about our own
machinery. Everything else was retiered around it: the searches stay
running but can no longer be a session's main work.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 4%
- Previous estimate: 4% (S016)
- Reason for no change: S018 changed the map, not the terrain. Removing
  a conjecture-complete object from the live list and naming the cubic
  reduction as the real deliverable makes the remaining work honest and
  better targeted, but it also makes explicit that six sessions of
  assembly-interface work had a smaller ceiling than recorded. Those two
  effects roughly cancel. The estimate stays where it is because nothing
  proved this session moved the conjecture itself, and because the one
  target that is genuinely reachable — the cubic reduction — is a
  reduction, not a resolution.

## Resume reading

1. `STATEMENT.md`
2. the **Roadmap** section above, then `A018` (1-atom completeness, the
   `L029` repair, and why `G015` is the deliverable)
3. `A017` (the parity structure theorem and the bipartite criterion) and
   `E015/README.md` (the hunt, the verification tables)
3. `A016` + `references/external-agent-strategy-memo-2026-07-24.md`
   (the channel widening this builds on)
4. `A015` (the pencil package `L033`, the endgame, the cascade data)
5. `A014` for the block frame; `E013/README.md` for the pinched
   catalogue
6. `CLAIMS.md` rows `L031`–`L035`, `C030`–`C034`; `OBLIGATIONS.md`
   `G013`/`G014`; `sessions/S016-…md`
