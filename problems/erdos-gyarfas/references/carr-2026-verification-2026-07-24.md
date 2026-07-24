# Line-by-line verification — Carr (2026), "Every Minimal Counterexample to the Erdős–Gyárfás Conjecture is Predominantly Cubic"

- Date of access and verification: 2026-07-24
- Source: A. Carr, *Every Minimal Counterexample to the Erdős–Gyárfás
  Conjecture is Predominantly Cubic*, **arXiv:2605.22844v1 [math.CO]**,
  submitted 13 May 2026 (4 pages, 2 figures; MSC 05C38, 05C35, 05C75).
  Author affiliation as printed: Independent Researcher.
- Text used: the arXiv LaTeXML HTML rendering
  <https://arxiv.org/html/2605.22844v1>, retrieved in full on 2026-07-24; the
  abstract page <https://arxiv.org/abs/2605.22844> was checked separately and
  reports v1 as the only version. Every statement quoted below is transcribed
  from that rendering. No v2 exists as of the access date.
- Scope of this note: complete verification of the exact statements **and the
  complete proofs** of Lemma 0.1, Corollary 0.1 (parts 1 and 2), Corollary 0.2,
  and Theorem 0.1, checked against the paper's own definitions; plus
  statement-correspondence of the dossier rows `C004`, `C005`, `C006` against
  what is actually printed.
- This note discharges the `G014` audit item that gates route `R2` of `G015`.
- Written in session `S019` (worker W2). It creates no claim, changes no
  ledger row, and asserts nothing beyond what is verified here.

## 0. The paper's own definitions (as printed)

Notation section, verbatim:

> All graphs considered in this note are finite, simple, and undirected. Let
> \(G=(V(G),E(G))\) be a graph with vertex set \(V(G)\) and edge set \(E(G)\).
> For a vertex \(v\in V(G)\), the neighborhood of \(v\) is
> \(N(v)=\{u\in V(G):uv\in E(G)\},\) and the degree of \(v\) is
> \(d(v)=|N(v)|.\) The minimum degree of \(G\) is denoted by
> \(\delta(G)=\min\{d(v):v\in V(G)\}.\) A graph \(H\) is a proper subgraph of
> \(G\) if \(H\subsetneq G\). A graph \(G\) is called \(k\)-regular if every
> vertex of \(G\) has degree \(k\). A cubic graph is a \(3\)-regular graph.
>
> In this note, a minimal counterexample to the Erdős–Gyárfás conjecture means
> a graph \(G\) with \(\delta(G)\geq 3\) that contains no cycle whose length is
> a power of \(2\), chosen with minimum possible order and, subject to that,
> minimum possible size.

Three definitional observations, all of which the proofs depend on:

- **D-a (target correspondence).** "contains no cycle whose length is a power
  of \(2\)" and this dossier's "no cycle of length \(2^k\) for an integer
  \(k\ge2\)" (`STATEMENT.md` `D004`) are the same condition: in a finite simple
  undirected graph every cycle has length \(\ge3\), so the powers of two that
  can occur as cycle lengths are exactly \(4,8,16,\dots\). This is precisely
  the remark already recorded in `D004`. **No mismatch.**
- **D-b (minimality order).** "minimum possible order and, subject to that,
  minimum possible size" is exactly the dossier's order-then-size convention.
  **No mismatch.**
- **D-c ("subgraph" is not defined).** The paper defines *proper* subgraph
  (\(H\subsetneq G\)) but never defines *subgraph*. The standard notion —
  \(V(H)\subseteq V(G)\), \(E(H)\subseteq E(G)\), and \(E(H)\) supported on
  \(V(H)\) — is what the proofs actually use, and the only subgraphs they ever
  construct are \(G-v\) (vertex deletion) and \(G-uv\) (edge deletion). This is
  a definitional elision, **not a gap**: every use is instantiated at an
  explicitly constructed subgraph. Under that reading, \(H\subsetneq G\) means
  either \(V(H)\subsetneq V(G)\), or \(V(H)=V(G)\) and \(E(H)\subsetneq E(G)\)
  — the case split used below.
- **D-d (empty subgraph).** \(\delta(H)\) is undefined when \(V(H)=\emptyset\).
  The paper does not exclude the empty subgraph from Lemma 0.1's quantifier.
  This is harmless: the conclusion is only ever applied to nonempty \(H\), and
  the dossier's row `C004` already restricts to "every proper subgraph with
  defined minimum degree", which is the conservative reading.

Throughout, "counterexample" means (paper's usage, consistent with the
dossier): a finite simple undirected graph with \(\delta\ge3\) and no cycle of
length a power of two.

## 1. Lemma 0.1

**Statement as printed.**

> **Lemma 0.1.** Let \(G\) be a minimal counterexample to the Erdős–Gyárfás
> conjecture. Then \(\delta(H)\leq 2\) for every proper subgraph
> \(H\subsetneq G\).

**Proof as printed.**

> Let \(G\) be a minimal counterexample with respect to order and size, and
> suppose \(H\subsetneq G\) is a proper subgraph with \(\delta(H)\geq 3\). By
> minimality of \(G\), the graph \(H\) cannot be a counterexample. Hence, \(H\)
> contains a cycle whose length is a power of \(2\). Since \(H\) is a subgraph
> of \(G\), the same cycle occurs in \(G\), contradicting that \(G\) is a
> counterexample. Therefore, \(\delta(H)\leq 2\) for every proper subgraph
> \(H\subsetneq G\).

**Reconstruction, every nontrivial step checked.**

1. *Existence of a minimal counterexample.* The lemma is conditional on \(G\)
   being one; if no counterexample exists it is vacuous. If some counterexample
   exists, the set of orders of counterexamples is a nonempty set of positive
   integers and has a least element \(n_0\); the set of sizes of order-\(n_0\)
   counterexamples is a nonempty set of nonnegative integers and has a least
   element. So the object is well defined. ✔ (Not spelled out in the paper;
   standard and immediate.)
2. *Assume \(H\subsetneq G\) with \(\delta(H)\ge3\) (so \(V(H)\ne\emptyset\)).*
3. *\(H\) is a counterexample.* \(H\) is finite, simple, undirected (subgraph of
   such). \(\delta(H)\ge3\) by assumption. Every cycle of \(H\) is a cycle of
   \(G\); \(G\) has no cycle of power-of-two length; hence neither does \(H\). ✔
4. *Contradiction with minimality.* Exactly one of the two cases of D-c holds.
   - \(V(H)\subsetneq V(G)\): then \(|V(H)|<|V(G)|\), so \(H\) is a
     counterexample of strictly smaller order — contradicting minimality of the
     order of \(G\). ✔
   - \(V(H)=V(G)\) and \(E(H)\subsetneq E(G)\): then \(|V(H)|=|V(G)|\), which is
     the minimum order, and \(|E(H)|<|E(G)|\), so \(H\) is a counterexample of
     the minimum order with strictly smaller size — contradicting minimality of
     the size of \(G\) subject to minimum order. ✔
5. The printed proof routes the same contradiction differently: it deduces from
   minimality that \(H\) is *not* a counterexample, then, since \(\delta(H)\ge3\)
   holds by assumption, concludes that \(H\) must contain a power-of-two cycle,
   which then lies in \(G\). Both routings are valid and use exactly the same
   two facts. The one compression is that step 4's case split (order versus
   size) is left implicit under the phrase "By minimality of \(G\)". It is the
   load-bearing point of the whole note, and it does close, as shown above.

**Verdict: VERIFIED.** No gap. Two elisions, both fillable in one line and
filled above: the well-ordering that makes "minimal counterexample" meaningful,
and the order/size case split.

**Reformulation used later in this dossier (equivalent, elementary).**
Lemma 0.1 says exactly: *\(G\) has no proper subgraph of minimum degree
\(\ge3\)*. Since every proper subgraph of \(G\) is contained in \(G-v\) for some
vertex \(v\) or in \(G-e\) for some edge \(e\), and since "has no nonempty
subgraph of minimum degree \(\ge3\)" is the definition of 2-degeneracy, this is
equivalent to: *\(G-v\) is 2-degenerate for every \(v\in V(G)\) and \(G-e\) is
2-degenerate for every \(e\in E(G)\)*.

## 2. Corollary 0.1(1) — the domination statement

**Statement as printed.**

> **Corollary 0.1.** Let \(G\) be a minimal counterexample to the
> Erdős–Gyárfás conjecture.
> 1. Every vertex of \(G\) is adjacent to a vertex of degree exactly \(3\).

**Proof as printed.**

> (1) Let \(v\in V(G)\). Since \(G-v\) is a proper subgraph of \(G\), Lemma
> \(0.1\) gives \(\delta(G-v)\leq 2\). Since every vertex of \(G\) has degree at
> least \(3\), the only way a vertex in \(G-v\) can have degree at most \(2\)
> after deleting \(v\) is if it was adjacent to \(v\) and had degree exactly
> \(3\) in \(G\). Therefore, \(v\) is adjacent to a vertex of degree exactly
> \(3\).

**Reconstruction, every nontrivial step checked.**

1. *\(G-v\) is a proper subgraph.* \(V(G-v)=V(G)\setminus\{v\}\subsetneq V(G)\). ✔
2. *\(G-v\) is nonempty, so \(\delta(G-v)\) is defined.* \(\delta(G)\ge3\)
   forces \(|V(G)|\ge4\), hence \(|V(G-v)|\ge3\ge1\). ✔ (Implicit in the paper;
   see D-d. One line, and true.)
3. *Lemma 0.1 applies:* \(\delta(G-v)\le2\), so there is
   \(u\in V(G)\setminus\{v\}\) with \(d_{G-v}(u)\le2\). ✔
4. *Identification of \(u\).* \(d_{G-v}(u)=d_G(u)-[\,u\in N(v)\,]\).
   - If \(u\notin N(v)\): \(d_{G-v}(u)=d_G(u)\ge3>2\), contradiction. So
     \(u\in N(v)\).
   - Then \(d_G(u)-1=d_{G-v}(u)\le2\), so \(d_G(u)\le3\); with \(d_G(u)\ge3\),
     \(d_G(u)=3\). ✔
5. So \(u\) is a neighbour of \(v\) of degree exactly \(3\). ✔

**Verdict: VERIFIED.** No gap. One elision (nonemptiness of \(G-v\)), filled
above.

## 3. Corollary 0.1(2) — the independence statement

**Statement as printed.**

> 2. The set of vertices of degree at least \(4\) forms an independent set.

**Proof as printed.**

> (2) Suppose \(u,v\in V(G)\) are adjacent vertices with \(d(u)\geq 4\) and
> \(d(v)\geq 4\). Deleting the edge \(uv\) decreases both degrees by exactly
> \(1\), so both vertices retain degree at least \(3\), while all other vertex
> degrees remain unchanged. Hence \(\delta(G-uv)\geq 3\), contradicting Lemma
> \(0.1\). Therefore, no two vertices of degree at least \(4\) can be adjacent.

**Reconstruction, every nontrivial step checked.**

1. \(G-uv\) has \(V(G-uv)=V(G)\) and \(E(G-uv)=E(G)\setminus\{uv\}\subsetneq
   E(G)\), so it is a proper subgraph. ✔
2. \(d_{G-uv}(u)=d_G(u)-1\ge3\), \(d_{G-uv}(v)=d_G(v)-1\ge3\), and for
   \(w\notin\{u,v\}\), \(d_{G-uv}(w)=d_G(w)\ge3\). Hence
   \(\delta(G-uv)\ge3\). ✔ (Simplicity is used: \(uv\) is a single edge, so
   removing it drops each endpoint's degree by exactly one. The paper's blanket
   simplicity hypothesis covers this.)
3. This contradicts Lemma 0.1. ✔

**Verdict: VERIFIED.** No gap. Figures 1 and 2 illustrate exactly this
computation for the \(k\)-regular case and carry no additional content.

**Provenance note.** The paper attributes this statement to Markström [7]
(K. Markström, *Extremal graphs for some problems on cycles in graphs*,
Congressus Numerantium 171 (2004), 177–188), and the abstract presents it as
Markström's observation. It was independently proved in this dossier as
`A001/L002` before the source was inspected, so it is available internally and
needs no import.

## 4. Corollary 0.2 — regular ⟹ cubic

**Statement as printed.**

> **Corollary 0.2.** If \(G\) is a regular minimal counterexample to the
> Erdős–Gyárfás conjecture, then \(G\) is cubic.

**Proof as printed.**

> Suppose \(G\) is \(k\)-regular. Since \(\delta(G)\geq 3\), one has \(k\geq 3\).
> If \(k\geq 4\), then every vertex has degree at least \(4\), contradicting
> Corollary \(0.1(2)\). Therefore \(k=3\), and hence \(G\) is cubic.

**Reconstruction.** The only step needing filling is *why* "every vertex has
degree at least 4" contradicts Corollary 0.1(2). Filler (one line): \(V(G)\neq
\emptyset\) and \(\delta(G)\ge3\), so \(E(G)\neq\emptyset\); pick any edge
\(uv\); both endpoints have degree \(k\ge4\), so both lie in the set of vertices
of degree \(\ge4\), which Corollary 0.1(2) says is independent — contradiction. ✔

**Verdict: VERIFIED,** with one elided but trivial step (named above). Not
imported by this dossier; verified because it was in the audit scope.

## 5. Theorem 0.1 — the 4/7 density bound

**Statement as printed.**

> **Theorem 0.1.** Let \(G\) be a minimal counterexample to the Erdős–Gyárfás
> conjecture. Then at least \(4/7\) of the vertices of \(G\) have degree exactly
> \(3\).

**Proof as printed.**

> Let \(V_{3}=\{v\in V(G):d(v)=3\}\) and \(V_{\geq 4}=\{v\in V(G):d(v)\geq 4\}.\)
> By Corollary \(0.1(2)\), the set \(V_{\geq 4}\) is independent. Hence every
> edge incident to a vertex of \(V_{\geq 4}\) joins it to a vertex of \(V_{3}\).
> Let \(e(V_{3},V_{\geq 4})\) denote the number of edges between the two sets.
> Since every vertex in \(V_{\geq 4}\) has degree at least \(4\), one has
> \(e(V_{3},V_{\geq 4})\geq 4|V_{\geq 4}|.\) On the other hand, every vertex in
> \(V_{3}\) has degree exactly \(3\), so \(e(V_{3},V_{\geq 4})\leq 3|V_{3}|.\)
> Therefore, \(4|V_{\geq 4}|\leq 3|V_{3}|.\) Since \(V(G)=V_{3}\cup V_{\geq 4}\),
> it follows that
> \(|V(G)|=|V_{3}|+|V_{\geq 4}|\leq|V_{3}|+\frac{3}{4}|V_{3}|=\frac{7}{4}|V_{3}|.\)
> Hence, \(|V_{3}|\geq\frac{4}{7}|V(G)|.\) Thus at least \(4/7\) of the vertices
> of \(G\) have degree exactly \(3\).

**Reconstruction, every nontrivial step checked.**

1. *\(V_3\) and \(V_{\ge4}\) partition \(V(G)\).* They are disjoint by
   definition, and their union is \(V(G)\) because \(\delta(G)\ge3\) means every
   degree is \(3\) or \(\ge4\). ✔ (Used twice: in "every edge incident to
   \(V_{\ge4}\) joins it to \(V_3\)" and in \(|V(G)|=|V_3|+|V_{\ge4}|\).)
2. *Every edge at a \(V_{\ge4}\)-vertex lands in \(V_3\).* A neighbour of
   \(b\in V_{\ge4}\) lies in \(V_3\cup V_{\ge4}\); independence of \(V_{\ge4}\)
   (Corollary 0.1(2)) excludes \(V_{\ge4}\). ✔
3. *Lower bound.* \(e(V_3,V_{\ge4})=\sum_{b\in V_{\ge4}}d(b)\) — an exact
   identity here, because all edges at \(V_{\ge4}\) go to \(V_3\) and the two
   sets are disjoint, so no edge is double-counted. Each \(d(b)\ge4\), giving
   \(e(V_3,V_{\ge4})\ge4|V_{\ge4}|\). ✔
4. *Upper bound.* \(e(V_3,V_{\ge4})=\sum_{a\in V_3}|N(a)\cap V_{\ge4}|\le
   \sum_{a\in V_3}d(a)=3|V_3|\). ✔
5. *Combination.* \(4|V_{\ge4}|\le3|V_3|\), i.e. \(|V_{\ge4}|\le\frac34|V_3|\);
   then \(|V(G)|=|V_3|+|V_{\ge4}|\le\frac74|V_3|\), i.e.
   \(|V_3|\ge\frac47|V(G)|\). ✔ Arithmetic checked.

**Verdict: VERIFIED.** No gap.

**Observation on what the proof uses (relevant to `G015` route R2; not a defect
of the paper).** Theorem 0.1's proof uses Corollary 0.1(**2**) only. It does
**not** use Corollary 0.1(**1**), and it does not use power-freeness beyond
what is already inside Corollary 0.1(2). The equality case
\(4|V_{\ge4}|=3|V_3|\) requires every \(V_{\ge4}\)-vertex to have degree exactly
\(4\) **and** every \(V_3\)-vertex to have all three of its neighbours in
\(V_{\ge4}\) — and the second condition contradicts Corollary 0.1(1), which says
every vertex (in particular every \(V_3\)-vertex) has a neighbour of degree
exactly \(3\). So the \(4/7\) bound is not attainable and the two corollaries
are not jointly exploited. This is the opening pursued in attempt `A020`.

## 6. Statement-correspondence against the dossier rows

| Dossier row | Recorded assertion (verbatim from `CLAIMS.md`) | Paper's statement (verbatim) | Verdict |
|---|---|---|---|
| `C004` | "In a counterexample minimizing order and then size, every proper subgraph with defined minimum degree has a vertex of degree at most 2." | Lemma 0.1: "Let \(G\) be a minimal counterexample to the Erdős–Gyárfás conjecture. Then \(\delta(H)\leq 2\) for every proper subgraph \(H\subsetneq G\)." | **Correspondence exact**, with the dossier strictly more conservative: it restricts the quantifier to subgraphs whose minimum degree is defined (see D-d), which the paper leaves unrestricted. Nothing is claimed that the paper does not prove. |
| `C005` | "Every vertex of an order-then-size minimal counterexample has a neighbor of degree exactly 3." | Corollary 0.1(1): "Every vertex of \(G\) is adjacent to a vertex of degree exactly \(3\)." | **Correspondence exact.** |
| `C006` | "At least \(4/7\) of the vertices of an order-then-size minimal counterexample have degree exactly 3." | Theorem 0.1: "Then at least \(4/7\) of the vertices of \(G\) have degree exactly \(3\)." | **Correspondence exact.** |

Hypothesis matching for all three: the paper's "minimal counterexample" is
defined (Notation, quoted in §0) as a graph with \(\delta\ge3\) and no cycle of
power-of-two length, of minimum order and then minimum size — which is exactly
an order-then-size minimal counterexample to `STATEMENT.md` version 0.1, by
D-a and D-b. **No mismatch found in any of the three.**

## 7. Overall verdict

**All four results verified: Lemma 0.1 — verified; Corollary 0.1(1) — verified;
Corollary 0.1(2) — verified; Corollary 0.2 — verified (one trivial elision);
Theorem 0.1 — verified.** No gap, no error, and no statement-correspondence
mismatch against `C004`, `C005`, `C006` as recorded. The note is four pages of
elementary minimal-counterexample arguments; every step is finite, exact, and
reproduced above.

Three consequences for the dossier, recorded here as observations only (this
note changes no ledger row):

1. **The three imports are now fully internally reconstructible.** The proofs of
   Lemma 0.1, Corollary 0.1(1) and Theorem 0.1 are reproduced in §§1–5 from
   `STATEMENT.md`'s definitions alone, using no unproved external input; the
   structural ingredient of Theorem 0.1 (independence of the degree-\(\ge4\)
   vertices) is in any case already proved internally as `A001/L002`. So
   `C004`–`C006` need not be carried as external dependencies of any argument
   that consumes them; the priority attribution to Carr (2026) and, for the
   independence statement, to Markström (2004) is of course unaffected.
2. **`C006` is not tight** — see the observation at the end of §5. Its equality
   case is refuted by `C005`.
3. **Nothing here bears on `C026`** (Carr, arXiv:2508.19302, diameter 2), which
   remains an abstract-strength import; it is cited by this note's paper as
   reference [8] and was not inspected.

## 8. Reproduction

The retrieved HTML was converted to plain text by tag-stripping (MathML
`alttext` retained) and read in full; both the abstract page and the HTML
rendering agree on version, date, and author. Anyone repeating this audit
should fetch <https://arxiv.org/abs/2605.22844> and confirm v1 is still the
current version before relying on §§1–6.
