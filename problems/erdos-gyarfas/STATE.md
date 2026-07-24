# Current state

- Last updated: 2026-07-24 (S014)
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
- **New (S014): `L031`–`L032`, the pendant/block reduction.** Stripping
  a degree-1 terminal of a taut (D)-gadget is a through-path bijection
  onto a **core** (both terminal degrees \(\ge2\)), shifting \(S\) by
  one and preserving the spectrum; strict pinch upstairs = closed ratio
  \(s_{\max}\le2s_{\min}\) downstairs; every core lifts back. Chains
  decompose at cut vertices into taut blocks (Minkowski through-sets,
  union spectra), and bridge counting extracts: **taut 2-atoms exist
  iff a power-free vertex-taut 2-connected core with
  \(s_{\max}\le2\,s_{\min}\) exists** (the block question). Sharpness:
  two Petersen\(-e\) blocks + a bridge = a strict taut core of order 20,
  so core-level spread-doubling is false and blocks are the right level.

## Imported frontier

- `C004`–`C009`, `C012`–`C014`, `C017`, `C024`–`C026` unchanged; the
  min-degree-3 literature frontier remains Bondy–Vince strength.

## Program status

`G013` has two live objects. (a) The **1-atom question** (unchanged).
(b′) The **block question**: a power-free vertex-taut 2-connected core
with \(s_{\max}\le2\,s_{\min}\) — equivalent to taut 2-atoms (`L032`),
and a witness disproves 0.1 by lift and ring. Exact catalogue through
order 14 (`E013`, `C030`/`C031`): the strict taut world is precisely six
pendant lifts (the five `C028` witnesses plus a new band-5 one at order
11 — the lift of Petersen minus an edge); the block world is precisely
five 2-connected cores, **all at exact equality \(s_{\max}=2s_{\min}\)**:
Petersen\(-e\) (order 10, band 4, \(S=\{4,5,7,8\}\)), A11/B11 (order 11,
band 5), C12 (order 12, band 5), D14 (order 14, band 6, swap-symmetric —
predicting exactly one strict band-7 witness at order 15). No strict
block exists through order 14. Every block is blocked from
power-freeness only by \(C_8\); **every \(C_8\) in the catalogue is the
symmetric difference of two through-paths** (23/23); at band 4 two
internally disjoint 4-paths force \(C_8\) directly. A power-free block
needs order \(\ge16\) (`C027`). Record repair: `C029` certified
\(S\subseteq\{3,4,5\}\) only; the \(s_{\min}\in\{4,5\}\) emptiness
through 14 is established by `C030`, not `C029`.

## Open obligations

- `G013` (core, refined S014): 1-atoms; the block question.
- `G002`, `G003`, `G007`: the global mechanism; `G007` routes through
  `G013`'s conditional transfer.
- `G004`: only the original 1997 Erdős article body remains uninspected.

## Strategy portfolio

- Primary: the **band-4 block rungs**. (i) Strict: prove no vertex-taut
  \(C_4\)-free 2-connected core has \(S\subseteq\{4,5,6,7\}\) (empty
  through order 14; the `L030` collapse machinery plus the new
  terminal-degree-\(\ge2\) leverage). (ii) Equality power: prove every
  vertex-taut \(C_4\)-free 2-connected core with \(S\subseteq\{4,\dots,8\}\)
  contains a \(C_8\) (at orders \(\ge16\): a \(C_8\) or \(C_{16}\)) —
  the first genuinely power-specific rung, guided by Petersen\(-e\); the
  candidate mechanism is the disjoint/intersecting dichotomy on the
  4-path system (disjoint pair \(\Rightarrow C_8\) outright; pairwise
  intersecting systems are rigid under \(C_4\)-freeness).
- Search leg: the order-15 closed catalogue under PyPy (any new block
  extends the lab; a strict block kills (i); a \(C_8\)-free block kills
  (ii) and is disproof material; also tests D14's predicted unique
  order-15 strict witness).
- Second alternative: minimal 1-atom structure theory.
- Deferred: order-16 census.
- Pivot triggers: a strict block found (kills (i), reweights toward
  disproof); a \(C_8\)-free equality block found (disproof protocol:
  check \(C_{16}\), lift, ring); both band-4 rung attacks stalling after
  honest effort (switch to 1-atom theory or the band-5 equality
  analogue).

## Human-level state

The disproof strategy needs a small two-terminal graph avoiding
power-of-two cycles with all its connection paths in a narrow band.
This session dissected every known near-miss and found they share one
anatomy: a one-edge "antenna" glued onto a two-terminal engine whose
path lengths span exactly a factor of two — and one of the four engines
is the Petersen graph minus an edge. Two theorems now make that anatomy
the whole story: the antenna trick is fully reversible, and any
candidate chops at its cut vertices into an engine chain, so the entire
question reduces to single 2-connected engines with path-ratio at most
two. The complete machine catalogue through 14 vertices contains
exactly five engines, all sitting at ratio exactly two, and each is
kept from disproving the conjecture by one thing only: an unavoidable
8-cycle, which in every case arises as the overlay of two
terminal-to-terminal paths. The fight is now exactly this: does every
such engine have to contain an 8-cycle, or does a larger engine dodge
it?

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 3%
- Previous estimate: 2% (S013)
- Reason for change: the taut side of the disproof interface collapsed
  onto a single sharply-searchable object (the block question) with an
  exact small catalogue, an identified extremal structure (Petersen
  minus an edge), and a concrete candidate mechanism for the first
  power-specific rung (two-path interference); this is the first time
  the power fight has both a clean statement and a lab. Still 3%, not
  more: the equality phenomenon and the \(C_8\)-forcing are finite
  observations, the block question is open in both directions past
  order 15, and the 1-atom question remains untouched.

## Resume reading

1. `STATEMENT.md`
2. `A014` (pendant/block reduction `L031`/`L032`, the composite, the
   mechanism data)
3. `E013/README.md` (catalogue, blocks, interference census)
4. `A013`/`A012`/`A011` for the rung/lobe/atom background
5. `CLAIMS.md` rows `L025`–`L032`, `C027`–`C031`; `OBLIGATIONS.md`
   `G013`; `sessions/S014-…md`
