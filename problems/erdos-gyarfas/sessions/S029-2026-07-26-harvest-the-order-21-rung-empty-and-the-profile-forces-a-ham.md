# S029 — harvest the order-21 rung: empty, and the profile forces a Hamiltonian through-path 19 for 19

- Date: 2026-07-26
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1, unchanged.
- Work / claim status: `active` / `open`, unchanged by this session.
- Strongest established facts in scope: `C043` (the \(\mathcal G\) ladder empty
  at orders 18–20), `C048` (the (F) ladder empty at orders 16–30 on the
  **Hamiltonian** stratum), `C047`(e) (only 22–29% of ordinary taut degree-2
  pairs are Hamiltonian).
- Open obligations in scope: `G015`.
- Inherited next action: harvest the `E024` order-21 rung and make the decisive
  measurement, \(\max S\) against \(n-1\).
- Session goal: exactly that.
- Falsifiable next move: a single order-21 profile member with \(\max S<n-1\)
  shows the profile does **not** force a Hamiltonian through-path, which would
  make `C048`'s emptiness a statement about a proper sub-stratum.

## Strategy audit

Mechanical closure of a pre-registered measurement; the strategic choice was
made in the `S027` post-close review and is not relitigated here. The one live
question was whether to trust the cloud-produced parts, and that is answered by
the gate (`O012`) plus the verification below, not by assumption.

## Work performed

### 1. Retrieval and verification

Six Railway volumes downloaded and merged (`merge_verify.py`). Checks, all
passed: **144/144 parts present exactly once**, every file matching the sha256
its own container recorded, each part self-describing as the order and part it
is filed under, and the per-part coverage identity
`profile == c16_blocked + survivors` holding on every part.

**Three parts had no class file** — 115, 99, 142, generating 205,928 / 351,893 /
365,671 graphs against `scan.py`'s `SAVE_LIMIT` of 200,000. Each was checked
individually: **all three contain zero degree-profile members**, so all 19
members were recovered and the extraction is complete. That was luck, not
design — see the recalibration note below.

The harvest was then run with the **local, already-anchored arm64 instrument**
(`E019/scan.py` via `E022/ladder.py`'s `load_scan`), not in the cloud, so every
number that reaches a ledger comes from the build the repository has always
trusted. Its own coverage assertion over all 144 parts passed.

### 2. The rung

Complete order-21 \(\{C_4,C_8\}\)-free class: **2,951,168 graphs**, 652,935
generator cpu-seconds (181.4 core-hours), maximum 33 edges.

- degree-profile members (exactly two degree-2 vertices, all others \(\ge3\)):
  **19**
- of those, \(C_{16}\)-blocked: **19**
- power-free survivors: **0**

So **the order-21 \(\mathcal G\)-profile class is empty**, extending `C043`'s
emptiness at 18–20. The degree-2 histogram over the class runs 19 / 1,071 /
15,792 / 106,188 / … with its mode at 8; power-free members number 308,098 with
**minimum degree-2 count 5** — no power-free member has 2, 3 or 4 degree-2
vertices at this order.

### 3. THE DECISIVE MEASUREMENT

For each of the 19 members, computed with the local instrument's own
primitives: \(\max S\) against \(n-1=20\), \(S\cap\{2,6,14,30\}\), and
\(16\in\mathrm{Spec}\). Every row additionally asserted \(\{C_4,C_8\}\)-freeness,
the exactly-two degree profile, the edge count, and the recorded invariant
\(\min S=d(a,b)\).

**Result: \(\max S=20=n-1\) on all 19. Every order-21 profile member carries a
Hamiltonian \(a\)–\(b\) path.** All 19 are also \(C_{16}\)-blocked.

Cumulative: **27 of 27** in-window profile objects are Hamiltonian (8 at orders
19–20, 19 at order 21), against `C047`(e)'s control base rate of **22–29%** for
ordinary taut degree-2 pairs. The pre-registered pivot did **not** fire.

### 4. A refinement, found en route

Eighteen of the 19 have both 6 and 14 in \(S\); **one does not** —
`T????A?O@?B?D??oQ?_KAoG?AoB?_@OO?LA?`, with \(d(a,b)=4\), \(\max S=20\), and
\(S\cap\{2,6,14,30\}=\{14\}\). So \(6\notin S\) for that member: the
\(S\supseteq[6,n-1]\) saturation of `A025` T3 is **not** universal at order 21,
while the double blocking survives (14 in \(S\) *and* a \(C_{16}\)). This is the
same break `S027` first saw at order 22, now witnessed one order lower.

## Results

### Computational evidence

- **The order-21 \(\mathcal G\)-profile class is empty** (0 power-free profile
  members over the complete 2,951,168-graph class). Floors advance: every
  \(\mathcal G\)-member has order \(\ge22\), every tight 1-atom \(\ge23\).
- **The exactly-two profile forces a Hamiltonian through-path on all evidence
  now available: 27/27**, base rate 22–29%. This is the strongest support the
  `E028` programme has that its ladder addresses the real question rather than
  a convenient slice.
- **Saturation is not universal**: one order-21 member has \(6\notin S\).

### What this does and does not establish

It does **not** prove the profile forces Hamiltonicity — 27 examples are
evidence, not a theorem — and `A027` T5 (the non-Hamiltonian stratum) remains
open and unproved at *every* order. What changed is the **prior**: before this,
the hypothesis rested on 8 points at two orders; it now rests on 27 across
three, including the first order where the class is large enough for the
question to have teeth.

## Failed routes and why

None attempted; this was a pre-registered measurement.

## Adversarial check

- The instrument was gated before use and re-verified locally (`O012`), and all
  six containers were confirmed at run time to carry the gated binary.
- Retrieval was verified rather than trusted: per-file hashes, full residue
  system, self-description, coverage identities.
- The three missing class files were **not** waved through — each was checked
  for profile content before the extraction was called complete.
- The measurement re-derives every class condition per row instead of trusting
  the upstream filter, and asserts \(\min S=d(a,b)\).
- The Hamiltonian result was checked against the possibility of being an
  artefact of how members are generated: the control is `C047`(e)'s 22–29%,
  computed on the same class by the same instrument, so 27/27 is not a
  selection effect.

## Recalibration note (carried into `process/compute.md` and `O012`)

Modulus 144 was chosen on the claim that every part would sit far under
`SAVE_LIMIT`. Three parts exceeded it, one by 1.8×. Nothing was lost, but only
because those parts happened to hold no profile members. The sizing rule must
be driven by the **tail** of the part-size distribution, not the mean — the
same error that made this session's wall-clock projections wrong (predicted
~7 h, actual 14.4 h; the mean part was predicted well, the tail badly).

## Canonical records changed

- [ ] `STATEMENT.md`
- [x] `STATE.md`
- [x] `CLAIMS.md`
- [x] `OBLIGATIONS.md`
- [ ] `PROOF.md`
- [ ] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: (F) empty on the Hamiltonian stratum at 16–30; the
  \(\mathcal G\)-profile class empty at 18–21; the profile is Hamiltonian on
  27/27 known members; the non-Hamiltonian stratum is cleared at no order.
- Remaining blockers: `G015`(b), the non-Hamiltonian stratum (`A027` T5).
- Recalibration decision: **continued**. The pivot did not fire, so the `E028`
  work stands as addressing the main question, and the non-Hamiltonian stratum
  is confirmed as the primary proof target rather than promoted to urgent.
- Best live alternative: prove the Hamiltonian forcing itself — turn 27/27 into
  a lemma — which would make `C048` a genuine closure of case (5b) at 16–30
  rather than a stratum result.
- Pivot trigger: a non-Hamiltonian in-window profile member at any order.
- Best next action: `A027` T5 — extend the chord-minimal descent from chords to
  bridges on the non-Hamiltonian stratum.
- Files a new session should read: this record, `C048`, `A027` T5, `C047`(e)
  for the control, and `O012`/`O014` for how the rung was produced.

## Plain-language recap

The big overnight computation finished. It surveyed every graph of a certain
kind on 21 points — nearly three million of them — looking for a specific type
of "escape" object. **There are none**, which pushes the floor up another notch:
any such object must now have at least 22 points.

The more important result is the side measurement. Nineteen graphs in that
survey had the exact shape the proof strategy cares about, and the question was
whether all of them contain a route from one special point to the other passing
through *every* point. The large exhaustive search we have been running for days
only covers graphs that do; if some don't, that search has been answering an
easier question than the one we need.

**All nineteen do.** Together with eight already known, that is twenty-seven out
of twenty-seven — where ordinary comparable graphs manage it only about a
quarter of the time. Not a proof, but strong evidence that the work already done
is aimed at the real target rather than a convenient corner of it.

One small surprise: one of the nineteen breaks a pattern every previously known
example followed, missing a value all the others contain. It is still caught by
the other blocking condition, so nothing collapses — but it shows the pattern
was a coincidence of small samples rather than a law.

## Proposed next step

Attack the half no computation has touched: the case where the route between the
two special points *cannot* reach every point. The concrete move is to extend
the existing descent argument from simple shortcuts to detours — where a detour
covers ground without shortening anything — and to exploit the fact that a
detour buying nothing forces its interior to be very regular, a shape already
proven not to exist here. That would either close the remaining case or expose
exactly what is missing. The alternative considered and deferred is trying to
prove the twenty-seven-out-of-twenty-seven pattern as a theorem; deferred
because the non-Hamiltonian case must be handled either way, and proving the
pattern would only remove the need for it, not replace it.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: **9%**
- Previous estimate, if any: 8% (S027, S028)
- Reason for change: +1. The Hamiltonian measurement was a genuine kill test
  with a pre-registered pivot, and it came back 27/27 against a 22–29% base
  rate. That materially raises the chance the completed `E028` ladder addresses
  case (5b) as a whole rather than a sub-stratum — the difference between
  "orders 16–30 are done" and "orders 16–30 are done for some of the objects".
  The increase is small because nothing was *proved*: the non-Hamiltonian
  stratum is open at every order, and the missing tool — a lower-bound theory
  for through-path length sets — is unchanged.
- Basis: most promising route is `A027` T5; strongest obstacle is that no
  technique yet forces through-path lengths from below; the evidence that moved
  the number is 27/27 against a measured control, not a new deduction.
