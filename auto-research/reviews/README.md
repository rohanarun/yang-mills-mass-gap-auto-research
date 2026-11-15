# Independent reviews

| Date | Tracks | Review | Scope and evidence |
| --- | --- | --- | --- |
| 2026-11-12 | T01; T02, T05, T07 | [Gap-target specification review](2026-11-12-T01-gap-target-specification/README.md) | AI-assisted review of the uncompiled `MassGapTarget.lean` against pinned upstream definitions by a contributor who did not write it. Written derivations and exact finite boost checks; no Lean elaboration, no subject-expert review |
| 2026-11-15 | T01; T07 | [Gap-target elaboration](2026-11-15-T01-gap-target-elaboration/README.md) | AI-assisted Lean 4.32.0 `--trust=0` elaboration of `MassGapTarget.lean` and `SpecVariants.lean` against the pinned upstream `ChallengeSpec`, plus four checked structural claims from the 2026-11-12 review and a failing control. Not by the target's author; no subject-expert review; no proof of the target |

No review by a subject expert and no review of a dynamical result is recorded yet. Review the exact result revision and assumptions rather than its summary. Use the [result template](../templates/result.md) and record the reviewer/session, reviewed commit or hashes, scope, commands when applicable, findings, and unresolved concerns. A second run by the original author should be labeled a self-check, not independent review.

Add each review here and link it from the result and affected track ledgers. Never replace the original evidence with the review.
