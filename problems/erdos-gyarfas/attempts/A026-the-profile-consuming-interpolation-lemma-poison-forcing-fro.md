# A026 — the profile-consuming interpolation lemma: poison forcing from min degree 3 off the terminals in the window

- Date opened: 2026-07-25
- Problem: `P-002`
- Status: active
- Portfolio role: primary (Tier 1, `G015` case (5b), proof side; session
  `S026` — the (F) program's named missing tool after the `C046`
  recalibration)

## Intended mechanism

Prove (F-S) on the window by an **interpolation lemma consuming the
exactly-two profile**. Target family, strongest first:

- **(I1, interval form)** Every vertex-taut two-terminal pair \((H,a,b)\)
  with \(H\) \(\{C_4,C_8\}\)-free, \(d(a)=d(b)=2\), every non-terminal
  degree \(\ge3\), and \(18\le n\le35\), has \(S\supseteq[c,n-1]\) for some
  \(c\le14\).
- **(I2, poison form)** …has \(S\cap\{6,14\}\ne\emptyset\). (All (F-S)
  needs; implied by (I1) since \(n\ge15\) puts \(14\in[c,n-1]\).)
- **(I3, step form)** …\(S\) contains no gap of length \(>g\) above
  \(\min S\), plus max/parity facts making \(\{6,14\}\) unavoidable.

The empirical basis (`A025` T3, `C046`): all eight profile objects satisfy
(I1) with \(c\in\{5,6\}\) (seven are gap-free intervals); the 9,061
near-miss rows show every weakening that drops the profile hypothesis is
false. The candidate mechanism to extract: what length-adjusting reroutes
does "every internal vertex has a third edge" enable that the near-misses
(with their extra degree-2 corridors) provably lack?

Why this is preferable to the live alternatives: it is the only surviving
proof-side move on the only surviving program ((F) ⟺ case (5b) below 36),
its kill set is on disk, and its data-first sub-move is cheap.

## Entry assumptions

Statement 0.1 verbatim. Consumed at recorded strength: `L049`/`L050` (T5,
tautness ⟺ interference-completeness), `L048`(iii) (spectrum identity),
`L042` (residual-object forced structure), `L046` (2-connected below 36),
`L051` (trunk bound), `C046` (census verdict + corpus), `C036`–`C044`
floors. The lemma targets are **speculation** until proved; no draft enters
the ledger below proved strength.

## Targeted obligations

- `G015`: exclude case (5b) — (I2) on the window closes it below 36
  ((F-S) ⟹ closure power-blocked; `L046` covers the chain side).
- `G013`(a): structure theory for the tight-1-atom question.

## Plan and decisive tests

1. **Dissection first (`E027`)**: contrast the 8 profile objects with the
   9,061-row corpus. Questions fixed in advance: (a) what does a near-miss
   \(S\) look like — interval-except-poisons, sparse even part, or
   corridor-quantized? (b) where do the extra degree-2 vertices sit
   relative to the terminals and to each other (corridor structure)?
   (c) which lengths adjacent to the gaps are present (gap boundary
   structure — is the miss at 6/14 a ±1 miss)? (d) does the profile/near-miss
   contrast localize (a reroute at a degree-\(\ge3\) vertex that fixes the
   gap)? Cheapest falsification: (d) comes back empty — no localizable
   contrast — and the local form dies.
2. **Kill discipline (binding, in this order)**: any candidate lemma must
   (i) **fail on the corpus** — if its hypotheses hold on any stored
   near-miss row it is unsound by construction; (ii) **fail off-window on
   the calibration pair** (`A021`: Petersen\(-e\) at order 10 is itself an
   exactly-two vertex-taut pair with \(S=\{4,5,7,8\}\), so any draft
   insensitive to \(\{C_4,C_8\}\)-freeness-plus-window is false); (iii)
   **succeed on the eight profile objects**.
3. Pivot triggers: no localizable contrast → global forms ((F-T)
   cycle-space compression; block-chain arithmetic on `L049`'s normal
   form). A draft holding on a corpus row → kill immediately. Any
   disagreement with `E026` recorded fields → soundness alarm, halt.

## Deductions

Notation: \((H,a,b)\) a taut pair, \(S\) its through-set, \(M=\max S\),
poison set \(\{6,14\}\); "profile" = exactly-two (all non-terminal degrees
\(\ge3\)); "corpus" = `E026`'s 9,061 stored taut gapped rows; "full dodge"
= \(2,6,14\notin S\).

### T1 (the dodge taxonomy) — computed (`E027` Q1/Q2, offered as `C047`)

The corpus realizes exactly three dodge shapes, all rigid:

- **A (short + 6-hole)**, 7,380 rows: \(M\le13\), a hole at 6 in an
  otherwise even-rich set. The minimal full dodges have \(M=13\)
  **exactly** at every order 16–20.
- **A′ (distance)**, 1,226 rows: \(\min S=7\) exactly (never \(\ge8\)),
  \(M\le13\).
- **B (long-range mod-4)**, 455 rows: \(M\ge15\), holes exactly at
  \(\{6,10,14\}\) (146 also gap the odd 7); 395/419 at order 20 have even
  part exactly \(\{4,8,12,16\}\subseteq4\mathbb Z\) — the `L034`
  channel-(iii) pattern realized in-window on non-bipartite members. The
  14-dodge is never by distance; the 6-dodge never by shortness.

### T2 (pair-locality and the frontier) — computed

The dodge is a property of the pair, not the member: the order-20
minimal-slack members carry one dodge pair beside five fully saturated
pairs, with full spectra and triangles. Full-dodge frontier: min ndeg2 =
5/7/5/6/5/6/**4** at orders 12–20; the ndeg2-4 realization is
adjacent-terminals (\(S=\{1\}\cup[8,13]\), reducing recursively to an
off-terminal distance dodge in \(H-a-b\)); non-adjacent frontier ndeg2 = 5.
**The profile hypothesis is load-bearing by two subdivision vertices at
order 20.** Consequence: any member-level lemma is dead; and the corpus
frontier trend is consistent with (F-S) failing at some order \(>20\) —
`E024` + the census extension is the standing test.

### T3 (the subdivision frame) — computed

Corridor weights pool to {2: 47,662, 3: 2,006, 4: 10} — dodges ride many
single subdivisions, never long corridors. Smoothing every dodge row to its
reduced graph \(H^*\): **99.1% (8,978/9,061) have a \(C_4\) or \(C_8\) in
the simple part of \(H^*\)** (all 83 exceptions are parallel-corridor
theta-hubs, all shape A). Shape B is 100% class-violating after reduction.
Near-misses are subdivisions of class-violating graphs; the profile is the
subdivision-free stratum where \(\{C_4,C_8\}\)-exclusion binds the
irreducible graph.

### T4 (odd-cycle supply: mechanism candidate killed) — computed

100% of dodge members carry triangles (and almost all carry
\(C_5/C_6/C_7\)). "The profile forces saturation because dodgers lack
\(\pm1\)-adjustment material" is refuted before drafting.

### T5 (the span law) — proved (one line)

In a \(\{C_4,C_8\}\)-free graph, no path has a chord of span 3 or span 7
(the chord plus the path arc is a \(C_4\)/\(C_8\)). Verified as an
assertion on all eight profile objects and all 36 Hamiltonian corpus rows
(no span-3/7 chord anywhere).

### T6 (the exchange calculus validates as the long-range engine) — computed

First-order disjoint-chord surgery on a single Hamiltonian path (savings
\(\sum(\sigma_k-1)\) over interior-disjoint chord families; every generated
length is a real path):

- On all eight profile objects it generates the **entire top of \(S\) down
  to 10** — every miss lies in \([4,9]\) — in particular **14 on all
  eight**; one object is fully generated.
- On the 36 Hamiltonian dodgers it fills no interval and respects every
  hole; their chord geometry (exactly two span-2 chords, remaining spans
  \(\equiv1,2\bmod4\)) makes savings \(\equiv3\pmod4\) — the class hitting
  \(\{14,10,6\}\) from \(M=17\) — unreachable by disjoint packings.

The observed profile spans \(\{2,4,5,6,9,12,13,14,17\}\); savings small
targets (\(M-14\in[3,20]\) in-window) sit exactly where the calculus is
strong.

### T7 (the redirect: the lemma splits, and the missing tool sharpens) — analysis; open

(F-S) on the profile decomposes against T1's taxonomy:

> **(L-A) (open target, speculation).** Short-range exclusion: every
> vertex-taut \(\{C_4,C_8\}\)-free profile pair with \(18\le n\le35\) has
> \(M\ge14\) — or, if \(M\le13\), then \(6\in S\).

> **(L-B) (open target, speculation).** Long-range poison forcing: every
> such pair with \(M\ge14\) has \(14\in S\) or \(6\in S\).

(L-A) ∧ (L-B) ⟹ (F-S). Both are windowed and profile-consuming; both fail
on the corpus by construction (T1 realizes their negations at ndeg2
\(\ge4\)), and the `A021` discipline reads: Petersen\(-e\) shows
\(C_8\)-freeness is necessary for (L-A) (it is \(C_4\)-free, taut,
exactly-two, \(M=8<14\) — but has \(C_8\)s), and both targets are vacuous
at their off-window orders on the calibration pair (\(M<14\) there). The
missing tool named by `A025` T4 ("a lower-bound theory for through-path
length sets") sharpens to:

- for (L-B): **the span/savings combinatorics of the chord system of a
  longest path under \(C_4/C_8\)-exclusion** — prove the in-window profile
  chord structure always realizes savings \(M-14\) or \(M-6\) (T5's span
  law + the C4/C8 chord-pair exclusions, e.g. no interlocking span-2
  pairs, are the raw material; the profile forces \(n-2\) internal
  vertices to carry chords or ears);
- for (L-A): **the ear-overload structure of short-range taut profile
  pairs** — with \(M\le13\) and \(n\ge18\), \(\ge4\) off-path vertices
  hang on ears whose internal vertices all branch (the near-misses'
  ear-internal vertices are exactly their corridor vertices; the profile
  forbids that), plus the T2 recursion for the adjacent case. No proof
  step exists yet for either; (L-A) has the thinner empirical margin
  (two subdivisions at order 20) and the harder outlook.

## Failure analysis

Nothing died unexpectedly; two mechanism candidates were killed cheaply and
deliberately: member-level hypotheses (T2) and odd-cycle supply (T4). The
dissection's pivot criterion ("no localizable contrast → drop the local
form") half-fired: the contrast is not terminal-local (remote subdivisions
flip a pair), but it **is** structured — the taxonomy is rigid and the
exchange engine reproduces the positive side — so the attempt continues
with the sharpened targets rather than pivoting to (F-T).

## Salvageable results

1. The dodge taxonomy T1 and frontier T2 (offered to the ledger as
   `C047`): the shapes any (F-S) proof must kill, with the pair-locality
   warning and the ndeg2-4 frontier objects named.
2. The subdivision frame T3: 99.1% class-violating reductions — the
   mechanism statement behind "the lemma must consume the profile".
3. The span law T5 (proved) and the exchange validation T6: the formal
   engine for the long-range half, calibrated on both sides.
4. The (L-A)/(L-B) split T7 with the sharpened tool spec — the next
   session's proof targets.
5. Kill-discipline artifacts: `corpus_rows_compact.json` (the refutation
   set, now with per-row shapes/corridors) and the six frontier members.

## Exit state

- Status: active (plan step 1, the dissection, is complete; step 2 — the
  proof attempt against (L-A)/(L-B) — is open)
- Promoted records: experiment `E027`; ledger row `C047` (dissection
  verdict) offered; `G015` updated.
- Next action: harvest `E024` first when it lands (census the order-21
  rung; a gapped exactly-two member kills (F-S)); then attack (L-B) via
  the chord-savings combinatorics (build the C4/C8 chord-pair exclusion
  table over a longest path; prove savings \(M-14\) or \(M-6\) reachable
  in-window on the profile) with (L-A) behind it (ear-overload +
  the T2 adjacent-case recursion).
