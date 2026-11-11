# Taking a logarithm before integration misses connected correlations

## Metadata

- Date: 2026-11-11; Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03, T04, T06. Outcome: counterexample to transferring a fixed-field mixed-log bound to a normalized correlation without further control.
- Evidence: written finite-probability/transfer-matrix calculation and exact SymPy checks. No Lean model or independent review.
- Repository base: `1fac2ea99ebdfe40ca8c2a51d42b522d9f54e77b`.
- Related: [connected-source bridge audit](../../general/2026-11-11-T03-connected-source-bridge/README.md) and [block-gap control](../2026-11-11-T03-auxiliary-resolvent-gap/README.md).

## The missing term

Let $\rho_{s,t}(U)>0$ be a twice differentiable density against a source-independent reference measure. Suppose the density and its derivatives have integrable dominating bounds near $(s,t)=(0,0)$, and $0<Z(s,t)=\int\rho_{s,t}\,d\mu<\infty$. Write $L=\log\rho$ and use normalized expectations at zero sources. Differentiating under the integral and applying the quotient rule gives

$$
\partial_s\partial_t\log Z\big|_0
=\mathbb E[L_{st}]+\mathbb E[L_sL_t]-\mathbb E[L_s]\mathbb E[L_t].
$$

Thus a bound on $L_{st}$ alone leaves $\mathrm{Cov}(L_s,L_t)$ uncontrolled. If sources enter linearly as $\rho_{s,t}=\rho_{0,0}\exp(sA+tB)$, then $L_{st}=0$ identically while the left side equals the entire connected correlation of $A$ and $B$.

The same formula applies after integrating out some variables: the conditional logarithm contributes its mixed derivative, and the covariance of its first derivatives is taken under the remaining measure. Positivity, differentiation under integration, normalization, and all source dependence must be checked for the actual application. A formal marked-log identity by itself does not supply them.

## Local finite-chain counterexample

Take the open Ising chain with $R$ edges, spins $\sigma_0,\ldots,\sigma_R\in\{-1,1\}$, and unnormalized density

$$
\rho_{s,t}(\sigma)=\exp\left(J\sum_{i=0}^{R-1}\sigma_i\sigma_{i+1}+s\sigma_0+t\sigma_R\right),\quad J>0.
$$

It has strictly positive weights and nearest-neighbor interactions. For every configuration and separation, $\partial_s\partial_t\log\rho_{s,t}=0$. Nevertheless

$$
\partial_s\partial_t\log Z\big|_0
=\langle\sigma_0\sigma_R\rangle=(\tanh J)^R>0.
$$

To verify all lengths, set $z=e^J$ and use the transfer matrix $T=\left(\begin{smallmatrix}z&z^{-1}\\z^{-1}&z\end{smallmatrix}\right)$. Its complementary projections onto $(1,1)$ and $(1,-1)$ have eigenvalues $\lambda_+=z+z^{-1}$ and $\lambda_-=z-z^{-1}$. Therefore $T^R=\lambda_+^RP_++\lambda_-^RP_-$ and

$$
Z(s,t)=2\lambda_+^R\left(\cosh s\cosh t+
(\lambda_-/\lambda_+)^R\sinh s\sinh t\right).
$$

The claimed correlation follows by differentiation. At fixed $J$ it does decay exponentially, with rate $-\log\tanh J$. The point is that the identically zero fixed-field mixed derivative does not determine that rate or bound it uniformly over couplings.

For the family $J_R=\tfrac12\log R$, $R\geq2$,

$$
(\tanh J_R)^R=\left(\frac{R-1}{R+1}\right)^R\longrightarrow e^{-2}>0.
$$

Thus no fixed finite $C$ and fixed $m>0$ bound this family's endpoint correlation by $Ce^{-mR}$. Allowing arbitrary size-dependent prefactors only at the endpoint would make such an inequality vacuous; that is not the uniform finite-volume estimate tested here. This is a discrete probability control, not a four-dimensional Yang–Mills model, a continuum limit, or an identification of its parameters with the upstream coupling.

## A separate scale-counting check

If a hypothetical RG argument obtains only one contraction $L_j^{-p}$ per blocking step and identifies the separation ratio with $\prod_jL_j$, then

$$
\prod_jL_j^{-p}=\left(\prod_jL_j\right)^{-p}.
$$

That is a power of separation, not an exponential in separation. In the audited source, `SOURCE_HISTORIES/Reserve.lean` defines a numerical local-error rate $L^{-2/5}$. It is **not** asserted there to be a physical correlation contraction. Even a proof that it supplied the hypothetical product above would not yield a positive mass gap. This observation does not rule out stronger dynamical RG mechanisms.

## Reproduction, lesson, and next question

From the repository root:

```sh
python3 auto-research/negative-results/2026-11-11-T03-log-integration-order/check_ising.py
```

[Output](ising-check.json) and [receipt](verification.json) record the transfer-matrix identities, direct enumeration of chains with one through five edges, the exact coupling-dependent limit, and the scale-product identity. Enumeration alone is not the all-length proof; that is the projection calculation above. No simulation was used.

Always identify whether a logarithm is taken before or after the remaining integration. Preserve the covariance term and source normalization. Reopen this route when the retained measure has a justified mixing estimate, or when an exact expansion of the **fully integrated** log partition function supplies uniformly weighted connected coefficients. A small intermediate activity or per-step error is insufficient. No independent review is recorded.
