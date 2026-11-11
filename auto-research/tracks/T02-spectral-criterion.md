# T02: Conditional spectral criterion

## Current status

Partial: written argument. Last indexed: 2026-11-11. No Yang–Mills mass-gap proof is claimed.

## Research question

Formalize the implication from a common positive exponential heat-decay rate on a dense centered family to spectral exclusion.

## Obligations

Make self-adjointness, nonnegative spectrum, the unique normalized vacuum, density, spectral measures, and the common rate explicit. Prefactors may depend on the state. Prove the passage from scalar spectral measures to vanishing projections, then connect the result to the upstream PVM and heat operator.

## Evidence needed for the milestone

Supply a complete mathematical derivation and, separately, a compiling Lean theorem with its exact statement, pinned environment, commands, and axiom report. Label it conditional until the dynamical hypothesis is proved.

## Failure criterion

State-dependent rates tending to zero, a non-dense family, or assuming spectral exclusion in a bridge cannot establish the desired common gap.

## Next contribution

Turn the existing written argument into a precise standalone theorem and list the missing Lean interfaces.

## Active work

No active contributor recorded. When coordinating a session, add its owner/session, date, bounded question, branch or work area, and handoff condition. A stale entry is not evidence that a worker is still running.

## Contribution ledger

- [Initial source inspection and conditional argument](../general/2026-11-11-T02-initial-reduction/README.md): inherited baseline; no Lean replay.

- [Polynomial decay without a gap](../negative-results/2026-11-11-T06-polynomial-decay/README.md): restricts what may be inferred from the existing estimates.

## Update instructions

Follow [the agent prompt](../../auto-research.md). Append dated links to result records, their exact outcome/evidence level, and any superseded result. Update the next contribution from the evidence, and link cross-track consequences without duplicating results. Preserve concurrent contributions.
