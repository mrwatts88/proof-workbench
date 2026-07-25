# E028 — exhaustive chord-minimal Hamiltonian profile search with poison-savings pruning over the window

- Date: 2026-07-25
- Problem: `P-002`
- Evidence class: **exhaustive search after a proved reduction** (`A027` T1/T2),
  with an exact decision stage per survivor — the production instrument of
  session `S027`
- Owner: session `S027`. Owned experiment record; writes no ledger.

## Question

Decide, order by order, the Hamiltonian-stratum form of the forcing target (F):

> **(H-F).** Is there a simple graph \(H\) of order \(n\), with two vertices
> \(a,b\) of degree 2 and every other degree \(\ge3\), no \(C_4\) and no
> \(C_8\), carrying a **Hamiltonian \(a\)–\(b\) path**, such that
> \(S(H,a,b)\cap\{2,6,14,30\}=\emptyset\) **and**
> \(\mathrm{Spec}(H)\cap\{16,32\}=\emptyset\)?

A YES at any \(n\in[18,35]\) is a case-(5b) residual object: its 2-path
closure is a tight 1-atom (the standing disproof-adjacent pivot trigger). A
NO at order \(n\) closes case (5b) at that order for every residual object
with a Hamiltonian through-path — i.e. proves (F) there on that stratum.

Note the two deliberate strengthenings over the recorded (F-S)/(F-T) split
(`A025` T4): the search decides the **disjunction** (F) directly — which is
all `G015` needs and gives strictly more hypotheses — and it uses the whole
poison set \(\{2,6,14,30\}\) rather than \(\{6,14\}\), since \(30+2=32\) is
also a power (`L048`(iii)).

## Logical scope

Exhaustive **after a proved reduction**, per order, for the Hamiltonian
stratum only:

- `A027` **T1** (chord-minimal descent, proved): if a counterexample to
  (H-F) exists at order \(n\), then one exists whose chord set is an
  inclusion-minimal cover of the \(n\) path positions. So enumerating
  chord-minimal covers loses nothing.
- `A027` **T2** (monotone reroute, proved): interval-disjoint chord families
  realise real \(a\)–\(b\) paths, so a family with savings
  \(M-\ell\), \(\ell\in\{2,6,14,30\}\), kills the branch. The savings set is
  a left-to-right DP, so the test fires on prefixes.

Both are *necessary* conditions on a hypothetical dodger, so pruning by them
can only discard non-counterexamples. **Emptiness at an order is therefore a
proof at that order**; a survivor is only a candidate and is decided by the
exact stage (full \(a\)–\(b\) path enumeration for \(S\), cycle detection for
\(\mathrm{Spec}\cap\{16,32\}\)).

What is **not** covered: pairs whose longest \(a\)–\(b\) path is not
Hamiltonian (`A027` T5 — the named residue); orders above the last completed
rung.

## Environment

- CPython 3.14.2 and PyPy 7.3.23 (3.11.15); anchors under both, production
  under PyPy at `nice -n 15`, single process. `E024` (the order-21
  \(\mathcal G\) ladder rung) held 8 cores at nice 0 throughout and was never
  touched.
- Imports (read-only) the `E026` → `E021`/`E019`/`E018` chain by `E027`'s
  pattern: `g6_decode`, `g6_encode`, `degrees`, `bipartition`, `bfs_dist`,
  `has_cycle_len`, `count_cycles_len`, `paths_with_essential`,
  `canonical_set` (nauty `labelg`), `petersen_minus_e`, the census class
  files. `E026/data` is listed before and after the import and asserted
  unchanged; every output path is rebound to `E028/data`.
- New code: the chord-minimal cover enumerator, the savings DP, the
  incremental forbidden-cycle tests, the independent brute-force reference
  enumerator, the independent path-length enumerator, certification.
- Stdlib only; fully deterministic (no randomness, no sampling); wall clock
  in timing fields only.

## Inputs and search space

For each \(M\) (path length; order \(n=M+1\)) the enumerator walks positions
\(0,1,\dots,M\) left to right and decides, at position \(p\), the set of
chords \((p,q)\) with \(q>p\). Constraints, all enforced exactly:

- coverage — \(\deg_{\mathcal C}(p)\ge1\) for \(0<p<M\) and
  \(\deg_{\mathcal C}(0)=\deg_{\mathcal C}(M)=1\);
- minimality — every chord has an endpoint of chord-degree 1, propagated
  forward as a *reservation* the moment a surplus chord is placed;
- class — no \(C_4\) and no \(C_8\) in \(P+\mathcal C\), tested through each
  newly added chord (every cycle of \(P+\mathcal C\) uses a chord, so this is
  exact, not a hand-derived pair table — `A027` T6 records a hand-table entry
  that was wrong and would have been used had the table been trusted);
- poison — the prefix savings set \(R_p\) must avoid
  \(\{M-2,M-6,M-14,M-30\}\cap[0,M]\);
- one symmetry break — reversal \(p\mapsto M-p\), enforced as
  span(chord at 0) \(\le\) span(chord at \(M\)).

\(M\in\{2,6,14,30\}\) needs no search: \(\max S=M\) is itself poison.

## Reproduction

```sh
python3 search.py anchors                    # 80,131 checks, CPython
pypy3   search.py anchors                    # 80,131 checks, PyPy (identical histogram)
nice -n 15 pypy3 search.py search 15 25      # run A: {C4,C8} only
nice -n 15 pypy3 search.py search 15 34 c16  # run B: the (F) hypothesis
nice -n 15 pypy3 search.py certify search_15_25.json   # independent re-check
```

Outputs in `data/`: `anchors_search_{cpython,pypy}.json`,
`search_15_25.json` and `search_15_34_c16.json` (per-order verdicts, prune
tallies, survivors), `production.log`, `production_c16.log`,
`certificates.json`.

## Anchors — 80,131 checks, both interpreters, identical check histograms

Families **a6** and **a7** were added *after* the delegated audit `R003`,
which found that the original suite, though large, never exercised any of
the three loss-capable prunes on a positive or nonempty instance (`R003`
F1/F2). They are the repair, and they are the checks the verdict actually
rests on.

- **a1** cycle-detector micro-tests, including the corrected chord-pair
  geometry (interior-disjoint chords close **no** extra cycle; crossing at
  offset 1 gives \(C_4\), at offset 3 gives \(C_8\); nested and
  shared-endpoint \(C_8\) witnesses), plus **45,683** agreement checks
  between the generic through-edge detector and the fast production
  specialisation and **32,570** agreement checks between per-chord
  detection and the independent whole-graph detector `has_cycle_len`
  (every cycle of \(P+\mathcal C\) uses a chord, so the two must agree
  exactly), over every system the enumerator builds at \(M=9,10,11\) and
  every cycle length in \(\{4,5,6,8,16\}\).
- **a2** the savings DP against explicit enumeration of interval-disjoint
  families on fixed systems, **and** the soundness of T2: every DP-generated
  length is asserted to be a genuine \(a\)–\(b\) path length.
- **a3** the enumerator against the independently written `brute_force`
  (different traversal, different cycle detector, different savings routine,
  no symmetry breaking, no minimality propagation): exact set equality at
  \(M=6..12\) with the poison prune under \(\{C_4,C_8\}\), at \(M=6..12\)
  under the **production** setting \(\{C_4,C_8,C_{16}\}\), at \(M=6..11\)
  without the poison prune, and — the **nonempty positive controls** — at
  \(M=6..10\) with only \(C_4\)-freeness (counts 0/1/11/80/660) and at
  \(M=6..10\) with \(\{C_4,C_{16}\}\). Symmetry breaking is verified to be
  exactly reversal-closure at \(M=6..12\).
- **a4** the eight profile objects: each is decoded, its degree profile,
  \(S\), \(\max S=n-1\) and Hamiltonian \(a\)–\(b\) path re-derived; the span
  law re-asserted; the chord set verified to be a cover; the first-order
  savings verified to hit the poison targets (reproducing `C047`(f)); and
  every minimal subcover verified to be again an exactly-two
  \(\{C_4,C_8\}\)-free member with an invariant signature in the recorded
  set. All eight turn out to be **already chord-minimal** (one subcover
  each).
- **a5** the calibration pair: Petersen\(-e\) has \(S=\{4,5,7,8\}\) and — the
  binding fact — **no Hamiltonian \(a\)–\(b\) path**, so it is outside the
  stratum by a named hypothesis; the order-14 exemplar has
  \(S=[3,13]\setminus\{6\}\), *is* Hamiltonian and exactly-two, and is
  excluded only because it carries \(C_8\)s. The order-19 member is confirmed
  \(C_{16}\)-carrying.
- **a6 (repair for `R003` F2) — the \(C_{16}\) detector on positive
  instances.** Run B's whole table is produced by the \(L=16\) branch of the
  production detector, a depth-15 search that a1 never drives to `True` (a1
  runs at order \(\le12\), where no \(C_{16}\) exists). a6 drives it at every
  path length \(M=15..34\): single chords of span 15 (chord + arc = \(C_{16}\));
  span-14 and span-16 chords as negatives; crossing pairs whose interference
  cycle is a \(C_{16}\); a deterministic multi-chord family compared across
  **three** detectors (production fast path, generic through-edge, and the
  imported whole-graph `has_cycle_len`) at \(L\in\{4,8,16\}\), including the
  "every cycle uses a chord" equivalence; and the eight profile objects,
  which carry 46–130 \(C_{16}\)s each. **539 positive and 63 negative
  \(C_{16}\) instances** across \(M=15..34\), zero disagreements between the
  three detectors. (The audit's own independent test — a third, set-based
  detector on 6,927 positive instances at \(M=15..22\) and 15,072 more at
  \(M=26..34\) — likewise found zero mismatches; that test is recorded in
  `R003`, not reproduced here.)
- **a7 (repair for `R003` F1) — the loss-capable prunes on nonempty sets.**
  The a3 comparisons are structurally empty-vs-empty, because the
  \(\{C_4,C_8\}\)-free chord-minimal class is itself empty below order 19.
  a7 runs inside the real class, where it is not: at orders 19 and 20, the
  symmetry-broken enumeration is checked to be **exactly** the reversal
  closure of the full one (6 vs 12 and 65 vs 102 covers); the savings DP is
  checked against explicit family enumeration on all 114 of those covers;
  and switching the poison prune on is checked to select **exactly** the
  covers whose savings miss the targets. Plus the full production
  configuration (symmetry **on**, poison **on**) against the independent
  reference on nonempty sets, class \(\{C_4\}\), \(M=8..11\).

## Cross-check against the recorded ladder (binding)

With the poison prune switched **off**, the enumerator counts chord-minimal
covers by order — an independent generation principle (chord-minimal covers
of a Hamiltonian path) against `C039`/`C043`'s geng + \(C_8\)-prune plugin:

| order \(n\) | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|
| chord-minimal covers | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 65 |

(`data/crosscheck_nopoison.json`; reproduced identically before and after
the minimality-reservation optimisation was added to the enumerator, the
second time \(14\times\) faster.)

Empty through 18 — the recorded emptiness of the exactly-two
\(\{C_4,C_8\}\)-free class (`C027`/`C039`/`C043`) — and at orders 19 and 20
the outputs reproduce the recorded profile objects **exactly, at
isomorphism level**: canonical forms (nauty `labelg`) of the 6 and 65 covers
give **1** and **7** classes, set-*equal* to the canonical forms of the 1 and
7 recorded objects. Nothing unrecorded appears, and nothing recorded is
missed. (An earlier draft said "four signatures" at order 20; that counted
\((n,\text{edges},\text{degree sequence},S)\) tuples, not isomorphism
classes — `R003` F7.)

## Results, run A — the \(\{C_4,C_8\}\)-only ladder (the (F-S) stratum)

Class constraint \(\{C_4,C_8\}\) only; \(C_{16}\)/\(C_{32}\) handled at the
exact stage. Survivors here are genuine \(\mathcal G\)-profile members with a
Hamiltonian \(a\)–\(b\) path on which the *first-order* calculus misses the
poison.

| \(M\) | order | savings targets | survivors | nodes | wall | exact-stage verdict |
|---|---|---|---|---|---|---|
| 15 | 16 | 13, 9, 1 | 0 | 10,345 | 0.4 s | — |
| 16 | 17 | 14, 10, 2 | 0 | 52,391 | 0.5 s | — |
| 17 | 18 | 15, 11, 3 | 0 | 145,178 | 1.1 s | — |
| 18 | 19 | 16, 12, 4 | 0 | 413,945 | 3.4 s | — |
| 19 | 20 | 17, 13, 5 | 0 | 1,374,926 | 11.8 s | — |
| 20 | 21 | 18, 14, 6 | **10** | 4,860,618 | 43.0 s | all killed twice: \(6,14\in S\), \(C_{16}\) present |
| 21 | 22 | 19, 15, 7 | **43** | 17,076,872 | 154.0 s | all killed twice: \(14\in S\) (30 also \(6\in S\)), \(C_{16}\) present |

Run A was stopped after \(M=21\) (its tree grows \(\approx\times3.5\) per
order and run B supersedes it). Certification of all 53 survivors:

- order 21: 10 systems, **3 up to isomorphism**, all 2-connected, girth 3,
  \(\min S\in\{3,5\}\), \(S\) a **full interval** \([\min S,20]\),
  95–130 \(C_{16}\)s;
- order 22: 43 systems, **16 up to isomorphism**, all 2-connected, girth 3,
  \(\max S=21\) throughout, 91–186 \(C_{16}\)s, and through-set shapes
  \([3,21]\) (2), \([4,21]\) (6), \([5,21]\) (14), \([6,21]\) (8),
  \([5,21]\setminus\{6\}\) (8), \(\{1,5\}\cup[8,21]\) (5, adjacent
  terminals).

These are the **first \(\mathcal G\)-profile objects ever exhibited at orders
21 and 22** in this dossier, and the 13 holed ones are the first in-window
exactly-two objects whose through-set is *not* a full interval — a genuine
refinement of the `A025` T3 saturation reading, which held on 8/8 objects.
Every one of the 53 still carries \(14\in S\) **and** a \(C_{16}\): the double
blocking is unbroken.

## Results, run B — the \((F)\)-hypothesis ladder (\(\{C_4,C_8,C_{16}\}\))

Adding \(C_{16}\)-freeness is not a strengthening of the target: it is the
second half of (F)'s negation, so run B decides (H-F) exactly, and by `A027`
T1 the descent still applies (freedom from a cycle length is hereditary).
It collapses the tree by \(7\times\) at order 19 rising to \(27\times\) at
order 21, and cuts the **node** growth rate from \(\approx\times3.5\) to
\(\approx\times1.9\) per order.

| \(M\) | order | savings targets | survivors | nodes | wall | poison-prune kills |
|---|---|---|---|---|---|---|
| 15 | 16 | 13, 9, 1 | 0 | 8,924 | 0.5 s | 1,445 |
| 16 | 17 | 14, 10, 2 | 0 | 26,080 | 0.6 s | 982 |
| 17 | 18 | 15, 11, 3 | 0 | 38,362 | 1.0 s | 880 |
| 18 | 19 | 16, 12, 4 | 0 | 61,040 | 1.7 s | 1,234 |
| 19 | 20 | 17, 13, 5 | 0 | 108,068 | 3.4 s | 738 |
| 20 | 21 | 18, 14, 6 | 0 | 182,613 | 6.5 s | 61 |
| 21 | 22 | 19, 15, 7 | 0 | 323,622 | 13.1 s | 33 |
| 22 | 23 | 20, 16, 8 | 0 | 634,125 | 28.6 s | 45 |
| 23 | 24 | 21, 17, 9 | 0 | 1,204,578 | 61.4 s | 17 |
| 24 | 25 | 22, 18, 10 | 0 | 2,164,278 | 116.4 s | 2 |
| 25 | 26 | 23, 19, 11 | 0 | 3,945,231 | 216.2 s | 1 |
| 26 | 27 | 24, 20, 12 | 0 | 7,577,405 | 504.0 s | **0** |
| 27 | 28 | 25, 21, 13 | 0 | 14,415,162 | 1220.0 s | **0** |
| 28 | 29 | 26, 22, 14 | 0 | 26,421,019 | 2200.5 s | **0** |

**Two disclosures the audit `R003` forced, both important.**

**(a) The ladder is an open-ended computation, not a window closure**
(`R003` F3(b)). The \(\times1.9\) figure above is the *node* ratio; the
*wall-clock* ratio is worse and worsening (2.15, 1.90, 1.86, 2.33, 2.42,
1.80 at \(M=23\ldots28\)) because per-node cost grows with graph size. On
that trend orders 30–35 are days of single-core computation, not hours. The
record states the **last completed rung** and claims nothing above it; the
earlier phrasing "brings the whole window into range" was an extrapolation
from node counts that the timing data does not support and has been
withdrawn.

**(b) Above order 26 the verdict is class-emptiness, not poison forcing**
(`R003` F4). The poison prune's branch kills fall away entirely — 61, 33,
45, 17, 2, 1, **0, 0, 0** at \(M=20\ldots28\) — so from \(M=26\) on the
search tree *with* the poison test is identical to the tree without it.
What run B proves at orders 27, 28 and 29 is therefore the **stronger**,
poison-free statement:

> there is no \(\{C_4,C_8,C_{16}\}\)-free graph at that order with exactly
> two degree-2 vertices, all other degrees \(\ge3\), and a Hamiltonian
> \(a\)–\(b\) path — whatever its through-set.

That implies (F) there a fortiori, but it exercises none of (F)'s forcing
mechanism, so no inference about *why* the poisons appear is supported above
order 26. It also amends `A027` T4's survivor-growth expectation: that
prediction is about run A (where it holds), not run B.

*(the run continues toward \(M=34\); rungs completed after session close are
excluded from every ledger row until harvested)*

## Interpretation

Narrowest justified conclusions.

1. **(H-F) holds at every order run B has decided.** No
   \(\{C_4,C_8\}\)-free graph with exactly two degree-2 vertices and a
   Hamiltonian \(a\)–\(b\) path, at any such order, escapes both the poison
   lengths \(\{2,6,14,30\}\) and the power cycles \(\{16,32\}\). Orders
   \(\le20\) agree with the census (`C046`) and the ladder (`C043`); every
   order from 21 up is **new**. This is (F) on the Hamiltonian stratum, so
   case (5b) is closed there at those orders.
2. **The first order-21 and order-22 \(\mathcal G\)-profile objects are
   exhibited** (run A). They are genuine \(\{C_4,C_8\}\)-free graphs with
   exactly two degree-2 vertices — the first ever produced at those orders
   in this dossier — and every one repeats the recorded **double
   blocking**: \(14\in S\) and a \(C_{16}\) present. *(They are Hamiltonian
   and first-order-dodging, so they are not the whole profile class at those
   orders; the `E024` rung decides that for 21.)*
3. **Saturation is not the mechanism.** All eight previously known profile
   objects had \(S\) equal to the full interval \([\min S,n-1]\) (`A025`
   T3), and so do all ten order-21 objects — but **13 of the 43 order-22
   objects do not**: 8 have \(S=[5,21]\setminus\{6\}\) and 5 have adjacent
   terminals with \(S=\{1,5\}\cup[8,21]\) (holes at \(\{2,3,4,6,7\}\)). So
   the interval reading that had been
   guiding the (F-S) attack is false in-window, at the first order where it
   could be tested — and yet the conclusion of (F) survives on every one of
   them, because they still carry 14 and a \(C_{16}\). Any future
   mechanism must explain 14 and 16 specifically, not \(S\) as a whole.
4. **The first-order calculus is provably weak at large \(M\)** (`A027` T4):
   the binding target is savings \(M-14\), so the monotone prune loses grip
   as \(M\) grows, and run A's survivors appear from \(M=20\) on. That is a
   statement about the *prune*, not about the objects — the exact stage
   killed every survivor by a wide margin. Run B does not suffer from it,
   because \(C_{16}\)-freeness prunes on structure rather than on length.
5. **The profile hypothesis is consumed exactly where `C047` says it must
   be.** Coverage of every path position by a chord is the profile's whole
   contribution; the 36 Hamiltonian corpus dodgers have \(\ge7\) degree-2
   vertices and their chord systems do not cover, so they are not inputs to
   this search — and neither calibration object survives its named
   hypothesis (Petersen\(-e\): no Hamiltonian \(a\)–\(b\) path; the order-14
   exemplar: carries \(C_8\)s).
6. **Scope caveats.** Nothing here bears on residual objects whose longest
   \(a\)–\(b\) path is not Hamiltonian (`A027` T5), on orders above the last
   completed rung, or on statement 0.1 itself. Run B's enumeration grows by
   \(\approx\times1.9\) per order, which is what bounds the reach; run A's
   by \(\approx\times3.5\).

## Independent checks

- Anchors under both interpreters, 78,507 checks each, identical check lists
  and identical recorded payloads.
- The enumerator is set-equal to an independently written brute-force
  enumeration wherever the latter is feasible, including nonempty controls.
- Every survivor is re-certified by `certify`: degree profile and
  \(\{C_4,C_8\}\)-freeness re-tested with the whole-graph detector
  `has_cycle_len`; \(S\) recomputed by a **second, independent** plain-DFS
  path enumerator and asserted equal to the `E018` enumerator's answer;
  \(C_{16}\) counted; 2-connectivity, bipartiteness and girth recorded;
  canonical forms via nauty `labelg` for the isomorphism count.
- The no-poison counts at orders \(\le20\) are checked against the recorded
  ladder and census figures, from an independent generation principle.
- **Delegated adversarial audit `R003`** (fresh-context `proof-reviewer`,
  independence mode `delegated-subagent`): **PASS at lemma-and-instrument
  level**, 0 critical / 4 major / 4 minor / 3 notes. The reviewer re-ran the
  shipped instrument outside the repository and reproduced run A
  \(M=15..21\) and run B \(M=15..23\) node counts **to the last digit**, and
  wrote its own enumerator from scratch (python sets not bitmasks,
  from-scratch cycle detection, explicit family enumeration for savings, no
  reservation propagation, no symmetry break) that is set-equal to `Search`
  on every case it ran including a 6,356-member nonempty control, and that
  independently returns the empty set for the run-B configuration at orders
  19–25. Every major finding is answered here: F1 and F2 by the new anchor
  families a6/a7; F3 by stating the last completed rung and withdrawing the
  window-reachability extrapolation; F4 by the class-emptiness disclosure
  above.
- **Dependency hygiene** (`R003` F9): run B's verdict uses **only**
  E028-local code — no imported `E018`/`E019` primitive enters it. Run A's
  *exact stage* does use the imported `paths_with_essential` (cross-checked
  there against this file's own independent path enumerator).
- **Provenance** (`R003` F5): `search.py` was edited during the session. The
  `Search` class and `cmd_search` were frozen before run A launched and were
  not touched again; all later edits are confined to `cmd_anchors` (the a3
  \(C_{16}\) comparisons, compact anchor storage, and the post-audit a6/a7
  repair). `search_15_25.json` therefore lacks the `forbidden` key that the
  current code writes — that key was added, together with the `c16`
  argument, between run A and run B. A superseded third revision's log was
  deleted rather than kept unlabelled. The audit re-ran the shipped code and
  reproduced both runs, which is the check that actually settles this.
- Not independently re-derived: the imported `E026`/`E019`/`E018`
  primitives and the class files (inherited at recorded strength).
