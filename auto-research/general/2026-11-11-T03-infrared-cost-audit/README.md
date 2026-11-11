# Infrared source audit: the missing state-cost bound

## Metadata

- Date: 2026-11-11; author: Rohan Arun with OpenAI Codex assistance.
- Primary track: T03. Related: T02, T04, T05, T06, T07.
- Outcome: conditional projection criterion and identification of a missing uniformity estimate.
- Evidence: source inspection, written derivation, and symbolic coefficient arithmetic. The upstream statements used here have **not** been independently kernel-replayed.
- Upstream: [revision 3456e5e](https://github.com/yang-mills-group/OpenAI-YM-20261028/tree/3456e5e75cf8d4cd558955a5c7638fba2d68f464); [source hashes](provenance.json).
- The separately formalized generic criteria are [here](../2026-11-11-T02-uniform-projection-criterion/README.md). They do not discharge the hypotheses below.

## Question

Can the existing quadratic spectral-shell estimate be upgraded to a gap by controlling its constants, without first establishing a new exponential-clustering theorem?

## Exact dependence of the inspected bound

Fix a phase and a finite word polynomial $A$. Write $v=A\Omega$ and $v^*=A^*\Omega$, using the actual adjoint/reversal operation. Let $R\geq0$ be a radius outside which the time-averaged commutator vanishes. The source supplies such a radius for each compactly supported word, not a uniform radius for all words.

[`annulus` and `dyadic`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/EveryPhase/Light.lean) give, taking the scalar mass bound to be the sum of the two diagonal masses,

$$
\mu_v((0,u])\leq\frac{64}{9}R^3\bigl(\|v\|^2+\|v^*\|^2\bigr)u^2,\qquad 0<u\leq1.
$$

This constant uses the ordinary three-dimensional Euclidean volume and the source Fourier convention `pref Space3 = (2*pi)^3`. Specifically, `fee R M = Vol(B_R) M (8 Vol(B_1))`; the annulus multiplier is `pref^-1 * (2*pi)`, and `dyadic` contributes a factor two. With $\mathrm{Vol}(B_R)=4\pi R^3/3$, the annulus coefficient is $32R^3M/9$ and the resulting low-energy coefficient is $64R^3M/9$.

The source's `light_bound` instead first takes upper bounds on both masses uniformly over the compact character space. That compactness is over **phases for one fixed word**. It is not compactness of the Hilbert unit sphere and supplies no common normalized bound over all words. `late` obtains its radius from `Polynomials.distant`; there the witness is $4r+1$ for a support bound $r$.

The adjoint-state term is essential: `Polynomials.star_operator` identifies the reversed polynomial with the adjoint on the common domain, and the commutator calculation involves both spectral measures. Dropping $\|A^*\Omega\|$ has no justification from the inspected argument.

## Conditional gap criterion

Let $P_u$ be the orthogonal spectral projection onto $(0,u]$. Suppose a dense family of centered vectors has representatives with

$$
R_A^3\bigl(\|A\Omega\|^2+\|A^*\Omega\|^2\bigr)\leq K\|A\Omega\|^2
$$

for one finite $K\geq0$. The shell estimate gives

$$
\|P_u v\|^2\leq\frac{64K}{9}u^2\|v\|^2.
$$

Continuity extends this inequality to the centered Hilbert space. If $K>0$, choose $0<u\leq1$ with $u<3/(8\sqrt K)$. A nonzero projection has a vector on which it acts as the identity, contradicting the strict coefficient bound. Hence $P_u=0$. If $K=0$, the displayed shell bound directly gives the same conclusion for all $0<u\leq1$.

This is a **conditional route**, not a derived Yang–Mills estimate. It requires uniform costs that the source has not provided. It is stronger than necessary to require such representatives densely throughout the Hilbert space; ordinary density alone does not bound these costs.

## A more focused low-energy approximation target

It suffices to control approximations only to vectors in the range of $P_u$. Suppose every such vector $x$ has a finite-word approximant $v=A\Omega$ with

$$
\|x-v\|\leq\eta\|x\|,\qquad
R_A^3\bigl(\|v\|^2+\|A^*\Omega\|^2\bigr)\leq K_u\|x\|^2.
$$

If $0\leq\eta<1$, the projection is contractive and the shell bound implies

$$
\|x\|\leq\|P_u(x-v)\|+\|P_uv\|
\leq\left(\eta+\frac83u\sqrt{K_u}\right)\|x\|.
$$

Thus $P_u=0$ whenever $\eta+(8/3)u\sqrt{K_u}<1$. The norm argument is represented by the generic Lean theorem `idempotent_eq_zero_of_approximation`. Applying it to the actual PVM still requires the complete shell inequality, projection properties, and approximation hypotheses.

Conversely, if a nonzero $x$ lies in that range, every such approximant must pay

$$
R_A^3\bigl(\|v\|^2+\|A^*\Omega\|^2\bigr)
\geq\frac{9}{64}(1-\eta)^2u^{-2}\|x\|^2.
$$

For fixed $\eta<1$, a bound $u^2K_u\to0$ would therefore exclude sufficiently small positive spectral energies. No such approximation-cost estimate is established here.

## Another exponential in the source is not a correlation bound

[`PCalc.FiniteBound.wave_price`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/PCalc/Loop.lean#L62) bounds the difference of second derivatives of two finite-volume functionals by a term involving $\exp(-\gamma c)$, with $c$ the lattice side parameter. [`Pane.surge`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/PhysicalNext/RG_NEXT_COMPLETE_REPEATABLE_NONLINEAR_STEP/Pane/Spectrum.lean) transports that finite-volume comparison.

The observed left-hand side is a derivative-comparison error. It is not a centered two-point function with arbitrary physical separation, nor a norm of the physical heat semigroup. A separate theorem would be needed to connect it to either gap criterion. Its exponential notation alone cannot fill that obligation. This source audit is selective, not an exhaustive exclusion of useful estimates in all upstream modules.

## Reproduction

From the repository root, with the pinned Python requirements installed:

```sh
python3 auto-research/general/2026-11-11-T03-infrared-cost-audit/check_constants.py
```

The run exited zero; [recorded output](constants-check.json) reports SymPy 1.14.0. This checks coefficient algebra, not the upstream shell theorem, its applicability, or uniformity. Inspect the pinned sources and [provenance](provenance.json) to reproduce the audit.

## Contribution and next question

T03 now has a precise cost estimate to seek: control localization and adjoint-state preparation for low-energy vectors so that $u^2K_u$ is small enough. T05 must supply the appropriate approximation theorem rather than qualitative density alone. T04 must preserve that cost in physical units and through limits. T02 supplies generic projection tools; T07 must check the actual source bridges.

A next attempt should select a specific field/observable class and derive an upper bound on its preparation cost, or prove an obstruction to the proposed bound. The [cyclicity obstruction](../../negative-results/2026-11-11-T06-cyclicity-cost/README.md) rules out a shortcut based solely on cyclicity.

## Review history

No independent mathematical review of this extraction or its application is recorded.
