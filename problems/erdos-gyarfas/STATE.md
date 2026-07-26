# Current state

- Last updated: 2026-07-26 (S032 — **the dossier has a proved case of statement
  0.1, and a proof that its own machinery cannot produce another one.** Nine
  delegated Opus workers, aimed at 0.1 itself rather than at `G015`, with the
  orchestrator re-verifying every load-bearing computation independently.
  **`L061`: every planar graph with \(\delta\ge4\) contains a cycle of length 4
  or 8** — also projective-planar, and 2-connected toroidal/Klein — via
  `L060` (in a \(C_4\)-free graph a 5-cycle with three edges in triangles forces
  a \(C_8\); verified exhaustively to order 11) and a discharging bound
  \(m\le2n-2\chi(S)\) colliding with \(m\ge2n\). Prior art: **not found**, in
  either the Erdős–Gyárfás or the planar-Turán literature; the by-product
  \(\mathrm{ex}_P(n,\{C_4,C_8\})\le2n-4\) appears to be the first planar Turán
  bound for a *set* of cycle lengths. **`L064`: `G013`(c) is resolved** — a
  gadget whose through-set lies in a single residue class mod any \(m\ge3\)
  makes 0.1 already false via a proper subgraph, so \(d(S)\in\{1,2\}\) always;
  the odd-prime-gcd channel, open with no theory and no search since S016, is
  closed together with every modulus (conditional only on the Fan import,
  `G017`). **`L059`, the finding that reframes the whole dossier:** any class
  closed under subdivision fails against any target avoiding \(t\mathbb N\),
  because \(L(G^{(t)})=t\,L(G)\); with \(t=3\), **no subdivision-closed
  hypothesis implies 0.1's conclusion**, and every through-set / ear / theta /
  exchange / interference law is subdivision-covariant. So the (F) programme and
  `L048`–`L052` cannot reach 0.1 however far they run — `L049` remains a correct
  theorem, but not a route. Two further barriers: **`L062`**, no additive
  surgery on a minimum counterexample can contradict anything (only
  length-preserving or power-of-two-multiplying reductions can), which is why
  the orchestrator's own contraction lemma audited **true but vacuous**; and
  **`L063`**, girth does not localize the spectrum (cubic graphs of girth exactly
  \(g\) with no cycle in \([g+1,M]\); explicit 768-vertex witness), so no
  shortest-cycle anchor works. Residue: **`L065`**, a minimum-order
  counterexample is non-bipartite, bridgeless, subgraph-minimal, blockwise
  non-bipartite and not a \(2^s\)-lift. **Frontier imports the dossier lacked:**
  Exoo arXiv:1403.5636 (\(G_{78}\), \(G_{450}\), \(G_{420}\) — the real
  near-counterexamples, now the primary calibration objects, `G018`);
  Heckman–Krakovski conclude "\(2^m\), \(2\le m\le7\)", **not** "4 or 8" (the
  buckyball is a 3-connected cubic planar \(\{C_4,C_8\}\)-free witness);
  Liu–Montgomery JAMS 2023 makes 0.1 entirely a bounded-degree question;
  Dean–Lesniak–Saito 1993 caps the mod-\(k\) route at \(k\le4\) permanently;
  Erdős believed 0.1 **false**. Withdrawn: "every non-planar graph has a cycle
  \(\equiv0\bmod4\)" is in print (Győri et al., JCTB 176 (2026), Lemma 2).
  Counterexample side: none; margin \(f(k)/2^{k+1}=1.25,\,1.5,\,\ge1.69\) is
  **widening**, evidence that 0.1 is true. No floor, status or statement changed)
- Previous update: 2026-07-26 (S031 — **the kill test that was never run: the
  interpolation genre is empty.** The recorded next action was to *prove*
  (INT). The dossier's binding kill discipline says test a candidate against
  **every** calibration object first; `C050` tested (INT) against the 24
  profile objects on disk and never against Calibration object #3, which S030
  had built eight theorems earlier in the same attempt. **`L056`:** that
  object — \(F-ab\) for \(F\) cubic, 3-connected, of girth \(\ge17\) — is a
  vertex-taut \(\{C_4,C_8\}\)-free exactly-two-profile pair with
  \(\min S\ge16\), because an \(a\)–\(b\) path plus the deleted edge is a
  cycle of \(F\). So **(INT) and (INT-14) are both false**. The delegated
  audit `R004` then made this **much stronger**: its finding F4 refuted the
  attempt's "no such object below order 70" clause with an explicit
  **order-30** witness — the **truncated Petersen graph** (every vertex
  replaced by a triangle; cubic, 3-connected, spectrum below 13
  \(=\{3,10,11,12\}\), so \(\{C_4,C_8\}\)-free) minus a **link** edge,
  giving a 2-connected exactly-two-profile pair with \(S=[9,26]\), hence
  \(8\notin S\). Chaining two copies at a cut vertex gives order 59 with
  \(S=[18,52]\), so \(14\notin S\). **(INT) is therefore false *inside* the
  case-(5b) window, not merely asymptotically**, with no import at all
  (verified, `E030`). `C050` could not have caught it: nothing with
  \(\min S>8\) has ever been *generated*, because the ladders stop at order
  21 and the smallest witness has order 30. **`L057`:** the natural repair —
  relativizing the threshold to \(\min S\), which is what the recorded pivot
  trigger does implicitly — fails too. The **triangle expansion** of a
  bipartite cubic 3-connected graph of girth \(\ge10\), minus an edge far
  from the triangle, is a *non-bipartite* class member with a parity hole at
  \(\min S+1\ge10\), so \(S\supseteq[\min S+c,\max S]\) fails for every \(c\)
  (import `X004`, existence use inside a negative result). **`L057` FAILED its audit
  twice and is NOT ESTABLISHED.** Round 1 (`R004` F1–F3, F5): the hole was not
  proved to open, two false numeric steps, and the named witness provably
  fails. Round 2, against the repairs: **F11** (the diameter route is a non
  sequitur once \(ab\) is fixed — repaired again, the requirement is now on
  the **order** via the tree ball bound \(\lvert B(\{a,b\},r-1)\rvert\le
  2^{\,r+1}-2\), which is automatic at \(g=10\)) and **F3′, still open**:
  `X004`'s 3-connectivity clause has **no source**, since Erdős–Sachs and the
  double cover supply none and cages — its only previous support — were
  withdrawn in the same revision. So `L057` sits at `proposed` and **may not
  be cited at all**. The genre conclusion does not depend on it: `L056` kills
  the absolute form and the bipartite one-liner kills the relativized form
  against a bipartite defender; what is open is exactly the *non-bipartite*
  relativized kill.
  **The genre is empty, and it is the third**: congruence (`C037`),
  membership (`L045`/`C045`), interpolation. One diagnosis fits all three —
  every class-level hypothesis is **local and hereditary**, hence inherited by
  large-girth cubic graphs minus an edge, and the two hypotheses the residual
  object has that those do not — power-freeness **above the girth**, and
  minimum-order minimality — have never been consumed by an (F)-side lemma.
  Conditional residue: any interpolation lemma plus `L042`'s forced
  memberships would pin \(S\) into one dyadic band,
  \(\max S<2\min S+O(1)\) — `L031`/`L032`'s block-question constraint; a
  convergence, not progress. **`L058`:** `A022` W1-T8 re-derived from the
  current block-order floor of 21 — **either \(H\) is 2-connected or
  \(n_0\ge42\)** — so the case-(5b) window is \(n_0\in[23,41]\)
  (\(H\)-orders \([22,40]\)) and the stopped `E028` ladder is **ten** rungs
  short of it, not four. That sharpens S030's ceiling finding rather than
  softening it. No floor, status or statement changed; both refuting objects
  are far from power-free. Audited `R004`)
- Previous update: 2026-07-26 (S030 — **the non-Hamiltonian stratum gets an
  engine, and the (F) programme gets a ceiling.** Three proved rows and one
  measurement, no generation. **`L053`:** a cubic non-Hamiltonian graph of
  girth \(\ge17\) minus an edge is an exactly-two-profile, 2-connected,
  \(\{C_4,C_8,C_{16}\}\)-free pair with **no** Hamiltonian through-path — so
  `C049`'s 27/27 cannot be promoted to a lemma at class strength, the
  non-Hamiltonian stratum is unavoidable, and calibration object #3 joins
  Petersen\(-e\). Asymptotic: it exhibits nothing in \([18,35]\) and moves no
  floor. **`L054`:** the bipartite exclusion dichotomy — a bipartite piece with
  \(\le2\) sub-cubic vertices inside a power-free graph disproves 0.1 (`L035`
  T3); recorded in three logical forms because the dichotomy form is *not* a
  contradiction inside `G015`. **`L055`:** the positive-savings theorem —
  **every** off-path component of a longest through-path admits a bridge with
  savings \(\ge1\), and \(\ge2\) when it has three or more attachments (the
  Y-identity \(\sigma(i,k)=\sigma(i,j)+\sigma(j,k)+2\beta\), maximality alone).
  `A027` T5's zero-savings obstruction **does not arise**, and `L052`(iii)'s
  reroute machinery transports from chords to bridges. The stratum is still
  cleared at **no** order (`A028` T8: components are not thinnable edge by
  edge, and the savings are per component, not per position).
  **The architectural finding:** `L046` supplies 2-connectivity only below
  order 36, so the (F) programme closes case (5b) for \(n_0\le35\) and **cannot
  prove `G015`** however far the ladder runs; with `R003` F4 and `L053` its top
  rungs are proving something that must stop being true. The ladder is demoted
  to a source of floors. **Successor architecture: (INT) ∧ (L-A)** — (INT)
  says \(S\supseteq[8,\max S]\) for a vertex-taut \(\{C_4,C_8\}\)-free
  exactly-two-profile pair; with \(\max S\ge14\) it forces \(14\in S\), poison,
  hence (F-S) **at every order**. `C050`/`E029` kill-tested (INT) on data
  already on disk: 24 recorded profile objects, **zero violations**, every hole
  in \(\{4,5,6\}\); the constant 8 is the smallest the corpus permits; a hole at
  14 needs five more degree-2 vertices than the profile has. New en route: a
  second non-interval profile object, at order 20)
- Earlier update: 2026-07-25 (S027 — **(F) is no longer a lemma to find; it
  is a finite decision procedure, and it comes back empty.** Two proved
  reductions (`L052`, `A027` T1/T2) — the **chord-minimal descent** (on a
  pair with a Hamiltonian \(a\)–\(b\) path the chords cover every path
  position, and any inclusion-minimal subcover inherits every hypothesis of
  (F)'s negation) and the **monotone reroute** (interval-disjoint chord
  families are real paths, so a savings hit certifies a poison length,
  monotonically and on prefixes) — turn the forcing target into an
  exhaustive per-order enumeration. Two aims were sharpened inside `A025`
  T4's frame: decide the **disjunction** (F) rather than (F-S)/(F-T)
  separately, which hands us \(C_{16}\)-freeness as a free hypothesis, and
  use the whole poison set \(\{2,6,14,30\}\). Verdict (`E028`/`C048`):
  **empty at every order 16–30** — the last completed rung, and the last that
  will be run (`S028` stopped the ladder there) — so case (5b)
  is closed there for every residual object with a Hamiltonian
  through-path. Audited: **`R003` PASS** at lemma-and-instrument level
  (0 critical / 4 major / 4 minor / 3 notes; all four majors repaired in
  place), and its two scope corrections are load-bearing: the ladder is an
  **open-ended computation**, not a window closure (wall-clock growth
  1.8–2.4 per rung), and above order 26 the poison prune stops firing, so
  orders 27–29 prove the **stronger** poison-free class-emptiness statement
  and exercise none of (F)'s forcing mechanism. En route: the **first
  \(\mathcal G\)-profile objects at orders 21 and 22** (10 and 43
  chord-minimal, 3 and 16 isomorphism classes), *all* doubly blocked
  (\(14\in S\), \(C_{16}\) present), and the first in-window exactly-two
  objects whose \(S\) is **not** a full interval — so saturation is not the
  mechanism, and the real one survives its first counterexamples. Adversarial
  audit `R003` delegated. Named residue: the **non-Hamiltonian stratum**
  (`A027` T5). `E024` untouched, still running, excluded from every ledger
  row)
- Earlier still: 2026-07-25 (S026 — **the corpus dissection is spent:
  the dodge mechanism is extracted, two candidate mechanisms are
  killed, and the interpolation lemma splits into (L-A) ∧ (L-B) with
  a validated formal engine for the long-range half.** Over the
  9,061-row `E026` corpus vs the eight profile objects + a 556-member
  control (`E027`/`C047`, attempt `A026`): the dodge economy has
  exactly **three rigid shapes** (A: short, \(\max S=13\) walls; A′:
  distance exactly 7; B: long-range, even part \(\subseteq4\mathbb
  Z\), holes at \(\{6,10,14\}\)); the dodge is **pair-local**
  (frontier members carry five saturated sibling pairs — member-level
  lemmas dead) with the frontier at **ndeg2 = 4 at order 20** (the
  profile load-bearing by two subdivision vertices); **99.1% of dodge
  rows smooth to class-violating reduced graphs** (near-misses are
  subdivisions escaping the class constraint; the profile is the
  subdivision-free stratum). The **span law** is proved (no chord of
  span 3 or 7 on any path in a \(\{C_4,C_8\}\)-free graph) and the
  **first-order chord-exchange calculus** generates the entire top of
  \(S\) down to 10 — including 14 — on all eight profile objects
  while respecting every dodger hole: the missing tool sharpens to
  **span/savings combinatorics of longest-path chord systems**.
  Floors unchanged; `E024` (order-21 rung) still **running**,
  excluded from every ledger)
- Problem: `P-002` — Erdős–Gyárfás Conjecture

## Exact target

Every finite simple undirected graph of minimum degree at least \(3\) contains a
cycle whose length is a power of two. See normalized `STATEMENT.md` version 0.1.

## Established

- `L001`–`L006`: block and edge-minimal reductions; counterexamples have
  \(\ge11\) vertices (hand proofs).
- `L008`–`L016` saturation package with delimitations.
- `L017`/`L018`/`L022` finite exclusions: every counterexample has at
  least **nineteen** vertices; extremal \(\{C_4,C_8\}\)-free window
  \([19,24]\); census capped at order 18.
- `L019`–`L024` the voltage-lift program, closed as a theorem
  (collision wall, reviewed `R001`).
- `L025`–`L030`: atom reduction; rung completeness; lobe decomposition;
  taut rungs \(s_{\min}\le3\) closed \(C_4\)-only; cubic reduction
  modulo 1-atoms.
- `L031`–`L032`: the pendant/block reduction — taut 2-atoms exist iff a
  power-free vertex-taut 2-connected **core** with \(s_{\max}\le2s_{\min}\)
  exists (the block question).
- `L033`: the band-4 pencil dichotomy. With \(d(x,y)=4\), either two
  internally disjoint 4-paths exist (equivalently a \(C_8\) through both
  terminals) or all 4-paths share one internal vertex; no
  \(C_4\)-freeness needed, and under it the pencil is terminal-adjacent
  with a rigid fan.
- `L034`: the generalized ring criterion — a power-free (D)-gadget
  disproves 0.1 whenever **some** \(L\)-fold sumset of \(S\) avoids the
  powers of two (pinch, all-odd, odd-prime gcd, mod-4 channels).
- **New (S016): `L035`, the parity structure theorem and the bipartite
  assembly criterion.** For a vertex-taut two-terminal graph,
  parity-constancy of the through-set is **equivalent** to
  bipartiteness (all-odd = terminals in opposite colour classes). Hence
  (T3) **any** connected bipartite power-free graph with at most two
  sub-cubic vertices disproves 0.1 — no path enumeration, no tautness
  test, no external import — and (T4) bipartite generation is an
  exhaustive instrument for `L034` channels (i) and (iii), modulo the
  standing 1-atom relativization. Not valid for channel (ii): the theta
  graph \(\Theta(3,3,3)\) is vertex-taut, non-bipartite, \(S=\{3\}\).

- **New (S018): `L036`, 1-atom completeness.** A 1-atom in the recorded
  sense (unique sub-cubic vertex, of degree 1 **or** 2) exists iff a
  counterexample exists — attach one pendant vertex to a counterexample.
  So the unrestricted 1-atom question is *conjecture-complete*, `L029`'s
  "cubic reduction modulo 1-atoms" is vacuous as originally stated and
  is restated with **tight** 1-atoms (exceptional degree exactly 2),
  and `A012` Remark T4.1 is withdrawn as unproved.
- **New (S020): `C036`/`C037` — `L041`'s decisive order is empty and
  the congruence route is closed.** The order-16 \(\mathcal G\)-profile
  scan (`E018`): 346,573,602 stream graphs (24-part split, sum
  reproduced by an independent unsplit `geng -u`), 29,713,305 in the
  profile class, **every one blocked by a \(C_8\)** (\(C_{16}\) never
  decisive), zero power-free — so \(\mathcal G\) has no order-16
  member and **every tight 1-atom has order \(\ge18\)** (`C036` with
  `L041`). Proximity datum: the minimum \(C_8\) count over the class
  is **1** (the bipartite class never went below 13). The mod-4
  companion (`A021`, instrument `E018/mod4.py`): the residual object's
  forced-membership profile is *realized* by vertex-taut \(C_4\)-free
  cores from order 10 — one order-10 witness **is Petersen\(-e\)**
  (labelg-verified) — with both admissible residue patterns and no
  invariant (`C037`), and the chain-calculus identity caps
  congruence information at parity (`A021` T1: the
  \(2|E(P)\cap E(Q)|\) leak). **No congruence-type theorem at any
  modulus can exclude case (5b) from the forced hypotheses alone**;
  the surviving proof-side levers are the chain-cancellation tension
  (Minkowski-additive) and mechanisms that make power-freeness itself
  fight (the band-4 pencil is the model — it is exactly the constraint
  Petersen\(-e\) violates). Petersen\(-e\) is the standing calibration
  object: any proposed case-(5b) exclusion must fail on it unless it
  invokes power-freeness or minimality.
- **New (S021): `L043`–`L047`, `C038`–`C040` — the chain case spent,
  the instrument built, the frontier moved.** Proof side: if the
  residual object's \(H\) has a cut vertex, every prefix and suffix of
  its block chain is forced by [min]-closures to meet all three
  forbidden families and to be non-bipartite (`L043`), the cancellation
  is quantified once and for all (`L045`: three exponent-disjointness
  conditions per cut — and therefore memberships alone can **never**
  exclude the chain case), and per-block `C027`-class order bounds give
  the dichotomy: **either \(H\) is 2-connected or \(n_0\ge36\)**
  (`L046`; 32 on the `C027`+`C036`-only lineage). The chain-case
  analogue of Petersen\(-e\) does not exist over blocks of order
  \(\le14\) (`C038` — kill refuted in range, single mechanism, named
  15/16 rung open). New forced structure on every residual object:
  terminal **power** saturation (`L044`, filter strength). Search side:
  `G014` item 6 is **discharged** — `E019`'s `genc48` (geng + PREPRUNE
  \(C_8\) plugin, 146 anchors both interpreters, 23 set-equality
  checks, cubic-24 external positive control) replaces
  filter-the-stream from order 17 up (~75× cheaper at 16, ~45,000×
  smaller output). **Order 17 is empty** (`C039`): tight 1-atoms
  \(\ge19\), \(\mathcal G\)-members \(\ge18\), `C027`'s whole class
  empty through 17; at the boundary (three degree-2 vertices, orders
  16–17) \(C_{16}\) is decisive — the first time in the dossier.
  Flagged min-degree-3 sweep audited (orchestrator slice checks at 18,
  three parts, 38.7M stream graphs, all clean) and extended by the
  same-day follow-up harvest to order 20: **no
  \(\{C_4,C_8\}\)-free \(\delta\ge3\) graph through order 20**
  (`C040`), so **every counterexample has \(\ge21\) vertices**
  (`L047`, extremal window now \([21,24]\) — four orders wide). The
  same harvest emptied the bipartite class at order 24 on the new
  instrument (`C034` extended; clean through 24, 25 with a pendant).
  External input: the MathOverflow-512914 quote (user-supplied) —
  cubic-20 figures now reproduced *exactly* (510,489 / 36,101, stage
  A), its cubic→min-degree-3 step **rejected** (that inference is the
  open `G015`) and superseded by the internal stage-B run.
- **New (S022): `L048`, `C041`–`C043` — the interference lever run to
  its verdict, and the atom floors at 20.** The dissection of the
  closest known objects (the min-\(C_8\) exemplars at orders 14–16,
  exhaustively re-extracted — 11/20/103 graphs with \(\le3\)
  \(C_8\)s — and the three-degree-2 \(C_{16}\) boundary at 16–17)
  landed the **interference outcome**: all **553** blocking cycles are
  two-through-path symmetric differences, for every admissible
  terminal reading; the recorded non-interference pivot trigger did
  **not** fire (`C041`). The property is empirically **exactly
  vertex-tautness-shaped** — a complete biconditional on the profile
  class at orders 10–12, zero failures over all 12,313 vertex-taut
  pairs of all connected graphs of orders 4–7 (`C042`) — with the
  necessity direction proved: interference cycles are confined to the
  essential subgraph (`L048`(i)). `L048` fixes the calculus:
  interference is the \(t=1\), leak-**pinned** case of `A021` T1's
  identity (a realization statement — the genre that survives both
  kill theorems `C037`/`L045`), and under interference-completeness
  \(\mathrm{Spec}(B)=T_1(H,a,b)\cup(S+2)\): the tight 1-atom's entire
  power-freeness becomes through-path-system arithmetic. On the table,
  labelled: candidate lemma **T5** ("vertex-taut \(\Rightarrow\)
  interference-complete", `A023`) with ordered kill tests, and the
  order-windowed forcing target **(F)**, calibrated on Petersen\(-e\)
  **and** the new order-14 exemplar `M?AA@?WcKWHOWOL??` (full
  membership triple, 3 interference \(C_8\)s). Search side (`C043`):
  order 18 profile-empty (class 108,447); order 19 carries the
  **first-ever profile member** (class 74,589) —
  `R???C@?GC_B?@_aAA_aP?W_?BO@Gc?`, vertex-taut, 2-connected,
  non-bipartite, blocked **twice independently** (46 \(C_{16}\)s;
  \(S=\{5..18\}\ni6,14\)) — and the 0-/1-buckets are empty at both
  orders, so **every tight 1-atom and every \(\mathcal G\)-member has
  order \(\ge20\)** (direct 1-bucket route and `L041` route agree);
  \(C_{16}\) is decisive on the whole \(\le4\)-degree-2 stratum at 19.
  **Follow-up harvest (same conversation, 2026-07-25):** stage A — the
  exemplar's **full cycle set decomposes**, 411/411 across every
  length, zero failures (determined-partner algorithm, independent of
  `E021`'s pairwise) — **T5 survived the sharpest available kill
  test**; stage C — the order-19 unsplit count = 74,589 **exactly**
  (the partition follow-up is closed); stage B — **order 20 spent**:
  class 2,569,481, profile **7** (all \(C_{16}\)-blocked, none
  power-free; 0-/1-buckets empty), so **every \(\mathcal G\)-member
  has order \(\ge21\) and every tight 1-atom \(\ge22\)** (`L041`
  cases (4)/(5) propagate `L047` and the \(\mathcal G\) floor; direct
  generation certifies \(\ge21\)); the three on-disk order-20 profile
  members were fully verified and T5-tested by the orchestrator —
  **all survive** (1,890/1,890 cycles; 254 \(C_{16}\) verdicts
  re-verified pairwise), and all three repeat the \(S\ni6,14\) double
  blocking. SAVE_LIMIT caveat recorded: order-20 class files are
  per-part 200k samples (18/19 were complete). **Second harvest
  (both residual legs landed):** the part-14 recollection recovered
  the four remaining order-20 profile members (stream total 439,745
  reproduced exactly; identities in `profile_n20_part14.g6`; all
  vertex-taut, 2-connected, 65–80 \(C_{16}\)s, \(S\ni6,14\)) and
  **T5 survives on all four** (2,360/2,360) — so **all eight profile
  objects in existence survive T5** (`C042`(e), 4,661/4,661 cycles),
  every one carrying the same double blocking; and stage D
  (`followup_s022b.py`) came back **empty at order 21** — `C040`
  runs 14–21 and **`L047` lifts to 22** (window \([22,24]\), three
  orders wide; atom floors unchanged at 22/21, case (5) still
  binding).
- **New (S023): `L049`/`L050`/`C044` — T5 is a theorem; the
  interference program's gate is passed.** The two remaining
  pre-registered kill rungs ran first and survived (`C044`:
  `smallworld 13` exhaustive in-class, class 10,966 = `A021`'s count,
  all 10,853 taut members pass on 1,614,300 cycles and **all 113
  non-taut members fail** — the biconditional exact at 13; order
  \(\le8\) **exhaustive** over every graph, every vertex-taut pair,
  every cycle — 36.8M cycles at order 8 alone; cyclomatic-bounded
  slices at 9–11 clean). Then the proof (`A024`, promoted `L049`):
  **every vertex-taut pair is interference-complete** — for every
  cycle \(C\) and every prescribed edge of \(C\) there are two
  distinct through-paths in **trunk-identical arc form** with
  symmetric difference exactly \(C\) — by the **trimming
  construction**: tautness forces the block chain (block–cut tree a
  path, terminals non-cut in the end blocks); Menger's fan corollary
  plus subdivision put a through-path through any prescribed cycle
  edge (**Lemma A**: cycle-edge essentiality in taut pairs, proved);
  trimming that path at its first/last \(V(C)\)-contacts and
  completing through **both** arcs yields the pair. The recorded
  weaving obstruction never arises — the woven middle is discarded,
  not controlled. Audited `R002` (delegated fresh context): **PASS at
  lemma level**, 0 critical / 0 major, 2 minor + 6 notes, all
  repaired in place; the reviewer re-ran every `E023` command
  independently and re-verified the claim set with its own
  implementation (all labelled graphs \(\le6\); the ten named
  objects). Mechanically verified per instance (`E023
  constructive`): every step asserted on 17.4M (cycle, edge)
  instances including **all eight profile objects** (the recorded
  4,661 cycles reproduced object by object). Consequences: `L050` —
  on connected \(\delta\ge2\) graphs, interference-complete ⟺
  vertex-taut (the `C042` law is a theorem; the pinched census and
  `C041`'s 553/553 are instances); `L048`(iii) **unconditional** for
  the case-(5b) residual object (vertex-taut by `L042`):
  \(\mathrm{Spec}(H)=T_1(H,a,b)\),
  \(\mathrm{Spec}(B)=T_1(H,a,b)\cup(S+2)\) — its entire
  power-freeness is through-path arithmetic, every spectrum element
  realized by a trunk-split pair. **(F) ⟺ case (5b) empty below 36**;
  (F) is now the whole proof side there. Imports: Menger
  \(k=2\)/Whitney and block facts B1–B3, precise statements in
  `references/textbook-classics-2026-07-25.md`.
- **New (S024): `L051`/`C045` — the (F) opening probe spent, branch
  (b) taken, (F) re-aimed.** The complete trunk-split power-collision
  realization tables of the ten named objects (`E025`, anchors 45+14
  both interpreters, every recorded reference field re-verified, the
  weave control separating trunk-split from weaving pairs): none of
  the nine pre-registered membership patterns is universal; **30
  cycles across six profile objects are membership-blind outright**
  (trunk-split sets \(\{(5,13,1)\}\), \(\{(9,11,2),(10,10,2)\}\), or
  \(\{(5,11,0)\}\)); the calibration pair's 100% `has_PP` structure
  (every calibration \(C_8\) realized by two power-length paths)
  collapses to 1–8/37–112 at the frontier. **The membership-collision
  form of (F) is dead** — the empirical third leg beside `C037`
  (congruence caps at parity) and `L045` (memberships cannot exclude
  the chain case). Proved en route: **`L051`, the trunk bound** —
  every trunk-split realization has \(s=t_a+t_b\le n-L\), hence
  \(x+y\le2n-L\) (trunks live on off-cycle vertices; one paragraph
  from `L049`'s arc form) — **tight on all ten objects** (max \(s\) =
  \(n-L\) exactly: 2/6/3/4 at orders 10/14/19/20); with `L048`(iii)
  the residual object's entire collision system is order-confined
  (\(C_{32}\) at order \(\le33\): \(s\le1\)). Frontier saturation
  recorded (`A025` T3): spectra exactly \([3,n]\setminus\{4,8\}\) and
  \(S\supseteq[6,n-1]\) with \(6,14\in S\) on **all eight** profile
  objects (the double blocking, now seen as saturation); the only
  known \(\mathbb P-2\) dodges (\(S\cap\{6,14\}=\emptyset\)) are the
  calibration pair at orders 10 and 14, both gapping \(S\) exactly at
  6. **(F) = (F-S) ∨ (F-T)** (`A025` T4, both order-windowed, both
  failing off-window on the calibration pair as the discipline
  requires): (F-S) — vertex-taut (5b)-profile pairs with
  \(4,8\notin\mathrm{Spec}\) in the window force
  \(S\cap\{6,14\}\ne\emptyset\) (closure blocked via
  \(\mathrm{Spec}(B)\supseteq S+2\)); (F-T) — they force
  \(16\in\mathrm{Spec}\). Either, proved on \([18,35]\), closes case
  (5b) there (`L046` covers the chain side). Candidate mechanism:
  **saturation/interpolation** — a lower-bound theory for through-path
  length sets of taut windowed pairs (missing tool, named; `L049`'s
  block chain + `L051` are the raw material). First falsifiable move:
  the **S-gap census at the window bottom** (`A025` T5) — the
  \(\{C_4,C_8\}\)-free two-degree-2 classes are on disk at 18–20
  (`E022/data`, order 20 SAVE_LIMIT-sampled) with 21 generating
  (`E024`): per member, the \(S\)-gap structure at \(\{2,6,14\}\) and
  tautness; no taut gapped member ⟹ (F-S) survives where the residual
  object lives; a taut gapped member kills (F-S) as stated and is
  calibration object #3; the gap-vs-order curve against 10–16
  measures the mechanism either way.
- **New (S025): `C046` — the S-gap census spent; (F-S) survives; the
  saturation mechanism is profile-bound.** Over every unordered
  degree-2 pair of every on-disk class member (orders 10–19 complete;
  order 20 the per-part-complete 11/16 sample, **572,519** graphs —
  the S022 "572,530" figure counted the 11 file headers, corrected
  against the scan tallies — plus the four part-14 profile members):
  18,754,354 pairs, 767,004 members, anchors 45+57 under both
  interpreters (the calibration pair must be *found* gapped+taut, and
  is; the eight profile objects matched field-for-field). **(a)**
  Zero exactly-two members are gapped — (F-S)'s hypothesis class has
  exactly eight known realizations, all with \(6,14\in S\); outcome
  (i) of the pre-registration. **(b)** The wider class realizes the
  dodge freely: 9,061 vertex-taut gapped pairs (8/8/371/24 at
  12/14/16/17; 2,727/167/5,756 at 18/19/20 — no decay), 6,934 full
  \(\mathbb P{-}2\) dodges (\(2,6,14\notin S\)), on members with
  4–11 degree-2 vertices (min 5/6/4 at 18/19/20, never \(\le3\);
  thin-strata caveat). **(c)** 5,419 taut gapped rows sit on
  **power-free** members, most 2-connected: at window orders, every
  residual-object hypothesis *except the exactly-two profile* is
  realized simultaneously with the full dodge — the (F-T) double
  blocking is likewise profile-specific. Consequence for the missing
  tool: the interpolation lemma must consume min degree \(\ge3\) off
  the terminals; nothing weaker is true. Verification: every gapped
  pair recomputed by the independent full enumerator (540,135
  agreements per run) + stride sample; per-line integrity on all
  members; two production runs, identical tallies; zero bipartite
  members in the classes.
- **New (S026): `C047` — the near-miss dissection; the dodge taxonomy,
  the subdivision frame, and the chord-exchange validation.** Against
  the eight profile objects and a stride control: **(a)** every corpus
  dodge is shape A (short + 6-hole; minimal full dodges have
  \(\max S=13\) *exactly* at orders 16–20), A′ (\(\min S=7\) exactly),
  or B (long-range; holes exactly \(\{6,10,14\}\); even part
  \(\subseteq4\mathbb Z\) — the `L034` channel-(iii) pattern in-window
  on non-bipartite members; needs \(\ge7\) degree-2 vertices);
  **(b)** the dodge is pair-local — the order-20 frontier members
  (ndeg2 4; one adjacent-terminals full dodge \(S=\{1\}\cup[8,13]\))
  carry five fully saturated sibling pairs, so no member-level
  hypothesis works, and the profile hypothesis is load-bearing by
  exactly two subdivision vertices; **(c)** corridors are short
  (weights 2–3) and 99.1% of dodge rows reduce (suppressing
  non-terminal degree-2 vertices) to graphs carrying a \(C_4\)/
  \(C_8\) — subdivision is the escape from the class constraint;
  **(d)** killed: member-level lemmas, odd-cycle-supply
  discrimination (100% of dodge members have triangles); **(e)**
  control base rates: ordinary taut pairs break the upper-interval
  property at 12–17% (holes at 7–9, nearly gone by 13), Hamiltonian
  pairs 22–29% — the profile-8's joint saturation is far outside
  both; **(f)** the **span law** (proved, `A026` T5: no span-3/7
  chords) plus the first-order disjoint-chord calculus reproduce the
  profile saturation from 10 up (14 on all eight; misses confined to
  \([4,9]\)) and exactly explain the dodgers' holes (two span-2
  chords + spans \(\equiv1,2\bmod4\) ⟹ savings never \(\equiv3\bmod
  4\)). Consequence (`A026` T7): **(F-S) ⟸ (L-A) ∧ (L-B)** — (L-A)
  short-range exclusion (\(\max S\ge14\) in-window on the profile, or
  \(6\in S\) when short); (L-B) long-range poison forcing
  (\(\max S\ge14\Rightarrow14\in S\) or \(6\in S\)) — with the
  chord-savings combinatorics as (L-B)'s engine and ear-overload as
  (L-A)'s candidate.
- **New (S027): `L052`/`C048` — (F) becomes a decision procedure, and it
  is empty on the Hamiltonian stratum.** `L052` (proved, `A027`): for a
  pair \((H,a,b)\) with \(d(a)=d(b)=2\), all other degrees \(\ge3\), and a
  **Hamiltonian \(a\)–\(b\) path** \(P=v_0\cdots v_M\): (i) the chords
  cover \(\{0,\dots,M\}\), with 0 and \(M\) covered exactly once; (ii) every
  inclusion-minimal subcover \(\mathcal C'\) gives \(H'=P+\mathcal C'\) with
  the same degree profile, the same Hamiltonian path,
  \(\mathrm{Spec}(H')\subseteq\mathrm{Spec}(H)\) and
  \(S(H')\subseteq S(H)\), every chord having an endpoint of chord-degree
  1 — so a search for a pair avoiding prescribed cycle lengths *and*
  prescribed through-lengths may be restricted to **chord-minimal** systems;
  (iii) interval-disjoint chord families give genuine \(a\)–\(b\) paths of
  length \(M-\sum(\sigma_k-1)\), with the savings set a left-to-right DP
  whose prefixes already certify membership; (iv) the corrected chord-pair
  geometry (interior-disjoint chords close **no** extra cycle — a
  hand-table entry that was wrong, caught by the instrument's anchors).
  Consequence (`E028`/`C048`): at each order, enumerate every chord-minimal
  cover whose graph is \(\{C_4,C_8,C_{16}\}\)-free and whose savings set
  misses \(\{M-2,M-6,M-14,M-30\}\); by (ii)/(iii) every counterexample
  yields one, so **emptiness proves (F) at that order**. Verdict: **empty at
  every order 16–30**, the last completed rung (node growth
  \(\approx\times1.9\) per order — the \(C_{16}\) hypothesis, free because
  it is half of (F)'s negation, cut it from \(\approx\times3.5\) and carried
  the ladder eight orders past the recorded frontier in under an hour;
  wall-clock growth is 1.8–2.4 per rung, so orders 31–35 are days of
  single-core computation and **nothing is claimed above the last completed
  rung** — `R003` F3). **Above order 26 the poison prune stops firing**
  (branch kills 61, 33, 45, 17, 2, 1, 0, 0, 0 at \(M=20\ldots28\)), so
  orders 27–29 prove the *stronger*, poison-free statement that the
  \(\{C_4,C_8,C_{16}\}\)-free chord-minimal Hamiltonian exactly-two stratum
  is empty — implying (F) a fortiori but exercising none of its mechanism
  (`R003` F4). Run A
  (\(\{C_4,C_8\}\) only) exhibited the **first \(\mathcal G\)-profile
  objects at orders 21 and 22** (10 and 43 chord-minimal ones, 3 and 16
  isomorphism classes, all 2-connected, girth 3, 91–186 \(C_{16}\)s), every
  one killed twice (\(14\in S\) on all 53, \(6\in S\) on 40, \(C_{16}\) on
  all 53); 13 of the order-22 objects have \(S\) **not** a full interval
  (holes at \(\{6\}\) or \(\{2,3,4,6,7\}\)) — the first in-window
  exactly-two objects breaking the `A025` T3 saturation pattern while
  keeping the double blocking. Independent cross-check of the recorded
  ladder from a different generation principle: with the poison prune off,
  chord-minimal cover counts are 0 at orders 12–18 and 6, 65 at 19, 20, all
  signatures already recorded. Not covered: pairs whose longest \(a\)–\(b\)
  path is not Hamiltonian (`A027` T5 — the named residue, with a first
  purchase: a zero-savings two-attachment off-path component forces an
  all-equal-length, hence bipartite, interior-degree-\(\ge3\) gadget, the
  class `L035`/`C034` has been emptying).
- **New (S030): `L053`/`L054`/`L055`, `C050` — the non-Hamiltonian stratum
  gets an engine, and the programme's ceiling is named.** `L053`: for every
  \(N\) there is a 2-connected exactly-two-profile pair of order \(\ge N\) with
  girth \(\ge17\) (hence no \(C_4\), \(C_8\), \(C_{16}\)) and **no Hamiltonian
  through-path** — a cubic non-Hamiltonian graph of large girth minus an edge
  (`X002` Haythorpe; independently `X003` Kochol's snarks plus the three-line
  proof that a Hamiltonian cubic graph is 3-edge-colourable). So the class-level
  hypotheses do **not** force Hamiltonicity: `C049`'s 27/27 is a small-order
  pattern, not a lemma, and any surviving form of that route must consume
  power-freeness, the poison condition, minimality, or an order bound
  (**calibration object #3**). The same object shows the ladder's
  class-emptiness verdict above order 26 must fail at some order. `L054`: the
  **bipartite exclusion dichotomy** — a connected bipartite subgraph with
  \(\le2\) sub-cubic vertices inside a power-free graph disproves 0.1 by
  `L035` T3; in range \(\le24\) it is an outright exclusion via `C034`, and
  inside `G015` the dichotomy form alone is *not* a contradiction. `L055`: the
  **positive-savings theorem** — for a power-free 2-connected profile pair and
  a longest \(a\)–\(b\) path, every component of \(H-V(P)\) admits a bridge of
  savings \(\ge1\) (\(\ge2\) with \(\ge3\) attachments, by the Y-identity, which
  uses maximality alone; exactly two attachments by parity via `L035` T2 and
  `L054`), plus the bridge span law and the transported coverage step. `A027`
  T5's zero-savings obstruction is removed; the stratum is nonetheless cleared
  at **no** order (`A028` T8). `C050` (`E029`, no generation): (INT) —
  \(S\supseteq[8,\max S]\) — holds on all 24 recorded profile objects with \(S\)
  recomputed from graph6, every hole in \(\{4,5,6\}\); over the 9,061-row corpus
  the minimum degree-2 count admitting a hole is 4 for every value \(\le7\) and
  **5** at 8 (so the constant is pinned), and a hole at **14** needs \(\ge7\)
  degree-2 vertices — five above the profile.
- **New (S031): `L056`–`L058` — the interpolation genre is empty, and the
  window is wider at the top and higher at the bottom.** `L056` (`A029` T1, audited
  `R004`, which **strengthened** it): **(INT) and (INT-14) are false, with
  explicit in-window witnesses.** Truncated Petersen minus a link edge is a
  2-connected vertex-taut \(\{C_4,C_8\}\)-free exactly-two-profile pair of
  order **30** with \(S=[9,26]\), so \(8\notin S\); chaining two copies at a
  cut vertex gives order **59** with \(S=[18,52]\), so \(14\notin S\).
  Neither imports anything (verified, `E030/truncation.py`). Asymptotically the
  same follows from `L053` (\(\min S\ge16\) for \(F-ab\) at girth
  \(\ge17\)). `L057` (`A029` T2, modulo `X004`; **audit FAIL
  twice, one major finding still open — NOT ESTABLISHED, do not cite**): the triangle
  expansion at one vertex of a bipartite cubic 3-connected graph of even girth
  \(g\ge10\) with \(\mathrm{diam}\ge g/2+1\), minus an edge on a shortest
  cycle at distance \(\rho\ge g/2\) from the triangle, is a
  **non-bipartite** class member with \(\min S=g-1\) odd and every even
  through-length \(\ge2\rho+2\) — a hole at \(\min S+1\ge10\)
  containing \(\rho+1-g/2\) even values, so
  \(S\supseteq[\min S+c,\max S]\) fails for every \(c\) and the recorded
  pivot trigger fires. **Diagnosis (`A029` T3(a)), the reusable part:** three
  genres are now proved unable to exclude case (5b) from class-level
  hypotheses — congruence (`C037`), membership (`L045`/`C045`), interpolation
  (`L056`/`L057`) — and all three fail because every class-level hypothesis
  (degree profile, forbidden short cycles, tautness, 2-connectivity) is
  **local and hereditary**, hence satisfied by \(F-ab\) for large-girth cubic
  \(F\). Power-freeness at powers **above the girth** and minimum-order
  minimality have never been consumed. Conditional residue (`A029` T3(b),
  **not** progress): an interpolation lemma plus `L042`'s forced
  power/Mersenne memberships plus the poison condition would give
  \(2^j-2-c<\min S\le2^j\le\max S\le2^{j+1}-3\), hence
  \(\max S<2\min S+O(1)\) — exactly `L031`/`L032`'s block-question
  constraint. `L058` (`A029` T5): `A022` W1-T8 with its block-order input
  raised from 16 to **21** (`C039` \(\le17\); `C043`/S022 at 18–20; at 21
  `C040` for the 0-bucket and `C049` for the 2-bucket) gives **either \(H\)
  is 2-connected or \(n_0\ge42\)**; with `C049`'s tight-1-atom floor the
  case-(5b) window is \(n_0\in[23,41]\), i.e. \(H\)-orders \([22,40]\), so
  the `E028` ladder stopped at 30 is **ten** rungs short, not four.
- **New (S019): `L037`–`L042`, both `G015` routes advanced in one
  orchestrated parallel run.** R2 side (`L037`/`L038`): the
  **subdivision descent** — the link graph on the degree-\(\ge4\) set of
  a minimal counterexample is power-free (cycles lift doubled) and, by
  order-minimality, 2-degenerate — gives \(3|V_3|\ge2n+3\), strictly
  past Carr's \(4/7\); the 15-vertex certificate S15 (`E017`) shows
  \(2/3\) is the exact ceiling of the non-power hypotheses, so the
  constant route to `G015` is **closed**, with the descent as the
  reusable residue. R1 side (`L039`–`L042`): the closure calculus and
  the (3,3) **bijection** onto the congruence class \(\mathcal G\)
  (through-set avoids \(\{2,6,14,\dots\}\); no \(s_{\max}\) window);
  the **engine + peel** (any counterexample below the minimum atom
  order \(n_0\) yields a *cubic* counterexample — the repair of the
  withdrawn T4.1); the five-case analysis at the defect vertex:
  **the conditional cubic reduction holds modulo excluding case (5b)**
  (defect non-cut, both neighbours cubic, residue vertex-taut), every
  tight 1-atom has order \(\ge17\), and the case-(5b) residual object
  is 2-connected, degree-\(\ge4\)-independent, **non-bipartite** (hand
  proof at every order), with forced power/Mersenne memberships and
  chain cancellation. `C004`–`C006` are upgraded to **verified**
  (line-by-line audit of arXiv:2605.22844v1). The two routes meet: a
  one-defect subgraph of the link graph is exactly a tight 1-atom.

## Imported frontier

- `C004`–`C006` now carried at **verified** strength (S019 line-by-line
  audit and internal reconstruction,
  `references/carr-2026-verification-2026-07-24.md`); `C006` superseded
  internally by `L038`. `C007`–`C009`, `C012`–`C014`, `C017`,
  `C024`–`C026` unchanged; the min-degree-3 literature frontier remains
  Bondy–Vince strength.

## Program status

`G013` has three live objects.

(a) The **tight 1-atom question** — does a power-free graph exist whose
unique sub-cubic vertex has degree exactly 2? Rewritten in S018 (the
unrestricted version is conjecture-complete, `L036`) and **structured in
S019**: every tight 1-atom has order \(\ge17\) (`L041`); a minimum-order
one with both defect-neighbours cubic corresponds bijectively to the
congruence class \(\mathcal G\) (`L039`), and under (R) the *only*
surviving configuration is case (5b) — that closure with a vertex-taut
residue, now heavily constrained (`L042`: 2-connected, non-bipartite,
degree-\(\ge4\)-independent, forced through-set arithmetic, chain
cancellation, band-4 pencil). For `G015` the conditional form suffices
and only case (5b) remains. Empty through order 15 stream-level
(`C027`) **and through order 16 for the exact \(\mathcal G\) profile
(`C036`, S020), through order 17 for `C027`'s **entire class** by
the dedicated generator (`C039`, S021), and through order 19 for the
profile ladder (`C043`, S022 — order 18 empty; order 19's unique and
first-ever profile member is vertex-taut but \(C_{16}\)-blocked and
\(S\)-violating, doubly excluded)** — **every tight 1-atom has order
\(\ge22\), every \(\mathcal G\)-member \(\ge21\)** (S022 harvest:
order 20 also spent — profile 7, all \(C_{16}\)-blocked, none
power-free; the 1-bucket is empty at 18–20, so \(\ge21\) holds
directly by generation, and `L041`'s cases (4)/(5) with `L047` give
\(\ge22\)); no bipartite tight 1-atom through order 24 (`C034`, S021
harvest). The congruence-obstruction leg
is retired (`C037`/`A021`) and the chain-cancellation leg is **spent
as a theorem** (S021, `L043`–`L046`): the tension cannot exclude the
chain case by arithmetic alone (`L045`), but per-block order bounds
confine that case to \(n_0\ge36\) (`L046`) — so the case-(5b) frontier
below 36 is exactly the **2-connected** residual object. Its proof
side now runs through the **interference program**, whose gate is
passed (S023): interference-completeness holds for **every**
vertex-taut pair (`L049`, theorem, audited `R002`), so the object's
power-freeness **is** through-path arithmetic unconditionally
(`L048`(iii): \(\mathrm{Spec}(B)=T_1\cup(S+2)\), every element a
trunk-split pair value) — and the forcing target **(F)** is now the
entire proof side below 36: (F) says the forced \(S\)-arithmetic
makes a power-length trunk-split collision unavoidable in the window
\([18,35]\), which is *equivalent* to case (5b)'s emptiness there.
**S024 spent (F)'s opening move**: the realization tables came back
with no membership pattern (branch (b), `C045`), so (F) is re-aimed
as **(F-S) ∨ (F-T)** — the window forces \(S\cap\{6,14\}\ne\emptyset\)
or \(16\in\mathrm{Spec}\) — with the trunk bound `L051` proved and
the S-gap census as the next move. **S025 spent the census**
(`E026`/`C046`): (F-S) survives its first kill test (zero gapped
exactly-two members on all of 10–20's disk classes), and the
mechanism is recalibrated — 9,061 vertex-taut gapped pairs off the
profile prove that tautness + class + order force nothing; the
interpolation lemma must consume the exactly-two profile itself.
**S026 spent the dissection** (`E027`/`C047`, attempt `A026`): the
dodge taxonomy is rigid (shapes A/A′/B), the dodge is pair-local
with the frontier two subdivisions from the profile, near-misses are
subdivisions of class-violating graphs, and the interpolation target
splits into **(L-A) ∧ (L-B) ⟹ (F-S)** with the span law proved and
the chord-exchange calculus validated as (L-B)'s engine (top-of-S
saturation from 10 up reproduced on all eight profile objects).
**S027 changed the shape of the target**: instead of proving a
savings-reachability lemma, `A027` proved two reductions (`L052`) that
make (F) a **finite decision problem per order**, sharpened the aim to
the disjunction (F) (which supplies \(C_{16}\)-freeness free) and to the
full poison set \(\{2,6,14,30\}\), and decided it — **empty at every
order 16–30** (`E028`/`C048`), i.e. case (5b) is closed there for every
residual object with a Hamiltonian through-path.
**S030 changed what the (F) program is for.** Three things, in order.
(1) `L053`: the class-level hypotheses do **not** force a Hamiltonian
through-path, so `C049`'s 27/27 is a pattern and not a lemma, the
non-Hamiltonian stratum must be handled on its own, and the ladder's
class-emptiness verdict above order 26 must fail at some order.
(2) `L055`: that stratum now has an engine — every off-path component
of a longest through-path pays savings \(\ge1\), so `A027` T5's
zero-savings obstruction is gone and the reroute machinery transports
from chords to bridges; two gaps remain before it is a decision
procedure (`A028` T8), and no order is cleared.
(3) The ceiling: `L046` supplies 2-connectivity only below 36, so the
(F) program — complete on **both** strata — would close case (5b) for
\(n_0\le35\) and leave \(n_0\ge36\) untouched. **It cannot prove
`G015`.** The recorded successor is order-unbounded: **(INT) ∧ (L-A)**
(`A028` T9), where (INT) — \(S\supseteq[8,\max S]\) for a vertex-taut
\(\{C_4,C_8\}\)-free exactly-two-profile pair — plus \(\max S\ge14\)
gives \(14\in S\), poison, hence (F-S) at every order.
**S031 refuted that successor before a session was spent on it.** `L056`:
`L053`'s own object satisfies every hypothesis of (INT) and has
\(\min S\ge16\), so **(INT) and (INT-14) are false**; `C050` could not have
caught it, since no on-disk object has \(\min S>8\) and none can exist
below order 70. `L057`: the relativized repair fails too, on a
*non-bipartite* object, so the recorded pivot trigger fires. **The
interpolation genre is empty** — the third after congruence and membership,
all three failing for one reason (`A029` T3(a)): class-level hypotheses are
local and hereditary, so \(F-ab\) for large-girth cubic \(F\) satisfies
every one of them. `L058` then re-derives the order dichotomy from the
current floors — 2-connected or \(n_0\ge42\) — putting the window at
\(n_0\in[23,41]\) and leaving the stopped ladder **ten** rungs short of it.
Tier 1's primary work is therefore the **non-Hamiltonian stratum** (`A028`
T8's two gaps), and the only shape of statement that can be order-unbounded
is one consuming power-freeness **above the girth** or minimum-order
minimality — no proof step exists for either.

(b′) The **block question** (pinched channel); after `L033` its band-4
case is exactly the **pencil endgame** — prove no vertex-taut
2-connected \(C_4\)-free core with \(d(x,y)=4\), \(s_{\max}\le8\) has a
pencilled 4-path system. Catalogue now through order **16**
(`C030`–`C032`, `C035`/S017): **eight equality blocks** — P10 =
Petersen\(-e\) (band 4), A11/B11/C12 (band 5), D14 (band 6), and from
the order-16 harvest F16 (band 4, terminal degrees (3,3), on a graph
with no sub-cubic vertex), G16 (band 4, (2,4)), H16 (band 6, (2,2),
first block with \(C_{16}\) in spectrum) — every one at exact equality
\(s_{\max}=2\,s_{\min}\); **no strict taut pinched pair exists at
order 16 at all** (strict catalogue complete at seven witnesses
through 16), no power-free closed taut pair at 16, and all three
band-4 core gadgets are disjoint-type, so the pencil endgame's
exhaustive empty base and the 100% two-through-path interference
census both extend through order 16. Hypothesis necessity (`C033`):
\(C_4\)-freeness is essential to both band-4 rungs. Three hand
constructions died to the cascade obstruction (`A015`).

(c) The **congruence channels**, now **split by `L035`**. Channels (i)
(all-odd \(S\)) and (iii) (\(S\subseteq2+4\mathbb Z\)) *are* the
bipartite class, and `E015`/`C034` searched it exhaustively: **no
power-free member at any order \(\le24\)** (\(\le25\) with a pendant),
with every member of the class carrying a \(C_8\) and the minimum
\(C_8\) count never dropping below 13 — so the \(C_{16}\) test is never
even decisive, and this channel is *further* from a witness than the
pinched one (whose equality blocks are blocked by 3–7 \(C_8\)s). What
survives in (c): channel (ii), the odd-prime-gcd channel — not
bipartite-forced, no structure theorem, no reduction, no dedicated
search — plus the missing parity analogue of `L032`'s 2-connected block
extraction. Two by-products of the same run: no bipartite counterexample
and no bipartite **tight** 1-atom at orders \(\le23\), verified
internally.

## Open obligations

- `G015` (**the proof-side deliverable; reduced in S019 to one
  configuration**): exclude case (5b) — no minimum-order tight 1-atom
  is the 2-path closure of a vertex-taut \(\mathcal G\)-member — and
  the cubic reduction follows (`L040`/`L041` supply every other case).
  The constant-density route is closed (`L038` delimitation); the
  order-16 scan is done and empty (`C036`) and the congruence hunt is
  dead (`C037`/`A021`). Live moves: the chain-cancellation tension
  (`L042` W1-T14), the disjoint long-link descent (`A020` W2-T8(c)),
  and the order-17 search rung via the `G014` item-6 generator.
- `G013` (core): tight 1-atoms; the block question (band 4 = pencil
  endgame, bands \(\ge5\) open); the odd-prime-gcd channel and the
  missing parity block-extraction.
- `G014`: source-audit the external memo's literature and census leads.
  Item (2) (bipartite \(\ge32\)) is **de-gated** — `L035` T3 removes the
  need for the Mersenne-window logic and `C034` verifies the range
  internally; items (1), (3)–(6) still gate their threads.
- `G002`, `G003`, `G007`: the global mechanism; `G007` routes through
  `G013`'s conditional transfer.
- `G004`: only the original 1997 Erdős article body remains uninspected.

## Roadmap (S018)

Standing instruction (user, S015): **all threads stay documented and
live**; sessions select by strategy audit, retire only on evidence. S018
adds a second instruction (user): weigh routes by what they would
*deliver* — the full conjecture first, a significant delimited result
second — and keep cheap legs running alongside rather than instead.

The tiers below replace the flat thread list. Threads A–F are all still
here; what changed is that each now says which tier it serves, and no
thread may be selected as a session's primary work on cheapness alone.

**Why the restructure.** Sessions 11–16 all worked inside the assembly
interface, whose proof-side best case is the *cubic reduction*, not 0.1
(`A016` M6). S018 then found that one of that interface's two halves —
the 1-atom question — is conjecture-complete (`L036`), so the recorded
"ceiling" was in fact circular. The dossier's real proof-side
deliverable is `G015`, and it had never been named as a target.

### Tier 0 — settle statement 0.1 (the mission)

No cheap move exists here, and none should be pretended. Two sub-cases:

- **A forcing mechanism at \(\delta\ge3\)** (`G003`, `G007`). The
  literature frontier is Bondy–Vince strength (two cycles differing by 1
  or 2); nothing forces a *specific* length. Every internal theorem so
  far (`L030`, `L033`, `L035`) has run on \(C_4\)-freeness or parity, and
  the power spectrum has never once had to fight — that is the diagnostic
  to keep watching.
- **A counterexample.** Best ticket: cubic, order \(\ge30\) (Thread C),
  because `C013` stops at 28 and `L029` concentrates the risk there.

### Tier 1 — the named deliverable: the cubic reduction (`G015`)

"0.1 holds iff it holds for cubic graphs." **S019 ran both routes in
parallel (audited worker subagents) and the target is now a single
configuration:**

- **R1, reframed to the conditional form** — "a tight 1-atom yields a
  cubic counterexample", which is all the reduction needs (`L040`); the
  unconditional "no tight 1-atom exists" is retired as an R1 target
  (unreachable by minimality: its reducts are counterexamples, not
  atoms). By `L041` the conditional form is proved **except in case
  (5b)**; excluding that case closes `G015`. S020 spent the first two
  recorded moves: the order-16 scan is **empty** (atom bound now
  \(\ge18\), `C036`) and the congruence obstruction is **dead at every
  modulus** (`C037`/`A021` — the forced hypotheses are realized from
  order 10, so they admit no refutation; parity is the ceiling of
  chain-calculus congruence information). **S021 spent the next two moves in one
  orchestrated run:** the chain-cancellation tension is now the theorem
  package `L043`–`L046` — quantified (`L045`: three exponent-
  disjointness conditions per cut are the whole forced content, so
  membership arithmetic alone can never exclude the chain case), with
  every prefix/suffix forced non-bipartite (`L043`) and the order
  dichotomy `L046` confining the chain case to \(n_0\ge36\) — **only
  the 2-connected configuration remains below 36**; and the order-17
  rung is **spent empty** by the new generator (`C039`: tight 1-atoms
  \(\ge19\); the chain-case kill test refuted through the order-14
  block catalogue, `C038`, named 15/16 rung open). **S022 ran moves (i) and (ii) to
  verdicts** (orchestrated: W1 `fable` on the dissection, W2 `opus` on
  the ladder, both audited with independent re-derivations): the
  dissection landed the **interference outcome** — no
  non-interference blocker exists at the frontier (`C041`, 553/553),
  the property is exactly tautness-shaped (`C042`), the calculus is
  proved (`L048`), and the ladder moved the floors to 20 with the
  **first-ever profile member** at order 19, doubly blocked
  (`C043`). **S023 closed the T5 program**: the remaining kill
  rungs ran first and survived (`C044`), then **T5 was proved
  outright** (`L049`, the trimming construction — no exchange
  argument exists in the final proof; audited `R002` PASS) with the
  spectrum identity unconditional (`L048`(iii) upgrade) and the
  biconditional a theorem on \(\delta\ge2\) (`L050`). Live moves
  against case (5b), in order — **S024 spent move (i)'s opening probe
  (branch (b)) and re-aimed the program**: (i) **the (F) program,
  now (F-S) ∨ (F-T)** (`A025` T4): the membership-collision form is
  dead (`C045` — no pattern survives the ten objects; 30
  membership-blind cycles), and (F) splits into (F-S) — in the window
  \([18,35]\), vertex-taut (5b)-profile pairs with
  \(4,8\notin\mathrm{Spec}\) force \(S\cap\{6,14\}\ne\emptyset\)
  (closure blocked) — and (F-T) — they force \(16\in\mathrm{Spec}\)
  (\(H\) blocked); either closes case (5b) below 36. Supporting
  structure proved: the trunk bound `L051` (\(s\le n-L\), tight on
  all ten objects — the collision system is order-confined).
  Candidate mechanism: **saturation/interpolation** (all eight
  profile objects have \(S\supseteq[6,n-1]\) and spectrum
  \([3,n]\setminus\{4,8\}\); the missing tool is a lower-bound theory
  for through-path length sets). **S025 spent the census** (`E026`/
  `C046`, outcome (i)): **(F-S) survives** — zero gapped exactly-two
  members anywhere on disk at 10–20 — and the tool's spec is
  sharpened: 9,061 vertex-taut gapped pairs off the profile (down to
  4 degree-2 vertices at order 20, most on power-free 2-connected
  members) prove the lemma must consume the **exactly-two profile**,
  not just tautness. **S026 spent the dissection sub-move**
  (`E027`/`C047`, attempt `A026`): the taxonomy (A/A′/B), the
  pair-locality warning, the ndeg2-4 frontier, the subdivision frame
  (99.1% class-violating reductions), the span law (proved), and the
  chord-exchange validation — the target lemma is now the split
  **(L-A) ∧ (L-B)** with the chord-savings combinatorics as (L-B)'s
  engine. **S027 replaced the lemma hunt with a decision procedure**
  (`A027`/`L052`, `E028`/`C048`): the chord-minimal descent plus the
  monotone-reroute prune make (F) exhaustively decidable per order,
  the disjunction is decided directly (so \(C_{16}\)-freeness is a
  free hypothesis, and it is what makes the window reachable), and
  the verdict is **empty at every order 16–30** (last completed rung;
  audited `R003` PASS, all four major findings repaired) — case (5b)
  closed there on the Hamiltonian stratum, with the first order-21/22
  \(\mathcal G\)-profile objects exhibited and all doubly blocked.
  Next falsifiable moves, **re-ordered by the S027 post-close review**
  (see `DECISIONS.md`: the remaining risk is stratified by *shape*, not
  by size — the Hamiltonian stratum is clear at 16–30, the
  non-Hamiltonian one at no order at all, so extending the ladder
  completes nothing): **(1) `E024` IS HARVESTED (`S029`, `C049`) — the
  measurement came back UNANIMOUS.** The complete order-21 class
  (2,951,168 graphs) has 19 degree-profile members, all
  \(C_{16}\)-blocked, **zero** power-free survivors — \(\mathcal G\)
  is empty at 21, every \(\mathcal G\)-member \(\ge22\), every tight
  1-atom \(\ge23\) — and **\(\max S=n-1\) on all nineteen**, so the
  exactly-two profile carries a Hamiltonian through-path on **27 of 27**
  known in-window objects against a 22–29% control (`C047`(e)). The
  pre-registered pivot did **not** fire: `C048`'s ladder is *supported*,
  not proved, to address case (5b) whole rather than a slice. One member
  has \(6\notin S\), so saturation is not universal. **`O012` was
  EXECUTED (`S028`)**: the rung runs on Railway behind a passed
  linux/amd64 anchor re-gate, at modulus 144 on six services, and the
  laptop is freed. Two corrections came out of it — width is *not* free
  (`geng` duplicates the tree above split level \(n-4\) once per part,
  so total work is \(\text{mod}\times A+B\) and the wall clock has a
  floor), and `scan.py` writes a part's class file only under
  `SAVE_LIMIT`, so an oversized part silently discards the graph6
  strings of its profile members (this cost 8 of the 11 members the
  stopped laptop run had found; modulus 144 avoids it). Cheap proxy
  still available on data already on disk: sweep the orders 18–20
  classes by degree-2 count and see whether \(\max S=n-1\) becomes
  universal as that count falls toward two. **(2) the non-Hamiltonian
  stratum** (`A027` T5 — extend the descent to bridges, where a
  zero-savings two-attachment component forces an all-equal-length
  bipartite interior-degree-\(\ge3\) gadget, the class `L035`/`C034`
  empties): this is now the primary *proof* work.
  **S030 SPENT MOVES (1) AND (2), AND RE-AIMED THE TIER.** Move (1)'s
  deferred alternative — promote 27/27 to a lemma — is **dead at class
  strength** (`L053`; calibration object #3), so the cheap
  degree-2-count proxy is pointless and is retired. Move (2) delivered
  its engine (`L055`: every off-path component pays savings \(\ge1\);
  `L054`: the bipartite transfer with its hypothesis finally matched)
  but **clears no order** — `A028` T8 names the two remaining gaps
  (component-atomic minimality; savings per component rather than per
  position). Above both: `L046` gives 2-connectivity only below 36, so
  the whole (F) programme is a **finite-window instrument** and cannot
  prove `G015`. S030 recorded the tier's primary work as (INT) ∧ (L-A)
  (`A028` T9), order-unbounded and calibrated by `C050`.
  **S031 REFUTED IT** (`L056`/`L057`, audited `R004`) and closed the whole
  **interpolation genre**; `L058` re-derived the window as
  \(n_0\in[23,41]\) (\(H\)-orders \([22,40]\)), which leaves the stopped
  ladder ten rungs short rather than four. **The tier's primary work is
  therefore the non-Hamiltonian stratum** (`A028` T8's two gaps), with
  `L055` as its engine — the only route that makes the window's interior
  fully decided rather than half-decided — and behind it the first
  (F)-side lemma consuming power-freeness **above the girth** or
  minimum-order minimality, the one shape of statement the three dead
  genres leave open.
  **(3) the `E028`
  ladder is STOPPED** — order 30 ran, came back empty, and the process
  was halted there (`S028`) rather than rolled into 31. It *is*
  parallelisable (the DFS branches at position 0 over the single chord
  \((0,q)\), giving \(\approx M\) independent root subtrees), so this
  is a judgement about value, not a limit: above order 26 the rungs
  prove class-emptiness rather than poison forcing (`R003` F4), so they
  buy confirmation and no understanding; behind them min-degree-3 at 22
  (\(\approx\)38 h) and the `C038` **kill rung** at block orders
  15–16 + the disjoint long-link descent (unchanged).
- **R2, constant route closed** — `C004`–`C006` verified and the bound
  improved to \(3|V_3|\ge2n+3\) (`L037`/`L038`), but S15 certifies
  \(2/3\) as the exact ceiling of the non-power hypotheses and no
  constant \(<1\) delivers the reduction. Surviving extension: the
  internally-disjoint longer-link descent (`A020` W2-T8(c)). The
  descent itself is the reusable mechanism, and the routes meet on the
  link graph (a one-defect subgraph of it is a tight 1-atom).

This remains the highest-value *reachable* target in the dossier: a
theorem about the conjecture rather than about our own gadget
formalism, and it would make Thread C's searches decisive instead of
conditional.

### Tier 2 — restricted-class theorems worth having on their own

- **Bipartite EGC** (Thread E): every bipartite \(\delta\ge3\) graph has
  a power-of-two cycle. `L035` fixes the class (girth \(\ge6\)
  bipartite), `C034` gives an internally verified base through order 24,
  and the naive "\(C_8\) always" form is *false* at large order
  (bipartite double covers of `C009`'s large-girth cubic graphs), so any
  proof must be order-bounded or consume \(C_{16}/C_{32}\). Reported
  externally only as a computation to 31 — a proof would be new.
- **The path-spectrum spread theorem** (Thread B3): under (D), is
  \(\gcd(S)\) always a power of 2? New genre — the literature's mod-\(k\)
  results are about cycle spectra, not two-terminal path spectra. The
  3-connected *cycle* analogue is a four-line Menger argument (`A016`
  M10) and is the proved cousin to start from; \(\Theta(3,3,3)\) shows
  the degree condition, not parity, must do the work.

### Tier 3 — cheap legs: run them, never *select* them

Harvest-only. None of these may be a session's primary work.

- Bipartite hunt (`E015`/`E019`): clean through order 24 (25 with a
  pendant) — the order-24 leg landed empty in the S021 same-day
  harvest, the first order covered by generation rather than genbg.
  Next leg: order 26 on the `-b` instrument (even orders; the
  unfinished odd-order-23 probe remains the recorded warning against
  interpolating even-order growth).
- The gcd scan over the existing order-\(\le16\) stream (needs path
  enumeration; the bipartite shortcut does not apply).
- Order-17+ legs of the pinched catalogue (Thread A/F).
- Census mining (Thread D), gated by `G014`.
- The min-degree-3 ladder at order 22 (≈38 h on 8 workers at the
  measured ×7.2 growth — a deliberate decision, no longer a cheap
  leg): orders 20 and 21 landed empty in the S021/S022 harvests
  (`C040` runs 14–21, `L047` at 22); order 22 is the window's bottom,
  so the next empty rung meets Markström's order-24 ceiling two away.

### Tier 4 — infrastructure with cross-thread leverage

- ~~The dedicated \(\{C_4,C_8\}\)-free generator~~ **Built (S021,
  `E019`/`C039`; `G014` item 6 discharged).** What it unlocked on day
  one: the order-17 \(\mathcal G\) rung (40 s wall), `C027`'s class to
  17, the min-degree-3 sweep to 19 (`C040`/`L047`). What it prices in:
  \(\mathcal G\) orders 18/19/20 at ≈4 min/25 min/2.8 h; cubic orders
  26/28 at ≈15 min/3.5 h (reproducing the remaining `C013`/`C014`
  lines) and **cubic order 30 — Tier 0's best counterexample ticket —
  at ≈2.3 days on 8 workers**; bipartite 24–26 in minutes-to-hours.
  Remaining instrument work if order 24+ \(\mathcal G\)-rungs are ever
  needed: port the same 60-line prune into a cubic-specialized host
  (genreg/minibaum) — recorded in `E019`'s design analysis, not needed
  through order 21.
- `G014` source audits for the imports that gate Tiers 1–3 (census
  provenance for Thread D; items (1),(3)–(5); new item (7), the
  MO-512914 thread body).

### Demoted and retired

- **Retired as a target:** the unrestricted 1-atom question
  (conjecture-complete, `L036`). It stays in the record as a
  completeness fact, not as work.
- **Demoted to Tier 3:** the pinched-channel rung ladder, including the
  pencil endgame (Thread A). It is real mathematics and stays live, but
  its best case is one channel of a ceiling-limited interface, so it no
  longer merits primary selection over Tier 1.

### Pivot triggers

A hit in a \(\mathcal G\)-profile scan at order 21+ satisfying the
\(S\)-condition (**immediate disproof** — a tight 1-atom; 16–20 were
consumed in S020–S022, the eight profile members at 19–20 all
\(C_{16}\)-blocked);
a \(\{C_4,C_8\}\)-free min-degree-3 graph at order 22+ (first at 22
would refute nothing but ends `L047`'s climb at the window's bottom;
a *power-free* one is a **counterexample**; 14–21 are all empty); a pencil-type band-4 taut core at order 17+; a
strict block or \(C_8\)-free equality block (disproof protocol);
**any** power-free member of the `E015` class at order 25+ (immediate
disproof, `L035` T3; 24 landed empty in the S021 harvest); a `G014`
audit overturning an assumed bound; a realized
\(\{7,8,12,13,14\}\)-shaped block through-set at order 15–16 (kills
arithmetic-only chain exclusion; the chain-case Petersen\(-e\) then
exists at order ~29); a non-decomposable cycle in a vertex-taut
pair would now **contradict the reviewed theorem `L049`** (the S023
rungs gave it 12.7M further chances and it never happened) — any such
find is a soundness alarm on `A024`/`R002`/the census predicate, to be
treated as a critical audit event, not a route pivot;
~~a membership-patterned regularity in the (F) realization tables~~
(**spent, S024**: the tables came back with no pattern — branch (b)
taken, the membership-collision form of (F) is dead, `C045`/`A025`);
~~a vertex-taut member of the 18+ class with
\(S\cap\{6,14\}=\emptyset\) in the S-gap census~~ (**spent, S025**:
the census found none on any exactly-two member — (F-S) survives —
while the wider class realizes the dodge freely, so the trigger's
surviving form is a **gapped vertex-taut exactly-two member at order
21+**, checked when each new ladder rung is censused; a wider-class
dodge is no longer a trigger, it is the recorded norm);
a **profile-consuming interpolation lemma that also holds on the
census's near-miss corpus** (would be false — 9,061 counterexamples
on disk — so any draft proof matching the corpus is unsound: use it
as the standing sanity check beside the calibration pair; after
S026, the sharp instances are the **36 Hamiltonian dodgers** for
(L-B) — any savings-forcing draft must fail on their chord systems —
and the **ndeg2-4/5 frontier members** for (L-A)); a **short-range
or gapped exactly-two member at order 21+** (a \(\max S\le13\)
profile pair kills (L-A) as stated; a gapped one kills (F-S) —
check each new ladder rung; **S027 note:** 13 of the order-22 objects
already have \(S\) non-interval with a hole at 6, so the *saturation*
form of the trigger has fired and is retired — what has never been seen
is a hole at **14** on an exactly-two pair in the window, and that is the
live form); a **power-free vertex-taut (5b)-profile pair anywhere in
the window** (defeats (F) in both forms and is one 2-path closure
away from a tight 1-atom — disproof-adjacent; **this is exactly what
each `E028` rung tests**, and it is the trigger to watch on every new
rung); ~~a **proof of (F-S) or (F-T) on the window**~~ (**superseded,
S027**: (F) is decided directly per order by `E028`, empty at every
order 16–30 on the Hamiltonian stratum — the live remainder is the
non-Hamiltonian stratum, `A027` T5, plus continuing the ladder, which is
open-ended and above order 26 proves class-emptiness rather than poison
forcing);
~~a profile object, at any order, with a hole in \(S\) at a value
\(\ge8\)~~ (**fired and spent, S031**: `L056`/`L057` exhibit them — the
distance stratum kills (INT) and (INT-14) outright, the parity stratum kills
every relativized form. The trigger has no live successor of that shape,
because the *genre* is closed, not just the conjecture);
~~Prove the Hamiltonian forcing (27/27 as a
lemma)~~ (**dead, S030**: `L053` — the class-level hypotheses do not
force it; calibration object #3);
**NEW, S031 — the live primary triggers.** (i) A **power-free vertex-taut
profile pair anywhere in \(H\)-orders \([22,40]\)** — disproof-adjacent,
report immediately; the window is `L058`'s, wider at the top than the
records previously said. ~~(ii) a \(\{C_4,C_8\}\)-free profile pair of order \(\le35\) with
\(\min S\ge9\)~~ (**answered immediately, `R004` F4**: truncated Petersen
minus a link edge, order **30**, \(S=[9,26]\) — so `L056` is in-window and
this is no longer a question. The open remnant, worth recording if seen but
not a trigger, is the *smallest* such order: it is \(>20\) by `C046` and
\(\le30\)). (iii)
Any lemma drafted for the non-Hamiltonian stratum that **holds** on
Calibration object #3 — that is a soundness alarm on the draft, since the
object satisfies every class-level hypothesis at arbitrarily large order.
**Calibration object #3 is now the primary calibration object for the (F)
side, ahead of Petersen\(-e\)**, and the check is mechanical: if a lemma's
hypotheses are girth-monotone and its conclusion names a value below the
girth, it is false;
a **failure of the `E028` growth trend** (a rung whose node count
breaks \(\approx\times1.9\) badly enough to stall the ladder before
order 35 — then the decision route needs a stronger prune or the T5
bridge theory must carry more);
exclusion of case (5b) outright (then `G015` is proved and Thread C
becomes the whole game).

### Process correction (S018)

Sixteen audits in a row selected the route with the cheapest decisive
computation. That criterion is what buried `G015` and what kept a
conjecture-complete object on the live list for six sessions. From now
on, a session's strategy audit must name the tier its selected route
serves, and must justify any Tier 3 selection as *background*, not as
the session's work.

## Human-level state

The programme's proof-side prize is one named theorem: **the conjecture
holds in general if and only if it holds for 3-regular graphs.** S019
attacked it down both of its routes at once — the first orchestrated
parallel session, one worker per route, everything audited before being
believed — and both routes moved.

The published-density route first: a 2026 paper of Carr proves that in
a smallest possible counterexample, at least 4/7 of the vertices have
degree exactly 3. We verified that paper line by line (it holds up),
then pushed the bound: at least two-thirds, plus a little more. The
push needed a genuinely new trick — the degree-3 vertices wedged
between two high-degree vertices act like markers on invisible edges,
and those invisible edges form their own smaller graph which inherits
the no-power-of-two property with all lengths halved; because the
original graph was the *smallest* offender, the smaller shadow graph
must be sparse. But the same session also proved this route can go no
further: an explicit 15-vertex example meets every hypothesis the
counting uses at exactly two-thirds density, and no percentage short of
100% ever delivers the reduction. So that route ends — honourably, with
a stronger theorem than the literature has and a reusable mechanism.

The internal route is now where the game is. The "single defect" graph
question (one vertex of degree 2, everything else degree 3 or more, no
power-of-two cycle) was analysed at its defect vertex, and of the five
possible local shapes, four are now impossible or lead exactly where we
want: a smaller offender, which a repaired argument converts into a
**3-regular** counterexample — which is the reduction succeeding, not
failing. One shape survives: the defect vertex sits on a triangle-free
"lens" whose two anchor points are both degree 3, with every vertex on
some anchor-to-anchor path. That single surviving configuration now
carries the whole theorem, and it is already known to be at least
17 vertices, two-connected, never two-colourable, and arithmetically
squeezed (its path lengths must hit some exact powers of two and miss
others).

S020 spent the order-16 search (empty — the dangerous object needs at
least 18 vertices) and killed the "remainders" proof route for good
(Petersen minus an edge satisfies every arithmetic condition the
dangerous configuration must satisfy, so no remainder argument can
ever exclude it).

S021 ran the two surviving moves in parallel — one worker on the
remaining proof idea, one building the search machine — and both
delivered.

The proof idea was the "cancellation across links of a chain" tension:
if the dangerous configuration were built like a chain of beads, each
bead is forced to contain certain forbidden path lengths while the
whole chain must avoid them — a tension that looked exploitable. The
session settled exactly what that tension is worth. On its own,
provably nothing: the forbidden lengths can always dodge each other
(the collision arithmetic is now a small closed table). But combined
with the search data the picture flips: each solid bead of such a
chain would itself have to be one of the rare graphs our searches have
been proving nonexistent, so **any chain-like dangerous configuration
needs at least 36 vertices**. Below that, the dangerous configuration
must be a single solid two-connected piece — one shape left, and the
cycles-interfering-with-each-other structure is now provably the only
kind of argument that can kill it.

The search machine got built the same afternoon: a modified version of
the standard graph generator that refuses ever to build an 8-cycle,
verified twenty-three ways against the old pipeline and against an
independently published census it reproduces exactly. It is roughly a
hundred times cheaper than the old filter-everything approach. Its
first production run emptied size 17 in forty seconds of wall clock
(the dangerous object now needs at least 19 vertices), and as a
by-product it swept the "minimum degree three" world — where any
counterexample to the whole conjecture must live — up through 19
vertices: empty, with the first unchecked orders independently
spot-audited against the old instrument (three slices, 38.7 million
graphs, all agreeing). A reader-supplied MathOverflow thread claimed
size 20 was already settled; auditing it showed its cubic computation
is right (and matches ours) but its leap from "no cubic example" to
"no example at all" silently assumes the very theorem this programme
is trying to prove — so we rejected that step and ran our own size-20
sweep, which needs no such assumption. It landed the same evening,
empty: **every counterexample to the conjecture now needs at least 21
vertices**, two better than the previous record, and the extremal
window is down to four sizes, 21 through 24. The same evening's runs
also emptied bipartite size 24 on the new machine (that class is now
clean through 24) and reproduced the thread's two cubic counts to the
digit — their computation was right, their inference was the only gap,
and nothing now rests on it.

S022 ran the two named moves in parallel — one worker dissecting the
near-miss graphs, one running the search ladder — and both delivered.

The dissection asked the one question the surviving proof route hangs
on: in the graphs closest to the dangerous configuration, is every
"blocking" cycle (the 8-cycle or 16-cycle that stops the graph from
being a counterexample seed) built by overlaying two terminal-to-
terminal paths — an *interference pattern* — or can a blocker exist
that the path system cannot see? The answer, across all 553 blocking
cycles of every closest object on record: **interference, every single
time**, and the trait tracks exactly the property ("every vertex
carries terminal-to-terminal traffic", vertex-tautness) that the
dangerous configuration is forced to have. Three small lemmas now pin
the mechanism down: under the conjectured completeness, the dangerous
object's entire "no power-of-two cycle" property becomes arithmetic of
its own path system — the one kind of argument the two earlier
impossibility theorems left alive. The lemma to prove next ("in a
vertex-taut graph, every cycle is such an overlay") is stated, its
evidence is strong (over 800,000 verified instances, zero failures),
its proof obstacles are named, and its kill tests are ordered and
cheap.

The search ladder swept sizes 18 and 19. Size 18: nothing. Size 19
produced a genuine first — the very first graph ever found with the
dangerous configuration's exact degree pattern — and it is killed
twice over, independently: a 16-cycle sits inside it, and its path
lengths hit two forbidden values. The new graph is itself the best
test object yet for the lemma above, and the overnight run launched
at close delivered: the lemma **survived** on it (all 411 of its
cycles are path overlays, zero exceptions); the size-20 sweep found
seven more graphs with the dangerous degree pattern — every one
killed by a 16-cycle, with each recovered one *also* hitting the two
forbidden path lengths, the same double death as size 19 — and the
size-19 consistency count came back exact. The lemma then survived on
all three of the size-20 graphs recoverable from disk (1,890 more
cycles, zero exceptions). Net: every single-defect seed now needs at
least 22 vertices, and the candidate lemma has passed its sharpest
cheap tests. The four size-20 graphs that fell outside a
data-retention window were regenerated (the stream recount matched
the original tally to the digit) and the lemma survived on them too —
so **all eight graphs in existence with the dangerous degree pattern
pass the lemma, on every one of their 4,661 cycles**, and every one
of the eight is killed by the same double mechanism (a 16-cycle plus
the two forbidden path lengths). And the size-21 sweep of the
minimum-degree-three world came back empty: **every counterexample
to the conjecture now needs at least 22 vertices**, and the extremal
window is down to three sizes, 22 through 24.

S023 finished what the overnight tests began. The two remaining cheap
attempts to kill the key lemma were run first — every candidate graph
with the right shape on 13 vertices, and every graph whatsoever up
through 8 vertices — and the lemma survived all of them, tens of
millions of cycles with not one exception. Then, instead of the
planned delicate argument about controlling how paths wind through a
cycle, a much simpler idea landed the proof outright: route a path
through any chosen edge of the cycle, throw away everything between
its first and last touches of the cycle, and complete the two kept
ends around both sides of the cycle. The two hybrid routes so built
are the desired pair, and all the winding one feared lives entirely
in the part that was thrown away. A fresh, isolated referee — given
only the claim and the proof, none of the discovery reasoning —
attacked it, re-ran every computation independently, rebuilt the
whole verification from scratch in its own code, and passed it with
only cosmetic repairs, each now applied. So the pattern spotted two
sessions ago ("every blocking cycle is an interference pattern of two
terminal-to-terminal paths") is now a theorem wherever the dangerous
configuration can live, and that configuration's defining
no-power-of-two property is now, provably and unconditionally, a
statement about the arithmetic of its own path system. What remains
of this branch of the programme is exactly one named question — the
forcing question: do the path lengths that configuration is *forced*
to have always collide into a power-of-two cycle when the graph is
small enough? Answer yes below 36 vertices, and the programme's
centerpiece theorem (the cubic reduction) is proved there.

S024 took that question's first step: it built the complete
"collision tables" of all ten graphs closest to the dangerous
configuration — for every power-of-two cycle in each graph, every way
that cycle arises as two terminal-to-terminal paths overlaid in the
theorem's normal form. The question the tables were built to answer:
do the special path lengths the dangerous configuration is forced to
carry (powers of two and their neighbours) drive the collisions? The
answer is a clean no — the collisions run through ordinary lengths,
thirty of the cycles involve no special length at all, and the two
small graphs where power lengths did drive everything turn out to be
small-size artifacts. That kills one candidate proof mechanism early
and cheaply, and the same tables revealed what actually governs the
collisions: geometry and size, not length arithmetic. Two facts stand
out. First, a newly proved (small) lemma: the shared part of any such
overlay must fit entirely outside the cycle, so at the sizes in
question the collisions have almost no room — a bound the data meets
exactly on every one of the ten graphs. Second, saturation: each of
the eight frontier graphs has cycles of *every* length except exactly
4 and 8, and terminal-to-terminal paths of *every* length from 6 up —
in particular the two "poison" lengths (6 and 14) whose presence
dooms a candidate seed. So the forcing question sharpens into two
concrete alternatives, either of which suffices below 36 vertices:
prove that in the critical size window every candidate is forced to
carry a poison path length, or prove it is forced to carry a
16-cycle. The next move is a direct census over the already-generated
databases: does any graph in the window escape both poison lengths?
If none does, the first alternative survives its cheapest test; if
one does, it is a named new test object and the attack shifts to the
second alternative.

S025 ran that census — every pair of degree-2 vertices of every
graph in the databases, three-quarters of a million graphs, nearly
nineteen million pairs, with the search code cross-checked against
two older independent programs on every interesting case and the
whole run executed twice with identical counts. The answer has two
halves, both sharp. First: no graph with the dangerous
configuration's exact shape (exactly two degree-2 vertices) escapes
the poison lengths — the eight known such graphs all carry both
poisons, and no ninth shape-matching graph exists in any database —
so the "poison is forced" alternative survives its cheapest kill
test exactly where the dangerous configuration would have to live.
Second, and just as important: graphs that are *near* the shape but
not exactly on it (three or more low-degree vertices instead of two)
escape the poisons freely — over nine thousand escapes, many on
graphs that also avoid all the forbidden cycles, growing rather than
dying out as size increases. So the escape phenomenon is real and
abundant right up to the wall, and it stops exactly at the shape
itself.

S026 dissected those nine thousand escapes against the eight
shape-matching graphs, and the anatomy came out cleaner than hoped.
Every escape works one of three ways, each rigid: keep all paths
short (the longest terminal-to-terminal path is *always* exactly 13
— one below the poison), start too far apart (distance exactly 7,
never more), or run a striking arithmetic pattern where the
even-length paths come only in multiples of four (killing lengths 6,
10 and 14 together). Three structural facts explain the escapes.
The escape belongs to the *pair*, not the graph — the frontier
graphs carry one escaping pair alongside five fully saturated ones,
so no whole-graph explanation can work. Every escape rides on
"corridor" vertices — degree-2 vertices that would be forbidden in
the exact shape — and 99% of escapes, when those corridors are
contracted away, reveal a graph that violates the forbidden-cycle
rules: the escapes are stretched-out versions of illegal graphs,
and the exact shape is precisely the class that cannot stretch.
And the escape frontier now stands two corridor vertices from the
exact shape. On the positive side, a concrete engine emerged: on
each of the eight shape-matching graphs, take one longest
terminal-to-terminal path and reroute it along its shortcut edges
(a one-line rule says shortcuts spanning 3 or 7 steps cannot exist,
because they would close a forbidden cycle) — and those reroutes
alone already produce every path length from 10 up to the maximum,
including both poisons, on all eight graphs, while provably
producing none of the escapees' missing lengths. The proof problem
is now two named lemmas: show that the exact shape in the critical
size range cannot keep all paths short (the thin-margin half), and
show that its shortcut structure always reaches down to a poison
length (the half the new engine covers).

S027 did not prove either lemma. It made them unnecessary — for most
of the remaining ground — by turning the question into something a
computer can settle outright, one size at a time.

Two small observations did it. First: in the exact shape, *every*
vertex of a full-length terminal-to-terminal path must have a shortcut
edge attached, because every vertex except the two endpoints needs a
third edge and there is nowhere else for it to go. So the shortcut
edges "cover" the path. And if we throw away every shortcut edge that
isn't needed for that covering, nothing we care about gets worse: the
graph stays inside the forbidden-cycle rules, its terminal-to-terminal
path lengths only shrink, and the degrees stay right. So a hypothetical
bad graph can always be assumed to be **shortcut-minimal** — which is a
finite, small family at each size. Second: rerouting along
non-overlapping shortcuts always produces a genuine path, so finding one
whose total saving lands on a forbidden length immediately disqualifies
the candidate — and that test can be applied to a half-built graph, not
just a finished one.

Together these turn "prove a lemma" into "enumerate a finite family and
check". Two further choices made it practical. We stopped trying to
prove either of the two alternative death sentences separately (a
forbidden path length, or a 16-cycle) and instead asked only that *at
least one* holds — which is all the programme needs, and which hands us
the absence of 16-cycles as a **free extra assumption**. And we counted
the forbidden path lengths honestly: 30 is one of them too, which
matters at the large end.

The result: at every size the search has reached — 16 through 29 — **there
is no such graph**. That is the programme's target question, answered
outright, eight sizes past where the previous machinery had reached, in
under an hour. The free extra assumption is what made it possible: it cut
the growth of the search from roughly three and a half times per size to
under two.

An independent referee, given only the claim and the code and none of the
reasoning, attacked all of it, re-ran the search outside the repository and
reproduced the numbers digit for digit, wrote its own search from scratch
and got the same answers, and passed the mathematics. It also found four
real problems with the *evidence*, two of which matter. First: the large
test suite, impressive as its size looked, never once made the crucial
sub-test say "yes" — every check of the 16-cycle detector ran on graphs too
small to contain a 16-cycle, so a bug there would have produced exactly the
clean sweep we observed. That gap is now closed with tests that force the
detector to fire, hundreds of times, at every size in range. Second, and
more interesting mathematically: past size 26 the "forbidden path length"
test stops doing any work at all — the graphs are already ruled out on
shape alone. So above that size we have proved something *stronger* than
intended (no such graph exists at all, whatever its path lengths) but
learned *nothing* about why the forbidden lengths appear. And the honest
reading of the growth rate is that the remaining sizes, 30 through 35, are
days of computing rather than hours: this is an open-ended ladder with a
stated last rung, not a finished sweep.

Two by-products are worth recording. The search produced the **first
exact-shape graphs ever exhibited at sizes 21 and 22** — ten and
forty-three of them — and every single one dies twice over, exactly as
all eight previously known ones did. And thirteen of the size-22 ones
break a pattern that had held on all eight: their terminal-to-terminal
path lengths are no longer a solid unbroken run (one length, 6, is
missing). So the "everything is present" explanation that had been
guiding the search is *not* the real mechanism — but the real mechanism
survived its first counterexamples, because those thirteen still carry
the length 14 and still carry a 16-cycle.

What is left is one honest gap: all of this assumes the graph has a
terminal-to-terminal path passing through *every* vertex. Every known
example does, but that is not proved. Closing that case is the next
piece of work, and it already has a first foothold — a detour that
saves nothing forces a very rigid two-colourable sub-structure, which is
exactly the family a different arm of this programme has been emptying
for several sessions.

S029 finished the big overnight survey at size 21 — nothing there
either, and all nineteen graphs of the right shape do have a route
through every point, twenty-seven out of twenty-seven overall against a
base rate near a quarter.

S030 asked whether that pattern could be turned into a proof, and the
answer is no. There are graphs of exactly the right shape, obeying every
structural rule, with no such route — they are just large. So the
pattern is real at the sizes we can search and false in general, and the
untouched case has to be handled on its own. Two literature lookups were
the whole cost.

Then it was handled, in part. The sticking point had been that a detour
hanging off the main route could in principle be a pure liability: it
covers ground while shortening nothing, which is what made the argument
stall. Two independent arguments now show that cannot happen. If the
detour touches the main route in three or more places, a short
calculation on the three legs of a Y forces one of its shortcuts to save
at least two steps — using nothing but the fact that the route was
chosen as long as possible. If it touches in exactly two places, then
either it saves something, or it is two-colourable in a very rigid way,
and a two-colourable piece of that kind hands us an outright
counterexample to the conjecture. Every detour pays. One more piece is
needed before this becomes a decision procedure, and it is named.

The third finding is accounting, and it is the important one. The search
ladder everyone has been climbing can only ever settle sizes below
thirty-six — not because the computer is slow, but because the
structural fact that sets up the whole question is only available below
thirty-six. Above that the ladder says nothing, however far it goes. And
a by-product of the first result shows its recent rungs have been
proving something that must stop being true at some size. So the
programme needed a route whose strength does not depend on size, and
there is one, hiding in the data: in every one of these graphs so far,
the set of achievable route-lengths has no holes above eight. If that is
a theorem then the length fourteen is always achievable, and fourteen is
exactly one of the lengths that kills a candidate — settling the case at
every size, with no search. Tested against everything on disk, it holds
on all twenty-four graphs of the right shape whose descriptions we
store, their holes stopping at six; eight is the smallest threshold the
data allows; and the nearest near-miss to fourteen needs five more
low-degree vertices than the shape permits. It is a conjecture, and
nearly two thousand graphs on disk break it the moment the shape
constraint is relaxed — which is precisely what any proof will have to
use.

S031 tested that conjecture against one more object, and it is false.

The object is not new. The previous session had *built* it, for a different
purpose: a large cubic graph with no short cycles at all, minus one edge. It
has exactly the right shape, obeys every structural rule, and is
two-connected — so it satisfies every hypothesis of the conjecture. But
because it has no short cycles, the two special points are far apart, and
**every** route between them is long. There is no route of length eight, and
none of length fourteen either. The conjecture, and the weaker version that
only asks about fourteen, are both simply false. The stored evidence could
not have caught this: every graph on disk has its two special points close
together. The survival of the earlier test measured the size of the
collection, not the truth of the conjecture.

An independent referee, given only the claim and the proof, then made the
result considerably worse for the conjecture. The session had guessed that any
such graph must have about seventy vertices — comfortably outside the range
that matters. That guess was wrong, and the referee produced the graph: take
the Petersen graph, blow every vertex up into a small triangle, and delete one
of the connecting edges. Thirty vertices, obeying every structural rule, and
the shortest route between its two special points has length nine — so length
eight is unreachable. **The conjecture fails inside the very size range the
search ladder is climbing**, not off at infinity. Joining two copies end to
end gives fifty-nine vertices with no route shorter than eighteen, which kills
the version that only asks about fourteen. Both were rebuilt and checked
here.

The obvious repair — ask only that there be no gaps *above the shortest
route* rather than above eight — was tested too, and also fails. Take a
two-colourable graph with no short cycles and replace one vertex by a
triangle: the result still has the right shape and is no longer
two-colourable, but routes of one parity stay cheap while routes of the other
parity become enormously expensive, so the achievable lengths have a long gap
immediately above the shortest one.

That makes three whole styles of argument now proved unable to settle this
case: remainder arithmetic, membership arithmetic, and now length
interpolation. They fail for the same reason, and the reason is diagnostic.
Each uses only *local* properties — how many edges at each vertex, which
short cycles are banned, that every vertex carries traffic — and every one of
those is shared by large graphs with no short cycles, where the arithmetic
the argument wants simply does not happen. The two properties the dangerous
object has that those decoys do not are that it avoids powers of two *above*
its own shortest cycle, and that it is the smallest of its kind. Neither has
ever been used.

A fourth finding is bookkeeping, and it also runs against us. The search
ladder's reach is bounded by a structural fact whose numerical threshold was
last computed three rounds of search results ago. Recomputing it moves the
range that needs covering from "sizes eighteen to thirty-five" to "sizes
twenty-three to forty-one". The ladder has reached thirty. So it is ten sizes
short of its own target, not four — and each further size costs roughly twice
the last.

## Resolution outlook

- Estimated chance of eventually settling the exact current statement: **7%**
- Previous estimate: 9% (S030); 9% (S029); 10% (S027)
- Reason for change: down two points, and every reason is negative information
  about **routes**, not about the problem. S030 held the estimate at 9% on the
  strength of an order-unbounded successor that offset its own ceiling
  finding; that successor is now **refuted**, not merely unproved (`L056`), so
  the stated reason for the previous estimate is withdrawn. Worse, the
  refutation is generic rather than incidental, and it is **not confined to
  large order**: the audit produced an order-30 witness, so (INT) is false in
  the very window the ladder is climbing. `L057` closes the relativized repair
  too (subject to its own re-audit), making **interpolation the third dead
  genre** after congruence and membership, and the shared diagnosis is now
  legible — every proof-side
  idea this programme has produced is expressible in *local, hereditary*
  hypotheses, and every such idea is defeated by a large-girth cubic graph
  minus an edge. The one arithmetic improvement, `L058`, also runs the wrong
  way: the window the ladder must cover is \(n_0\in[23,41]\), so ten rungs
  remain rather than four. Against that, nothing proved was lost — the floors,
  `L049`, `L052`, `L055` are untouched — and the session cost two theorems'
  worth of effort instead of a spent route.
- Basis: most promising route is the **non-Hamiltonian stratum** (`A028` T8's
  two gaps), which has a proved engine (`L055`) and a bounded objective; the
  live alternative is the first (F)-side lemma to consume power-freeness
  **above the girth** or minimum-order minimality, which is the only shape the
  three dead genres leave open and for which no proof step exists; strongest
  obstacle, now stated sharply — **no (F)-side lemma has ever consumed either
  of those two hypotheses**, and `L056`/`L057` show nothing weaker can work;
  the evidence that informed the judgment is `L056` (a proved refutation of
  the recorded architecture, with an explicit **order-30** witness inside the
  window — audited `R004`, which strengthened it), `L057` (the same for the
  relativized repair, audit **FAIL** and repaired but not re-audited) and
  `L058` (the window is wider at the top and higher at the bottom), against
  the standing facts that no order of the non-Hamiltonian
  stratum is cleared and that even full success on case (5b) proves the
  **cubic reduction** (`G015`), not statement 0.1 — Tier 0 still has no cheap
  move.

## Resume reading

1. `STATEMENT.md`
2. **`A029`** (this arc's attempt: **T1** the distance stratum refuting (INT)
   and (INT-14), **T2** the triangle expansion refuting every relativized
   form, **T3** the three-dead-genres diagnosis and the conditional dyadic
   pinning, **T5** the re-derived order dichotomy and the real window, **T4**
   the re-aim) and **`R004`** (its delegated audit). Read `A029` T3(a) before
   drafting any new (F)-side lemma: it tells you which shapes are already
   proved impossible.
3. **`A028`** (the previous arc: T1 no class-level Hamiltonian forcing +
   calibration object #3, T2 the bipartite exclusion dichotomy, **T3–T7 the
   positive-savings theorem** and the bridge span/coverage laws, **T8 the two
   remaining gaps — the live work**, T9 the ceiling and the now-refuted
   (INT) ∧ (L-A) successor); `E029/README.md` only for what `C050` measured,
   not for what it concluded
4. **`A022` W1-T8** (the order dichotomy whose constant `L058` supersedes),
   then **`A027`** (the chord-minimal descent T1, the monotone-reroute prune
   T2, what the search decides T3, the calculus's reach T4, the
   non-Hamiltonian residue T5 that `A028` T3–T5 discharges, the corrected
   chord-pair table T6) and **`E028/README.md`** (the instrument, the anchors,
   both ladder runs); then **`A026`** (the dissection, the span law, and the
   chord-exchange calculus — a true statement about the measured objects, and
   **not** promotable to a class-level theorem, `L056`) and **`A025`** (the
   (F-S)/(F-T) frame); then `A024`/`A023` (the T5 theorem and interference
   frame) and `A019` (the case analysis, the engine/peel, the residual object)
5. **The live work is proof-side, not the ladder.** The `E028` ladder is
   **stopped** at \(H\)-order 30 (`S028`) and demoted to a source of floors
   (`S030`): it cannot prove `G015` at any length, because `L058` supplies
   2-connectivity only below \(n_0=42\), and it is now **ten** rungs short of
   even that window. Do **not** restart it, and do not re-run `E024`
   (harvested, `C049`). The next move is `A029`'s exit action — close `A028`
   T8's two gaps on the **non-Hamiltonian stratum**; do **not** pursue (INT),
   which `L056`/`L057` refuted. If a search is ever wanted again, `E028`
   resumes with
   `nice -n 15 pypy3 search.py search <M0> <M1> c16` (anchors first, both
   interpreters), and a survivor passing the exact stage is a case-(5b)
   residual object — **report immediately, disproof-adjacent**.
6. `R003` (the delegated audit of the descent and the instrument), then
   `E027/README.md` (the dissection: taxonomy, frontier, subdivision frame,
   control rates, the exchange validation) with `corpus_rows_compact.json` as
   the per-row refutation set for any *profile-consuming* draft;
   then `E026/README.md` (the census) and the `E021`/`E022` READMEs for the
   imported instruments
7. `A021` (the congruence kill and the calibration discipline —
   Petersen\(-e\) shows \(C_8\)-freeness is necessary for (L-A); calibration
   object #3 of `L053` is now the **primary** calibration object for the whole
   (F) side, and `L056`/`L057` are what it killed) and `A022`/`E020` (the
   chain package and its 15/16 kill rung)
8. `CLAIMS.md` rows `L056`–`L058` (new, S031), `L053`–`L055`/`C050` (S030),
   `C049` (S029), `L052`/`C048` (S027), `C047` (S026), `C046` (S025),
   `L051`/`C045` (S024), `L049`/`L050`/`C044` (S023) (and `L039`–`L048`,
   `C036`–`C043` for the frame), plus the **dependency notes at the foot of
   `CLAIMS.md`**, which record exactly how far `L053`–`L058` and `C050` may be
   cited; `OBLIGATIONS.md` `G015`/`G013`
9. `sessions/S031-…md` (this session: the omitted kill test, the dead genre,
   the re-derived window) and `S019`–`S030` for the preceding arc
