# E012 — All-terminal-pair search for taut C4-free gadgets with through-set in {3,4,5}, and the endgame dichotomy check

- Date: 2026-07-24
- Problem: `P-002`
- Evidence class: falsification search for a proved lemma (`A013` T8 = `L030`)
  plus instance-exhaustive verification of its endgame

## Question

`A013` T8 asserts: no vertex-taut C4-free (D)-gadget \((H,a,b)\) has
\(S(H,a,b)\subseteq\{3,4,5\}\). Search exhaustively for a counterexample at
orders 6–14, over **every admissible terminal pair** of every graph in the
class — including pairs with both terminal degrees \(\ge3\), which
`E011`/`C028` never examined (that survey fixed the terminals as the two
sub-cubic vertices). Separately, verify the proof's final dichotomy (T8
Case A / Case B) on every three-matchings structure at \(k\in\{2,4\}\).

## Logical scope

The experiment can refute `L030` (one taut hit would) but not prove it; the
theorem's universal claim rests on the `A013` hand proofs. Coverage at each
order \(n\le14\) is exhaustive for the theorem's targets: a (D)-gadget of
order \(n\) is connected, C4-free, min degree \(\ge1\), with at most two
sub-cubic vertices (only terminals may be sub-cubic) and degree sum
\(\ge3(n-2)+2=3n-4\), hence \(\ge\lceil(3n-4)/2\rceil\) edges — exactly the
`E010` geng stream class; and every admissible terminal pair of every stream
graph is scanned. The two prefilters (see below) are necessary conditions of
the target, so rejecting on them loses no coverage. The A2 anchor is
exhaustive for the endgame structure class at \(k\in\{2,4\}\) only.

## Environment

- Tool and version: CPython 3.14.2; geng from nauty 2.9.3
  (`/opt/homebrew/bin/geng`), same anchored invocation as `E010`/`E011`
  (`geng -q -c -f -d1 n mine:0`, `mine`\(=\lceil(3n-4)/2\rceil\)).
- Dependencies: standard library only. Graph primitives (graph6 decoder,
  degree/C4 detectors) copied verbatim from `E011/verify_taut.py`, which was
  anchored there against the independent `E010` pipeline; the pair scan,
  distance prefilters, bounded-abort path DFS, and endgame enumerator are
  new to this experiment.
- Exact arithmetic / floating point: integer bitmask arithmetic throughout.
- Random seed: none (deterministic enumeration).

## Inputs and search space

The `E010` stream at orders 6–14 (totals asserted against `C027` records:
4; 5; 36; 84; 918; 4,058; 52,331; 389,734; 5,605,161). Per graph: admissible
terminal pairs are those containing every sub-cubic vertex and with degree
sum \(\ge3\) (graphs with \(\ge3\) sub-cubic vertices admit none). Per pair,
in order:

1. distance prefilter: \(3\le d(a,b)\le5\) (else \(s_{\min}\notin\{3,4,5\}\));
2. eccentricity prefilter: \(d(a,v)+d(v,b)\le5\) for every \(v\) (a vertex
   at position \(i\) of a length-\(\ell\le5\) simple \(a\)–\(b\) path has
   \(d(a,v)\le i\), \(d(v,b)\le\ell-i\); necessary for tautness given
   \(S\subseteq\{3,4,5\}\));
3. exact all-simple-paths DFS, aborting on the first \(a\)–\(b\) arrival of
   length \(\ge6\); on completion \(S\subseteq\{3,4,5\}\) holds exactly and
   tautness is read off the essential-vertex mask (union of path supports).

Fixed anchors: \(K_{3,3}-e\); all 218 three-matchings structures at
\(k\in\{2,4\}\); the five `E011` taut pinched gadgets; \(P_4\).

## Reproduction

```sh
python3 scan_pairs.py anchors
python3 scan_pairs.py run 6 7 8 9 10 11 12 13 14
```

Outputs land in `data/pairs_n{n}.json` (per-order counts, every taut hit —
none — and every non-taut \(S\subseteq\{3,4,5\}\) pair verbatim).

## Results

Anchors: all 736 checks pass. \(K_{3,3}-e\) is reported **taut** with
\(S=\{3,5\}\) by the scan machinery (positive control) and contains a
\(C_4\) (so it is absent from every C4-free stream). All 218 three-matchings
structures satisfy the T8 dichotomy exactly: a \(C_4\) is present **iff**
some \(x\) has \(\sigma(\varphi(x))=\psi(\sigma(x))\) (Case A), and every
\(C_4\)-free structure has a simple \(a\)–\(b\) path of length \(\ge7\) and
is rejected by the scan (Case B); both branches occur. The five `E011` taut
pinched gadgets are rejected on distance (\(d(a,b)=6\)). \(P_4\) admits no
pair.

| n | stream | eligible graphs | pairs | reject dist | reject ecc | reject long | non-taut S⊆{3,4,5} | **taut hits** |
|---|---|---|---|---|---|---|---|---|
| 6 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| 7 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| 8 | 36 | 1 | 1 | 0 | 0 | 1 | 0 | **0** |
| 9 | 84 | 4 | 11 | 6 | 0 | 5 | 0 | **0** |
| 10 | 918 | 38 | 298 | 238 | 10 | 50 | 0 | **0** |
| 11 | 4,058 | 256 | 1,300 | 823 | 177 | 300 | 0 | **0** |
| 12 | 52,331 | 2,143 | 9,808 | 5,844 | 2,099 | 1,865 | 0 | **0** |
| 13 | 389,734 | 20,432 | 101,216 | 58,241 | 26,492 | 16,483 | 0 | **0** |
| 14 | 5,605,161 | 241,135 | 1,357,597 | 760,676 | 417,046 | 179,875 | 0 | **0** |

Stream totals reproduce the `E010`/`C027` records at every order (asserted
in the script). Runtimes: \(\le11.5\)s per order through 13, 160.2s at
order 14 (all CPython 3.14.2).

## Interpretation

- No taut C4-free (D)-pair with \(S\subseteq\{3,4,5\}\) exists at any order
  \(\le14\), over all terminal choices: `L030`'s prediction survives its
  falsification search, one full order beyond `C028`'s survey and with the
  degree-\(\ge3\)-terminal slice covered for the first time.
- Stronger than predicted: **not even a non-taut** (D)-pair with
  \(S\subseteq\{3,4,5\}\) exists at these orders — every pair passing both
  prefilters is rejected by a length-\(\ge6\) path. (`L026` implies non-taut
  pinched pairs at small \(s_{\min}\) exist only if counterexamples to 0.1
  do, so their absence here is consistent; their absence is *not* implied by
  `L030` and is recorded as an observation only.)
- The T8 endgame dichotomy is exactly right on every structure instance in
  reach: the Case-A block condition characterizes the \(C_4\)s, and Case B
  always yields a length-\(\ge7\) path.
- Claim-ledger update: `C029`.

## Independent checks

The graph primitives are the `E011` implementations, previously
cross-validated bidirectionally against `E010` on identical streams; the
stream totals asserted here re-anchor the generation leg. The new scan logic
is validated by the positive control (A1), the exhaustive structural anchor
(A2, 218/218), the negative controls (A3, A4), and the internal
DFS-vs-BFS consistency assert on every completed pair.
