# Current state

- Last updated: 2026-07-24 (S016)
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

## Imported frontier

- `C004`–`C009`, `C012`–`C014`, `C017`, `C024`–`C026` unchanged; the
  min-degree-3 literature frontier remains Bondy–Vince strength.

## Program status

`G013` has three live objects.

(a) The **1-atom question** (unchanged; the only sub-question with
direct proof-side yield — the ceiling). New datum: no *bipartite*
1-atom exists at orders \(\le21\) (`C034`).

(b′) The **block question** (pinched channel); after `L033` its band-4
case is exactly the **pencil endgame** — prove no vertex-taut
2-connected \(C_4\)-free core with \(d(x,y)=4\), \(s_{\max}\le8\) has a
pencilled 4-path system. Catalogue through order 15 (`C032`): five
equality blocks (P10 = Petersen\(-e\) at band 4, A11/B11/C12 band 5,
D14 band 6), no strict block, closed bands 4–7 only. The order-16
closed scan launched in S015 completed and was being harvested
concurrently by a separate agent (session `S017`) while S016 ran; its
results are that session's to record and are deliberately not folded in
here — read `S017` and the `E013` README for the order-16 catalogue
before treating "through order 15" as current. Hypothesis necessity
(`C033`): \(C_4\)-freeness is essential to both band-4 rungs. Three
hand constructions died to the cascade obstruction (`A015`).

(c) The **congruence channels**, now **split by `L035`**. Channels (i)
(all-odd \(S\)) and (iii) (\(S\subseteq2+4\mathbb Z\)) *are* the
bipartite class, and `E015`/`C034` searched it exhaustively: **no
power-free member at any order \(\le21\)** (\(\le22\) with a pendant),
with every member of the class carrying a \(C_8\) and the minimum
\(C_8\) count never dropping below 13 — so the \(C_{16}\) test is never
even decisive, and this channel is *further* from a witness than the
pinched one (whose equality blocks are blocked by 3–7 \(C_8\)s). What
survives in (c): channel (ii), the odd-prime-gcd channel — not
bipartite-forced, no structure theorem, no reduction, no dedicated
search — plus the missing parity analogue of `L032`'s 2-connected block
extraction. Two by-products of the same run: no bipartite counterexample
and no bipartite 1-atom at orders \(\le21\), verified internally.

## Open obligations

- `G013` (core): 1-atoms; the block question (band 4 = pencil endgame,
  bands \(\ge5\) open); the odd-prime-gcd channel and the missing
  parity block-extraction.
- `G014`: source-audit the external memo's literature and census leads.
  Item (2) (bipartite \(\ge32\)) is **de-gated** — `L035` T3 removes the
  need for the Mersenne-window logic and `C034` verifies the range
  internally; items (1), (3)–(6) still gate their threads.
- `G002`, `G003`, `G007`: the global mechanism; `G007` routes through
  `G013`'s conditional transfer.
- `G004`: only the original 1997 Erdős article body remains uninspected.

## Strategy portfolio

Standing instruction (user, S015): **all threads stay documented and
live**; sessions select by strategy audit, retire only on evidence.

- Thread A (pinched channel, proof side): the **pencil endgame**, fan
  case first — it owns the proved structure and the `A015` cascade
  pressure points; then the unique-path case. Sub-threads: the band-2
  closed rung as an `L030`-style warm-up; band-5 equality analogue.
- Thread B (congruence channels, disproof side): **B1/B2 are now one
  thread and largely executed** — the bipartite hunt (`E015`), empty
  through order 21; its live continuation is order 22+ (splits
  \((9,13)\), \((10,12)\), \((11,11)\) at 22), where genbg is the
  bottleneck and a dedicated \(C_4\)-free bipartite generator or
  SAT-modulo-symmetries would be the tool-building move. **B3 (new,
  the channel's open half):** structure theory for the odd-prime-gcd
  channel — is there a mod-\(p\) analogue of `L035`, or a proof that
  \(\gcd(S)\) with an odd prime factor is impossible under (D)?
  \(\Theta(3,3,3)\) shows the degree condition must do the work.
- Thread C (cubic frontier, disproof side): reproduce Markström 26/28,
  then order 30, where any \(\{C_4,C_8,C_{16}\}\)-free cubic graph is a
  counterexample outright; `L029` makes cubic decisive modulo 1-atoms.
  Requires the dedicated generator (`G014` item 6).
- Thread D (census mining, disproof side): power-length tests over
  existing cubic vertex-transitive / girth-\(\ge9\) / snark / cage
  lists (imports gated by `G014`).
- Thread E (proof side, new theorems): **bipartite EGC** — now with an
  internally verified base range (`C034`) and a sharpened target: every
  member of the class so far is killed by \(C_8\) alone, so the
  theorem to attempt is "bipartite + min degree 3 + \(C_4\)-free
  \(\Rightarrow C_8\)" — but that is *false* at large order (bipartite
  double covers of `C009`'s large-girth cubic graphs are cubic,
  bipartite, of girth \(\ge g\)), so the real theorem must be
  order-bounded or must consume the \(C_{16}\)/\(C_{32}\)
  alternatives. Also: Carr 4/7 → 1; 3-connectivity structure (the
  mod-\(m\) spectrum-confinement sketch, `A016` M10).
- Thread F (infrastructure): 1-atom structure theory; order-17+ legs of
  the pinched catalogue; the \(\{C_4,C_8\}\)-free generator build.
- Pivot triggers: a pencil-type band-4 taut core at order 16+ (kills
  the endgame as stated); a strict block or \(C_8\)-free equality block
  (disproof protocol); **any** power-free member of the `E015` class at
  order 22+ (immediate disproof, `L035` T3); a `G014` audit overturning
  an assumed bound.

## Human-level state

The disproof program builds counterexamples by chaining copies of a
two-terminal "engine" into a ring, so the ring's cycle lengths are sums
of the engine's path lengths. Last session an audited outside review
widened the hunt: sums can dodge the powers of two by *arithmetic* —
if every path length is odd, an odd number of them sums to something
odd, never a power of two — not only by squeezing lengths into a
factor-of-two window. This session proved that the odd-length hunting
ground has an exact identity: an engine has all-odd path lengths
precisely when it is **two-colourable** (bipartite) with its two
terminals in different colours, provided no part of it is idle. That
turns a search that needed path enumeration into one that needs only a
two-colouring plus a check for forbidden cycle lengths, and it shrinks
the haystack enormously — two-colourable engines with no 4-cycle are
rare. The search was rebuilt on that basis and run: **nothing exists up
to 21 vertices** (22 with a pendant), against a general wall that
stands at 15. Every candidate is killed by an 8-cycle, and never
barely — the fewest 8-cycles any candidate has is 13. The same run
incidentally confirms, from our own computation rather than an
unverified citation, that no two-colourable counterexample and no
two-colourable "single-defect" graph exists in that range. What the
theorem does *not* cover is the third arithmetic trick (all path
lengths sharing an odd factor); a small example shows that trick is not
about two-colouring at all, so it now stands as the one congruence
channel with no theory behind it.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 4%
- Previous estimate: 4% (S015)
- Reason for no change: this session converted one of the three new
  channels into a solved-instrument, cheaply searchable form and then
  emptied it six orders past the general frontier — real progress on
  *coverage* and a genuine new theorem — but the outcome was negative
  in the direction that matters for a disproof, and the margin data
  (never fewer than 13 blocking \(C_8\)s) argues the parity channel is
  further from a witness than the pinched one, not closer. Against
  that: the proof side gained nothing decisive, the ceiling correction
  from S015 still holds, the 1-atom question is untouched outside the
  bipartite instance, and the odd-prime-gcd channel is now visibly
  theory-free. Net: unchanged.

## Resume reading

1. `STATEMENT.md`
2. `A017` (the parity structure theorem and the bipartite criterion) and
   `E015/README.md` (the hunt, the verification tables)
3. `A016` + `references/external-agent-strategy-memo-2026-07-24.md`
   (the channel widening this builds on)
4. `A015` (the pencil package `L033`, the endgame, the cascade data)
5. `A014` for the block frame; `E013/README.md` for the pinched
   catalogue
6. `CLAIMS.md` rows `L031`–`L035`, `C030`–`C034`; `OBLIGATIONS.md`
   `G013`/`G014`; `sessions/S016-…md`
