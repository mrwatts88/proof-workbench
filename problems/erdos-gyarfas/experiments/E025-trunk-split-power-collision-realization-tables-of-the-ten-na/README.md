# E025 — Trunk-split power-collision realization tables of the ten named objects

- Date: 2026-07-25
- Problem: `P-002`
- Evidence class: exhaustive realization tables of finitely many named
  graphs (descriptive structure-mining; the two one-line proved facts
  the data suggested are recorded in `A025`, not here)
- Owner: session `S024` (attempt `A025`)

## Question

The (F) program's opening probe (`STATE.md`/`problem.json` first
action after S023). Under `L049` every cycle of a vertex-taut pair
\((H,a,b)\) is realized by a **trunk-split pair**: \(P=T_a\,A_1\,T_b\),
\(Q=T_a\,A_2\,T_b\) with \(A_1,A_2\) the two \(u\)–\(v\) arcs of the
cycle and \(T_a\) (\(a..u\)), \(T_b\) (\(v..b\)) shared trunks meeting
the cycle only at \(u\) resp. \(v\); by `L048`(iii) the case-(5b)
residual object's power-freeness is exactly the **non-realization** of
power lengths by such pairs. This experiment builds, for each of the
ten named objects — the eight \(\mathcal G\)-profile members (orders
19–20), Petersen\(-e\), and the order-14 full-triple exemplar — the
complete table of realizations of every power cycle (their
\(C_8\)s/\(C_{16}\)s):

- **all-pairs layer**: every witnessing pair \((P,Q)\) with
  \(E(P)\triangle E(Q)=E(C)\), recorded as \((x,y,s)\) multiplicities
  (`E021`/`E013` census semantics);
- **trunk-split layer**: the subset in `L049` arc form, each with its
  full shape \((x,y,s\,|\,a_1,a_2\,|\,t_a,t_b)\) — arc lengths
  \(a_1+a_2=\ell(C)\), trunk lengths \(t_a+t_b=s\),
  \(x=t_a+a_1+t_b\), \(y=t_a+a_2+t_b\), every invariant asserted per
  pair.

A witnessing pair is trunk-split **iff** \(E(P)\setminus E(Q)\) is
connected (then it is a single arc, its complement the other arc, and
the shared part splits into the two end trunks; the classifier asserts
each claim of this equivalence per pair rather than assuming it).

The point of the probe (pre-registered in `tables.py`'s docstring
before the first table was built): classify every realized length
against the forced-membership classes \(\mathbb P=\{4,8,16,32,64\}\),
\(\mathbb P-1\), \(\mathbb P-2\), and test nine per-cycle existential
patterns (`has_P`, `has_P1`, `has_PP`, `has_P1P1`, `has_forced_pair`,
`has_equal`, `has_s0`, `has_P2`, `all_P2`) for universality across
all ten objects. A candidate (F) mechanism must hold for every power
cycle of **all ten** — including both calibration objects (`A021`
discipline).

## Logical scope

- The tables are **exhaustive for the ten named graphs**: every simple
  \(a\)–\(b\) path pair is enumerated per object, so per power cycle
  the witnessing-pair list and its trunk-split sub-list are complete.
- They prove **no universal statement** — nothing about the class at
  other orders, nothing about power-free graphs (all ten objects are
  power-blocked by construction), nothing about statement 0.1. The
  pattern verdicts are exact for these graphs and are **evidence
  about the shape of (F)**, not steps of a proof of (F).
- The two proved one-liners the data suggested (the trunk bound
  \(s\le n-\ell(C)\) and its consequences) are recorded and proved in
  `A025`, not claimed here.

## Environment

- macOS 15 / darwin 25.5.0, arm64, 12 cores. **Machine-contention
  note** (`process/concurrency.md`): `E024` (order-21 rung, 8 worker
  processes) ran throughout; all E025 runs are single-process and
  timing fields are contended-machine figures.
- PyPy 7.3.23 (Python 3.11.15) production; CPython 3.14.2 anchor
  re-run and full-payload cross-check.
- Primitives imported by path from `E021/dissect.py` (which loads
  `E018/scan.py`, `E018/mod4.py`, `E013/catalogue.py`);
  `sys.dont_write_bytecode` set; all data writes redirected to
  `E025/data`. No census/path/cycle/tautness primitive re-implemented.
  New code: the trunk-split classifier (`arc_endpoints`,
  `shared_trunks`), the table builder, the pattern evaluator.
- Deterministic; stdlib only; no randomness; wall clock only in
  timing fields.

## Inputs and search space

The ten objects with their recorded reference data, loaded from the
experiments that produced them and asserted against the fresh
computation (terminals, \(S\), spectrum, path counts, cycle counts,
power-cycle counts, tautness, 2-connectivity):

| tag | source of record |
|---|---|
| P10-Petersen\(-e\) | `E013/data/cores.json` core 3 (+ recorded `symdiff_combos`) |
| N14-exemplar `M?AA@?WcKWHOWOL??` | `E021/data/interference_family1.json` (per-blocker combos) |
| N19-profile `R???C@?GC_B?@_aAA_aP?W_?BO@Gc?` | `E022/data/exemplar_t5_n19.json` |
| N20-A/B/C | `E022/data/t5_n20_profile.json` |
| N20p14-A/B/C/D | `E022/data/collect_n20_part14.json` |

## Reproduction

```sh
pypy3   tables.py anchors      # E021's 45-check suite + 14 new checks (also under python3)
pypy3   tables.py tables       # -> data/realization_tables.json
pypy3   tables.py patterns     # -> data/pattern_verdicts.json
python3 tables.py tables realization_tables_cpython.json   # cross-check
```

## Anchors

- `E021`'s 45-check suite re-passed through the import, **45/45 under
  PyPy 7.3.23 and CPython 3.14.2** (standing rule: anchors re-pass
  before any extension).
- 14 new-code checks, both interpreters: the \(C_{16}\) cycle graph
  (one realization, trunk-split, shape `8,8,0|8,8|0,0`, flags
  equal/s0/PP); the tail graph (pendant 2-path: trunk-split `6,6,2`
  with trunks (2,0), stratum "one"); the **weave control** (\(C_6\) +
  chord + two pendants: the classifier must find both witnessing pairs
  of the \(C_6\) and exclude the weaving pair `5+7-2*3` from the
  trunk-split layer while keeping `5,5,2|3,3|1,1`; both chord
  \(C_4\)s trunk-split-realized); Petersen\(-e\): all-pairs combos
  **equal the recorded `E013` census** and per-cycle pair counts equal
  `E021.dissect_pair`'s on the same blocker order; N14: per-blocker
  all-pairs combos and strata **equal the recorded `E021` family-1
  data**; N19: vertex-taut with 398 through-paths (recorded).
- Per-object assertions during `tables`: \(C_4\)-freeness; terminals =
  the degree-2 pair; tautness; \(S\), spectrum, path/cycle/power-cycle
  counts equal to every recorded reference field; power lengths
  present in the spectrum exactly as declared (\(\{8\}\) for the
  calibration pair, \(\{16\}\) for the eight profile members); the
  \(t=1\) identity \(x+y-2s=\ell(C)\) on every witnessing pair; the
  full arc-form invariant set on every trunk-split pair (single-arc
  connectivity both sides, matching endpoints, trunk path structure,
  trunk attachment, \(t_a+t_b=s\), \(a_1+a_2=\ell(C)\), the two
  length identities); **every power cycle has \(\ge1\) witnessing
  pair and \(\ge1\) trunk-split realization** (a failure of either is
  a pre-registered soundness alarm against `L049` — neither fired).

## Results

Totals: **604 power cycles** (7 + 3 \(C_8\)s; 46 + 112 + 105 + 37 +
69 + 80 + 80 + 65 \(C_{16}\)s), **61,901 witnessing pairs**, **1,971
trunk-split realizations**. Wall 4.3 s (PyPy). CPython re-run:
payloads **identical** (meta/timing fields excluded).

### The pattern verdict — no pre-registered pattern is universal

Cycles satisfying / power cycles (`data/pattern_verdicts.json` records
the failing-cycle indices per object):

| object | has_P | has_P1 | has_PP | has_P1P1 | forced_pair | equal | s0 | has_P2 | all_P2 |
|---|---|---|---|---|---|---|---|---|---|
| P10-Petersen\(-e\) | 7/7 | 0/7 | **7/7** | 0/7 | 7/7 | 6/7 | 2/7 | 0/7 | 0/7 |
| N14-exemplar | 3/3 | 2/3 | **3/3** | 0/3 | 3/3 | 1/3 | 0/3 | 0/3 | 0/3 |
| N19-profile | 22/46 | 25/46 | 4/46 | 6/46 | 10/46 | 14/46 | 11/46 | 22/46 | 2/46 |
| N20-A | 64/112 | 83/112 | 4/112 | 29/112 | 33/112 | 18/112 | 26/112 | 69/112 | 7/112 |
| N20-B | 60/105 | 69/105 | 4/105 | 22/105 | 26/105 | 20/105 | 16/105 | 69/105 | 4/105 |
| N20-C | 25/37 | 20/37 | 5/37 | 12/37 | 13/37 | 15/37 | 7/37 | 14/37 | 2/37 |
| N20p14-A | 13/69 | 64/69 | 1/69 | 48/69 | 49/69 | 3/69 | 5/69 | 32/69 | 4/69 |
| N20p14-B | 57/80 | 49/80 | 8/80 | 27/80 | 29/80 | 22/80 | 11/80 | 43/80 | 4/80 |
| N20p14-C | 57/80 | 44/80 | 8/80 | 24/80 | 27/80 | 30/80 | 11/80 | 38/80 | 3/80 |
| N20p14-D | 26/65 | 39/65 | 4/65 | 4/65 | 7/65 | 14/65 | 24/65 | 42/65 | 9/65 |

Even the weakest disjunction — *some trunk-split realization touches
some membership class at all* — fails: **30 cycles across six profile
objects are realized only through membership-blind lengths**, in
exactly three shapes: \(\{(5,13,1)\}\) (N19 ×3, N20-B ×4),
\(\{(9,11,2),(10,10,2)\}\) (N20-C ×4, N20p14-B ×2, N20p14-C ×8),
\(\{(5,11,0)\}\) (N20p14-B ×2, N20p14-D ×7).

### The calibration contrast

Both calibration objects are 100% on `has_PP` — **every \(C_8\) is
realized by two power-length paths** (Petersen\(-e\): `4,4,0|4,4|0,0`
on both stratum-"both" cycles, `4,8,2|2,6` on the rest, plus the equal
`5,5,1|4,4`; N14: the `4,8,2|2,6|1,1` fan with `3,9,2|1,7` /
`5,7,2|3,5` companions on two cycles, and one all-equal cycle
`8,8,4`/`9,9,5`×2/`10,10,6`) — while the eight profile objects sit at
1–8 out of 37–112. The power-participant structure of the calibration
pair is a small-order artifact, and the `A021` discipline (a proposed
mechanism must also hold at the frontier objects) correctly kills
"forced power-length paths collide" as an (F) mechanism candidate.

### What does organize the tables (the window structure)

- **The trunk bound is tight everywhere.** Every trunk-split
  realization satisfies \(s=t_a+t_b\le n-\ell(C)\) (the trunks live on
  the \(\le n-\ell(C)\) off-cycle vertices — proved in `A025` T2), and
  every object **realizes the bound exactly**: max \(s\) = 2 =
  \(10-8\) (P10), 6 = \(14-8\) (N14), 3 = \(19-16\) (N19), 4 =
  \(20-16\) (all seven order-20 objects). \(C_{16}\) s-distribution
  pooled: \(s=0\): 111, \(s=1\): 403, \(s=2\): 763, \(s=3\): 482,
  \(s=4\): 182.
- **Arc splits pooled** (\(C_{16}\)s): (4,12): 510, (5,11): 310,
  (3,13): 271, (7,9): 248, (6,10): 232, (8,8): 152, (2,14): 145,
  (1,15): 73 — every split occurs, short-arc reroutes dominate, the
  equal split is a 152/1,941 minority (equal-length pairs are
  invisible to the length **set** \(S\)).
- **The trunk-split skeleton is thin**: 2.6–4.0 realizations per cycle
  on average, against 76–138 witnessing pairs per cycle on the profile
  objects (9–13 on the calibration pair) — \(\approx\)3%.
- Strata of the 594 \(C_{16}\)s: both 111 / one 366 / neither 117;
  every "both" cycle has exactly one \((u,v)\) pair, forced to
  \((a,b)\) (n\_distinct\_uv = 1 on exactly the 111 "both" cycles — a
  consistency check of the arc form).
- **Spectra and \(S\)-sets at the frontier are saturated**: all eight
  profile objects have spectrum exactly \([3,n]\setminus\{4,8\}\) and
  \(S\) a gap-free interval \([5,n-1]\) or \([6,19]\) (N20p14-A:
  \(\{3\}\cup[6,19]\)) — in particular **\(6,14\in S\) for all
  eight** (the recorded double blocking). Both calibration objects gap
  \(S\) exactly at 6 (their \(\mathbb P-2\) dodge: P10
  \(S=\{4,5,7,8\}\), N14 \(S=[3,13]\setminus\{6\}\)).

## Interpretation

Narrowest justified conclusions.

1. **The pre-registered probe outcome is branch (b)**: no
   membership-patterned regularity organizes the power-collision
   realizations of the ten named objects — all nine registered
   patterns fail on the profile objects (several also on the
   calibration pair), and 30 cycles are membership-blind outright. An
   (F) mechanism of the form "the forced \(\mathbb P\)/\(\mathbb
   P-1\)/\(\mathbb P-2\) memberships collide arithmetically" has no
   empirical basis at the frontier.
2. What replaces it (recorded and argued in `A025`): the tables are
   organized by **window/order arithmetic** — the tight trunk bound
   \(s\le n-\ell(C)\), the thin trunk-split skeleton, and the
   saturation of \(S\) and the spectrum at the frontier orders (every
   profile object's \(S\) is interval-full and contains 6 and 14;
   every spectrum is everything except 4 and 8).
3. Nothing here proves or refutes (F); the tables are its evidence
   base and redirect its attack from membership arithmetic to
   window/order arithmetic (`A025`).

## Independent checks

- All-pairs layer asserted equal to the recorded `E013` census
  (Petersen\(-e\)) and the recorded `E021` family-1 per-blocker combos
  (N14) — the new enumerator against two independently produced
  records — and to `E021.dissect_pair` per cycle on Petersen\(-e\).
- Every recorded reference field of the `E022` JSONs (terminals,
  \(S\), spectra, path/cycle/\(C_{16}\) counts, tautness,
  2-connectivity) reproduced exactly for the eight profile objects.
- Full-payload cross-interpreter check: PyPy production vs CPython
  re-run **identical** (timing/meta fields excluded).
- Not independently re-implemented: the census primitives themselves
  (imported `E013`/`E018`/`E021` lineage, anchored 45/45 both
  interpreters).
