# E009 — Collision-wall construction verification

- Problem: `P-002`
- Attempt: `A010` (Theorem W7 and supporting lemmas W1–W6)
- Created: 2026-07-24 (session `S010`)
- Tool: `wall.py`, Python 3.14.2 (CPython), exact integer arithmetic, no
  randomness

## Purpose

Mechanically verify every ingredient of the collision-wall proof on
concrete instances. This is a consistency check of the proof's steps and
constants, not a proof: the theorem quantifies over all bases and groups,
and only the listed finite instances are tested here.

## What is checked

1. **W1/W3 (structure).** For each base (theta3, dumbbell, bouquet2,
   \(K_4\), \(K_{3,3}\), prism): every arc-digraph state has out-degree
   \(\ge2\), and the digraph is strongly connected (forward and backward
   BFS from a root reach all \(2m\) states).
2. **W4 (period).** The digraph period computed by BFS-layer gcd is in
   \(\{1,2\}\), equals 2 exactly for the bipartite bases (theta3,
   \(K_{3,3}\)) — matching the pre-registered expected values — and the
   tail-side class advances by one along every transition.
3. **W5 (reach constant).** `R_B` is computed as the least \(R\) such
   that every ordered arc pair is connected by an exact-length path at
   every admissible length in \([R,200]\); the tail is required to be
   stable for at least 50 consecutive lengths below the horizon.
   Measured: theta3 2, dumbbell 4, bouquet2 2, \(K_4\) 6, \(K_{3,3}\) 4,
   prism 6.
4. **W6 (seed).** The pigeonhole seed search at length
   \(\ell^*=\lfloor\log_2(2m\lvert\Gamma\rvert)\rfloor+2\) always finds a
   collision, and the trimmed pair satisfies all five seed properties
   (asserted directly).
5. **W7 (construction).** For every base × every group (Z5, Z7, Z9,
   \(Z_7{\rtimes}Z_3\), Heisenberg mod 3, \(Z_9{\rtimes}Z_3\), \(A_5\);
   multiplication tables axiom-checked including full associativity) ×
   five deterministic assignments (identity, constant, all-distinct,
   two affine patterns): the assembled walk
   \(\Omega=U\cdot\mathrm{rev}(Y)\cdot Y'\cdot\mathrm{rev}(U')\) is
   verified — by an independent definition-level checker on the raw arc
   list — to be non-backtracking cyclically (hence tailless), closed, of
   length exactly \(L\), and of identity net voltage, for a ladder of ten
   admissible lengths at the threshold \(4\ell^*+4R_B+8\) and for the
   first three powers of two above it (up to 512).
6. **Negative controls.** The checker rejects a backtracking pair, a
   non-closed pair, and a wrong-length walk.
7. **Cross-engine anchor.** For (theta3, dumbbell, bouquet2) × (Z5, Z7,
   \(Z_7{\rtimes}Z_3\)) samples, the independent `E008` per-assignment DP
   reports certificate failure at every power of two above the theorem's
   threshold that lies in its range (64), for every simple tree-gauge
   assignment sampled — existence agreeing between two structurally
   different algorithms.
8. **Exhaustive arms** (`--exhaustive`). All \(5^3=125\) Z5-assignments
   on theta3 and on the dumbbell, all \(25\) on bouquet2, and all
   \(5^6=15{,}625\) on \(K_4\), each at 4–7 admissible lengths including
   a power of two: 64,425 constructions, all verified.

Final run: **all checks passed (9,606,333 assertions)**.

## Reproduce

    python3 wall.py               # standard sweep
    python3 wall.py --exhaustive  # adds the exhaustive small sweeps (~2 min)

## Logical scope

- Verification covers six bases, seven groups, and the listed
  assignments and lengths; the theorem's universal claims rest on the
  proofs in `A010`, not on this experiment.
- `R_B` here is the *empirical* reach constant with a stable-tail
  requirement; W5 proves such a constant exists but gives no formula.
  The construction only ever uses lengths \(\ge R_B\) at which the
  exact-length DP succeeded, so no unverified reachability is assumed.
- The cross-engine anchor tests existence agreement only at powers within
  the E008 DP's range; it is an anchor, not an independent proof.
- Base and group data are imported from `E007`/`E008` and re-checked at
  load (group axioms; expected periods pre-registered in the script).
