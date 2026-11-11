# Correction: upstream already supplies the branch conditions

## Metadata and correction

- Date / author: 2026-11-11; Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03, T06, T07. Base: `3e4346626680f8ef782d0e2daca99056428d9c7d`.
- Upstream pin: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`.
- Outcome: correction of an incomplete source audit, a producer/consumer dependency map, and a successful targeted branch-proof replay. No new mass-gap estimate.

**Our earlier claim that the upstream source leaves the three `Patch.Branches` conditions unproved was incorrect.** The comment in `RG/Patch.lean` identifies obligations at that interface; later modules supply them. The earlier spin-j audit inspected consumers without following the producers. The same incomplete reading affected the framing of our subsequent SU(2) uniqueness work.

This correction changes the attribution and assessment of progress. Frame uniqueness and patch-size-independent synchronization are already upstream results. Our explicit quaternion constants and optimization certificates must be assessed as specialized calculations against that existing work, not as filling an absent upstream uniqueness proof. They have not been shown novel or independently reviewed.

## Existing source results

All links below use the pinned revision.

| Obligation or ingredient | Existing upstream declaration | What its statement supplies |
| --- | --- | --- |
| Minima cluster | [`YM.Branch.Pairs.compare_energy`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Branch/Synchronize.lean#L127) | Average squared pairwise distance at most `4*d^2`, without a data-size factor |
| Feedback stays near identity | [`YM.Branch.Pairs.closeness`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Branch/Synchronize.lean#L172) | Bound `3*d` after centering the nearest point to the centroid at identity |
| Uniqueness modulo common gauge | [`YM.Branch.align`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Branch/Synchronize.lean#L232) | A positive cutoff independent of the number of points and route labels, for general source `Gauge` inputs |
| Frame uniqueness | [`YM.RG.frame_unique`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Branch/Uniform.lean#L18) | A positive group-dependent cutoff sufficient for all patches and all configurations satisfying `usesMin` |
| Predictor uniqueness | [`YM.RG.predictor_unique`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Branch/Uniform.lean#L58) | A positive group-dependent predictor cutoff sufficient for all patches |
| An eligible axial root | [`YM.Axial.eligible`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Branch/Pick.lean#L119) | For every route order, some root is eligible whenever `axial_factor >= 16` |
| All three branch conditions | [`YM.Axial.viable`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Branch/Pick.lean#L137) | For every positive penalty, a single kernel satisfies `Branches` for every patch |
| A chosen kernel with the proof attached | [`YM.Next.Foundations.kernel` and `branches`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Next/FOUNDATIONS/Primary.lean#L66) | A classical choice of the viable kernel, with a theorem proving its branch conditions |

The axial proof is an induction over coordinate slabs, not a curvature-smallness argument. `YM.Axial.existence` gives a bound `4 * number_of_axes * (2*radius+1) * faces`. Four axes give the sufficient factor 16, matching the factor already built into the proof of `viable`. This is upstream work, not a new bound obtained here.

The dependency chain is `Center -> Synchronize -> Uniform -> Slide -> Pick`; local imports beneath `Pick` comprise 22 YM modules. The foundation consumer also has many unrelated imports and is outside this narrow replay target.

## An existing patch-size-independent frame bound

There is also a direct written corollary of the source lemmas that changes the interpretation of our earlier comparison chart. In the source's unnormalized Frobenius norm, suppose every routed transport is within $d$ of identity and $h$ is a global minimizer. Rotate $h$ by a common group element so that identity is a nearest group point to its centroid. The existing `closeness` bound gives

$$
\|\mathrm{feedback}(h,i)-1\|\leq3d.
$$

The existing `self_consistent` lemma says $h_i$ is a nearest group point to that feedback. Comparing to identity and applying the triangle inequality gives $\|h_i-1\|\leq6d$. Therefore every pair satisfies $\|h_i-h_j\|\leq12d$. Reanchoring at the centre and dividing by the representation normalization yields

$$
\max_i \mathrm{chord}(h_iA_i^{-1})\leq\min\{2,12\varepsilon\},
$$

where $A$ is the centre-based axial frame and $\varepsilon=\mathrm{frame\_cut}$. Common left multiplication and right multiplication preserve the Frobenius distances. The unnormalized pairwise `12*d` bound is now checked in [BranchCorollary.lean](BranchCorollary.lean), using the replayed upstream lemmas, with Lean 4.32.0 and `--trust=0`; see its [receipt](corollary-verification.json) and [axiom output](corollary-check.log). The axial-frame dictionary and normalized `12*epsilon` application above remain written deductions. This is a corollary of upstream work, not a new dynamical result.

Thus patch-size independence was already available upstream. Our PR #4's explicit fundamental-SU(2) bound $4\varepsilon/\sqrt{1-2\varepsilon^2}$ can be compared to this elementary `12*epsilon` corollary, but the smaller coefficient has not been shown to improve the best available literature or upstream consequence. The earlier chart compared our own preliminary sketch with our later calculation; it must not be presented as showing that upstream lacked a uniform bound.

## What this does and does not settle

- The three branch conditions are supplied by upstream theorems for suitable kernels. They are not, by themselves, unresolved global premises of the construction.
- The interface still matters: arbitrary positive `KernelChoices` need not satisfy `Branches`; consumers must use the actual supplied proof for their kernel.
- `Axial.viable` states penalty equality and all-patch branch validity. Although its proof constructs a witness with axial factor 16, that numeric equality is not exposed in the existential statement. Do not infer the fields of a later `Classical.choose` by treating the witness written inside an opaque proof as a computational definition.
- In particular, these existence statements do not supply our desired explicit frame-cutoff bound `<= 1/16` or strict predictor cutoff `< 1` for a later chosen kernel. Those quantitative applications still need an appropriate statement for the same kernel.
- None of these results controls bad-branch probabilities or spatial correlations under the interacting fine-field law. They do not establish exponential heat decay or a mass gap.

## Replay scope

**Successful scoped replay:** all 22 YM modules in the import closure of `YM.Branch.Pick`, followed by an axiom probe, passed the pinned Lean 4.32.0 with `--trust=0 -j1`, without source changes. Compilation took 86.356 seconds after preparing the matching Mathlib cache. The seven audited declarations report only `propext`, `Classical.choice`, and `Quot.sound`. See the [verification receipt](verification.json), [per-module report and source hashes](replay-report.json), [combined logs](replay.log), and [axiom output](axioms.log). The foundation consumer and the full upstream construction were not compiled. This is independent execution of upstream proofs, not independent mathematical review of the full construction.

The driver [replay_branch.py](replay_branch.py) follows the source imports of `YM.Branch.Pick`, copies only those files into a separate build workspace, and invokes the pinned Lean 4.32.0 with `--trust=0 -j1`. It stops at the first unsuccessful compilation without patching source. It records every attempted module and exit status; the final probe, if reached, prints axiom dependencies for the listed branch declarations.

Usage:

```sh
python3 replay_branch.py UPSTREAM LEAN_BINARY PACKAGE_DIRECTORY OUTPUT_DIRECTORY
```

Use the pinned Mathlib revision `81a5d257c8e410db227a6665ed08f64fea08e997` and its dependency manifest. All generated files belong in the authorized external workspace. Exact replay outcomes and source hashes are recorded in the accompanying receipt; a successful dependency prefix is not verification of the unreached branch theorems or of the full construction.

## Corrected research priority

Audit producer declarations and their consumers before treating a structure field or local comment as an unresolved theorem. Search the entire pinned repository for the field, producer names, and instances; then distinguish a source proof, a successful replay, and a physical application. Preserve the historical mistake and append a correction rather than silently claiming it was never made.

The useful next work is a scoped replay/semantic audit of these existing results, quantitative bounds for the actual chosen kernel, and the unresolved probability/spatial covariance estimates. Re-proving existence or uniqueness already supplied upstream must not be counted as new progress toward the mass gap without a demonstrated additional consequence.
