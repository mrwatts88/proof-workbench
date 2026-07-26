# Reference audit — large-girth cubic graphs, non-Hamiltonian ones, and snarks

- Date: 2026-07-26
- Session: `S030`
- Purpose: supply the external existence facts used by `A028` T1 (the
  no-class-level-Hamiltonian-forcing theorem). Nothing else in the dossier
  consumes these rows.

Import discipline: each row below records the precise statement used, the
hypotheses as matched to our use, the source, and the strength at which the
dossier may cite it. None of these is re-derived internally; all are classical
or published existence results, imported at the strength stated.

---

## `X001` — Erdős–Sachs: regular graphs of arbitrary girth

**Statement used.** For every \(k\ge3\) and every \(g\ge3\) there exist
\(k\)-regular simple graphs of girth at least \(g\); moreover there are such
graphs of arbitrarily large order (adding order is free — take disjoint unions
or larger members of the family).

**Source.** P. Erdős and H. Sachs, *Reguläre Graphen gegebener Taillenweite mit
minimaler Knotenzahl*, Wiss. Z. Martin-Luther-Univ. Halle-Wittenberg
Math.-Natur. Reihe **12** (1963), 251–257. Standard textbook result; also
recorded in every survey of the cage problem, with the quantitative form
\(g(k,n)\ge(1-o(1))\log_{k-1}n\).

**Hypothesis match.** We use it only for \(k=3\) and \(g=17\). Simple,
undirected, finite — matches `D001`.

**Strength.** `reported-classical`. Not verified line by line here; it is a
1963 result reproved many times (and constructively realised by explicit
families — Ramanujan graphs, sextet graphs). Our use of it is an *existence*
use in a negative result (it produces a calibration object), so an error in it
could only remove a warning, never create a false claim in `PROOF.md`.

---

## `X002` — Haythorpe: non-Hamiltonian cubic graphs of arbitrary girth

**Statement used.** For every \(g\) there exist non-Hamiltonian 3-regular
simple graphs of girth at least \(g\). The construction may be chosen
**3-edge-connected** (bridgeless).

**Source.** M. Haythorpe, *Non-Hamiltonian 3-regular graphs with arbitrary
girth*, Universal Journal of Applied Mathematics **2**(1) (2014), 72–78;
arXiv:1902.10344. Abstract, verbatim: "It is well known that 3–regular graphs
with arbitrarily large girth exist. Three constructions are given that use the
former to produce non-Hamiltonian 3–regular graphs without reducing the girth,
thereby proving that such graphs with arbitrarily large girth also exist. The
resulting graphs can be 1–, 2– or 3–edge-connected depending on the
construction chosen."

**Hypothesis match.** We use the 3-edge-connected variant at \(g=17\). For a
cubic graph, vertex connectivity equals edge connectivity, so the 3-edge-
connected variant is **3-connected** — this is the classical fact
\(\kappa=\kappa'\) for cubic graphs, used to get 2-connectivity of the
calibration object after one edge deletion.

**Strength.** `reported`. Abstract read directly; the constructions were not
audited line by line. See `X003` for a logically independent second route to
the same existence statement, so `A028` T1 does not rest on a single source.

---

## `X003` — Kochol's snarks, plus the elementary non-Hamiltonicity of snarks

**Statement used (external half).** For every \(g\) there exist snarks — cubic,
cyclically 5-edge-connected graphs of chromatic index 4 — of girth at least
\(g\).

**Source.** M. Kochol, *Snarks without small cycles*, J. Combin. Theory Ser. B
**67**(1) (1996), 34–47. This is the negative solution of the Jaeger–Swart
girth conjecture (which had asserted every snark has girth \(\le6\)).
Restated and improved in R. Lukoťka / E. Máčajová / J. Mazák / M. Škoviera and
in *Girth, oddness, and colouring defect of snarks* (arXiv:2106.12205), which
records that it "improves Kochol's original construction of snarks with large
girth (1996)" and provides "infinitely many nontrivial snarks of any prescribed
girth \(g\ge5\)".

**Internal half (hand proof, not imported).** *A cubic graph with a Hamiltonian
cycle has chromatic index 3.* Let \(G\) be cubic with Hamiltonian cycle \(C\).
Cubic graphs have even order, so \(C\) is an even cycle; two-colour \(E(C)\)
alternately. The edges off \(C\) form a perfect matching (each vertex has
exactly one), so give them a third colour. Hence \(\chi'(G)=3\). Contrapositive:
**a snark is non-Hamiltonian.**

**Strength.** External half `reported`; internal half `proved` (three lines,
above).

**Why both `X002` and `X003` are recorded.** They give the same conclusion —
non-Hamiltonian cubic graphs of arbitrarily large girth, 3-connected — through
disjoint literature. `A028` T1 is therefore not hostage to either source.

---

## What is *not* claimed

- No claim is made about the **order** at which the calibration object first
  appears. A cubic graph of girth 17 has order in the thousands, so `A028` T1 is
  an asymptotic statement. It says nothing about the extremal window
  \([22,24]\) or the case-(5b) window \([18,35]\), and it is recorded that way.
- No claim is made that any of these graphs is **power-free**. They are not
  expected to be: they are calibration objects, i.e. witnesses that a proposed
  lemma's hypotheses are too weak, in the sense already used in this dossier
  for Petersen\(-e\) (`C037`).
