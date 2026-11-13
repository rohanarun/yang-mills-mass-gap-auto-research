# Research archive

Start with [auto-research.md](../auto-research.md), which defines the research tracks and agent work cycle. Every investigation must leave a result here and contribute a link and next step to its affected track ledger.

## Results

- [General research](general/README.md): derivations, audits, experiments, and handoffs.
- [Negative results](negative-results/README.md): obstructions, failed approaches, and inconclusive attempts.
- [Independent reviews](reviews/README.md): mathematical and verification reviews.
- [Result template](templates/result.md): required metadata, evidence, and lessons.

## Track ledgers

- [T01: Statement and specification audit](tracks/T01-statement-audit.md)
- [T02: Conditional spectral criterion](tracks/T02-spectral-criterion.md)
- [T03: Nonperturbative infrared estimates](tracks/T03-infrared-estimates.md), including the [Step 3 exponential-decay research plan](tracks/T03-infrared-estimates.md#step-3-exponential-decay-research-plan).
- [T04: Continuum, volume, and physical scales](tracks/T04-limits-and-scales.md)
- [T05: Selected phases and dense observable families](tracks/T05-phases-and-density.md)
- [T06: Counterexamples and negative results](tracks/T06-obstructions.md)
- [T07: Independent verification and proof integration](tracks/T07-verification-and-integration.md)

## Latest contributions

- [Gap-target specification review](reviews/2026-11-12-T01-gap-target-specification/README.md): first T01 review of the uncompiled gap target. Written argument that its energy-slab form is equivalent to an invariant-mass gap under the upstream axioms; the common gap across refinements is stronger than a per-hierarchy gap. Exact finite boost checks passed; nothing was checked in Lean and no mass-gap estimate is involved.

- [Bare Wilson frame-branch probability](general/2026-11-11-T03-bare-branch-probability/README.md): written fixed-patch failure bound uniform in total volume, using the existing axial theorem. It applies to the bare SU(2) law only; finite geometry/scalar diagnostics passed, no Lean proof or spatial decay.

- [Correction and scoped upstream replay](general/2026-11-11-T03-upstream-branch-audit/README.md): the branch conditions already have upstream proofs. Their 22-module chain and a frame-bound corollary passed Lean trust-zero checks. Full-construction replay and spatial decay remain open.
- Recorded: [SU(2) frame uniqueness certificate](general/2026-11-11-T03-frame-uniqueness/README.md). Written sufficient condition `frame_cut <= 1/16` and quantitative optimization-error bound modulo gauge; exact rational certificates passed. Builds on merged PR #4; not a physical spectral estimate.
- Recorded: [Patch-size-independent minimizing-frame control](general/2026-11-11-T03-frame-axial-control/README.md), with [energy-only failure control](negative-results/2026-11-11-T03-frame-energy-only/README.md). Written smooth-branch estimate and conditional replacement by explicit fine loops; exact quaternion checks passed. No bad-branch probability or spatial estimate.
- [Spin-$j$ prediction mean and closure audit](general/2026-11-11-T03-spin-j-prediction-mean/README.md): written bond-tag mean for every SU(2) spin, sharp bound $4j^2(1-r)$ on the predictor nonlinearity, and a source audit naming the remaining non-polynomial mechanisms (branch indicators, `1/card eligible`, `selected`). Exact checks passed; no spatial estimate.

- [Peter–Weyl spectrum of the blocking noise](general/2026-11-11-T03-peter-weyl-noise-spectrum/README.md): written exact one-step noise eigenvalues $I_{2j+1}/I_1$ for every SU(2) observable, including repeated and overlapping links. The noise is rate-neutral, so spatial decay must come from the fine law and prediction map. Exact checks passed; no spatial estimate.

- Recorded: [Actual-weight SU(2) cutoff endpoint audit](general/2026-11-11-T03-cutoff-endpoint/README.md), with [endpoint failure controls](negative-results/2026-11-11-T03-cutoff-endpoint/README.md). Derives the predictor condition's cutoff range, sharpens the remainder, and isolates an unproved fine-law small-ball hypothesis. Written derivations and exact finite checks; no spatial estimate or Lean proof.
- Recorded: [SU(2) predictor average and masked truncation](general/2026-11-11-T03-predictor-average/README.md), with [cutoff/margin controls](negative-results/2026-11-11-T03-predictor-threshold/README.md). Written tag average and a conditional geometric approximation bound; exact rational checks passed, spatial covariance remains open.
- [One-step SU(2) loop-noise transfer](general/2026-11-11-T03-loop-noise-transfer/README.md) and [failure controls](negative-results/2026-11-11-T03-perimeter-not-separation/README.md): written exact covariance transfer to averaged fine-field predictions; rational and finite checks passed, spatial estimate open.
- [Gauge-invariant response](general/2026-11-11-T03-gauge-orbit-response/README.md) and [symmetry-only mixing controls](negative-results/2026-11-11-T06-gauge-only-mixing/README.md): written forest identity narrows the target to joint loop information; exact finite non-Abelian checks passed, spatial decay remains open.
- [Buffered posterior and local hidden predictions](general/2026-11-11-T03-buffered-posterior/README.md): written two-noise bound and exact finite controls identify the local covariance that still needs spatial decay.
- [External YM3D transfer assessment](general/2026-11-11-T03-ym3d-transfer-audit/README.md): two checkers and 29 supplied tests replayed; finite-gas tools are useful, while normalization, dimension, and continuum bridges remain open.
- [Coarse block conditional bounds](general/2026-11-11-T03-block-conditional-bounds/README.md) and [normalization/latent-noise controls](negative-results/2026-11-11-T03-conditional-normalization/README.md): written source-derived bound without spatial decay; exact finite checks passed.

- [Checked Laplace support theorem and criterion audit](general/2026-11-11-T02-laplace-support/README.md): scalar support equivalence and energy-window pullback, with the dynamical obligation still explicit.

- [Lean-checked conditional criteria](general/2026-11-11-T02-uniform-projection-criterion/README.md): Six generic lemmas/controls checked with Lean 4.32.0 and --trust=0; no Yang–Mills application proved.
- [Infrared cost audit](general/2026-11-11-T03-infrared-cost-audit/README.md): Written extraction of localization/adjoint costs and a conditional approximation target; source not replayed.
- [Cyclicity does not control adjoint costs](negative-results/2026-11-11-T06-cyclicity-cost/README.md): Written operator-algebra counterexample; not a Yang–Mills model.
- [Strong-coupling theorem scope](negative-results/2026-11-11-T04-strong-coupling-scope/README.md): Primary-source comparison; bounded coupling regime does not directly cover the running continuum family.

## Baseline

The initial evidence remains in [research/mass-gap-20261111](../research/mass-gap-20261111/FirstPass.txt). The records below index it without implying new verification:

- [Conditional spectral reduction](general/2026-11-11-T02-initial-reduction/README.md).
- [Scalar polynomial-decay obstruction](negative-results/2026-11-11-T06-polynomial-decay/README.md).

No scheduler or autonomous process is installed by this archive or its prompt.
