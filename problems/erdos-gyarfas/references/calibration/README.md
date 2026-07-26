# Calibration objects for `P-002` (statement 0.1)

Created S032, 2026-07-26. **These supersede Petersen\(-e\), the order-14 exemplar
and calibration object #3 as the primary calibration objects (`G018`).**

Every drafted lemma about a counterexample to statement 0.1 must be checked
against these **before** work begins on it. A lemma that *holds* on any of them
without consuming power-freeness above the girth or minimum-order minimality is
a soundness alarm: these graphs satisfy every local, hereditary hypothesis
anyone has proposed, and several of them clear three consecutive powers of two.

All properties below were verified by the S032 orchestrator with independently
written code, from the stored graph6 strings, not taken on report.

| file | order | verified properties |
|---|---|---|
| `cubic78-no-4-8-16.g6` | 78 | connected, **cubic**, 117 edges; **no \(C_4\), no \(C_8\), no \(C_{16}\)**; **\(C_{32}\) present**. Independently matches Exoo's \(f(4)\le78\) (arXiv:1403.5636). **The strongest near-counterexample in the file.** It fails by exactly one power. |
| `cubic98-no-4-8-16.g6` | 98 | connected, cubic; no \(C_4\), \(C_8\), \(C_{16}\); \(C_{32}\), \(C_{64}\) present. H7-inflation of the Heawood graph. Not a record (78 is smaller) but built by an independent route. |
| `bipartite38-girth6-no-C8.g6` | 38 | connected, **cubic, bipartite** (19+19), **girth exactly 6**, cycle counts 19/0/171/323/969 at lengths 6/8/10/12/14 — **no \(C_4\), no \(C_8\)**. The hexagonal torus \(H(19,1,8)\). Refutes "bipartite + \(\delta\ge3\) + girth 6 \(\Rightarrow C_8\)" (`L069`) and is provably the minimum such **toroidal** graph. |
| `planar24-cubic-3conn-no-4-8.g6` | 24 | cubic, **planar**, **3-connected**; spectrum \(\{3,5,6,7\}\cup[9,24]\) — exactly 4 and 8 missing; \(C_{16}\) present. The **unique** smallest 3-connected cubic planar \(\{C_4,C_8\}\)-free graph (`C051`; none at order \(\le22\), one at 24, none at 26). |
| `gadget241-rho1.g6` | 241 | 3-terminal gadget: exactly three degree-2 vertices, all others cubic; no \(C_4\), no \(C_8\); all three terminal path sets \(=\{2\}\), so \(\rho=1\) exactly. Refutes the proposed "\(\rho\ge2\)" substitution barrier (`L074`). |

## Not stored here, but equally binding — construct them, they are two lines each

- **The buckyball \(C_{60}\)** (truncated icosahedron): 3-connected **cubic
  planar**, no \(C_4\), no \(C_8\), smallest power cycle \(C_{16}\). Its
  existence is why "3-connected cubic planar \(\Rightarrow C_4\) or \(C_8\)" is
  false, and why Heckman–Krakovski state \(2\le m\le7\).
- **The truncated dodecahedron**: 3-connected cubic planar, 20 triangles and 12
  decagons, no \(C_4\), no \(C_8\). Pentagon-free, where the buckyball is
  triangle-free — together they show **neither a 3-face nor a 5-face can be
  excluded** in a planar counterexample (`L073`).
- **Two buckyballs glued at a vertex**: planar, \(\delta\ge3\), one vertex of
  degree 6, no \(C_4\), no \(C_8\). Refutes "a planar counterexample is cubic"
  (`L073`).
- **The \(K_4-e\) necklace \(N_t\)** (\(t\) copies of \(K_4-e\), connector edges
  \(v_iu_{i+1}\)): **cubic, 2-connected, Hamiltonian** on \(4t\) vertices,
  spectrum \(\{3,4\}\cup[3t,4t]\). Refutes Conjecture SF (`L066`). Verified at
  \(t=3,4,5\).
- **The parity necklace** (\(t\) odd copies of the 10-vertex bridge of
  \(K_{2,3}\) and \(K_{2,3}+e\)): cubic on \(10t\) vertices with **entire even
  cycle spectrum \(=\{4\}\)**. Refutes every window strengthening of 0.1
  (`L066`). Verified at \(t=3,5\).
- **Exoo's \(G_{450}\)** (arXiv:1403.5636): cubic, no \(2^m\)-cycle for
  \(m\le5\) — Tutte–Coxeter with every vertex replaced by a 15-vertex gadget.
  Not reconstructed here; the terminal alignment to the base's chord structure is
  what kills the 32-cycles and an arbitrary assignment does not work.
- **Exoo's \(G_{420}\)**: 3-connected cubic **planar**, no \(2^m\) for
  \(m\le4\). Refutes Heckman–Krakovski's suggested improvement to \(m\le4\), so
  the true planar exponent bound is \(5\le m\le7\).

## The one shape a counterexample still needs

A counterexample must dodge \(\sim\log_2 n\) powers, so its cycle spectrum needs
a fresh gap before **every** doubling — gaps spread across the whole spectrum,
including the top. Two data points bracket the question:

- **Second-half gaps do exist at \(\delta\ge3\).** The \(K_4-e\) necklace on
  \(4t\) vertices has spectrum \(\{3,4\}\cup[3t,4t]\); its gap \([5,3t-1]\)
  extends well past the spectrum's midpoint \(2t\). But it contains a \(C_4\).
- **Nobody can produce one without a \(C_4\).** The only published "many gaps"
  family (Goedgebeur–Jooken–Provoost–Zamfirescu, arXiv:2506.09667) has, in the
  authors' own words, cycle spectrum of size \(2/3\) the order with **all gaps in
  the first half**, and "gaps in the second half of the spectrum elude us"
  (`C052`). A full second half is an interval of multiplicative width 2 and
  therefore contains a power of two.

So the sharp disproof question is **not** the literature's "can there be gaps in
the second half?" — the answer is yes — but **"can second-half gaps coexist with
\(C_4\)-freeness?"** That is the junction of the two live threads and the single
best-posed target on the disproof side.
