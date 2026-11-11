# A strong-coupling lattice theorem does not directly cover the running continuum family

## Metadata

- Date: 2026-11-11; author: Rohan Arun with OpenAI Codex assistance.
- Tracks: T04, T03, T06.
- Outcome: scope mismatch for direct application of a specific existing lattice result.
- Evidence: primary-source comparison and written asymptotic argument. No new theorem of Yang–Mills dynamics or formal verification is claimed.

## Primary sources

Shen, Zhu, and Zhu, [A stochastic analysis approach to lattice Yang–Mills at strong coupling, arXiv:2204.12737v1](https://arxiv.org/abs/2204.12737v1), state a positive lattice mass gap for a sufficiently small inverse-coupling regime. For $SU(N)$ their stated condition is $|\beta_{\rm paper}|<1/[16(d-1)]$.

Their [equation (1.2)](https://arxiv.org/html/2204.12737v1) uses $N\beta_{\rm paper}\sum_p\operatorname{ReTr}(U_p)$ in the exponent. The upstream [Wilson law](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicWilson.lean) uses $-\beta_{\rm repo}\sum_p(1-\operatorname{ReTr}(U_p)/N)$. With matching once-per-plaquette counting, constants cancel on normalization and the coefficients match at $\beta_{\rm repo}=N^2\beta_{\rm paper}$. Different fixed counting conventions would change this fixed factor, not the divergence below. This is a coefficient comparison, not a formal identification of the two theories.

## Obstruction to direct reuse

The upstream [WilsonRegularity.running](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/ChallengeSpec.lean#L10) requires a positive limiting slope for $\beta_{\rm repo}/\log(1/a)$, uniformly over volumes. Its strictly increasing integer denominator forces $a\to0$, hence $\log(1/a)\to\infty$. Taking an error smaller than half the positive slope gives $\beta_{\rm repo}\to+\infty$ uniformly over the volume parameter.

At a fixed gauge-group rank, division by the fixed normalization factor cannot keep $\beta_{\rm paper}$ in the cited bounded interval. Therefore the cited strong-coupling theorem cannot simply be applied at every sufficiently fine cutoff along this continuum family. Infinite-volume control within its stated coupling regime does not establish the required cutoff-uniform estimate.

## What remains possible

This does not rule out a renormalization argument that reaches a suitable effective strong-coupling regime. Such a route must identify the actual blocked measure, account for generated interactions, prove the required estimates there, and transport them back in physical units. None of those steps follows merely from citing the lattice theorem.

Agents should always compare action normalizations, coupling ranges, and the direction of the cutoff limit before importing a mass-gap estimate. Reopen the direct route only if its hypotheses are proved for the actual family, or if a proved extension covers the running regime.

## Review status

The abstract and displayed action were inspected; the full paper's proofs were not independently reproduced. No independent review of this comparison is recorded.
