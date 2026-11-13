# Positive averaged curvature does not ensure a volume-uniform gap

- Date: 2026-11-13; Rohan Arun with OpenAI Codex assistance.
- Tracks: T03, T04, T06, T07. Base: `5f41029f18f89695cb0867f612ca5ecd33985054`.
- Outcome: counterexample to an averaged-curvature inference, not to Yang–Mills or its physical gap.
- Evidence: written continuous SU(2) construction and all-n variational bound; exact polynomial and quaternion checks. No Lean proof, novelty claim, or independent review.
- [Companion derivation and source provenance](../../general/2026-11-13-T03-averaged-posterior-covariance/README.md), [script](../../general/2026-11-13-T03-averaged-posterior-covariance/check_average.py), [receipt](../../general/2026-11-13-T03-averaged-posterior-covariance/verification.json).

## Claim being tested

Does a uniform positive lower bound on the unweighted average of the product-frame Bakry–Émery matrix establish a volume-uniform Poincare gap, when the measure is smooth, positive, gauge invariant, and obtained using the source's independent SU(2) noise?

No. The example below satisfies all those conditions, with fixed noise strength and averaged curvature at least 2I, but its auxiliary Poincare constant tends to zero as the number of plaquettes increases.

## Smooth gauge-invariant mixture

Choose n pairwise edge-disjoint plaquettes on growing finite tori; their separations can be arbitrarily large. Let W_i be their half-traces and H product probability Haar on all links. Fix 0<c<1 and give the prediction links the density

$$
\rho(Q)=\frac12\prod_{i=1}^n(1+cW_i(Q))
+\frac12\prod_{i=1}^n(1-cW_i(Q)).
$$

Each product is normalized because E_H W_i=0 and edge-disjoint plaquettes depend on independent Haar links. The density is smooth, strictly positive, and gauge invariant. It is a mixture with one shared sign, not a local Wilson law or a demonstrated actual prediction pushforward. No construction-wide translation/isotropy or phase assumptions are claimed.

Apply the same normalized independent-link noise at fixed kappa>0. One distinct-link plaquette acquires the factor a(kappa)^4, with a=I_2/I_1; disjoint plaquettes allow the convolution to factor within each mixture component. Thus the exact output is

$$
f_n(V)=\frac12\prod_{i=1}^n(1+bW_i(V))
+\frac12\prod_{i=1}^n(1-bW_i(V)),\qquad b=c\,a^4\in(0,1).
$$

All other links remain Haar. The [single-plaquette convolution argument](../2026-11-13-T03-geometric-noise-only/README.md) proves the factor a^4, including inverse edge orientations.

## Spatial covariance and a slow gauge-invariant observable

For one Haar SU(2) holonomy, its scalar coordinate W satisfies E W=E W^3=0 and E W^2=1/4. Given the shared sign sigma, the W_i are independent with means sigma b/4 and second moments 1/4. Therefore

$$
\mathbb E_{f_n}W_i=0,\qquad
\mathrm{Cov}_{f_n}(W_i,W_j)=b^2/16\quad(i\ne j).
$$

There is no separation decay. For F_n=n^{-1} sum_i W_i,

$$
\mathrm{Var}_{f_n}(F_n)=\frac{1}{4n}+\frac{n-1}{16n}b^2.
$$

On the product of unit round S^3 link metrics, varying any one of a plaquette's four links gives gradient squared norm 1-W_i^2: multiplication and inversion by fixed unit quaternions are isometries, and the scalar coordinate on S^3 has that gradient norm. Edge disjointness eliminates cross terms, hence

$$
\int |\nabla F_n|^2 f_n\,dH
=\frac{4}{n^2}\sum_i\mathbb E_{f_n}(1-W_i^2)=\frac3n.
$$

Define the auxiliary Poincare constant by the infimum of this Dirichlet quotient over nonconstant smooth functions. Testing with F_n gives

$$
\boxed{\lambda_n\leq\frac{48}{4+(n-1)b^2}\longrightarrow0.}
$$

This upper bound also applies if the variational problem is restricted to gauge-invariant functions: F_n is gauge invariant. It does not require choosing a quotient metric or identifying this diffusion with the physical Hamiltonian.

Every fixed n still has a positive auxiliary gap by bounded-density comparison to Haar; the result concerns loss of uniformity. Meanwhile the companion identity gives averaged Bakry–Émery matrix at least 2I for every n. There is no contradiction: curvature must be controlled against configuration-dependent gradients, not just averaged against constant vectors.

## Evidence, scope, and failure lesson

Exact polynomial integration checks the normalization, mean, variance, Dirichlet expression, and Rayleigh quotient for n=1 through 6, symbolically in b. Twenty exact quaternion samples check each individual-link gradient identity. These diagnostics support the displayed all-n analytic argument; they do not independently prove it or establish an actual Yang–Mills measure.

The shared hidden sign creates persistent correlations explicitly. The actual local dynamics could exclude such behavior; doing so requires a dynamical theorem. Gauge invariance, smoothness, independent output noise, and averaged covariance alone do not exclude it. Reopen this route with spatial posterior control or a justified multiscale/gradient-weighted bound that uses the actual law. Do not infer physical mass-gap failure from an auxiliary comparison model.
