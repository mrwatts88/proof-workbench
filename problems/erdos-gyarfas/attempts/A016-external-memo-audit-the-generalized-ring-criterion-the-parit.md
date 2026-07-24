# A016 — External memo audit: the generalized ring criterion, the parity channel, and the program ceiling

- Date opened: 2026-07-24
- Problem: `P-002`
- Status: active
- Portfolio role: reframing (audit of external strategic input)

## Intended mechanism

During S015 the user supplied a strategy memo produced by a different AI
agent (`references/external-agent-strategy-memo-2026-07-24.md`). Its
headline: the dossier's 2-atom definition (pinch, \(s_{\max}<2s_{\min}\))
captures only one sufficient instance of the ring disproof mechanism —
`A011` R1's exact spectrum formula supports a wider criterion (any
\(L\)-fold sumset of the through-set avoiding all powers of two), with
parity/congruence instances the pinched frame cannot see. This attempt
audits every mathematical claim in the memo against the records and
first-principles checks, records the verified core as `L034`, corrects
the dossier's overstated framing, itemizes what survives of the current
program, and files the memo's strategy paths into the portfolio without
dropping any existing thread (user's standing instruction).

An external memo is speculative input: nothing here is imported on its
authority. Every verdict below is re-derived; literature items are
unverified leads pending `G014`.

## Entry assumptions

Definitions D-A1–D-A5 and R1–R5 of `A011` at their proved strength;
`L022`, `C023`, `C027` for the finite coverage statements. No new
assumptions; statement 0.1 unchanged.

## Targeted obligations

- `G013`: the disproof-interface definition itself (the audited gap).
- `G014` (new): source audit of the memo's literature and census leads.

## Audit of the memo's claims

**M1 — "R1 proves the ring spectrum exactly; pinching is only one
sufficient way to dodge the sumset." VERIFIED.** `A011` R1 is proved for
every (D)-gadget and every \(L\ge3\): \(R_L\) is simple with
\(\delta\ge3\) and \(\mathrm{Spec}(R_L)=\mathrm{Spec}(H)\cup\Sigma_L\);
the ⊆ direction of the proof shows every ring cycle not inside one copy
has length an \(L\)-term sum over \(S\), and the ⊇ direction's argument
realizes every such sum (consecutive witness paths share exactly their
gateway). Nothing in R1 uses the pinch; R2 (dyadic placement) is where
pinching enters, purely to *exhibit* a power-free window. Hence the
generalized criterion (recorded as `L034`):

> If \((H,a,b)\) is a power-free (D)-gadget and for some \(L\ge3\) the
> \(L\)-fold sumset \(\{s_1+\dots+s_L: s_i\in S\}\) contains no power of
> two, then \(R_L(H,a,b)\) is a counterexample to 0.1.

**M2 — the three sumset instances. VERIFIED (two-line arithmetic
each).** (i) \(S\) all odd, \(L\) odd: every sum is odd; powers of two
\(\ge4\) are even (sums are \(\ge 3s_{\min}\ge3>2\)). (ii)
\(\gcd(S)\) divisible by an odd prime \(p\): every sum is, and no power
of two is; every \(L\ge3\) works. (iii) \(S\subseteq2+4\mathbb Z\),
\(L\) odd: sums \(\equiv2L\equiv2\pmod4\), while powers of two \(\ge4\)
are \(\equiv0\pmod4\) and sums exceed 2. The memo's example gadget
shapes check out: \(S=\{3,7\}\) has
\(\Sigma_3=\{9,13,17,21\}\) (power-free), is excluded from D-A3 by
\(7\ge2\cdot3\), and is permitted by `L030` (which forces only
\(s_{\max}\ge6\) at \(s_{\min}=3\); note \(6\) is even, so an all-odd
band-3 gadget in fact needs \(7\in S\) — `L030` already forces the
\(\{3,7\}\)-shape on the taut parity ladder). \(S=\{2,6\}\) has
\(\Sigma_3=\{6,10,14,18\}\) (power-free) and escapes `L028`
(\(S\subseteq\{2,3\}\) only). Both would be genuine disproofs if
realized power-free.

**M3 — "the corrected necessary condition." VERIFIED with a precision
repair.** Contrapositive of `L034`: if 0.1 is true, then for every
power-free (D)-gadget and **every** \(L\ge3\), the \(L\)-fold sumset of
\(S\) contains a power of two. Instances: \(S\) is not all-odd (some
through-path has even length); \(\gcd(S)\) is a power of 2;
\(S\not\subseteq2+4\mathbb Z\). The memo's "equivalently: no bipartite
graph with min degree \(\ge3\) except at two vertices in opposite parts
is power-free" is the canonical *instance*, not an equivalence: a
bipartite (D)-gadget with terminals in opposite parts has all through
lengths odd, but all-odd \(S\) does not force bipartiteness. Also note
the parity constraint on bands: all-odd \(S\) forces \(d(a,b)\) odd, so
the taut parity ladder lives at odd bands 3, 5, 7, … — disjoint from
the band-4 pencil battlefield of `L033`.

**M4 — "the block catalogue at \(e\le0\) is a catalogue of the wrong
class." OVERSTATED; the correct statement:** the pinched channel is one
genuine ring channel among several, and `L026`–`L033` close or reduce
*that channel* exactly as recorded — no recorded row is false, and
`L032`'s equivalence about taut 2-atoms *as defined* stands. What dies
is the **exclusivity framing**: `A011` R5's title ("the sharp
walk-to-cycle form"), `G013`'s "closes the entire ring/assembly
disproof channel", and `PROOF.md`'s "the sharp conditional form of
walk-to-cycle transfer" all overstated pinching as *the* criterion.
The full assembly interface is: 1-atoms, plus power-free (D)-gadgets
with any power-dodging sumset channel (pinch, parity, gcd, mod-4, or
any other \(L\)-fold avoidance). Each channel taut-relativizes
separately through `L027` (the lobe decomposition is channel-agnostic),
but the pendant/block machinery of `L031`/`L032` is pinch-specific
(excess arithmetic; note the pendant shift \(S\mapsto1+S\) *flips
parity*, so the parity channel needs its own reduction theory —
untouched).

**M5 — "E010/E012/E013 never looked for it." TRUE AT THE CATALOGUE
LAYER, but the frontier is unaffected: VERIFIED MITIGATION.** `C027` is
stream-level: every connected \(C_4\)-free graph with \(\le2\) sub-cubic
vertices and \(\ge\lceil(3n-4)/2\rceil\) edges at orders \(\le15\)
contains a \(C_8\). Every (D)-gadget lies in that class (degree sum
\(\ge3n-3\)), so **no power-free (D)-gadget of any through-set profile
exists through order 15** — the parity/gcd/mod-4 channels are exactly as
empty as the pinched one there; gadgets with both terminal degrees
\(\ge3\) are excluded through order 18 by `L022`/`C023` as recorded in
`C027`'s row. What the taut catalogues (`E011`–`E013`) never scanned is
the *shape* data for the new channels (e.g. all-odd taut cores below
the power-free frontier, the analogue of the five equality blocks); the
banded scanners cannot see them (a \(\{3,7\}\)-gadget is rejected as
"long" at ceiling 6), so a dedicated odd-\(S\) scan mode is needed
(abort on the first even through-path — an efficient dual of the
banded abort).

**M6 — "the program's ceiling." CORRECT and now explicit.** By `L026`,
full spread-doubling is equivalent to 0.1 only through the *non-taut*
rungs (hiding two counterexample copies), which are conjecture-complete;
so complete success on both live sub-questions ("no taut 2-atom" + "no
1-atom") closes the assembly channel and delivers the cubic reduction
(`L029`) — it does **not** prove 0.1. Of the two, only the 1-atom
question has direct proof-side yield. This was implicit in
`L026`/`L029`'s notes; it is now stated as the program ceiling in
`G013`. The same ceiling applies to the new channels (an all-odd
non-taut rung is also conjecture-complete: two hidden copies give
\(S=\{1\}\), all odd).

**M7 — the S012/S013 "surprise" diagnosis. PLAUSIBLE, RECORDED AS
INTERPRETATION.** The observation that pinching is strong enough that
\(C_4\)-freeness alone kept closing rungs (against S012/S013's
predictions) is consistent with the record; the inference "the parity
channel is where the power spectrum must actually fight" is strategy
judgment, not a theorem. It is, however, corroborated by a fact the
memo did not have: `L033`'s band-4 pencil dichotomy needed no power
input either — the first genuinely power-specific fight has not yet
been forced anywhere in the pinched ladder.

**M8 — search engineering. RECORDED.** Filtering geng's \(C_4\)-free
stream cannot reach orders 19+ (graphs) or 17+ (gadget classes at
acceptable cost); a dedicated \(\{C_4,C_8\}\)-free generator (canonical
construction path with incremental \(C_8\) rejection, à la Markström
2004) or SAT-modulo-symmetries is the right instrument for the next
frontier push. This threads with the deferred order-16/17 legs.

**M9 — literature and census leads. UNVERIFIED; filed as `G014`.**
Chen–Saito (min degree 3 forces a cycle of length \(\equiv0\bmod3\));
Nowbandegani–Esfandiari (bipartite counterexamples have \(\ge32\)
vertices; also the memo's "verified externally to 31" for bipartite
EGC); Heckman–Krakovski (3-connected cubic planar EGC); Shauger and
Daniel–Shauger (Erdős–Gyárfás for classes excluding large stars);
the cubic vertex-transitive census (\(\le1280\) vertices, Zenodo); cubic
girth-\(\ge9\) censuses (58–64 vertices); snark and cage lists (House of
Graphs). None may be cited in a proof step until audited with precise
statements and sources. The memo's Path-1 window logic (bipartite
gadgets of order \(\le31\) must have a Mersenne through-length, because
otherwise \(H+ab\) would be a bipartite counterexample of order
\(\le31\), contradicting the \(\ge32\) bound; hence the live target is
\(S\ni3,7,\) or \(15\)) is arithmetically sound (\(1+s=2^k\iff s\)
Mersenne; \(a,b\) in opposite parts keeps \(H+ab\) bipartite and lifts
both terminal degrees) but is **conditional on the unverified
\(\ge32\) import**.

**M10 — the 3-connectivity sample. VERIFIED as a sketch.** In a
3-connected graph, for any edge \(uv\), \(G-uv\) is 2-connected, so
Menger gives two internally disjoint \(u\)–\(v\) paths of lengths
\(q,r\ge2\); with the edge these give cycles \(q+1\), \(r+1\), \(q+r\).
If every cycle length were \(\equiv0\pmod m\) then \(q\equiv
r\equiv-1\) and \(q+r\equiv-2\equiv0\), so \(m\mid2\): no 3-connected
graph confines its cycle spectrum to the multiples of an odd
\(m\ge3\). Provisional (promotable after a written-up proof pass);
the memo's two 3-connectivity targets are filed in the portfolio.

**M11 — "the voltage-lift retirement is certificate-level only."
ALREADY RECORDED.** This is exactly the recorded caveat on
`L024`/`C020`–`C022` (per-base corollary, certificate-level, truth-level
coverage six bases / cyclic groups / orders 12–30). No change needed.

## Plan and decisive tests

Recorded for the next session's strategy audit (nothing executed now,
per the user's instruction):

1. **Parity-channel calibration** (memo Path 1, first move): an
   odd-\(S\) taut scan over the existing stream at orders \(\le15\)
   (new scan mode: abort on any even through-path; the banded E013
   scanners cannot do this). Outcome either exhibits all-odd taut
   cores below the power-free frontier (the parity analogue of the
   five equality blocks — reshapes the program) or shows the taut
   parity channel is shape-empty like the pinched one.
2. **Bipartite gadget hunt** (Path 1 proper): genbg-generated bipartite
   near-cubic two-terminal gadgets, opposite parts, girth \(\ge6\), no
   \(C_8/C_{16}\), orders 16–24; any power-free hit disproves 0.1 by a
   3-ring (`L034`).
3. **Cubic census extension** (Path 2): reproduce Markström 26/28 as
   anchors, then order 30 — where any \(\{C_4,C_8,C_{16}\}\)-free cubic
   graph is a counterexample outright; `L029` makes cubic decisive
   modulo 1-atoms.
4. **Census mining** (Path 3): power-length tests over existing cubic
   vertex-transitive / girth-\(\ge9\) / snark / cage lists (imports to
   be verified first, `G014`).
5. **Bipartite EGC** (Path 4, proof side): the `L030`/`L033` collapse
   machinery with parity leverage; would close the parity channel's
   bipartite instance as a theorem.
6. **Carr 4/7 strengthening** (Path 5, proof side) and
   **3-connectivity** (Path 6: 2-cut chain decomposition; 3-connected
   cubic EGC beyond planar; the mod-\(m\) sample as a first lemma).
7. Kill tests: (1) is killed by an empty calibration (then the parity
   channel's *taut* shape data is as empty as the pinched one and the
   channel's priority drops accordingly); (2)–(4) are killed/decided by
   their searches; the existing pencil endgame and order-16-derived
   threads (S015 first half) remain live in parallel — no thread is
   retired by this audit.

## Failure analysis

Not applicable as failure: the audit *confirmed* the memo's core and
bounded its overstatements. The dossier-side failure it exposes is a
framing error, not a false theorem: three records presented the pinch
condition as the criterion ("sharp", "entire channel") when it is one
channel. Root cause: D-A3 was defined from R2's sufficient condition
rather than from R1's criterion, and no later session re-derived the
criterion from R1. The repair is `L034` plus corrective notes; every
proved row stands.

## Salvageable results

Everything: `L034` (the generalized criterion and its instances);
the corrected necessary-condition family (M3); the ceiling statement
(M6); the odd-band observation (parity ladder at bands 3, 5, 7 —
disjoint from the `L033` band-4 battlefield, so both programs proceed
without collision); the search-engineering and literature leads
(`G014`); the six-path portfolio, carried alongside all pre-existing
threads.

## Exit state

- Status: active (audit complete; execution deferred to the next
  session's strategy audit per user instruction)
- Promoted records: `L034`; corrective notes on `L025`/`G013`/PROOF
  framing; `G014` opened; memo preserved verbatim in `references/`.
- Next action: fold into the S015 close; the next session audits the
  expanded portfolio with the parity-channel calibration as the
  cheapest decisive first move alongside the inherited pencil-endgame
  thread.
