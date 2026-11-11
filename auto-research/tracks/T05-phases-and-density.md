# T05: Selected phases and dense observable families

## Current status

Partial: scalar energy-window bridge checked; phase/density application open. Last indexed: 2026-11-11. No Yang–Mills mass-gap proof is claimed.

## Research question

Transport candidate bounds to the selected phase and a dense vacuum-orthogonal family in its Hilbert space.

## Obligations

Audit the character decomposition, positivity, full support, continuity, vacuum subtraction, and the finite-word density argument. Distinguish full zero-energy projection from the vacuum projection until their equality is established. A stress-trace channel alone requires a separate density argument.

## Evidence needed for the milestone

Prove a phase-transfer or density lemma with explicit hypotheses and attach it to the same hierarchy used by the proposed gap theorem. Record precisely where all-phase, almost-everywhere, or selected-phase conclusions hold.

## Failure criterion

A raw averaged correlation bound, cancellation between phases, or one non-cyclic observable does not establish a bound for all physical states.

## Next contribution

Connect positive-energy pushforwards to the actual selected phase and a dense family, retaining all dynamical hypotheses.

## Active work

No active contributor recorded. When coordinating a session, add its owner/session, date, bounded question, branch or work area, and handoff condition. A stale entry is not evidence that a worker is still running.

## Contribution ledger

- 2026-11-11: [One-step loop-noise transfer](../general/2026-11-11-T03-loop-noise-transfer/README.md): averaged predictions are gauge invariant by the integrated kernel identity; the scalar formula is restricted to fundamental SU(2), and simple edge-distinct loops are not proved sufficient for the continuum dense family. The transformed observable class is not shown closed under iteration.
- 2026-11-11: [Peter–Weyl noise spectrum](../general/2026-11-11-T03-peter-weyl-noise-spectrum/README.md): spin-network functions form a dense gauge-invariant family on which one step of SU(2) noise is explicit. Density in the reconstructed Hilbert space and the prediction half are not addressed.
- 2026-11-11: [Gauge-orbit response audit](../general/2026-11-11-T03-gauge-orbit-response/README.md): source-matched invariance of transported insertions and written orbit reduction. Individual fundamental-loop traces can omit relative non-Abelian information; no dense-family or continuum phase identification was proved.
- [Initial source inspection and conditional argument](../general/2026-11-11-T02-initial-reduction/README.md): inherited baseline; no Lean replay.

- 2026-11-11: [Infrared cost audit](../general/2026-11-11-T03-infrared-cost-audit/README.md): Written extraction of localization/adjoint costs and a conditional approximation target; source not replayed.
- 2026-11-11: [Cyclicity does not control adjoint costs](../negative-results/2026-11-11-T06-cyclicity-cost/README.md): Written operator-algebra counterexample; not a Yang–Mills model.
- 2026-11-11: [Lean-checked conditional criteria](../general/2026-11-11-T02-uniform-projection-criterion/README.md): Six generic lemmas/controls checked with Lean 4.32.0 and --trust=0; no Yang–Mills application proved.

- 2026-11-11: [Checked Laplace support theorem and criterion audit](../general/2026-11-11-T02-laplace-support/README.md): standard scalar support equivalence and energy-window pullback checked; no new YM dynamical estimate.

## Update instructions

Follow [the agent prompt](../../auto-research.md). Append dated links to result records, their exact outcome/evidence level, and any superseded result. Update the next contribution from the evidence, and link cross-track consequences without duplicating results. Preserve concurrent contributions.
