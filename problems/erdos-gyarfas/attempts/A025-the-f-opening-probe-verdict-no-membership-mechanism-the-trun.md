# A025 — The (F) opening probe verdict: no membership mechanism; the trunk bound and the S-saturation redirect

- Date opened: 2026-07-25
- Problem: `P-002`
- Status: closed (probe complete; verdict recorded; (F) re-aimed)
- Portfolio role: primary (Tier 1, `G015` case (5b), proof side;
  session `S024`)

## Intended mechanism

The recorded first move of the (F) program (`A023` T6 consuming
`L049`; `STATE.md`/`problem.json` after S023): build the
**power-collision realization tables** of the ten named objects — for
every \(C_8/C_{16}\), every trunk-split realization \((x,y,s)\) with
\(x,y\in S\) — and read them against the forced memberships of the
case-(5b) residual object (\(S\cap\mathbb P\ne\emptyset\),
\(S\cap(\mathbb P-1)\ne\emptyset\), \(S\cap(\mathbb P-2)=\emptyset\);
`A019` W1-T10 under (R)). Pre-registered decisive outcomes: **(a)** a
membership-patterned regularity across all ten objects names (F)'s
mechanism and starts its proof attempt; **(b)** its absence redirects
(F) toward window/order arithmetic. Binding calibration (`A021`
discipline): any proposed mechanism must fail on Petersen\(-e\) and
the order-14 exemplar unless it consumes power-freeness or minimality.

## Entry assumptions

Statement 0.1 verbatim. Consumed at recorded strength: `L049` (T5 +
trunk-identical arc form), `L048`(iii) unconditional
(\(\mathrm{Spec}(H)=T_1\), \(\mathrm{Spec}(B)=T_1\cup(S+2)\), every
\(T_1\) element a trunk-split pair value), `L042` (the residual
object's forced properties), `L046` (2-connected below 36), the
`C036`–`C044` search floors, and the ten objects' identities
(`E013`/`E021`/`E022` data, re-verified field by field in `E025`).
The probe itself drops power-freeness — its objects are blocked by
construction; it measures how the collisions the residual object must
avoid are actually realized.

## Targeted obligations

- `G015`: exclude case (5b) — (F) is its entire proof side below
  order 36 (`L048`(iii) + `L046`).
- `G013`(a): structure theory for the tight-1-atom question.

## Plan and decisive tests

1. Anchors first (standing rule): `E021`'s 45-check suite through the
   import, plus new-code controls including a weaving pair the
   trunk-split classifier must reject. Outcome: 45/45 + 14/14 under
   both interpreters (`E025`).
2. The tables, with every recorded reference field asserted and two
   pre-registered **soundness alarms** (a power cycle with no
   witnessing pair, or with no trunk-split realization, would
   contradict the reviewed `L049`). Outcome: tables built; neither
   alarm fired (604/604 power cycles have both).
3. The pattern verdict: nine per-cycle existential patterns fixed in
   code before the first table was built; universality across all ten
   objects = outcome (a).

## Deductions

Notation as in `A023`/`A024`; \(n=|V(H)|\), \(L=\ell(C)\); classes
\(\mathbb P=\{4,8,16,32,64\}\), \(\mathbb P-1\), \(\mathbb P-2\).

### T1 (the probe verdict: outcome (b)) — computed (`E025`, exhaustive for the ten objects)

**No membership-patterned regularity exists.** Over the 604 power
cycles and their complete trunk-split tables (1,971 realizations):

1. None of the nine pre-registered patterns is universal. The
   sharpest failures: `has_P` (a power-length path participates in
   some realization) fails on 270 of the 594 profile-object
   \(C_{16}\)s; `has_PP` fails on 556; `has_forced_pair` fails on
   400.
2. Even the weakest disjunction — some realization touches **any**
   membership class — fails: **30 cycles across six profile objects
   are membership-blind** (entire trunk-split sets in exactly three
   shapes: \(\{(5,13,1)\}\), \(\{(9,11,2),(10,10,2)\}\),
   \(\{(5,11,0)\}\)).
3. The calibration contrast: both calibration objects are 100% on
   `has_PP` — every \(C_8\) of Petersen\(-e\) and the order-14
   exemplar is realized by two power-length paths — while the profile
   objects sit at 1–8 of 37–112. "Forced power paths collide" is a
   small-order artifact, correctly killed by the frontier half of the
   calibration discipline.

**Consequence for (F).** An (F) mechanism of the form "the forced
\(\mathbb P/\mathbb P-1/\mathbb P-2\) memberships force the collision
arithmetically" has no empirical basis: at the frontier the collisions
are realized through arithmetically generic length pairs, and some
only through membership-blind ones. This extends the two kill theorems
(`C037`: congruence information caps at parity; `L045`: membership
arithmetic cannot exclude the chain case) by an empirical third leg:
membership arithmetic does not even *organize* the realization shapes.
Pre-registered branch **(b)** is taken: (F) redirects to window/order
arithmetic (T3–T5 below).

### T2 (the trunk bound) — proved

**Claim.** Let \((H,a,b)\) be any two-terminal pair, \(n=|V(H)|\), and
let \(C\) be a cycle of \(H\) realized by a trunk-split pair with
shape \((x,y,s\,|\,a_1,a_2\,|\,t_a,t_b)\) (`L049` arc form). Then
\[ s \;=\; t_a+t_b \;\le\; n-L, \qquad\text{hence}\qquad
   x+y \;=\; L+2s \;\le\; 2n-L , \]
and \(\max(x,y)\le s+L-1\le n-1\).

*Proof.* \(T_a\) is a path from \(a\) to \(u\) with
\(V(T_a)\cap V(C)=\{u\}\): its \(t_a\) non-\(u\) vertices lie off
\(C\). Likewise \(T_b\)'s \(t_b\) non-\(v\) vertices, and
\(V(T_a)\cap V(T_b)=\emptyset\), so \(H\) has at least \(t_a+t_b\)
vertices outside \(V(C)\): \(t_a+t_b\le n-|V(C)|=n-L\). The rest is
\(x+y=2s+L\) (`L049`) and \(x=s+a_x\le s+L-1\) (arcs have \(\ge1\)
edge). ∎

**Tightness (computed, `E025`).** All ten objects realize \(s=n-L\)
exactly (2/6/3/4 for orders 10/14/19/20). The pooled \(C_{16}\)
\(s\)-distribution is \(\{0{:}111,\ 1{:}403,\ 2{:}763,\ 3{:}482,\
4{:}182\}\).

**Reading.** This is the first piece of the window arithmetic (F) now
lives in: in the window \([18,35]\), a \(C_{16}\) trunk-split collision
must have \(s\le n-16\le 19\) and both path lengths in
\([\,\min S,\ n-1\,]\) with \(x+y=16+2s\) — for the residual object
the *entire* freedom of the collision system is confined by order.
(For \(C_{32}\): \(s\le n-32\), so at orders \(\le33\) only \(s\le1\)
shapes exist at all.)

### T3 (frontier saturation) — computed (`E025`, the eight profile objects)

1. **Spectra**: every profile object's cycle spectrum is exactly
   \([3,n]\setminus\{4,8\}\) — the full interval with only the two
   forbidden powers missing. Suppressing 4 and 8 in this class at
   orders 19–20 does not thin the spectrum anywhere else, and 16 is
   present with multiplicity 37–112.
2. **Through-sets**: every profile object's \(S\) contains the full
   interval \([6,n-1]\) (seven of eight are gap-free intervals
   \([5,n-1]\) or \([6,19]\); N20p14-A is \(\{3\}\cup[6,19]\)) — in
   particular **\(6,14\in S\) for all eight**, the recorded
   \(S\ni\{6,14\}\) double blocking. Both calibration objects gap
   \(S\) exactly at 6 (P10: \(\{4,5,7,8\}\); N14:
   \([3,13]\setminus\{6\}\)) — the \(\mathbb P-2\) dodge is realized
   at orders 10 and 14 and has never been seen at 19–21.
3. The trunk-split skeleton is thin (2.6–4.0 realizations per cycle
   on average vs 76–138 witnessing pairs on the profile objects), and
   every arc split \((1,15)\dots(8,8)\) occurs, short-arc reroutes
   dominating.

### T4 (the redirect: two named sub-targets replace the membership mechanism) — analysis; both open

The residual object must simultaneously achieve
\(S\cap\{2,6,14,30\}=\emptyset\) (else the closure \(B=H+u\) has a
power cycle via \(\mathrm{Spec}(B)\supseteq S+2\)) and
\(16,32\notin\mathrm{Spec}(H)=T_1\) (with 4, 8 excluded by
\(C_4/C_8\)-freeness). Reading T1+T3 against this, (F) splits into two
falsifiable sub-targets, either of which closes its order slice:

> **(F-S) (open target, speculation).** In the window: every
> vertex-taut (5b)-profile pair \((H,a,b)\) with
> \(4,8\notin\mathrm{Spec}(H)\) at order \(18\le n\le35\) has
> \(S\cap\{6,14\}\ne\emptyset\).

> **(F-T) (open target, speculation).** In the window: every such
> pair has \(16\in\mathrm{Spec}(H)\) (resp. \(32\) where applicable).

(F-S) \(\Rightarrow\) the closure is power-blocked; (F-T)
\(\Rightarrow\) \(H\) itself is. Either statement, proved on
\([18,35]\), closes case (5b) there (with `L046` covering the chain
side); their disjunction is what (F) needs. Evidence: all eight
profile objects satisfy **both** conclusions (that is exactly the
double blocking); the searches through order 21 have produced no
member violating either.

**Calibration (binding, `A021` discipline).** Both sub-targets are
order-windowed, and both **fail off-window on the calibration pair**
by construction: Petersen\(-e\) (order 10) and the order-14 exemplar
have \(S\cap\{6,14\}=\emptyset\), and the exemplar is
\(C_8\)-blocked, not \(C_{16}\)-blocked. So neither sub-target can be
proved by an argument insensitive to order — the window hypothesis is
doing necessary work, which is the consumption pattern the discipline
demands (here the consumed resource is the order window rather than
power-freeness directly; power-freeness enters as the
\(4,8\notin\mathrm{Spec}\) hypothesis). Any proposed proof of (F-S)
or (F-T) must be checked to fail at orders 10 and 14 on these two
objects.

**Why this genre survives the kill theorems.** (F-S)/(F-T) are
**realization-forcing** statements about \(S\) and
\(\mathrm{Spec}=T_1\) — the genre `C037`/`L045` left alive — and they
do not run through membership-class collision arithmetic, which T1
killed empirically. The candidate mechanism is **interpolation /
saturation**: tautness + the profile degrees + \(\{C_4,C_8\}\)-freeness
appear to force interval-saturated through-sets at window orders (T3;
6 and 14 land in \(S\) because *everything* in \([6,n-1]\) does), and
the length-16 slot catches the compressed cycle mass (T3.1). What a
proof needs, named: a lower-bound mechanism for through-path length
sets in taut windowed pairs (a path-interpolation lemma: under which
hypotheses is \(S\) forced to contain \([c,n-1]\) for some
\(c\le14\)?), or a cycle-space compression argument for
\(16\in\mathrm{Spec}\). Both are new tools; neither exists in the
dossier yet. The block chain + trunk-split normal form (`L049`) and
the trunk bound (T2) are the available raw material.

### T5 (the falsifiable first move of the redirect) — recorded as next action

**The S-gap census at the window bottom.** The \(\{C_4,C_8\}\)-free
two-degree-2 class is on disk at orders 18–20 (`E022/data`
`class_n18/19/20_part*` — order 20 is SAVE_LIMIT-sampled, 18/19
complete) and order 21 is being generated (`E024`, running). For
every member: compute \(S\) and record the gap structure at 6 and 14
(and tautness for the members with a gap). Outcomes: **(i)** if no
member at 18–20 has \(S\cap\{6,14\}=\emptyset\) while vertex-taut,
(F-S) survives its first kill test exactly where the residual object
would live, and the census's gap-vs-order curve (compared with orders
10–16, where gapped members exist — the calibration pair among them)
measures the saturation mechanism directly; **(ii)** a vertex-taut
member with \(S\cap\{6,14\}=\emptyset\) **kills (F-S) as stated**,
becomes calibration object #3 (it realizes the \(\mathbb P-2\) dodge
in-window), and leaves (F-T) as the surviving sub-target — it is
\(C_{16}\)-blocked (else it would be a \(\mathcal G\)-member, a
standing pivot trigger); **(iii)** the same scan re-reads the class
for (F-T) for free (every member's \(C_{16}\) status is decided by
the generator's own certificates at collection time — re-verify on
the gapped members). Cost: path-set enumeration per member,
\(\approx\)183k graphs at 18–19 + the 572k order-20 sample; hours
under PyPy, parallelizable, and safe to run after `E024` finishes or
throttled alongside it.

## Failure analysis

No route died unexpectedly: the probe was a pre-registered two-outcome
instrument and outcome (b) occurred. What *is* dead, with the reason
preserved: **the membership-collision form of (F)** — the forced
memberships do not organize the collision realizations (T1), so no
proof attempt of that form should be started. The A023 evidence
reading that motivated it ("the class data plus T1 say the path system
does always achieve the 8-collision") survives, but the *mechanism* is
saturation/compression, not membership arithmetic. Residual risks,
stated plainly: (F-S)/(F-T) are conjectures with eight data points
plus emptiness evidence; the saturation mechanism (T4) has no proof
step yet; and all realization evidence is at orders \(\le20\) while
the window runs to 35 — the upper window (22–35), where spectra can
in principle thin, is untouched by any table.

## Salvageable results

1. **T1** — the probe verdict (outcome (b)) with the complete tables
   (`E025/data/realization_tables.json`): the membership-collision
   mechanism is dead as an (F) route; 30 named membership-blind
   cycles.
2. **T2** — the trunk bound \(s\le n-L\), \(x+y\le2n-L\) (proved,
   tight on all ten objects): the base inequality of the window
   arithmetic (offered to the ledger).
3. **T3** — frontier saturation: spectra exactly
   \([3,n]\setminus\{4,8\}\), \(S\supseteq[6,n-1]\) with \(6,14\in S\)
   on all eight profile objects; the calibration pair's gap-at-6 as
   the only known \(\mathbb P-2\) dodges (orders 10, 14).
4. **T4** — the redirect: (F) = (F-S) ∨ (F-T), both order-windowed,
   both calibrated, with the saturation/interpolation mechanism and
   its missing tools named.
5. **T5** — the S-gap census as the next falsifiable move, with its
   three outcomes pre-registered.

## Exit state

- Status: closed (probe complete and read; the (F) program re-aimed
  at (F-S)/(F-T) with the S-gap census as the first move)
- Promoted records: experiment `E025` (tables + pattern verdicts);
  deduction rows offered to the ledger: T1/T3 (computational
  observation), T2 (proved lemma), T4 (program reframing, conjecture
  strength).
- Next action: the S-gap census at the window bottom (T5), then the
  saturation-mechanism proof attempt against whichever sub-target
  survives.
