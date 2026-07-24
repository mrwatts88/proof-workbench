# A009 — Non-abelian voltage sieve past the commutator cascade

- Date opened: 2026-07-23
- Problem: `P-002`
- Status: active
- Portfolio role: falsification-side tool-building, direct successor to
  `A008` (opened in the same session after A008's kill condition fired;
  authorized by the session's recorded pivot and the user's direction to
  continue immediately)

## Intended mechanism

`A008`/`L021` killed every abelian voltage group: commutator words are
voltage-invisible over abelian groups and land on power-of-two lengths.
The escape must therefore be non-abelian. But non-abelian is not enough:

- **Solvable groups re-admit the disease one level up.** If \(\Gamma'\)
  is abelian (metabelian \(\Gamma\)), double commutators
  \([[W_1,W_2],[W_3,W_4]]\) are voltage-trivial, and their lengths
  \(4(\lvert W_1\rvert+\lvert W_2\rvert+\lvert W_3\rvert+\lvert
  W_4\rvert)\) hit \(32\) with the same minimal pieces that gave the
  abelian kill at \(8\). Nesting the derived series doubles lengths at
  each level — iterated commutators are *perfectly tuned* to produce
  powers of two. Exponent laws add a second channel: if \(x^q=e\) in
  \(\Gamma\), the power-twisted commutator
  \(W_1^{q}W_2W_1^{-q}W_2^{-1}\) is voltage-trivial with length
  \(2(q\lvert W_1\rvert+\lvert W_2\rvert)\), adjustable to a power of
  two by choosing \(\lvert W_2\rvert\).
- **Feit–Thompson closes the odd-order door.** Every odd-order group is
  solvable, so the "odd order avoids wrapped power cycles" framing from
  S009's first plan targeted groups that the cascade predictably kills.
  (The projection lemma never needed odd order; its proof is
  group-agnostic. Odd order was a convenience, not a requirement.)
- **The smallest group immune to the entire cascade is \(A_5\)**
  (order 60): perfect (\(A_5'=A_5\)), so no level of the derived series
  vanishes; its exponent is 30, and \(30\ell\) is never a power of two.
  The only \(2\)-power element orders are the involutions, and a walk
  \(W\) of length \(2^{k-1}\) carrying an involution voltage gives a
  voltage-trivial walk \(W^2\) of length \(2^k\) — but the
  per-assignment certificate below automatically covers this (it
  enumerates all walks of length \(2^k\), including squares).

Machinery: `L019` and `L020`, as proved in `A008`, hold for an arbitrary
finite voltage group — the proofs use only reversal antisymmetry
\(\alpha(\bar a)=\alpha(a)^{-1}\), simplicity of the derived graph, and
telescoping of the fibre coordinate, none of which is commutative. (The
gauge lemma's tree-reduction becomes
\(\beta(a)=c(\mathrm{tail}(a))^{-1}\alpha(a)\,c(\mathrm{head}(a))\);
the derived-graph isomorphism is \((u,g)\mapsto(u,g\,c(u))\); the
verification is line-by-line the A008 computation in multiplicative
notation.) What does *not* generalize is the abelian walk-class trick:
net voltage is now an ordered product, so there is no
assignment-independent finite class datum. The certificate becomes a
per-assignment dynamic program over states (arc, group element) — for
groups of order \(\le60\) and cycle-rank-2 bases this is a few hundred
thousand operations per assignment, and the assignment spaces
(\(21^2\), \(27^2\), \(60^2\)) are exhaustible outright.

## Entry assumptions

`D001`–`D004`; the A008 lemmas `L019`/`L020` with their group-agnostic
proofs; standard finite group theory. Feit–Thompson is used only for
route selection (skip odd-order groups), never inside a claim. The
solvable-cascade kill words above are stated as *testable predictions*
with proof sketches, not as proved claims; the E008 runs test them per
group, and only the outcomes enter the ledger.

## Targeted obligations

- `G012(b)`: first kill-or-survive data for non-abelian voltage groups.
- The negation of `C001` directly: a full-certificate survivor over
  \(A_5\) on a 2-vertex base is a 120-vertex counterexample candidate.

## Plan and decisive tests

1. Build the per-assignment group certificate in `E008`; anchor it
   bidirectionally against the `E007` hyperplane sieve on cyclic groups
   (the two engines must agree hit-for-hit at every assignment and every
   power length), against the Petersen lift (first hit exactly at 8),
   and against full group-axiom and structure checks (associativity,
   \(A_5\) perfectness, Heisenberg exponent 3).
2. Cascade probes (predictions registered in advance): over
   \(\mathbb{Z}_7\rtimes\mathbb{Z}_3\) (metabelian, order 21) every
   admissible assignment on every tested base should be certificate-dead
   by length \(\le32\); over the exponent-3 Heisenberg group (order 27)
   loop-bearing and theta bases should die by \(\le16\); \(K_4\) by
   \(\le32\). Confirmation validates the cascade theory cheaply;
   refutation would itself be news (a solvable survivor past the
   predicted wall).
3. The real test: exhaust \(A_5\) assignments on theta3, dumbbell,
   bouquet2 (lift orders 120, 120, 60), certificate through the largest
   power \(\le\) order (64, 64, 32).
4. Success trigger: a surviving assignment — then immediately: explicit
   lift construction, detector verification at 4/8/16, an independent
   second implementation of the walk check before any candidate claim,
   and the mandatory counterexample review path.
5. Kill trigger: \(A_5\) dies everywhere — then the obstruction is not
   the derived series and not an exponent law; extract the killing walk
   words from the DP, identify the mechanism, record it, and route the
   finding to `G012`/`G007` (it would be a new forcing pattern beyond
   `L021`).

## Deductions

- The L019/L020 group-agnosticism note above (a re-walk of the A008
  proofs in multiplicative notation, no new steps).
- **Predictions confirmed, with margin (E008, `C022`).** Every simple
  assignment over \(\mathbb{Z}_7\rtimes\mathbb{Z}_3\), both order-27
  groups, and \(A_5\), on every tested base, is certificate-dead by
  length **16** — at or before every pre-registered bound. Solvable
  deaths arrive even earlier than the double-commutator lengths because
  short element orders supply power-twisted kills first.
- **The \(A_5\) outcome identifies the real obstruction (provisional
  mechanism, exact data).** \(A_5\) is immune to the derived-series and
  exponent channels, yet all 3600 assignments on each cycle-rank-2 base
  die by 16. The mechanism matching the data is the **collision wall**:
  non-backtracking walks of length \(L\) from a vertex number
  \(\gtrsim3\cdot2^{L-1}\) against only \(\lvert\Gamma\rvert\) voltage
  values; once \(2^{L-1}\gg\lvert\Gamma\rvert\), same-voltage walk
  pairs exist and \(W\cdot\overline{W'}\) is an identity-voltage
  tailless non-backtracking closed walk of length \(2L\) (modulo
  first/last-arc diversity bookkeeping). Predicted death at
  \(2^k\approx2\log_2\lvert\Gamma\rvert\): observed 16 at
  \(\lvert\Gamma\rvert\in\{21,27,60\}\) everywhere. The lemma is *not*
  yet proved; it is the refined `G012` target.
- **Why no coset trick can dodge the wall (provisional).** If all arc
  voltages lay in a coset \(tH\) confining walk values, reverses lie in
  \(t^{-1}H\), and undirectedness forces \(t^{-1}H=tH\), i.e.
  \(t^2\in H\): any value confinement has period at most 2 in length.
  Power lengths are even, so parity is the only filter available and it
  never protects them. This closes the most obvious escape from the
  collision wall and explains why no group structure whatsoever showed
  an effect beyond setting which of \(\{4,8,16\}\) bites first.

## Failure analysis

Kill trigger 5 of the plan fired: \(A_5\) — the smallest group immune
to every structural kill channel — is certificate-dead by 16 on all
cycle-rank-2 bases, with zero survivors among all 3600 assignments per
base. The route's first wrong assumption, visible only in hindsight:
that group *structure* (commutators, exponents) was the binding
constraint. It never was; group *size* is. The certificate dies by
counting at \(\approx2\log_2\lvert\Gamma\rvert\), while power-freeness
of the lift needs survival to \(\approx n_B\lvert\Gamma\rvert\) — an
exponential gap no choice of group can cross. Structure only determines
which small power strikes first. The voltage-certificate program as a
counterexample generator is therefore finished for **all** finite
groups, not only the abelian ones `A008` killed.

## Salvageable results

- The collision-wall lemma as a sharply posed target (refined `G012`):
  "for every finite group, every voltage assignment on a min-degree-3
  base admits an identity-voltage tailless nb closed walk of length
  \(2^k\) for every \(2^k\ge C\log_2\lvert\Gamma\rvert+C_B\)" — the
  composition construction is explicit and only arc-diversity
  bookkeeping is open; a counterexample family would itself be a new
  value-confinement lever (and the coset argument above already rules
  out the obvious ones).
- The proof-side reading: minimum degree 3 forces identity-voltage
  closed walks at *every* even length past a logarithmic threshold —
  quantitative raw material for the `G007` interval-forcing route,
  where the open gap becomes walk-to-cycle injectivity, i.e. exactly
  the conjecture's hard core seen from a new angle.
- The verified group-table + per-assignment-DP machinery (E008),
  reusable for any future finite-group question in this dossier.
- The confirmed cascade predictions, which validate the L021-style word
  analysis as a reliable predictive tool.

## Exit state

- Status: closed (kill trigger 5 fired; verdict exhaustive on the
  tested bases and groups)
- Promoted records: `C022` to `CLAIMS.md`; `G012` refined in
  `OBLIGATIONS.md`; the E008 experiment record
- Next action: the session's proposed next step — attempt the
  collision-wall lemma as the closing theorem of the lift program (its
  proof also feeds `G007`), with the proof-side interval lemma as the
  standing alternative
