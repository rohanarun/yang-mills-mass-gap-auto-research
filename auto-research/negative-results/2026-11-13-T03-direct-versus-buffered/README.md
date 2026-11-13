# Direct interaction locality is not buffered independence

- Date: 2026-11-13; Rohan Arun with OpenAI Codex assistance.
- Tracks: T03, T06; related T04/T07.
- Outcome: a standard exact control against replacing a buffered marginal by a fixed-buffer conditional. Not a new theorem or a Yang–Mills counterexample.
- Evidence: written finite-chain calculation and 21 exact rational enumerations. No Lean proof or independent review.
- Base: `ff784a0ae4a886580dfb8e0c7aa4e9dac6ce94f6`.
- Companion: [source-derived regular spatial tail](../../general/2026-11-13-T03-regular-spatial-tail/README.md), [script](../../general/2026-11-13-T03-regular-spatial-tail/check_tail.py), [output](../../general/2026-11-13-T03-regular-spatial-tail/checks.json), [receipt](../../general/2026-11-13-T03-regular-spatial-tail/verification.json).

## Tested inference

An exponential bound on direct interaction terms meeting two regions does not by itself control their correlation after the intervening variables are integrated. Even an identically zero direct mixed variation does not imply independence of the marginal endpoints.

Take spins sigma_0,...,sigma_L in {-1,1}, L>=2, with law

$$
P(\sigma)=\frac12\prod_{i=0}^{L-1}\frac{1+q\sigma_i\sigma_{i+1}}2,
\qquad 0<q<1.
$$

This is a normalized nearest-neighbour Markov chain. Its negative log density is a sum of edge terms. No edge term depends on both endpoints for L>=2. Consequently its direct four-term mixed difference in sigma_0 and sigma_L vanishes when all intermediate spins are fixed.

But summing all intermediate spins gives

$$
P(\sigma_0=a,\sigma_L=b)=\frac{1+q^L ab}{4},\qquad
\mathrm{Cov}(\sigma_0,\sigma_L)=q^L>0.
$$

The kernel identity follows inductively from summing a product of two binary transition factors. The endpoint marginal has a nonzero effective coupling, despite the vanishing direct mixed difference. For fixed q it does decay exponentially; this example is not a failure of clustering. It shows that the rate comes from the local dynamics and its propagation, which must be controlled separately. If q varies toward one with regulators, direct locality alone supplies no common positive rate.

This chain identity was already used in the [buffered-posterior record](../../general/2026-11-11-T03-buffered-posterior/README.md). The present use is a conditioning check for the new regular-sector estimate, not new mathematics. The script enumerates lengths 2 through 8 for q=1/5, 2/3, 9/10 and checks normalized endpoint laws, covariance, and absence of any direct common edge term.

The actual Yang–Mills law retains a reference action, generated regular interactions, and an exact-coverage forced gas. The companion result bounds only the direct regular contribution and its conditional perturbation. Turning those inputs into a buffered correlation estimate requires an additional propagation/mixing theorem for the remaining law. No failure of the mass gap follows from this diagnostic.
