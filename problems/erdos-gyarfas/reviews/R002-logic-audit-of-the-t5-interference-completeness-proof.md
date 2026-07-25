# R002 — Logic and dependency audit of the T5 interference-completeness proof

- Date: 2026-07-25
- Problem: `P-002`
- Reviewed statement version: 0.1 (main statement unchanged; the review
  target is the lemma-level result offered as `L049`/`L050`, i.e.
  deductions T1–T6 in
  `attempts/A024-proof-of-t5-vertex-taut-implies-interference-complete-via-th.md`)
- Reviewed proof revision: A024 as of session `S023`, before ledger
  promotion (CLAIMS/PROOF rows for T5 do not exist yet; the ledger
  promotion is gated on this review)
- Review type: logic — logic / hypotheses / counterexample / computation / exposition
- Independence mode: delegated-subagent
- Note: created manually because `proofctl.py review` gates on a
  main-statement proof candidate; this is a lemma audit and the main
  claim status is unchanged (`open`). Same exception as `R001`.
- Target identification (read this, then the target, then write the
  verdict): the claims under audit are, verbatim from A024 —
  **T1** (tautness forces the block chain, with splice), **T2** (fan
  corollary via imported Menger k=2), **T3** (subdivision preserves
  2-connectivity), **T4** (Lemma A: in a vertex-taut pair every edge
  on a cycle lies on a simple a–b path), **T5** (the theorem: in a
  vertex-taut pair every cycle is the edge symmetric difference of two
  distinct simple a–b paths, with the trunk-identical arc form and
  prescribed-edge freedom), **T6(a)–(c)** (corollaries: 2-connected
  all-pairs completeness; the min-degree-2 tautness biconditional;
  the unconditional case-(5b) spectrum identity via `L048`).
  The imported classical statements are in
  `references/textbook-classics-2026-07-25.md`. The mechanical
  instance verification lives in `experiments/E023-.../rungs.py`
  (`constructive` commands) with data in `E023/data/`; re-running it
  is permitted as part of this audit. Definitions (interference cycle,
  vertex-taut) must be checked against their recorded census semantics
  (`CLAIMS.md` rows `C041`/`C042`/`L048`; `E013`/`E021` predicate).

## Verdict

**PASS at lemma level.** T1, T2, T3, T4, and T5 are proved as stated,
at the stated generality: for every finite simple graph \(H\) and every
pair \(a\ne b\) with \((H,a,b)\) vertex-taut in the recorded census
sense, every cycle \(C\) of \(H\) is the edge symmetric difference of
two **distinct** simple \(a\)–\(b\) paths, with the trunk-identical arc
form and the prescribed-edge freedom as stated — no connectivity,
degree, or freeness side condition is consumed (connectivity is
*derived* from tautness in T1). T6(a) and T6(c) are correct
corollaries at their recorded citation strengths. T6(b) (offered
`L050`) is mathematically correct but carries the one real defect
found: a formally circular citation of T1(5) inside the converse
remark (finding F1, minor — the splice proof never uses tautness, so
the repair is a rescoping restatement, not new mathematics).

**No critical or major findings. Two minor findings (F1, F2) and six
notes.** Ledger promotion of `L049`/`L050` and the `L048`(iii) upgrade
can proceed once F1 and F2 are repaired as described in the table; no
new obligation is required if they are repaired at promotion time.

What was actively attacked and did not break:

- **Negation search.** I attempted to build a vertex-taut pair with a
  non-decomposable cycle at every structural corner the proof turns
  on: cycles in middle blocks of long chains, cycles through one/both
  terminals, cycles sharing long runs of edges with the witness path
  \(R\) (the weaving regime the discarded middle absorbs), \(K_2\)
  blocks at the ends, terminals adjacent to the cycle, triangle
  cycles with adjacent \(u,v\). Every such configuration is handled
  by the written argument, and an exhaustive independent search (own
  code, below) over **all labelled graphs on \(\le6\) vertices** and
  all ten named frontier objects found zero failures of T5, of Lemma
  A, or of the T6(b) biconditional.
- **Case-split exhaustiveness.** T1's leaf-off-path argument, T6(b)'s
  leaf-block case analysis (including \(a\) or \(b\) being a cut
  vertex in the non-taut branch, \(\ge3\)-leaf trees, and the
  same-end-block configuration, which is redundant under the
  "otherwise" hypothesis but disposed of correctly anyway) were
  expanded case by case; all exhaustive.
- **Hidden hypotheses.** Checked for silent nonemptiness,
  connectedness, \(a\ne b\), and simplicity assumptions; the only
  convention doing work is \(a\ne b\), which is definitional in the
  recorded census predicate (F6, note).
- **Computation.** Every recorded `E023` command was re-run with all
  writes redirected outside the repository: every aggregate
  reproduces exactly (details in the computation audit section).

## Findings

| Finding | Severity | Location | Issue | Required resolution | Obligation |
|---|---|---|---|---|---|
| F1 | minor | A024 T1 remark (converse), consumed by T6(b)/`L050` | The remark derives tautness for a block chain "by (5)", but T1(5) as stated sits under T1's ambient hypothesis "(H,a,b) vertex-taut" — a formally circular citation when used to *derive* tautness. Substantively non-circular: the proof of (5) uses only chain properties (1)–(3) plus B1 (edge-disjointness of blocks), never tautness; in T6(b)'s application the chain properties hold by construction (T a path + B1/B2). | Restate the splice as a standalone lemma about chain-decomposed graphs (hypothesis: the blocks form a chain with \(a,b\) placed as in (3)); cite that in the remark and T6(b). No proof text changes. Repair before promoting `L050`. | none if repaired at promotion |
| F2 | minor | A024 T7, kill-rung bullet | Lists "the dense completion of order 8" among the spent rungs T5 survived; `E023`'s README records `n8_dense` as **running at write-up and not citable**, and no `tautslice_n8_dense` data file exists. An unfinished background job's results are claimed in the attempt narrative (not load-bearing for the proof — the sparse order-8 slice and everything else cited is on disk and reproduced). | Strike the mention or harvest the landed run before ledger promotion; keep the dense row out of `C044` unless landed. | none if repaired at promotion |
| F3 | note | A024 T1, second proof paragraph | The two-component dichotomy ("suppose \(a,b\) lie in one component of \(H-x\) … so they lie in different components") is well-typed only for cut vertices \(x\notin\{a,b\}\). Paragraph 3 (whose proof is independent of paragraph 2) shows \(a,b\) are not cut vertices, and every later use of the dichotomy is for a cut vertex, so the logic closes; the scope should be stated or the paragraphs swapped. | One clause or a swap. | — |
| F4 | note | A024 T3 | The connectivity case list checks \(r=m\), \(r=p\), \(r\notin\{m,p,q\}\); \(r=q\) is omitted (symmetric to \(r=p\) under \(p\leftrightarrow q\)). | Add "symmetrically \(r=q\)". | — |
| F5 | note | A024 T6(a) | "vertex-taut (T2 fan through any \(w\))" silently includes \(w\in\{a,b\}\), where T2 (three *distinct* vertices) does not apply; that corner is trivial (\(a,b\) lie on any \(a\)–\(b\) path, which exists by connectivity). | One clause. | — |
| F6 | note | A024 entry assumptions / offered `L049` row | \(a\ne b\) is definitional in the census predicate (`E018/mod4.py paths_with_essential` asserts `a != b`; verified in code). The ledger statement of `L049` should carry \(a\ne b\) explicitly rather than by convention. | Copy the convention into the row text. | — |
| F7 | note | A024 T6(c), final sentences | The set identity \(\mathrm{Spec}(H)=\{x+y-2s:\text{realized trunk-split pairs}\}\) needs "trunk-split pair" to mean the full Moreover-form of T5 — in particular \(V(A_1)\cap V(A_2)=\{u,v\}\) — for the \(\supseteq\) direction (a loose shared-prefix/suffix pair can have a symmetric difference that is a union of \(\ge2\) cycles). Determinate as written because the term is defined in T5's statement; spell it out in the `L048`(iii) upgrade note. | Define "trunk-split" in the upgrade note. | — |
| F8 | note | `references/textbook-classics-2026-07-25.md` | T1 also uses "every vertex of a connected graph on \(\ge2\) vertices lies in a block" and "distinct blocks are edge-disjoint"; both are immediate from the recorded block definition and B1 (an edge has two endpoints) but are not itemized in B1–B3. | Half a sentence in the reference note or inline. | — |

## Statement correspondence

**T5 concludes exactly the target claim.** Quantifier order as
required: for every finite simple \(H\), every pair \(a\ne b\), if
\((H,a,b)\) is vertex-taut then for every cycle \(C\) (and moreover
for every prescribed edge \(pq\in E(C)\)) there exist two distinct
simple \(a\)–\(b\) paths \(P,Q\) with
\(E(P)\,\triangle\,E(Q)=E(C)\), in trunk-identical arc form with
\(pq\in E(P)\cup E(Q)\). The witnesses depend on \(C\) (and \(pq\)),
as they must. Distinctness is proved via \(E(A_1)\ne E(A_2)\), both
arcs nonempty — valid because a cycle has \(\ge3\) edges and
\(u\ne v\) is *proved* (positions of \(p\ne q\) separate the first and
last hits), not assumed. Exactness of the symmetric difference is a
disjoint-union computation whose three disjointness inputs
(\(V(T_a)\cap V(C)=\{u\}\), \(V(T_b)\cap V(C)=\{v\}\),
\(V(T_a)\cap V(T_b)=\emptyset\)) each follow from the first/last-hit
choice on the simple path \(R\); I verified each inclusion by hand and
mechanically (below). **No side conditions:** connectivity is derived
inside T1 from tautness; no degree, \(C_4\)-freeness, power-freeness,
or order hypothesis appears anywhere in T1–T5. Boundary cases checked
by hand: \(H=K_2\) (taut, no cycles, T5 vacuous), \(H\) a single
cycle containing \(a,b\), \(a\) and/or \(b\) on \(C\) (trivial
trunks; \(P,Q\) = the two arcs — consistent with `L048`(ii)), \(k=1\)
vs \(k>1\) chains, \(u,v\) adjacent on \(C\) (arc sizes 1 and
\(\ge2\)).

**Definitions match the recorded census semantics exactly** (verified
in the code, not just the prose): `E013/catalogue.py all_ab_paths`
returns each simple \(a\)–\(b\) path once as an edge frozenset;
`E021/dissect.py dissect_pair` declares a cycle decomposable iff some
pair from `itertools.combinations(paths, 2)` has
`e1 ^ e2 == edges` — i.e. two distinct simple \(a\)–\(b\) paths,
distinct as edge sets, symmetric difference exactly the cycle's edge
set — which is A024's definition verbatim (a simple \(a\)–\(b\) path
in a simple graph is determined by its edge set, so path-distinctness
and edge-set-distinctness coincide; a path and its reversal are the
same edge set and can never witness a nonempty difference).
`E018/mod4.py paths_with_essential` computes the union of vertex sets
over all simple \(a\)–\(b\) paths and asserts \(a\ne b\); tautness =
full mask, matching "every vertex of \(H\) lies on at least one
simple \(a\)–\(b\) path" (F6: make \(a\ne b\) explicit in the ledger
row). `all_cycles` enumerates each simple cycle of length \(\ge3\)
once, matching `D003`.

**T1–T4, T6 each conclude their stated claims.** T1's chain
properties (1)–(5) are all proved (F3 ordering note); the remark is
correct with F1's rescoping. T2 is the classical fan lemma, derived
from the imported Menger \(k=2\) applied to \(G+z\) (apex
2-connectivity checked inline; \(|V|\ge4\); \(w\ne z\); the
both-via-\(s\) case correctly excluded as a shared internal vertex;
\(w\notin\{s,t\}\) guarantees neither path is a single edge to
\(z\)). T3 is complete modulo the symmetric \(r=q\) case (F4). T4
applies B3 + T1 + T3 + T2 with all three T2 vertices distinct
(\(m\) is new; \(c_{i-1}\ne c_i\) from T1) and the contraction of
\(m\) is legitimate because \(m\)'s only neighbours are \(p,q\) and
\(pq\notin E(B_i')\). T6(a): correct (F5 corner). T6(b): the case
analysis is exhaustive — 2-connected (contradiction via T2); some
leaf block interior missing both terminals (explicit non-interference
cycle via the leaf block being 2-connected under \(\delta\ge2\) —
the \(K_2\) leaf is correctly killed by a degree-1 vertex — plus
`L048`(i)); otherwise \(\le2\) leaves force a path, and the only
surviving placement is T1(3)'s chain, taut by the (repaired) remark.
The \(\delta\ge2\) hypothesis is doing real, necessary work (a
pendant tree off a taut core is non-taut yet interference-complete —
checked by hand), and the claimed scope covers `C042`'s profile class
(connected, \(\delta\ge2\)) as asserted. T6(c): a pure corollary
chain — case-(5b) tautness is definitional (`L041`/`L042` case
description), T5 discharges `L048`(iii)'s completeness hypothesis,
and the identities quoted are `L048`(ii)/(iii) verbatim (F7 note on
"trunk-split").

## Dependency audit

Dependency graph (arrows = "used by"), verified acyclic:

- B1, B2 → T1; Menger(k=2, forward) → T2; T3 self-contained;
- B3, T1, T2, T3 → T4; T4 + T1(5) → T5;
- T2, T5 → T6(a); T2, T5, T1-remark, `L048`(i), B2 → T6(b);
- `L042`-tautness (definitional for case (5b)), T5, `L048`(ii)/(iii)
  → T6(c).

**No dependency on T5's own conclusion anywhere upstream of T5.**
T6(b) uses T5 only for the ⟸ direction; the ⟹ direction uses
`L048`(i) and block structure only — not circular. The single
citation-hygiene defect is F1 (T1(5) cited under a hypothesis being
derived); it is severed by restating the splice under chain
hypotheses, which is what its written proof already assumes and uses.

**Imported claims cited at recorded strength.** `L048` is a proved
CLAIMS row whose clause (iii) is explicitly conditional on
interference-completeness ("a hypothesis here"); T6(c) consumes it
exactly as a conditional discharged by T5 — no strength inflation.
`L048`'s own support (`A021` T1, `A019` W1-T1(1)) is independent of
A024, so no cycle through `L048`. `C041`/`C042` are cited
descriptively only (calibration, evidence), never as premises. `A023`
T5 (the labelled conjecture) is the *target*, never a premise.

**External imports.** Menger \(k=2\)/Whitney: the reference note
states the precise global vertex form with \(|V|\ge3\), and A024 uses
only the forward direction on \(G+z\) — hypotheses matched one by one
(2-connectivity of \(G+z\) proved inline; \(\ge4\) vertices;
\(w\ne z\) distinct). B1–B3: stated in the note with standard
sources; each use in T1/T4/T6(b) is within the stated content
(shared-vertex bound, tree structure + leaves are blocks + component
correspondence under cut-vertex deletion, cycles inside one
2-connected block). Two standard block facts used but not itemized
(F8): "every vertex of a connected \(\ge2\)-vertex graph lies in a
block" and "distinct blocks are edge-disjoint"; both immediate from
the note's own definitions (maximality; B1 + an edge has two
endpoints). No research-strength external import anywhere.

**Case splits.** T1's exactly-two-components argument, the
leaf-off-\(\Pi\) extraction (a node off the path forces a *leaf* off
the path; leaf = block by B2), and T6(b)'s four-way analysis were
each expanded and found exhaustive; the same-end-block sub-case of
T6(b) is unreachable under its "otherwise" hypothesis but is disposed
of correctly anyway (harmless redundancy, no finding).

## Computation audit (permitted by the target identification)

All re-runs were executed through a reviewer wrapper that redirects
every data write to the reviewer scratchpad; the repository tree was
not modified. Toolchain: PyPy 7.3.23 (Python 3.11.15), CPython
3.14.2, nauty geng 2.9301 — matching the recorded environment.
Deterministic integer/set arithmetic throughout; no floating point,
no seeds; geng streams pinned by the recorded switch sets
(`geng_args(13)` = `-q -c -f -d2 13 19:78`, verified in source).

1. **Recorded commands re-run, exact agreement on every aggregate**
   (timing fields aside): `anchors` 45/45 under both interpreters;
   `tautcal` reproduces `E021`'s four recorded aggregate keys
   exactly; `smallworld13` (class 10,966; taut 10,853; 1,614,300 taut
   cycles, 0 non-decomposable; 113/113 non-taut members fail);
   all five `tautslice` rows (n8 8:12, n9 9:13, n9 14:14, n10 10:13,
   n11 11:13) identical to the recorded JSONs; `constructive general
   4 5 6 7` (12,313 taut pairs / 723,926 cycle instances / 3,727,132
   edge instances, all pass); `constructive slice` n8 and n9
   (2,008,186 and 11,577,122 edge instances, all pass);
   `constructive named` — all ten objects, per-object cycle and
   edge-instance counts identical, including 411 at order 19 and the
   seven order-20 profile members totalling 4,250 (66,038 profile
   edge instances).
2. **Independent reproduction with reviewer-written code** (own g6
   parser, own DFS path/cycle enumeration, own tautness computation,
   brute-force pair search; no geng, no candidate primitives):
   - T5 statement + Lemma A over **all labelled graphs** on 4, 5, 6
     vertices (strictly wider than the iso-free streams): 84 / 3,220
     / 210,600 taut pairs, 192 / 18,620 / 3,190,440 cycle instances —
     zero failures;
   - the T6(b) biconditional over all labelled *connected*
     \(\delta\ge2\) graphs on 4–6 vertices: 183,460 pairs, 6,480
     non-taut — taut ⟺ complete holds with **zero exceptions in both
     directions**;
   - all ten named objects re-verified independently: Petersen\(-e\)
     rebuilt from the reviewer's own Petersen construction (edge
     (0,1) removed; edge-transitivity makes the isomorphism type
     unique), 29 cycles, 0 non-decomposable; the order-14 exemplar
     (64 cycles), the order-19 exemplar (398 paths — the recorded
     through-path count — 411 cycles), and all seven order-20 profile
     members (766/774/350/572/648/648/492 cycles): all terminals
     recomputed from the degree profile agree with the recorded
     pairs, and **zero non-decomposable cycles anywhere**.
3. **Search completeness / scope discipline:** the E023 scope
   statements are correctly narrow (exhaustive only for the delimited
   classes; "a pass does not prove T5"); the one overclaim is A024
   T7's mention of the unlanded order-8 dense completion (F2). The
   cross-reference "10,966 = the `A021` count" was not verified
   against `A021` (isolation); the number itself is reproduced
   directly from the generator stream, so nothing load-bearing rests
   on the cross-reference.

## Independence note

Read, in order, before writing the verdict: `STATEMENT.md`; this
review record's header and target identification; `PROOF.md`;
`CLAIMS.md` (header rows plus the targeted rows `C040`–`C043`,
`L048`, located by search); `OBLIGATIONS.md` rows `G013`/`G015`;
the identified target `attempts/A024-...` (the candidate under
review, named by the target identification — the **only** file under
`attempts/` read); `references/textbook-classics-2026-07-25.md`;
`E023` README, `rungs.py`, and all recorded `E023/data` JSONs; the
imported primitive sources `E021/dissect.py` (predicate,
`dissect_pair`, `cmd_smallworld`), `E018/scan.py` and `mod4.py`
(tautness/profile instruments), `E013/catalogue.py` (path/cycle
enumerators); `process/review-playbook.md`. Exception recorded: the
candidate lives in an attempt record rather than `PROOF.md`, so
reading `attempts/A024` was required and was directed by the review
record itself. No other `attempts/`, no `sessions/`, and no earlier
`reviews/` content was read before this verdict was written; in
particular `A021`'s order-13 count and `A023`'s original conjecture
record were **not** consulted (the target identification quotes T5
verbatim). The invoking prompt contained only the problem slug, the
record path, the review type, and the start instruction — no
discovery narrative; no contamination to report. All computations
above were re-run and independently re-implemented by this reviewer
in a scratchpad outside the repository; no canonical record other
than this review file was modified.
