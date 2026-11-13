# Exact averaged posterior covariance and its geometric limitation

## Metadata and bounded task

- Date: 2026-11-13; Rohan Arun with OpenAI Codex assistance.
- Tracks: T03-B/D, T04, T06, T07. Base: `5f41029f18f89695cb0867f612ca5ecd33985054` (PR #11).
- Upstream: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [verified source hashes](provenance.json).
- Outcome: written exact averaged covariance identity for the actual finite SU(2) blocking law and a volume-independent matrix bound; these do not supply a spatial estimate or physical gap.
- Evidence: source inspection, written continuous argument, exact finite/polynomial diagnostics. No new Lean proof, independent review, or novelty claim.
- Task: retain the diagonal cancellation in the [posterior Hessian](../2026-11-13-T03-geometric-posterior-curvature/README.md), and test whether averaging supplies the missing geometric control. Falsification: incorrect conditioning, failure of the covariance identity, or a claimed uniform gap contradicted by a gauge-invariant comparison law. Computation: finite exact algebra only.

The exact averaged bound does hold. A separate comparison law shows it cannot, on its own, establish a uniform auxiliary Poincare gap or spatial decay. This continues the geometric route by testing a specific relaxation of pointwise curvature positivity; it does not discharge the Yang–Mills dynamical obligation.

## Source and joint noise coordinates

Fix a finite actual step in fundamental SU(2), with M independent coarse links and kappa=penalty*beta>0. Let z=(U,t) contain the full fine field and shared tags, and let rho be its normalized prior. Retain generated interactions and write Q_e(z) for the chosen prediction. The coarse density f and posterior pi_V are exactly those of the companion record.

The source noise is a product of normalized densities k_kappa(V_e Q_e^{-1}); see [`Block.lean`, noise/density](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Block.lean#L68). [`History.Transfer` and `partition_eq`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/History.lean#L223) identify its output with the normalized generated law.

Set R_e=Q_e^{-1}V_e=(x_e,y_e), with y_e in R^3. Conditional on z, substitute V_e=Q_e R_e. Haar invariance and centrality of k imply that R_e have independent densities proportional to exp(kappa x_e), independent also of z. This assertion concerns the **joint generative law**, not the posterior after fixing V. The latter can be strongly correlated.

Put a=I_2(kappa)/I_1(kappa). Rotation symmetry and integration by parts on S^3 give

$$
\mathbb E x_e=a,\quad \mathbb E y_e=0,\quad
\mathbb E[y_e y_f^T]=\delta_{ef}\frac{a}{\kappa}I_3.
$$

For the variance identity, the divergence-free rotation X with Xx=-y_j and Xy_j=x gives integral X(y_j exp(kappa x))=0, hence E y_j^2=a/kappa. The first moment formula is in the [noise record](../2026-11-11-T03-loop-noise-transfer/README.md). These identities do not assume a factorized fine law.

## Cancellation after averaging: an exact matrix identity

Use the fixed product tangent frame V_e exp(s xi_e). Stack y_e into Y in R^(3M), let

$$
 m(V)=\mathbb E[Y\mid V],\qquad C(V)=\mathrm{Cov}(Y\mid V),
 \qquad r_e(V)=\mathbb E[x_e\mid V].
$$

By the law of total covariance and E m=0,

$$
\boxed{\mathbb E_f C(V)=\frac{a}{\kappa}I_{3M}
-\mathbb E_f[m(V)m(V)^T].}
\tag{1}
$$

Consequently 0 <= E_f C <= (a/kappa) I in positive-semidefinite order, independently of M. Averaging the exact source-matched Hessian yields

$$
\boxed{\mathbb E_f[\mathrm{Ric}+\mathrm{Hess}\,S_{\mathrm{eff}}]
=2I+\kappa^2\mathbb E_f[m(V)m(V)^T].}
\tag{2}
$$

In this specified frame,

$$
2I\preceq\mathbb E_f[\mathrm{Ric}+\mathrm{Hess}\,S_{\mathrm{eff}}]
\preceq(2+\kappa a)I.
$$

This is an average of matrix components, not an intrinsic identification of arbitrary tangent spaces. It includes every fine interaction through the posterior and makes the diagonal cancellation exact. It bounds E C, not E||C||, absolute covariance row sums, or C(V) for every V. It contains no distance factor.

The averaged Hessian/Fisher identity itself is standard: for any smooth positive density f=exp(-S) on this compact product, a constant-frame vector field X has zero Haar divergence and geodesic flow, so integration by parts gives E_f X^2 S=E_f(XS)^2. Polarization gives the matrix statement. Our additional channel-specific assertion is the upper bound and its explicit a/kappa posterior decomposition. The marginalization formula is related to [Louis's missing-information identity](https://doi.org/10.1111/j.2517-6161.1982.tb01203.x); neither general identity is claimed as new.

## Why this does not close a functional inequality

A curvature proof through the integrated Bochner identity needs curvature paired with gradients that depend on V:

$$
\int (\mathrm{Ric}+\mathrm{Hess}\,S)(\nabla g,\nabla g)f\,dH.
$$

Equation (2) only controls constant-frame test vectors after averaging. One cannot take the variable gradient outside the integral. Unfavorable regions can coincide with gradients of functions that distinguish slowly exchanging parts of the measure.

The [comparison-law record](../../negative-results/2026-11-13-T03-averaged-curvature-gap/README.md) makes this failure precise. At one fixed positive kappa, smooth positive gauge-invariant hidden laws on n disjoint plaquettes produce outputs satisfying (1)-(2), yet two separated loop traces have covariance b^2/16 and the auxiliary Poincare constant obeys

$$
\lambda_n\leq\frac{48}{4+(n-1)b^2}\longrightarrow0,
\qquad b=c\,a(\kappa)^4>0.
$$

The example deliberately contains a shared global hidden sign and is not the actual local Yang–Mills prior. It tests exactly the information lost by retaining only (1)-(2). It extends the earlier [gauge-only mixing controls](../../negative-results/2026-11-11-T06-gauge-only-mixing/README.md) to continuous SU(2), the actual noise channel, and a quantitative vanishing auxiliary-gap bound.

## Evidence and next task

Run `python3 auto-research/general/2026-11-13-T03-averaged-posterior-covariance/check_average.py` from the repository root. [Output](checks.json) and [receipt](verification.json) record six exact Haar-polynomial cases, 20 rational-quaternion plaquette-gradient cases, and four finite-channel total-covariance cases; all passed. The finite-channel cases test the conditional covariance bookkeeping, not the continuous source theorem. Haar moments used in the polynomial checks are the analytic S^3 coordinate moments Catalan(k)/4^k at even degree 2k; this is exact polynomial integration, not sampling.

The script imports quaternion helpers from the PR #11 record; its hash is in the receipt. Continuous changes of variables, integration by parts, and the all-n comparison proof remain written and unreviewed. No Yang–Mills simulation, new Lean check, or independent verification is claimed.

Next task: identify a spatial estimate for the actual posterior or a bound on unfavorable curvature weighted by the relevant varying gradients, with uniform cutoff/volume constants. A multiscale method must prove its scale-by-scale hypotheses, rather than substituting a positive unweighted mean. [Bauerschmidt–Bodineau](https://arxiv.org/abs/1907.12308) supply a model-specific multiscale criterion for massive sine-Gordon, not the missing Yang–Mills estimate. Auxiliary configuration-space relaxation remains distinct from physical imaginary time, with locality, scale, reconstruction, phase, and density bridges still open.

No research worker remains active after handoff. The Yang–Mills mass gap remains unproved.
