import GapCriteria
import Mathlib.Analysis.Normed.Group.InfiniteSum

/-!
Absolute convergence and separation decay from a weighted cover budget.
The geometric and budget hypotheses are explicit. This does not identify
the coefficients with the physical Yang--Mills connected correlation.
-/
set_option autoImplicit false
noncomputable section
namespace MassGapResearch

theorem decay_of_cover_budget {ι : Type*} (c : ι → ℂ) (N : ι → ℝ)
    {a B d Gamma : ℝ} (ha : 0 ≤ a) (hB : 0 ≤ B)
    (hgeom : ∀ i, d ≤ N i * (4 * B + 2) + 2 * B)
    (hweighted : Summable fun i => ‖c i‖ * Real.exp (a * N i))
    (hbudget : (∑' i, ‖c i‖ * Real.exp (a * N i)) ≤ Gamma) :
    Summable c ∧
      ‖∑' i, c i‖ ≤ Gamma * Real.exp (a * (2 * B - d) / (4 * B + 2)) := by
  let q := a * (2 * B - d) / (4 * B + 2)
  have hden : 0 < 4 * B + 2 := by linarith
  have hq (i : ι) : -a * N i ≤ q := by
    dsimp [q]
    apply (le_div_iff₀ hden).2
    have h := mul_le_mul_of_nonneg_left (hgeom i) ha
    nlinarith only [h]
  have hpoint (i : ι) : ‖c i‖ ≤ Real.exp q * (‖c i‖ * Real.exp (a * N i)) := by
    calc
      ‖c i‖ = ‖c i‖ * 1 := by ring
      _ ≤ ‖c i‖ * Real.exp (q + a * N i) :=
        mul_le_mul_of_nonneg_left (Real.one_le_exp (by linarith [hq i])) (norm_nonneg _)
      _ = _ := by rw [Real.exp_add]; ring
  have hnorm : Summable fun i => ‖c i‖ :=
    (hweighted.mul_left (Real.exp q)).of_nonneg_of_le (fun i => norm_nonneg _) hpoint
  refine ⟨hnorm.of_norm, ?_⟩
  calc
    ‖∑' i, c i‖ ≤ ∑' i, ‖c i‖ := norm_tsum_le_tsum_norm hnorm
    _ ≤ ∑' i, Real.exp q * (‖c i‖ * Real.exp (a * N i)) :=
      hnorm.tsum_le_tsum hpoint (hweighted.mul_left (Real.exp q))
    _ = Real.exp q * (∑' i, ‖c i‖ * Real.exp (a * N i)) := tsum_mul_left
    _ ≤ Real.exp q * Gamma := mul_le_mul_of_nonneg_left hbudget (Real.exp_pos _).le
    _ = _ := by dsimp [q]; ring

end MassGapResearch

#print axioms MassGapResearch.decay_of_cover_budget
