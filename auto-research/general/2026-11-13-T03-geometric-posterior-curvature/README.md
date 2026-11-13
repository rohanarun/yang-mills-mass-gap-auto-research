# Geometric curvature of the actual coarse law: the posterior covariance term

## Metadata and result

- Date: 2026-11-13; Rohan Arun with OpenAI Codex assistance.
- Tracks: T03-B/D, T04, T06, T07. Repository base: `ff784a0ae4a886580dfb8e0c7aa4e9dac6ce94f6`.
- Upstream: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).
- Outcome: written exact Hessian formula for the normalized generated measure in fundamental SU(2), a sufficient posterior-covariance criterion for positive Bakry–Émery curvature, and a gauge-invariant comparison law that defeats a noise-only positivity claim.
- Evidence: source inspection and written analysis; [exact finite/symbolic checks](checks.json). **No new Lean proof, full upstream replay, independent mathematical review, or Yang–Mills decay estimate.**
- Related: [buffered posterior](../2026-11-11-T03-buffered-posterior/README.md), [noise transfer](../2026-11-11-T03-loop-noise-transfer/README.md), and [bare curvature criterion](../../negative-results/2026-11-12-T03-bakry-emery-scope/README.md). This work does not depend on unmerged PR #10.

The bounded question is whether geometry of the *actual generated law* can replace an unavailable bare Wilson curvature estimate. We obtain the exact quantity to control, not its required positive lower bound. The marginal log-density Hessian identity is standard, related to the missing-information identity in statistics; no novelty is claimed. See [Louis (1982)](https://doi.org/10.1111/j.2517-6161.1982.tb01203.x).

Two different curvatures must be kept separate: a plaquette measures field curvature, whereas the Bakry–Émery tensor below measures the geometry of configuration space together with its probability density.

## 1. Actual law and smoothness despite branch masks

Fix one finite source step with `Branches`, fundamental SU(2), and kappa = penalty * beta > 0. Keep its complete fine probability law mu, including every generated interaction. For z=(U,t), define

$$
\rho(dU,t)=\mu(dU)L_U(t),\quad
Q_e(z)=S.\mathrm{prediction}(U,t)_e,\quad
\Phi(V,z)=\kappa\sum_e[1-\mathrm{Re}(V_eQ_e(z)^{-1})].
$$

Here Re denotes the scalar part of a unit quaternion, equal to half the fundamental trace, and L is the joint likelihood with shared site tags. It sums to one. These are the definitions in [`RG/Block.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Block.lean).

If M is the number of independent coarse links and z_kappa is the one-link penalty normalizer, the coarse density relative to product probability Haar is exactly

$$
f(V)=z_\kappa^{-M}Z(V),\quad
Z(V)=\int e^{-\Phi(V,z)}\rho(dz),\quad
S_{\mathrm{eff}}(V)=-\log f(V).
$$

`Transfer` and `partition_eq` in [`History.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/History.lean) identify this with the actual normalized generated density. The normalizer is independent of V and therefore disappears from derivatives, not from the definition of the law.

Every frame choice, cutoff mask, and likelihood factor depends on z, not V. For fixed finite M, 0 <= Phi <= 2 kappa M, so exp(-2 kappa M) <= Z(V) <= 1. Every V-derivative of the integrand is bounded uniformly over z: it is an exponential of a linear function of the bounded quaternion coordinates Q, differentiated on a compact product of spheres. Dominated differentiation proves that f and S_eff are smooth in V even if Q is only measurable in U. No derivative of a minimizing frame or branch indicator is taken.

This establishes finite-dimensional smoothness, not bounds uniform in volume on all derivatives. The source supplies measurability and normalization; this differentiability application is a written argument, not a newly replayed source theorem.

## 2. Exact intrinsic Hessian

Use the product of round unit S^3 metrics on coarse links, with Ricci tensor 2I. Identify a tangent vector with imaginary quaternions xi_e through the product geodesic V_e(s)=V_e exp(s xi_e). Set

$$
Q_e^{-1}V_e=(x_e,y_e),\quad x_e\in\mathbb R,\ y_e\in\mathbb R^3,
\qquad
\pi_V(dz)=Z(V)^{-1}e^{-\Phi(V,z)}\rho(dz).
$$

Then the first and second derivatives of Phi along this geodesic are

$$
\Phi'=\kappa\sum_e y_e\cdot\xi_e,\qquad
\Phi''=\kappa\sum_e x_e|\xi_e|^2.
$$

Direct differentiation of -log Z gives the exact identity

$$
\mathrm{Hess}\,S_{\mathrm{eff}}(\xi,\xi)
=\kappa\sum_e\mathbb E_{\pi_V}x_e|\xi_e|^2
-\kappa^2\mathrm{Var}_{\pi_V}\left(\sum_e y_e\cdot\xi_e\right).
\tag{1}
$$

Define r_e(V)=E_pi x_e and the 3-by-3 covariance blocks

$$
C_{ef}(V)=\mathbb E_{\pi_V}[(y_e-\mathbb E y_e)(y_f-\mathbb E y_f)^T].
$$

Polarization of the geodesic second derivative yields, in the specified tangent coordinates,

$$
\mathrm{Ric}+\mathrm{Hess}\,S_{\mathrm{eff}}
=2I+\kappa\,\mathrm{diag}(r_e I_3)-\kappa^2 C(V).
\tag{2}
$$

The covariance is under the **full posterior conditioned on all coarse links V**, not under the fine prior or a product approximation. Marginalization subtracts a positive semidefinite covariance term. Dropping it would reverse the useful direction of the estimate.

Equations (1)-(2) specialize a standard marginalization identity to the actual source kernel. They expose the previously uncontrolled posterior correlations in a geometric form; they do not control those correlations.

## 3. A precise sufficient criterion, still unproved for the actual law

Since C_fe is the transpose of C_ef, the block operator norm and 2ab <= a^2+b^2 give

$$
\sum_{e,f}\xi_e^T C_{ef}\xi_f
\leq\sum_e|\xi_e|^2\sum_f\|C_{ef}\|.
$$

Consequently, a sufficient uniform Bakry–Émery lower bound is

$$
2+\kappa r_e(V)-\kappa^2\sum_f\|C_{ef}(V)\|
\geq\lambda>0
\quad\hbox{for every }V,e.
\tag{3}
$$

An operator inequality for (2) could be sharper than this absolute row sum. Constants must be tracked over the selected cutoffs, volumes, and physical scales. Bounded scores alone only give a row sum potentially proportional to M. A prior field-curvature expectation or a rare-event probability does not automatically bound this conditional covariance for every V.

Under the usual finite-dimensional Bakry–Émery hypotheses, (3) would control the auxiliary diffusion generated by the weighted configuration-space Laplacian. It is **not automatically a physical Hamiltonian mass gap**. Spatial estimates, locality costs, physical units, reconstruction, phase, and density bridges remain necessary. A multiscale version may be more appropriate than demanding (3) at every configuration and scale.

There is precedent for combining renormalization and geometric functional inequalities: [Bauerschmidt–Bodineau](https://arxiv.org/abs/1907.12308) prove a multiscale criterion and apply it to a massive sine-Gordon model. Its supplied mass, Gaussian decomposition, and model-specific estimates cannot be imported as Yang–Mills mass generation. [Moncrief–Marini–Maitra](https://arxiv.org/abs/1809.06318) discuss orbit-space geometry weighted by the quantum ground state; that is not the same measure or metric as the finite Euclidean configuration law used here.

## 4. An exact cancellation control

Consider one link with hidden prediction Q distributed by Haar. Convolution with the normalized noise leaves the output Haar, hence S_eff is constant. In the posterior, x=Re(Q^-1 V), y=Im(Q^-1 V), and a=E x=I_2(kappa)/I_1(kappa). Symmetry gives E y=0.

For the divergence-free rotation X on S^3 with Xx=-y_j and Xy_j=x, integrate X(y_j exp(kappa x)) over Haar. The integral vanishes, giving

$$
\mathbb E y_j^2=a/\kappa.
$$

Thus the two terms in (1) cancel exactly: kappa a - kappa^2(a/kappa)=0 in every direction. The covariance is not a negligible correction even in this simplest case. This is a written Haar integration-by-parts control, not a Lean result or a claim of posterior independence on a lattice with loops.

## 5. Gauge-invariant obstruction to noise-only curvature positivity

The [separate negative-result record](../../negative-results/2026-11-13-T03-geometric-noise-only/README.md) gives a continuous SU(2) comparison law on prediction links,

$$
d\rho_Q(Q)=[1+cW_p(Q)]\,dH(Q),\qquad 0<c<1,
$$

where W_p is a fundamental plaquette trace. It is normalized, strictly positive, smooth, and gauge invariant. After the same independent link-noise channel, its output density is exactly

$$
f(V)=1+bW_p(V),\qquad b=c\,[I_2(\kappa)/I_1(\kappa)]^4.
$$

At a central configuration with plaquette holonomy -I, a unit circulation direction has Bakry–Émery curvature

$$
2-\frac{4b}{1-b}.
$$

For c=3/4 and kappa=10, a rational Bessel-series enclosure proves a>17/20, giving curvature at most -223378/389437 < 0. The direction has zero graph divergence at the central configuration and changes the plaquette holonomy; it is not an infinitesimal gauge direction.

This is **not a realization of the selected Yang–Mills prediction law**. A single distinguished plaquette also does not impose the full translation/isotropy hypotheses of that law. It disproves only the generic inference that positivity, gauge invariance, and this noise channel alone force positive product-metric Bakry–Émery curvature. Quotient Ricci curvature is a different object and is not evaluated by the test.

Even this comparison model has a positive auxiliary Poincaré constant by bounded-density comparison with Haar. Thus failure of this pointwise curvature criterion does not imply failure of a spectral gap, still less failure of the Yang–Mills mass gap.

## Evidence and reproduction

Run from the repository root:

```sh
python3 auto-research/general/2026-11-13-T03-geometric-posterior-curvature/check_geometry.py
```

[Script](check_geometry.py), [output](checks.json), [receipt](verification.json). Python 3.9.6 and SymPy 1.14.0. The script checks 24 exact rational-quaternion gauge/noise identities, six finite latent-mixture first/second derivative identities, the cycle Hessian and divergence, and a rigorous rational positive-series enclosure at kappa=10. These support the algebra; the continuous source differentiation, Haar convolution, and conditional-to-physical implications are not checked by a finite experiment. The Bessel enclosure uses the same positive-series remainder argument as the earlier noise record. No numerical Yang–Mills sampling or new Lean proof was performed.

Selective source inspection also found many unrelated uses of the word "posterior" in upstream selection machinery. No absence or novelty claim is inferred from that search. The source-matched conclusions above follow from the explicitly cited kernel and history definitions.

## Failure lesson, next task, and review

The geometric attempt did not establish (3). It identified the exact negative covariance term and ruled out a positivity shortcut that ignores the fine dynamics. Smoothness in coarse coordinates does not require differentiating the branch masks; quantitative curvature requires the full conditioned law.

Next bounded task: derive a spatially resolved bound for C_ef under a specified actual posterior pi_V, or find a rigorous multiscale/averaged criterion that can tolerate its unfavorable regions. Preserve the Haar cancellation when estimating diagonal terms, and retain shared tags and all generated interactions. An arbitrary-latent-law estimate cannot use the desired positivity because the comparison law above violates it. Do not use the auxiliary diffusion time as physical imaginary time without a proof.

2026-11-13: initial AI-assisted derivation and checks proposed for review. No independent review or novelty assessment. The Yang–Mills mass gap remains unproved.
