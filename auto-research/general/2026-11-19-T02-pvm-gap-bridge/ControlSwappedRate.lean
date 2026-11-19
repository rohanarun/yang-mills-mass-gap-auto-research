import LaplaceSupport

set_option autoImplicit false
noncomputable section
namespace YangMills.MassGapResearch
open MeasureTheory Set

/-- Negative control: swapping `∃ C` and `∃ r > 0` inside `∀ ψ ∈ D` (allowing
state-dependent decay rates) fails to imply `μ (Iio m) = 0`. -/
theorem bad_state_dependent_gap {m : ℝ} (hm : 0 < m)
    (μ : ℕ → Measure ℝ) [∀ n, IsFiniteMeasure (μ n)]
    (h : ∀ n, ∃ r > 0, ∀ t : ℝ, 0 ≤ t →
      Integrable (fun e : ℝ => Real.exp (-t * e)) (μ n) ∧
      (∫ e : ℝ, Real.exp (-t * e) ∂(μ n)) ≤ 1 * Real.exp (-t * r)) :
    ∀ n, μ n (Iio m) = 0 := by
  intro n
  obtain ⟨r, _hr, hn⟩ := h n
  exact MassGapResearch.measure_Iio_zero_of_heat_bound (μ n) hn

end YangMills.MassGapResearch
