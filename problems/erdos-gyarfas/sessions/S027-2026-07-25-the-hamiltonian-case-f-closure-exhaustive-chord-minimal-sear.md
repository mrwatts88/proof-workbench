# S027 — the Hamiltonian-case (F) closure: exhaustive chord-minimal search for a dodging profile object over the whole window

- Date: 2026-07-25
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1 (unchanged)
- Work / claim status: `active` / `open`
- Strongest established facts: `L049`/`L050` (interference-completeness ⟺
  vertex-tautness, audited `R002`); `L048`(iii) (the residual object's
  power-freeness *is* through-path arithmetic:
  \(\mathrm{Spec}(B)=T_1\cup(S+2)\), so \(S\) must avoid
  \(\{2,6,14,30\}\) and \(\mathrm{Spec}(H)\) must avoid \(\{4,8,16,32\}\));
  `L046` (case (5b) is a single 2-connected configuration below order 36);
  `L047` (every counterexample has \(\ge22\) vertices); `C046` (the census:
  zero gapped exactly-two members on disk at 10–20); `C047`/`A026` (the
  dodge taxonomy, the span law, the validated chord-exchange calculus).
- Open obligations in scope: `G015` (exclude case (5b)); `G013`(a).
- Inherited next action: **harvest `E024` first** (the order-21
  \(\mathcal G\) rung, running since S023 close), **then** the (L-B)
  chord-savings attempt.
- Session goal (user-directed): skip the harvest — `E024` is not finished
  and its most likely outcome (an empty rung) moves a floor without
  bearing on (F) — and go straight to the highest-value proof move, "the
  shortcut lemma".
- Falsifiable next move: decide, order by order, whether a
  \(\{C_4,C_8\}\)-free exactly-two pair with a Hamiltonian \(a\)–\(b\) path
  can dodge both the poison lengths and the power cycles.

## Strategy audit

- **Why the inherited route might work.** (L-B) is the half of the split
  with a *validated engine*: `C047`(f) showed disjoint-chord surgery on one
  Hamiltonian path already generates the whole top of \(S\) down to 10,
  including 14, on all eight profile objects, and provably fills nothing on
  the 36 Hamiltonian dodgers. So the mechanism is real; what was missing was
  a proof that the chord system always *reaches* savings \(M-14\) or
  \(M-6\).
- **Fastest way to falsify it.** Exhibit a chord system meeting every
  derived constraint whose disjoint packings miss the target savings. That
  is a finite question at each path length — which is what made the next
  move obvious: rather than guess the lemma, **decide** the question.
- **Mechanistically distinct alternative considered.** Suppressing both
  degree-2 terminals maps the pair to a min-degree-3 graph of order
  \(n-2\), which `C040` empties for \(n\le23\) — a cheap but narrow lever
  (it only forces the existence of some short cycle through a terminal,
  not a poison length), and it dies above order 23. Recorded, not selected.
- **Selected route and reason.** Reduction-first, not lemma-first: prove
  that a hypothetical dodger can be assumed **chord-minimal** and that
  monotone reroutes give a *sound one-sided* prune, then enumerate. Two
  aims were sharpened at the same time, both strictly in our favour and both
  inside `A025` T4's frame: prove the **disjunction** (F) rather than (F-S)
  or (F-T) separately (only (F) closes case (5b), and assuming both
  conclusions fail hands us \(C_{16}\)-freeness as a *free extra
  hypothesis*), and use the **whole** poison set \(\{2,6,14,30\}\) rather
  than \(\{6,14\}\) (\(30+2=32\)). Tier 1, `G015`.
- **Pivot criterion.** If the enumeration's survivor count or node count
  exploded before the window was covered, drop to the bridge recursion of
  `A027` T5 or to a stronger route calculus. It did explode under the
  \(\{C_4,C_8\}\)-only prune — and adding \(C_{16}\)-freeness (free, as
  above) collapsed it instead of pivoting.

## Work performed

Attempt `A027`, experiment `E028`.

1. **Proved the two reductions** (`A027` T1/T2, offered as `L052`):
   *chord-minimal descent* — on a pair with a Hamiltonian \(a\)–\(b\) path
   the chords cover every path position (positions 0 and \(M\) exactly
   once), and passing to any inclusion-minimal subcover preserves the
   degree profile, the Hamiltonian path, and — since cycle-length freedom
   and through-sets are hereditary downward — every hypothesis of (F)'s
   negation; and *monotone reroute* — interval-disjoint chord families
   realise genuine \(a\)–\(b\) paths, with the savings set given by a
   left-to-right DP whose prefixes already certify membership.
2. **Corrected a hand-derived chord-pair table entry** (`A027` T6): two
   *interior-disjoint* chords close no cycle with the path. The wrong entry
   was caught by the instrument's own anchors before use; the instrument
   tests the whole graph rather than a table, which is why it could not
   propagate.
3. **Built and anchored `E028`**: 80,131 checks under CPython 3.14.2 and
   PyPy 7.3.23 with identical histograms (78,519 before the post-audit
   repair added families a6/a7), including exact set-equality
   against an independently written brute-force enumerator on every case
   where the latter is feasible (with nonempty positive controls
   0/1/11/80/660 at \(M=6..10\) under \(C_4\)-freeness alone), assertion
   that every DP-generated length is a real path length, and full
   re-derivation of the eight profile objects.
4. **Cross-checked the recorded ladder from an independent generation
   principle**: with the poison prune off, chord-minimal cover counts are 0
   at orders 12–18 and 6, 65 at orders 19, 20, and the order-19/20 outputs
   carry only invariant signatures already recorded for the eight profile
   objects — reproducing `C027`/`C039`/`C043` without geng.
5. **Ran the ladder** (`E028`, offered as `C048`), in two configurations:
   run A with \(\{C_4,C_8\}\) only (the (F-S) stratum) and run B with
   \(\{C_4,C_8,C_{16}\}\) (the (F) hypothesis).
6. **Opened `R003`** and delegated an adversarial audit of the reduction and
   the instrument to a fresh `proof-reviewer` subagent.

## Results

**Proved.**

- `L052` (`A027` T1/T2/T6) — the chord-minimal descent, the monotone
  reroute with its DP, and the corrected chord-pair geometry. This is what
  converts "a lemma nobody knows how to prove" into "a finite decision
  problem per order", and it is independent of the (F) program: it uses only
  heredity of cycle-length freedom and of through-sets under spanning
  subgraphs.

**Computational (offered as `C048`; exhaustive after `L052`).**

- **Run B decides (F) on the Hamiltonian stratum, order by order, and it is
  empty at orders 16–29** (the last completed rung at session close; node
  growth \(\approx\times1.9\) per order). Two scope facts, both established
  by the audit and recorded at full strength: the ladder is an **open-ended
  computation**, not a window closure (wall-clock growth 1.8–2.4 per rung, so
  orders 30–35 are days of single-core computing); and **above order 26 the
  poison prune stops firing** (branch kills 61, 33, 45, 17, 2, 1, 0, 0, 0 at
  \(M=20\ldots28\)), so orders 27–29 prove the *stronger*, poison-free
  statement that the \(\{C_4,C_8,C_{16}\}\)-free chord-minimal Hamiltonian
  exactly-two stratum is empty — implying (F) a fortiori but exercising none
  of its forcing mechanism.
- **Run A exhibited the first \(\mathcal G\)-profile objects at orders 21
  and 22** — 10 and 43 chord-minimal ones, in 3 and 16 isomorphism classes,
  all 2-connected with girth 3 and 91–186 \(C_{16}\)s. **Every one is killed
  twice**: \(14\in S\) on all 53 (40 also have \(6\in S\)) and a \(C_{16}\)
  on all 53. The double blocking is unbroken at the two orders beyond the
  recorded frontier.
- **New structure at the frontier**: 13 of the order-22 objects have \(S\)
  *not* a full interval (holes at \(\{6\}\), or at \(\{2,3,4,6,7\}\) with
  adjacent terminals). These are the first in-window exactly-two objects
  breaking the `A025` T3 saturation pattern — while still carrying 14 and a
  \(C_{16}\). So saturation is *not* the mechanism; the mechanism is
  narrower and survives its first counterexamples.

**Provisional insight.**

- `A027` T5's zero-savings case has a first purchase: a two-attachment
  off-path component with no savings forces an all-equal-length, hence
  **bipartite**, gadget with interior degrees \(\ge3\) — exactly the class
  the bipartite hunt (`L035`/`C034`) has been emptying. The transfer is not
  done (power-freeness is not yet matched), but it names a route.

**The engineering fact that mattered.** Adding \(C_{16}\)-freeness is free —
it is the second half of (F)'s negation — and it cut the enumeration's
growth from \(\approx\times3.5\) to \(\approx\times1.9\) per order (a
\(27\times\) node reduction at order 21). That is what brought the window
into range; without it the ladder would have stalled around order 26.

## Failed routes and why

Nothing died. The \(\{C_4,C_8\}\)-only configuration (run A) hit its
pre-registered pivot criterion — survivor and node counts growing too fast
to cover the window — and the pivot taken was to *use a hypothesis already
available* rather than to change mechanism. Run A was kept because its
survivors are the new objects.

The recorded plan's first step (harvest `E024`) was deliberately deferred at
the user's direction and on its own merits: it is unfinished, and its likely
outcome moves a floor without bearing on (F). It remains untouched and
running, excluded from every ledger row.

## Adversarial check

- Every prune in the instrument is one-sided by construction and was checked
  to be so: coverage, minimality (with its forward *reservation*
  propagation), forbidden cycles, poison savings, and the reversal symmetry
  break, the last verified empirically to be exactly reversal-closure.
- The enumerator is set-equal to an independently written brute-force
  reference wherever the latter runs, including nonempty controls.
- Every survivor was re-certified: degrees and \(\{C_4,C_8\}\)-freeness
  re-tested with the whole-graph detector, \(S\) recomputed by a **second
  independent** plain-DFS path enumerator and asserted equal to the `E018`
  enumerator's answer, canonical forms via nauty `labelg`.
- The two calibration objects are excluded by *named* hypotheses, not by the
  order window: Petersen\(-e\) has no Hamiltonian \(a\)–\(b\) path
  (\(\max S=8=n-2\)), and the order-14 exemplar is Hamiltonian and
  exactly-two but carries \(C_8\)s.
- A hand-derived chord-pair table entry was found wrong and is recorded
  (`A027` T6).
- A fresh-context `proof-reviewer` audit was delegated (`R003`), targeted at
  exactly the two places where an error would be fatal: whether the descent
  is really lossless, and whether any prune can discard a genuine
  counterexample. **Verdict: PASS at lemma-and-instrument level** — 0
  critical, 4 major, 4 minor, 3 notes. The reviewer reproduced both runs'
  node counts to the last digit from the shipped instrument run outside the
  repository, and re-derived run B's emptiness at orders 19–25 with an
  enumerator it wrote from scratch.
- **The audit's decisive finding, and this session's own blind spot.** The
  original 78,519-check suite looked strong and was, on the load-bearing points,
  vacuous: the \(\{C_4,C_8\}\)-free chord-minimal class is empty below
  order 19, so every enumerator-vs-reference comparison compared two *empty*
  sets, and the depth-15 \(C_{16}\) branch — which produces run B's entire
  table — was only ever called on graphs of order \(\le12\), where it can
  only return `False`. A bug there would have been indistinguishable from a
  proof. Repaired in place with anchor families a6/a7 (539 positive
  \(C_{16}\) instances across \(M=15..34\) against three detectors;
  reversal closure and poison-prune selection verified on the nonempty
  order-19/20 cover sets); suite now 80,131 checks, both interpreters,
  identical histograms. The lesson generalises and is recorded for that
  reason: check count is not coverage, and a suite that never makes its own
  critical sub-test say "yes" has not tested it.
- Two further corrections adopted verbatim: the window-reachability
  extrapolation is **withdrawn** (F3), and the class-emptiness reading of
  orders 27–29 is recorded as such (F4). The cross-check was *strengthened*
  by the audit — restated at isomorphism level it recovers exactly the
  recorded profile objects (1 and 7 classes at orders 19 and 20).

## Canonical records changed

- [ ] `STATEMENT.md`
- [x] `STATE.md`
- [x] `CLAIMS.md`
- [x] `OBLIGATIONS.md`
- [ ] `PROOF.md` (unchanged — no change to the integrated argument for
      statement 0.1)
- [x] `DECISIONS.md` (two rows: decide the disjunction (F) by exhaustive
      enumeration after a proved reduction, rather than proving a disjunct;
      and defer the `E024` harvest)
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: (F) — hence case (5b) — is **decided and empty on the
  Hamiltonian stratum at orders 16–29**, by exhaustive enumeration after a
  proved reduction, audited and independently reproduced; the ladder
  continues, open-ended, and above order 26 it is a class-emptiness ladder
  rather than a poison-forcing one.
- Remaining blockers: (a) the ladder above order 29 (open-ended; days of
  computing per rung on the measured trend); (b) the non-Hamiltonian
  stratum (`A027` T5); (c) nothing else below order 36 — `L046` covers the
  chain branch.
- Recalibration decision: continued, with the target sharpened from
  "(F-S) or (F-T)" to "(F) directly, decided per order".
- Best live alternative or reframing: the bipartite transfer for T5's
  zero-savings bridges.
- Pivot trigger: a survivor that passes the exact stage (a case-(5b)
  residual object — disproof-adjacent); or a rung whose node count breaks
  the \(\times1.9\) trend badly enough to stall the ladder before order 35.
- Best next action: see *Proposed next step*.
- Files a new session should read: `A027`, `E028/README.md`, `R003`, then
  `A026`/`A025` for the frame.

## Plain-language recap

*(see the closing message)*

## Proposed next step

*(see the closing message)*

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 10%
- Previous estimate: 8% (S026)
- Reason for change: for the first time in the programme, the surviving
  proof-side question stopped being "find a lemma nobody knows how to prove"
  and became "run a finite decision procedure". Two small proved reductions
  turned the forcing target into an exhaustive search that is empty at
  orders 16–29, eight orders past the previous frontier and in under an
  hour, and a delegated fresh-context audit passed the reduction and
  reproduced the numbers with independent code. Against: that same audit
  established that the ladder is **open-ended** rather than a window
  closure, and that above order 26 it proves class-emptiness and stops
  informing (F)'s mechanism — so it stopped teaching us anything exactly
  where the mechanism was the point; the result is confined to pairs with a
  Hamiltonian through-path, and the remaining stratum is exactly where the
  near-miss corpus says the escapes live; and even a complete closure of
  case (5b) proves the *cubic reduction*, not the conjecture. The change is
  deliberately small: real, structural, and still two named steps from the
  programme's own deliverable.
