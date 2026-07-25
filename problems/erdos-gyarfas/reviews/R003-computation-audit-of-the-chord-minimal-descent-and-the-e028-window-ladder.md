# R003 — Computation and reduction audit of the chord-minimal descent and the E028 window ladder

- Date: 2026-07-25
- Problem: `P-002`
- Reviewed statement version: 0.1 (main statement unchanged; the review
  target is the lemma-level reduction offered as `L052` and the
  computational verdict offered as `C048`)
- Reviewed revision: `attempts/A027-…md` deductions T1–T6 and
  `experiments/E028-…/search.py` + `README.md`, as of session `S027`,
  before ledger promotion
- Review type: computation — logic / hypotheses / counterexample / computation / exposition
- Independence mode: delegated-subagent
- Note: created manually because `proofctl.py review` gates on a
  main-statement proof candidate; this is a lemma-plus-computation audit and
  the main claim status is unchanged (`open`). Same exception as `R001`/`R002`.

## Target identification

The claims under audit, verbatim from `A027`:

- **T1 (chord-minimal descent)** — for a graph \(H\) with exactly two
  degree-2 vertices \(a,b\), all other degrees \(\ge3\), and a Hamiltonian
  \(a\)–\(b\) path \(P\), the chord set covers every path position (0 and
  \(M\) exactly once), and every inclusion-minimal subcover \(\mathcal C'\)
  yields \(H'=P+\mathcal C'\) with the same degree profile, the same
  Hamiltonian path, \(\mathrm{Spec}(H')\subseteq\mathrm{Spec}(H)\),
  \(S(H')\subseteq S(H)\), and every chord having an endpoint of chord-degree 1.
- **T2 (monotone reroute)** — interval-disjoint chord families realise
  genuine \(a\)–\(b\) paths of length \(M-\sum(\text{span}-1)\), and the
  reachable-savings set is the stated left-to-right DP.
- **T3 (what the search decides)** — the combination: an empty enumeration
  at order \(n\) proves (H-F) at that order; a survivor is only a candidate.
- **T6** — the correction to the hand-derived chord-pair table (interior-
  disjoint chords close no extra cycle).
- **The instrument** `E028/search.py`: whether the enumerator is exhaustive
  over chord-minimal covers, whether every prune is sound (one-sided), and
  whether the symmetry break loses solutions.
- **The verdict `C048`**: the per-order emptiness table of run B and the
  survivor certification of run A.

## Instructions to the reviewer

Start from `STATEMENT.md`, then read `A027` and `E028/README.md`, then the
instrument. Attack in this order:

1. **Is T1 actually true as stated?** Check every step of the descent,
   especially: the claim that the unique chord at \(v_0\) survives in every
   subcover; that \(H'\) keeps *exactly* two degree-2 vertices; and that
   every property the search relies on is hereditary downward.
2. **Is T2 sound?** Check that interval-disjoint (endpoint-sharing allowed)
   families really give simple paths, and that the DP computes exactly the
   set of such sums.
3. **Is every prune one-sided?** A prune that can discard a genuine
   counterexample destroys the proof content of an empty run. Examine the
   minimality *reservation* propagation and the symmetry break with
   particular suspicion.
4. **Is the enumeration exhaustive?** Construct, or argue for, a
   chord-minimal cover the position-by-position DFS could miss.
5. **Re-run the instrument yourself**, outside this repository if you
   prefer, and re-derive at least one order's verdict with your own code.
6. **Does the empty verdict mean what `C048` says it means?** In particular:
   the scope restriction to pairs with a Hamiltonian \(a\)–\(b\) path, and
   whether `C048` overstates coverage anywhere.

Do not read the session record or prior attempts before forming an initial
verdict.

## Verdict

**PASS at lemma-and-instrument level, with findings — 0 critical, 4 major,
4 minor, 3 notes.** The mathematics survived every attack I could mount.

- **`T1` (chord-minimal descent) is true as stated.** Coverage, the survival
  of the unique chords at \(v_0\) and \(v_M\) in *every* subcover, the
  "exactly two degree-2 vertices" conclusion, downward heredity of
  cycle-length freedom and of \(S\), and the equivalence "inclusion-minimal
  cover \(\iff\) every chord has an endpoint of chord-degree 1" all check
  out. The descent stays inside `L039`'s class \(\mathcal G\): \(H'\) is
  connected, exactly-two, \(\mathrm{Spec}(H')\subseteq\mathrm{Spec}(H)\),
  \(S(H')\subseteq S(H)\), same order, same Hamiltonian path.
- **`T2` (monotone reroute) is true, and its soundness — the one property
  whose failure would delete a genuine counterexample — is now verified at
  scale.** I re-derived the interval arithmetic by hand and then certified
  **13,572,714 DP-generated savings across 2,131,960 chord systems**
  (exhaustive over *all* chord subsets at \(M=6,7\); randomised at
  \(M=8..24\)) as genuine \(a\)–\(b\) path lengths using my own path
  enumerator. Zero violations. The bitmask DP is set-equal to my explicit
  interval-family enumeration on every one of those systems.
- **`T6` is correct.** I re-derived all four interaction cases and the
  interior-disjoint case (cycle space of \(P+\{e,f\}\) has dimension 2, and
  \(C_e\triangle C_f\) is a disjoint union when the interiors are disjoint,
  hence not a cycle).
- **The enumerator is exhaustive over chord-minimal covers and every prune is
  one-sided.** The position-by-position DFS is a complete decision tree over
  the chord set (each chord \((i,j)\) is decided exactly once, at position
  \(i\)); the minimality *reservation* propagation is exactly equivalent to
  a leaf-only minimality test; the poison prefix prune is sound because
  \(R_p\subseteq R_M=\Sigma\) monotonically; the reversal symmetry break
  keeps at least one representative of every reversal orbit. I could not
  construct a chord-minimal cover the DFS misses, and an **independently
  written enumerator of mine** (python sets not bitmasks, from-scratch cycle
  detection, explicit family enumeration for savings, *no* reservation
  propagation, *no* symmetry break) is **set-equal** to `Search` on every
  case I ran, including a 6,356-element nonempty control.
- **The recorded numbers reproduce exactly** from the shipped `search.py`,
  run outside the repository: run A \(M=15..21\) and run B \(M=15..23\), node
  counts identical to the last digit.
- **The empty verdict means what `C048` says it means**, subject to the
  scope caveats it already records (Hamiltonian stratum only; nothing above
  the last completed rung) — plus the four major findings below, which
  concern the *evidence* and the *description*, not the argument.

What blocks a clean pass is this: **none of the three prunes that can delete
a genuine counterexample — the poison DP, the reversal symmetry break, and
\(C_{16}\) detection — is exercised on a single nonempty (resp. positive)
instance by any recorded check** (`F1`, `F2`). The 78,519-check anchor suite
is 99.7% one micro-property, and 28 of its 32 enumerator-vs-reference
comparisons compare two *empty* sets. I supplied the missing controls myself
and they all pass, so the verdict stands; but as recorded, `C048`'s
verification story does not establish what it is cited for. Separately,
`C048` currently contains unfilled `NN` placeholders and therefore cannot be
cited at all (`F3`), and the top of the ladder is no longer testing (F)'s
mechanism (`F4`).

## Findings

| # | Severity | Area | Finding |
|---|---|---|---|
| F1 | major | instrument verification | 28 of the 32 `a3` enumerator-vs-reference anchor checks compare two **empty** sets; the 4 nonempty ones run with the poison prune *and* the symmetry break switched off. Neither loss-capable prune is validated on any nonempty instance. |
| F2 | major | instrument verification | The production \(C_{16}\) detector — the prune that produces run B's entire all-zero table — is exercised by the anchors only at \(M=9,10,11\), i.e. on graphs of order \(\le12\) where no \(C_{16}\) can exist. Every recorded \(L=16\) check is `False == False`. |
| F3 | major | claim scope / bookkeeping | `C048` as written in `CLAIMS.md` contains literal `NN`/`NNRANGE` placeholders in its headline verdict, so it is presently uncitable; and the recorded expectation that \(C_{16}\)-freeness "brings the whole window \([18,35]\) into range" is contradicted by the measured wall-clock growth (\(\times2.0\)–\(2.4\) per rung, not the quoted \(\times1.9\) node growth). |
| F4 | major | interpretation of the computation | The poison prune stops firing near the top of the ladder (61, 33, 45, 17, **2**, **1**, **0** branch kills at \(M=20..26\)). At \(M=26\) the (F)-specific content of run B is *exactly zero*: the verdict there is the purely structural fact that the \(\{C_4,C_8,C_{16}\}\)-free chord-minimal Hamiltonian stratum is empty. No inference about (F)'s forcing mechanism is supported at those orders. |
| F5 | minor | provenance | `search.py` was edited **after** run A was recorded and **after** the in-flight run B started (PID 49223 at 14:03, file mtime 14:04); `search_15_25.json` lacks the `forbidden` key the current code writes, proving a different revision produced it; `run_15_34.log` preserves a *third*, superseded revision's node counts, unlabelled. The instrument is untracked in git, so the record cannot establish that the shipped code produced the recorded numbers. (I established it by re-running.) |
| F6 | minor | reproducibility / exposition | The README's Reproduction block does not reproduce the load-bearing run: it gives `search 15 25` (run A) and never shows the `c16` argument; the outputs list omits `search_15_34_c16.json` and `production_c16.log`. The anchor count is given as **78,507** in three places; the actual figure under both interpreters is **78,519** (`CLAIMS.md` has it right; the module docstring says "40+ checks"). |
| F7 | minor | cross-check accuracy | The cross-check paragraph says "order 20: **four** signatures". There are exactly **two**. Conversely the cross-check is *stronger* than claimed: at isomorphism level it recovers precisely the eight recorded profile objects with nothing unrecorded. |
| F8 | minor | selection bias / double counting | "extending the saturation observation from eight objects to **eighteen**" and "all eighteen known in-window profile objects [carry a Hamiltonian path]" — the ten new objects are *constructed on* a Hamiltonian path, so they cannot be evidence about the `T5` gap, and they are only **3** graphs up to isomorphism. |
| F9 | note | dependency hygiene | Run B's verdict uses **only** E028-local code; no imported `E018`/`E019` primitive enters it. Run A's exact stage does use the imported `paths_with_essential`. The record should say which verdict rests on which code base — it is a strength of run B that is currently invisible. |
| F10 | note | certification coverage | `cmd_search` stores at most 200 survivors per order in `examples`, and `cmd_certify` re-verifies only `examples`. Harmless now (10 and 43), disclosed in `C048`, but silently partial if run A is ever extended past 200 survivors. |
| F11 | note | exposition | README Interpretation 1 says "(H-F) holds at orders 16–21"; its own run A table already gives 16–22 and its run B table 16–24 (16–28 as of this audit). The record understates itself. |

### F1 — the enumerator-vs-reference anchors are 28/32 vacuous *(major)*

`cmd_anchors`'s `a3` block is the only place where `Search` is compared with
the independently written `brute_force`, and it is also where the symmetry
break is checked. Measured directly (reviewer run, `drv_gaps.py`):

| check | \(M\) range | class | poison | symmetry | outcome |
|---|---|---|---|---|---|
| `a3.exact` | 6–12 | \(\{4,8\}\) | on | off | **0 vs 0** at every \(M\) |
| `a3.c16` | 6–12 | \(\{4,8,16\}\) | on | off | **0 vs 0** at every \(M\) |
| `a3.nopoison` | 6–11 | \(\{4,8\}\) | off | off | **0 vs 0** at every \(M\) |
| `a3.sym` | 6–12 | \(\{4,8\}\) | off | on vs off | **0 vs 0** at every \(M\) |
| `a3.c16ctrl` | 6–10 | \(\{4,16\}\) | **off** | **off** | 0/1/11/80/660 — the only nonempty control |

The cause is structural, not accidental: the \(\{C_4,C_8\}\)-free
chord-minimal cover class is empty at every order \(\le18\) (the enumerator
itself proves this — see the cross-check table), while every `a3` check runs
at \(M\le12\), i.e. order \(\le13\). So the checks *cannot* be nonempty.

**Concrete failure scenario.** Replace `if M - p < self.s0` by
`if M - p <= self.s0` in `Search.choose` — i.e. break the symmetry
non-canonically so that reversal-symmetric systems are discarded. Every one
of the 78,519 anchor checks still passes (all `a3.sym` comparisons remain
\(\emptyset=\emptyset\)), and run B still reports `survivors=0` at every
order — but the search would now be losing exactly the palindromic covers.
That class is not empty: at order 20, 28 of the 65 symmetry-broken covers
are reversal-symmetric. The same argument applies to any over-aggressive
edit of the poison test in `Search.step`.

**Reviewer-supplied controls (all pass).** Reversal-closure
\(a\subseteq b\) and \(a\cup\rho(a)=b\) verified on nonempty instances:

- class \(\{C_4\}\), poison **on**, \(M=8..12\): broken 1/10/10/192/3872 vs
  full 2/14/15/302/6356 — closure exact at every \(M\);
- class \(\{C_4\}\), poison **off**, \(M=7..12\): 1/6/47/379/3356/28520 vs
  1/11/80/660/5774/50619 — closure exact;
- **inside the real class \(\{C_4,C_8\}\)**, the first nonempty test that
  exists: order 19 (6 vs 12) and order 20 (65 vs 102) with poison off, and
  orders 21 (10 vs 20) and 22 (43 vs 66) with poison **on** — closure exact
  in all four;
- full production configuration (symmetry **on**, poison **on**) against
  `brute_force`, class \(\{C_4\}\), \(M=6..11\): reversal closure of the
  broken run equals the reference exactly.

And the reservation/prefix machinery against a reference that uses **neither**
(minimality and poison tested only at the leaf), class \(\{C_4\}\) and
\(\{C_4,C_8\}\), \(M=6..12\): identical sets throughout, up to 6,356 members.

### F2 — the \(C_{16}\) prune is never positively exercised *(major)*

Run B's verdict is produced overwhelmingly by
`creates_forbidden_fast(adj, u, w, (4,8,16))`; from \(M=24\) on it is
produced *almost entirely* by its \(L=16\) branch (`F4`). The two anchors
that touch it, `a1.fast-agree` (45,683 checks) and `a1.fast-vs-hascycle`
(32,570 checks) — together 99.7% of the headline 78,519 — enumerate systems
at \(M=9,10,11\). Those graphs have at most 12 vertices, so *every* \(L=16\)
comparison in the suite is `0 == 0` / `False == False`.

**Concrete failure scenario.** A bug in `_walk` at depth 15 (the \(L=16\)
call is `_walk(adj, u, 1<<u, w, 1<<w, 15)`, a code path never taken with a
positive answer anywhere in the anchor suite) that returns `True` spuriously
would prune every branch of run B and produce exactly the observed all-zero
table at every order — indistinguishable, on the recorded evidence, from a
proof.

**Reviewer test (passes).** Three detectors — the production
`creates_forbidden_fast`, the generic `has_cycle_through_edge`, and my own
from-scratch set-based `cycle_through_edge` — compared on random chord
systems:

- \(M=15..22\): **6,927 positive** and 7,620 negative through-edge \(C_{16}\)
  instances, plus 2,400 whole-graph comparisons against `has_cycle_len` and
  my own minimum-vertex enumerator. Zero mismatches.
- \(M=26..34\) (the top of the window, where nothing recorded reaches):
  15,072 through-edge instances over \(L\in\{4,8,16\}\)
  (\(C_4\): 3,191 pos / 1,833 neg; \(C_8\): 4,971/53; \(C_{16}\):
  5,011/13) plus 675 whole-graph comparisons. Zero mismatches.

So the detector is right. The record does not show it.

### F3 — `C048` is uncitable as written, and the window is not in range *(major)*

Two distinct defects.

**(a) Placeholders.** `CLAIMS.md` row `C048` reads "no dodging profile object
exists at orders 16–**NN**", "survivors 0 at every order **NNRANGE** (nodes
8,924 … **NN**)". A claim whose headline quantifier is a placeholder cannot
be cited at any strength. As of this audit the true last completed run B rung
is \(M=27\) (**order 28**); orders 29–35 are undecided.

**(b) The window is not in range on the measured growth.** `A027` and the
README both rest the plan on "\(\approx\times1.9\) per order … which is what
brings the whole window \([18,35]\) into range". That is the *node* ratio.
The *wall-clock* ratio is worse and worsening, because per-node cost grows
with graph size:

| \(M\) | 22 | 23 | 24 | 25 | 26 | 27 |
|---|---|---|---|---|---|---|
| seconds | 28.6 | 61.4 | 116.4 | 216.2 | 504.0 | 1220.0 |
| ratio | — | 2.15 | 1.90 | 1.86 | 2.33 | 2.42 |

Extrapolating the last rung at ratio 2.0–2.4, orders 29–35 cost between
\(\approx3.5\) and \(\approx11\) days on the single core the run is using —
the last rung alone between 9 h and 5 days. The claim "brings the whole
window into range" is an extrapolation from node counts that the timing data
does not support, and the ladder should be recorded as an open-ended
computation with a stated last-completed rung, not as a window closure.

### F4 — the top of the ladder is class-emptiness, not poison forcing *(major)*

Prune tallies from `search_15_34_c16.json`, `prunes["poison"]` (branches
killed by the \(T2\) savings test):

| \(M\) | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| poison kills | 1445 | 982 | 880 | 1234 | 738 | 61 | 33 | 45 | 17 | **2** | **1** | **0** |

At \(M=26\) the poison test never returned `True` even once. Therefore the
search tree with the poison prune is *identical* to the tree without it, and
what run B actually proved at order 27 is the stronger, poison-free
statement:

> There is no \(\{C_4,C_8,C_{16}\}\)-free graph of order 27 with exactly two
> degree-2 vertices (all other degrees \(\ge3\)) carrying a Hamiltonian
> \(a\)–\(b\) path — chord-minimal or not (by `T1`'s descent).

This is logically *stronger* than (H-F) at that order, so the verdict is not
damaged. But three consequences must be recorded or the result will be cited
for more than it shows:

1. `C048`'s framing ("no **dodging** profile object exists") invites the
   reading that the through-set arithmetic was tested at orders 25–28. It
   was not; at order 27 it was used zero times.
2. Nothing about (F)'s *mechanism* — the saturation/interpolation programme
   `A026` T7 is trying to prove — is supported by the rungs at \(M\ge24\).
   The evidence for the mechanism is confined to \(M\le23\), and it is
   already thin at \(M=20..23\) (17–61 kills against \(10^5\)–\(10^6\)
   nodes).
3. `A027` T4's prediction that "the survivor count must grow with \(M\) until
   \(M\ge31\)" is realised in run A (0,0,0,0,0,10,43) but not in run B, and
   the reason is not that the prune got stronger — it is that the class
   itself empties. T4's analysis of the calculus's reach does not anticipate
   this and should be amended.

The right record here is a per-rung poison-prune tally beside the survivor
count, and an explicit statement that from order \(\approx25\) the ladder is
a structural emptiness result about the \(\{C_4,C_8,C_{16}\}\)-free
Hamiltonian exactly-two stratum.

### F5 — instrument revision drift *(minor)*

`data/` currently holds artefacts from **three** different revisions of
`search.py`, none of them identified:

- `run_15_34.log` (13:30) — run A with node counts 13,596 / 66,054 /
  186,390 / 550,080 / 1,852,563 / 6,603,038 at \(M=15..20\);
- `production.log` + `search_15_25.json` (14:00) — run A with node counts
  10,345 / 52,391 / 145,178 / 413,945 / 1,374,926 / 4,860,618 at the same
  \(M\); `search_15_25.json` has no `forbidden` key, which the current code
  always writes;
- the in-flight run B (PID 49223, started 14:03) writing
  `production_c16.log`, against a `search.py` whose mtime is 14:04.

Same configuration, different node counts, no provenance record. I closed
this by re-running the shipped instrument outside the repository: run A
\(M=15..21\) and run B \(M=15..23\) reproduce the 14:00 and in-flight numbers
**exactly**, so the edits were semantically neutral for both runs. The
record should say so (or pin a hash), because on its own face it does not.

### F6 — reproduction commands and the anchor count *(minor)*

`README.md` "Reproduction" gives
`nice -n 15 pypy3 search.py search 15 25`, which is **run A**. The verdict
`C048` leads with **run B**, whose command is `search 15 34 c16`; the `c16`
positional argument appears nowhere in the README. The "Outputs in `data/`"
list omits `search_15_34_c16.json` and `production_c16.log`. Anchor count:
README says 78,507 (three occurrences); both `anchors_search_*.json` files
record **78,519**, which I reproduced under PyPy in an isolated copy
(`78519 checks passed (3.11.15/PyPy), 9.2 s`). The module docstring still
says "40+ checks".

### F7 — the order-20 signature count, and a stronger cross-check *(minor)*

The README's cross-check paragraph says "order 19: one signature, 28 edges;
order 20: **four** signatures, 29 and 30 edges". Reviewer re-run of the
poison-off enumeration (counts 0,0,0,0,0,0,0,**6**,**65** at orders 12–20 —
reproduced exactly):

- order 19: 1 signature — 10 chords, 28 edges, degrees \(2^2 3^{16} 4\), ×6;
- order 20: **2** signatures — 10 chords / 29 edges / \(2^2 3^{18}\) ×17, and
  11 chords / 30 edges / \(2^2 3^{16} 4^2\) ×48.

Both are in the recorded profile signature set, so the substantive claim
holds; "four" is wrong. In the other direction the record *understates* its
own evidence: at isomorphism level (nauty `labelg`, symmetry break off) the
enumeration gives 12 covers → **1** isomorphism class at order 19 and 102
covers → **7** isomorphism classes at order 20, and all eight classes are
*exactly* the eight recorded profile objects, with **zero** unrecorded
graphs. Given that the order-20 census was a partial (11/16 parts + part-14)
sample, this is a genuinely independent completeness check on the
chord-minimal Hamiltonian stratum and deserves to be stated at that strength.

### F8 — "eighteen objects" *(minor)*

Two problems with README Interpretation 2 and the parallel sentence in
`C048`'s scope paragraph:

- **Circularity.** "all eighteen known in-window profile objects [carry a
  Hamiltonian \(a\)–\(b\) path]" is offered next to the `T5` gap (whether the
  profile *forces* a Hamiltonian through-path). Ten of the eighteen were
  produced by a search that constructs graphs on a Hamiltonian path. They are
  a selected sample and carry no information about `T5`.
- **Double counting.** The ten order-21 survivors are **3** graphs up to
  isomorphism (`certify`; I reproduced 3 at order 21 and 16 at order 22 with
  `labelg`). The honest tally at orders \(\le21\) is 8 + 3 = **11**
  isomorphism classes, and at order 22 a further 16, of which **13** break
  the interval/saturation pattern the sentence is extending.

## What I tried and failed to break

Recorded so the pass is not mistaken for a light touch.

1. **Tried to find a chord-minimal cover the DFS misses.** Attacked the
   reservation propagation from five directions: a chord whose *left*
   endpoint has degree 1 and right endpoint degree \(\ge2\) (correctly left
   unreserved); a position reserved before its own `choose` runs (correctly
   allowed to close at degree 1, forbidden to emit); double reservation of
   the same position from two different left endpoints (impossible — the
   loop skips reserved \(q\)); reservation release on the early-return path
   inside `close` (correctly released); and `into[p]`/`out[p]` stack
   discipline under backtracking (balanced, `pop()` always removes the chord
   just added). None yields a lost solution, and the reservation-free
   reference confirms it empirically.
2. **Tried to break the symmetry break.** Checked the orbit argument
   (reversal swaps span-at-0 with span-at-\(M\); `\ge` keeps at least one
   representative, both when equal), the case where the chord at 0 *is* the
   chord at \(M\) (\(s_0\) is `None` at that moment, so the filter is
   correctly skipped), and the interaction with prefix pruning (the poison
   set \(\Sigma\) is reversal-invariant, and prefix pruning never kills a
   globally valid system). Then verified reversal-closure empirically on
   nonempty instances in the real class, which the anchors never do.
3. **Tried to make the poison prune over-prune.** \(R_p\subseteq R_M\) by
   monotonicity of the recurrence, so a prefix hit is a genuine hit; the
   \(R\) array is recomputed at the right moment (`step(p)` after all chords
   *into* \(p\) are decided, unaffected by chords *out of* \(p\)). Then
   certified 13.5M DP savings as real path lengths.
4. **Tried to make the incremental cycle test miss a forbidden cycle.** The
   "last chord added" argument is airtight (every cycle of \(P+\mathcal C\)
   uses a chord, and at the moment the last one is added all others are
   present). Confirmed against a whole-graph detector on 3,075 systems at
   \(M=15..34\).
5. **Tried to make the chord-count prune \(|\mathcal C'|\ge n\) unsound.**
   It is sound with room to spare: minimality gives an injection
   chord \(\mapsto\) private endpoint, so \(|\mathcal C'|\le n-1\); the
   tally `prunes["count"]` is 0 at every rung, confirming it never binds.
6. **Tried to find an order in the window that the search skips.** Only
   \(M\in\{2,6,14,30\}\) are skipped, correctly: \(\max S=M\) is itself
   poison there, so order 31 needs no search.
7. **Tried to find a poison length or power the window misses.**
   \(S\subseteq[1,34]\) and \(\mathrm{Spec}\subseteq[3,35]\) for \(n\le35\),
   so \(\{2,6,14,30\}\) and \(\{4,8,16,32\}\) are exhaustive; \(C_{32}\) is
   deliberately deferred to the exact stage, which is a relaxation and
   therefore safe.
8. **Tried to catch the imported layer writing into a sibling experiment.**
   Ran the whole instrument from a copy outside the repository: repository
   `E028/data` and `E026/data` untouched, all output rebound.
9. **Independently re-derived the verdicts.** My own enumerator, sharing no
   code with `E028`, returns the empty set for the run B configuration at
   orders 19, 20, 21, 22, 23, 24, 25 — matching `E028` exactly at every one
   (it was still running order 26 at write time). Timings 7.9 s → 626.8 s.

## Independence note

Independence mode as recorded: `delegated-subagent`. Honest account of what
I read and in what order:

1. `problems/erdos-gyarfas/STATEMENT.md`;
2. this review record (`R003`);
3. `process/review-playbook.md`, `process/proof-standard.md`;
4. `attempts/A027-…md` — **the identified candidate**. The review record
   names `A027` T1–T6 as the object under audit, so it plays the role
   `PROOF.md` normally plays. I read only `A027`, no other attempt;
5. `experiments/E028-…/README.md` and `experiments/E028-…/search.py`;
6. `experiments/E028-…/data/*` (logs, JSON, certificates);
7. `CLAIMS.md` rows `L052`, `C048`, `L039`, `L042`, `L046`, `L048`, `C043`
   and the `G015` row of `OBLIGATIONS.md` — read **only** to check that
   claims are cited at their recorded strength and that (H-F) instantiates
   (F) correctly. These are ledgers, explicitly permitted.

**Exceptions and contamination.** None taken. I did **not** read
`sessions/S027-*`, `A026`, any other attempt, `PROOF.md`, `DECISIONS.md`,
`STATE.md`, `LOG.md`, or the earlier reviews `R001`/`R002` at any point,
before or after forming the verdict. The invoking prompt contained only the
slug, the record path, the review type, and operational constraints about
the running job — no discovery narrative. One unavoidable partial exposure:
the `git log` I ran to check whether `search.py` is tracked printed recent
commit subjects, which summarise sessions S023–S026; I had already read the
`G015` obligation row by then and the exposure changed nothing in the
findings, but I record it rather than leave it silent.

**Machine discipline.** I did not touch the running production job
(PID 49223) or `E024`'s eight `genc48` workers, and wrote nothing into
`E028/data`. Every re-run was done from a copy of `search.py` under
`/private/tmp/…/scratchpad/exps/E028x`, with sibling experiment directories
symlinked read-only, at `nice -n 15`, single process.

## Reviewer audit log

Environment: CPython 3.14.2, PyPy 7.3.23 (3.11.15), macOS/arm64. All runs
`nice -n 15`, single process, outside the repository.

| # | What | Result |
|---|---|---|
| 1 | `pypy3 search.py anchors` in isolated copy | **78,519** checks pass, 9.2 s; repository `E028/data` and `E026/data` untouched |
| 2 | anchor payload comparison, both stored JSONs | check-name lists byte-identical between CPython and PyPy; 78,253/78,519 checks are `a1` detector-agreement |
| 3 | poison-off cross-check, orders 12–20 | 0,0,0,0,0,0,0,**6**,**65** — reproduces the recorded table exactly; signatures: 1 at order 19, **2** at order 20 (`F7`) |
| 4 | isomorphism cross-check via nauty `labelg` | order 19: 12 covers → 1 class; order 20: 102 covers → 7 classes; all 8 classes are exactly the 8 recorded profile objects, 0 unrecorded |
| 5 | run A reproduction, \(M=15..21\), shipped code | node counts 10,345 / 52,391 / 145,178 / 413,945 / 1,374,926 / 4,860,618 / 17,076,872 — identical to `production.log`; survivors 0,0,0,0,0,10,43 |
| 6 | run B reproduction, \(M=15..23\), shipped code | 8,924 / 26,080 / 38,362 / 61,040 / 108,068 / 182,613 / 323,622 / 634,125 / 1,204,578 — identical to `production_c16.log` |
| 7 | independent enumerator vs `Search`, nonempty controls, class \(\{C_4\}\), poison **on** | \(M=8..12\): 2 / 14 / 15 / 302 / **6,356** — set-equal at every \(M\) |
| 8 | independent enumerator vs `Search`, class \(\{C_4\}\), poison off | \(M=6..11\): 0/1/11/80/660/5,774 — set-equal (also reproduces the recorded 0/1/11/80/660 control) |
| 9 | independent enumerator, run B configuration | orders 19–25 all **empty**, matching `E028` exactly (order 26 still running at write time) |
| 10 | reference with **no** reservation propagation and **no** poison prefix prune | classes \(\{C_4\}\) and \(\{C_4,C_8\}\), \(M=6..12\): set-equal to `Search` at every \(M\) |
| 11 | symmetry-break reversal closure, nonempty | class \(\{C_4\}\) poison on/off \(M=6..12\); class \(\{C_4,C_8\}\) orders 19,20 (poison off) and 21,22 (poison on) — \(a\subseteq b\) and \(a\cup\rho(a)=b\) exact in all cases |
| 12 | \(T2\) soundness stress test | 2,131,960 chord systems (exhaustive at \(M=6,7\); random \(M=8..24\)); **13,572,714** DP savings each certified a genuine \(a\)–\(b\) path length by an independent enumerator; DP set-equal to explicit family enumeration; **0** violations |
| 13 | \(C_{16}\) detector, positive instances | \(M=15..22\): 6,927 positive / 7,620 negative through-edge instances, three detectors; \(M=26..34\): 15,072 instances over \(L\in\{4,8,16\}\) plus 675 whole-graph checks; **0** mismatches |
| 14 | prune tallies from `search_15_34_c16.json` | `count` prune 0 at every rung; `poison` prune 1445→**0** over \(M=15..26\) (`F4`); `capped` false at every rung |
| 15 | wall-clock growth of run B | 28.6 / 61.4 / 116.4 / 216.2 / 504.0 / 1220.0 s at \(M=22..27\); ratios 2.15/1.90/1.86/2.33/2.42 (`F3`) |

Reviewer code and logs are under
`/private/tmp/claude-501/-Users-mattwatts-code-rh/a10ee577-cdf0-4c84-9de0-e45704e78ff4/scratchpad/`
(`audit/indep.py`, `exps/E028x/drv_*.py`, `audit/indep_c16.log`). They are
scratch, not repository records; if the session wants any of them preserved
as evidence, they must be copied into an experiment record by the session,
not by this review.
