# T06: Counterexamples and negative results

## Current status

Partial: scalar, cyclicity, massless-locality, block-gap, and bare SU(2) single-link influence, and conditional-normalization obstructions recorded. Last indexed: 2026-11-11. No Yang–Mills mass-gap proof is claimed.

## Research question

Find exact obstructions to proposed inferences and experiments that expose missing assumptions before expensive proof work.

## Obligations

Start from the scalar spectral density E exp(-E). Explore proposed improvements to polynomial bounds, state-dependent rates, finite-volume gaps, and phase averaging. State exactly which assumptions an example satisfies. Keep toy spectral models separate from full Yang–Mills theories.

## Evidence needed for the milestone

Record a reproducible counterexample, failed derivation, or inconclusive computation with the precise claim tested, evidence level, and a condition that could justify reopening the approach. Link it to affected tracks.

## Failure criterion

Failure to find a proof or a failed numerical experiment is not a proof of impossibility. A toy model cannot refute the full construction unless it meets every relevant hypothesis.

## Next contribution

Test candidate infrared/preparation estimates against the recorded counterexamples; distinguish dynamical hypotheses from qualitative density.

## Active work

No active contributor recorded. When coordinating a session, add its owner/session, date, bounded question, branch or work area, and handoff condition. A stale entry is not evidence that a worker is still running.

## Contribution ledger

- 2026-11-12: [Curvature (Bakry–Émery) scope](../negative-results/2026-11-12-T03-bakry-emery-scope/README.md): scope obstruction for curvature methods on the bare Wilson law; not a Yang–Mills counterexample.

- 2026-11-11: The [branch audit](../general/2026-11-11-T03-upstream-branch-audit/README.md) retracts the inference from an interface comment to absence of upstream proofs. Existing producers supply all three branch conditions; the physical covariance problem remains separate.
- 2026-11-11, recorded: [Frame certificate scope](../general/2026-11-11-T03-frame-uniqueness/README.md) separates exact uniqueness from approximate anchored stability. The uniform optimization-error bound is modulo common gauge rotation; the energy-only anchored counterexample remains valid. A positive certificate matrix does not establish a physical mass gap.
- 2026-11-11, recorded: [Energy-only frame control](../negative-results/2026-11-11-T03-frame-energy-only/README.md) fails uniformly in patch size: an anchored low-energy configuration can remain distance two away. The positive theorem uses exact minimization, including the centre variation. Fixed additive loop errors also do not imply spatial decay.
- 2026-11-11: [Peter–Weyl noise spectrum](../general/2026-11-11-T03-peter-weyl-noise-spectrum/README.md): the noise-only obstruction extends from simple loops to every observable; noise eigenvalues depend on spin content, never on separation. Written argument with exact checks; not a Yang–Mills counterexample.
- 2026-11-11: [Spin-$j$ prediction mean](../general/2026-11-11-T03-spin-j-prediction-mean/README.md): for $j\geq1$ the fallback prediction mean is not a function of the fundamental connector mean $M$; exact and analytic examples. Substituting $M$ into higher-spin observables is invalid.
- 2026-11-11: [Actual-weight cutoff endpoint control](../negative-results/2026-11-11-T03-cutoff-endpoint/README.md). The source convolution weights admit all radial connector means. Predictor uniqueness permits `c=1` with arbitrarily small active means; a quadratic small-ball law can still give only algebraic truncation decay. Connector-space and illustrative probability controls, not a counterexample to physical Yang–Mills decay.
- 2026-11-11: [Predictor threshold controls](../negative-results/2026-11-11-T03-predictor-threshold/README.md). The radial predictor moment map jumps at the strict cutoff; uniqueness does not prevent its norm from approaching zero. These are moment-map controls, not a proof that all actual selected configurations realize the boundary.
- 2026-11-11: [Perimeter/separation and repeated-link controls](../negative-results/2026-11-11-T03-perimeter-not-separation/README.md): exact finite non-Abelian noise leaves correlated loop signals, repeated-link factors fail, and overlapping loops retain conditional variance. No Yang–Mills counterexample; actual fine-law mixing remains open.
- 2026-11-11: [Gauge-only mixing and individual-trace controls](../negative-results/2026-11-11-T06-gauge-only-mixing/README.md): exact non-Abelian finite examples show that forest screening does not remove loop correlations and individual fundamental-loop traces need not determine a joint orbit. No Yang–Mills counterexample or mass-gap estimate.
- 2026-11-11: [Local versus global hidden posterior](../general/2026-11-11-T03-buffered-posterior/README.md): an exact independent-hidden-variable control has zero local response but nonzero whole-posterior TV. Buffered-chain checks isolate the hidden correlation factor from noise amplitude. These are finite probability controls, not Yang–Mills counterexamples.
- [Polynomial decay without a gap](../negative-results/2026-11-11-T06-polynomial-decay/README.md): scalar obstruction with exact symbolic checks.

- 2026-11-11: [Cyclicity does not control adjoint costs](../negative-results/2026-11-11-T06-cyclicity-cost/README.md): Written operator-algebra counterexample; not a Yang–Mills model.
- 2026-11-11: [Strong-coupling theorem scope](../negative-results/2026-11-11-T04-strong-coupling-scope/README.md): Primary-source comparison; bounded coupling regime does not directly cover the running continuum family.
- 2026-11-11: [Lean-checked conditional criteria](../general/2026-11-11-T02-uniform-projection-criterion/README.md): Six generic lemmas/controls checked with Lean 4.32.0 and --trust=0; no Yang–Mills application proved.

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
