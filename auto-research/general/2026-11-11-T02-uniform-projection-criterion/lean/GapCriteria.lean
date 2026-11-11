import Mathlib.Analysis.Normed.Operator.ContinuousLinearMap
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
Conditional spectral tools. No Yang--Mills gap is assumed to be established.
The hypotheses containing uniformity or approximation estimates are explicit.
-/
set_option autoImplicit false
noncomputable section
open Filter Set
open scoped Topology
namespace MassGapResearch

section Normed
variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- An idempotent bounded operator strictly contracting every vector is zero. -/
theorem idempotent_eq_zero_of_bound (P : E →L[ℝ] E)
    (hid : ∀ x, P (P x) = P x) {q : ℝ} (hq : q < 1)
    (hbound : ∀ x, ‖P x‖ ≤ q * ‖x‖) : P = 0 := by
  ext x
  have h := hbound (P x)
  rw [hid] at h
  have hz : ‖P x‖ = 0 := by
    have hn := norm_nonneg (P x)
    nlinarith
  exact norm_eq_zero.mp hz

/-- Uniformity on a dense family suffices by continuity. -/
theorem idempotent_eq_zero_of_dense_bound (P : E →L[ℝ] E)
    (hid : ∀ x, P (P x) = P x) {D : Set E} (hD : Dense D)
    {q : ℝ} (hq : q < 1)
    (hbound : ∀ x ∈ D, ‖P x‖ ≤ q * ‖x‖) : P = 0 := by
  apply idempotent_eq_zero_of_bound P hid hq
  exact hD.induction hbound
    (isClosed_le P.continuous.norm (continuous_const.mul continuous_norm))

/-- It suffices to approximate vectors in the projection range with a
uniformly small combined approximation and projected-state cost. -/
theorem idempotent_eq_zero_of_approximation (P : E →L[ℝ] E)
    (hid : ∀ x, P (P x) = P x)
    (hcontract : ∀ x, ‖P x‖ ≤ ‖x‖)
    {eta q : ℝ} (hsmall : eta + q < 1)
    (happrox : ∀ x, P x = x → ∃ v : E,
      ‖x - v‖ ≤ eta * ‖x‖ ∧ ‖P v‖ ≤ q * ‖x‖) : P = 0 := by
  ext y
  let x := P y
  have hx : P x = x := hid y
  obtain ⟨v, hv, hpv⟩ := happrox x hx
  have hdiff : x - P v = P (x - v) := by rw [map_sub, hx]
  have hnorm : ‖x‖ ≤ (eta + q) * ‖x‖ := calc
    ‖x‖ ≤ ‖x - P v‖ + ‖P v‖ := norm_le_norm_sub_add x (P v)
    _ = ‖P (x - v)‖ + ‖P v‖ := by rw [hdiff]
    _ ≤ ‖x - v‖ + ‖P v‖ := add_le_add (hcontract _) le_rfl
    _ ≤ eta * ‖x‖ + q * ‖x‖ := add_le_add hv hpv
    _ = (eta + q) * ‖x‖ := by ring
  have hz : ‖x‖ = 0 := by
    have hn := norm_nonneg x
    nlinarith
  exact norm_eq_zero.mp hz
end Normed

/-- A nonnegative scalar bounded by one fixed decaying exponential is zero. -/
theorem zero_of_exponential_bound {mass C delta : ℝ}
    (hmass : 0 ≤ mass) (hdelta : 0 < delta)
    (hbound : ∀ t : ℝ, 0 ≤ t → mass ≤ C * Real.exp (-delta * t)) :
    mass = 0 := by
  have hlim : Tendsto (fun t : ℝ => C * Real.exp (-delta * t)) atTop (𝓝 0) := by
    simpa using (Real.tendsto_exp_atBot.comp
      (tendsto_id.const_mul_atTop_of_neg (neg_lt_zero.mpr hdelta))).const_mul C
  have hzero : mass ≤ 0 := ge_of_tendsto hlim
    ((eventually_ge_atTop (0 : ℝ)).mono fun t ht => hbound t ht)
  exact le_antisymm hzero hmass

/-- Scalar core of the Laplace-transform gap argument. The spectral-measure
lower bound and heat upper bound must be supplied, not assumed proved for YM. -/
theorem zero_of_laplace_comparison {mass C a m : ℝ}
    (hmass : 0 ≤ mass) (ham : a < m)
    (hbound : ∀ t : ℝ, 0 ≤ t →
      Real.exp (-a * t) * mass ≤ C * Real.exp (-m * t)) : mass = 0 := by
  apply zero_of_exponential_bound (C := C) hmass (sub_pos.mpr ham)
  intro t ht
  apply (mul_le_mul_iff_right₀ (Real.exp_pos (-a * t))).mp
  calc
    Real.exp (-a * t) * mass ≤ C * Real.exp (-m * t) := hbound t ht
    _ = Real.exp (-a * t) * (C * Real.exp (-(m-a) * t)) := by
      rw [mul_left_comm, ← Real.exp_add]
      congr 2
      ring

/-- Negative control: replacing the strict contraction by a non-strict
bound at one admits the nonzero identity projection. -/
theorem identity_counterexample :
    ∃ P : ℝ →L[ℝ] ℝ, (∀ x, P (P x) = P x) ∧
      (∀ x, ‖P x‖ ≤ 1 * ‖x‖) ∧ P ≠ 0 := by
  refine ⟨ContinuousLinearMap.id ℝ ℝ, ?_, ?_, ?_⟩
  · intro x; rfl
  · intro x; simp
  · intro h
    have he := congrArg (fun f : ℝ →L[ℝ] ℝ => f 1) h
    norm_num at he

#print axioms idempotent_eq_zero_of_bound
#print axioms idempotent_eq_zero_of_dense_bound
#print axioms idempotent_eq_zero_of_approximation
#print axioms zero_of_exponential_bound
#print axioms zero_of_laplace_comparison
#print axioms identity_counterexample
end MassGapResearch
