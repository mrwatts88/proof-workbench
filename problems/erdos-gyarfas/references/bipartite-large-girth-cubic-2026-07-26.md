# Reference audit — bipartite cubic graphs of large girth

- Date: 2026-07-26
- Session: `S031`
- Purpose: supply the single external existence fact used by `A029` T2 (the
  parity-stratum refutation of every relativized interpolation conjecture).
  Nothing else in the dossier consumes this row.

Import discipline as in `references/large-girth-non-hamiltonian-cubic-2026-07-26.md`:
precise statement used, hypotheses matched to our use, source, and the
strength at which the dossier may cite it.

---

## `X004` — bipartite cubic 3-connected graphs of girth \(\ge10\)

**Statement used (decoupled form — this matters, see below).** Fix an even
\(g\ge10\). For every \(D\) there exists a connected **bipartite** 3-regular
simple graph that is 3-connected, has girth \(\ge g\), and has diameter
\(\ge D\). Girth is held **fixed** while order and diameter grow.

**Why decoupled.** `A029` T2 consumes the **diameter**, not the girth: it needs
a vertex at distance \(\rho\ge g/2\) from a chosen shortest-cycle edge, i.e.
\(\mathrm{diam}\ge g/2+1\), and it needs \(\rho\to\infty\) *with \(g\) fixed*
to make the hole arbitrarily long. A coupled statement of the form "larger
girth forces larger order, hence larger diameter" does **not** supply that,
and this was `R004` F3 against an earlier revision of this row. The bipartite
parity bound \(\rho\le\mathrm{diam}-1\), proved inside `A029` T2(v), is why
the diameter must exceed \(g/2\) rather than merely reach it.

**Withdrawn: the Tutte 12-cage as a witness.** An earlier revision named it.
It has girth 12 and diameter 6, so \(\rho\le5<6=g/2\): it **fails** the
requirement. More generally every \((3,g)\)-cage has diameter \(\approx g/2\)
and therefore lies in the failing regime — cages are extremal in exactly the
wrong direction here, and no cage can serve as the witness. Recorded so that
no later session reaches for one.

**Route.** Bipartite cubic graphs of girth \(\ge g\) exist for every \(g\)
(the Erdős–Sachs argument of `X001` applies verbatim to the bipartite case;
equivalently, for a cubic \(G\) of girth \(\ge g\) the bipartite double
cover \(G\times K_2\) is bipartite, cubic and of girth \(\ge g\), because
a cycle of the cover projects to a non-backtracking closed walk of the same
length, which contains a cycle of at most that length). Arbitrarily large
diameter at fixed girth is the standard "many graphs, few of small diameter"
observation: a cubic graph of diameter \(D\) has at most \(1+3(2^{D}-1)\)
vertices, so any infinite family of bipartite cubic graphs of girth \(\ge g\)
has unbounded diameter. What is **not** derived internally is 3-connectivity —
the double-cover route does not supply it — which is why this row is an
import rather than a lemma.

**Sources.** W. T. Tutte, *A family of cubical graphs*, Proc. Cambridge
Philos. Soc. **43** (1947), 459–474 (the 8-cage); C. T. Benson, *Minimal
regular graphs of girths eight and twelve*, Canad. J. Math. **18** (1966),
1091–1094 (the 12-cage). Cage tables and the 3-connectivity of cages are
standard in every survey of the cage problem (e.g. Exoo–Jajcay, *Dynamic
cage survey*, Electron. J. Combin., Dynamic Survey DS16). P. Erdős and
H. Sachs (1963) as recorded in `X001`.

**Hypothesis match.** `A029` T2 uses only: bipartite, cubic, simple, finite,
3-connected, even girth \(\ge10\), and \(\mathrm{diam}\ge g/2+1\) — the
last so that a vertex at distance \(\ge g/2\) from a chosen shortest-cycle
edge exists. It does not use regularity of the bipartition classes beyond
cubicity, vertex-transitivity, or any incidence-geometric property. A single
instance with \(g=10\) and diameter \(\ge6\) already defeats the recorded
pivot-trigger form; unbounded diameter at fixed girth is used only to defeat
(INT-rel\(_c\)) for **every** constant \(c\).

**Strength.** `reported-classical`. Not verified line by line here. Its use
is an **existence** use inside a *negative* result — it produces a
calibration object showing a conjecture's hypotheses are too weak — so an
error in it could only remove a warning, never create a false claim in
`PROOF.md`. The operative half of `A029` (T1, the refutation of (INT) and
(INT-14)) uses **none** of this row: its witnesses are explicit finite graphs
of orders 30 and 59, verified in `E030`.

---

## What is *not* claimed

- No claim that the objects of `A029` T2 are power-free. They are not
  expected to be, and nothing downstream assumes it. They are calibration
  objects in the sense fixed by `C037` for Petersen\(-e\).
- No claim about the smallest order at which `A029` T2's construction is
  realisable. The \((3,10)\)-cage bound of 70 vertices is a lower bound for
  the underlying girth-10 graph, but the diameter requirement pushes the
  usable orders higher and this row does not pin them down.
- **Nothing here is needed for `A029` T1.** T1's witnesses — truncated
  Petersen minus a link edge (order 30) and its two-copy chain (order 59) —
  are explicit and import-free. This row gates only T2 / `L057`.
