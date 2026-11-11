# T04: Continuum, volume, and physical scales

## Current status

Partial: coupling and prefactor scope audited; limit transfer open. Last indexed: 2026-11-11. No Yang–Mills mass-gap proof is claimed.

## Research question

Prove that a candidate positive rate survives the cutoff and infinite-volume limits used by the construction.

## Obligations

Write the exact order and type of convergence, normalization of physical time and lattice spacing, state identifications, and behavior of vacuum subtraction. Keep the rate positive along the actual chosen subsequences. Do not exchange limits or take operator-norm limits without a theorem.

## Evidence needed for the milestone

Give a limit-transfer lemma applicable to the same upstream family, with every uniformity assumption visible and separately sourced. Identify which assumptions remain dependent on T03.

## Failure criterion

A positive gap only at finite volume, a rate tending to zero, or positivity only in lattice units is insufficient. A divergent chosen prefactor alone need not block a support-first limit argument once a common spectral threshold is proved; document which transfer argument is used.

## Next contribution

Prove the correct spectral-measure convergence with one positive rate. Distinguish direct heat-bound transfer from support-first arguments, which can replace prefactors by total masses.

## Active work

No active contributor recorded. When coordinating a session, add its owner/session, date, bounded question, branch or work area, and handoff condition. A stale entry is not evidence that a worker is still running.

## Contribution ledger

- 2026-11-11, proposed for review: [Predictor-average truncation](../general/2026-11-11-T03-predictor-average/README.md) gives a written uniform approximation error at fixed loop length and cutoff margin `0<c<1`. That margin is not established for the fixed source kernel; truncation degree is not physical time, and no continuum correlation bound follows.
- 2026-11-11: [One-step loop-noise transfer](../general/2026-11-11-T03-loop-noise-transfer/README.md): scalar coefficient has a written uniform bound at fixed history/level, but its exponent is loop perimeter, not separation or physical time. Iterating levels needs a proved observable expansion and scale costs; no limit estimate obtained.
- 2026-11-11: [Buffered posterior reduction](../general/2026-11-11-T03-buffered-posterior/README.md): written two-noise bound remains uniform for fixed link counts but has no spatial rate; cutoff/volume-uniform local posterior covariance remains open.
- 2026-11-11: [External YM3D transfer assessment](../general/2026-11-11-T03-ym3d-transfer-audit/README.md): 3D fixed-spacing strong-coupling estimates cannot be imported into the 4D continuum target without matching laws and scale dependence; supplied arithmetic/scope tests replayed.
No contributions recorded yet.

- 2026-11-11: [Infrared cost audit](../general/2026-11-11-T03-infrared-cost-audit/README.md): Written extraction of localization/adjoint costs and a conditional approximation target; source not replayed.
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
