# Yang–Mills Mass Gap Auto-Research

**Correction, 2026-11-11:** [PR #6](https://github.com/rohanarun/yang-mills-mass-gap-auto-research/pull/6) locates and replays the existing upstream branch producers. Uniform frame uniqueness, predictor uniqueness, and axial eligibility are already supplied upstream. Earlier absence claims are retracted; this PR provides an explicit SU(2) calculation to compare with existing results, not the first proof of uniform frame control or branch existence.

An initial investigation of what additional estimate could establish a positive mass gap for the construction in [OpenAI-YM-20261028](https://github.com/yang-mills-group/OpenAI-YM-20261028).

**This repository does not prove the Yang–Mills mass gap.** It contains a standard conditional spectral argument, an explicit obstruction to inferring a gap from polynomial decay, and an uncompiled Lean specification for a stronger target.

## What is established here?

| Item | Status |
| --- | --- |
| Polynomial decay alone does not imply a spectral gap | Explicit scalar spectral example; its integrals were checked symbolically |
| A common exponential decay rate on a dense family implies a gap | Written full argument; scalar support and generic projection components checked; actual Yang–Mills/dense-state integration remains open |
| Positive mass gap for the upstream Yang–Mills construction | **Unproved** |
| Generic projection/Laplace tools | Six lemmas/controls checked with Lean 4.32.0 and `--trust=0`; [receipt](auto-research/general/2026-11-11-T02-uniform-projection-criterion/verification.json) |
| Scalar Laplace support equivalence | Checked with Lean 4.32.0 and `--trust=0`, including integrability and the energy-window pullback; [receipt](auto-research/general/2026-11-11-T02-laplace-support/verification.json) |
| Proposed Yang–Mills Lean gap target | Definitions only; **not compiled** |
| Independent replay of upstream Lean proofs | **Not performed** |

The initial inspection uses upstream revision [`3456e5e`](https://github.com/yang-mills-group/OpenAI-YM-20261028/tree/3456e5e75cf8d4cd558955a5c7638fba2d68f464). The upstream README explicitly leaves positive mass gap outside its claim. Its verification reports are not independent verification by this project.

## Research progress — 11 November 2026

**Verified formal infrastructure; the Yang–Mills mass gap remains unproved.**

- [Six initial generic lemmas and controls](auto-research/general/2026-11-11-T02-uniform-projection-criterion/README.md) passed Lean 4.32.0 with `--trust=0`, covering projection contraction and scalar exponential comparisons.
- The [new Laplace support theorem](auto-research/general/2026-11-11-T02-laplace-support/README.md) now checks the full finite-measure equivalence: an integrable exponential Laplace bound at rate `m` is equivalent to no measure below `m`. It also checks the sharp endpoint and the pullback to a positive-energy window. [Proof receipt](auto-research/general/2026-11-11-T02-laplace-support/verification.json).
- A [formal criterion audit](auto-research/general/2026-11-11-T02-laplace-support/CriterionAudit.lean) confirms that the proposed strict approximation condition is itself equivalent to a zero projection. The condition must be derived from independent dynamical estimates; simply proposing it does not resolve the gap.
- The [infrared source audit](auto-research/general/2026-11-11-T03-infrared-cost-audit/README.md) isolates the missing localization/adjoint-state cost. [Cyclicity alone does not supply it](auto-research/negative-results/2026-11-11-T06-cyclicity-cost/README.md), and a [cited strong-coupling lattice theorem does not directly cover the running continuum regime](auto-research/negative-results/2026-11-11-T04-strong-coupling-scope/README.md).
- A [variable-time refinement](auto-research/general/2026-11-11-T03-variable-time-average/README.md) improves the written localization cost from cubic to quadratic in the support radius. Lean checks the scalar optimization; the measure-rescaling bridge remains a written derivation. The estimate is still polynomial.
- Two further controls show why more dynamics is needed: a [massless local field](auto-research/negative-results/2026-11-11-T06-massless-locality/README.md) satisfies the relevant locality assumptions without a gap, and an [auxiliary block gap](auto-research/negative-results/2026-11-11-T03-auxiliary-resolvent-gap/README.md) need not control the retained modes. Exact scalar and matrix checks passed.
- A [connected-source audit](auto-research/general/2026-11-11-T03-connected-source-bridge/README.md) now derives exponential separation decay for coefficients satisfying the upstream cover-budget hypotheses; the abstract series bound passed Lean `--trust=0`. The actual trajectory definitions leave an additional retained-field covariance in the physical connected coefficient. An [exact local Ising-chain control](auto-research/negative-results/2026-11-11-T03-log-integration-order/README.md) confirms why a fixed-field logarithmic bound cannot remove it.
- The [terminal RG audit](auto-research/general/2026-11-11-T03-terminal-covariance/README.md) gives a written covariance decomposition with the correct source scaling. The coarse endpoint remains a growing-volume interacting measure, so its covariance requires an additional mixing estimate. Exact finite-state checks passed; no new dynamical bound was obtained.
- A [single-link influence audit](auto-research/negative-results/2026-11-11-T03-single-link-influence/README.md) rules out the specified total-variation contraction test for bare four-dimensional SU(2) at beta at least one: a written lower bound exceeds the threshold. All 216 finite boundary-pair checks and exact rational checks passed. This is a route obstruction, not a mass-gap estimate; the generated coarse measures remain open.
- A [coarse block audit](auto-research/general/2026-11-11-T03-block-conditional-bounds/README.md) derives a written conditional-law bound from the actual noise kernel, uniform in cutoff and volume for fixed block size. It has no distance decay. [Exact normalization and latent-field controls](auto-research/negative-results/2026-11-11-T03-conditional-normalization/README.md) identify why small activities or local smoothing alone cannot supply the missing spatial estimate.

- A [buffered-posterior refinement](auto-research/general/2026-11-11-T03-buffered-posterior/README.md) improves the written singleton noise influence bound to two noise factors and isolates the local hidden-prediction covariance that needs spatial control. Exact symbolic identities and ten rational buffered-chain cases passed. The estimate still has no distance decay and has not been formalized in Lean.
- An [assessment of the external YM3D verification program](auto-research/general/2026-11-11-T03-ym3d-transfer-audit/README.md) replayed two supplied checkers and 29 tests successfully. Its finite-gas tools and overlapping source audit are useful; the inspected material does not supply the missing normalized posterior estimate or a 4D continuum mass gap.

- A [gauge-invariant response audit](auto-research/general/2026-11-11-T03-gauge-orbit-response/README.md) narrows the conditional target: observing only a forest of links leaves gauge-invariant expectations unchanged; general exterior data retain joint loop information. [Exact non-Abelian controls](auto-research/negative-results/2026-11-11-T06-gauge-only-mixing/README.md) confirm that symmetry alone does not imply decay and individual loop traces can omit relevant information. This is a written symmetry reduction, not a dynamical decay estimate or Lean proof.

- An [exact written one-step SU(2) loop formula](auto-research/general/2026-11-11-T03-loop-noise-transfer/README.md) transfers covariance of vertex-disjoint fundamental loops to explicit averaged predictions under the fine-field law. The known noise coefficient suppresses perimeter, not separation. Rational coefficient enclosures and finite non-Abelian checks passed; [repeated-link and noise-only shortcuts fail](auto-research/negative-results/2026-11-11-T03-perimeter-not-separation/README.md). The fine-field spatial covariance remains unbounded by this argument.

- A [Peter–Weyl diagonalization of the blocking noise](auto-research/general/2026-11-11-T03-peter-weyl-noise-spectrum/README.md) gives the exact one-step noise eigenvalues $I_{2j+1}(\kappa)/I_1(\kappa)$ for every SU(2) observable, including repeated and overlapping links. On link-disjoint classes with bounded spin cutoff and support size, it shows the noise changes prefactors but preserves separation rates. Two independent rational enclosures and an exact $Q_8$ control passed. This is standard harmonic analysis applied to the source kernel; the spatial covariance of the prediction observables remains unbounded.

- A [spin-$j$ prediction-mean record](auto-research/general/2026-11-11-T03-spin-j-prediction-mean/README.md) gives the bond-tag average of the prediction for every SU(2) spin, a sharp written bound $4j^2(1-r)$ between the nonlinear minimizing predictor and the linear connector average, and a source audit of where non-polynomial dependence on the fine field enters. It assumes the upstream `Branches` hypotheses, which the source leaves unproved. Exact integer-spin checks passed. Branch indicators and the minimizing frame remain uncontrolled, and no covariance bound follows.

- Merged in PR #1: the [SU(2) predictor-average calculation](auto-research/general/2026-11-11-T03-predictor-average/README.md) makes the nonlinear tag average explicit and gives a cutoff-preserving geometric truncation under the additional hypothesis `0 < predictor_cut < 1`. Exact rational checks passed. [Threshold controls](auto-research/negative-results/2026-11-11-T03-predictor-threshold/README.md) show why the mask and a norm margin cannot be discarded. No spatial covariance bound or Lean proof was obtained.

- Merged in PR #3: the [actual-weight cutoff audit](auto-research/general/2026-11-11-T03-cutoff-endpoint/README.md) derives `predictor_cut <= 1` from the fundamental SU(2) predictor-uniqueness condition and sharpens the approximation remainder. At cutoff one, a conditional integrated bound replaces the unavailable uniform margin, but its fine-law small-ball hypothesis remains unproved. Twelve convolution certificates, 792 rational remainder cases, and twelve radial integrals passed exact checks. These are written derivations and finite controls, not spatial decay or a Lean proof.

- Proposed for PR review: a [minimizing-frame estimate](auto-research/general/2026-11-11-T03-frame-axial-control/README.md) removes the patch-size factor from the comparison with an explicit axial frame, for fundamental SU(2) on the smooth branch and a sufficiently small frame cutoff. Exact quaternion controls passed. This yields a conditional replacement by fine Wilson loops; bad-branch probabilities, frame uniqueness, and spatial covariance remain open. The theorem is written, not formalized in Lean.

- Proposed for dependent PR review: a [SU(2) uniqueness certificate](auto-research/general/2026-11-11-T03-frame-uniqueness/README.md) gives a written sufficient condition for the source's minimizing-frame uniqueness clause: `0 < frame_cut <= 1/16`. It also controls optimization error modulo a common gauge rotation. Exact finite matrix checks passed. This depends on PR #4 and does not verify the chosen history's cutoff, the remaining branch clauses, or spatial decay; no Lean proof or independent review.

The checked Lean declarations report only `propext`, `Classical.choice`, and `Quot.sound`. These results are publishable as a reproducible research notebook and formalization contribution; **no new Yang–Mills mass-gap theorem or mathematical novelty is claimed**. Independent review, a novelty assessment, full upstream replay, and the essential nonperturbative estimate remain outstanding. The next milestone is an estimate derived for the actual hierarchy that stays positive through the continuum and infinite-volume limits—not a larger count of generic lemmas.

## The starting point

The source theorem [`light_bound`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/EveryPhase/Light.lean#L221) bounds low-energy spectral weight for finite word states by a constant times the square of the energy threshold. The theorem [`inverse_square`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/EveryPhase/Decay.lean#L173) gives

$$
0\leq\langle\psi,(e^{-tH}-P_0)\psi\rangle\leq C_\psi t^{-2},\qquad t\geq1.
$$

Here $P_0$ is initially the full zero-energy projection. The upstream vacuum argument identifies that projection with the vacuum line. These are source-level observations, pending independent replay.

## Why polynomial decay is insufficient

Consider the finite positive measure

$$
d\mu(E)=Ee^{-E}\,dE,\qquad E>0.
$$

It satisfies

$$
\mu((0,u])=1-(1+u)e^{-u}\leq\frac{u^2}{2},\qquad
\int_0^\infty e^{-tE}\,d\mu(E)=\frac{1}{(1+t)^2}.
$$

Every interval $(0,u)$ nevertheless has positive measure. Thus quadratic control of low-energy weight and inverse-square heat decay allow spectral weight arbitrarily close to zero.

The notes realize this as a nonnegative self-adjoint operator with a unique zero-energy vacuum and no positive gap. **This is an obstruction to a spectral inference, not a counterexample to the full Yang–Mills construction.** It does not satisfy all of the upstream Wilson, field-theoretic, OPE, and trace requirements.

## The conditional route to a gap

Let $H\geq0$ be self-adjoint, with normalized vacuum $\Omega$ and $\ker H=\mathbb C\Omega$. Suppose a dense subset $D$ of $\Omega^\perp$ satisfies

$$
\exists m>0\;\;\forall\psi\in D\;\;\exists C_\psi\geq0\;\;\forall t\geq1:\quad
\langle\psi,e^{-tH}\psi\rangle\leq C_\psi e^{-mt}.
$$

The prefactor can depend on the state. **The positive rate must be common to the dense family.**

For $0<a<m$, spectral positivity gives

$$
e^{-at}\mu_\psi((0,a])\leq\langle\psi,e^{-tH}\psi\rangle
\leq C_\psi e^{-mt}.
$$

Taking $t\to\infty$ forces $\mu_\psi((0,a])=0$. Letting $a\uparrow m$, then using density and boundedness of spectral projections, gives $P((0,m))=0$ and

$$
\sigma(H)\subseteq\{0\}\cup[m,\infty).
$$

This is a standard reduction. The unresolved mathematical work is to derive its exponential estimate from Yang–Mills dynamics with a rate that survives cutoff removal and infinite volume.

## Research target

A concrete intermediate target is strict contraction at a fixed physical Euclidean time:

$$
\left\|e^{-\tau H}\big|_{\Omega^\perp}\right\|\leq q<1,\qquad \tau>0.
$$

This would give a gap of at least $-\log(q)/\tau$. At continuum level it reformulates the gap; it does not supply a new proof. Its possible value is as a target for quantitative estimates before taking limits.

The remaining obligations include a common positive physical rate, the correct vacuum subtraction, control of both limiting operations, and a dense family of states. An estimate for only the stress-trace channel does not automatically cover the whole Hilbert space. An unselected phase average does not automatically imply the corresponding estimate for the selected phase.

## Research workflow

Agents should start with [auto-research.md](auto-research.md), choose a research track, and record every investigation—including negative and inconclusive results—in [auto-research/](auto-research/README.md). Each result must update its track ledger with evidence, remaining assumptions, and a concrete next question. The prompt and archive do not launch a background job.

## Files

- [First-pass notes](research/mass-gap-20261111/FirstPass.txt): detailed argument, operator example, source locations, and remaining obligations.
- [Lean target](research/mass-gap-20261111/MassGapTarget.lean): proposed gap and strengthened existence definitions, with no proof asserted.
- [Symbolic check](research/mass-gap-20261111/check_obstruction.py): exact integral and asymptotic calculations for the scalar example.
- [Recorded output](research/mass-gap-20261111/obstruction-check.json): output from the symbolic check.
- [Provenance](research/mass-gap-20261111/provenance.json): upstream revision, source hashes, and verification status.

## Reproduce the symbolic check

With Python 3 and `venv` available, from this repository's root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python research/mass-gap-20261111/check_obstruction.py
```

The check verifies the total mass, low-energy integral, heat integral, and failure of every positive exponential decay rate for the scalar example. It does not verify the Yang–Mills construction or the spectral theorem argument in Lean.

`MassGapTarget.lean` imports `ChallengeSpec` from the pinned upstream project. This repository does not bundle that project's dependencies or provide a standalone Lean build. Upstream pins Lean **4.32.0**. The target remains uncompiled and also requires a mathematical review of its specification; it asks for a common gap per chosen Wilson family across volume refinements, a stronger requirement than a separate gap for each resulting hierarchy.

## Contributors

Contributions from people and AI-assisted researchers are welcome. Start with [auto-research.md](auto-research.md) and [CONTRIBUTING.md](CONTRIBUTING.md). Useful negative results, corrections, and independent reviews receive credit alongside positive results.

Snapshot: **11 November 2026**. Contribution state and mathematical verification are separate. Being on `main` does not establish a Yang–Mills mass gap.

| Work | Contributor | Contribution | Verification status | State |
| --- | --- | --- | --- | --- |
| [Initial investigation](research/mass-gap-20261111/FirstPass.txt) | [Rohan Arun (@rohanarun)](https://github.com/rohanarun), with OpenAI Codex assistance | Source inspection, standard conditional spectral criterion, and proposed gap specification | Written argument; Lean target uncompiled; upstream proofs not independently replayed | On main |
| [Polynomial-decay obstruction](auto-research/negative-results/2026-11-11-T06-polynomial-decay/README.md) | Rohan Arun, with OpenAI Codex assistance | Explicit scalar spectral example showing why polynomial decay alone does not imply a gap | Exact symbolic integral/asymptotic checks; not a counterexample to the full Yang–Mills construction | On main |
| [Research tracks and archive](auto-research.md) | Rohan Arun, with OpenAI Codex assistance | Seven research tracks, agent instructions, result template, and preservation of negative results | Documentation contribution; no mathematical verification implied | On main |
| [Conditional Lean tools](auto-research/general/2026-11-11-T02-uniform-projection-criterion/README.md) | Rohan Arun, with OpenAI Codex assistance | Five generic criteria and a non-strict-bound counterexample | Lean 4.32.0 trust-zero check passed; no YM application proved | On main |
| [Infrared source audit](auto-research/general/2026-11-11-T03-infrared-cost-audit/README.md) and related obstructions | Rohan Arun, with OpenAI Codex assistance | Extracted preparation costs, a cyclicity counterexample, and a coupling-regime comparison | Written/source-level analysis; coefficient algebra checked; independent review pending | On main |
| [Laplace support and criterion audit](auto-research/general/2026-11-11-T02-laplace-support/README.md) | Rohan Arun, with OpenAI Codex assistance | Finite-measure support equivalence, energy-window pullback, and criterion-strength audit | Lean 4.32.0 trust-zero checks passed; standard results, no new YM estimate | On main |
| [Time-average refinement and infrared controls](auto-research/general/2026-11-11-T03-variable-time-average/README.md) | Rohan Arun, with OpenAI Codex assistance | Written localization improvement, massless-field control, and auxiliary resolvent audit | Scalar optimization checked in Lean; scalar/matrix checks passed; no YM gap or independent review | On main |
| [Connected-source bridge and integration control](auto-research/general/2026-11-11-T03-connected-source-bridge/README.md) | Rohan Arun, with OpenAI Codex assistance | Conditional coefficient decay, source-matched covariance audit, and [terminal RG decomposition](auto-research/general/2026-11-11-T03-terminal-covariance/README.md) | Abstract series bound checked in Lean; exact finite-chain checks; no retained-field decay or YM gap | On main |
| [Single-link influence obstruction](auto-research/negative-results/2026-11-11-T03-single-link-influence/README.md) | Rohan Arun, with OpenAI Codex assistance | Bare SU(2) contraction lower bound and conditional perturbation tolerance | Written analytic argument; exact geometry/arithmetic checked; no Lean proof or independent review | On main |
| [Coarse block conditional audit](auto-research/general/2026-11-11-T03-block-conditional-bounds/README.md) | Rohan Arun, with OpenAI Codex assistance | Uniform finite-block noise bound, exact-coverage audit, and normalization/latent-field controls | Written source application; exact symbolic/rational checks; no spatial decay, Lean proof, or independent review | On main |
| [Buffered posterior and local response](auto-research/general/2026-11-11-T03-buffered-posterior/README.md) | Rohan Arun, with OpenAI Codex assistance | Exact conditional-law reduction and written two-noise influence bound | Exact finite checks passed; no spatial decay, Lean proof, or independent review | On main |
| [External YM3D assessment](auto-research/general/2026-11-11-T03-ym3d-transfer-audit/README.md) | Rohan Arun, with OpenAI Codex assistance; external authors credited in the record | Scoped source assessment and replay of supplied checkers | Two checkers and 29 tests passed; external analytic claims not verified | On main |
| [Gauge-invariant response](auto-research/general/2026-11-11-T03-gauge-orbit-response/README.md) | Rohan Arun, with OpenAI Codex assistance | Source-matched forest identity, joint-loop reduction, and finite controls | Written argument and exact non-Abelian checks; no spatial decay, Lean proof, or independent review | On main |
| [One-step SU(2) loop transfer](auto-research/general/2026-11-11-T03-loop-noise-transfer/README.md) | Rohan Arun, with OpenAI Codex assistance | Actual-kernel loop covariance identity and conditional tag factorization | Written derivation, rational coefficient enclosures, exact finite controls; no spatial decay or Lean proof | On main |
| [Peter–Weyl noise spectrum](auto-research/general/2026-11-11-T03-peter-weyl-noise-spectrum/README.md) | Rohan Arun, with Claude (Anthropic) assistance | Exact one-step SU(2) noise eigenvalues on all observables, overlap covariance, and rate-neutrality statement | Written derivation; two-route rational enclosures and exact finite control passed; cited Bessel inequalities not re-proved; no spatial decay, Lean proof, or independent review | Included in PR #2 |
| [Spin-$j$ prediction mean](auto-research/general/2026-11-11-T03-spin-j-prediction-mean/README.md) | Rohan Arun, with Claude (Anthropic) assistance | Bond-tag mean for all spins, sharp predictor bound, one-step sector formula, closure audit | Written derivation; exact integer-spin checks passed; AI cross-check only; relies on unproved upstream `Branches` hypotheses; no covariance bound, Lean proof, or independent review | Included in PR #2 |
| [SU(2) predictor average](auto-research/general/2026-11-11-T03-predictor-average/README.md) | Rohan Arun, with OpenAI Codex assistance | Exact bond-tag mean, conditional masked truncation, and threshold controls | Written argument and rational checks; cutoff margin and spatial covariance remain open | Merged in PR #1 |
| [Actual-weight cutoff endpoint](auto-research/general/2026-11-11-T03-cutoff-endpoint/README.md) | Rohan Arun, with OpenAI Codex assistance | Cutoff characterization, improved remainder, and conditional integrated approximation | Written argument and exact finite controls; actual fine-law small-ball and spatial estimates remain open | Merged in PR #3 |
| [SU(2) frame control](auto-research/general/2026-11-11-T03-frame-axial-control/README.md) | Rohan Arun, with OpenAI Codex assistance | Written minimizing-frame bound without patch-size loss and conditional fine-loop replacement | Exact finite quaternion controls; no probability bound, spatial decay, Lean proof, or independent review | Proposed for PR review |
| [SU(2) frame uniqueness](auto-research/general/2026-11-11-T03-frame-uniqueness/README.md) | Rohan Arun, with OpenAI Codex assistance | Written sufficient cutoff condition and quadratic certificate; optimization-error bound modulo gauge | Exact finite certificates; depends on PR #4; no source formalization or physical mass gap | Proposed dependent PR |

[Full contributor credits](CONTRIBUTORS.md) record authorship, AI assistance, inherited work, and future contributions. Credits remain when results are corrected or superseded; their evidence status is updated.

The underlying construction is the work credited by [yang-mills-group/OpenAI-YM-20261028](https://github.com/yang-mills-group/OpenAI-YM-20261028). This repository is an independent project, not an official OpenAI publication or an endorsement by upstream authors. The spectral criterion is standard and is not claimed as a novel theorem.

## License

The original code and documentation in this repository are licensed under the [Apache License 2.0](LICENSE). See [NOTICE](NOTICE) for attribution. Referenced upstream work and external dependencies retain their own licenses and notices; this repository does not relicense them.
