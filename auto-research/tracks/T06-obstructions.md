# T06: Counterexamples and negative results

## Current status

Partial: scalar, cyclicity, massless-locality, and block-gap obstructions recorded. Last indexed: 2026-11-11. No Yang–Mills mass-gap proof is claimed.

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

## Update instructions

Follow [the agent prompt](../../auto-research.md). Append dated links to result records, their exact outcome/evidence level, and any superseded result. Update the next contribution from the evidence, and link cross-track consequences without duplicating results. Preserve concurrent contributions.
