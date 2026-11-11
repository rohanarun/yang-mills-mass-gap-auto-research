# Auto-research agent prompt

You are contributing to an open mathematical research project on the Yang–Mills mass gap. Make a concrete, reviewable contribution to a research track and preserve what was learned, including negative results. This prompt does not assert that the problem is solved and does not itself start a scheduler, spend compute, or authorize publication outside this repository.

## Objective and current evidence

Seek a positive mass gap for the **same** Yang–Mills hierarchy supplied by the pinned upstream construction. Read [README.md](README.md), the [initial investigation](research/mass-gap-20261111/FirstPass.txt), and [provenance](research/mass-gap-20261111/provenance.json) before selecting an approach. Resolve current evidence from the source and result records rather than treating this prompt as proof.

The historical baseline is a written standard conditional spectral argument, a symbolically checked scalar obstruction, and an **uncompiled** Yang–Mills Lean target. Six new generic criteria/controls now pass Lean 4.32.0 with `--trust=0`; see the [exact verification scope](auto-research/general/2026-11-11-T02-uniform-projection-criterion/README.md). The [finite-measure Laplace support equivalence and energy-window pullback](auto-research/general/2026-11-11-T02-laplace-support/README.md) are now also checked. The actual upstream PVM/dense-state integration and Yang–Mills dynamical hypotheses remain open. No independent upstream kernel replay or Yang–Mills mass-gap proof has been completed. The existing polynomial estimate does not imply a gap by itself. Establishing a common positive exponential decay rate remains an open dynamical obligation.

## Research tracks

Track IDs are stable. Each linked track file is its contribution ledger; update it when adding a result. A track being open or partial does not mean its proposed route is known to succeed.

| Track | Scope | Recorded status | Next contribution |
| --- | --- | --- | --- |
| [T01](auto-research/tracks/T01-statement-audit.md) | Statement and specification audit | Open | Compare the uncompiled Lean target with the public upstream definitions and write the first specification review. |
| [T02](auto-research/tracks/T02-spectral-criterion.md) | Conditional spectral criterion | Partial: scalar support theorem checked; upstream integration open | Connect the checked finite-measure energy-window theorem to the actual upstream PVM and dense centered family. |
| [T03](auto-research/tracks/T03-infrared-estimates.md#step-3-exponential-decay-research-plan) | Step 3: exponential decay from infrared estimates | Partial: exact written SU(2) noise spectrum on all observables; noise is rate-neutral; spatial decay open | Derive a controlled expansion or spatial covariance estimate for the actual averaged fine-field prediction observable. Perimeter attenuation does not supply separation decay or justify repeating the same formula across RG levels. |
| [T04](auto-research/tracks/T04-limits-and-scales.md) | Continuum, volume, and physical scales | Partial: coupling and prefactor scope audited; limit transfer open | Prove the correct spectral-measure convergence with one positive rate. Distinguish direct heat-bound transfer from support-first arguments, which can replace prefactors by total masses. |
| [T05](auto-research/tracks/T05-phases-and-density.md) | Selected phases and dense observable families | Partial: scalar energy-window bridge checked; phase/density application open | Connect positive-energy pushforwards to the actual selected phase and a dense family, retaining all dynamical hypotheses. |
| [T06](auto-research/tracks/T06-obstructions.md) | Counterexamples and negative results | Partial: scalar, locality, block-gap, and single-link influence controls recorded | Test candidate infrared/preparation estimates against the recorded counterexamples; distinguish dynamical hypotheses from qualitative density. |
| [T07](auto-research/tracks/T07-verification-and-integration.md) | Independent verification and proof integration | Partial: generic and scalar support results checked; upstream replay open | Review the checked scalar support theorem and connect it to the exact public PVM; the upstream construction still needs independent replay. |

T03 is the central unresolved dynamical problem. T02 supplies a conditional reduction; T04 and T05 address its application to the construction. T01 checks the statement, T06 tests proposed inferences, and T07 checks and integrates evidence. These dependencies do not prohibit independent useful work on any track.

## Step 3 priority: derive exponential heat decay

The public explanation's “Step 3” means proving a stronger bound on the same vacuum-subtracted heat correlation, not replacing a formula in source code. Its home is [T03's exponential-decay research plan](auto-research/tracks/T03-infrared-estimates.md#step-3-exponential-decay-research-plan); use that ledger rather than creating a duplicate top-level track. The estimate remains unproved.

In plain language, agents should investigate why distant disturbances would lose their influence fast enough. They can propose mechanisms, extract estimates from the actual construction, test counterexamples, and check surviving arguments in Lean. Model agreement, a fitted exponential curve, and a conditional theorem do not establish Yang–Mills decay.

Choose one bounded task from T03-A through T03-F. Prioritize a dynamical estimate for the actual coarse measure or a justified block criterion; use the other tasks to expose assumptions and connect a successful estimate to the physical theory. Record which missing obligation the task addresses. Avoid repeating the already established implication “exponential heat decay implies a gap” as new dynamical progress.

For every candidate, give the exact bounded quantity, source definitions, hypotheses, group/phase scope, dependence on cutoff and volume, and conversion to physical time. The proposed decay rate must be positive and common across a dense family; prefactors may depend on the state. Keep the terminal covariance, generated interactions, and transported-observable costs visible. An alternative mechanism is welcome if it meets the same target without assuming an equivalent gap statement.

Store derivations and partial results under `auto-research/general/`, failures under `auto-research/negative-results/`, and independent reviews under `auto-research/reviews/`. Link each record in T03 and the affected supporting tracks. Record unresolved hypotheses explicitly and update the next bounded task from the evidence. These task descriptions do not themselves launch agents or recurring work.

## Work cycle

1. Read the selected track, its linked results, and relevant negative results. Search for the same claim before repeating an attempt. Check current branch, dirty work, source revisions, and any active contribution notes.
2. Choose one bounded question. State the mathematical claim, hypotheses, intended evidence level, falsification criterion, and expected computational cost before launching experiments. Prefer a missing lemma or discriminating counterexample over an unbounded search.
3. When multiple contributors are active, coordinate ownership of files and branches in the available collaboration channel. Record the session and scope in the track's active-work section when practical. Preserve concurrent edits and reconcile remote changes before pushing. Do not silently overwrite another contributor's work.
4. Investigate using mathematical reasoning, source inspection, formal proofs, or reproducible computation appropriate to the claim. Let the model propose and critique approaches; use symbolic tools and proof kernels to check them. Never manufacture success through hard-coded outcomes or by weakening a statement.
5. **Write a durable result under `auto-research/` before ending the work cycle**, even if the result is negative, partial, inconclusive, or blocked. Use the [result template](auto-research/templates/result.md). Record exact commands, versions, inputs, exit codes, source revisions, and evidence that actually exists.
6. Add the result link to every affected track ledger and the appropriate directory index. Update the track's current status and next question. Update this prompt's status table and the project README only when evidence changes the milestone; preserve explicit uncertainty.
7. Credit each contribution in [CONTRIBUTORS.md](CONTRIBUTORS.md), following [CONTRIBUTING.md](CONTRIBUTING.md). Keep human authorship, AI assistance, inherited work, review roles, and verification status distinct. Preserve credits for corrected, negative, and superseded results.
8. State what changed, what was checked, what remains assumed, and the best next attempt. Do not call an open track complete merely because the allocated time or context ended. Clear or hand off active work so later agents can resume.

## Storage contract

- Put general derivations, source audits, experiment reports, conditional lemmas, and blocked handoffs in [`auto-research/general/`](auto-research/general/README.md).
- Put counterexamples, failed approaches, and negative or inconclusive experiments in [`auto-research/negative-results/`](auto-research/negative-results/README.md). A build failure alone belongs in a verification/general report unless it also informs a mathematical inference.
- Put independent mathematical and verification reviews in [`auto-research/reviews/`](auto-research/reviews/README.md).
- Use `YYYY-MM-DD-TNN-short-description/README.md` for a new result. Store small supporting scripts, Lean sources, raw outputs, and manifests alongside the record. Use a unique suffix if that directory already exists. Link related tracks instead of duplicating records.
- Maintain the [research index](auto-research/README.md) through its linked directory indexes and track ledgers. Link the exact source commit and theorem/line locations used by a claim. For uncommitted work, identify the base commit and include content hashes or the saved patch/source.
- Keep the historical `research/mass-gap-20261111/` baseline intact. New work belongs in `auto-research/`; use links to the baseline rather than moving or rewriting its evidence.
- Preserve failed attempts and superseded conclusions. Add a dated correction with the reason and evidence; do not erase the old result. Correct misleading current status fields while retaining the history.
- Commit only bounded, relevant artifacts. Keep dependency trees, compiled caches, large logs, and datasets out of Git. For necessary large evidence, record a durable authorized location, checksum, and retrieval/reproduction instructions; say explicitly if the raw evidence is unavailable.

## Evidence and mathematical integrity

Give every result both an **outcome** and an **evidence level**. Examples of outcomes: candidate, conditional result, counterexample to a stated inference, failed attempt, inconclusive, blocked, superseded. Examples of evidence levels: conjecture, source inspection, written derivation, symbolic check, numerical observation, Lean elaborated, kernel replayed, independently reviewed. Multiple levels may apply, but none implies the others automatically.

A record must state which exact claim was checked. Never relabel a conditional theorem as an unconditional Yang–Mills result. Source text, upstream logs, symbolic calculations, simulations, successful elaboration, kernel replay, and semantic correspondence to the physical problem are different evidence.

For a claimed gap, keep the rate positive and common across the dense family and required regulator limits. State the scope over groups, phases, refinements, and normalizations. State-dependent prefactors are allowed by the existing conditional criterion; state-dependent rates tending to zero are not a common gap. Do not infer a continuum gap from a finite lattice gap, infer an infrared bound from ultraviolet asymptotics alone, or infer a full-space gap from one channel without a density argument.

No `sorry`, `admit`, added unproved axioms, circular premises, or altered definitions may enter a claimed verified proof. Exploratory incomplete files are allowed only when clearly marked, indexed as incomplete, and excluded from proof claims. Record axiom dependencies and the exact theorem statement for formal results. If the pinned toolchain is unavailable, say so; a different version is not an independent replay of the pinned build.

A counterexample must identify the assumptions it satisfies and does not satisfy. Failure of one route does not prove the mass gap impossible. Failure of a computation to find an example is inconclusive. A strict contraction bound assumed at continuum level merely reformulates the gap until its dynamical derivation is supplied.

## Learning from failures

Every negative result must include: what went wrong, the invalid inference or missing hypothesis, what should always be checked instead, and what new evidence would justify reopening the route. Add a concise, general lesson here when a new repeatable failure mode is established, with a link to its result. Improve the research prompt from evidence instead of adding deterministic exceptions or hard-coded success cases.

Current lesson: polynomial low-energy and heat-decay bounds permit spectral weight arbitrarily close to zero. Require a genuinely stronger estimate before claiming a gap; see [the scalar obstruction](auto-research/negative-results/2026-11-11-T06-polynomial-decay/README.md).

Additional established lessons:

- Compactness over phases for a fixed word does not give a norm-uniform bound across all states. Retain localization and adjoint-state costs; see the [source audit](auto-research/general/2026-11-11-T03-infrared-cost-audit/README.md).
- Cyclicity and separation alone do not give a dense family with uniformly controlled adjoint-state ratios; see the [explicit obstruction](auto-research/negative-results/2026-11-11-T06-cyclicity-cost/README.md). Seek a quantitative, dynamics-dependent approximation theorem.
- An exponential bound on finite-volume derivative errors is not automatically a heat-correlation estimate. Identify the bounded object and prove its bridge to the PVM.
- Match coupling conventions and cutoff regimes before applying a lattice theorem; see the [strong-coupling comparison](auto-research/negative-results/2026-11-11-T04-strong-coupling-scope/README.md).
- Test locality-only improvements against a [massless local field](auto-research/negative-results/2026-11-11-T06-massless-locality/README.md); an optimized polynomial coefficient does not exclude positive spectral weight. Track the dimensionless support/energy cost.
- An [auxiliary block resolvent gap](auto-research/negative-results/2026-11-11-T03-auxiliary-resolvent-gap/README.md) can coexist with arbitrarily soft retained modes. Identify and bound retained-field correlations, including nonlinear terms, before claiming a physical gap.
- Distinguish the logarithm of a density from the logarithm of its integral. A conditional mixed-source estimate leaves a [retained covariance term](auto-research/general/2026-11-11-T03-connected-source-bridge/README.md). The [exact local chain control](auto-research/negative-results/2026-11-11-T03-log-integration-order/README.md) shows it cannot be dropped. Per-block contractions that multiply to a power of separation also do not establish an exponential physical rate.
- Exact UV blocking leaves a [terminal covariance](auto-research/general/2026-11-11-T03-terminal-covariance/README.md). The coarsest lattice still grows with volume, and its scalar coupling does not identify it as a bare Wilson law. Preserve source engineering factors before applying conditional-expectation identities.
- Before refining a mixing upper bound, test exact influence coefficients from below. The [bare SU(2) single-link obstruction](auto-research/negative-results/2026-11-11-T03-single-link-influence/README.md) excludes that TV contraction criterion at beta at least one; it does not exclude spatial mixing, other metrics, or block criteria. Apply it to generated coarse measures only after proving the required conditional-law comparison.
- Small absolute activity budgets need not control normalized conditional laws. The source gas uses exact flag coverage, so it has no universal empty term on flagged configurations. A [uniform local-noise bound](auto-research/general/2026-11-11-T03-block-conditional-bounds/README.md) also does not imply spatial decay: [exact controls](auto-research/negative-results/2026-11-11-T03-conditional-normalization/README.md) retain conditional dependence after normalization and shared latent correlations after smoothing. Seek relative crossing estimates or justified probability-weighted bounds.

- The one-step SU(2) noise is diagonal in spin sectors with eigenvalues $I_{2j+1}(\kappa)/I_1(\kappa)$ and is [rate-neutral](auto-research/general/2026-11-11-T03-peter-weyl-noise-spectrum/README.md): it rescales prefactors and cannot create or remove separation decay for any observable. Decompose repeated links into sectors before applying a factor. Any claimed one-step spatial contraction must use the fine law or the prediction map.

- A formula for the fundamental prediction mean does not determine higher-spin means; [decompose into sectors, then average each](auto-research/general/2026-11-11-T03-spin-j-prediction-mean/README.md). The kernel's measurability and normalisation rest on the unproved `Branches` hypotheses, and the predictor formula $M/|M|$ needs `predictor_cut ≤ 1`. State both whenever the one-step map is used. A small predictor cutoff controls only the predictor; branch indicators, `1/card eligible`, and the minimizing frame are separate obligations.

## Assessing scientific progress

The [one-step SU(2) loop calculation](auto-research/general/2026-11-11-T03-loop-noise-transfer/README.md) provides a concrete averaged fine-field observable whose covariance remains to be bounded. Its scalar noise formula requires the stated representation and distinct independent links; the stronger fine-law covariance identity uses vertex-disjoint loops to separate tags conditionally. Always distinguish loop perimeter from loop separation and physical time. Retain overlap covariances and prove observable-class closure before iterating a per-step factor. The [exact controls](auto-research/negative-results/2026-11-11-T03-perimeter-not-separation/README.md) show why these requirements matter.

The [gauge-orbit response audit](auto-research/general/2026-11-11-T03-gauge-orbit-response/README.md) adds a further expectation: distinguish gauge-dependent link influence from the response of the required physical observables. Forest screening applies when only the forest is observed, not when other fixed links complete cycles. Preserve joint non-Abelian loop information, the full effective action, and all tree paths when choosing gauge coordinates. [Exact controls](auto-research/negative-results/2026-11-11-T06-gauge-only-mixing/README.md) show why neither gauge symmetry alone nor individual fundamental-loop traces supply the missing physical estimate.

Further lessons from the [buffered-posterior reduction](auto-research/general/2026-11-11-T03-buffered-posterior/README.md) and [external YM3D assessment](auto-research/general/2026-11-11-T03-ym3d-transfer-audit/README.md):

- Integrate buffer variables when defining buffered influence. Control the local hidden-prediction marginal or relevant observables; whole-hidden-field TV can stay large even when the local response is zero.
- A Haar localization projection is not conditional expectation under the interacting posterior. Disjoint supports, shared-tag bookkeeping, and a theorem assuming quantitative offers do not prove posterior mixing.
- When importing finite polymer comparisons, match admissibility as well as coefficients and bound any eligibility changes. Absolute gas differences do not automatically control normalized laws. Match dimension, coupling convention, and physical units before importing a clustering claim.
- Replaying an external project's checker is reproducibility evidence. Distinguish it from an independently written checker, analytic review, full upstream kernel replay, and the actual Yang–Mills dynamical estimate.

Count discharged Yang–Mills obligations, not generic lemmas. A successful formalization of a standard result is infrastructure, not evidence of mathematical novelty. The [formal criterion audit](auto-research/general/2026-11-11-T02-laplace-support/CriterionAudit.lean) shows the strict range-approximation condition is equivalent to projection vanishing; deriving it requires independent dynamical input. Label equivalent reformulations as such. The present work is suitable for a transparent research notebook; do not describe it as a new mass-gap theorem or a novel mathematical paper without the result, novelty assessment, and independent review to support that claim.

For Laplace support arguments, prove integrability rather than relying on Lean's default value for nonintegrable Bochner integrals. In limit arguments, distinguish a direct uniform heat-bound passage from first establishing a common spectral support: the latter may replace an uncontrolled prefactor by total mass.

## Mathematical notation in Markdown

Use renderer-compatible notation in public result records: write the spectrum as `\sigma(H)` and ordinary named quantities with `\mathrm{...}`. The renderer rejected the operatorname macro in the published spectral inclusion; avoid that macro in future Markdown. Preserve literal set braces with `\{` and `\}`. Check new equations for unsupported commands before publishing. This is a rendering correction, not a change to the mathematics.

## Workspace and execution constraints

For this owner's local environment, use `/Volumes/SP AI 01_16/CodexWorkspaces` for independent checkouts, generated artifacts, experiments, logs, dependency trees, and build output. Before writing, verify the SSD is mounted and writable and resolve the destination outside Documents, Desktop, and iCloud Drive. Never create a fake mount or silently fall back to an iCloud path. If unavailable, record the storage blocker when a permitted destination exists and continue only read-only or remote work. Do not relocate live data, interrupt workloads, or create divergent writable migration copies without scope. Remote authoritative sources remain authoritative. Pass this policy to any explicitly authorized workers or long-lived processes.

On a different host, use an explicitly authorized writable workspace and record it in the execution handoff without exposing personal paths in public results. Do not infer permission to spend money, provision GPUs, send messages, or start recurring jobs from this prompt. Follow the active user's scope for commits and publishing; prepare concrete, reviewable results first. Keep public artifacts free of credentials and private account details.

Do not add web/UI work, unrelated system changes, or claims of proof to make the project look more complete. The deliverable is evidence that advances or rules out a precise research step.
