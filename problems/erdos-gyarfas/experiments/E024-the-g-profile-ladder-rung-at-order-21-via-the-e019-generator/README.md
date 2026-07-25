# E024 — The G-profile ladder rung at order 21 via the E019 generator (S023 close-of-session background leg)

- Date: 2026-07-25 (launched at S023 close)
- Problem: `P-002`
- Evidence class: exhaustive scan of a delimited finite class
  (generation-layer lineage as in `C039`/`C043`), **RUNNING — no
  result here is citable until a later session harvests it**
- Owner: session `S023` (launch only; harvest is named follow-up work)

## Question

Does the exactly-two-degree-2 \(\{C_4,C_8\}\)-free profile class at
order 21 contain members, and if so, is any of them power-free with
\(S\cap(\mathbb P-2)=\emptyset\) (a \(\mathcal G\)-member — and then a
tight 1-atom seed, an **immediate disproof** trigger)? Every new
profile member is also a new data point for the (F) program
(`STATE.md` S023): its \(C_{16}\) blocking and \(S\)-arithmetic join
the eight recorded profile objects' realization tables.

## Logical scope

Exhaustive for the stated class at order 21 when the 16-part run
harvests cleanly (partition property anchored in `C039`); inherits the
generation-layer caveat of the `E019` lineage. Empty ⟹ every
\(\mathcal G\)-member has order \(\ge22\) and (with `L041`/`L047`
propagation, to be re-derived at harvest) the tight-1-atom floor
moves; nonempty ⟹ members analysed per the `C043` protocol
(spectrum, tautness, \(S\)-condition, T5/`L049` constructive check).

## Environment

- Instrument: `E019/scan.py` + `genc48`, reused by path import through
  `E022/ladder.py`'s `load_scan` (its no-side-effect guarantees:
  `sys.dont_write_bytecode`, before/after listing of `E019/data`,
  DATA rebound to `E024/data` before any command). Neither `E019` nor
  `E022` is written.
- PyPy 7.3.23; 16 parts `r/16`, 8 concurrent workers;
  `--verify-all` on throughout; projected \(\approx\)21 h wall from
  the recorded \(\times8.25\) order-20 growth (74,188 CPU-s at 20).
- Anchors: the 146-check suite is re-passed through the same import
  path as stage 0 of the driver, before any production part
  (process rule); the run aborts if the gate fails.

## Reproduction

```sh
pypy3 rung21.py            # full pipeline: anchors gate -> 16 parts -> harvest + spotcheck
pypy3 rung21.py part 0/16  # a single part (what the pipeline spawns)
```

Outputs land in `data/`: `scan_n21_part*of16.json`,
`class_n21_part*of16.txt`, the harvest and spotcheck files, and
`rung21_status.json` (live stage status; `run21.log` the part log).

## Results

**RUNNING at S023 close.** This section is to be completed by the
harvesting session; per the parallel-session rules the leg is excluded
from every ledger until then (`STATE.md`/`problem.json` record it as
launched and not citable). The harvesting session must: check
`rung21_status.json` for the anchor-gate pass and per-part return
codes, re-verify the harvest assertions, spotcheck, and only then
write claims.

## Interpretation

None until harvested.

## Independent checks

To be recorded at harvest (the `C043` protocol: independent unsplit
count or dual-split partition check if the rung is nonempty at the
profile level; brute-force spectrum re-verification of near-boundary
members; T5/`L049` constructive check on any profile member).
