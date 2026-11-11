import GapCriteria

/-!
Scalar algebra for the variable-time locality estimate.
The measure pushforward, locality, and Yang--Mills application are not
formalized here. `optimized_bound` explicitly assumes the rescaled estimate.
-/
set_option autoImplicit false
noncomputable section
namespace MassGapResearch.AveragingScale

def cost (r T : ℝ) : ℝ := (4 * r + T)^3 / T

theorem rescaling_identity (r u T : ℝ) (hT : T ≠ 0) :
    ((4 * r + T) / T)^3 * (T * u)^2 = cost r T * u^2 := by
  unfold cost
  field_simp

theorem cost_decomposition (r T : ℝ) (hT : T ≠ 0) :
    cost r T - 108 * r^2 = (T - 2 * r)^2 * (T + 16 * r) / T := by
  unfold cost
  field_simp
  ring

theorem cost_lower_bound {r T : ℝ} (hr : 0 ≤ r) (hT : 0 < T) :
    108 * r^2 ≤ cost r T := by
  have h := cost_decomposition r T (ne_of_gt hT)
  have hn : 0 ≤ (T - 2 * r)^2 * (T + 16 * r) / T :=
    div_nonneg (mul_nonneg (sq_nonneg _) (by positivity)) hT.le
  linarith

theorem cost_at_optimum {r : ℝ} (hr : 0 < r) :
    cost r (2 * r) = 108 * r^2 := by
  unfold cost
  field_simp
  ring

/-- The physical rescaled spectral estimate remains an explicit premise. -/
theorem optimized_bound {F : ℝ → ℝ} {r M u : ℝ}
    (hr : 0 < r) (hsmall : 2 * r * u ≤ 1)
    (hbound : ∀ T : ℝ, 0 < T → T * u ≤ 1 →
      F u ≤ (64 / 9 : ℝ) * cost r T * M * u^2) :
    F u ≤ 768 * r^2 * M * u^2 := by
  have h := hbound (2 * r) (by positivity) hsmall
  rw [cost_at_optimum hr] at h
  convert h using 1
  ring

/-- At radius c/u the optimized dimensionless cost does not decrease. -/
theorem inverse_energy_radius (c M u : ℝ) (hu : u ≠ 0) :
    768 * (c / u)^2 * M * u^2 = 768 * c^2 * M := by
  field_simp

end MassGapResearch.AveragingScale

#print axioms MassGapResearch.AveragingScale.rescaling_identity
#print axioms MassGapResearch.AveragingScale.cost_decomposition
#print axioms MassGapResearch.AveragingScale.cost_lower_bound
#print axioms MassGapResearch.AveragingScale.cost_at_optimum
#print axioms MassGapResearch.AveragingScale.optimized_bound
#print axioms MassGapResearch.AveragingScale.inverse_energy_radius
