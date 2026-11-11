import GapCriteria
import Mathlib.MeasureTheory.Integral.Bochner.Set

/-!
Finite positive measures: exponential Laplace bounds characterize absence
of mass below a threshold. This is not a Yang--Mills dynamical estimate.
-/
set_option autoImplicit false
noncomputable section
open Filter Set MeasureTheory
open scoped Topology
namespace MassGapResearch

variable (μ : Measure ℝ) [IsFiniteMeasure μ]

/-- A finite measure supported above a lower bound has finite heat integrals
at every nonnegative time. The threshold itself may be any real number. -/
theorem heat_integrable_of_lower_bound {b t : ℝ} (ht : 0 ≤ t)
    (hbelow : ∀ᵐ x ∂μ, b ≤ x) :
    Integrable (fun x : ℝ => Real.exp (-t * x)) μ := by
  apply (integrable_const (Real.exp (-t * b))).mono'
    (Real.continuous_exp.comp (continuous_const.mul continuous_id)).aestronglyMeasurable
  filter_upwards [hbelow] with x hx
  change ‖Real.exp (-t * x)‖ ≤ Real.exp (-t * b)
  rw [Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]
  exact Real.exp_le_exp.mpr (mul_le_mul_of_nonpos_left hx (neg_nonpos.mpr ht))

/-- Positivity gives a lower bound on the Laplace transform from the mass
of a half-line, with no hypothetical gap inserted into the hypotheses. -/
theorem halfline_mass_le_heat {a t : ℝ} (ht : 0 ≤ t)
    (hi : Integrable (fun x : ℝ => Real.exp (-t * x)) μ) :
    Real.exp (-t * a) * μ.real (Iic a) ≤
      ∫ x : ℝ, Real.exp (-t * x) ∂μ := by
  calc
    _ = ∫ _x : ℝ in Iic a, Real.exp (-t * a) ∂μ := by
      rw [setIntegral_const, smul_eq_mul, mul_comm]
    _ ≤ ∫ x : ℝ in Iic a, Real.exp (-t * x) ∂μ := by
      apply integral_mono_ae (integrable_const _) hi.integrableOn
      filter_upwards [ae_restrict_mem (μ := μ) measurableSet_Iic] with x hx
      exact Real.exp_le_exp.mpr (mul_le_mul_of_nonpos_left hx (neg_nonpos.mpr ht))
    _ ≤ ∫ x : ℝ, Real.exp (-t * x) ∂μ :=
      setIntegral_le_integral hi (ae_of_all _ fun x => (Real.exp_pos _).le)

/-- A common exponential rate removes every closed half-line strictly
below it. Integrability is explicit because a Bochner integral is zero
by convention for a nonintegrable function. -/
theorem measure_Iic_zero_of_heat_bound {a m C : ℝ} (ham : a < m)
    (h : ∀ t : ℝ, 0 ≤ t →
      Integrable (fun x : ℝ => Real.exp (-t * x)) μ ∧
      (∫ x : ℝ, Real.exp (-t * x) ∂μ) ≤ C * Real.exp (-t * m)) :
    μ (Iic a) = 0 := by
  apply (measureReal_eq_zero_iff).mp
  apply zero_of_laplace_comparison (C := C) measureReal_nonneg ham
  intro t ht
  rw [show -a * t = -t * a by ring, show -m * t = -t * m by ring]
  exact (halfline_mass_le_heat μ (a := a) ht (h t ht).1).trans (h t ht).2

/-- Countable rational exhaustion gives the exact open spectral threshold. -/
theorem measure_Iio_zero_of_heat_bound {m C : ℝ}
    (h : ∀ t : ℝ, 0 ≤ t →
      Integrable (fun x : ℝ => Real.exp (-t * x)) μ ∧
      (∫ x : ℝ, Real.exp (-t * x) ∂μ) ≤ C * Real.exp (-t * m)) :
    μ (Iio m) = 0 := by
  have hcover : Iio m = ⋃ q : {q : ℚ // (q : ℝ) < m}, Iic (q.val : ℝ) := by
    ext x
    constructor
    · intro hx
      change x < m at hx
      obtain ⟨q, hxq, hqm⟩ := exists_rat_btwn hx
      exact mem_iUnion.mpr ⟨⟨q, hqm⟩, hxq.le⟩
    · intro hx
      obtain ⟨q, hq⟩ := mem_iUnion.mp hx
      exact lt_of_le_of_lt hq q.property
  rw [hcover]
  apply measure_iUnion_null_iff.mpr
  intro q
  exact measure_Iic_zero_of_heat_bound μ q.property h

/-- Conversely, absence of mass below m yields the heat bound with total
mass as prefactor. No nonzero measure or positive m is required. -/
theorem heat_bound_of_measure_Iio_zero {m : ℝ} (hgap : μ (Iio m) = 0)
    {t : ℝ} (ht : 0 ≤ t) :
    Integrable (fun x : ℝ => Real.exp (-t * x)) μ ∧
      (∫ x : ℝ, Real.exp (-t * x) ∂μ) ≤ μ.real univ * Real.exp (-t * m) := by
  have hbelow : ∀ᵐ x ∂μ, m ≤ x := by
    apply ae_iff.mpr
    simpa only [not_le, Set.Iio_def] using hgap
  have hi := heat_integrable_of_lower_bound μ ht hbelow
  refine ⟨hi, ?_⟩
  calc
    _ ≤ ∫ _x : ℝ, Real.exp (-t * m) ∂μ := by
      apply integral_mono_ae hi (integrable_const _)
      filter_upwards [hbelow] with x hx
      exact Real.exp_le_exp.mpr (mul_le_mul_of_nonpos_left hx (neg_nonpos.mpr ht))
    _ = _ := by rw [integral_const, smul_eq_mul]

/-- The precise scalar equivalence. Obtaining either side for Yang--Mills
still requires new dynamical input. -/
theorem heat_bound_iff_measure_Iio_zero (m : ℝ) :
    (∃ C : ℝ, 0 ≤ C ∧ ∀ t : ℝ, 0 ≤ t →
      Integrable (fun x : ℝ => Real.exp (-t * x)) μ ∧
      (∫ x : ℝ, Real.exp (-t * x) ∂μ) ≤ C * Real.exp (-t * m)) ↔
    μ (Iio m) = 0 := by
  constructor
  · rintro ⟨C, _hC, h⟩
    exact measure_Iio_zero_of_heat_bound μ h
  · intro hgap
    exact ⟨μ.real univ, measureReal_nonneg,
      fun t ht => heat_bound_of_measure_Iio_zero μ hgap ht⟩

/-- The spectral threshold is open: an atom exactly at m is permitted. -/
theorem threshold_atom_allowed (m : ℝ) :
    (Measure.dirac m) (Iio m) = 0 ∧ (Measure.dirac m) {m} = 1 := by
  simp

/-- Apply the scalar result to the energy pushforward after removing the
zero-energy sector. This gives the original measure's open energy window,
not yet an operator-valued statement about the Yang--Mills PVM. -/
theorem energy_window_zero_of_heat_bound
    {α : Type*} [MeasurableSpace α] (ρ : Measure α) [IsFiniteMeasure ρ]
    (energy : α → ℝ) (hmeas : Measurable energy) {m C : ℝ}
    (h : ∀ t : ℝ, 0 ≤ t →
      Integrable (fun e : ℝ => Real.exp (-t * e))
        ((ρ.restrict {x | 0 < energy x}).map energy) ∧
      (∫ e : ℝ, Real.exp (-t * e)
        ∂((ρ.restrict {x | 0 < energy x}).map energy)) ≤ C * Real.exp (-t * m)) :
    ρ {x | 0 < energy x ∧ energy x < m} = 0 := by
  have hz := measure_Iio_zero_of_heat_bound
    ((ρ.restrict {x | 0 < energy x}).map energy) h
  rw [Measure.map_apply hmeas measurableSet_Iio,
    Measure.restrict_apply (measurableSet_Iio.preimage hmeas)] at hz
  have hs : energy ⁻¹' Iio m ∩ {x | 0 < energy x} =
      {x | 0 < energy x ∧ energy x < m} := by
    ext x
    simp only [mem_inter_iff, mem_preimage, mem_Iio, mem_setOf_eq, and_comm]
  rw [hs] at hz
  exact hz

#print axioms heat_integrable_of_lower_bound
#print axioms halfline_mass_le_heat
#print axioms measure_Iic_zero_of_heat_bound
#print axioms measure_Iio_zero_of_heat_bound
#print axioms heat_bound_of_measure_Iio_zero
#print axioms heat_bound_iff_measure_Iio_zero
#print axioms threshold_atom_allowed
#print axioms energy_window_zero_of_heat_bound
end MassGapResearch
