# R004 — Logic audit of the interpolation refutations (A029 T1/T2)

- Date: 2026-07-26
- Problem: `P-002`
- Reviewed statement version: 0.1 (main statement unchanged; the review
  targets two lemma-level *refutations* offered as `L056` and `L057`)
- Reviewed revision: `attempts/A029-the-interpolation-genre-is-empty-…md`
  deductions T1, T2 and T3(b), as of session `S031`, before ledger promotion.
  **The attempt was revised twice while this audit was running** (see
  "Revision tracking"); the verdict below audits the **current** text.
- Review type: logic — logic / hypotheses / counterexample / computation / exposition
- Independence mode: delegated-subagent
- Note: created manually because `proofctl.py review` gates on a
  main-statement proof candidate; this is a lemma-level audit and the main
  claim status is unchanged (`open`). Same exception as `R001`–`R003`.

## Target identification

Under audit, verbatim from `A029`:

- **T1.** The object of `L053` (a cubic 3-connected simple graph \(F\) of
  girth \(\ge17\), minus an edge \(ab\)) is a vertex-taut
  \(\{C_4,C_8\}\)-free profile pair with \(\min S\ge16\); therefore the
  recorded conjectures **(INT)** (\(S\supseteq[8,\max S]\)) and **(INT-14)**
  (\(\max S\ge14\Rightarrow14\in S\)) are **false**.
- **T2.** The triangle expansion of a bipartite cubic 3-connected graph of
  girth \(\ge10\), minus an edge far from the triangle, is a *non-bipartite*
  vertex-taut \(\{C_4,C_8\}\)-free profile pair with a hole in \(S\) at
  \(\min S+1\ge10\); therefore no relativized form
  \(S\supseteq[\min S+c,\max S]\) holds, and the recorded pivot trigger
  fires.
- **T3(b).** The conditional dyadic pinning: an interpolation lemma plus
  `L042`'s forced memberships plus the poison condition would give
  \(2^j-2-c<\min S\le2^j\le\max S\le2^{j+1}-3\), hence
  \(\max S<2\min S+2c+2\).

## Questions the audit must answer

1. Is T1 correct, and in particular is every hypothesis of (INT) genuinely
   satisfied by the object — profile pair, vertex-tautness,
   \(\{C_4,C_8\}\)-freeness — with no hypothesis of (INT) overlooked or
   silently weakened when it was quoted?
2. Is `L053` being used inside its recorded scope, or does T1 extend it?
3. Is T2's connectivity argument complete, including the degenerate branch?
   Is the parity bookkeeping (\(k\in\{0,1,2\}\) triangle edges) exhaustive?
   Are the numeric thresholds (\(\rho\), diameter, girth) mutually
   consistent, i.e. does the hole provably open?
4. Is T3(b)'s derivation valid, and is it correctly labelled conditional?
5. Is anything claimed at greater strength than proved — in particular, is
   any floor, window, or status changed by these results?

## Verdict

**FAIL at lemma level** — because of T2 only.

- **T1, offered as `L056`: PASS.** (INT) and (INT-14) are false. In the
  current text the refutation is *not* asymptotic: it rests on two explicit
  finite graphs (orders 30 and 59) which this audit produced, verified from
  scratch, and then re-verified against the instrument the session added
  (`E030/truncation.py`). One residual minor overstatement (F17).
- **T2, offered as `L057`: FAIL — not proved.** Two items block promotion: an
  unproved bridge from the ambient hypothesis (a *diameter* bound) to the
  quantity the construction consumes (the *eccentricity of a pre-chosen
  edge*), F11; and an import row, `X004`, whose decoupled statement now cites
  no source for the regime it asserts, F3′. Everything else in T2 verifies.
  My judgement is that the T2 statement is **true and repairable in a few
  lines**, but it is not proved by the current text.
- **T3(b): PASS**, correctly labelled conditional, side conditions now
  carried.

Consequence for the portfolio: the interpolation genre is dead *absolutely*
(T1 — and now inside the window, not merely asymptotically). Its
*relativized* death is established against a bipartite defender by the "cheap
half" (\(\tilde F-ab\), all-odd through-set), and is **not yet established**
against the non-bipartite defender that `L042` licenses, which is the case
that matters. `L057` should not be promoted, and the pivot trigger should not
be recorded as having fired, until F11 and F3′ are closed.

### Revision tracking

The audit target moved twice under the review. To keep the record honest:

- **rev 1** (text as dispatched): T2(v) chose \(ab\) to maximise \(\rho\) and
  derived \(\rho\ge5\) from "diameter \(\ge5\)". Findings F1, F2 (critical),
  F3, F4 (major), F5, F7, F8 (minor).
- **rev 2** (mid-review): T2(v) rebuilt around \(\rho\ge g\) and an order
  bound \(N>1+3(2^{g-1}-1)\). This fixed F1 and F5 but still inferred the
  eccentricity of a pre-chosen edge from a diameter bound (and asked for
  \(\rho\ge g\), which \(\rho\le\mathrm{diam}-1\) makes impossible when the
  diameter is exactly the \(g\) the bound forces).
- **rev 3** (current): T2(v) rebuilt again around \(\rho\ge g/2\) and
  \(\mathrm{diam}\ge g/2+1\), with \(\rho\le\mathrm{diam}-1\) proved and the
  even bound sharpened to \(2\rho+2\); T1 rebuilt around the audit's order-30
  and order-59 witnesses; `X004` restated in decoupled form with the Tutte
  12-cage withdrawn; T3(b)'s side conditions carried.

The verdict, the findings table and the severities below describe **rev 3**.
Repairs are marked resolved only where I re-derived the repaired step myself.

## Findings

| Finding | Severity | Status | Location | Issue | Required resolution |
|---|---|---|---|---|---|
| F11 | major | **open** | T2 (v) choice 2; repeated as the "i.e." in `X004` "Hypothesis match" | "choose \(v\) with \(\rho=d(\{a,b\},v)\ge g/2\), **which is possible as soon as** \(\mathrm{diam}(\tilde F)\ge g/2+1\)" is a non sequitur. \(ab\) is already fixed (choice 1); what is consumed is \(\mathrm{ecc}(\{a,b\})\), and a diameter bound is a max over *all* pairs. From \(\mathrm{diam}=D\) one gets only \(\mathrm{ecc}(\{a,b\})\ge(D-1)/2\), so the diameter route needs \(D\ge g+1\), not \(g/2+1\). | Replace the diameter hypothesis by the **order** hypothesis \(N>2^{g/2+1}-2\) and prove the one-line ball bound \(\lvert B(\{a,b\},g/2-1)\rvert\le2+4(2^{g/2-1}-1)=2^{g/2+1}-2\). (I verified the stated implication is nevertheless *true*, but only via the bipartite Moore bound **and** its equality classification — Moore-extremal bipartite cubic graphs are generalized-polygon incidence graphs of diameter exactly \(g/2\) — none of which is in the record.) |
| F3′ | major | **open** (mutated from F3) | `references/bipartite-large-girth-cubic-2026-07-26.md`, `X004` | The row now asserts, at `reported-classical` strength, the *decoupled* statement (bipartite, cubic, **3-connected**, girth \(\ge g\) fixed, diameter \(\ge D\) arbitrary). Its only 3-connectivity support was "cages of girth \(\ge5\) are 3-connected" — and the same revision **withdraws cages** as witnesses because they are extremal in the wrong direction. Erdős–Sachs (`X001`) and the double-cover route give no connectivity, as the row itself states. So the regime asserted has **no source**. | Cite a source, or derive it: e.g. for cubic graphs \(\kappa=\kappa'\) (already used for `X002`), so it suffices to import bridgeless/cyclically-connected bipartite cubic families of fixed girth and unbounded order; or import the standard random-cubic fact. Until then `L057` rests on an unsourced existence claim. |
| F17 | minor | **open** | T1 boxed claim | "a vertex-taut \(\{C_4,C_8\}\)-free **2-connected** profile pair of order 30 …, **and one** of order 59" — the order-59 chain is *not* 2-connected: the identified vertex is a cut vertex by construction. (INT-14) needs only vertex-tautness, so nothing downstream breaks, but the adjective must not be inherited. | Split the two witnesses' adjective lists. |
| F12 | minor | **open** | T2 (v), the \(\max S\) step | "\(v\) is not a cut vertex of the 2-connected \(\tilde F-ab\), so some \(a\)–\(b\) path of \(\tilde F-ab\) passes through \(v\)" — non-cut-vertex-ness does not produce a path through \(v\). | Cite what is already proved: \(H=F_1-ab\) is 2-connected, hence vertex-taut, so \(v_1\) lies on an \(a\)–\(b\) path of \(H\), which meets \(T\). One line, no new machinery. |
| F13 | minor | **open** | T2 (v), "Arbitrarily long holes" | "letting \(\mathrm{diam}(\tilde F)\to\infty\) … makes \(\rho\) … arbitrarily long" is asserted. | True in one line via \(\mathrm{ecc}(\{a,b\})\ge(\mathrm{diam}-1)/2\); state it. |
| F14 | note | **open** | `E030` record; `X004` "Strength" | `E030/README.md` documents only `check.py` (the girth-6 Haar instance); `truncation.py`, which now carries T1's operative witness, is undocumented, and the README's results table still quotes T2's pre-repair \([g,2\rho)\) form. `X004` says T1's witnesses "of orders 30 and 59 [are] verified in `E030`" — only the order-30 one is machine-verified there; the order-59 chain is *derived* (correctly) by Minkowski additivity. | Document `truncation.py`; state the 59 as derived. |
| F15 | note | **open** | T2 (iv) | The parenthetical "\(k=0\) covers both '\(Q\) misses \(T\)' and '\(Q\) passes through exactly one \(T\)-vertex'" describes a case that cannot occur: each \(v_i\) has exactly one non-\(T\) edge, so a path visiting \(v_i\) internally uses a \(T\)-edge, and \(a,b\notin T\). Harmless (the length formula holds either way). | Delete or correct. |
| F16 | note | **open** | T2 (iv) header | Italic header still reads "Even lengths cost \(2\rho\)"; the body now proves \(2\rho+2\), which is what (v) consumes. | Cosmetic. |
| F1 | critical | **resolved in rev 2/3** | T2 (v) | The hole was not proved to open: \(ab\) was chosen to maximise \(\rho\), which is orthogonal to \(\min S=g-1\). | Now choice 1 puts \(ab\) on a shortest cycle and \(\min S=g-1\) is *proved* (\(\ge\) from (iii); \(\le\) because the girth cycle's vertices are within \(g/2-1<\rho\) of \(\{a,b\}\), so it avoids \(v\)). I re-derived both directions: correct. |
| F2 | critical | **resolved in rev 3** | T2 (v) numerics | "diameter \(\ge5\Rightarrow\rho\ge5\)" (false: \(\rho\le\mathrm{diam}-1\)) and "\(2\rho\ge g+1\)" from \(\rho\ge(g-1)/2\) (false: gives \(2\rho\ge g-1\)). | Both gone; the parity bound \(\rho\le\mathrm{diam}-1\) is now proved in (v) in the form I gave. Residue is F11. |
| F4 | major | **resolved in rev 3** | T1 diagnosis; Salvageable 1; T4 move 4 | "a profile pair with \(\min S\ge9\) needs … girth \(\ge10\), hence order \(\ge70\)" and "none can exist below order 70" were **false**; the audit's counterexample has girth 3 and order 30. | T1 now carries the order-30 and order-59 witnesses; the scope note is corrected to "not asymptotic"; T4 move 4 is answered. Verified: see the counterexample audit. |
| F5 | minor | **resolved in rev 3** | T2 (iv) vs. boxed claim | Claim used \(2\rho+2\), proof used \(2\rho\). | (iv) now proves \(|Q|=|\mathrm{seg}_a|+1+|\mathrm{seg}_b|\ge2\rho+1\), even \(\Rightarrow\ge2\rho+2\). Correct, and tight on `E030`'s instance (smallest even length 14 \(=2\rho+2\)). |
| F6 | minor | **resolved in rev 3** | T3(b) | Unstated side conditions. | \(2^j\ge c+2\) now in the display; uniqueness now carries \(2^{j-1}\ge c+2\) (equivalently \(c\le2^{j-1}-2\)) — I re-derived it, correct; \(c\) declared integer, which the Mersenne step needs. |
| F7 | minor | **resolved in rev 3** | T1 diagnosis | The shape-A′ cap is `C047`(a), not `C046`(b), and those rows carry \(\ge4\) degree-2 vertices. | Corrected, and the inference weakened. |
| F8 | minor | **resolved in rev 3** | T2 (i)/(ii) | Case split omitted a single cut vertex; \(E(\tilde F)\subseteq E(F_1)\) is false; \(\ell-k\ge3\) tacit. | All three addressed. |
| F9 | note | accepted | T3(b) closing | \(\max S<2\min S+O(1)\) is about the case-(5b) residual object; `L031`/`L032`'s \(s_{\max}\le2s_{\min}\) is about a power-free 2-connected **core**. Different objects; stays analysis. | — |
| F10 | note | — | T1 | T1 survived every attack attempted here; no proved row is contradicted by T1 or T2, and (INT) is cited by no proved row. | — |

### Answers to the five questions

1. **Yes.** Every hypothesis of (INT) as recorded in `C050` is met by both the
   `L053` object and the order-30 object, and nothing was dropped in the
   quotation — I checked specifically for an implicit power-freeness or
   \(C_{16}\)-freeness hypothesis, which would have made T1 a scope overrun.
   There is none.
2. **Inside scope.** `L053`'s row records the ambient \(F\) (cubic,
   3-edge-connected, girth \(\ge17\)), so T1's use of \(F\) rather than \(H\)
   is licensed. The order-30/59 witnesses use no import at all.
3. **(i) yes, including the degenerate branch and (rev 3) the single cut
   vertex. The \(k\in\{0,1,2\}\) bookkeeping is exhaustive** (a path meets a
   triangle in a subpath; \(a,b\notin T\)). **The thresholds are still not
   fully consistent: the hole does not provably open**, because the vertex
   \(v\) that (v) requires is not shown to exist from the stated hypothesis
   (F11).
4. **Valid, and correctly labelled conditional.** I re-derived every step
   including the two side conditions and the Mersenne tightening.
5. **Yes, and in both directions.** T2 is still stated at greater strength
   than proved (F11, F3′). T1 previously *understated*: (INT) fails at order
   30, inside the window — now corrected. **No floor moves and no status
   changes**: both T1 witnesses contain \(C_{16}\) (verified:
   \(\mathrm{Spec}(P^{\ast}-ab)=\{3\}\cup[10,27]\)) and are far from
   power-free; nothing here bears on statement 0.1.

## Statement correspondence

- **(INT) as citable** (`C050`, `tested`): "for a vertex-taut
  \(\{C_4,C_8\}\)-free exactly-two-profile pair,
  \(S(H,a,b)\supseteq[8,\max S]\)". `A029`'s Notation defines *profile pair*
  identically. No power-freeness, no \(C_{16}\)-freeness, no 2-connectivity,
  no order bound. **The quotation is faithful.**
- **Order-30 witness against those hypotheses, one at a time.** \(P^{\ast}\) =
  truncated Petersen; \(H=P^{\ast}-ab\) for a link edge \(ab\). Profile pair ✓
  (degree multiset \(2^23^{28}\)); \(\{C_4,C_8\}\)-free ✓
  (\(\mathrm{Spec}(H)=\{3\}\cup[10,27]\)); vertex-taut ✓ (2-connected, and
  verified directly: all 30 vertices lie on an \(a\)–\(b\) path);
  \(S=[9,26]\) ✓. Hence \(8\in[8,\max S]\setminus S\).
- **Order-59 witness.** Two copies glued at a terminal: profile pair ✓
  (\(2^23^{56}4^1\)), \(\{C_4,C_8\}\)-free ✓ (no cycle crosses a cut vertex),
  vertex-taut ✓ (concatenate block through-paths), \(S=S(H)+S(H)=[18,52]\) ✓
  by Minkowski additivity (`L035`(a)/`L032`). Hence \(14\notin S\),
  \(\max S\ge14\). **Not 2-connected** (F17).
- **T2's object** meets the profile/\(\{C_4,C_8\}\)/tautness/non-bipartite
  hypotheses; what is not established is the property that makes it a
  refutation — the existence of the ambient \(v\) at distance \(\ge g/2\).

## Dependency and circularity audit

Claims checked at recorded strength: `L053`, `L050`/`L049`, `L035`(a)/T2,
`L042`, `L048`(iii), `L031`/`L032`, `L046`, `C043`, `C046`, `C047`, `C049`,
`C050`.

- **No circularity.** T1 (current form) depends on nothing but the explicit
  graphs; its asymptotic form depends on `L053`+`X002`/`X003`. T2 depends on
  `X004` alone. T3(b) depends on `L042` plus the hypothetical lemma.
- **No proved row is contradicted.** I searched `CLAIMS.md` for every mention
  of (INT): it appears only in `C050` (a `tested` row recording a *survived
  kill test*) and in the dependency note, which already forbids citing it as
  support for any proved row. `C050`'s 24/24 and `C046`/`C047`'s censuses run
  to order \(\le21\) and are untouched by objects of order 30 and 59; the
  order-30 object is not power-free, so no floor moves.
- **Citation strength.** `X004` is used for an existence claim in a negative
  result — right discipline — but the row's sourcing no longer covers the
  statement it makes (F3′).

## Edge-case and counterexample audit

**Against T1 — attacks tried, all failed.** Looked for an (INT) hypothesis the
object fails (none); checked \(S\ne\emptyset\); checked the degenerate length-1
path (excluded, \(ab\notin E(H)\)); checked whether the refutation secretly
needs \(F\) non-Hamiltonian (it does not — strictly less than `L053` records);
checked whether \(P^{\ast}\) might be \(C_{16}\)-free, which would have made it
a class member rather than a calibration object (it is not: \(16\in
\mathrm{Spec}\)).

**Against the rev-1 diagnosis — attack succeeded (F4).** Constructed the
counterexample now adopted into T1: cycles of a truncation project to Petersen
cycles of length \(\ell\ge5\) and have length in \([2\ell,3\ell]\), so
\(\mathrm{Spec}(P^{\ast})\cap[4,9]=\emptyset\) and the shortest cycle through a
link edge is \(2\cdot5=10\). Measured independently (my own code) and then
reproduced by `E030/truncation.py`: order 30, 45 edges, cubic, 3-connected
(all 435 pairs), \(\mathrm{Spec}\cap[3,13]=\{3,10,11,12,13\}\); after deleting
a link edge, degree multiset \(2^23^{28}\), 2-connected, vertex-taut, 8,576
\(a\)–\(b\) paths, \(S=[9,26]\).

**Against T2 — the surviving attack (F11).** Three facts, all checkable:

1. \(d_{F_1}(x,T)=d_{\tilde F}(x,v)\), so
   \(\rho=\min(d(a,v),d(b,v))\).
2. \(\tilde F\) bipartite and \(ab\in E\) force \(d(a,v)\) and \(d(b,v)\) to
   differ by exactly 1, so \(\rho\le\mathrm{diam}(\tilde F)-1\). *(Now proved
   in the attempt; measured \(\rho_{\max}=\mathrm{diam}-1\) in 13 of 13
   bipartite cubic 3-connected test graphs.)*
3. What (v) needs is \(\mathrm{ecc}(\{a,b\})\ge g/2\) for the **pre-chosen**
   \(ab\). A diameter bound gives only \(\mathrm{ecc}(\{a,b\})\ge
   (\mathrm{diam}-1)/2\).

Failure scenario for the argument as written: any \(\tilde F\) with
\(\mathrm{diam}=g/2+1\) in which the chosen shortest-cycle edge is central —
the hypothesis holds, the required \(v\) is not produced by it, and every
claimed hole position lies at or below the smallest even through-length. The
conclusion is rescued only by the counting argument of the required
resolution, which is not in the record. (For \(g=10\) the rescue is free:
\(2^{g/2+1}-2=62\) and every bipartite cubic graph of girth 10 has \(\ge70\)
vertices, so \(\rho\ge5\) is automatic and the pivot-trigger form of T2 needs
**no** diameter hypothesis at all. For \(g=12\) the rescue fails exactly at
the Tutte 12-cage, \(N=126=2^{7}-2\) — consistent with its withdrawal.)

**Mechanism tests of T2 run here** (girth 6–8, so below T2's \(g\ge10\): these
test the bookkeeping, not the statement). The rev-1 recipe was run verbatim on
six named bipartite cubic 3-connected graphs and seven seeded random ones. It
produced **no hole at all** on the two cages — Heawood ((3,6)-cage,
\(\mathrm{diam}=3=g/2\)) and Tutte–Coxeter ((3,8)-cage,
\(\mathrm{diam}=4=g/2\)) — and produced exactly
\(\{h\ \mathrm{even}:\min S<h<2\rho+2\}\) on the four non-cages
(Möbius–Kantor \(\{6\}\), Pappus \(\{6\}\), Desargues \(\{6,8\}\), Dyck
\(\{6,8\}\)). This confirms the sharpened \(2\rho+2\) bound of rev 3 (11/11
instances) and confirms that cages are the failing family.

**Vacuity checks.** T2 correctly produces nothing at the orders of the eight
profile objects. T3(b) correctly fails on them (\(14\in S\)).

## Imported theorem and computation audit

- **`X002`/`X003` via `L053`.** Hypotheses matched; T1's asymptotic form uses
  strictly less than the row records. No finding.
- **`X004`.** Statement now decoupled, which is what T2 consumes — but the
  3-connectivity of the decoupled family is sourced to cages, and cages are
  withdrawn in the same revision (F3′). The "Hypothesis match" paragraph
  repeats the F11 non sequitur ("a vertex at distance \(\rho\ge g/2\) …, i.e.
  \(\mathrm{diam}\ge g/2+1\)"): that is a *necessary*, not a sufficient,
  condition.
- **`E030`, re-run.** `python3 check.py` reproduces its recorded output
  exactly (base \(H(52;\{0,1,5\})\): \(N=104\), girth 6, diameter 12,
  3-connected; \(F_1\) order 106; \(\min S=5=g-1\); parity law 0 violations;
  smallest even through-length 14; holes 6, 8, 10, 12 with an extra odd hole
  at 7). I rebuilt the base graph independently and confirmed order,
  cubicity, bipartiteness, girth 6, diameter 12, 3-connectivity, and
  \(\rho_{\max}=11\). Two audit remarks: (a) the instance's diameter (12) is
  double what the order threshold forces, and its \(v\) was found by **direct
  search** over 54 candidates — so `E030` does **not** exercise the inference
  F11 attacks, and the README's "the `X004` import is the only part of T2
  this experiment does not exercise" is one item short; (b) `python3
  truncation.py` reproduces the order-30 witness independently of my code
  (its "cycle lengths <13" label is off by one — the list it prints includes
  13; my independent enumeration agrees with the list, not the label).
- **This review's own computations.** Written from scratch in a scratchpad,
  no code read from `experiments/` before the first verdict, CPython, exact
  integer arithmetic, no floating point; one seeded generator
  (`random.seed`) used only for the mechanism stress test. All searches are
  exhaustive over the stated finite objects: 3-connectivity by deleting every
  vertex pair, spectra by exhaustive DFS, through-sets by exhaustive path
  enumeration. Named LCF graphs were reconstructed and then *verified* to have
  the girth, diameter, bipartiteness and connectivity attributed to them, so a
  mis-remembered LCF could only have changed which graph was tested.

## Resolution audit

Resolved and re-verified by me: F1, F2, F4, F5, F6, F7, F8 (each repair
re-derived independently, not accepted on the author's report).

Open and blocking `L057`: **F11**, **F3′**. Open and non-blocking: F12, F13,
F17; notes F14, F15, F16, F9.

`L056` may be promoted once F17's adjective is split. `L057` should not be
promoted, and "the recorded pivot trigger fires" should not enter any ledger,
until F11 and F3′ are closed.

## Independence note

Read before the first verdict, in this order and nothing else: `STATEMENT.md`;
this record's Target identification and Questions; `A029` (rev 1) in full;
`CLAIMS.md` rows `L031`, `L032`, `L035`, `L042`, `L046`, `L048`, `L049`,
`L050`, `L053`, `L054`, `L055`, `C043`, `C044`, `C046`, `C047`, `C049`,
`C050`, plus the dependency notes; both files in `references/`;
`process/review-playbook.md`; `templates/review.md`.

Not read at any point: `sessions/`, `PROOF.md`, `STATE.md`, `problem.json`,
`LOG.md`, `DECISIONS.md`, earlier reviews, and every attempt other than
`A029`. `A029` T5 is outside the scope fixed in Target identification and was
not audited; nothing in T1/T2/T3(b) depends on it (T1's aside "inside the
case-(5b) window \([22,40]\) of T5" is decoration — the order-30 witness is
inside the recorded window \([18,35]\) independently of T5).

**Exceptions taken, recorded explicitly.** (a) After the first verdict was
written, the coordinator reported two in-place corrections to `A029` and a new
experiment; I then read `A029` rev 2 and rev 3, `E030/README.md`,
`E030/check.py`'s output, `E030/truncation.py`, the rewritten `X004`, and the
attempt's own response-to-review section, and re-audited. The response section
was read only to check whether any finding was reported resolved that is not;
none was — the attempt states plainly that the T2 repair is un-re-audited. All
"resolved" marks above are mine, from re-deriving the repaired step. (b) The
audit target changed twice under review, so this record is not a review of a
frozen artefact; the Revision tracking section states exactly which text each
severity applies to.

No discovery narrative was supplied beyond the slug, the record path, the
review type, and the list of records to consult. All computations are the
reviewer's own; the order-30 and order-59 witnesses now in T1 were produced by
this audit, which is why F4 is marked resolved in the target rather than
outstanding.

---

## Second round (the reviewer re-audited the repairs)

The audit was resumed against the revised attempt. Steps (i)–(iv) of T2 and
all of T1 and T3(b) were re-derived and confirmed; the \(2\rho+2\) bound was
measured tight in 11 of 11 computed instances. Two **new major** findings, and
three minor, were raised against the repairs themselves:

| Finding | Severity | Status | Resolution |
|---|---|---|---|
| F11 | major | **resolved** | Deriving \(\rho\) from the diameter is a non sequitur once \(ab\) is fixed: what the construction consumes is the eccentricity of a *pre-chosen edge*, and \(\mathrm{diam}=D\) gives only \(\mathrm{ecc}(\{a,b\})\ge(D-1)/2\). Repaired with the reviewer's own suggestion: hypothesise the **order** and use the tree ball bound \(\lvert B(\{a,b\},r-1)\rvert\le2^{\,r+1}-2\). Diameter is now absent from the argument and from `X004`. At \(g=10\), \(r=g/2\) the bound reads \(N>62\), automatic for a girth-10 cubic graph. |
| F3′ | major | **OPEN** | `X004` now asserts 3-connectivity in a regime it does not source: Erdős–Sachs and the bipartite double cover supply none, and cages — its only previous support — were withdrawn in the same revision. Recorded as a boxed unresolved finding in the reference file. **`L057` is not established**, stays at `proposed`, and may not be cited. |
| F17 | minor | **resolved** | T1's boxed claim let "2-connected" scope over the order-59 chain, which has a cut vertex. Reworded: the chain is vertex-taut but not 2-connected, and (INT) requires only vertex-tautness. |
| F12 | minor | **resolved** | The \(T\)-meeting path was justified by "\(v\) is not a cut vertex", which does not produce a path *through* \(v\). Replaced by the already-proved vertex-tautness of \(H\). |
| F13 | minor | **resolved** | "\(\rho\to\infty\) from \(\mathrm{diam}\to\infty\)" was asserted. The order/ball bound of F11's repair supplies \(\rho\ge r\) directly. |
| — | note | **resolved** | `E030`'s README labelled the truncation scan "cycle lengths \(<13\)"; the enumeration reaches 13. Relabelled, and it is recorded that there is no 13-cycle. |

**Net standing.** `L056` — **proved and audited**, and materially strengthened
by the audit (order-30 and order-59 witnesses, in-window, no imports).
`L058` — proved in the `L046` frame. `L057` — **not established**, blocked on
F3′. The interpolation-genre conclusion rests on `L056` plus the bipartite
one-liner and does **not** depend on `L057`; the non-bipartite relativized
kill is the part that remains open.
