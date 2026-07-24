# Current state

- Last updated: 2026-07-24 (S012)
- Problem: `P-002` — Erdős–Gyárfás Conjecture

## Exact target

Every finite simple undirected graph of minimum degree at least \(3\) contains a
cycle whose length is a power of two. See normalized `STATEMENT.md` version 0.1.

## Established

- `L001`–`L006`: block and edge-minimal reductions; hand proofs that every
  counterexample has \(\ge11\) vertices.
- `L008`–`L013` saturation package with `L014`–`L016` delimitations.
- `L017`/`L018`/`L022` finite exclusions: every counterexample has at
  least **nineteen** vertices; extremal \(\{C_4,C_8\}\)-free window
  \([19,24]\); census capped at order 18.
- `L019`–`L021` lift machinery; `L023`–`L024` the collision-wall theorem
  (reviewed, `R001`): the lift/falsification program is closed as a
  theorem.
- `L025` atom reduction (S011): a 1-atom or a pinched power-free
  two-terminal gadget (2-atom) yields counterexamples by
  doubling/triangle or ring-in-dyadic-gap assembly; contrapositively 0.1
  forces **spread-doubling** (\(s_{\max}\ge2\,s_{\min}\)).
- **New (S012): the corrected rung program.** `L026` rung completeness:
  2-atoms with \(S=\{1\}\) or \(s_{\min}=2\) exist **iff**
  counterexamples exist (two counterexample copies hide behind cut
  vertices), so the unrestricted bottom rungs — and spread-doubling
  itself — are each *equivalent* to statement 0.1. `L027` lobe
  decomposition: every gadget is vertex-taut or hangs a lobe at one cut
  vertex; power-free lobes are 1-atoms or min-degree-3 power-free
  graphs. `L028` taut bottom rungs: no taut gadget has \(S=\{1\}\); no
  taut \(C_4\)-free gadget has \(s_{\min}=2\), \(S\subseteq\{2,3\}\)
  (\(C_4\)-freeness alone suffices) — every 2-atom with
  \(s_{\min}\le2\) therefore routes through the 1-atom question and has
  order \(\ge17\). `L029` cubic reduction: modulo the 1-atom question,
  every minimal counterexample is cubic — 0.1 ⟺ no cubic counterexample
  and no 1-atom.

## Imported frontier

- `C004`–`C009`, `C012`–`C014`, `C017`, `C024`–`C026` unchanged
  (Bondy–Vince read in the published PDF; `C025`/`C026`
  abstract-strength). The min-degree-3 literature frontier remains
  exactly Bondy–Vince strength.

## Program status

The disproof interface (`G013`) is concentrated on two objects. (a) The
**1-atom question**: a power-free graph with exactly one sub-cubic vertex
(degree 2 in the minimal case, `L029`) — now triply central: it is the
sole content of the unrestricted bottom rungs, the lobe half of every
non-taut 2-atom, and the sole obstruction to the cubic reduction. (b)
**Taut 2-atoms with \(s_{\min}\ge3\)**: \(K_{3,3}-e\) realizes the taut
pinched shape at \(s_{\min}=3\) the moment \(C_4\) is allowed (its only
power is the 4-cycle), so the next rung is exactly where the
power-spectrum fight starts. `C027`/`C028` (exhaustive): no atom of any
kind through order 15; through order 13 every taut pinched gadget has
\(s_{\min}=6\) with interval through-set \(\{6,\dots,11\}\) and a
\(C_8\) — taut pinched \(s_{\min}\in\{3,4,5\}\) is empty there even
before \(C_8\)-freeness is imposed.

## Open obligations

- `G013` (core, refined S012): 1-atoms and taut \(s_{\min}\ge3\)
  2-atoms.
- `G002`, `G003`, `G007`: the global mechanism; `G007` routes through
  `G013`'s conditional transfer.
- `G004`: only the original 1997 Erdős article body remains uninspected.

## Strategy portfolio

- Primary: the **taut \(s_{\min}=3\) rung** — prove that no taut
  \(C_4\)-free power-free (D)-gadget with \(S\subseteq\{3,4,5\}\)
  exists, or exhibit one (disproof via `L025` R3). Structure available:
  terminals at distance 3, tautness pins every vertex to a short
  \(a\)–\(b\) path, \(C_4\)-freeness bounds shared neighborhoods;
  `C028`'s survey says the target is empty through order 13 even without
  \(C_8\)-freeness, and \(K_{3,3}-e\) is the shape to beat. Falsifiable
  both ways.
- Live alternative: minimal 1-atom structure theory (the sub-cubic
  vertex has degree 2; next: 2-connectivity, cycle structure through the
  exceptional vertex, interaction with `L022`-style census arguments).
- Deferred: order-16 atom census (multi-part PyPy, `E006`/S009 pattern,
  \(\sim\!15\times\) order 15).
- Pivot trigger: a taut pinched \(s_{\min}=3\) gadget found (disproof
  protocol: assemble the ring, verify, fresh reproduction audit); or the
  taut rung closing with a mechanism that generalizes (promote to the
  spread-doubling ladder); or the rung stalling with no forcing after
  honest effort (switch to 1-atom structure or the census).

## Human-level state

The project's disproof interface asks for a small two-terminal graph that
avoids power-of-two cycles while keeping all its connection paths in a
narrow band. This session stress-tested the inherited plan — prove the
narrowest cases impossible by hand — and found it was secretly circular:
in those narrowest cases a would-be gadget can smuggle an entire
counterexample inside parts that no connection path ever visits, so
proving them impossible is exactly as hard as the whole conjecture. The
repair is a cleanliness condition ("taut": every vertex must serve some
connection path), which provably confines all smuggling to hanging
"lobes" that are themselves near-counterexamples. Under it the two
narrowest cases really are impossible, by short arguments using only the
absence of 4-cycles. A byproduct: unless a specific near-counterexample
object (a "1-atom") exists, the whole conjecture reduces to 3-regular
graphs. Machine checks verified every new lemma on tens of thousands of
real graphs and mapped the enemy's actual shapes: the smallest honest
pinched gadgets keep their paths in the band 6–11 and always carry an
8-cycle.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 2%
- Previous estimate: 2% (S011)
- Reason for no change: the session corrected a plan premise (the
  unrestricted rungs were illusory targets) and delivered real
  unconditional lemmas, but the correction itself shows the rung ladder
  cannot shortcut the global problem: the honest fight is the taut
  \(s_{\min}\ge3\) region and the 1-atom question, both of which retain
  the conjecture's global-forcing character. Clarity is not proximity.

## Resume reading

1. `STATEMENT.md`
2. `A012` (rung completeness, lobe decomposition, taut rungs, cubic
   reduction)
3. `A011` (the atom reduction), `E010`/`E011` READMEs
4. `CLAIMS.md` rows `L025`–`L029`, `C027`–`C028`; `OBLIGATIONS.md`
   `G013`
5. `sessions/S012-…md`
