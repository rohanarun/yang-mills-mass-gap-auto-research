# Contributors

Useful contributions remain credited even when later corrected, superseded, or not merged. Authorship, AI assistance, upstream attribution, review, and verification are recorded separately. A credit is not an endorsement or a claim that the mass gap has been proved.

| Contributor | Contribution and evidence |
| --- | --- |
| [Rohan Arun (@rohanarun)](https://github.com/rohanarun), with OpenAI Codex assistance | [Initial source inspection and conditional spectral reduction](research/mass-gap-20261111/FirstPass.txt); [uncompiled Lean target](research/mass-gap-20261111/MassGapTarget.lean). No Yang–Mills gap proof or independent upstream replay claimed. |
| Rohan Arun, with OpenAI Codex assistance | [Polynomial-decay obstruction](auto-research/negative-results/2026-11-11-T06-polynomial-decay/README.md), with exact symbolic checks. The example concerns a scalar spectral inference and does not satisfy all Yang–Mills construction hypotheses. |
| Rohan Arun, with OpenAI Codex assistance | Repository setup, [agent prompt](auto-research.md), seven [track ledgers](auto-research/README.md), research/result templates, and contribution workflow. |
| Rohan Arun, with OpenAI Codex assistance | [Six generic conditional lemmas and controls](auto-research/general/2026-11-11-T02-uniform-projection-criterion/README.md), checked with Lean 4.32.0 and `--trust=0`; [infrared cost audit](auto-research/general/2026-11-11-T03-infrared-cost-audit/README.md); cyclicity and strong-coupling scope obstructions. No Yang–Mills gap theorem or full upstream replay. |
| Rohan Arun, with OpenAI Codex assistance | [Checked finite-measure Laplace support equivalence, energy-window pullback, and criterion audit](auto-research/general/2026-11-11-T02-laplace-support/README.md). Lean 4.32.0 trust-zero checks passed; standard infrastructure with no new Yang–Mills estimate claimed. |
| Rohan Arun, with OpenAI Codex assistance | [Variable-time localization refinement](auto-research/general/2026-11-11-T03-variable-time-average/README.md), [massless local-field control](auto-research/negative-results/2026-11-11-T06-massless-locality/README.md), and [auxiliary resolvent audit](auto-research/negative-results/2026-11-11-T03-auxiliary-resolvent-gap/README.md). Written derivations with scalar Lean and exact symbolic checks; no new Yang–Mills gap estimate or independent review. |
| Rohan Arun, with OpenAI Codex assistance | [Connected-source bridge](auto-research/general/2026-11-11-T03-connected-source-bridge/README.md) and [log/integration-order control](auto-research/negative-results/2026-11-11-T03-log-integration-order/README.md). Abstract coefficient decay checked in Lean; source-matched retained covariance identity, [terminal RG decomposition](auto-research/general/2026-11-11-T03-terminal-covariance/README.md), and exact finite-state checks; no Yang–Mills mass gap or independent review. |
| Rohan Arun, with OpenAI Codex assistance | [Single-link influence obstruction](auto-research/negative-results/2026-11-11-T03-single-link-influence/README.md): written bare SU(2) total-variation lower bound and conditional perturbation tolerance; exact finite geometry and rational arithmetic checks. No mass-gap estimate, Lean formalization, or independent review. |

## Inherited work and tools

- The authors and contributors credited in [OpenAI-YM-20261028](https://github.com/yang-mills-group/OpenAI-YM-20261028), including its [NOTICE](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/NOTICE), own the attribution for the underlying construction and proof sources. They are referenced as upstream authors, not represented as participants or endorsers of this repository.
- The existing spectral criterion is a standard application of the spectral theorem, not a new theorem claimed by this project.
- Lean, Mathlib, and SymPy are independently developed tools and libraries. Using them does not make their maintainers authors or reviewers of these research claims.

## Adding a credit

Follow [CONTRIBUTING.md](CONTRIBUTING.md). Include the contributor's preferred public name/handle, the actual work, result/PR/commit link, disclosed AI assistance, inherited credits, and precise evidence status. Credit meaningful negative results and independent reviews. Do not fabricate names, model versions, endorsements, or verification. Record who performed a review separately from the result's author.
