# T03: Nonperturbative infrared estimates

## Current status

Partial: source costs audited; dynamical estimate still open. Last indexed: 2026-11-11. No Yang–Mills mass-gap proof is claimed.

## Research question

Derive a new quantitative Yang–Mills estimate strong enough to yield a positive physical decay rate.

## Obligations

Trace the upstream Wilson/blocking estimates and the locality argument behind light_bound. Seek a justified fixed-physical-time contraction, exponential clustering sufficient for a dense family, or another mechanism that actually excludes a spectral interval. Track dependence on coupling, cutoff, volume, state, and phase.

## Evidence needed for the milestone

Provide an inequality with derived constants and all hypotheses, identify the exact upstream witnesses it applies to, and show why the estimate goes beyond the existing inverse-square bound. A conditional contraction lemma is useful but does not close this track.

## Failure criterion

A contraction factor approaching one, a rate vanishing with the regulators, or a relabeling of the desired gap as an assumption leaves the central problem open.

## Next contribution

Derive a preparation-cost or decay bound from independent Yang–Mills dynamics. The abstract strict approximation condition is equivalent to projection vanishing.

## Active work

No active contributor recorded. When coordinating a session, add its owner/session, date, bounded question, branch or work area, and handoff condition. A stale entry is not evidence that a worker is still running.

## Contribution ledger

- [Polynomial decay without a gap](../negative-results/2026-11-11-T06-polynomial-decay/README.md): restricts what may be inferred from the existing estimates.

- 2026-11-11: [Infrared cost audit](../general/2026-11-11-T03-infrared-cost-audit/README.md): Written extraction of localization/adjoint costs and a conditional approximation target; source not replayed.
- 2026-11-11: [Lean-checked conditional criteria](../general/2026-11-11-T02-uniform-projection-criterion/README.md): Six generic lemmas/controls checked with Lean 4.32.0 and --trust=0; no Yang–Mills application proved.
- 2026-11-11: [Cyclicity does not control adjoint costs](../negative-results/2026-11-11-T06-cyclicity-cost/README.md): Written operator-algebra counterexample; not a Yang–Mills model.
- 2026-11-11: [Strong-coupling theorem scope](../negative-results/2026-11-11-T04-strong-coupling-scope/README.md): Primary-source comparison; bounded coupling regime does not directly cover the running continuum family.

- 2026-11-11: [Checked Laplace support theorem and criterion audit](../general/2026-11-11-T02-laplace-support/README.md): standard scalar support equivalence and energy-window pullback checked; no new YM dynamical estimate.

## Update instructions

Follow [the agent prompt](../../auto-research.md). Append dated links to result records, their exact outcome/evidence level, and any superseded result. Update the next contribution from the evidence, and link cross-track consequences without duplicating results. Preserve concurrent contributions.
