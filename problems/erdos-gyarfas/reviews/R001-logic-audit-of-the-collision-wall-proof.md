# R001 — Logic and dependency audit of the collision-wall proof

- Date: 2026-07-24
- Problem: `P-002`
- Reviewed statement version: 0.1 (main statement unchanged; the review
  target is the lemma-level result `L023`/`L024`, i.e. W1–W8 in
  `attempts/A010-the-collision-wall-lemma-identity-voltage-tailless-walks-at.md`)
- Reviewed proof revision: A010 as of session `S010`
- Review type: logic — logic / hypotheses / counterexample / computation / exposition
- Independence mode: delegated-subagent
- Note: created manually because `proofctl.py review` gates on a
  main-statement proof candidate; this is a lemma audit and the main
  claim status is unchanged (`open`).

## Verdict

**Pass at lemma level.** The mathematical core is sound: W1–W6 are proved,
Theorem W7 is proved as stated (both bullets and the "in particular"
power-of-two form with \(C=4\), \(C_B=4\lceil\log_2 m\rceil+4R_B+24\)),
and W7 + W8's displayed interval argument deliver exactly the formal
statement that `G012` asks for. Every junction check, parity computation,
and threshold inequality in W7 was re-derived independently and holds; the
voltage telescoping uses no commutativity. No critical or major finding.

Three **minor** findings (F1–F3) concern import hygiene and the scope of
W8's closing prose, and should be repaired when `L023`/`L024` are entered
into `CLAIMS.md` and `G012` is resolved. Three **notes** (F4–F6) are
nonblocking. The E009 computation reproduces exactly, and an independent
conclusion-level probe (different algorithm, different bases, different
groups) found no violation of W7 on 3,136 admissible lengths.

## Findings

| Finding | Severity | Location | Issue | Required resolution | Obligation |
|---|---|---|---|---|---|
| F1 | minor | W5, proof, "(Schur: … finite Frobenius bound)" | The numerical-semigroup fact — a set of positive integers closed under addition with gcd \(p\) contains every sufficiently large multiple of \(p\) — is asserted by name, not derived, and has no `references/` entry. A010's entry assumptions ("standard finite group theory; elementary graph theory") do not cover it, and the attempt claims "no external theorem is imported." | Either give the standard three-line proof inline (pick \(g_1,\dots,g_k\in S\) with \(\gcd=p\); Bézout integers \(u_i\) with \(\sum u_ig_i=p\); every multiple of \(p\) above \(k\max_i\lvert u_i\rvert g_1\cdot\max_i g_i\) is a nonnegative combination), or add a `references/` entry (e.g. Brauer 1942 / Ramírez Alfonsín, *The Diophantine Frobenius Problem*) and drop the "no external theorem" claim. | none required (repair at promotion) |
| F2 | minor | W8, first sentence; Remark "walks, not cycles" | W8 invokes "the `L019` walk certificate" for **every** finite group \(\Gamma\), but `CLAIMS.md` records `L019` for \(\mathbb{Z}_m\)-voltage assignments only. The group-agnostic form exists in the dossier (the `C022` row cites "`L019`/`L020` in their group-agnostic form (`A009`)"), but it is not a ledger row, so W8 as written cites `L019` above its recorded strength. Concrete instance: W8 applied to \(A_5\) on the prism references a certificate that `L019`'s row does not define. | When promoting `L024`, either promote the group-agnostic projection lemma (proved in `A009`) as its own claim row and cite it, or make `L024`'s dependency read "group-agnostic form of `L019` (`A009`)" exactly as `C022` does. | none required (repair at promotion) |
| F3 | minor | W8, closing sentence ("the voltage-certificate route to a counterexample is closed for all finite groups with an effective bound") | Overstated scope. What is proved: (i) W7's walk theorem for **all** \((B,\Gamma,\alpha)\) with no size restriction; (ii) certificate failure inside the L019 window \([\,4\log_2\lvert\Gamma\rvert+C_B,\;n\lvert\Gamma\rvert\,]\) only when \(\lvert\Gamma\rvert\ge\Gamma_0(B)\); (iii) finite verdicts `C020` (six bases, all \(\mathbb{Z}_m\)) and `C022` (three group orders, four bases). The regime "small fixed \(\Gamma\), large \(B\)" is untouched: e.g. \(\Gamma=\mathbb{Z}_2\) on a chain of \(t\) triple-edge blocks (\(n=t+1\), \(\delta\ge3\), diameter \(t\)) has \(R_B\ge t-O(1)\), so \(C_B+4>2n=n\lvert\Gamma\rvert\) for large \(t\) and the certificate window contains no power of two — W7/W8 then say nothing about those certificates (`L021` might, but W8 does not invoke it). `PROOF.md`'s own phrasing ("close the lift-certificate route for all finite voltage groups **on the tested bases**") is the correctly scoped version. | Scope the `L024` row and the `G012` resolution text to: per-base effective closure for \(\lvert\Gamma\rvert\ge\Gamma_0(B)\), plus the finite verdicts; do not record a blanket "closed for all finite groups" over all bases. | none required (repair at promotion) |
| F4 | note | `G012` text vs. W7 | `G012`'s parenthetical promises `G007` "identity-voltage closed walks forced at every **even** length past a log threshold." W7 forces \(L\equiv0\pmod4\) in general and every even \(L\) only for non-bipartite bases. A010's own proof-side reading states this correctly; the `G012` resolution note should record the mod-4 restriction for bipartite bases so `G007` inherits the true strength. | State the mod-4 caveat in the resolution column of `G012`. | — |
| F5 | note | A010 Exit state vs. `CLAIMS.md`/`OBLIGATIONS.md` | A010's exit state says "Promoted records: `L023`, `L024` to `CLAIMS.md`," but `CLAIMS.md` contains no such rows, and `G012` is still `open`. The canonical records are the conservative (correct) side of the conflict; the attempt prose is ahead of the ledger. | When acting on this review, perform the actual promotion (with F2/F3 scoping) or amend the exit-state wording to "pending promotion." | — |
| F6 | note | W7, Branch step | The choice of two **distinct** continuations \(x\ne x'\) is never used: no junction condition involves \(x\) versus \(x'\) (junctions 1 and 3 rest on \(e\ne f\); junctions 2 and 4 on the seed's distinct first arcs), and \(T_2>T_1\) always. The construction would be correct with \(x=x'\). Harmless, but the proof text implies the distinctness carries load. | Optional: note the redundancy, or keep \(x\ne x'\) and say it is for exposition only. | — |

## Statement correspondence

- **Target.** `G012` (OBLIGATIONS row): for every finite group \(\Gamma\),
  every connected base of minimum degree \(\ge3\), and every voltage
  assignment, a tailless non-backtracking closed walk of length \(2^k\)
  with identity net voltage exists for every
  \(2^k\ge C\log_2\lvert\Gamma\rvert+C_B\), \(C\) absolute, \(C_B\)
  depending only on \(B\). Theorem W7's "in particular" clause delivers
  exactly this with \(C=4\) and \(C_B=4\lceil\log_2 m\rceil+4R_B+24\),
  both effectively computable from \(B\); the two bullets are strictly
  stronger (all \(L\equiv0\bmod4\); all even \(L\) when non-bipartite).
  Verified: any \(2^k\ge4\log_2\lvert\Gamma\rvert+C_B\) satisfies
  \(2^k\ge24\), hence \(4\mid 2^k\), and the strict inequality
  \(4\ell^*+4R_B+8\le4\log_2\lvert\Gamma\rvert+4\lceil\log_2m\rceil+4R_B+20<4\log_2\lvert\Gamma\rvert+C_B\)
  holds (20 < 24), so the first bullet applies. No quantifier is shifted:
  the seed, branch, and steering are chosen after \(\Gamma,\alpha,L\) are
  fixed, and the walk length is exactly \(L\), not merely \(\ge L\) or
  \(\equiv L\).
- **Conventions.** The multigraph/arc/voltage conventions are
  self-contained in A010 and do not conflict with `D001`–`D004`, which
  govern the simple-graph main statement. The lemma makes no claim about
  `C001`; the "walks, not cycles" and basepoint remarks correctly disclaim
  the two ways the result could be over-read. `PROOF.md` contains no
  premature integration (candidate status: none).
- **W6/W7 interface.** W6's seed properties (length
  \(\lambda_1\in[2,\ell^*-1]\), common endpoints, equal voltages, distinct
  first arcs, shared last arc) are exactly the properties W7 consumes; the
  \(\lambda_1\le\ell^*-1\) upper bound is the one used in the threshold
  chain \(N_0=\tfrac L2-2\lambda_1-2\ge2R_B+4\), which I re-derived and
  confirm (it needs precisely \(L\ge4\ell^*+4R_B+8\)).
- **W8 vs `G012`.** W8's displayed claim (certificate failure at some
  \(2^k\le n\lvert\Gamma\rvert\) for \(\lvert\Gamma\rvert\ge\Gamma_0(B)\),
  \(\Gamma_0\) effective) follows from W7 plus "a power of two lies in
  \([x,2x)\) for \(x\ge1\)" — correct. Its closing prose overstates scope
  (finding F3), and its certificate naming exceeds `L019`'s recorded
  strength (finding F2).

## Dependency and circularity audit

Dependency DAG as used (verified line by line, no cycles):

- Conventions/(R) → W1, W6, W7. The reversal identity (R) and
  "reverse of nb is nb" were checked directly from the definitions
  (legality of \(a\to b\) iff \(\mathrm{head}(a)=\mathrm{tail}(b)\),
  \(b\ne\bar a\), which is symmetric under \((a,b)\mapsto(\bar b,\bar a)\)).
- W1 (uses only \(\delta\ge3\)) → W3 (out-degree \(\ge2\) of every state),
  W6 (the \(2^{\ell^*-1}\) count).
- W2 (uses only \(\delta\ge3\) and the arc-end count at a vertex) → W3.
  The equality-case bookkeeping was re-derived, including the loop
  accounting: a loop arc in \(C\) contributes 1 to out and 1 to in against
  the loop's two arc-ends, so \(\mathrm{out}_C(v)+\mathrm{in}_C(v)\le\deg(v)\)
  holds with loops; then \(\lvert C\rvert=\lvert S\rvert\) versus
  \(\sum_{v\in S}(\deg(v)-1)\ge2\lvert S\rvert\) distinct \(C\)-arcs forces
  \(S=\emptyset\). Sound.
- W3 (uses W1, W2; weak connectivity from scratch) → W4 (only for the
  "canonical partition" phrasing), W5. The anti-automorphism/sink-source
  argument is correct: sink \(T\) is continuation-closed, W2 gives
  \(x,\bar x\in T\), so \(T=\bar T\) is isolated in a weakly connected
  condensation, hence everything. The weak-connectivity steps (a)/(b) were
  checked including the case where the chosen in-arc \(c\) coincides with
  one of the target arcs (loop at the common vertex): the transitions used
  remain legal.
- W4 (standalone case analysis; loop/parallel/simple split is exhaustive
  and exclusive) → W5 (the "each transition switches tail-sides" fact),
  W7 (the value of \(p\)). The three-cycle arithmetic
  \((i+1)+(j-i+2)-(j+1)=2\) is correct and all three subgraphs are genuine
  cycles of length \(\ge3\) since \(2\le i<j\le t\); the bipartite/odd-cycle
  equivalences for multigraphs (loops odd, 2-cycles even and realizable as
  tailless nb closed walks) were checked.
- W5 (uses W3, W4) → W7. The residue bookkeeping is correct: length mod
  \(p\) is well defined per ordered pair, agrees with
  \(\chi(\tau)-\chi(\sigma)\) for \(p=2\), and the insertion argument gives
  every \(T\ge R_B\) of the right residue. The only asserted-not-derived
  step is the semigroup fact (finding F1).
- W6 (uses W1, pigeonhole over \(2m\lvert\Gamma\rvert\) values) → W7.
  \(2^{\ell^*-1}>2m\lvert\Gamma\rvert\) verified from
  \(\ell^*=\lfloor\log_2(2m\lvert\Gamma\rvert)\rfloor+2\); the
  \(\lambda_1\ge2\) exclusion (a length-1 suffix cannot have distinct first
  and equal last arcs) and \(\lambda_1\le\ell^*-1\) (else \(X=X'\)) are both
  correct, using left cancellation only.
- W7 (uses W4, W5, W6) → W8. The four junction pairs are exactly
  \((e,\bar f)\), \((\overline{\mathrm{first}(W)},\mathrm{first}(W'))\),
  \((f,\bar e)\), \((\overline{\mathrm{first}(W')},\mathrm{first}(W))\);
  each legality condition reduces to \(e\ne f\) or
  \(\mathrm{first}(W)\ne\mathrm{first}(W')\), which hold by construction
  and by the seed. The length identity \(2(t_1+t_2)=4\lambda_1+2N_0+4=L\)
  and the parity chain for \(p=2\) (\(L\equiv0\bmod4\Rightarrow N_0\)
  even \(\Rightarrow T_2\equiv-T_1\equiv T_1\equiv\tau\bmod2\)) were
  re-derived. The telescoping
  \(h_1h_2^{-1}h_2h_1^{-1}=\mathrm{id}\) is associativity-only; no
  commutativity is used anywhere (checked against the non-abelian probe
  groups as well).
- W8 additionally references `L019` (naming/interpretation only — findings
  F2, F3) and `C020`/`C022` (finite context). W7 does **not** use `L021`,
  the E008 heuristic wall, or any experimental output; `E009` is
  verification, not support. No circular dependency exists anywhere in
  W1–W8.

## Edge-case and counterexample audit

Cases actively attacked (all survived):

- **Single-vertex bouquet base** (two loops): W3's weak-connectivity step
  (a) alone must connect all four arcs — it does (\(\deg\ge4\), so a third
  out-arc always exists); W4 gives \(p=1\) via the legal self-transition
  \(l\to l\) (\(\bar l\ne l\)); W7's steering vertex \(z\) is the unique
  vertex. Verified computationally (bouquet2 × Z2/Z8/S3/Q8).
- **Loop arcs as the steering pair**: if \(e,f\) are the two arcs of one
  loop at \(z\) (\(f=\bar e\), possible only when \(p=1\)), junctions 1 and
  3 become \((e,e)\) and \((\bar e,\bar e)\), both legal since a loop arc
  is not its own reverse. No hidden failure.
- **Seed first arcs mutually reverse** (\(\mathrm{first}(W')=
  \overline{\mathrm{first}(W)}\), forced loop arcs at \(u_1\)): junctions
  2 and 4 are still exactly the condition
  \(\mathrm{first}(W)\ne\mathrm{first}(W')\); legal.
- **Bipartite multigraph with parallel edges** (not covered by E009): W4's
  parallel-edge branch plus the bipartite direction give \(p=2\); verified
  on the 4-vertex "bipmulti" base with doubled edges (probe below),
  including the class-advance property and the absence of odd closed
  walks.
- **Mixed loop + parallel base** and **loop hanging off a triple edge**:
  W2/W3/W4/W5 verified computationally (bases "mixed", "loop3").
- **Boundary seed lengths**: \(\lambda_1=2\) (maximal trimming) and
  \(\lambda_1=\ell^*-1\) (minimal trimming — the tight case of the
  threshold inequality) both leave \(N_0\ge2R_B+4\); the p=2 branch needs
  \(N_0\ge2R_B+1\) and the p=1 branch \(N_0\ge2R_B\); margins check out.
- **\(T_1=T_2\) degeneracy**: impossible (\(T_2\ge T_1+3\)), so
  \(xA\ne x'B'\); irrelevant anyway since no step needs the pieces
  distinct.
- **Hypothesis sharpness** (negating W2/W3 premises): at \(\delta=2\) the
  directed cycle's arc set is nonempty, continuation-closed, and
  reverse-free, and \(\mathcal A(C_n)\) is disconnected — so both lemmas
  genuinely consume \(\delta\ge3\), and the proofs use it exactly where
  claimed (W2's \(\deg-1\ge2\); W3's third out-arc; W4's three neighbors;
  W6's branching; W7's branch/steer choices).
- **Odd lengths / wrong residues**: the construction is inherently of even
  length \(2(t_1+t_2)\); the theorem claims nothing at odd \(L\) or at
  \(L\equiv2\bmod4\) on bipartite bases, and the probe confirmed
  bipartite bases have no odd-length closed nb walks at all (parity
  sanity).

No counterexample to any of W1–W8's formal statements was found, by hand
or by machine.

## Imported theorem and computation audit

- **Imports.** A010 claims no external theorem is imported. This is true
  except for the numerical-semigroup/Frobenius fact inside W5 (finding
  F1). The `L019`/`C020`/`C022` references in W8 are internal claims;
  `L019` is cited above ledger strength (finding F2). `C020`/`C022` are
  cited at recorded strength (finite certificate verdicts).
- **E009 re-run (recorded commands).** `python3 wall.py` reproduced with
  all checks passed, 686,933 assertions; `python3 wall.py --exhaustive`
  reproduced with 9,606,333 assertions — exactly the README's recorded
  count. Python 3.14.2, integer arithmetic, deterministic. Code audit:
  the checker `verify_walk` is definition-level (cyclic nb including
  wrap, closure, exact length, identity voltage from the raw arc list)
  and independent of the construction internals; negative controls
  present; `ell_star=(2m\lvert\Gamma\rvert).bit_length()+1` matches W6's
  \(\lfloor\log_2(2m\lvert\Gamma\rvert)\rfloor+2\); group tables are
  axiom-checked at load, including full associativity. The empirical
  \(R_B\) (stable-tail heuristic, horizon 200) is honestly disclosed in
  the README; the construction never assumes unverified reachability
  because `steer` fails loudly, so this caveat cannot leak an error into
  the verified walks. One benign strictness: `construct` requires
  \(N_0\ge2R_B+1\) even for \(p=1\) (theorem needs \(2R_B\)) — safe.
- **Independent probe (this review).** A conclusion-level check that does
  not reuse the A010/E009 construction: build the product digraph on
  states \((\text{arc},g)\) with edges \((a,g)\to(b,g\alpha(b))\); closed
  walks of length \(L\) (any basepoint) biject with rotations of
  identity-voltage tailless nb closed walks of length \(L\) in the base;
  existence is read off the diagonal of the boolean \(L\)-th power
  (bitset matrices, exact). Bases: theta3, bouquet2, loop3 (loop +
  triple edge), mixed (loop + parallel pair + path), bipmulti (bipartite
  with doubled edges), \(K_4\), cube \(Q_3\), Petersen — five of these
  are outside E009's base list. Groups (independent implementations,
  axioms fully checked): \(\mathbb{Z}_2,\mathbb{Z}_3,\mathbb{Z}_8,
  \mathbb{Z}_{21},S_3,Q_8\) — all outside E009's group list. Four
  deterministic assignments per pair (constant generator, distinct,
  affine LCG pattern, tree-trivialized). For every case the probe
  verified: W3 strong connectivity (forward/backward closure), W4 period
  via closed-walk gcd with the bipartite equivalence and class advance,
  W5 empirical stable reach (horizon 400, stability window 120), W6 seed
  existence and all five properties (independent BFS collision code),
  and the W7 conclusion at **every** admissible length from
  \(4\ell^*+4R_{\min}+8\) to \(+63\), where \(R_{\min}\) is the minimal
  empirical reach constant — a threshold at least as demanding as the
  theorem's (any valid W5 constant is \(\ge R_{\min}\)). Result: **all
  3,136 admissible lengths verified, zero failures**, across 108
  (base, group, assignment) cases; bipartite parity sanity passed; the
  observed onset of the gap-free regime was always far below the proved
  threshold, consistent with W7 being a conservative upper bound.
  PyPy 7.3.23, deterministic, no floating point. (Probe script in the
  session scratchpad; method fully specified above and in it.)

## Resolution audit

- No finding is critical or major; no new obligation is strictly required
  by the playbook. The verdict stands without repairs.
- Before or at promotion of `L023`/`L024` and resolution of `G012`, the
  invoking session should: (F1) add the inline proof or reference for the
  semigroup fact and correct A010's "no external theorem" sentence; (F2)
  cite the group-agnostic projection lemma at ledger strength; (F3) scope
  the `L024` row and `G012` resolution to per-base effective closure
  (\(\lvert\Gamma\rvert\ge\Gamma_0(B)\)) plus the finite verdicts, per
  `PROOF.md`'s existing "on the tested bases" phrasing; (F4) record the
  mod-4 caveat for bipartite bases in the `G007` hand-off; (F5) reconcile
  the exit-state/ledger discrepancy.
- This review is the logic/dependency audit. `process/proof-standard.md`
  requires a second, distinct audit only for main-statement promotion;
  for a partial-result claim row, `CLAIMS.md` may record `L023`/`L024` as
  proved with this review as support once F1–F3 are addressed, per the
  partial-results clause of the proof standard.

**Repair log (S010, post-verdict).** All five repairs were applied in
the same session: F1 — the numerical-semigroup fact now carries a full
inline proof in W5 (Bézout split \(P-N=p\), the ladder
\(x_b=qN+bp\), \(\Lambda=qN+g_1\)); no external import, so A010's
"no external theorem" sentence stands. F2 — W8 now cites "`L019` in
its group-agnostic form, proved in `A009`," matching `C022`'s citation
strength, and the `L024` row carries the same dependency. F3 — W8
gained an explicit scope paragraph (per-base closure for
\(\lvert\Gamma\rvert\ge\Gamma_0(B)\) plus the finite verdicts; the
small-group/large-base regime named as untouched, with the reviewer's
\(\mathbb Z_2\)-chain example), and the `L024` row and `G012`
resolution use that scoping. F4 — the `G012` resolution records the
mod-4 restriction for bipartite bases. F5 — A010's exit state now
matches the ledger after actual promotion. F6 — a parenthetical in
W7's branch step notes that \(x\ne x'\) is expository only.

## Independence note

Delegated to the `proof-reviewer` subagent in a fresh context. Reading
order: `STATEMENT.md`; this review record; `process/review-playbook.md`;
`process/proof-standard.md`; `A010` (the review target); `OBLIGATIONS.md`
(row `G012`). The initial verdict on W1–W7 was formed at that point. Then,
as permitted for the W8/certificate context and promotion-strength checks:
`CLAIMS.md` (rows `L019`–`L022`, `C020`–`C022` and dependency notes),
`experiments/E009` (README and `wall.py`, re-run in both modes), and
`PROOF.md` (to confirm no premature integration). Not read: `sessions/`,
`STATE.md`, `LOG.md`, `DECISIONS.md`, any attempt other than `A010`
(including `A008`/`A009`), and any other review. No exception was needed.
The invoking prompt contained the slug, record path, review type, target
description, and a list of areas to stress-test (junction checks, parity
and threshold arithmetic, multigraph edge cases); it contained no
discovery narrative, no proof reasoning beyond what `A010` itself states,
and no claimed verdict. Computations: E009 re-run under CPython 3.14.2
reproduced the recorded assertion counts exactly; the independent probe
(written from scratch for this review) ran under PyPy 7.3.23.
