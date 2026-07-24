# E008 — Non-abelian lift certificates: solvable cascade probes and A5

- Date: 2026-07-23
- Problem: `P-002`
- Evidence class: exhaustive per-assignment certificate computation over
  finite groups given by verified multiplication tables
- Supports: attempt `A009`, claim `C022`

## Question

`A008`/`L021` killed every abelian voltage group. `A009` asks: does the
L019 walk certificate survive over non-abelian groups? Pre-registered
predictions: solvable groups fall to the iterated-commutator /
exponent-law cascade (order 21 dead by length 32; the exponent-3
Heisenberg group dead by 16); the perfect group \(A_5\) is immune to
both mechanisms and is the live test.

## Inputs and search space

Groups (all constructed as multiplication tables and fully axiom-checked
at runtime): \(\mathbb{Z}_7\rtimes\mathbb{Z}_3\) (order 21, metabelian),
Heisenberg mod 3 (order 27, exponent 3, class 2),
\(\mathbb{Z}_9\rtimes\mathbb{Z}_3\) (order 27, exponent 9), \(A_5\)
(order 60, perfect), plus cyclic groups for anchoring. Bases: the three
cycle-rank-2 bases (theta3, dumbbell, bouquet2), plus \(K_4\) for the
solvable groups. Every voltage assignment in \(\Gamma^\mu\) is tested
(no sampling); non-simple lifts are excluded by explicit preconditions
(loops: \(c\ne e\), \(c^2\ne e\); two loops at a vertex: \(d\notin\{c,
c^{-1}\}\); parallel edges: pairwise distinct voltages including the
tree's \(e\)).

The certificate is the group-agnostic form of `L019`: the lift has no
\(L\)-cycle if no tailless non-backtracking closed walk of length \(L\)
in the base has ordered net voltage \(e\). Computed by a synchronized
dynamic program over states (start arc, current arc, group element),
start arcs restricted to non-tree arcs (valid because a tailless
non-backtracking closed walk cannot lie in a forest, rotations preserve
the tailless property, and \(e\) is conjugation-invariant, so rebasing
is harmless).

## Results

`data/probes-mu2-bases.txt` (cycle-rank-2 bases, all five groups) and
`data/probes-k4-solvable.txt` (\(K_4\), solvable groups). Summary —
`first_hit` counts simple assignments by the first power length at
which the certificate fails:

- **Order 21** (prediction: dead \(\le32\)): every simple assignment on
  theta3, dumbbell, bouquet2, \(K_4\) dies by **16**.
- **Order 27, both groups** (prediction: Heisenberg dead \(\le16\)):
  every simple assignment dies by **16**.
- **\(A_5\)** (immune to the cascade; certificate lengths through 64 at
  lift order 120): every one of the 3600 assignments on each
  cycle-rank-2 base dies by **16**.
- **Zero survivors anywhere.**

The \(A_5\) result identifies the true obstruction, since neither the
derived series nor an exponent law applies: it is the **collision
wall**. Non-backtracking walks of length \(L\) from a vertex number
\(\gtrsim 3\cdot2^{L-1}\) on a cubic base while carrying only
\(\lvert\Gamma\rvert\) possible voltages; once \(2^{L-1}\gg
\lvert\Gamma\rvert\), two same-voltage walks exist, and composing one
with the reverse of the other yields an identity-voltage tailless
non-backtracking closed walk of length \(2L\) (arc-diversity
bookkeeping aside — see scope). This predicts certificate death at
\(2^k\approx2\log_2\lvert\Gamma\rvert\), which matches every observed
first-hit table: death by 16 at group orders 21–60 across all bases and
all five groups, with structured earlier deaths (4 and 8) where
short relations exist.

## Logical scope

All results are certificate-level: they prove that no voltage
assignment over these groups on these bases can be *walk-certified*
power-of-two-free, hence the sieve can produce no counterexample
candidate from them. They do not prove the lifts contain power cycles.
The collision-wall explanation is stated here as a mechanism matching
the data, with the composition construction explicit but its
arc-diversity bookkeeping not yet a proved general lemma — that proof
is the refined `G012` target; nothing in the ledger cites it as proved.
The solvable-cascade kill words (double commutators, power-twisted
commutators) were pre-registered predictions in `A009` and are
confirmed by the data at or before the predicted lengths; they are
likewise not promoted as general lemmas.

## Method and code

`nasieve.py`, standard library only; imports bases and the E007 module
for anchoring, `E004` detectors for ground-truth spot checks. Group
constructors build multiplication tables; `Group.check_axioms` verifies
identity, inverses, and full associativity (\(O(n^3)\) table lookups)
for every group used, and structure checks verify: order-21 group
non-abelian with commutator closure of size 7; Heisenberg non-abelian,
commutator closure 3, exponent 3; \(\mathbb{Z}_9\rtimes\mathbb{Z}_3\)
commutator closure 3 with an element of order 9; \(A_5\) non-abelian,
perfect (commutator closure 60), element orders \(\{1,2,3,5\}\).

## Environment

- Tool and version: PyPy 7.3.23 (Python 3.11.15), macOS 26.5.1 arm64;
  anchors also pass under CPython 3.14.2
- Dependencies: Python standard library; `E007/lifts.py` (bases, walk
  vectors, cyclic lift builder), `E004` detectors
- Exact arithmetic / floating point: exact integer arithmetic throughout
- Random seed: none (fully deterministic)

## Reproduction

```sh
pypy3 nasieve.py anchors
pypy3 nasieve.py probe g21 theta3      # and dumbbell, bouquet2, k4
pypy3 nasieve.py probe heis3 theta3    # and dumbbell, bouquet2, k4
pypy3 nasieve.py probe g27b theta3     # and dumbbell, bouquet2, k4
pypy3 nasieve.py probe a5 theta3       # and dumbbell, bouquet2
```

## Interpretation

Kill trigger 5 of `A009` fired: \(A_5\) dies, and the obstruction is
neither the derived series nor an exponent law but the collision wall —
a group-size-versus-walk-count pigeonhole that applies to **every**
finite voltage group. Since a lift of order \(n_B\lvert\Gamma\rvert\)
must dodge power lengths up to that order while certificates die at
\(\approx2\log_2\lvert\Gamma\rvert\), the voltage-certificate program
as a counterexample generator is finished for all groups, not just
abelian ones. What survives: the collision-wall lemma as a sharply
posed, hand-provable target (refined `G012`), and its proof-side
reading — minimum degree 3 forces identity-voltage closed walks at
every even length past a logarithmic threshold — as quantitative input
to the interval-forcing route (`G007`).

## Independent checks

- Bidirectional cross-engine anchor: over cyclic groups (as tables),
  the per-assignment DP hit set equals the `E007` hyperplane predicate
  ("some walk-class vector orthogonal to \(x\) mod \(m\)") for **every**
  assignment and every power length \(\in\{4,8,16\}\), on theta3 and
  dumbbell at \(m\in\{5,7,9\}\).
- The dumbbell lift over \(\mathbb{Z}_5\), \(x=(1,2)\) (Petersen): hit
  set exactly \(\{8\}\) among lengths \(\{4,8\}\), matching Petersen's
  girth 5 and its 8-cycle; the explicit lift built from the group table
  equals the `E007` builder's graph, and the `E004` detectors confirm
  no \(C_4\) and a present \(C_8\).
- Full group-axiom verification (including \(O(n^3)\) associativity)
  and the structure assertions listed above for every group used.
- All anchors pass under both PyPy and CPython.
