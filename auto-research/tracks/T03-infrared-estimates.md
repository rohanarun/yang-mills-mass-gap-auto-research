# T03: Nonperturbative infrared estimates

## Current status

Partial: a written buffered-posterior reduction improves singleton noise influence to two noise factors and isolates the local hidden-prediction covariance; spatial decay and terminal mixing remain open. An external 3D program supplies useful finite checks but no imported decay estimate. Last indexed: 2026-11-11. No Yang–Mills mass-gap proof is claimed.

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

Bound the local hidden-prediction covariance with a distant likelihood ratio under the actual buffered posterior, preferably for the required gauge-invariant observable class. Preserve shared branch choices, generated interactions, and transported insertions. Do not require the entire hidden posterior to remain unchanged. An imported finite gas estimate must control relative normalization and any changed eligibility; the two-noise influence bound still has no distance decay.

## Active work

No active file ownership. 2026-11-11 handoff: buffered-posterior derivation and external 3D transfer assessment recorded below; the next bounded task is the local posterior spatial estimate.

## Contribution ledger

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
