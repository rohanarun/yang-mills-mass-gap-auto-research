# T07: Independent verification and proof integration

## Current status

Partial: generic tools, 22 upstream branch modules, and four further source-level frame/predictor bounds checked; full probability transfer and full-construction replay open. Last indexed: 2026-11-13. No Yang–Mills mass-gap proof is claimed.

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

- 2026-11-13: [Actual-kernel curvature transfer](../general/2026-11-13-T03-blocked-curvature-transfer/README.md): `minimizing_chord`, `frame_chord`, `best_chord`, and `predict_chord` passed Lean 4.32.0 `--trust=0`, with only propext/Classical.choice/Quot.sound. These instantiate source `Patch` definitions. The common-gauge footprint, kernel moment integration, and history application remain written; finite footprint checks are not their proof.

- 2026-11-11: [Bare Wilson frame-branch probability](../general/2026-11-11-T03-bare-branch-probability/README.md) records 157,464 finite coordinate-route checks, four face counts, and scalar diagnostics. New analytic/source application remains written and unreviewed; only the inherited axial theorem is within the earlier scoped Lean replay.

- 2026-11-11: The [branch audit](../general/2026-11-11-T03-upstream-branch-audit/README.md) replayed the 22-module `YM.Branch.Pick` closure and seven-declaration axiom probe with Lean 4.32.0 `--trust=0`. A `12*d` pairwise corollary also passed. Full construction and foundation consumer not replayed.
- 2026-11-11: [External YM3D transfer assessment](../general/2026-11-11-T03-ym3d-transfer-audit/README.md): independently executed two repository-provided checkers and 29 tests at pinned revision; all passed. This is selected arithmetic/scope replay, not an independently written verifier, analytic proof, or upstream Lean replay.
- [Initial source inspection and conditional argument](../general/2026-11-11-T02-initial-reduction/README.md): inherited baseline; no Lean replay.

- 2026-11-11: [Lean-checked conditional criteria](../general/2026-11-11-T02-uniform-projection-criterion/README.md): Six generic lemmas/controls checked with Lean 4.32.0 and --trust=0; no Yang–Mills application proved.
- 2026-11-11: [Infrared cost audit](../general/2026-11-11-T03-infrared-cost-audit/README.md): Written extraction of localization/adjoint costs and a conditional approximation target; source not replayed.

- 2026-11-11: [Checked Laplace support theorem and criterion audit](../general/2026-11-11-T02-laplace-support/README.md): standard scalar support equivalence and energy-window pullback checked; no new YM dynamical estimate.

- 2026-11-11: [Variable-time averaging](../general/2026-11-11-T03-variable-time-average/README.md): written rescaling gives quadratic localization cost; scalar optimization checked, physical bridge not formalized.
- 2026-11-11: [Auxiliary resolvent gap audit](../negative-results/2026-11-11-T03-auxiliary-resolvent-gap/README.md): inspected block precision estimates do not supply retained-field correlations; exact Gaussian counterexample checked.

- 2026-11-11: [Connected-source bridge](../general/2026-11-11-T03-connected-source-bridge/README.md): cover-budget separation bound passed trust-zero checking; written identity isolates covariance of the actual normalized one-marker ratios under the retained vacuum measure.

## Update instructions

Follow [the agent prompt](../../auto-research.md). Append dated links to result records, their exact outcome/evidence level, and any superseded result. Update the next contribution from the evidence, and link cross-track consequences without duplicating results. Preserve concurrent contributions.
