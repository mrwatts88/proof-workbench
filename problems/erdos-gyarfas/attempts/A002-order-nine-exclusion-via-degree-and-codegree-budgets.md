# A002 — Order-nine exclusion via degree and codegree budgets

- Date opened: 2026-07-23
- Problem: `P-002`
- Status: active

## Intended mechanism

Combine the \(C_4\)-free common-neighbor budget from `A001/L003` with the
independence of high-degree vertices in an edge-minimal counterexample
(`A001/L002`). At order \(9\), the budget leaves only two degree sequences,
both rigid enough to exclude directly.

## Entry assumptions

- `D001`–`D004`.
- `L002` and the codegree inequality proved in `A001/L003`.
- For contradiction, an edge-minimal counterexample \(G\) of order \(9\).

## Targeted obligations

- `G003`: strengthen the finite structural frontier.
- `G005`: begin the exact \(C_4\)-free analysis at order \(9\).

## Plan and decisive tests

1. List every degree sequence allowed by the codegree inequality and the
   handshake parity condition.
2. Test the unique-degree-\(4\) case by expanding one neighborhood.
3. Test the three-degree-\(4\) case using the independent high-degree set.

## Deductions

### `L005` — Every counterexample has at least ten vertices

**Proof.** By `L003`, it remains only to exclude order \(9\). Choose an
edge-minimal counterexample \(G\) of that order. It has no \(4\)-cycle, so
\[
  \sum_{v\in V(G)}\binom{d(v)}2\le\binom92=36. \tag{1}
\]
A degree at least \(6\) would contribute at least
\(\binom62+8\binom32=39\), so every degree is \(3,4,\) or \(5\). Let \(t_i\)
be the number of degree-\(i\) vertices. Relative to nine degree-\(3\)
vertices, (1) gives
\[
  3t_4+7t_5\le9. \tag{2}
\]
The degree sum \(27+t_4+2t_5\) is even, so \(t_4\) is odd. If \(t_5\ge1\),
(2) forces \(t_4=0\), contradicting parity. Hence \(t_5=0\), and (2) and
parity leave exactly
\[
  (4,3^8)\quad\text{or}\quad(4^3,3^6). \tag{3}
\]

First suppose the degree sequence is \((4,3^8)\), and let \(v\) be the
degree-\(4\) vertex. The graph induced by its four neighbors has maximum
degree at most \(1\), since a two-edge path there would form a \(4\)-cycle
through \(v\). Let it contain \(e\) edges, so \(e\le2\). The four neighbors,
all cubic, require \(8-2e\) edges to the remaining four vertices. No remaining
vertex can meet two of them, again because that would form a \(4\)-cycle
through \(v\). Thus \(8-2e\le4\), forcing \(e=2\). Every remaining vertex
therefore has exactly one neighbor in \(N(v)\) and, being cubic, exactly two
neighbors among the other remaining vertices. Those four vertices induce a
2-regular simple graph, necessarily a \(4\)-cycle: a contradiction.

Now suppose the sequence is \((4^3,3^6)\). Let \(A\) be the three
degree-\(4\) vertices and \(B\) the six cubic vertices. By `L002`, \(A\) is
independent, so there are \(12\) edges from \(A\) to \(B\). For \(x\in B\),
write \(r_x=|N(x)\cap A|\). Any pair of vertices in \(A\) has at most one
common neighbor, hence
\[
  \sum_{x\in B}\binom{r_x}{2}\le\binom32=3. \tag{4}
\]
But \(\binom r2\ge r-1\) for every integer \(r\ge0\), and therefore
\[
  \sum_{x\in B}\binom{r_x}{2}
  \ge\sum_{x\in B}(r_x-1)=12-6=6,
\]
contradicting (4). Both sequences in (3) are impossible. \(\square\)

## Failure analysis

The method succeeds at order \(9\), but its raw degree budget admits seven
sequences at order \(10\). Additional neighborhood and cycle structure is
needed there.

## Salvageable results

- `L005` raises the proved counterexample lower bound from \(9\) to \(10\).
- The inequality
  \[
    \sum_{x\in L}\binom{r_x}{2}\le\binom{|H|}{2}
  \]
  is useful whenever the high-degree set \(H\) is independent and \(L\) is
  its complement.

## Exit state

- Status: completed
- Promoted records: `L005` in `CLAIMS.md`
- Next action: classify the seven feasible degree patterns at order \(10\).
