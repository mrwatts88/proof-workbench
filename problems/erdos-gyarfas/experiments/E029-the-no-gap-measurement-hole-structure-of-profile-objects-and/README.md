# E029 — the no-gap measurement: hole structure of profile objects and the corpus violation frontier by degree-2 count

- Date: 2026-07-26
- Problem: `P-002`
- Session: `S030`
- Attempt: `A028` T9
- Evidence class: exhaustive over the recorded objects; a complete re-reading
  of an existing corpus. **Nothing is generated** — no new graph class, no new
  ladder rung.

## Question

`A028` T9 formulates the successor target to `A026` T7's (L-A)/(L-B) split:

> **(INT) — the no-gap conjecture.** For a vertex-taut \(\{C_4,C_8\}\)-free
> exactly-two-profile pair \((H,a,b)\), \(S(H,a,b)\supseteq[\,8,\max S\,]\).

Two measurements, both from data already on disk:

- **(A) Does (INT) hold on every recorded profile object, and which hole values
  occur at all?** The profile objects whose graph6 strings are stored are the
  19 order-21 members (`E024`), the 4 order-20 part-14 members (`E022`), and
  the order-19 first-ever member (`C043`) — 24 objects. \(S\) is recomputed
  from the graph6 string by exact path enumeration, not read from a summary.
- **(B) Where is (INT) first false?** The `E027` near-miss corpus (9,061
  vertex-taut gapped pairs, every one with \(\ge4\) degree-2 vertices) stores a
  per-row hole list and degree-2 count. For each hole value, the minimum
  degree-2 count at which that hole occurs is the margin between the profile
  and the nearest recorded refutation.

## Logical scope

- (A) is **exhaustive over the stored profile objects** and re-derives every
  class condition per row. It is not exhaustive over all profile objects in
  existence: three of the eight order-19/20 objects (`C043`) are not stored as
  graph6 and are not re-checked here; their \(S\) sets are recorded as
  saturated (\(\supseteq[6,n-1]\), `A025` T3), which implies (INT).
- (B) is **exhaustive over the recorded corpus**, which is itself the complete
  set of vertex-taut gapped pairs over the on-disk classes at orders 10–20
  (order 20 sampled per `C046`). Absence of a hole value at a given degree-2
  count therefore means "not in the corpus", not "impossible".
- Neither measurement can prove (INT). A violation on a profile object would
  **disprove** it; none occurs.

## Environment

- `pypy3` 7.3.x and CPython 3.14.2 (both run; identical output).
- Primitives imported verbatim from `E019/scan.py` (`g6_decode`, `degrees`,
  `profile_pair`, `path_lengths`, `has_c4`, `from_edges`, `g6_encode`) — the
  arm64 build the dossier has always trusted, anchored as recorded in `C039`.
- Exact integer arithmetic throughout; no floating point, no randomness.

## Inputs and search space

- `E024/data/profile_n21_mod144_merged.txt` — 19 order-21 profile members.
- `E022/data/profile_n20_part14.g6` — 4 order-20 profile members.
- The order-19 member `R???C@?GC_B?@_aAA_aP?W_?BO@Gc?`, transcribed from
  `STATE.md`/`C043` and round-trip checked.
- `E027/data/corpus_rows_compact.json` — the 9,061-row near-miss corpus.
- Calibration objects for the anchors: Petersen\(-e\) (built from an explicit
  edge list, not read from disk) and the order-14 object `M?AA@?WcKWHOWOL??`.

## Reproduction

```sh
cd problems/erdos-gyarfas/experiments/E029-the-no-gap-measurement-hole-structure-of-profile-objects-and
pypy3 nogap.py anchors      # 6 anchors, all reproducing recorded quantities
pypy3 nogap.py run          # writes data/nogap.json
python3 nogap.py run        # second interpreter, identical output
```

## Results

**Anchors (6, both interpreters, all pass).** Each reproduces a quantity
recorded independently of this experiment: Petersen\(-e\)'s \(S=\{4,5,7,8\}\)
and non-Hamiltonicity (`C037`); the order-14 calibration object's single hole
at 6 and its Hamiltonicity (`A025` T3, `A027`); the order-19 member's
\(S=[5,18]\) exactly (`C043`); the order-21 rung's 19 members, all with
\(\max S=20\), exactly one with \(6\notin S\) and that one with \(\min S=4\)
(`C049`); the corpus's 9,061 rows (`C047`); graph6 round-trip on every object.

**(A) Profile objects — 24 checked, 0 (INT) violations.**

- Every hole occurring in any of the 24 lies in \(\{4,5,6\}\); **no hole
  anywhere at 7 or above**.
- Two of the 24 are gapped at all:
  - order 21, `T????A?O@?B?D??oQ?_KAoG?AoB?_@OO?LA?`: \(S=[4,20]\setminus\{6\}\)
    (the `C049` exception, reproduced);
  - order 20, `S????A?O@_@_?oIABODC?S@?@a?H_CA_?`: \(S=[3,19]\setminus\{4,5\}\)
    — **new**: a second non-interval profile object, at order 20. It is
    consistent with `A025` T3 (which asserts \(S\supseteq[6,n-1]\), not that
    \(S\) is an interval), and it strengthens the `S027` finding that
    saturation is not the mechanism: non-interval profile objects exist one
    order below where they were first seen.
- All 24 are \(C_4\)-free and Hamiltonian, re-derived per row.

**(B) The corpus violation frontier.** Minimum degree-2 count (`ndeg2`) at
which each hole value occurs anywhere in the 9,061 rows:

| hole value \(h\) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| min `ndeg2` | 4 | 4 | 4 | 4 | 4 | 4 | **5** | 7 | 6 | 8 | **7** |

- 1,920 of the 9,061 rows have a hole \(\ge8\); the smallest degree-2 count
  that admits one is **5**, and all six `ndeg2 = 4` rows (the corpus frontier,
  `C047`(b)) have holes confined to \([2,7]\).
- No hole above 14 occurs anywhere in the corpus.

## Interpretation

The narrowest justified conclusions, offered as `C050`:

1. **(INT) survives its first kill test.** It holds on every recorded profile
   object, and the objects are not close to violating it: their holes stop at
   6, two below the conjecture's threshold.
2. **The constant 8 is pinned from both sides.** Holes at every value
   \(\le7\) are realised at the corpus's minimum degree-2 count of 4; the first
   hole at 8 needs 5. So (INT) with any constant \(\le7\) is **false** on the
   near-miss frontier, and 8 is the smallest constant the data permits. This is
   a sharper calibration than `A026` T7's (L-B), which fixed no constant.
3. **The operative case has a five-vertex margin.** The value that matters is
   14 (it is poison, \(14\in\mathbb P-2\)), and no corpus row opens a hole at 14
   below `ndeg2 = 7` — five degree-2 vertices above the profile. The weakened,
   operative form
   > **(INT-14)** a vertex-taut \(\{C_4,C_8\}\)-free profile pair with
   > \(\max S\ge14\) has \(14\in S\)
   is therefore better supported than full (INT), and by `L048`(iii) it is all
   (F-S) needs.
4. **The profile hypothesis remains load-bearing**, as `C046`(b)/`C047`(b)
   said: (INT) is false without it (1,920 refutations on disk), so any proof
   must consume min degree \(\ge3\) off the terminals.

What this does **not** establish: (INT) at any order, for any object not on
disk. It is a conjecture with a kill test survived and a sharp constant, not a
lemma.

## Independent checks

- Two interpreters (PyPy and CPython), identical output including the full
  per-row \(S\) sets.
- \(S\) is recomputed from graph6 by exact path enumeration rather than read
  from `C043`/`C049` summaries, and independently agrees with them on every
  recorded field (the a3/a4 anchors are exactly this comparison).
- Petersen\(-e\) is built from an explicit edge list inside this instrument,
  not read from any stored file, so the a1 anchor is independent of the
  dossier's data layer.
- The corpus half re-derives the hole lists' consequences from `E027`'s stored
  rows; the stored rows were themselves produced by `E027` with its own
  anchors (35 checks, both interpreters) and cross-validated against the
  independent `E026` enumerator.
- Every graph read round-trips through `g6_encode(g6_decode(·))`.
