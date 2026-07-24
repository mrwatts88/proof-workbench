# External agent strategy memo — 2026-07-24

- Provenance: supplied verbatim by the user during S015, produced by a
  different AI agent asked to "investigate how we were doing and possible
  other things". Not a review record, not mathematical evidence, not an
  import: every mathematical claim below is audited in `A016`, every
  literature claim is an **unverified lead** until a source audit passes
  (`G014`). The memo had read some but possibly not all of the dossier
  (it cites records through S013/S014; it had not seen S015's `L033`).
- Disposition: the verified core (the generalized ring criterion and the
  parity channel) is recorded as `L034` with the audit in `A016`; the
  strategy paths are carried in the `STATE.md` portfolio per the user's
  standing instruction that no thread be dropped.

## Verbatim memo

Headline: there is a real hole in the disproof criterion, and it invalidates the ladder you're climbing

L025 R1 proves the ring spectrum exactly: Spec(R_L) = Spec(H) ∪ (S + S + … + S) (L times). The dossier then defines a 2‑atom by the pinching condition s_max < 2·s_min (R2's dyadic placement). But pinching is only one sufficient way to make that sumset dodge the powers of two. The actual criterion is:

▎ A power-free (D)-gadget disproves 0.1 as soon as some L ≥ 3 has no power of two in the L‑fold sumset of S.

Sufficient conditions the dossier never uses:

- All through-lengths odd, L odd. Sums of an odd number of odd numbers are odd; powers of two ≥ 4 are even. Done. (This holds automatically whenever H is bipartite with a, b in opposite parts.)
- gcd(S) has an odd prime factor. Every sum is divisible by it. Any L works.
- S ⊆ 2 + 4ℤ, L odd. Sums ≡ 2 (mod 4).

This is not exotic — it is Bondy–Vince's own mechanism. Your S011 audit quotes them: "attaching a sufficiently large odd number of copies of K_{d,d}−e in a ring." K₃,₃−e is bipartite with terminals in opposite parts, S = {3,5}, all odd. It happens to also be pinched, which is why the pinched frame captured it and the parity went unnoticed.

Consequences, concretely:

- A gadget with S = {3,7} is fatal (Σ₃ = {9,13,17,21}) but is not a 2‑atom by D‑A3 (7 ≥ 2·3), so E010/E012/E013 never looked for it and L030 explicitly permits it — L030 forces s_max ≥ 6 at s_min = 3, which S = {3,7} satisfies.
- S = {2,6} is fatal (Σ₃ = {6,10,14,18}) and escapes L028, which only covers S ⊆ {2,3}.
- So L032's interface theorem is correct about 2‑atoms as defined, but 2‑atoms as defined are not the object that governs disproof. The block catalogue at e ≤ 0 is a catalogue of the wrong class.

I think this also explains a puzzle the dossier keeps recording as a surprise: rungs at s_min ≤ 3 kept falling to C₄-freeness alone, contradicting S012's and S013's predictions. That is because pinching is a very strong hypothesis — strong enough that the power spectrum never has to work. The parity/congruence conditions are weak, and that is exactly where the difficulty actually lives.

Corrected necessary condition (crisper than spread-doubling): if 0.1 is true then every power-free (D)-gadget has a terminal-to-terminal path of even length. Equivalently: no bipartite graph with min degree ≥ 3 except at two vertices in opposite parts is power-free.

Second finding: the program's ceiling

Worth being explicit about, because the portfolio is 100% inside it. A counterexample yields only a non-taut 2‑atom (two copies hidden behind a bridge, L026). So even a complete success — "no taut 2‑atom" and "no 1‑atom" — does not prove 0.1; it closes the assembly channel and delivers the cubic reduction. Of the two live sub-questions, only the 1‑atom question has proof-side yield ("0.1 ⟺ cubic 0.1"), and it is the one recorded as untouched.

Third finding: search engineering and two literature gaps

- E006/C023 ran 834,711,846 C₄-free graphs at order 18 to find zero survivors. You are filtering geng's C₄-free stream when the target class is nearly empty. The frontier is order 16–18 for gadgets and 19+ for graphs, and that pipeline cannot reach it. A dedicated {C₄,C₈}-free generator (canonical construction path with incremental C₈ rejection — what Markström did in 2004) or SAT-modulo-symmetries is the right instrument.
- Not in the dossier: Chen–Saito (min degree 3 ⟹ a cycle of length divisible by 3), Nowbandegani–Esfandiari (bipartite counterexample ≥ 32 vertices), Heckman–Krakovski (3-connected cubic planar), Shauger / Daniel–Shauger.
- The voltage-lift retirement is a certificate-level closure only. L024 kills the sufficient condition; it says nothing about actual lift spectra. Truth-level coverage is six bases, cyclic groups, orders 12–30.

Six paths, ranked

1. The parity channel (disproof, cheapest, highest value). Target: a bipartite graph, all degrees 3 except one degree-2 vertex in each part, girth ≥ 6, no C₈, no C₁₆, order 16–31. Any hit disproves 0.1 via a 3-ring. Order ≥ 16 is forced by C027; order ≤ 31 is not covered by the bipartite ≥32 bound, because that bound only rules out H + ab — which is power-free unless S contains a Mersenne number. So the live target is bipartite near-cubic gadgets with a through-path of length 3, 7 or 15. genbg handles bipartite degree-bounded generation natively and the class is small. Calibration first: rerun E013 at orders ≤14 with the filter "S all odd" instead of "e ≤ 0" — cheap, and it tells you whether all-odd taut cores exist at all.

2. Push the cubic census past Markström (disproof, decisive). At order 30 a cubic {C₄,C₈,C₁₆}-free graph is a counterexample outright (32 > 30). The published frontier is 28, from 2004. The class is minuscule (4, 23, 251 at orders 24, 26, 28) — reproduce 26 and 28 as anchors against your E005, then attempt 30, 32, 34. By L029 (modulo 1-atoms) cubic is the whole problem.

3. Mine existing censuses instead of generating (disproof, nearly free). Structured graphs are where spectrum confinement lives, and other people have already built the lists: the cubic vertex-transitive census up to 1280 vertices (~110k graphs, on Zenodo), cubic graphs of girth ≥ 9 (58–64 vertices — these avoid C₄ and C₈ automatically, so the entire question is C₁₆/C₃₂), snarks ≤ 36, the cages, House of Graphs collections. Testing lengths 4/8/16 is cheap. This directly tests the "high-girth escape" at its extremal point and is squarely in the mission's "lean on existing verified knowledge" line. Adjacent and unexplored: local/evolutionary search over Hamiltonian cubic chord diagrams at n = 30–62, minimising the count of forbidden-length cycles.

4. EGC for bipartite graphs (proof, new theorem, closes path 1). "Every bipartite graph with min degree 3 has a cycle of length 4, 8 or 16." Verified externally to 31 vertices. The interference algebra is cleaner here than in general — e.g. two 6-cycles sharing a path of length 2 force a C₈ immediately — and your L030 middle-layer-collapse machinery transfers with parity as extra leverage. This is the natural home for the machinery you've built, and unlike the pinched rungs it is a rung on the right ladder.

5. Strengthen Carr's 4/7 (proof, frontier-passing, no 1-atom dependency). Carr (May 2026) has "at least 4/7 of a minimal counterexample is cubic". Pushing 4/7 → 1 gives the cubic reduction without routing through the 1-atom question, and it is exactly where the newest literature sits — the most publishable target currently visible. Keep the 1-atom attack as the alternative route to the same theorem.

6. Exploit 3-connectivity (proof, structural, unused). In a 3-connected graph every edge uv sits in a theta with a path of length 1 (Menger on G−uv), so cycle lengths q+1, r+1, q+r are simultaneously constrained — leverage the dossier has never used. Free sample: if all cycle lengths were ≡ 0 (mod m), then q ≡ r ≡ −1 and q+r ≡ −2 ≡ 0, so m | 2. Hence no 3-connected graph confines its cycle spectrum to the multiples of an odd m — which kills the most natural modular escape at 3-connectivity. Two targets: reduce minimal counterexamples to 3-connected (your chain decomposition at cut vertices should extend to 2-cuts), and EGC for 3-connected cubic graphs beyond Heckman–Krakovski's planar case.

What I'd do first

Path 1's calibration run (odd-S filter on the existing E013 machinery at orders ≤14) is a few hours and either finds all-odd taut cores — which changes the whole picture — or confirms the parity channel is as empty as the pinched one. Then the bipartite gadget search at orders 16–24. Both are decisive, both are cheap, and both test something the last four sessions structurally could not see.
