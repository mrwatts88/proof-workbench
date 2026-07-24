# E006 — General {C4,C8}-free frontier at orders 14–17, extended to 18

- Date: 2026-07-23 (orders 14–17, session S007); order 18 added
  2026-07-24 (session S009, same pipeline, run under PyPy)
- Problem: `P-002`
- Evidence class: exhaustive per stated order (generation delegated to
  nauty's geng, anchored; all downstream tests independent and exact)

## Question

Does any connected graph on \(14\), \(15\), \(16\), \(17\), or \(18\)
vertices have minimum degree at least \(3\) while avoiding both
\(C_4\) and \(C_8\)? At orders \(\le 15\) such a graph would be exactly a connected
counterexample to `C001`; at orders \(16\)–\(31\) a connected
counterexample is exactly such a graph that also avoids \(C_{16}\), so
survivors (if any) are additionally tested for \(C_{16}\). A minimum-order
counterexample is connected, so per-order emptiness here excludes all
counterexamples of that order (`A007`).

The published general frontier before this run was order \(15\): Royle's
2002 search (`C012`) exhausted orders \(\le 15\), and no later general
computation is inspectable (`references/source-audit-2026-07-23-S007.md`).
Orders \(16\) and \(17\) are therefore past the verifiable frontier.

## Logical scope

Exhaustive for the stated orders, conditional on geng's correctness for
the delegated class (connected, \(C_4\)-free via `-f`, minimum degree
\(\ge 3\) via `-d3`). Everything downstream of generation is re-checked
independently: minimum degree and \(C_4\)-freeness (codegree criterion) on
every generated graph, \(C_8\)/\(C_{16}\) by the `E004` whole-graph
detector. geng itself is anchored on published counts (A1, A5), against
the independent `E004` search (A2), and with two-sided filter controls
(A3, A4); see Independent checks.

This is a finite exclusion; it says nothing about the universal statement
beyond the stated orders.

## Environment

- CPython 3.14.2, standard library only; nauty 2.9.3 (Homebrew bottle)
  supplying `geng`, `labelg`, `planarg`; macOS 26.5.1 arm64
- Order 18 leg: PyPy 7.3.23 (Python 3.11.15), same nauty binaries; the
  anchor suite was re-run and passed under PyPy before the order-18 run
- Exact arithmetic; no floating point; no randomness (process scheduling
  affects output order only; survivor lists are sorted)
- Detectors imported from the validated `E004` module via `E005`'s loader;
  graph6 decoding from `E005/e005lib.py` (self-tested, round-tripping)

## Inputs and search space

- `geng -q -c -f -d3 <n>` per order, optionally split into `res/mod`
  parts (order 16: 12 parts; order 17: 24 parts).
- Every streamed graph: assert order, minimum degree \(\ge 3\), and
  independent codegree \(C_4\)-freeness (a violation aborts the run);
  keep exactly the graphs with no \(C_8\).
- Survivors: full cycle spectrum, planarity, bipartiteness, Mersenne
  witness profile across all nonedges (path lengths \(3,7,15\)), and the
  counterexample test (no \(C_4,C_8,C_{16}\) — \(C_{32}\) is impossible at
  \(n\le 31\)).

## Reproduction

```sh
python3 frontier.py anchors
python3 frontier.py run 14 15
python3 frontier.py run 16 --parts 12 --workers 5
python3 frontier.py run 17 --parts 24 --workers 8
pypy3   frontier.py anchors
pypy3   frontier.py run 18 --parts 48 --workers 8   # ~2h50m wall
```

## Results

Anchors (all passed):

```text
A1 geng n=8 connected cubic = 5 (A002851 5)
A1 geng n=10 connected cubic = 19 (A002851 19)
A1 geng n=12 connected cubic = 85 (A002851 85)
A1 geng n=14 connected cubic = 509 (A002851 509)
A2 n=11: c4_free_min_deg3=9 c4c8_free=0 (E004: 0)
A2 n=12: c4_free_min_deg3=57 c4c8_free=0 (E004: 0)
A2 n=13: c4_free_min_deg3=503 c4c8_free=0 (E004: 0)
A3 order-10 C4-free cubic class: 3 graphs, all have C8
A4 C16 detector: Markstroem yes, l016_graph(4) no
A5 geng -f n=5 squarefree graphs = 18 (A006786 18)
A5 geng -f n=6 squarefree graphs = 44 (A006786 44)
A5 geng -f n=7 squarefree graphs = 117 (A006786 117)
A5 geng -f n=8 squarefree graphs = 351 (A006786 351)
```

Census:

```text
n=14: c4_free_min_deg3_connected=6059      c4c8_free=0   counterexamples=0
n=15: c4_free_min_deg3_connected=91433     c4c8_free=0   counterexamples=0
n=16: c4_free_min_deg3_connected=1655659   c4c8_free=0   counterexamples=0
n=17: c4_free_min_deg3_connected=34758006  c4c8_free=0   counterexamples=0
n=18: c4_free_min_deg3_connected=834711846 c4c8_free=0   counterexamples=0
```

(The order-18 line is the S009 extension: 48 `res/mod` parts, 8 PyPy
workers, roughly 2h50m wall; `data/survivors_n18.g6` and
`data/survivors_n18.json` are empty like their smaller-order
counterparts.)

## Interpretation

No graph on \(14\)–\(18\) vertices with minimum degree at least \(3\)
avoids both \(C_4\) and \(C_8\); the \(C_{16}\) test at orders
\(16\)–\(18\) never activated because the \(\{C_4,C_8\}\)-free class was
already empty. With the connectivity reduction and `L017` this proves
`A007/L018` (every counterexample has at least \(18\) vertices), and the
order-18 extension proves `A007/L022`: every counterexample has at
least \(19\) vertices. The smallest \(\{C_4,C_8\}\)-free graph of
minimum degree \(3\) has at least \(19\) vertices, while `E005` holds
such graphs at order \(24\); the extremal threshold for this class now
lies in \([19,24]\). Recorded as `C016` (orders 14–17) and `C023`
(order 18) supporting `L018` and `L022` (the proved bounds).

## Independent checks

- A1/A5: geng's counts equal the published OEIS values A002851 (connected
  cubic, four orders — exercising `-c -d3 -D3`) and A006786 (squarefree
  graphs, four orders — exercising `-f`).
- A2: at orders \(11\)–\(13\) the pipeline's end-to-end conclusion (zero
  \(\{C_4,C_8\}\)-free graphs) matches `E004`, a fully independent
  labelled enumeration with its own five anchors, run with a different
  generator, different symmetry handling, and different rejection logic.
- A3/A4: two-sided controls — a nonzero class known to be wiped out by the
  \(C_8\) filter is wiped out; known \(C_{16}\)-positive and
  \(C_{16}\)-negative graphs classify correctly.
- In-run: every graph re-verified for minimum degree and \(C_4\)-freeness
  independently of geng's own pruning; any failure aborts.
- External consistency: Royle's archived table (`C012`) reports \(775\)
  and \(5369\) graphs at orders \(14\) and \(15\) for his *restricted*
  class (adds the independent-high-degree condition), all containing
  \(C_8\); the full classes here are supersets (\(6059\), \(91433\)) and
  reach the same all-contain-\(C_8\) conclusion.
