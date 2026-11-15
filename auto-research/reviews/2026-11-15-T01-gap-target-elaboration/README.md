# Lean elaboration of the gap target and its specification variants

**No Yang–Mills mass gap is proved here.** This record checks that the proposed target *definitions* elaborate against the pinned upstream build, and it formalizes four small structural claims from the [T01 specification review](../2026-11-12-T01-gap-target-specification/README.md). Elaboration shows that the statements are well-typed. It does not show that the target is true, that it is the right target, or that any Yang–Mills theory satisfies it.

## Metadata

- Result ID and date: `2026-11-15-T01-gap-target-elaboration`, 2026-11-15.
- Author/agent/session: Sudarsh ([@Sudarsh3301](https://github.com/Sudarsh3301)) directed the work; the commands were run and this record was written with Claude (Anthropic) assistance. Neither wrote `MassGapTarget.lean` or `SpecVariants.lean`.
- Primary track and related tracks: T01; T07.
- Outcome: both target files elaborate with no messages and no source changes; four checks pass; a failure control fails as expected.
- Evidence level(s): Lean 4.32.0 elaboration with `--trust=0`; axiom report. AI-assisted; no subject-expert review.
- Repository base commit: `ff784a0` (`main`, merge of PR #9). Inputs (sha256): `MassGapTarget.lean` `8313a08042a8dcf6a1785a5a38d03a7c448b774e0265b93e9bdb54cf573ee82c`; `SpecVariants.lean` `c8e28a434e78fb50d449839eb9ece6c7d3b51d797bef18ba4553f8dc1f3e346b`; [`ChecksTail.lean`](ChecksTail.lean) `918deafbc6d11665637242513303dccfab73298215d4d7a2f1636025d384ff0c`.
- Upstream: `yang-mills-group/OpenAI-YM-20261028` at `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; library `WilsonPublic` (`PublicTheory`, `PublicWilson`, `ChallengeSpec`).
- Toolchain and dependencies: Lean 4.32.0 (commit `8c9756b28d64dab099da31a4c09229a9e6a2ef35`, `x86_64-w64-windows-gnu`); Mathlib `81a5d257c8e410db227a6665ed08f64fea08e997`; all package revisions are in [`verification.json`](verification.json).
- Related results: [T01 specification review](../2026-11-12-T01-gap-target-specification/README.md) (reviewed here, not superseded); [baseline target](../../../research/mass-gap-20261111/MassGapTarget.lean).

## Question and exact claim

Question: do `MassGapTarget.lean` and `SpecVariants.lean` elaborate, unchanged, against the pinned upstream `ChallengeSpec`, and do four structural statements from the T01 review hold in Lean?

Established here:

1. Both files elaborate with exit code 0 and empty output. No source change was needed.
2. `HasEnergyGapAt T m ↔ EnergySlabEmpty T m` holds by `Iff.rfl`, so the review's restatement is the same proposition.
3. `GappedJointExistence → JointExistence` (upstream `ChallengeSpec.lean` L186–L188): the target keeps every clause of upstream existence.
4. `GappedJointExistence → GappedJointExistencePerHierarchy`: the common-gap target implies the per-hierarchy variant.
5. `HasEnergyGapAt T m → 0 < m' → m' ≤ m → HasEnergyGapAt T m'`: the gap property is monotone downward in `m`. The proof uses only the upstream PVM field `intersection` and the measurability of the open slab.

Falsification criterion: any elaboration error, any `sorry`, or any axiom beyond `propext`, `Classical.choice` and `Quot.sound` would fail this check.

Not established: the slab/invariant-mass equivalence (review Proposition 2); that the reverse implication of item 4 fails; that the target is satisfiable; any statement about the upstream witness `YangMills.hierarchy`.

## Approach and derivation

[`make_probe.py`](make_probe.py) builds a single probe file: `import ChallengeSpec`, then the two target bodies verbatim (each without its import line), then [`ChecksTail.lean`](ChecksTail.lean). The target files themselves are also run unchanged. Items 2–4 are quantifier bookkeeping. For item 5, put $A=\{0<\mathrm{time}<m'\}$ and $B=\{0<\mathrm{time}<m\}$. Both are open, hence measurable, and $A\cap B=A$ because $m'\le m$. The upstream field `intersection` gives $P(A)=P(A\cap B)=P(A)\circ P(B)=P(A)\circ 0=0$.

## Reproduction and evidence

Working directory: a checkout of the upstream repository at `3456e5e`.

```
lake exe cache get          # exit 0 in the author's run; its log is not kept here
python -I <repo>/auto-research/reviews/2026-11-15-T01-gap-target-elaboration/run_checks.py <upstream checkout>
```

[`run_checks.py`](run_checks.py) runs `lake env lean --trust=0` on each input and first runs `lake build WilsonPublic` and records its exit code and log ([`WilsonPublic-build.log`](WilsonPublic-build.log)); the first build in the author's run compiled 8658 jobs with no warnings, and the recorded rerun is a no-op. It then writes the logs and [`verification.json`](verification.json):

| Input | Exit code | Expected | Log |
| --- | --- | --- | --- |
| `MassGapTarget.lean` (unchanged) | 0 | 0 | [`MassGapTarget.log`](MassGapTarget.log) (empty) |
| `SpecVariants.lean` (unchanged) | 0 | 0 | [`SpecVariants.log`](SpecVariants.log) (empty) |
| Probe: both bodies + checks | 0 | 0 | [`Checks.log`](Checks.log) |
| Failure control: item 5's proof with the hypothesis changed to `m ≤ m'` | 1 | 1 | [`ControlReversed.log`](ControlReversed.log) |

Axiom report ([`Checks.log`](Checks.log)): all five definitions and all four checks depend only on `propext`, `Classical.choice` and `Quot.sound`. No `sorry` warning appears. The control fails with a type mismatch inside the proof, at the use of `hle`. It shows that the proof depends on `m' ≤ m` and that the checker rejects a broken proof; it does not show that the reversed statement is false. The probe and control files are generated, not committed; their sha256 values are in the receipt.

Resources: the `WilsonPublic` build finished in under 2 minutes after the Mathlib cache download (observed, not timed precisely); each Lean run takes under a minute. Only `WilsonPublic` was built. The full upstream construction was **not** built or replayed.

## Outcome and limits

The target is now a well-typed Lean statement over the pinned upstream API, and four of the review's structural remarks are machine-checked. This is a statement check, not a proof check: the target contains no proof. Kernel acceptance of the definitions says nothing about whether they express the intended physical problem; that remains the job of the written review and of a subject-expert read. The run used Windows (`x86_64-w64-windows-gnu`); the earlier receipts in this repository do not state their platform.

## Failure lesson or revised expectation

No failure. One limit is worth recording: definitions that elaborate can still be vacuous or unsatisfiable. Nothing here excludes either.

## Track contributions and next experiment

- T01: target and variants elaborated; review items checked as listed. Next bounded task: formalize review Proposition 2 (energy slab empty ⇔ invariant-mass gap) under upstream W0 and the `PoincareAction` fields. Success criterion: a trust-zero Lean proof with the same axiom report. Dependency: Mathlib `charFun` uniqueness at the pinned revision, as the review notes. Cost: likely several sessions.
- T07/T02: the review's Observation 4 (instantiate the checked [scalar support theorem](../../general/2026-11-11-T02-laplace-support/README.md) at `energyMomentum.diagonal`) can now be attempted against these elaborated definitions.

## Review and correction history

- 2026-11-15: first record. The status "uncompiled" in the current README, agent prompt, track ledgers and indexes is updated in this change. Historical records that say "uncompiled" are left unchanged; they were accurate when written. The header comments in `MassGapTarget.lean` ("has not been elaborated") and `SpecVariants.lean` ("UNCOMPILED") are now stale. They are deliberately not edited here, so that the input hashes above and in the 2026-11-12 review stay valid; this record supersedes those two status comments.
