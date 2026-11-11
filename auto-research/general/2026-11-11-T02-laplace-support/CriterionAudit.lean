import GapCriteria

/-! Audit the logical strength of the abstract approximation criterion.
This equivalence supplies no estimate for Yang--Mills dynamics. -/
set_option autoImplicit false
noncomputable section
namespace MassGapResearch

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- Under the projection assumptions, existence of the advertised strict
approximation bounds is equivalent to the zero projection. The reverse
implication is vacuous on its zero range. -/
theorem strict_range_approximation_iff_zero (P : E →L[ℝ] E)
    (hid : ∀ x, P (P x) = P x)
    (hcontract : ∀ x, ‖P x‖ ≤ ‖x‖) :
    (∃ eta q : ℝ, 0 ≤ eta ∧ 0 ≤ q ∧ eta + q < 1 ∧
      ∀ x, P x = x → ∃ v : E,
        ‖x - v‖ ≤ eta * ‖x‖ ∧ ‖P v‖ ≤ q * ‖x‖) ↔ P = 0 := by
  constructor
  · rintro ⟨eta, q, _heta, _hq, hsmall, happrox⟩
    exact idempotent_eq_zero_of_approximation P hid hcontract hsmall happrox
  · intro hp
    refine ⟨0, 0, le_rfl, le_rfl, by norm_num, ?_⟩
    intro x hx
    have hx0 : x = 0 := by simpa only [hp, ContinuousLinearMap.zero_apply] using hx.symm
    subst x
    exact ⟨0, by simp, by simp⟩

#print axioms strict_range_approximation_iff_zero
end MassGapResearch
