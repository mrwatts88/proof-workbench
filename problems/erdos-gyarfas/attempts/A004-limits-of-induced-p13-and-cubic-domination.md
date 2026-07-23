# A004 — Limits of induced-P13 and cubic domination

- Date opened: 2026-07-23
- Problem: `P-002`
- Status: completed

## Intended mechanism

Combine the imported conclusions for an order-then-size minimal counterexample:
the cubic vertices dominate, at least \(4/7\) of the graph is cubic, and an
induced \(P_{13}\) exists. The proposed local mechanism was that every
attachment of the cubic dominating set to that path which avoids \(C_4\) and
\(C_8\) must close a \(C_{16}\).

## Entry assumptions

- `D001`–`D004`.
- `C004`–`C007`, used only at their recorded strengths.
- For the proposed forcing step, the absence of \(C_4\) and \(C_8\).

## Targeted obligations

- `G003`: find a global power-of-two cycle-forcing mechanism.
- `G006`: decide the induced-\(P_{13}\)/cubic-domination route.

## Plan and decisive tests

1. Determine how much cubic domination actually restricts an induced
   \(P_{13}\).
2. Search the smallest cubic completion consisting of the path and five
   independent outside vertices.
3. Test the claimed implication against finite cubic graphs of girth at least
   \(17\), which avoid \(C_4,C_8,C_{16}\) by definition.

## Deductions

### Cubic domination is vacuous on the cubic case

Every connected cubic graph satisfies all three imported minimality conclusions
`C004`–`C006`:

- every proper nonempty subgraph has a vertex of degree at most \(2\);
- every vertex has a cubic neighbor;
- every vertex, and hence at least \(4/7\) of the vertices, is cubic.

For the first assertion, let \(H\) be a proper nonempty subgraph of a connected
cubic graph \(G\). If \(V(H)=V(G)\), some edge of \(G\) is missing from \(H\),
and an endpoint has degree at most \(2\) in \(H\). If \(V(H)\) is proper,
connectedness gives an edge of \(G\) from \(V(H)\) to its complement, and its
endpoint in \(V(H)\) again has degree at most \(2\) in \(H\). The other two
assertions are immediate.

Thus `C004`–`C006` do not distinguish a hypothetical cubic counterexample from
an arbitrary connected cubic graph.

### `L007` — The imported structural bundle does not force \(C_{16}\)

There exists a finite connected cubic graph \(G\) which satisfies the
minimal-counterexample conclusions `L002` and `C004`–`C006`, contains the
induced \(P_{13}\) conclusion drawn from `C007`, and has no cycle of length
\(4\), \(8\), or \(16\).

**Proof.** By `C009`, applied with \(g=17\) and with one cycle as the prescribed
2-factor, there is a finite Hamiltonian cubic graph \(G\) of girth at least
\(17\). It is connected because it is Hamiltonian. Its girth excludes cycles
of lengths \(4,8,16\).

Take thirteen consecutive vertices on a Hamiltonian cycle. They form a
12-edge path. Any chord between nonconsecutive vertices of this path would,
together with the intervening path segment, form a cycle of length at most
\(13\), contradicting the girth. Hence this path is induced.

The preceding observation shows that every connected cubic graph satisfies
`C004`–`C006`; `L002` holds because every edge has degree-\(3\) endpoints and
there are no vertices of degree above \(3\). The induced path is the structural
conclusion supplied by `C007` for a counterexample. Therefore \(G\) has all the
asserted properties but no \(C_{16}\). \(\square\)

This lemma refutes the proposed implication
\[
  \{\text{minimality conclusions, cubic domination, induced }P_{13},
       \text{ no }C_4,C_8\}
  \Longrightarrow C_{16}.
\]
It does not refute the Erdős–Gyárfás conjecture: the constructed graph may have
a longer power-of-two cycle, and `L007` makes no assertion about \(C_{32}\),
\(C_{64}\), and so on.

### `C010` — Exact result in the smallest five-hub completion family

`E003` exhaustively considered cubic graphs on vertices
\(\{0,\ldots,17\}\) with a specified induced \(P_{13}\). The residual degree
of the path into the other five vertices is \(2+11+2=15\), exactly their total
cubic degree, so those five vertices must be independent. Equivalently:

- \(0,\ldots,12\) induce \(P_{13}\);
- \(13,\ldots,17\) are independent;
- every vertex is cubic.

There is no order-\(18\) cubic graph containing an induced \(P_{13}\) while
avoiding both \(C_4\) and \(C_8\). This is a tested finite result, not part of
the proof of `L007`.

## Failure analysis

The first decisive failure is quantifier-level: cubic domination need not
produce new attachments to the induced path. If the path vertices are cubic,
their path neighbors already witness domination. More strongly, `L007` gives
a complete cubic graph satisfying every structural conclusion used by the
route while avoiding \(C_4,C_8,C_{16}\).

Consequently, a finite classification using only those local restrictions
cannot force \(C_{16}\). Adding the absence of all longer power-of-two cycles
would simply restore the full counterexample hypothesis and would not by itself
explain a noncircular forcing step.

## Salvageable results

- `L007` is a reusable separation example for any proposed local route.
- `C010` shows that the most compressed five-hub cubic completion fails for a
  different reason: it already forces \(C_4\) or \(C_8\).
- Any replacement for this route must use a genuinely global restriction not
  shared by arbitrary connected cubic graphs of large girth.

## Exit state

- Status: completed
- Promoted records: imported existence theorem `C009`, proved limitation
  `L007`, tested finite result `C010`
- Next action: identify a nonlocal constraint on a minimal counterexample and
  stress-test it against the girth-\(17\) cubic family before trying to force a
  particular power-of-two length.
