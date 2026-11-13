import ChallengeSpec

/-!
UNCOMPILED specification variants, 2026-11-12. NOT a proof, NOT checked.

This file has not been elaborated with any Lean toolchain. It contains
definitions only and asserts no theorem. It accompanies the T01
specification review in this directory and must not be cited as verified.

`EnergySlabEmpty` restates the body of `HasEnergyGapAt` from
`research/mass-gap-20261111/MassGapTarget.lean` so that this file depends
only on the pinned upstream `ChallengeSpec`.
-/
set_option autoImplicit false
noncomputable section
namespace YangMills.MassGapResearch.SpecReview

/-- The reviewed target: no spectral weight at energies strictly between
`0` and `m`. Same statement as `HasEnergyGapAt`. -/
def EnergySlabEmpty {H : HilbertSpace} {Labels : FieldLabels}
    (T : WightmanTheory H Labels) (m : ℝ) : Prop :=
  0 < m ∧ T.energyMomentum.projection
    {k : Spacetime | 0 < time k ∧ time k < m} = 0

/-- Invariant-mass form: no nonzero spectral point of invariant mass
squared below `m ^ 2`. The review argues in writing that, under upstream
`W0` and the `PoincareAction` structure, this is equivalent to
`EnergySlabEmpty`. That equivalence is NOT formalized here. -/
def InvariantMassGap {H : HilbertSpace} {Labels : FieldLabels}
    (T : WightmanTheory H Labels) (m : ℝ) : Prop :=
  0 < m ∧ T.energyMomentum.projection
    {k : Spacetime | k ≠ 0 ∧ minkowskiSquare k < m ^ 2} = 0

/-- Weaker target: each hierarchy has its own positive gap. The existing
`GappedJointExistence` implies this by reordering quantifiers; the
converse is not expected to hold without a uniformity argument. -/
def GappedJointExistencePerHierarchy : Prop :=
  ∀ g : GaugeGroup, g.IsSimple → ∃ C : WilsonFamily g,
    WilsonRegularity C ∧
      ∀ p : ℕ → ℕ, StrictMono p → ∃ q : ℕ → ℕ, StrictMono q ∧
        ∃ T : Hierarchy C,
          T.Properties (p ∘ q) ∧ ∃ m : ℝ, EnergySlabEmpty T.theory m

end YangMills.MassGapResearch.SpecReview
