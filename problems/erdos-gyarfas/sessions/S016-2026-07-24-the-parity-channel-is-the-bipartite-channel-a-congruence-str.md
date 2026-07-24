# S016 — The parity channel is the bipartite channel: a congruence structure theorem and the bipartite gadget hunt

- Date: 2026-07-24
- Problem: `P-002`

## Starting checkpoint

- Statement version: 0.1
- Work / claim status: `active` / `open`
- Strongest established facts: `L022` (counterexamples \(\ge19\)
  vertices); `L025`–`L033` the atom/rung/block/pencil program; `L034`
  the generalized ring criterion with its parity, gcd and mod-4
  channels; `C027` (no power-free (D)-gadget of any profile through
  order 15); `C030`–`C033` the pinched catalogue through order 15.
- Open obligations in scope: `G013` (1-atoms; the block question; the
  congruence channels), `G014` (import audits).
- Inherited next action: (i) an odd-\(S\) taut *scan mode* over the
  existing order-\(\le15\) stream ("abort on the first even
  through-path") to produce the parity channel's shape catalogue; (ii)
  the `G014` source audits; with the pencil endgame co-primary.
- Session goal: execute or improve on (i), and give the parity channel
  the reduction theory `A016` M4 recorded as missing.
- Falsifiable next move: prove or refute "vertex-taut + parity-constant
  through-set \(\Rightarrow\) bipartite" — refutation kills the whole
  reframing and sends the channel back to enumeration-bound scanning.
- Note: the order-16 pinched scan launched in S015 was being harvested
  concurrently by a different agent (session `S017`); per the user it is
  that agent's job and was left untouched here — no `E013` file was read
  for content or written by this session.

## Strategy audit

- Why the inherited route might work: the parity channel had never been
  shape-scanned, and the banded scanners provably cannot see
  \(S=\{3,7\}\)-type gadgets, so a dedicated mode would produce genuinely
  new catalogue data.
- Fastest way to falsify it: notice what the scan would actually cover.
  Its class — (D)-gadgets at orders \(\le15\) — is exactly the class
  `C027` already proved empty of power-free members, and profile-agnostically
  so. The scan could therefore only ever return *near-miss shapes*, never a
  witness, and it would cost a full re-scan of a 61.8M-graph stream to do it.
- Mechanistically distinct alternative or reframing: ask what all-odd
  \(S\) *is*, structurally, instead of scanning for it. Parity of a
  through-set looks numerical, but in a graph where every vertex lies on
  some through-path it is forced by a 2-colouring — which, if true,
  converts the channel from "enumerate paths and check parity" into
  "generate bipartite graphs and check forbidden cycles", a class several
  orders cheaper.
- Selected route and reason: the reframing, with the theorem proved and
  machine-verified *before* the search was built. Expected value
  dominates: it either fails fast (one counterexample among ~100k small
  instances) or it upgrades the memo's bipartite remark from "an
  instance" to "the whole channel" and reaches orders no other thread
  can. It also removes an unverified external dependency (`G014` item 2)
  instead of waiting on it.
- Pivot criterion: the exhaustive small-order check refuting the
  equivalence (→ revert to the inherited scan mode); or any power-free
  member of the bipartite class (→ disproof protocol immediately).

## Work performed

- **Proved `L035` (`A017` T0–T5).**
  - T0: for *any* vertex-taut two-terminal graph, every cut vertex
    separates the terminals, the block–cut tree is a path, \(S\) is the
    Minkowski sum of the block through-sets, and each block is vertex-taut
    — `A014` T3.1/T3.2/T3.4 with the degree hypotheses deleted (their
    recorded proofs never used the degrees).
  - T1 (parity fan lemma): in a 2-connected graph containing an odd
    cycle, any two vertices are joined by simple paths of both parities.
    Proof: attach an apex \(z\) adjacent to \(a,b\) (2-connectivity is
    preserved), take a 2-fan from \(z\) to the odd cycle, and use its two
    arcs, whose lengths sum to an odd number.
  - T2 (the structure theorem): for a vertex-taut two-terminal graph,
    \(S\) is parity-constant **iff** the graph is bipartite; all-odd
    corresponds to terminals in opposite colour classes. Tautness is
    exactly the hypothesis that fails in the pendant-triangle example.
  - T3 (the criterion): **any** connected bipartite power-free graph with
    at most two sub-cubic vertices disproves 0.1 — case \(t=0\) outright,
    \(t=1\) via `L025` R4, \(t=2\) by a 3-ring of the graph (all-odd) or
    of its pendant lift/reduction (all-even). No path enumeration, no
    tautness test, no external import.
  - T4 (completeness): every parity-channel witness is vertex-taut and
    hence bipartite, or non-taut and hence already a disproof by `L027`.
    Scope caveat recorded: \(\Theta(3,3,3)\) is vertex-taut,
    non-bipartite with \(S=\{3\}\), so channel (ii) is **not** covered.
  - T5: the \(C_4\)-free counting bound \(3q-4\le\binom p2\) on part
    sizes, used to skip provably empty splits inside an exhaustive run.
- **Verified the theorem before recording it (`E015/verify_parity.py`).**
  Every connected graph of order \(\le7\) (994 graphs, 39,690 ordered
  terminal pairs) and every connected \(C_4\)-free graph of orders 8–9
  (926 graphs — the full geng counts — 63,696 pairs), through-sets and
  essential masks by explicit simple-path enumeration: T2's kill
  condition never fired (952 hypothesis instances), T1 held in 27,196,
  T0's chain/Minkowski structure in 33,962, and all 10,788
  parity-constant non-bipartite pairs were non-taut.
- **Built and ran `E015/bipscan.py` (`C034`).** genbg `-Z1 -d2` over the
  T5-admissible splits generates the class exactly; per graph the test is
  a 2-colouring plus exact existence tests for \(C_8\)/\(C_{16}\).
  Result: **no power-free member at any order \(\le21\)** — class sizes
  0, 0, 2, 1, 6, 8, 75, 197, 2,715, 10,865 at orders 12–21 — with
  **every** member containing a \(C_8\) and the minimum \(C_8\) count
  never below 13. An order-22 run was launched and left unfinished
  (heavily loaded machine); it is deliberately excluded from `C034`.
- **Two by-products of the same run:** no bipartite 1-atom (the
  one-sub-cubic-vertex column: 332 candidates at order 20, 1,208 at 21)
  and no bipartite counterexample to 0.1 (the min-degree-\(\ge3\) column:
  50 at 20, 69 at 21) at orders \(\le21\) — the second verifies
  internally the range that `G014` item (2) was going to supply.
- **Corrections recorded** to `A016` M3 and M4 (both too weak; see
  below) and to `G014` item (2)'s gating status.

## Results

- Proved claims: `L035` (T0 degree-free chain decomposition; T1 parity
  fan lemma; T2 parity structure theorem; T3 bipartite assembly
  criterion; T4 channel completeness with its scope caveat; T5 part-size
  bound).
- Refuted in-session: `A016` M3's verdict that the memo's bipartite
  reformulation is "the canonical instance, not an equivalence" — it is
  an equivalence on the taut side, which is the only side any rung of
  `G013` works with; and `A016` M4's "the parity channel has no
  reduction theory yet" — the pendant shift toggles the two bipartite
  sub-cases (all-odd \(\leftrightarrow\) all-even) rather than
  destroying the structure. Both corrections *strengthen* the audited
  external memo. Also retired (as superseded, not falsified) the
  inherited odd-\(S\) scan mode.
- Computational evidence: `C034` (the hunt, orders 12–21) and the
  verification tables in `E015/README.md`.
- Provisional insights (not lemmas): the margin observation — the parity
  class is blocked by \(\ge13\) \(C_8\)s uniformly, against 3–7 for the
  pinched channel's equality blocks, so the parity channel looks
  *further* from a witness, not closer; and the sharpened Thread E
  target (a "bipartite + min degree 3 + \(C_4\)-free \(\Rightarrow C_8\)"
  theorem is false at large order, since bipartite double covers of
  `C009`'s large-girth cubic graphs lie in the class, so any bipartite
  EGC proof must be order-bounded or must consume \(C_{16}/C_{32}\)).
- Imported facts needing verification: unchanged (`G014` items 1, 3–6);
  item 2 is no longer needed by this thread.

## Failed routes and why

No route abandoned on evidence. One inherited plan (the odd-\(S\) taut
scan mode) was retired as superseded: the structure theorem makes its
class a strict sub-case of a cheaper, wider search, and its stated
purpose (shape data) is delivered by `E015`'s class listing instead. The
order-22 leg failed only on wall-clock, not mathematically.

## Adversarial check

- The theorem's own kill condition was run exhaustively before the
  theorem entered the ledger, over two independent families (all small
  graphs; all small \(C_4\)-free graphs), with through-sets computed by
  brute-force path enumeration rather than by the theory being tested.
- The search pipeline was cross-validated against the *other* generator:
  `crosscheck 14` rebuilds the class from the `E010`/`E013` geng stream,
  canonicalizes both sides with `labelg`, and asserts set equality.
- The cycle detector was cross-validated against an independent
  brute-force enumerator on all 994 connected graphs of order \(\le7\)
  and 1,000+ bipartite graphs of orders 8–11, plus known spectra
  (Petersen \(\{5,6,8,9\}\) matching `E013`'s recorded anchor; Heawood
  \(\{6,8,10,12,14\}\); \(Q_4\) bipancyclic for the \(C_{16}\) test).
- The split-skipping bound (T5) was validated by running genbg on every
  split it rejects at orders 8–14 and confirming emptiness — so the
  exhaustiveness claim does not rest on the bound being *believed*.
- Named-object control: the unique cubic member at order 14 is the
  Heawood graph, confirmed by canonical form — the class had to contain
  the (3,6)-cage, and it does.
- Claim discipline: the order-22 run is excluded from every record
  because it did not finish; the margin data is labelled descriptive,
  with the explicit note that large-girth bipartite cubic graphs show
  \(C_8\)-freeness in the class is not impossible in general.

## Canonical records changed

- [x] `STATEMENT.md` (unchanged; statement version stays 0.1)
- [x] `STATE.md`
- [x] `CLAIMS.md` (`L035`, `C034` + dependency notes)
- [x] `OBLIGATIONS.md` (`G013` sub-question (c) split; `G014` item 2 de-gated)
- [x] `PROOF.md`
- [x] `DECISIONS.md`
- [x] `LOG.md`
- [x] `problem.json` and index
- [x] Session-scoped changes committed
- [x] Commit pushed to configured upstream

## Ending checkpoint

- Current frontier: finite exclusions unchanged (`L022`); the pinched
  channel's catalogue as of order 15 here — the order-16 harvest is
  `S017`'s, recorded concurrently and not folded into this session's
  records; **the parity/mod-4 channels
  are now identified with the bipartite class and empty through order
  21** (22 with a pendant), with no bipartite 1-atom and no bipartite
  counterexample in that range either.
- Remaining blockers: `G013` (1-atoms; the pencil endgame and higher
  pinched rungs; the odd-prime-gcd channel, now the only congruence
  channel with no structure theory; the missing parity analogue of
  `L032`'s block extraction), `G014` (items 1, 3–6), `G007`, `G002`,
  `G003`.
- Recalibration decision: pivoted *within* Thread B — the inherited scan
  mode was replaced by a theorem plus a different search instrument, and
  the thread's disproof leg is now largely executed rather than open.
  Every other thread stays live per the standing instruction.
- Best live alternative or reframing: Thread A (the pencil endgame, fan
  case first); Thread B3 (structure theory for the odd-prime-gcd
  channel — is there a mod-\(p\) analogue of `L035` under condition
  (D)?); Thread C (the cubic census at order 30).
- Pivot trigger: any power-free member of the `E015` class at order 22+
  (immediate disproof by `L035` T3); a pencil-type band-4 taut core at
  order 16+; a `G014` audit overturning an assumed bound.
- Best next action: finish the order-22 bipartite leg (splits
  \((9,13)\), \((10,12)\), \((11,11)\); re-run `bipscan.py run 22` on an
  unloaded machine, or split by `res/mod`), then open Thread B3 — the
  odd-prime-gcd channel — by testing whether condition (D) forbids
  \(\gcd(S)\) from having an odd prime factor, with \(\Theta(3,3,3)\) as
  the recorded obstruction to any purely parity-style argument.
- Files a new session should read: `STATE.md`, `A017`, `E015/README.md`,
  `A016` + the memo reference, `A015`, `CLAIMS.md` `L031`–`L035` /
  `C030`–`C034`, `OBLIGATIONS.md` `G013`/`G014`, this session.

## Plain-language recap

The programme tries to disprove the conjecture by building a small
two-terminal "engine" and chaining copies of it into a ring, so that the
ring's cycle lengths are sums of the engine's path lengths; the engine
wins if those sums can miss every power of two. Last session an outside
review pointed out that sums can miss the powers of two by *arithmetic*
— for instance, if every path through the engine has odd length, then
adding up an odd number of them always gives an odd number, and no power
of two is odd. That opened a hunting ground nobody had mapped.

This session proved what that hunting ground actually is. In an engine
with no idle parts, "all path lengths odd" is not a numerical
coincidence: it happens exactly when the engine can be coloured with two
colours so that neighbours differ and the two terminals get different
colours. So the arithmetic condition and a purely visual condition are
the same condition. Two consequences follow. First, checking a candidate
no longer requires listing its paths — colour it, then look for the
forbidden cycle lengths; that is enormously cheaper. Second, generating
two-colourable graphs is now known to miss nothing in this channel, so
the search is complete rather than merely suggestive.

The rebuilt search then ran far past where the general search dies. The
general hunt is exhausted at 15 vertices; this one is exhausted at 21
(22 if the engine has a dangling vertex), and it found nothing — every
single candidate contains an 8-cycle, and not narrowly: the fewest
8-cycles any candidate has is thirteen. The same run also confirms, from
our own computation instead of an uncorroborated citation, that no
two-colourable counterexample and no two-colourable "single-defect"
graph exists in that range. What is *not* covered is the third
arithmetic trick from the outside review — all path lengths sharing an
odd common factor — and a small example shows that trick has nothing to
do with two-colouring, so it is now the one channel with no theory
behind it at all.

## Proposed next step

Two moves, in order. First, finish the 22-vertex leg of the same search
(it was launched this session and was still running when the machine
became too busy); it either extends the empty range by one order or —
if it finds anything — disproves the conjecture on the spot. Second,
open the one arithmetic channel that this session's theorem does *not*
cover: engines whose path lengths all share an odd common factor. The
concrete first question is whether the degree condition (every internal
vertex has at least three neighbours) rules that out, since the obvious
small example that realises it — a three-way theta with three paths of
length 3 — fails exactly that condition. Considered and deferred: the
bottleneck ("pencil endgame") fight, which is untouched and still
co-primary; the 3-regular census extension to 30 vertices; and the
remaining source audits, which no longer gate this thread.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: 4%
- Previous estimate, if any: 4% (S015)
- Reason for change: none. The session produced a genuine theorem and a
  large coverage gain, but in the negative direction for a disproof, and
  the margin data (never fewer than thirteen blocking 8-cycles) suggests
  this channel is further from a witness than the pinched one rather
  than closer. The proof side gained a sharper target but no theorem,
  and the ceiling correction from the previous session still limits what
  the whole engine programme can deliver.
- Basis: most promising routes — the pencil endgame and bipartite EGC on
  the proof side, the cubic census at order 30 and the untheorised
  gcd channel on the disproof side; strongest obstacles — nothing yet
  forces spread or power cycles at any generality, the gcd channel has
  no structure theory, and success on the whole assembly interface would
  still only reduce the conjecture to cubic graphs; evidence — `L035`,
  `C034`, and the verification tables in `E015`.

This is a subjective research outlook, not mathematical evidence or a claim-status
promotion.
