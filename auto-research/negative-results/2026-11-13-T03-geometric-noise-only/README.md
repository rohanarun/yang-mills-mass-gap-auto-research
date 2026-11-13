# Gauge invariance and smoothing do not ensure positive curvature

## Metadata and tested claim

- Date: 2026-11-13; Rohan Arun with OpenAI Codex assistance.
- Tracks: T03, T06, T07; related physical-scope warning in T04.
- Outcome: counterexample to a stated inference, not a counterexample to Yang–Mills or its mass gap.
- Evidence: written continuous Haar-convolution argument, exact symbolic identities, and rational series bounds. No Lean proof or independent mathematical review.
- Sources, commands, versions, and receipts: [companion derivation](../../general/2026-11-13-T03-geometric-posterior-curvature/README.md), [script](../../general/2026-11-13-T03-geometric-posterior-curvature/check_geometry.py), [checks](../../general/2026-11-13-T03-geometric-posterior-curvature/checks.json), [verification](../../general/2026-11-13-T03-geometric-posterior-curvature/verification.json).

The failed inference is: a gauge-invariant hidden prediction law, convolved with the source's normalized independent SU(2) link noise, necessarily produces positive Bakry–Émery curvature in the product round metric. The example below violates that inference even for a smooth strictly positive hidden law. It does not establish that this law is realizable as the actual fine-field/tag prediction pushforward. It singles out one face and does not satisfy every symmetry or dynamical hypothesis of the actual construction.

## Continuous gauge-invariant comparison law

Use a finite coarse torus with side at least three, one plaquette p with four distinct independent links, and product probability Haar measure H. Let W_p be half the real fundamental trace of its oriented holonomy. For 0<c<1, take

$$
\rho_Q(dQ)=[1+cW_p(Q)]H(dQ).
$$

This is gauge invariant, smooth, and bounded between 1-c and 1+c. It is normalized because integrating any one of the four links gives integral W_p=0.

Let k_kappa(g) be the probability density proportional to exp(kappa Re(g)), equivalently the source's normalized exp(-kappa(1-Re(g))) penalty. Apply the exact independent-link noise channel to this prediction law. Its output is

$$
f(V)=\int\prod_e k_\kappa(V_eQ_e^{-1})[1+cW_p(Q)]H(dQ)
=1+bW_p(V),\qquad b=c\,a(\kappa)^4,
$$

where a(kappa)=I_2(kappa)/I_1(kappa). To see the equality, substitute Q_e=G_e^{-1}V_e. The G_e are independent with central density k_kappa; their fundamental matrix means and inverse means both equal a I. Each distinct plaquette edge therefore contributes one factor a, including the two inverse orientations. All other links integrate to one. This is an exact continuous group integral, not a finite-group approximation. The first-moment formula is derived in the [earlier noise record](../../general/2026-11-11-T03-loop-noise-transfer/README.md).

## A horizontal cycle with negative curvature

Label the four edges 0:0→1, 1:1→2, 2:3→2, and 3:0→3, so the plaquette word is V_0 V_1 V_2^{-1} V_3^{-1}. Start with V_0=-1 and the other links equal to 1. Choose a unit imaginary quaternion i and the product geodesic

$$
V_0(t)=-e^{ti},\quad V_1(t)=e^{ti},\quad
V_2(t)=e^{-ti},\quad V_3(t)=e^{-ti}.
$$

Other links are constant. Then W_p(t)=-cos(4t), the tangent squared norm is 4, and for S_eff=-log f,

$$
S_{\mathrm{eff}}''(0)=-\frac{16b}{1-b}.
$$

Each unit round SU(2) factor has Ricci tensor 2I. Thus in the unit direction of this geodesic,

$$
(\mathrm{Ric}+\mathrm{Hess}\,S_{\mathrm{eff}})(\widehat\xi,\widehat\xi)
=2-\frac{4b}{1-b}<0\quad\text{if }b>\frac13.
$$

At this central configuration, the adjoint connection is trivial. The edge tangent signs (1,1,-1,-1) have zero vertex divergence, so this direction is orthogonal to infinitesimal gauge directions in the product metric. It changes loop holonomy; the negative potential curvature is not solely a gauge-coordinate effect. This does **not** compute the Ricci tensor of a gauge quotient or prove negative Bakry–Émery curvature in a quotient metric.

## Certified finite parameters

Take kappa=10 and c=3/4. Positive-term Bessel series with a geometric remainder bound certify

$$
a(10)>\frac{17}{20},\qquad
b>\frac{250563}{640000}>\frac13.
$$

The unit curvature is consequently less than -223378/389437, hence strictly negative. The script checks the rational enclosure, exact cycle Hessian, zero divergence, and 24 rational-quaternion gauge/noise identities. Its six finite latent-mixture checks also verify the sign and ordering in the companion Hessian formula. These checks support the written argument; they are not a formal verification of the continuous construction.

## What this does and does not exclude

The comparison law still has a positive auxiliary Poincare constant. Indeed, write nu for product Haar and let lambda_H>0 be a Poincare constant for nu. Since 1-b <= f <= 1+b,

$$
\mathrm{Var}_{f\nu}(g)
\leq(1+b)\mathrm{Var}_{\nu}(g)
\leq\frac{1+b}{\lambda_H(1-b)}\int|\nabla g|^2 f\,d\nu.
$$

The first inequality follows by choosing the nu mean as a candidate centering constant. Thus failure of pointwise positive curvature does not imply failure of a functional inequality, let alone absence of a physical mass gap.

The result rules out only a universal positivity argument based on gauge invariance and this noise channel. Reopening the proposed geometric route requires an additional property of the actual Yang–Mills prediction posterior, or a justified criterion allowing unfavorable curvature regions. Preserve the negative covariance in the exact Hessian identity; account for diagonal cancellation rather than bounding its pieces separately without control. A configuration-space diffusion gap is not a physical Hamiltonian gap without further arguments.

No independent review has occurred. The Yang–Mills mass gap remains unproved.
