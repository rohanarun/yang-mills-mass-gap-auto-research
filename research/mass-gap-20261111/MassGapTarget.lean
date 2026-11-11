import ChallengeSpec

/-!
Research target, 2026-11-11. NOT a proof of mass gap.
This file has not been elaborated with the repository's pinned Lean 4.32.0.
The gap is required for the SAME hierarchy that satisfies the Wilson,
reconstruction, OPE, and non-freeness conditions.
-/
set_option autoImplicit false
noncomputable section
namespace YangMills.MassGapResearch

/-- Exclude every strictly positive energy below m in the joint PVM.
Together with the existing positive-energy and unique-vacuum properties,
this is an energy-gap target. No explicit Hamiltonian is needed here. -/
def HasEnergyGapAt {H : HilbertSpace} {Labels : FieldLabels}
    (T : WightmanTheory H Labels) (m : ℝ) : Prop :=
  0 < m ∧ T.energyMomentum.projection
    {p : Spacetime | 0 < time p ∧ time p < m} = 0

/-- Research target: a common positive physical gap for each chosen gauge
family, on every requested volume refinement. This is stronger than merely
requesting some gap separately for each resulting hierarchy. -/
def GappedJointExistence : Prop :=
  ∀ g : GaugeGroup, g.IsSimple → ∃ C : WilsonFamily g,
    WilsonRegularity C ∧ ∃ m : ℝ, 0 < m ∧
      ∀ p : ℕ → ℕ, StrictMono p → ∃ q : ℕ → ℕ, StrictMono q ∧
        ∃ T : Hierarchy C,
          T.Properties (p ∘ q) ∧ HasEnergyGapAt T.theory m

end YangMills.MassGapResearch
