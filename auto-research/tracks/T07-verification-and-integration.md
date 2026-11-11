# T07: Independent verification and proof integration

## Current status

Partial: generic and scalar support results checked; upstream replay open. Last indexed: 2026-11-11. No Yang–Mills mass-gap proof is claimed.

## Research question

Independently replay relevant source proofs and integrate successful lemmas into an end-to-end argument without changing their meaning.

## Obligations

Use the exact pinned upstream revision and toolchain first. Record dependency revisions, commands, exit codes, theorem statements, admitted assumptions, and kernel/axiom audit outputs. Track partial builds separately from a complete upstream replay. Perform semantic review as well as proof checking.

## Evidence needed for the milestone

Produce a verification receipt tied to exact source hashes and reviewed theorem statements. Integration must use the same Wilson family and hierarchy, discharge every mass-gap hypothesis, and obtain an independent review before any headline proof claim.

## Failure criterion

Compilation with added axioms, sorry, weakened goals, incompatible dependencies, or a different witness does not verify the intended result. Kernel acceptance alone does not establish correspondence with the physical problem.

## Next contribution

Review the checked scalar support theorem and connect it to the exact public PVM; the upstream construction still needs independent replay.

## Active work

No active contributor recorded. When coordinating a session, add its owner/session, date, bounded question, branch or work area, and handoff condition. A stale entry is not evidence that a worker is still running.

## Contribution ledger

- [Initial source inspection and conditional argument](../general/2026-11-11-T02-initial-reduction/README.md): inherited baseline; no Lean replay.

- 2026-11-11: [Lean-checked conditional criteria](../general/2026-11-11-T02-uniform-projection-criterion/README.md): Six generic lemmas/controls checked with Lean 4.32.0 and --trust=0; no Yang–Mills application proved.
- 2026-11-11: [Infrared cost audit](../general/2026-11-11-T03-infrared-cost-audit/README.md): Written extraction of localization/adjoint costs and a conditional approximation target; source not replayed.

- 2026-11-11: [Checked Laplace support theorem and criterion audit](../general/2026-11-11-T02-laplace-support/README.md): standard scalar support equivalence and energy-window pullback checked; no new YM dynamical estimate.

## Update instructions

Follow [the agent prompt](../../auto-research.md). Append dated links to result records, their exact outcome/evidence level, and any superseded result. Update the next contribution from the evidence, and link cross-track consequences without duplicating results. Preserve concurrent contributions.
