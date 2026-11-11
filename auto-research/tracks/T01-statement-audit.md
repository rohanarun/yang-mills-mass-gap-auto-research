# T01: Statement and specification audit

## Current status

Partial: first written specification review recorded; target still uncompiled and not expert-reviewed. Last indexed: 2026-11-12. No Yang–Mills mass-gap proof is claimed.

## Research question

Audit whether the proposed gap predicate and its quantifiers express the intended physical problem for the same upstream hierarchy.

## Obligations

Review HasEnergyGapAt, GappedJointExistence, the joint energy-momentum PVM, vacuum uniqueness, positive energy, physical units, and the upstream JointExistence witnesses. Distinguish an energy gap from an invariant-mass formulation; any claimed equivalence needs its hypotheses and proof. Check whether a common gap across volume refinements is necessary or an intentionally stronger target.

## Evidence needed for the milestone

Produce a definition-by-definition map with immutable source references, explicit assumptions, and a reviewed target. Any change of formulation must preserve the intended conclusion and explain its relation to the previous target.

## Failure criterion

A weakened statement, a gap for an unrelated theory, or quantifiers that assume the desired conclusion invalidates the proposed target.

## Next contribution

Elaborate `MassGapTarget.lean` and the uncompiled `SpecVariants.lean` against the pinned upstream build and record the receipt. Then formalize the written slab/invariant-mass equivalence, and obtain a subject-expert read of the review. State for any future gap claim whether its rate is common across volume refinements or per hierarchy.

## Active work

No active contributor recorded. When coordinating a session, add its owner/session, date, bounded question, branch or work area, and handoff condition. A stale entry is not evidence that a worker is still running.

## Contribution ledger

- [Initial source inspection and conditional argument](../general/2026-11-11-T02-initial-reduction/README.md): inherited baseline; no Lean replay.

- 2026-11-12: [Gap-target specification review](../reviews/2026-11-12-T01-gap-target-specification/README.md): AI-assisted review by a contributor who did not write the target. Written arguments that the upstream PVM is fixed by the translations, that the energy-slab target is equivalent to an invariant-mass gap under upstream W0 and Poincaré structure, and that the zero-energy sector is the vacuum line. Findings: common gap is stronger than a per-hierarchy gap; the value of `m` is not canonical; the target is witness-agnostic and concerns the selected phase. Source inspection, written derivation, exact finite boost checks. No Lean elaboration or expert review.

## Update instructions

Follow [the agent prompt](../../auto-research.md). Append dated links to result records, their exact outcome/evidence level, and any superseded result. Update the next contribution from the evidence, and link cross-track consequences without duplicating results. Preserve concurrent contributions.
