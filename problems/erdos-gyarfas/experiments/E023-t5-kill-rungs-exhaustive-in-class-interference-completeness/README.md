# E023 — T5 kill rungs: exhaustive in-class interference-completeness at order 13, sparse general-graph slices at orders 8–11, and the constructive verification of the trimming proof

- Date: 2026-07-25
- Problem: `P-002`
- Evidence class: exhaustive scans over exactly delimited finite
  classes, plus a per-instance mechanical verification of a recorded
  proof's construction (see Logical scope)
- Owner: session `S023` (attempt `A024`)

## Question

`A023` T5 (the candidate lemma of the interference program): *if
\((H,a,b)\) is vertex-taut, is every cycle of \(H\) an interference
cycle — the edge symmetric difference of two distinct simple
\(a\)–\(b\) paths?* This experiment runs the two remaining
pre-registered kill rungs (`STATE.md`/`problem.json` first action),
extends them with four cheap neighboring slices, and then — after the
`A024` proof of T5 was written — re-executes the proof's own
construction step by step on every instance in scope, so that any gap
in the argument fails a concrete assertion on a concrete graph.

The predicate, engine, and tautness instrument are `E021`'s, imported
by file path exactly as `E021` imports `E018`/`E013` (no primitive
re-implemented; `sys.dont_write_bytecode` set; all data writes
redirected to `E023/data`).

## Logical scope

- The order-13 rung and the order-8–11 slices are **exhaustive for
  their delimited classes** (stated per run below). They prove nothing
  outside those classes and nothing about power-free graphs or
  statement 0.1.
- The `constructive` runs are a **verification instrument for the
  `A024` proof**: for every vertex-taut pair in scope, for every cycle
  and every cycle edge, they assert the existence of the Lemma-A
  witness and every invariant of the trimming construction (trunk
  hit-sets, simplicity of both hybrid paths, symmetric difference
  exactly the cycle, membership of both hybrids in the census path
  list). A pass does not *prove* T5 (the proof does); a single failed
  assertion would *refute the proof as written* at a named step on a
  named instance.
- The `tautcal` run re-derives `E021`'s recorded `tautgeneral`
  aggregates with the new slice driver before that driver is used on
  anything new; agreement is asserted, not eyeballed.

## Environment

- macOS 15 / darwin 25.5.0, arm64, 12 cores; no sibling workers;
  single-process runs only (several run concurrently as independent
  processes).
- PyPy 7.3.23 (Python 3.11.15) for production; CPython 3.14.2
  additionally for the anchor suite. nauty `geng` 2.9.3 on PATH
  (`/opt/homebrew/bin`).
- Primitives imported by path: `E021/dissect.py` (which itself loads
  `E018/scan.py` as `scan`, `E018/mod4.py`, `E013/catalogue.py`).
  `E021.DATA`, `scan.DATA`, `cat.DATA` redirected to `E023/data`
  before any call.
- Deterministic; standard library only; wall clock only in timing
  fields.

## Reproduction

```sh
pypy3   rungs.py anchors            # E021's 45-check suite (also under python3)
pypy3   rungs.py tautcal            # slice driver vs recorded E021 aggregates
pypy3   rungs.py smallworld13       # kill rung 1 (exhaustive in-class, order 13)
pypy3   rungs.py tautslice 8 8 12 n8_sparse
pypy3   rungs.py tautslice 9 9 13 n9_sparse
pypy3   rungs.py tautslice 9 14 14 n9_e14
pypy3   rungs.py tautslice 10 10 13 n10_sparse
pypy3   rungs.py tautslice 11 11 13 n11_sparse
pypy3   rungs.py tautslice 8 13 28 n8_dense   # completes order 8 exhaustively
pypy3   rungs.py constructive general 4 5 6 7
pypy3   rungs.py constructive slice 8 8 12 n8_sparse
pypy3   rungs.py constructive slice 9 9 13 n9_sparse
pypy3   rungs.py constructive named
```

## Anchors and calibration

- `anchors`: E021's 45-check suite through the import — **45/45 under
  PyPy 7.3.23 and 45/45 under CPython 3.14.2** (rule: anchors re-pass
  before any extension).
- `tautcal`: the new slice loop over all connected graphs of orders
  4–7 with the full edge range reproduces `E021/tautgeneral.json`
  **exactly**: pairs 19,476; taut pairs 12,313; cycles tested 723,926;
  non-decomposable 0 (asserted per key).
- `smallworld13`'s class size **10,966** equals the `A021` recorded
  order-13 profile-class count; the engine is `E021`'s
  `cmd_smallworld` itself, order argument 13, output redirected.

## Results

### Kill rung 1 — `smallworld 13` (exhaustive over the profile class at order 13, power-freeness dropped)

Class = connected, \(C_4\)-free, exactly two degree-2 vertices, all
other degrees \(\ge3\) (`E018` stream, `geng -q -c -f -d2 13 19:78`).

| quantity | value |
|---|---|
| class members | 10,966 (= `A021` record) |
| vertex-taut members | 10,853 |
| cycles of taut members tested | 1,614,300 |
| **non-decomposable among them** | **0** |
| non-taut members | 113 |
| their cycles (non-decomposable) | 10,255 (10,142) |
| non-taut members with a non-decomposable cycle | **113/113** |
| wall time | 191.4 s (PyPy) |

**T5 survives its largest pre-registered rung, and the tautness
biconditional is exact at order 13** (every taut member fully
decomposable, every non-taut member failing) — extending the `C042`
pattern from orders 10–12 to 13 with zero exceptions either way.

### Kill rung 2 — sparse general-graph slices (no degree condition, no \(C_4\)-freeness)

Streams `geng -q -c n mine:maxe`; every vertex pair of every graph
with at least one cycle; vertex-taut pairs tested on **every cycle of
the graph**.

| n | edges | graphs | pairs | taut pairs | cycles tested | non-dec | time |
|---|---|---|---|---|---|---|---|
| 8 | 8–12 | 2,794 | 78,232 | 25,907 | 399,120 | **0** | 2.2 s |
| 9 | 9–13 | 16,011 | 576,396 | 130,842 | 2,131,695 | **0** | 13.5 s |
| 9 | 14 | 13,855 | 498,780 | 224,320 | 7,115,669 | **0** | 62.6 s |
| 10 | 10–13 | 34,833 | 1,567,485 | 120,252 | 1,193,874 | **0** | 8.1 s |
| 11 | 11–13 | 44,490 | 2,446,950 | 39,360 | 217,272 | **0** | 2.9 s |

The slices are exhaustive for their cyclomatic-bounded classes
(cyclomatic number \(\le5\) at order 8, \(\le6\) at 9, \(\le4\) at 10,
\(\le3\) at 11) — the sparse, long-cycle world where the recorded
weaving obstruction would have had to live. The dense completion of
order 8 (`tautslice 8 13 28`) landed in the same session — see the
`n8_dense` subsection at the end of this file — making order 8
exhaustive over **all** connected graphs.

### Constructive verification of the `A024` proof (every step asserted per instance)

For every vertex-taut pair in scope, every cycle \(C\), **every edge
\(pq\in E(C)\)**: a census path through \(pq\) exists (Lemma A); the
first/last-hit trimming invariants hold; both hybrids are simple
\(a\)–\(b\) paths; their symmetric difference is exactly \(C\); both
hybrids occur in the census path list.

| scope | taut pairs | cycle instances | (cycle, edge) instances | result | time |
|---|---|---|---|---|---|
| all connected graphs, orders 4–7 | 12,313 | 723,926 | 3,727,132 | **all pass** | 17.7 s |
| order-8 slice, edges 8–12 | 25,907 | 399,120 | 2,008,186 | **all pass** | 10.2 s |
| order-9 slice, edges 9–13 | 130,842 | 2,131,695 | 11,577,122 | **all pass** | 61.6 s |
| named objects (below) | 10 | 4,754 | 66,866 | **all pass** | 0.7 s |

Named objects: Petersen\(-e\) (29 cycles / 204 edge instances), the
order-14 full-triple exemplar `M?AA@?WcKWHOWOL??` (64 / 624), the
order-19 profile member `R???C@?GC_B?@_aAA_aP?W_?BO@Gc?` (411 /
5,530 — the recorded S022 cycle total reproduced), and all seven
order-20 profile members (766+774+350+572+648+648+492 = 4,250 cycles
/ 61,508 edge instances — again the recorded totals, so all **eight
profile objects in existence** pass the constructive proof check on
all 4,661 recorded cycles).

## Interpretation

Narrowest justified conclusions.

1. Both pre-registered T5 kill rungs are spent and **survived**, with
   the four extension slices and the order-8 dense completion also
   clean: no non-decomposable cycle exists in any vertex-taut pair in
   any scanned class (order 13 in-class exhaustive; **orders \(\le8\)
   general exhaustive** — every graph, every vertex-taut pair, every
   cycle; cyclomatic-bounded slices at 9–11).
2. The tautness biconditional (`C042`) is exact on the full profile
   class at order 13.
3. Every step of the `A024` trimming proof executes successfully on
   every instance in scope, including the eight profile objects at
   orders 19–20 — the case-(5b)-adjacent world. The proof's claim set
   has no counterexample anywhere it can currently be tested.
4. None of this is the proof: T5's universal statement rests on
   `A024`'s argument (audited in `R002`), not on these scans.

## Independent checks

- The engine and tautness instrument are `E021`'s own, re-anchored
  (45/45, both interpreters) before any new run.
- The new slice driver was calibrated against `E021`'s recorded
  aggregates before first use (exact match on all four keys).
- `smallworld13` reproduces the `A021` class count at order 13.
- The named-object runs reproduce the S022 per-object cycle totals
  (411; 766, 774, 350, 572, 648, 648, 492) recorded in
  `E022/data/exemplar_t5_n19.json`, `t5_n20_profile.json` and the
  part-14 recollection.
- Not independently re-implemented: geng (imported generation layer,
  anchored as in `E010`–`E022`).
- Cross-interpreter: `tautcal` and `constructive named` re-run in full
  under CPython 3.14.2 — every aggregate and every per-object
  cycle/edge-instance count identical to the PyPy production run
  (production JSON copies are the PyPy re-run).

### `n8_dense` (order 8, edges 13–28; completes order 8) — landed

| n | edges | graphs | pairs | taut pairs | cycles tested | non-dec | time |
|---|---|---|---|---|---|---|---|
| 8 | 13–28 | 8,300 | 232,400 | 192,188 | 36,398,537 | **0** | 1,590.9 s |

Coverage arithmetic: 2,794 (edges 8–12) + 8,300 (edges 13–28) =
11,094 = all connected order-8 graphs with \(\ge8\) edges; the
remaining 23 connected order-8 graphs are the trees (7 edges), which
have no cycles and satisfy the property vacuously. A vertex-taut pair
requires connectivity (a vertex in another component lies on no
\(a\)–\(b\) path), so with `tautcal`'s orders 4–7 this makes T5's
conclusion **exhaustively verified on every graph of order \(\le8\)
and every vertex-taut pair**: order-8 totals 218,095 taut pairs and
36,797,657 cycles tested, zero non-decomposable.
