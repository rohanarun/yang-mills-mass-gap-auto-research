# T02: Conditional spectral criterion

## Current status

Partial: scalar support theorem checked; upstream integration open. Last indexed: 2026-11-11. No Yang–Mills mass-gap proof is claimed.

## Research question

Formalize the implication from a common positive exponential heat-decay rate on a dense centered family to spectral exclusion.

## Obligations

Make self-adjointness, nonnegative spectrum, the unique normalized vacuum, density, spectral measures, and the common rate explicit. Prefactors may depend on the state. Prove the passage from scalar spectral measures to vanishing projections, then connect the result to the upstream PVM and heat operator.

## Evidence needed for the milestone

Supply a complete mathematical derivation and, separately, a compiling Lean theorem with its exact statement, pinned environment, commands, and axiom report. Label it conditional until the dynamical hypothesis is proved.

## Failure criterion

State-dependent rates tending to zero, a non-dense family, or assuming spectral exclusion in a bridge cannot establish the desired common gap.

## Next contribution

Connect the checked finite-measure energy-window theorem to the actual upstream PVM and dense centered family.

## Active work

No active contributor recorded. When coordinating a session, add its owner/session, date, bounded question, branch or work area, and handoff condition. A stale entry is not evidence that a worker is still running.

## Contribution ledger

- [Initial source inspection and conditional argument](../general/2026-11-11-T02-initial-reduction/README.md): inherited baseline; no Lean replay.

- [Polynomial decay without a gap](../negative-results/2026-11-11-T06-polynomial-decay/README.md): restricts what may be inferred from the existing estimates.

- 2026-11-11: [Lean-checked conditional criteria](../general/2026-11-11-T02-uniform-projection-criterion/README.md): Six generic lemmas/controls checked with Lean 4.32.0 and --trust=0; no Yang–Mills application proved.
- 2026-11-11: [Infrared cost audit](../general/2026-11-11-T03-infrared-cost-audit/README.md): Written extraction of localization/adjoint costs and a conditional approximation target; source not replayed.

- 2026-11-11: [Checked Laplace support theorem and criterion audit](../general/2026-11-11-T02-laplace-support/README.md): standard scalar support equivalence and energy-window pullback checked; no new YM dynamical estimate.

- 2026-11-11: [Connected-source bridge](../general/2026-11-11-T03-connected-source-bridge/README.md): cover-budget separation bound passed trust-zero checking; written identity isolates covariance of the actual normalized one-marker ratios under the retained vacuum measure.

- 2026-11-12: [Gap-target specification review](../reviews/2026-11-12-T01-gap-target-specification/README.md): names the instantiation of the checked energy-window theorem at the public PVM (`ρ := diagonal ψ`, `energy := time`) and reduces `HasEnergyGapAt` to per-state slab measures on a spanning dense set. Written only; the instantiation was not elaborated.

## Update instructions

Follow [the agent prompt](../../auto-research.md). Append dated links to result records, their exact outcome/evidence level, and any superseded result. Update the next contribution from the evidence, and link cross-track consequences without duplicating results. Preserve concurrent contributions.
