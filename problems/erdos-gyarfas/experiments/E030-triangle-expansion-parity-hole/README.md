# E030 — the triangle expansion: T2's parity hole, and T1's order-30 witness

- Date: 2026-07-26
- Session: `S031`
- Attempt: `A029` T2 (part 1) and `A029` T1 (part 2)
- Status: complete; all assertions pass under both interpreters

## What this is for

`A029` T2 proves that no relativized interpolation conjecture
\(S\supseteq[\min S+c,\max S]\) holds at class strength, by constructing a
**non-bipartite** vertex-taut \(\{C_4,C_8\}\)-free exactly-two-profile pair
whose through-set has a long parity hole immediately above \(\min S\). The
construction has five steps, each an assertion about an explicit graph. This
experiment builds such a graph from scratch and checks all five directly,
rather than leaving them as hand arguments.

## Scope — read this before citing

The instance built here has **girth 6**, so it contains \(C_8\)s and is
**not** a member of the \(\{C_4,C_8\}\)-free class. It is therefore **not** a
counterexample to anything, and no ledger row rests on it.

What it verifies is the **mechanism**: the connectivity argument for the
triangle expansion, the cycle-spectrum containment, the parity bookkeeping
over \(k\in\{0,1,2\}\) triangle edges, the bound "even through-lengths cost
\(2\rho+2\)", and the resulting hole. Raising the girth from 6 to \(\ge10\)
changes no step of the argument; that step is the `X004` import, and it is
the only part of T2 this experiment does not exercise. Part 2 below is
different in kind: it verifies an explicit **class member** for T1.

## Instrument

`check.py` — self-contained, no dependencies, ~200 lines. Everything is
computed from scratch: girth and diameter by BFS from every vertex,
\(k\)-connectivity by brute-force enumeration of all vertex cuts of size
\(<k\), the cycle spectrum below \(g\) by DFS, and the bottom of the
through-set by depth-bounded DFS with a distance-to-target prune (so the
enumeration of short \(a\)–\(b\) paths is **exhaustive** up to the stated
bound, not sampled).

Run: `python3 check.py` (also run under `pypy3`; identical output).

## The instance

Base graph: the cyclic Haar graph \(H(52;\{0,1,5\})\) — bipartite, cubic,
order 104, girth **6**, diameter **12**, verified 3-connected by exhaustive
cut enumeration. T2(v) requires order \(>2^{\,r+1}-2\) for the chosen radius; here \(\rho=6\)
is exhibited directly, which is what the bound is for.

Chosen edge \(ab=(0,52)\): the shortest cycle through it has length 6, i.e.
it lies on a shortest cycle, as T2(v) requires (choice 1). Chosen expansion
vertex \(v=11\) with \(\rho=6\ge g/2=3\) (choice 2; 54 candidates were
available).

Expanded graph \(F_1\): order 106, 159 edges, cubic, verified 3-connected.
\(H=F_1-ab\): order 106, exactly two degree-2 vertices, all others \(\ge3\),
verified 2-connected — hence vertex-taut.

## Results

| T2 step | assertion | verdict |
|---|---|---|
| (i) | \(F_1\) is cubic and 3-connected | **true** (no cut of size 1 or 2) |
| (ii) | \(\mathrm{Spec}(F_1)\cap[3,g)=\{3\}\) — the triangle is the only short cycle | **true** |
| (ii) | \(H\) is an exactly-two-degree-2 profile pair, 2-connected | **true** |
| (iii) | \(\min S=g-1=5\), and it is odd | **true** |
| (iv) | a through-path has even length **iff** it uses exactly one triangle edge | **true, 0 violations** over every enumerated path |
| (iv) | every even through-length is \(\ge2\rho+2\) | **true, and tight**: \(\rho=6\), smallest even length **14** \(=2\rho+2\) |
| (v) | \(\min S+1\) is a hole | **true** (6 absent) |
| (v) | every even value in \([g,2\rho+2)\) is absent | **true** (6, 8, 10, 12 all absent) |

Through-lengths \(\le14\): \(\{5,9,11,13,14\}\).

**The sharp bound, and how the audit used it.** The smallest even
through-length is **14**, which is exactly \(2\rho+2\), not \(2\rho=12\).
An earlier revision of T2 proved only \(|Q|\ge2\rho\), and `R004` F5
required the sharper \(2\rho+2\) — which this experiment had been measuring
all along. The repair therefore changes no number here; it brings the proof up
to what the data already showed.

**Recorded beyond the claim.** \(7\) is also absent — an *odd* hole, which
T2's parity argument neither predicts nor needs. Recorded as an observation,
not a claim; `check.py` asserts exactly T2's statement and nothing stronger.
An earlier draft of the script asserted that *all* holes are even, which is
false here; that was the script's error, not the mechanism's, and was
corrected.

## Part 2 — the order-30 witness for `A029` T1 (`truncation.py`)

Added after the `R004` audit (finding F4). The attempt's draft asserted that a
\(\{C_4,C_8\}\)-free profile pair with \(\min S\ge9\) needs order \(\ge70\).
That is false; the audit produced the counterexample and this script rebuilds
and verifies it independently.

`truncation.py` constructs the **truncated Petersen graph** \(P^{\ast}\) —
every vertex of the Petersen graph replaced by a triangle, each triangle
vertex inheriting one of its three edges — deletes a **link** edge, and checks
every claim.

| assertion | verdict |
|---|---|
| \(P^{\ast}\) is cubic, order 30, 45 edges | **true** |
| cycle lengths **at most 13** are exactly \(\{3,10,11,12\}\) (the enumeration reaches 13; there is no 13-cycle) | **true** — so \(C_4\)-free and \(C_8\)-free |
| \(P^{\ast}\) is 3-connected (exhaustive cut enumeration) | **true** |
| \(H=P^{\ast}-ab\) has exactly two degree-2 vertices, min degree 2 | **true** |
| \(H\) is 2-connected, hence vertex-taut | **true** |
| \(S(H,a,b)=[9,26]\), a full interval | **true** (exhaustive path enumeration) |
| \(8\notin S\) while \(\max S=26\) | **true** — **(INT) is false at order 30** |

Order 30 is **inside** the case-(5b) window (\(H\)-orders \([22,40]\), `L058`)
and inside the previously recorded window \([18,35]\). So `A029` T1 is not an
asymptotic result.

\(14\in S\) here, so this object does not refute (INT-14). Chaining two copies
— identify \(b\) of one with \(a\) of the other — gives order \(30+30-1=59\)
with \(S=S+S=[18,52]\) (a path through a cut vertex splits, so the through-set
is the sumset), hence \(14\notin S\) and \(\max S=52\): **(INT-14) is false at
order 59**. That step is arithmetic on the verified \(S=[9,26]\) and needs no
further computation.

Both objects contain \(C_{16}\) and are far from power-free: they are
calibration objects, not counterexample candidates, and no floor moves.

## Reproduction

```
cd problems/erdos-gyarfas/experiments/E030-triangle-expansion-parity-hole
python3 check.py        # ~0.5 s   (part 1, the parity hole)
pypy3   check.py        # identical output
python3 truncation.py   # ~2 s     (part 2, the order-30 witness)
```

Deterministic: no randomness, no seeds, no external data. The graph is
generated from the two integers \(n=52\), \(b=5\) written in `main()`.
