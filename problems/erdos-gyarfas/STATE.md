# Current state

- Last updated: 2026-07-24 (S015)
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
  power-free vertex-taut 2-connected **core** (non-terminal degrees
  \(\ge3\), terminal degrees \(\ge2\)) with \(s_{\max}\le2\,s_{\min}\)
  exists (the block question).
- **New (S015): `L033`, the band-4 pencil dichotomy.** In any graph
  with \(d(x,y)=4\): the (2,2)-vertices are exactly the 4-path middles
  (product structure per middle), and either two internally disjoint
  4-paths exist — equivalently a \(C_8\) **through both terminals** —
  or all 4-paths share one internal vertex. No \(C_4\)-freeness needed.
  Under \(C_4\)-freeness the pencil vertex is unique and adjacent to a
  terminal (a middle pencil forces a unique 4-path), the fan is rigid
  (strands biject with middles, unique exits, no cross chords, forced
  hexagons), and both terminal neighborhoods split near/far (T3).
- **New (S015, external memo audited in `A016`): `L034`, the
  generalized ring criterion.** A power-free (D)-gadget disproves 0.1
  whenever **some** \(L\)-fold sumset of \(S\) avoids the powers of two
  — a direct corollary of `L025`'s ring lemma that D-A3's pinch never
  exhausted. New channels: all-odd \(S\) with \(L\) odd (bipartite
  instance: terminals in opposite parts), odd-prime gcd, and
  \(S\subseteq2+4\mathbb{Z}\); fatal shapes invisible to the pinched
  frame: \(S=\{3,7\}\), \(S=\{2,6\}\). Necessary conditions for 0.1
  now include an even through-path in every power-free (D)-gadget.
  The "pinch = the criterion" glosses are retracted (framing error;
  every proved row stands). Program ceiling explicit: assembly closure
  + 1-atoms yields the cubic reduction, not 0.1 itself.

## Imported frontier

- `C004`–`C009`, `C012`–`C014`, `C017`, `C024`–`C026` unchanged; the
  min-degree-3 literature frontier remains Bondy–Vince strength.

## Program status

`G013` has three live objects. (a) The **1-atom question** (unchanged;
the only sub-question with direct proof-side yield — the ceiling).
(b′) The **block question** (pinched channel); after `L033` its band-4
case is exactly the **pencil endgame**: prove no vertex-taut
2-connected \(C_4\)-free core with \(d(x,y)=4\), \(s_{\max}\le8\) has a
pencilled 4-path system — success closes band 4 in the strengthened
form "\(C_8\) through both terminals" (no \(C_{16}\) caveat at any
order). Catalogue (`C030`–`C032`): through order 15 the block world is
exactly five equality blocks (P10 = Petersen\(-e\) band 4, A11/B11/C12
band 5, D14 band 6); no strict block; the strict-15 scan found exactly
one taut pinched pair = D14's pendant lift (the predicted unique band-7
witness); closed hits occupy bands 4–7 only; the band-4 closed world is
three objects, only P10 a core, disjoint-type. Order 16 is the first
order where a hit could be \(C_8\)-free (`C027` ends at 15); an
order-16 closed scan was launched in S015 and was still running at
session close — its harvest is reserved for a short dedicated
follow-up session and is deliberately not part of `C032`. Hypothesis necessity (`C033`):
with \(C_4\)s allowed, strict blocks exist from order 6
(\(K_{3,3}-e\)), strict band-4 blocks with \(S=\{4,5,6,7\}\) at order
8, and \(C_8\)-free band-4 equality cores at order 9 — \(C_4\)-freeness
is essential to both band-4 rungs. Against the endgame, three hand
constructions died to a forced \(C_8\), a forced 9-path, and forced
\(C_4\)s (the cascade obstruction, `A015`); the (3,3)–(4,4) deep
territory is the untested escape. The band-2 closed rung
(\(S\subseteq\{2,3,4\}\), \(4\in S\)) is the last \(C_4\)-only gap
below band 4. (c) **The congruence channels** (`L034`, new): power-free
(D)-gadgets with all-odd \(S\) (bipartite instance: terminals in
opposite parts, girth \(\ge6\), no \(C_8/C_{16}\)), odd-prime gcd, or
\(S\subseteq2+4\mathbb{Z}\) — any hit disproves 0.1 by an odd ring.
Empty through order 15 (`C027` is profile-agnostic; through 18 for
degree-\(\ge3\) terminal pairs), but the taut shape data was never
scanned (banded scanners cannot see \(S=\{3,7\}\)); the all-odd ladder
lives at odd bands 3, 5, 7 only — disjoint from the band-4 pencil
battlefield; no pendant/block reduction theory exists for it yet
(pendant shifts flip parity). Conditional on the unverified \(\ge32\)
bipartite import (`G014`), bipartite gadgets of order \(\le31\) must
carry a Mersenne through-length (3, 7, or 15).

## Open obligations

- `G013` (core, refined twice in S015): 1-atoms; the block question —
  band 4 = the pencil endgame, bands \(\ge5\) open; the congruence
  channels (parity/gcd/mod-4), shape-unscanned.
- `G014` (new): source-audit the external memo's literature and census
  leads before any of them supports a step.
- `G002`, `G003`, `G007`: the global mechanism; `G007` routes through
  `G013`'s conditional transfer.
- `G004`: only the original 1997 Erdős article body remains uninspected.

## Strategy portfolio

Standing instruction (user, S015): **all threads stay documented and
live**; sessions select by strategy audit, retire only on evidence.

- Thread A (pinched channel, proof side): the **pencil endgame**, fan
  case first — it owns the proved structure (hexagons, no cross chords,
  the \(N(c)\) inventory, far/near splits) and the cascade pressure
  points; then the unique-path case. Sub-thread: the band-2 closed rung
  as an `L030`-style warm-up; band-5 equality analogue thereafter.
- Thread B (congruence channels, disproof side, from the audited memo):
  (B1) odd-\(S\) calibration scan over the existing stream at orders
  \(\le15\) (new scan mode: abort on any even through-path — the
  parity analogue of the equality-block shape catalogue); (B2)
  bipartite gadget hunt at orders 16–24 (genbg; terminals in opposite
  parts, girth \(\ge6\), no \(C_8/C_{16}\); conditional Mersenne
  window \(S\ni3,7,15\)); any power-free hit disproves 0.1 by a 3-ring.
- Thread C (cubic frontier, disproof side): reproduce Markström 26/28,
  then order 30, where any \(\{C_4,C_8,C_{16}\}\)-free cubic graph is a
  counterexample outright; `L029` makes cubic decisive modulo 1-atoms.
  Requires the dedicated \(\{C_4,C_8\}\)-free generator (`G014` item 6)
  rather than geng filtering.
- Thread D (census mining, disproof side): power-length tests over
  existing cubic vertex-transitive / girth-\(\ge9\) / snark / cage
  lists (imports gated by `G014`); the girth-\(\ge9\) lists reduce to
  pure \(C_{16}/C_{32}\) questions.
- Thread E (proof side, new theorems): bipartite EGC ("min degree 3
  bipartite forces \(C_4/C_8/C_{16}\)" — closes Thread B's channel if
  true; the `L030`/`L033` collapse machinery plus parity leverage);
  Carr 4/7 → 1 (cubic reduction without the 1-atom detour);
  3-connectivity structure (2-cut chain decomposition; the mod-\(m\)
  spectrum-confinement exclusion sketch in `A016` M10).
- Thread F (infrastructure): 1-atom structure theory; order-17+ legs;
  the \(\{C_4,C_8\}\)-free generator build.
- Pivot triggers: a pencil-type band-4 taut core at order 16+ (kills
  the endgame as stated); a strict block or \(C_8\)-free equality
  block (disproof protocol); an all-odd taut core found by B1
  (re-weights the whole portfolio toward the parity channel); any
  `G014` audit overturning an assumed bound.

## Human-level state

The disproof strategy builds counterexamples by chaining copies of a
two-terminal "engine" into a ring, where the ring's cycle lengths are
sums of the engine's path lengths. Until now the program only hunted
engines whose path lengths squeeze inside a factor-of-two window (the
sums then dodge the powers of two by landing between consecutive
powers). An external review, audited and confirmed this session,
pointed out the sums can dodge the powers by *arithmetic* instead: if
all path lengths are odd, sums of an odd number of them are odd —
never a power of two — and similar tricks work with common factors.
So there are several parallel hunting grounds, not one. Everything
proved so far stands (the factor-of-two hunt was genuinely closed
through 15 vertices, and this session's bottleneck theorem still
governs its smallest open case), and the searches already done
incidentally show the new grounds are also empty through 15 vertices.
But the new grounds were never mapped structurally, they need their
own theory, and one of them (odd path lengths, realized by bipartite
engines) comes with cheap decisive searches. Also made explicit: even
total success on the engine program would "only" reduce the conjecture
to 3-regular graphs — the full proof needs more. The portfolio now
carries both the old threads (the bottleneck fight, the 16-vertex
harvest) and six new ones (the parity hunt, extending a 2004 census of
3-regular graphs to 30 vertices where a hit is instantly a
counterexample, mining existing graph censuses, a bipartite version of
the conjecture as a new theorem target, tightening a 2026 result that
4/7 of a minimal counterexample is 3-regular, and unused
3-connectivity leverage), per the user's instruction that no thread be
dropped.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 4%
- Previous estimate: 3% (S014)
- Reason for change: the assembly disproof interface widened — the
  audited external memo exposed parity/congruence ring channels the
  pinched frame could not see, several with cheap decisive searches
  (bipartite gadgets at orders 16–31, the cubic census at order 30
  where any hit is a counterexample outright), and the proof side
  gained two frontier-adjacent targets (bipartite EGC, Carr 4/7 → 1).
  Small increase only: every new channel is still empty through order
  15, the new literature imports are unverified, the ceiling
  correction cuts the proof-side yield of the engine program, and the
  1-atom question remains untouched.

## Resume reading

1. `STATEMENT.md`
2. `A016` (the memo audit: `L034`, channels, ceiling, corrections) and
   `references/external-agent-strategy-memo-2026-07-24.md`
3. `A015` (the pencil package `L033`, the endgame, the cascade data)
4. `E014/README.md`, `E013/README.md` (order-15/16 extension)
5. `A014` for the block frame; `A013`/`A012`/`A011` background
6. `CLAIMS.md` rows `L031`–`L034`, `C030`–`C033`; `OBLIGATIONS.md`
   `G013`/`G014`; `sessions/S015-…md`
