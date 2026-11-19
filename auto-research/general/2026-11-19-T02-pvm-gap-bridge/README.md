# Checked bridge from scalar heat bounds to the public energy-momentum PVM

**No Yang-Mills mass gap or dynamical decay estimate is proved here.** This record formalizes the conditional Hilbert-space and projection-valued measure bridge (`T02`, `T07`, and `T01` review Observations 1, 3, and 4) in Lean 4.35.0 with `--trust=0`.

## Metadata

- Result ID and date: `2026-11-19-T02-pvm-gap-bridge`, 2026-11-19.
- Author: Ahraz, with AI agent assistance.
- Primary track and related tracks: T02 (primary), T01, T05, T07.
- Outcome: 18 Lean theorems and controls checked with `--trust=0 -j1`, using only `propext`, `Classical.choice`, and `Quot.sound`.
- Evidence levels: Lean 4.35.0 kernel replay (`--trust=0`) against the pinned upstream public specification, plus one failing negative-control file (`exit 1`). No independent human review.
- Repository sources used: [`GapCriteria.lean`](../2026-11-11-T02-uniform-projection-criterion/lean/GapCriteria.lean), [`LaplaceSupport.lean`](../2026-11-11-T02-laplace-support/LaplaceSupport.lean), [`MassGapTarget.lean`](../../../research/mass-gap-20261111/MassGapTarget.lean), and [`SpecVariants.lean`](../../reviews/2026-11-12-T01-gap-target-specification/SpecVariants.lean).
- Upstream pin: `yang-mills-group/OpenAI-YM-20261028` at `3456e5e75cf8d4cd558955a5c7638fba2d68f464` (`PublicTheory.lean`, `PublicWilson.lean`, `ChallengeSpec.lean`).
- Toolchain and dependency versions: `leanprover/lean4:v4.35.0` with Mathlib `56a005855ea17e0b0958f73ec801ae140b0a1679` (exact package hashes in [`verification.json`](verification.json)).

## Question and exact claim

The `T02` and `T07` track ledgers and the `T01` specification review (Observation 4) identify the open formal step between the scalar theorem `energy_window_zero_of_heat_bound` and `HasEnergyGapAt`: instantiating the scalar measure at `T.energyMomentum.diagonal ψ` along `time`, lifting vanishing diagonal slab mass to the operator `T.energyMomentum.projection`, and extending from a spanning dense family (or the vacuum complement) to the full Hilbert space.

[`PVMGapBridge.lean`](PVMGapBridge.lean) checks five groups of statements without assuming or proving any Yang-Mills dynamical decay bound:

1. **Measurability**: `time`, `spatial`, and `minkowskiSquare` are continuous on `Spacetime`, so `{0 < time}`, the open energy slab `{0 < time < m}`, and `{k ≠ 0 ∧ minkowskiSquare k < m^2}` are measurable.
2. **PVM norm identity**: For measurable `B`, self-adjointness and idempotence (`E.intersection` and `E.selfAdjoint`) give `‖E.projection B ψ‖^2 = (E.diagonal ψ).real B`, so `E.projection B ψ = 0 ↔ E.diagonal ψ B = 0`.
3. **Observation 1 and Observation 3**: `Measure.ext_of_charFun` applies directly to `Spacetime` (`EuclideanSpace ℝ (Fin 4)`) with no extra typeclass work (`diagonal_eq_of_same_translations`). Under `W0`, `W1`, and `W2`, the vacuum energy-momentum measure equals `Measure.dirac 0` (`vacuum_diagonal_eq_dirac_zero`), and the open energy-slab projection vanishes on the vacuum (`vacuum_slab_projection_eq_zero`).
4. **Observation 4 (`HasEnergyGapAt` from per-state heat bounds)**: Let `positiveEnergyMeasure T ψ` push `(T.energyMomentum.diagonal ψ).restrict {0 < time}` forward along `time`. If `0 < m` is one common rate and every `ψ ∈ D` admits its own prefactor `C_ψ` bounding the Laplace integral of `positiveEnergyMeasure T ψ` by `C_ψ * exp (-t * m)` for all `t ≥ 0`, then `HasEnergyGapAt T m` holds whenever:
   - the complex linear span of `D` is dense in `H.carrier` (`hasEnergyGapAt_of_spanning_heat_bounds`),
   - `T.W1` holds and the bound holds for smeared field words `T.fields.vector word` (`hasEnergyGapAt_of_word_heat_bounds`), or
   - `W0`, `W1`, and `W2` hold and the span of `D` is dense in `(ℂ ∙ Ω)ᗮ` (`hasEnergyGapAt_of_W0_W1_W2_vacuum_orth_heat_bounds`).
5. **Invariant-mass inclusion and rate-uniformity controls**: `energySlabEmpty_of_invariantMassGap` checks `InvariantMassGap T m → EnergySlabEmpty T m` via `S_m ⊆ R_m`. `state_dependent_rates_allow_subthreshold_atoms` proves that positive state-dependent rates `m / (n + 2)` still allow positive mass below `m`, and [`ControlSwappedRate.lean`](ControlSwappedRate.lean) fails typechecking (`exit 1`) when the common rate is replaced by a per-state rate.

## Approach and derivation

On any measurable set `B`, `P := E.projection B` satisfies `P (P ψ) = P ψ` and `P.adjoint = P`, so `inner ℂ (P ψ) (P ψ) = inner ℂ ψ (P ψ) = ((E.diagonal ψ).real B : ℂ)`. Applying `MassGapResearch.energy_window_zero_of_heat_bound` at `ρ := T.energyMomentum.diagonal ψ` and `energy := time` kills `(T.energyMomentum.diagonal ψ) S_m` and hence `P(S_m) ψ` for each `ψ ∈ D`. Linearity extends `P(S_m) = 0` to `Submodule.span ℂ D`, and continuity closes it on `H.carrier`. For `(ℂ ∙ Ω)ᗮ`, orthogonal decomposition `H = (ℂ ∙ Ω) ⊔ (ℂ ∙ Ω)ᗮ` combines `P(S_m) Ω = 0` with density in `(ℂ ∙ Ω)ᗮ`.

## Reproduction and evidence

Stage upstream `PublicTheory.lean`, `PublicWilson.lean`, and `ChallengeSpec.lean` from `3456e5e75cf8d4cd558955a5c7638fba2d68f464` alongside `GapCriteria.lean`, `LaplaceSupport.lean`, `MassGapTarget.lean`, `SpecVariants.lean`, `PVMGapBridge.lean`, and `ControlSwappedRate.lean` in a Lean `v4.35.0` workspace with Mathlib `v4.35.0`, then run:

```sh
lake exe cache get
lake build WilsonPublic GapCriteria MassGapTarget SpecVariants
lake env lean --trust=0 -j1 PVMGapBridge.lean
lake env lean --trust=0 -j1 ControlSwappedRate.lean # expected exit code 1
```

Outputs are recorded in [`PVMGapBridge.log`](PVMGapBridge.log), [`ControlSwappedRate.log`](ControlSwappedRate.log), and [`verification.json`](verification.json). Every checked theorem reports only `propext`, `Classical.choice`, and `Quot.sound`.

## Outcome and limits

- Checked in Lean `--trust=0`: `MassGapTarget.lean`, `SpecVariants.lean`, `PVMGapBridge.lean` (`18` declarations), and rejection of `ControlSwappedRate.lean`.
- Not established here: any Yang-Mills heat-decay estimate, identification of Euclidean hierarchy correlations with the Laplace integral of `positiveEnergyMeasure T ψ`, the Lorentz-boost direction `EnergySlabEmpty → InvariantMassGap`, or replay of the full upstream construction.

## Failure lesson or revised expectation

`Measure.ext_of_charFun` requires no custom Borel or second-countability wrapper on `Spacetime` in Mathlib `v4.35.0`. The remaining formal gap in `T01` Proposition 2 is only the Lorentz-boost covering step (`EnergySlabEmpty → InvariantMassGap`).

## Track contributions and next experiment

- T02 and T07: Observation 4 is now checked in Lean `--trust=0` against `ChallengeSpec` for dense-span sets, smeared `W1` field words, and `(ℂ ∙ Ω)ᗮ`.
- T01: Observations 1 and 3 and the inclusion direction of Proposition 2 are Lean-checked. Next bounded formal step: formalize the Lorentz-boost covering direction `EnergySlabEmpty → InvariantMassGap` under `W0` and `PoincareAction`.

## Review and correction history

- 2026-11-19: initial Lean 4.35.0 `--trust=0` record.
