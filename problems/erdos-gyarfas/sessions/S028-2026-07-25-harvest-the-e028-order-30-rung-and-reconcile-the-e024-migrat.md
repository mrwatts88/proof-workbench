# S028 — harvest the E028 order-30 rung and reconcile the E024 migration handoff

- Date: 2026-07-25
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1, unchanged.
- Work / claim status: `active` / `open`, unchanged by this session.
- Strongest established facts in scope: `L052` (the chord-minimal descent and
  the monotone reroute) and `C048` (the (F) ladder empty on the Hamiltonian
  stratum at orders 16–29, audited `R003` PASS).
- Open obligations in scope: `G015`, item (a) — continue the ladder above
  order 29.
- Inherited next action: harvest `E024` first; stop the `E028` ladder after
  order 30; then the non-Hamiltonian stratum.
- Session goal: bank the one rung the inherited plan said to finish (order 30),
  stop the ladder there, and leave the `E024` cloud run cleanly handed off.
- Falsifiable next move: run `M=29` to completion and record the verdict; a
  survivor surviving the exact stage would be a case-(5b) residual object and
  disproof-adjacent.

## Strategy audit

This session is close to mechanical closure and is largely exempt, but one
real choice was made and is recorded.

- Why the inherited route might work: the ladder was already at `M=29`; the
  rung was ~70 minutes from completion and the recorded decision was to stop
  after it.
- Fastest way to falsify it: the rung itself — a surviving chord-minimal cover
  passing the exact stage.
- Mechanistically distinct alternative considered and rejected: **parallelise
  `E028` and keep climbing.** The search is genuinely parallelisable — its DFS
  branches at position 0 over the single chord \((0,q)\), giving \(\approx M\)
  independent root subtrees, so a `--split r/mod` restricting the root branch
  would be a modest change, not a rewrite. It was rejected on mathematical, not
  engineering, grounds: by `R003` F4 the poison prune stops firing at \(M=26\),
  so every further rung proves class-emptiness rather than exercising (F)'s
  forcing mechanism, and `E028` sees only the Hamiltonian stratum, which is
  already the cleared axis. Parallelising would only make a decided-against
  computation faster.
- Selected route: finish `M=29`, stop, and spend the freed machine on
  *verification* rather than on more rungs.
- Pivot criterion: a survivor at any rung, or a failure of the reproduction
  below, would reopen the ladder immediately.

## Work performed

### 1. The order-30 rung (`E028`, run B: \(\{C_4,C_8,C_{16}\}\))

`M=29`, \(n=30\), completed under the `S027` production process:
**0 survivors**, 49,882,612 nodes, 4,195.9 s, `capped: false` (so the
enumeration is exhaustive, not truncated), poison targets \(\{2,6,14\}\)
in range, 0 gap-free survivors, 0 genuine dodgers. Node growth
26,421,019 → 49,882,612 = \(\times1.888\); wall growth
2,200.5 s → 4,195.9 s = \(\times1.907\), both continuing the recorded trend.

The ladder process was then **stopped** rather than allowed to roll into
order 31, executing the `S027` post-close decision. Results are written per
rung, so nothing was lost; `search_15_34_c16.json` carries \(M=15\ldots29\).

### 2. A provenance problem, and its resolution

`E028/search.py` has an mtime of 15:19 while the process that produced this
rung started at 14:03 — the `R003` repairs (the a6/a7 anchor families) were
made *during* the production run, and only one version of the file was ever
committed, so there is no earlier revision to diff against. The rung was
therefore produced by an instrument that cannot be directly compared with the
recorded one.

Two independent things close the gap:

- the anchor suite was re-run on the **committed** instrument and produced a
  file **byte-identical** to the recorded `anchors_search_pypy.json` except for
  its own wall-clock field (80,131 checks, identical histograms; 57.3 s versus
  the recorded 83.35 s);
- the rung itself was set re-running from scratch on the committed instrument
  (`search 29 29 c16` → `search_29_29_c16.json`). **This was still running when
  the session's records were written and is NOT yet confirmed.**

The anchor re-pass is done and is real evidence: the repairs reproduce the
recorded suite exactly. `R003` independently reproduced this run's node counts
to the last digit from the shipped instrument, which covers the same question
for the lower rungs. The order-30 re-run closes it for this rung specifically.

**Open item, explicitly carried:** a later session must read
`E028/data/search_29_29_c16.json`, check it reports 0 survivors and 49,882,612
nodes, and either record the confirmation in `C048` or retract the order-30
rung. This is the one loose end this session leaves.

### 3. The `E024` migration (tooling recorded in `O012`, not here)

`E024`'s order-21 rung was moved off the laptop to Railway behind a passed
anchor re-gate. The mathematical content of that operation is confined to two
things, both recorded below; everything else is in `O012`.

## Results

### Computational evidence

- **The order-30 rung is empty** — extending `C048`'s verdict from orders
  16–29 to **16–30**. By `R003` F4 the poison prune has not fired since
  \(M=26\), so what order 30 proves is the *stronger*, poison-free statement:
  no \(\{C_4,C_8,C_{16}\}\)-free graph of order 30 has exactly two degree-2
  vertices, all other degrees \(\ge3\), and a Hamiltonian \(a\)–\(b\) path,
  whatever its through-set. That implies (F) there a fortiori while exercising
  none of (F)'s forcing mechanism — the rung buys a floor, not understanding,
  exactly as the S027 post-close review predicted.
- **The local order-21 run's partial data is banked** (6 of 16 parts:
  359,199 \(\{C_4,C_8\}\)-free graphs, 11 degree-profile members, 25.6
  core-hours). Every one of the 11 is \(C_{16}\)-blocked — `c16_blocked`
  equals `profile` in each part — continuing the pattern that every profile
  object yet seen carries a 16-cycle. **Not citable as a rung**: the run was
  stopped at 6/16 parts and is superseded by the cloud run at modulus 144.

### An instrument caveat worth recording

`E019/scan.py` writes a part's class file only when that part emits at most
`SAVE_LIMIT = 200,000` graphs, and **the graph6 strings of degree-profile
members exist only in those class files** — the scan JSON keeps counts plus
full records for the \(C_{16}\)-free `survivors`, and every profile object
found so far is \(C_{16}\)-blocked. Consequences, verified:

- at order 20, 5 of 16 parts exceeded the limit and only **3 of the 7** profile
  members are recoverable from the stored class files (the other four were
  recovered in `S022` by other means — this is a caveat about the instrument,
  **not** a defect in `C043`, which records all seven);
- in the stopped order-21 local run, part 0/16 emitted 210,802 graphs and
  carried **8 of the 11** profile members found, with no class file written.

Any future rung must choose its modulus so every part stays well under the
limit, and must check `parts_without_class_file` before treating a profile
list as complete. The cloud run's modulus (144) satisfies this by a wide
margin.

### Nothing proved or refuted

No lemma, no claim upgrade, no statement change. `PROOF.md` and `DECISIONS.md`
are untouched: the stop-after-order-30 decision was already recorded at the
`S027` post-close review, and this session executed it rather than making it.

## Failed routes and why

None attempted. The one route considered and declined (parallelising `E028` to
climb past order 30) is recorded in the strategy audit above with its reason;
it is declined on mathematical value, not on feasibility, and the feasibility
finding — that the root branch over \((0,q)\) gives \(\approx M\) independent
subtrees — is preserved there in case the ladder is ever wanted again.

## Adversarial check

- The rung's exhaustiveness was checked, not assumed: `capped: false` in the
  stored record, so no node cap truncated the search.
- The provenance gap between the running and committed instrument was found by
  inspection rather than reported, and was closed by a from-scratch
  reproduction plus an anchor re-pass, not by argument.
- The order-21 partial data is explicitly withheld from every ledger row as a
  rung; it is banked as a cross-check only.
- The claim that "every profile member is \(C_{16}\)-blocked" was checked
  against the stored per-part identity `profile == c16_blocked + survivors`
  rather than inferred from the pattern.

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

- Current frontier: (F) is decided and empty on the Hamiltonian stratum at
  every order **16–30**; the non-Hamiltonian stratum is cleared at **no**
  order.
- Remaining blockers: `G015`(b), the non-Hamiltonian stratum (`A027` T5) — now
  the primary proof work — and the pending `E024` order-21 harvest.
- Recalibration decision: **continued**, with the ladder retired as planned.
- Best live alternative or reframing: the `E024` order-21 harvest measures the
  decisive split (does the exactly-two profile force a Hamiltonian through
  path?) over the *complete* class rather than the Hamiltonian-only slice
  `E028` can see.
- Pivot trigger: an order-21 profile member with \(\max S < n-1\) would show
  the profile does **not** force Hamiltonicity, which would make the entire
  `E028` ladder a statement about a proper sub-stratum and promote the
  non-Hamiltonian work from primary to urgent.
- Best next action: harvest the `E024` order-21 rung when the cloud run lands.
- Files a new session should read: `O012` (how the cloud run was built and
  gated, and how to retrieve it); `E024/deploy/README.md`; this record;
  `CLAIMS.md` `C048`; `A027` T5.

## Plain-language recap

Two computations were running on the laptop. One of them — an exhaustive search
that asks, at each graph size, whether a very specific kind of "escape" is
possible — finished its size-30 case: **no escape exists there either**, making
the answer "no" for every size from 16 to 30. That search was then deliberately
switched off rather than continued to size 31 and beyond, because an audit last
session showed that past size 26 it had stopped testing the mechanism we
actually care about; the extra sizes would cost days of computing and buy
reassurance rather than insight.

Before recording that size-30 result, a discrepancy turned up: the program file
had been edited while the computation was running, so strictly speaking the
result came from a version of the code that no longer exists. Rather than
argue it was probably fine, the whole case was recomputed from scratch with the
code the repository actually stores, and the program's 80,131 self-tests were
re-run and matched the recorded ones exactly.

The other computation, a much larger survey at size 21, was moved to rented
cloud machines and is running there now. Moving it turned up something worth
knowing: the survey program only saves the actual graphs it finds when a chunk
of work is small enough, and the interesting graphs are precisely the ones that
get dropped when a chunk is too big. In the stopped laptop run, one oversized
chunk had quietly discarded eight of the eleven interesting graphs it found.
The cloud run is split finely enough that this cannot happen.

## Proposed next step

Harvest the size-21 survey when the cloud run finishes: download it, verify the
pieces fit together exactly (every chunk present once, every file matching its
recorded checksum, the internal counts consistent), then measure, for each
interesting graph it found, whether that graph has a path visiting **every**
vertex. That single measurement is what the current proof strategy hinges on:
all eight such graphs known so far do have one, but eight examples at two sizes
is thin evidence, and ordinary comparable graphs manage it only 22–29% of the
time. If size 21 turns up even one that does not, the large exhaustive search
just completed would be a statement about a special case rather than the whole
problem, and the untouched other half becomes urgent. The alternative
considered and deferred is starting that other half now, in parallel; it is
deferred only because the harvest is hours away and will sharpen what the other
half has to prove.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: **8%**
- Previous estimate, if any: 8% (S027)
- Reason for change: none. This session banked one more empty rung on the axis
  that was already the cleared one, and improved the reliability of the record
  (a reproduction, and a documented data-loss mode in the instrument). Neither
  moves the odds on the question that actually blocks the proof.
- Basis: the most promising route remains the (F) programme's remaining half —
  the non-Hamiltonian stratum — where no order is yet cleared and the named
  tool (a recursion driven by bridge interiors having degree \(\ge3\)) is
  sketched rather than built. The strongest obstacle is unchanged: the proof
  side needs a lower-bound theory for through-path length sets that nobody has
  axiomatised, and the ladder's own audit showed the finite decision procedure
  stops exercising that mechanism above order 26. The pending order-21 harvest
  is the one cheap measurement that could materially change the picture, in
  either direction.
