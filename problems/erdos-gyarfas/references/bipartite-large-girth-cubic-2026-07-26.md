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

**Statement used (decoupled form).** Fix an even \(g\ge10\). For every \(N_0\)
there exists a connected **bipartite** 3-regular simple graph that is
**3-connected**, has girth \(\ge g\), and has order \(\ge N_0\). Girth is held
**fixed** while the order grows.

**Order, not diameter.** An earlier revision of this row asked for large
*diameter*. `A029` T2 does not need it: with \(ab\) fixed first, what the
construction consumes is a vertex far from a **pre-chosen edge**, and the
girth makes \(B(\{a,b\},r-1)\) a tree of size \(\le2^{\,r+1}-2\), so order
\(>2^{\,r+1}-2\) already supplies one at distance \(\ge r\). Diameter
hypotheses were wrong twice here (`R004` F2(a), F11) and are gone. At
\(g=10\), \(r=g/2\) the bound reads \(N>62\), which a girth-10 cubic graph
(order \(\ge70\)) satisfies automatically.

**Withdrawn: the Tutte 12-cage as a witness.** An earlier revision named it as
satisfying a diameter requirement it does not meet. With the order form it is
simply not the relevant kind of object, and it stays withdrawn.

> ## ⚠ UNRESOLVED — `R004` F3′ (major, open)
>
> **The 3-connectivity clause of this row has no source.** The two routes
> recorded below — Erdős–Sachs (`X001`) and the bipartite double cover —
> supply bipartiteness, cubicity and girth, and **neither supplies
> connectivity**, as the "Route" paragraph itself states. The only support
> the row ever had for 3-connectivity was "cages of girth \(\ge5\) are
> 3-connected", and the same revision that decoupled the statement
> **withdrew cages**. So as recorded, `X004` asserts an existence claim in a
> regime it does not source.
>
> Consequences, stated plainly: **`L057` is not established.** It is recorded
> at `proposed` and may not be cited. The interpolation-genre conclusion does
> **not** depend on it — `L056` (audited, passed) kills the absolute form
> outright at order 30, and the bipartite one-liner \(\tilde F-ab\) kills the
> relativized form against a bipartite defender. What is unproved is exactly
> the *non-bipartite* relativized kill.
>
> To discharge: either source bipartite cubic **3-connected** graphs of fixed
> girth \(\ge10\) and unbounded order, or replace 3-connectivity by something
> derivable — note `A029` T2 uses it only to make \(H=F_1-ab\) vertex-taut, so
> any hypothesis delivering vertex-tautness would do.

**Sources.** W. T. Tutte, *A family of cubical graphs*, Proc. Cambridge
Philos. Soc. **43** (1947), 459–474 (the 8-cage); C. T. Benson, *Minimal
regular graphs of girths eight and twelve*, Canad. J. Math. **18** (1966),
1091–1094 (the 12-cage). Cage tables and the 3-connectivity of cages are
standard in every survey of the cage problem (e.g. Exoo–Jajcay, *Dynamic
cage survey*, Electron. J. Combin., Dynamic Survey DS16). P. Erdős and
H. Sachs (1963) as recorded in `X001`.

**Hypothesis match.** `A029` T2 uses only: bipartite, cubic, simple, finite,
3-connected, even girth \(\ge10\), and order \(>2^{\,r+1}-2\) for the chosen
radius \(r\ge g/2\). It does not use regularity of the bipartition classes
beyond cubicity, vertex-transitivity, or any incidence-geometric property.
Unbounded order at fixed girth is used only to defeat (INT-rel\(_c\)) for
**every** constant \(c\); a single \(g=10\) instance already defeats the
recorded pivot-trigger form, and there the order condition is automatic.

**Strength.** `reported-classical` for the girth/bipartite/cubic clauses;
**unsourced** for 3-connectivity (see the boxed finding above). Its use
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
