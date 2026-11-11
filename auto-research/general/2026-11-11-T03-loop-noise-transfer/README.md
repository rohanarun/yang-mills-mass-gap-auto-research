# Exact one-step noise transfer for SU(2) loop correlations

## Metadata and bounded question

- Date / author: 2026-11-11; Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03-B/C, related T04, T05, T06.
- Base: `346263bc79c95062042078e7d20f4dac669f79da`.
- Upstream: `yang-mills-group/OpenAI-YM-20261028`, pin `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).
- Outcome: written exact loop/covariance transfer for one actual blocking step, specialized to SU(2) in its two-dimensional fundamental representation. It isolates a fine-field covariance; it does not establish its spatial decay.
- Evidence: source-matched written derivation, rational Bessel-series enclosures, and exact finite non-Abelian controls. No Lean formalization, full upstream replay, or independent mathematical review.
- Question: after the [gauge-orbit reduction](../2026-11-11-T03-gauge-orbit-response/README.md), what does the actual blocking noise do to physical loop observables, and can this alone supply a separation-dependent bound?
- Falsification: wrong trace normalization, reuse of one noise variable as independent copies, or failure to retain shared tags invalidates the transfer. Bounded checks use Python's standard library and finite sums only.

## 1. Source matching and representation scope

Fix a selected history, cutoff $N\geq1$, volume $p$, and its step from level 1 to 0. Retain the full normalized fine law $P_1(dU)=Z_1^{-1}v_1(U)d\mu_1(U)$, including every generated interaction. Let $t$ denote the joint site/bond choices, with conditional law $L_U(t)=S.\mathrm{likelihood}(U,t)$, and put $Q(U,t)=S.\mathrm{prediction}(U,t)$.

The [exact buffered-law record](../2026-11-11-T03-buffered-posterior/README.md) identifies the actual coarse law as the marginal of

$$
P_1(dU)L_U(t)\prod_e k_\kappa(V_eQ_e^{-1})\,dH(V_e),
\qquad \kappa=\lambda\beta_1>0.
$$

Here $\lambda$ is the fixed positive kernel penalty. This uses [RG/Block.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Block.lean), [Push.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Push.lean), and the selected recurrence in [History.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/History.lean).

The source defines $\mathrm{price}(g)=1-\mathrm{Re}\,\mathrm{Tr}(g)/d$ in [MatrixGroup.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Gauge/MatrixGroup.lean#L112). For the fundamental SU(2) representation, $x(g)=\mathrm{Tr}(g)/2$ is real, and the normalized noise is exactly

$$
k_\kappa(g)=\frac{e^{\kappa x(g)}}{Z(\kappa)},
\qquad Z(\kappa)=\int_{SU(2)}e^{\kappa x(g)}dH(g).
$$

The constant $e^{-\kappa}$ cancels. This calculation is not asserted for every source `Gauge`: that structure permits other compact groups and representations, including reducible ones. Centrality of a matrix integral alone does not make it scalar in a reducible representation.

## 2. The exact scalar coefficient

Identify SU(2) with unit quaternions $(x,\mathbf y)\in S^3$. Conjugation rotates $\mathbf y$ while preserving $x$, so a conjugation-invariant density depending only on $x$ has zero mean imaginary coordinates. Therefore

$$
\int g\,k_\kappa(g)dH(g)=a(\kappa)I,
\qquad
\int g^{-1}k_\kappa(g)dH(g)=a(\kappa)I,
$$

where

$$
a(\kappa)=
\frac{\int_{-1}^1x e^{\kappa x}\sqrt{1-x^2}\,dx}
{\int_{-1}^1e^{\kappa x}\sqrt{1-x^2}\,dx}
=\frac{I_2(\kappa)}{I_1(\kappa)}.
$$

The Haar marginal is $(2/\pi)\sqrt{1-x^2}\,dx$. To check the Bessel normalization directly, write $D$ for the denominator and $J=\int e^{\kappa x}(1-x^2)^{3/2}dx$. Integration by parts gives $\kappa J=3\int xe^{\kappa x}\sqrt{1-x^2}dx$. The integral formula [DLMF 10.32.2](https://dlmf.nist.gov/10.32.E2) gives $I_1=\kappa D/\pi$ and $I_2=\kappa^2J/(3\pi)$, proving the ratio. This is standard harmonic analysis, not a novel special-function identity.

For $\kappa>0$, symmetry pairs $x$ and $-x$ to make the numerator strictly positive; positivity of the density and $x<1$ almost everywhere give $a<1$. Differentiating the bounded integral yields $a'(\kappa)=\mathrm{Var}_{k_\kappa H}(x)>0$. Thus $0<a(\kappa)<1$. For a fixed selected history the band $\beta_1\leq2\widehat\beta_1$ gives

$$
a(\kappa)\leq a(2\lambda\widehat\beta_1)<1
$$

uniformly in $N\geq1,p$. This is a coefficient bound, not a physical spectral gap.

## 3. Edge-distinct loop identity

Let $C$ be a closed oriented walk of length $\ell_C$ which uses each independent coarse link at most once, allowing either traversal orientation. Let $W_C(V)=\tfrac12\mathrm{Tr}(\prod_{e\in C}V_e^{\epsilon_e})$.

Conditionally on $(U,t)$, write $V_e=N_eQ_e$ with independent $N_e$ of density $k_\kappa$. For a forward traversal, $\mathbb E[V_e\mid U,t]=aQ_e$; for an inverse traversal, $V_e^{-1}=Q_e^{-1}N_e^{-1}$ and its mean is $aQ_e^{-1}$. Independence and multilinearity of matrix multiplication then give

$$
\mathbb E[W_C(V)\mid U,t]=a^{\ell_C}W_C(Q(U,t)).
$$

Define the actual averaged prediction observable

$$
\overline W_C(U)=\sum_t L_U(t)W_C(Q(U,t)).
$$

It is measurable and bounded by one in absolute value. It is gauge invariant: integrating the full gauge-covariant kernel against the gauge-invariant $W_C$ gives an invariant function of $U$, and this function equals $a^{\ell_C}\overline W_C(U)$ with $a>0$. This argument does not assume that individual branch selections transform separately.

If $C,D$ have disjoint link sets, the output noises also separate between the loops. With $\rho(dU,t)=P_1(dU)L_U(t)$,

$$
\mathrm{Cov}_{P_0}(W_C,W_D)
=a^{\ell_C+\ell_D}
\mathrm{Cov}_{\rho}(W_C(Q),W_D(Q)).
$$

All traces are real in this fundamental SU(2) calculation. This formula follows by applying the conditional product identity and the two one-loop identities, then subtracting the means.

## 4. Vertex-disjoint loops remove the conditional tag covariance

The source likelihood has the exact form

$$
L_U(s,b)=\prod_x p_x(s_x\mid U)
\prod_e p_e(b_e\mid U,s_{e_-},s_{e_+}).
$$

Each prediction $Q_e$ depends on $U$, the two endpoint site tags, and its own bond tag. In `Block.lean`, inspect `frames`, `connector`, `prediction`, and `likelihood`; `chosen` explicitly uses `frameMass_sum` and `predictorMass_sum` to normalize these factors. The definitions in [Patch.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Patch.lean#L148) show the conditional masses and branch-dependent predictions.

For vertex-disjoint $C,D$, integrate all bond tags outside their link sets first: every such conditional factor sums to one, including bonds connecting the two vertex sets. Then integrate unused site tags. The remaining factors separate between the two sets of vertices and bonds. Hence their prediction loops are independent **conditional on the complete fine field $U$**. No independence of the fine field, or disjointness of its read footprints, is assumed.

Consequently the one-step identity strengthens to

$$
\boxed{
\mathrm{Cov}_{P_0}(W_C,W_D)
=a(\kappa)^{\ell_C+\ell_D}
\mathrm{Cov}_{P_1}(\overline W_C,\overline W_D).
}
$$

For edge-disjoint loops sharing vertices, the previous $\rho$ formula remains valid, but a conditional tag covariance can remain. For overlapping link sets, a conditional output-noise covariance also has to be retained. These distinctions are essential.

## 5. What remains dynamical

For two separated elementary plaquettes, the prefactor is $a^8$. It is the same at every separation. Since $|\overline W|\leq1$, Cauchy–Schwarz supplies only $|\mathrm{Cov}_{P_0}|\leq a^8$, with no spatial rate.

The actual next estimate is therefore spatial decay of $\mathrm{Cov}_{P_1}(\overline W_C,\overline W_D)$, with complete read footprints and the required regulator control. The formulas identify precisely what averaging must be bounded; they do not bound it. A common positive physical rate, transported-source identification, phase selection, and a dense physical observable family still have to be proved.

It is invalid to iterate $a^\ell$ across levels while treating $\overline W_C$ as the same simple loop. In `Patch.predict`, the output can be a minimizing group element or a selected connector; the probabilities also depend on the fine configuration. The averaged observable is generally a nonlinear function of fine fields and is not shown to lie in a loop class closed under another identical calculation. Any expansion into a controlled observable class needs its coefficients, support costs, and errors proved.

## 6. Exact controls and scalar enclosures

Run from this repository root:

```sh
python3 auto-research/general/2026-11-11-T03-loop-noise-transfer/check_loop_noise.py
```

[Receipt](verification.json): Python 3.9.6, standard library only, exit 0, 0.133 seconds. [Output](check-output.json) contains two distinct kinds of evidence:

1. **SU(2) coefficient enclosures.** Using the positive series [DLMF 10.25.2](https://dlmf.nist.gov/10.25.E2), exact rational sums enclose $I_1,I_2$ at $\kappa=1/2,1,2,5,10$. If $t_k=(\kappa/2)^{2k+n}/[k!(k+n)!]$, successive ratios decrease. After index $M=40$, the omitted tail is at most $t_{M+1}/(1-q)$ with $q=\kappa^2/[4(M+2)(M+n+2)]<1$. Positive interval division and outward rounding give the recorded rational enclosures. For example, $0.240193723870\leq a(1)\leq0.240193723871$. These sample values are not universal physical constants.
2. **Finite non-Abelian controls.** On $Q_8$, choose exact Boltzmann noise at $\kappa=\log2,\log3$, where the normalized trace is in $\{-1,0,1\}$. The mean coefficients are $3/17$ and $2/7$, respectively; these are not the continuous SU(2) coefficients. For each parameter the code enumerates all 4,096 noise assignments for 12 oriented square/prediction cases, including noncommuting predictions. All edge-distinct identities pass. A two-square model with correlated hidden loop signs verifies covariance $(1/2)a^8$ by combining the directly enumerated conditional distributions.

The finite controls also exhibit the necessary exclusions. A backtrack $VV^{-1}$ has trace one, not $a^2$. With $Q=I$, a twice-used edge gives $\mathbb E[\tfrac12\mathrm{Tr}(N^2)]=-7/17$ at $\kappa=\log2$, whereas $a^2=9/289$. The same-loop covariance has positive conditional noise variance even for fixed predictions.

The correlated-sign model can be gauge-averaged without changing its loop traces or the noise-transfer calculation, and the loops can be separated by unused edges. Its correlation then still has no distance decay. This is a counterexample to a noise-only inference, not to Yang–Mills: it does not supply the selected Wilson fine law, local RG dynamics, continuum limit, or reconstruction. See the [failure record](../../negative-results/2026-11-11-T03-perimeter-not-separation/README.md).

## Handoff and review

The new concrete object is $\overline W_C$, defined from the actual branch probabilities and predictions. Seek a source-derived weighted expansion or another covariance estimate for this observable under $P_1$, retaining the full reference action and generated interactions. The success criterion is a separation-dependent bound that survives the required limits; a smaller perimeter coefficient does not meet it.

Review status: current author/assistant analysis and exact checks only. The general compact-group integration, tag-factorization application, and complete source correspondence remain written, not formally replayed. No mathematical novelty or mass-gap proof is claimed.
