/-!
Checks appended by `make_probe.py` after the verbatim bodies of
`MassGapTarget.lean` and `SpecVariants.lean`. Definitions only are reused;
nothing here changes those definitions. NOT a mass-gap proof.
-/
namespace YangMills.MassGapResearch.ElaborationChecks
open YangMills YangMills.MassGapResearch YangMills.MassGapResearch.SpecReview

/-- The review states that `EnergySlabEmpty` restates `HasEnergyGapAt`. -/
theorem energySlabEmpty_iff {H : HilbertSpace} {Labels : FieldLabels}
    (T : WightmanTheory H Labels) (m : ℝ) :
    HasEnergyGapAt T m ↔ EnergySlabEmpty T m := Iff.rfl

/-- The review states that the target implies upstream `JointExistence`
by forgetting `m`. -/
theorem jointExistence_of_gapped (h : GappedJointExistence) :
    JointExistence := by
  intro g hg
  obtain ⟨C, hC, m, _, h⟩ := h g hg
  refine ⟨C, hC, fun p hp => ?_⟩
  obtain ⟨q, hq, T, hT, _⟩ := h p hp
  exact ⟨q, hq, T, hT⟩

/-- The review states that the common-gap target implies the
per-hierarchy variant by reordering quantifiers. -/
theorem perHierarchy_of_gapped (h : GappedJointExistence) :
    GappedJointExistencePerHierarchy := by
  intro g hg
  obtain ⟨C, hC, m, _, h⟩ := h g hg
  refine ⟨C, hC, fun p hp => ?_⟩
  obtain ⟨q, hq, T, hT, hgap⟩ := h p hp
  exact ⟨q, hq, T, hT, m, hgap⟩

/-- The review states that the gap property is monotone downward in `m`.
This uses only the upstream `intersection` field of the joint PVM. -/
theorem hasEnergyGapAt_mono {H : HilbertSpace} {Labels : FieldLabels}
    {T : WightmanTheory H Labels} {m m' : ℝ}
    (h : HasEnergyGapAt T m) (hm' : 0 < m') (hle : m' ≤ m) :
    HasEnergyGapAt T m' := by
  refine ⟨hm', ?_⟩
  have hc : Continuous time := by unfold time; fun_prop
  have meas : ∀ a : ℝ,
      MeasurableSet {p : Spacetime | 0 < time p ∧ time p < a} := fun a =>
    ((isOpen_lt continuous_const hc).inter
      (isOpen_lt hc continuous_const)).measurableSet
  have hsub : {p : Spacetime | 0 < time p ∧ time p < m'} ∩
      {p : Spacetime | 0 < time p ∧ time p < m} =
      {p : Spacetime | 0 < time p ∧ time p < m'} :=
    Set.inter_eq_left.mpr fun p hp => ⟨hp.1, lt_of_lt_of_le hp.2 hle⟩
  rw [← hsub, ← T.energyMomentum.intersection (meas m') (meas m), h.2]
  exact ContinuousLinearMap.comp_zero _

end YangMills.MassGapResearch.ElaborationChecks

#print axioms YangMills.MassGapResearch.HasEnergyGapAt
#print axioms YangMills.MassGapResearch.GappedJointExistence
#print axioms YangMills.MassGapResearch.SpecReview.EnergySlabEmpty
#print axioms YangMills.MassGapResearch.SpecReview.InvariantMassGap
#print axioms YangMills.MassGapResearch.SpecReview.GappedJointExistencePerHierarchy
#print axioms YangMills.MassGapResearch.ElaborationChecks.energySlabEmpty_iff
#print axioms YangMills.MassGapResearch.ElaborationChecks.jointExistence_of_gapped
#print axioms YangMills.MassGapResearch.ElaborationChecks.perHierarchy_of_gapped
#print axioms YangMills.MassGapResearch.ElaborationChecks.hasEnergyGapAt_mono
