# E005 — Markström 24-vertex graphs: verification and reproduction

- Date: 2026-07-23
- Problem: `P-002`
- Evidence class: exact verification of a named imported graph, plus an
  exhaustive reproduction of a reported census (cubic, per stated order)

## Question

Markström (2004) reports that the smallest cubic graphs avoiding both
\(C_4\) and \(C_8\) have \(24\) vertices, that exactly four such graphs
exist at order \(24\), and that exactly one of the four is planar; the
planar one is the “Markström graph,” House of Graphs id 51419. The reported
graphs are the literature's nearest misses to a counterexample and the
intended test material for the saturation line. Can the named graph be
obtained and verified exactly, and can the order-\(24\) census be
reproduced independently, so that the four graphs are held internally
rather than trusted?

## Part 1 — verification of House of Graphs 51419

`hog51419.json` is the House of Graphs API payload for graph 51419,
downloaded 2026-07-23 and stored verbatim. `verify_markstrom.py` checks the
JSON's own consistency (adjacency list vs matrix), then verifies on the
adjacency-list graph: order \(24\), cubic, connected, non-bipartite, planar
(nauty `planarg`), no \(C_4\) (independent codegree criterion), no
\(C_8\) and the full cycle spectrum (the `E004` whole-graph detector),
presence of \(C_{16}\), and isomorphism between the adjacency-list graph
and the JSON's stored canonical graph6 form (nauty `labelg`). All checks
passed:

```text
order=24 degrees_cubic=True
connected=True
cycle_spectrum=[3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
girth=3 no_C4=True no_C8=True has_C16=True
bipartite=False
isomorphic_to_hog_canonicalForm=True
planar=True
nonedges=240 with_path3=105 with_path7=225 with_path15=240
nonedges_without_any_witness=0
edge_maximal_power_cycle_free=True
```

The last three lines are the new observation (`C015`): every one of the
\(240\) nonedges carries a simple path of length \(3\), \(7\), or \(15\) —
indeed every nonedge carries one of length \(15\) — so adding any edge
creates a \(C_4\), \(C_8\), or \(C_{16}\). At order \(24\) a \(C_{32}\) is
impossible, so this is exactly the Mersenne-witness half of the `L008`
saturation condition; the graph fails the full `L008` package only because
it already contains a \(C_{16}\). (The printed flag
`edge_maximal_power_cycle_free` names the witness-coverage test that ran;
the graph is not power-cycle-free, so it is not an `L008` object itself.)

## Part 2 — reproduction of the order-24 census

`generate24.py` generates every connected \(C_4\)-free cubic graph on
\(n\) vertices with nauty's `geng` (`-c -f -d3 -D3`, edge count fixed to
\(3n/2\); parallel `res/mod` parts at orders \(22\) and \(24\)), re-tests
\(C_4\)-freeness independently on every graph (codegree criterion), and
keeps the graphs with no \(C_8\) (the `E004` detector). Restricting to
connected graphs loses nothing: a disconnected cubic \(\{C_4,C_8\}\)-free
graph on \(\le 24\) vertices would need a connected cubic
\(\{C_4,C_8\}\)-free component on \(\le 12\) vertices, and orders \(\le
22\) are empty.

Validation anchors (`generate24.py anchors`, all passed):

```text
anchor geng n=8 connected cubic = 5 (A002851: 5)
anchor geng n=10 connected cubic = 19 (A002851: 19)
anchor geng n=12 connected cubic = 85 (A002851: 85)
anchor geng n=14 connected cubic = 509 (A002851: 509)
anchor n=10 C4-free cubic class: 3 graphs, 0 pass the no-C8 filter (E002: 0 expected)
anchor controls: K4 passes no-C8; cube's C8 detected
```

Census results (`generate24.py generate/filter`, orders 14–24):

```text
n=14: c4_free_cubic_connected=36 c4c8_free=0
n=16: c4_free_cubic_connected=269 c4c8_free=0
n=18: c4_free_cubic_connected=2761 c4c8_free=0
n=20: c4_free_cubic_connected=36101 c4c8_free=0
n=22: c4_free_cubic_connected=553227 c4c8_free=0
n=24: c4_free_cubic_connected=9467449 c4c8_free=4
```

The four order-24 survivors (sorted graph6, from `data/survivors_n24.g6`),
with spectra and Mersenne-witness profiles from the filter step and
planarity re-checked by `planarg -V` after the wrapper fix noted below:

```text
survivor[0] g6=W??????_A?C?E?D??WCCCOg?P_?O`?X?A_O?@@O@?W?GH??
  spectrum={3,6,7,9..24}      planar=False  witness3=108 witness7=240 witness15=240 unwitnessed=0
survivor[1] g6=W??????_A?C?E?D??WC_Cb?@C_?@QB?O?a_??d??Q_??Gc?
  spectrum={3,5,6,7,9..24}    planar=False  witness3=102 witness7=237 witness15=240 unwitnessed=0
survivor[2] g6=W????A?O@?A?A?`??oE?A@W@_O?_g?e??HC??aG@?S?@CO?
  spectrum={3,5,6,7,9..24}    planar=False  witness3=114 witness7=238 witness15=240 unwitnessed=0
survivor[3] g6=W???C@?G?_@?@??_OGE@?WO?oO?oO?PG?CW?@__??F??Og?
  spectrum={3,5,6,7,9..24}    planar=True   witness3=105 witness7=225 witness15=240 unwitnessed=0
```

Cross-checks against the literature and House of Graphs: the survivor
count \(4\) equals Markström's Table 3; exactly one survivor is planar,
as Markström states; and that planar survivor is `labelg`-isomorphic to
House of Graphs 51419 (canonical forms compared after canonicalizing both
sides). All four contain \(C_{16}\), so none is a counterexample. New
observation (recorded in `C018`): all four — not only the named Markström
graph — are fully Mersenne-witness-covered: adding any edge to any of
them creates a \(C_4\), \(C_8\), or \(C_{16}\). Survivor[0] additionally
has no \(5\)-cycle.

## Environment

- CPython 3.14.2, standard library only, plus nauty (Homebrew bottle:
  `geng`, `labelg`, `planarg`; version recorded below); macOS 26.5.1 arm64
- nauty version: 2.9.3
- Exact arithmetic throughout; no floating point, no randomness
- Detectors imported from the validated `E004` module; the graph6 codec is
  self-tested against nauty's own encoding (`C~` is \(K_4\)) and round
  trips on every self-check graph

## Reproduction

```sh
python3 verify_markstrom.py
python3 generate24.py anchors
python3 generate24.py all      # hours; orders 22 and 24 run in parts
```

## Interpretation

Part 1 upgrades the reported Markström graph to an internally verified
object and adds the witness-coverage observation `C015`. Part 2 reproduces
the order-\(24\) line of Markström's Table 3 and the emptiness of all
smaller cubic orders, upgrading that part of `C014` from a reported
computation to an internally reproduced one; the order-26 and order-28
counts (23 and 251) remain imported at reported strength only. These are
finite facts about the extremal boundary; they bear on `C001` only by
supplying verified test material for the saturation route.

## Independent checks

- geng's cubic counts anchored against OEIS A002851 at four orders; its
  `-f` flag is separately anchored in `E006` against OEIS A006786
  (squarefree graph counts, orders 5–8).
- Every generated graph is re-tested for \(C_4\)-freeness by the codegree
  criterion, independent of geng's `-f` pruning.
- Two-sided controls for the no-\(C_8\) filter: the order-10 anchor class
  (nonzero, all with \(C_8\)) is fully rejected; \(K_4\) (no \(C_8\))
  passes; the cube's \(C_8\) is detected.
- The planar survivor is checked for isomorphism with HoG 51419
  (`labelg`), tying the reproduced census to the externally published
  object; the survivor count is checked against Markström's Table 3.
- A wrapper bug was caught by exactly this external cross-check: the
  first survivor pass called `planarg -q -p` and treated nonempty stdout
  as "planar", but `-p` (planar_code output format) emits its
  `>>planar_code<<` header even for nonplanar input, so all four
  survivors initially read as planar — contradicting Markström's
  "only one planar". Direct `planarg -V` verdicts and the fixed wrapper
  (no `-p`) give one planar among the four, agreeing with the paper; the
  named-graph verification in Part 1 was unaffected in substance (that
  graph is genuinely planar). The defective call never fed any claim.
