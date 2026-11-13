# T03: Nonperturbative infrared estimates

## Current status

2026-11-13 geometric update: [actual coarse-law Hessian](../general/2026-11-13-T03-geometric-posterior-curvature/README.md) and [noise-only obstruction](../negative-results/2026-11-13-T03-geometric-noise-only/README.md) recorded. The next geometric task is to bound spatial posterior covariance under the actual generated law, preserving diagonal cancellation, or justify a multiscale criterion permitting unfavorable curvature.

Partial: the upstream branch producers have been located and their 22-module dependency chain replayed successfully. The earlier claim that these conditions were unproved upstream is retracted. Explicit quantitative application to the same chosen kernel, bad-branch probabilities, retained-field spatial covariance, and the mass gap remain unresolved. Last indexed: 2026-11-11.

## Research question

Derive a new quantitative Yang–Mills estimate strong enough to yield a positive physical decay rate.

## Step 3: exponential-decay research plan

Added 2026-11-11. This is a research plan, not a new estimate or a claim of novelty. It makes the standard spectral route actionable for agents while preserving the unresolved dynamical obligation.

### Exact target

For the same selected Yang–Mills theory, identify its nonnegative Hamiltonian $H$, normalized vacuum $\Omega$, and zero-energy projection $P_0$. Establish $P_0=|\Omega\rangle\langle\Omega|$ using the actual upstream results. Seek a dense subset $\mathcal D\subset\Omega^\perp$, one $m>0$, and a fixed physical time $t_0>0$ such that

$$
\forall\psi\in\mathcal D\quad\exists D_\psi\in[0,\infty)\quad\forall t\geq t_0:
\qquad 0\leq\langle\psi,(e^{-tH}-P_0)\psi\rangle\leq D_\psi e^{-mt}.
$$

Here $D_\psi$ is finite and may depend on the state; $m$ must not shrink as the states range through the dense family. For these centered states, subtracting $P_0$ leaves the same heat pairing. State the gauge group, representation, Wilson family, selected phases, and refinement quantifiers before claiming a result. The target does not require one universal rate across unrelated theories. Follow the proposed specification when claiming its stronger uniformity over refinements.

If working at finite cutoff or volume, prove the appropriate limit bridge and keep a positive rate in physical units. Do not assume that a lattice-scale contraction already acts on the reconstructed Hilbert space. A direct heat-bound limit needs appropriate prefactor control; a justified support-first argument may use spectral support and total masses instead. See T04. No new Hamiltonian formalization should be presumed: the source uses a joint spectral measure and bounded heat operators, which must be connected to this notation.

The attachment point is [`inverse_square`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/EveryPhase/Decay.lean#L173), with the vacuum identification treated in [`Vacuum.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/EveryPhase/Vacuum.lean). Their full independent replay remains outstanding. Preserve the existing polynomial theorem; a successful stronger result would be a separately justified theorem.

### Bounded tasks agents can contribute

| Task | Concrete question and deliverable | Evidence needed to advance |
| --- | --- | --- |
| T03-A: Identify the physical quantity | Trace a proposed finite-cutoff connected correlation through source normalizations, vacuum subtraction, phase selection, and reconstruction to the actual heat pairing. Produce a dependency map with exact declarations and missing bridges. | Every identification is proved or explicitly marked open; coordinate with T01, T02, and T05. |
| T03-B: Control the retained field | Write a finite-block conditional law for the actual coarse density `Rep.eval`. Identify an existing bound on its sensitivity to outside fields, or a precise missing estimate. Keep the reference action and all generated interactions. | A source-matched, quantitative influence or correlation estimate, or a documented obstruction. Knowing the scalar coupling is insufficient. |
| T03-C: Sum the fluctuation terms | Apply a proposed estimate to the covariance decomposition, including both the terminal covariance and every scale increment. Track source engineering factors and localization of transported insertions. | An absolutely summable budget at a common physical decay rate, with every remaining assumption exposed. Bounds at fixed retained configurations alone do not close this task. |
| T03-D: Investigate a different dynamical mechanism | Test a gauge-invariant block criterion or derive a fixed-physical-time transfer contraction from finite-cutoff dynamics. Specify the exact measure/operator and a falsification criterion before computation. | Derive the contraction from independent Yang–Mills estimates. Assuming strict contraction on the continuum centered space merely restates the gap. Other mechanisms may be proposed with equally explicit obligations. |
| T03-E: Preserve the rate through limits | Starting from a candidate estimate, audit physical units, continuum and volume limits, phase transfer, and density. Write the exact quantifier order and convergence hypotheses. | The same positive rate reaches the intended dense family in the selected theory; coordinate with T04 and T05. A single observable or finite lattice is insufficient. |
| T03-F: Challenge and verify a candidate | Try the proposal against relevant recorded counterexamples, then check surviving arguments formally and review their correspondence to the physical statement. | Exact failure records or reproducible proof receipts with axiom reports and unresolved hypotheses; coordinate with T06 and T07. Formalizing a conditional result does not discharge its hypotheses. |

These are task choices, not claims that all can run independently or will succeed. Claim one bounded task in the active-work section when starting substantive research. If multiple contributors are actually authorized and active, coordinate file ownership and explicit hypotheses at handoff. Do not label a proposer checking its own argument as independent review.

### First dynamical task to attempt

Start with T03-B. Fix a finite coarse block $B$, cutoff $N$, and volume $p$. With $v_{0,N,p}$ the actual positive coarse density and $\eta$ the exterior field, derive the canonical conditional law

$$
\gamma_{B,N,p}(dU_B\mid\eta)=
\frac{v_{0,N,p}(U_B,\eta)\,d\mu_B(U_B)}
{\int v_{0,N,p}(V_B,\eta)\,d\mu_B(V_B)}.
$$

Specify the boundary variables, block geometry, distance, and observable class. Justify positivity, integrability, and any derivatives used. Trace which reference-action and activity budgets could control this normalized law when a distant boundary field changes. State an explicit decay or contraction inequality and determine whether its hypotheses are supplied by the actual selected history.

A useful first deliverable is either a derived boundary-sensitivity bound with its constants or a source-level demonstration that a specific proposed budget does not control the needed quantity. Both belong in a durable result record; neither alone is a mass-gap proof. Do not substitute a bare Wilson measure or discard the terminal covariance. The existing bare SU(2) single-link TV obstruction does not settle a block criterion or the large-$N$ coarse law.

Begin with source inspection and written analysis; estimate resource needs before simulation or formal replay. Numerical work may suggest or falsify a proposed finite-cutoff inequality, but a finite-time exponential fit cannot exclude an eventual slow tail or establish uniformity in the limits.

### Completion and handoff requirements

For each attempt, save the exact claim, derivation, verification commands actually run, source revision, remaining assumptions, and next discriminating task. Use the repository result template and link the result here and in the relevant directory index. Preserve failed attempts and update the agent prompt when a general failure lesson is established.

Step 3 is complete only when a dynamical argument proves the stated exponential target for the same reconstructed theory, with the required density, phase, and limit bridges. A conditional criterion, equivalent reformulation, generic Lean lemma, numerical fit, or list of agent outputs does not meet that milestone. Mass-gap claims additionally require checking the spectral conclusion against the intended public specification and independent review.

## Obligations

Trace the upstream Wilson/blocking estimates and the locality argument behind light_bound. Seek a justified fixed-physical-time contraction, exponential clustering sufficient for a dense family, or another mechanism that actually excludes a spectral interval. Track dependence on coupling, cutoff, volume, state, and phase.

## Evidence needed for the milestone

Provide an inequality with derived constants and all hypotheses, identify the exact upstream witnesses it applies to, and show why the estimate goes beyond the existing inverse-square bound. A conditional contraction lemma is useful but does not close this track.

## Failure criterion

A contraction factor approaching one, a rate vanishing with the regulators, or a relabeling of the desired gap as an assumption leaves the central problem open.

## Next contribution

The [averaged-covariance follow-up](../general/2026-11-13-T03-averaged-posterior-covariance/README.md) closes the unweighted-average shortcut: its bound holds for every input law, including a comparison family with a vanishing auxiliary gap. Next use actual dynamical information to control spatial posterior response or curvature tested against varying gradients. A plain expectation of the Hessian cannot replace that estimate.

Geometric follow-up: use the [actual posterior Hessian formula](../general/2026-11-13-T03-geometric-posterior-curvature/README.md) to derive a spatial estimate on its covariance blocks, retaining cancellation with the diagonal mean term. Alternatively, formulate a multiscale functional-inequality criterion that permits negative curvature regions. State which extra property of the actual prediction law excludes the [comparison-law obstruction](../negative-results/2026-11-13-T03-geometric-noise-only/README.md). Keep the auxiliary-diffusion-to-physical-correlation bridge explicit.

For the [new bare-law branch bound](../general/2026-11-11-T03-bare-branch-probability/README.md), first identify a specific RG step and derive a curvature-moment estimate under its actual fine input law. Preserve generated interactions and normalization. The geometric event inclusion already converts such a moment to frame-branch probability; do not substitute the bare Wilson law at later steps.

Determine whether the exact selected kernel has `predictor_cut < 1`. If it equals one, derive a cutoff/volume-uniform small-ball bound for positive connector-mean norm under the actual fine-field/site-tag law; the conditional conversion to integrated approximation error is now written. Then bound connected correlations of masked truncated observables, retaining shared frames, generated interactions, degree-dependent costs, and complete supports. Approximation convergence alone does not bound spatial covariance.

The upstream branch audit already supplies uniform frame control. A complementary bounded task is to establish quantitative applicability for the selected kernel and control the remaining predictor and covariance errors. The noise spectrum alone supplies no spatial estimate; preserve the finite-spin/support restrictions in its rate comparison and prove observable-class closure before iterating RG steps. Extend any successful bound to the transported insertions and required dense family in physical units.

## Active work

2026-11-13 follow-up handoff: `research/averaged-curvature-obstruction` builds on PR #11 and records the exact averaged identity and quantitative comparison-law obstruction. No worker remains running. The actual spatial posterior estimate remains unresolved.

2026-11-13 handoff: `research/geometric-posterior-curvature` records the written Hessian identity, exact diagnostics, and scoped counterexample. No running worker or recurring process remains after handoff. The actual posterior estimate and physical bridge remain open.

2026-11-11 handoff: `research/bare-wilson-branch-probability` records the bare-law probability calculation and its blocked-law limitation; no active worker is claimed after handoff. `research/upstream-branch-audit` records the producer correction, successful scoped replay, and a checked corollary. No ongoing worker is claimed. Follow actual kernel proofs and explicit quantitative hypotheses; do not reclassify upstream branch existence as a missing mass-gap estimate.

## Contribution ledger

- 2026-11-13 follow-up: [Exact averaged posterior covariance](../general/2026-11-13-T03-averaged-posterior-covariance/README.md) and [averaged-curvature obstruction](../negative-results/2026-11-13-T03-averaged-curvature-gap/README.md). Written volume-independent averaged bound; smooth gauge-invariant comparison laws retain distant loop covariance and have an auxiliary gap upper bound tending to zero. Exact diagnostics passed, no Lean proof or actual spatial estimate.

- 2026-11-13: [Geometric posterior-curvature derivation](../general/2026-11-13-T03-geometric-posterior-curvature/README.md) and [comparison-law obstruction](../negative-results/2026-11-13-T03-geometric-noise-only/README.md). The next geometric task is to bound spatial posterior covariance under the actual generated law, preserving diagonal cancellation, or justify a multiscale criterion permitting unfavorable curvature.

- 2026-11-12: [Curvature (Bakry–Émery) scope](../negative-results/2026-11-12-T03-bakry-emery-scope/README.md): written criterion $\beta<1/[4(d-1)]$ for the bare SU(2) Wilson law, Hessian assembled exactly and checked against finite differences; the threshold equals the notebook's cited strong-coupling coefficient and lies below the endpoint coupling `bar`. The displayed sufficient bound certifies only strong coupling; sharper or generated-measure bounds remain separate open tasks. Floating-point evidence only; no Lean proof or review.

- 2026-11-11, recorded: [Bare Wilson frame-branch probability](../general/2026-11-11-T03-bare-branch-probability/README.md). Written normalized-law bound of order log(beta)/beta for fixed patch and cutoff, uniform in torus volume; uses existing upstream axial existence. Cost grows like radius^10/cutoff^2. Finite geometry/scalar checks passed; no new Lean proof, blocked-law bridge, predictor-branch estimate, or spatial decay.

- 2026-11-11, recorded: [SU(2) frame uniqueness](../general/2026-11-11-T03-frame-uniqueness/README.md). Written `frame_cut <= 1/16` sufficient condition and quadratic certificate; nine frustrated noncommuting fixtures, 108 energy comparisons, and twelve nonreciprocal algebra cases passed exact checks. Builds on merged PR #4; no selected-history cutoff verification, Lean proof, independent review, or physical mass gap.
- 2026-11-11, recorded: [Minimizing-frame/axial-frame control](../general/2026-11-11-T03-frame-axial-control/README.md). Written pointwise SU(2) bound independent of patch size on the smooth branch, a conditional fine-loop replacement, and exact quaternion checks. The proof uses centre reanchoring and local optimality; [small energy alone is insufficient](../negative-results/2026-11-11-T03-frame-energy-only/README.md). Small-cutoff hypothesis, bad-branch probabilities, and spatial covariance remain unresolved for the selected history. No Lean proof or independent review.
- 2026-11-11, recorded: [Upstream branch correction and replay](../general/2026-11-11-T03-upstream-branch-audit/README.md). Existing uniform uniqueness, axial eligibility, and viable-kernel theorems located; 22 upstream modules and a `12*d` pairwise corollary passed Lean trust-zero checks. Retracts the earlier unsupported absence claim; no physical decay bound.
- 2026-11-11: [Spin-$j$ prediction mean and closure audit](../general/2026-11-11-T03-spin-j-prediction-mean/README.md): written SU(2) bond-tag mean for all spins; sharp bound $4j^2(1-r)$ between the minimizing predictor and the linear connector average; one-step formula valid for repeated links, conditional on site tags; source audit listing branch indicators, `1/card eligible`, and the minimizing frame as the uncontrolled non-polynomial mechanisms. Uses the upstream-supplied `Branches` conditions and `predictor_cut ≤ 1`. Exact integer-spin checks passed; AI cross-check only; no covariance bound, Lean proof, or independent review.

- 2026-11-11: [Peter–Weyl noise spectrum](../general/2026-11-11-T03-peter-weyl-noise-spectrum/README.md): written exact action of the one-step SU(2) noise on all observables (eigenvalues $I_{2j+1}/I_1$), explicit overlap covariance, and a rate-neutrality statement: on bounded finite-spin, link-disjoint classes the noise changes prefactors but preserves separation rates. Two-route rational enclosures and an exact $Q_8$ control passed. Cited Bessel inequalities not re-proved; no spatial decay, Lean proof, or independent review.

- 2026-11-11: [Actual-weight cutoff endpoint audit](../general/2026-11-11-T03-cutoff-endpoint/README.md). Written predictor-uniqueness characterization `c <= 1`, improved remainder, and conditional integrated bound; twelve integer convolution certificates, 792 rational remainder cases, and twelve exact radial integrals passed. [Endpoint controls](../negative-results/2026-11-11-T03-cutoff-endpoint/README.md) exclude a uniform norm margin at `c=1`. No actual fine-law small-ball or spatial estimate, Lean proof, or independent review.
- 2026-11-11: [SU(2) predictor average and masked truncation](../general/2026-11-11-T03-predictor-average/README.md). Written exact tag average and uniform truncation under the explicit extra hypothesis `0 < predictor_cut < 1`; 378 scalar rational checks and three noncommuting loop cases passed. [Threshold controls](../negative-results/2026-11-11-T03-predictor-threshold/README.md) preserve the mask and margin obligations. No spatial decay or Lean proof.
- 2026-11-11: [Exact one-step SU(2) loop transfer](../general/2026-11-11-T03-loop-noise-transfer/README.md): written source-matched covariance identity, conditional tag factorization for vertex-disjoint loops, rational coefficient enclosures, and exact finite controls. [Perimeter/separation and repeated-link controls](../negative-results/2026-11-11-T03-perimeter-not-separation/README.md) exclude noise-only and unproved iteration shortcuts. No spatial decay, Lean proof, or independent review.
- 2026-11-11: [Gauge-invariant conditional response](../general/2026-11-11-T03-gauge-orbit-response/README.md): source-matched invariance and written forest-conditioning identity reduce the target to joint exterior loop orbits. [Finite controls](../negative-results/2026-11-11-T06-gauge-only-mixing/README.md) rule out symmetry-only mixing and loss of joint loop information. Exact non-Abelian enumeration passed; no spatial decay or Lean proof.
- 2026-11-11: [Buffered posterior and local prediction response](../general/2026-11-11-T03-buffered-posterior/README.md): written source-matched conditional law, two-noise influence bound, and covariance reduction; exact symbolic identities and ten buffered-chain cases passed. No spatial decay, Lean proof, or independent review.
- 2026-11-11: [External YM3D transfer assessment](../general/2026-11-11-T03-ym3d-transfer-audit/README.md): inspected overlapping source audits and finite-gas comparison; two supplied checkers and 29 tests replayed successfully. Absolute gas bounds, 3D strong-coupling estimates, and conditional spectral criteria do not close the local posterior estimate.

- 2026-11-11: [Step 3 research plan](#step-3-exponential-decay-research-plan): explicit exponential target, tasks T03-A through T03-F, finite-block starting question, and evidence requirements. Documentation only; no new bound or verification claim.

- [Polynomial decay without a gap](../negative-results/2026-11-11-T06-polynomial-decay/README.md): restricts what may be inferred from the existing estimates.

- 2026-11-11: [Infrared cost audit](../general/2026-11-11-T03-infrared-cost-audit/README.md): Written extraction of localization/adjoint costs and a conditional approximation target; source not replayed.
- 2026-11-11: [Lean-checked conditional criteria](../general/2026-11-11-T02-uniform-projection-criterion/README.md): Six generic lemmas/controls checked with Lean 4.32.0 and --trust=0; no Yang–Mills application proved.
- 2026-11-11: [Cyclicity does not control adjoint costs](../negative-results/2026-11-11-T06-cyclicity-cost/README.md): Written operator-algebra counterexample; not a Yang–Mills model.
- 2026-11-11: [Strong-coupling theorem scope](../negative-results/2026-11-11-T04-strong-coupling-scope/README.md): Primary-source comparison; bounded coupling regime does not directly cover the running continuum family.

- 2026-11-11: [Checked Laplace support theorem and criterion audit](../general/2026-11-11-T02-laplace-support/README.md): standard scalar support equivalence and energy-window pullback checked; no new YM dynamical estimate.

- 2026-11-11: [Variable-time averaging](../general/2026-11-11-T03-variable-time-average/README.md): written rescaling gives quadratic localization cost; scalar optimization checked, physical bridge not formalized.
- 2026-11-11: [Massless local-field control](../negative-results/2026-11-11-T06-massless-locality/README.md): written counterexample to a locality-only inference, with scalar coefficient/scaling checks; not a Yang–Mills model.
- 2026-11-11: [Auxiliary resolvent gap audit](../negative-results/2026-11-11-T03-auxiliary-resolvent-gap/README.md): inspected block precision estimates do not supply retained-field correlations; exact Gaussian counterexample checked.

- 2026-11-11: [Connected-source bridge](../general/2026-11-11-T03-connected-source-bridge/README.md): cover-budget separation bound passed trust-zero checking; written identity isolates covariance of the actual normalized one-marker ratios under the retained vacuum measure.
- 2026-11-11: [Log/integration-order control](../negative-results/2026-11-11-T03-log-integration-order/README.md): exact finite Ising-chain calculation shows that a vanishing fixed-field mixed-log derivative does not bound the physical correlation uniformly.
- 2026-11-11: [Terminal RG covariance](../general/2026-11-11-T03-terminal-covariance/README.md): written recursion preserves source scaling and an explicit level-zero covariance; the coarse lattice still grows with volume. Exact finite-state check passed.
- 2026-11-11: [Single-link influence obstruction](../negative-results/2026-11-11-T03-single-link-influence/README.md): written all-volume SU(2) argument gives a row sum above 9/8 at beta at least one; 216 boundary pairs and rational arithmetic checked. This excludes the specified bare-law contraction test, not a mass gap or arbitrary coarse measures.
- 2026-11-11: [Coarse block conditional bounds](../general/2026-11-11-T03-block-conditional-bounds/README.md): written noise-kernel bound is uniform in cutoff and volume for a fixed link block, but has no distance decay. [Normalization and latent-noise controls](../negative-results/2026-11-11-T03-conditional-normalization/README.md) passed exact checks; relative spatial estimates remain open.

## Update instructions

Follow [the agent prompt](../../auto-research.md). Append dated links to result records, their exact outcome/evidence level, and any superseded result. Update the next contribution from the evidence, and link cross-track consequences without duplicating results. Preserve concurrent contributions.
