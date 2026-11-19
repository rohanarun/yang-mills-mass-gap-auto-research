import MassGapTarget
import SpecVariants
import LaplaceSupport

/-!
Conditional bridge from per-state scalar heat bounds to the public Yang--Mills
energy-momentum PVM (`T02` / `T07` / `T01` review Observation 4).

**No Yang--Mills mass gap or dynamical decay estimate is proved here.**
Every gap conclusion below is explicitly conditional on per-state exponential
Laplace bounds at one common positive rate `m` across a dense-span family
(allowing state-dependent prefactors `C_ψ`), or on `InvariantMassGap`.
-/
set_option autoImplicit false
noncomputable section

namespace YangMills.MassGapResearch

open Filter Set MeasureTheory YangMills
open scoped Topology InnerProductSpace

section Measurability

theorem continuous_time : Continuous time :=
  (EuclideanSpace.proj timeAxis).continuous

theorem measurable_time : Measurable time :=
  continuous_time.measurable

theorem continuous_spatial : Continuous spatial := by
  unfold spatial
  exact (PiLp.continuous_toLp 2 (fun _ : SpaceAxis => ℝ)).comp
    (continuous_pi fun i => (EuclideanSpace.proj i.castSucc).continuous)

theorem continuous_minkowskiSquare : Continuous minkowskiSquare := by
  unfold minkowskiSquare
  exact (continuous_time.pow 2).sub (continuous_spatial.norm.pow 2)

theorem measurableSet_posTime : MeasurableSet {p : Spacetime | 0 < time p} :=
  (isOpen_lt continuous_const continuous_time).measurableSet

theorem measurableSet_energySlab (m : ℝ) :
    MeasurableSet {p : Spacetime | 0 < time p ∧ time p < m} :=
  ((isOpen_lt continuous_const continuous_time).inter
    (isOpen_lt continuous_time continuous_const)).measurableSet

theorem measurableSet_massRegion (m : ℝ) :
    MeasurableSet {p : Spacetime | p ≠ 0 ∧ minkowskiSquare p < m ^ 2} :=
  (isOpen_ne.inter (isOpen_lt continuous_minkowskiSquare continuous_const)).measurableSet

end Measurability

section PVMOperators

variable {H : HilbertSpace}

/-- On measurable sets, a self-adjoint idempotent PVM projection satisfies
`‖P(B) ψ‖² = μ_ψ(B)`. -/
theorem pvm_norm_sq_eq_diagonal_real (E : EnergyMomentumMeasure H)
    {B : Set Spacetime} (hB : MeasurableSet B) (ψ : H.carrier) :
    ‖E.projection B ψ‖ ^ 2 = (E.diagonal ψ).real B := by
  let P := E.projection B
  have hid : P (P ψ) = P ψ := by
    have hcomp := (E.intersection hB hB).trans (by rw [Set.inter_self])
    exact DFunLike.congr_fun hcomp ψ
  have hadj : P.adjoint = P := E.selfAdjoint hB
  have hinner : inner ℂ (P ψ) (P ψ) = (((E.diagonal ψ).real B : ℝ) : ℂ) := by
    calc
      inner ℂ (P ψ) (P ψ) = inner ℂ ψ (P.adjoint (P ψ)) :=
        (ContinuousLinearMap.adjoint_inner_right P ψ (P ψ)).symm
      _ = inner ℂ ψ (P ψ) := by rw [hadj, hid]
      _ = (((E.diagonal ψ).real B : ℝ) : ℂ) := (E.diagonalIdentity hB ψ).symm
  have hself : inner ℂ (P ψ) (P ψ) = ((‖P ψ‖ ^ 2 : ℝ) : ℂ) := by
    simp [Complex.ofReal_pow]
  exact Complex.ofReal_injective (hself.symm.trans hinner)

/-- Vanishing of the PVM projection at `ψ` is equivalent to vanishing of the
scalar diagonal spectral measure `E.diagonal ψ` on `B`. -/
theorem pvm_apply_eq_zero_iff_diagonal_zero (E : EnergyMomentumMeasure H)
    {B : Set Spacetime} (hB : MeasurableSet B) (ψ : H.carrier) :
    E.projection B ψ = 0 ↔ E.diagonal ψ B = 0 := by
  have hsq := pvm_norm_sq_eq_diagonal_real E hB ψ
  constructor
  · intro hzero
    apply (measureReal_eq_zero_iff).mp
    rw [← hsq, hzero, norm_zero, sq, zero_mul]
  · intro hzero
    have hreal : (E.diagonal ψ).real B = 0 := (measureReal_eq_zero_iff).mpr hzero
    have hnorm_sq : ‖E.projection B ψ‖ ^ 2 = 0 := hsq.trans hreal
    exact norm_eq_zero.mp (sq_eq_zero_iff.mp hnorm_sq)

/-- A bounded complex-linear operator vanishing on a set whose `ℂ`-span is dense
vanishes everywhere. -/
theorem clm_eq_zero_of_dense_span (A : H.Operator) {D : Set H.carrier}
    (hD : Dense (Submodule.span ℂ D : Set H.carrier))
    (hzero : ∀ ψ ∈ D, A ψ = 0) : A = 0 := by
  have hspan : Submodule.span ℂ D ≤ LinearMap.ker A.toLinearMap :=
    Submodule.span_le.mpr hzero
  have hon_span : ∀ v ∈ (Submodule.span ℂ D : Set H.carrier), A v = 0 :=
    fun v hv => hspan hv
  ext x
  exact hD.induction hon_span (isClosed_eq A.continuous continuous_zero) x

end PVMOperators

section WightmanBridge

variable {H : HilbertSpace} {Labels : FieldLabels}

/-- Observation 1 (`T01` review): `Measure.ext_of_charFun` applies directly to
`Spacetime` (`EuclideanSpace ℝ (Fin 4)`), so under `W0` the translation action
uniquely determines every state's joint energy-momentum diagonal measure. -/
theorem diagonal_eq_of_same_translations
    (T₁ T₂ : WightmanTheory H Labels) (hW0₁ : T₁.W0) (hW0₂ : T₂.W0)
    (htrans : ∀ x : Spacetime, T₁.translations.operator x = T₂.translations.operator x)
    (ψ : H.carrier) :
    T₁.energyMomentum.diagonal ψ = T₂.energyMomentum.diagonal ψ := by
  apply Measure.ext_of_charFun
  ext x
  rw [hW0₁.spectralRepresentation ψ x, hW0₂.spectralRepresentation ψ x, htrans x]

/-- Observation 3 (`T01` review): under `W0`, `W1` (`‖Ω‖ = 1`), and `W2`
(`vacuumInvariant`), the vacuum's joint energy-momentum measure is `δ_0`. -/
theorem vacuum_diagonal_eq_dirac_zero (T : WightmanTheory H Labels)
    (hW0 : T.W0) (hW1 : T.W1) (hW2 : T.W2) :
    T.energyMomentum.diagonal T.fields.vacuum.1 = Measure.dirac (0 : Spacetime) := by
  let Ω := T.fields.vacuum.1
  apply Measure.ext_of_charFun
  ext x
  have htrans_vac : T.translations.operator x Ω = Ω := by
    rw [← T.translationCompatibility x]
    exact hW2.vacuumInvariant (T.poincare.pureTranslation x)
  have hinner_vac : inner ℂ Ω Ω = (1 : ℂ) := by
    have hself : inner ℂ Ω Ω = ((‖Ω‖ ^ 2 : ℝ) : ℂ) := by
      simp [Complex.ofReal_pow]
    rw [hself, hW1.domain.normalizedVacuum]
    norm_num
  rw [hW0.spectralRepresentation Ω x, htrans_vac, hinner_vac, charFun_dirac]
  simp

/-- Under `W0`, `W1`, and `W2`, the open energy-slab projection vanishes on the
vacuum vector without any dynamical assumption. -/
theorem vacuum_slab_projection_eq_zero (T : WightmanTheory H Labels)
    (hW0 : T.W0) (hW1 : T.W1) (hW2 : T.W2) (m : ℝ) :
    T.energyMomentum.projection {p : Spacetime | 0 < time p ∧ time p < m}
      T.fields.vacuum.1 = 0 := by
  rw [pvm_apply_eq_zero_iff_diagonal_zero T.energyMomentum
    (measurableSet_energySlab m) T.fields.vacuum.1,
    vacuum_diagonal_eq_dirac_zero T hW0 hW1 hW2]
  have hnot : (0 : Spacetime) ∉ {p : Spacetime | 0 < time p ∧ time p < m} := by
    simp [time]
  rw [Measure.dirac_apply' _ (measurableSet_energySlab m)]
  simp [hnot]

/-- Positive-energy pushforward of `T.energyMomentum.diagonal ψ` along `time`. -/
def positiveEnergyMeasure (T : WightmanTheory H Labels) (ψ : H.carrier) :
    Measure ℝ :=
  ((T.energyMomentum.diagonal ψ).restrict {p : Spacetime | 0 < time p}).map time

/-- Per-state exponential Laplace decay at rate `m` kills `P(S_m) ψ`. -/
theorem pvm_slab_apply_zero_of_heat_bound (T : WightmanTheory H Labels)
    {m C : ℝ} (ψ : H.carrier)
    (h : ∀ t : ℝ, 0 ≤ t →
      Integrable (fun e : ℝ => Real.exp (-t * e)) (positiveEnergyMeasure T ψ) ∧
      (∫ e : ℝ, Real.exp (-t * e) ∂(positiveEnergyMeasure T ψ)) ≤
        C * Real.exp (-t * m)) :
    T.energyMomentum.projection {p : Spacetime | 0 < time p ∧ time p < m} ψ = 0 := by
  rw [pvm_apply_eq_zero_iff_diagonal_zero T.energyMomentum
    (measurableSet_energySlab m) ψ]
  exact MassGapResearch.energy_window_zero_of_heat_bound
    (T.energyMomentum.diagonal ψ) time measurable_time h

/-- Observation 4 (`T02` / `T07`): per-state positive-energy Laplace bounds at
one **common** positive rate `m` across a dense-span set `D` (with arbitrary
state-dependent prefactors `C_ψ`) establish `HasEnergyGapAt T m`. -/
theorem hasEnergyGapAt_of_spanning_heat_bounds (T : WightmanTheory H Labels)
    {D : Set H.carrier} {m : ℝ} (hm : 0 < m)
    (hD : Dense (Submodule.span ℂ D : Set H.carrier))
    (hheat : ∀ ψ ∈ D, ∃ C : ℝ, ∀ t : ℝ, 0 ≤ t →
      Integrable (fun e : ℝ => Real.exp (-t * e)) (positiveEnergyMeasure T ψ) ∧
      (∫ e : ℝ, Real.exp (-t * e) ∂(positiveEnergyMeasure T ψ)) ≤
        C * Real.exp (-t * m)) :
    HasEnergyGapAt T m := by
  refine ⟨hm, clm_eq_zero_of_dense_span _ hD ?_⟩
  intro ψ hψ
  obtain ⟨C, hC⟩ := hheat ψ hψ
  exact pvm_slab_apply_zero_of_heat_bound T ψ hC

/-- Equivalent phrasing for `SpecReview.EnergySlabEmpty`. -/
theorem energySlabEmpty_of_spanning_heat_bounds (T : WightmanTheory H Labels)
    {D : Set H.carrier} {m : ℝ} (hm : 0 < m)
    (hD : Dense (Submodule.span ℂ D : Set H.carrier))
    (hheat : ∀ ψ ∈ D, ∃ C : ℝ, ∀ t : ℝ, 0 ≤ t →
      Integrable (fun e : ℝ => Real.exp (-t * e)) (positiveEnergyMeasure T ψ) ∧
      (∫ e : ℝ, Real.exp (-t * e) ∂(positiveEnergyMeasure T ψ)) ≤
        C * Real.exp (-t * m)) :
    SpecReview.EnergySlabEmpty T m :=
  hasEnergyGapAt_of_spanning_heat_bounds T hm hD hheat

/-- Under `W1` (`denseDomain` and `cyclicVacuum`), per-word heat bounds at one
common rate `m > 0` on smeared field word vectors `(T.fields.vector word).1`
already cover a dense-span family and imply `HasEnergyGapAt T m`. -/
theorem hasEnergyGapAt_of_word_heat_bounds (T : WightmanTheory H Labels)
    (hW1 : T.W1) {m : ℝ} (hm : 0 < m)
    (hwords : ∀ word : List (Labels.carrier × TestFunction),
      ∃ C : ℝ, ∀ t : ℝ, 0 ≤ t →
        Integrable (fun e : ℝ => Real.exp (-t * e))
          (positiveEnergyMeasure T (T.fields.vector word).1) ∧
        (∫ e : ℝ, Real.exp (-t * e)
          ∂(positiveEnergyMeasure T (T.fields.vector word).1)) ≤
            C * Real.exp (-t * m)) :
    HasEnergyGapAt T m := by
  have hD : Dense (Submodule.span ℂ
      (Set.range fun word => (T.fields.vector word).1) : Set H.carrier) := by
    rw [← hW1.domain.cyclicVacuum]
    exact hW1.domain.denseDomain
  apply hasEnergyGapAt_of_spanning_heat_bounds T hm hD
  rintro ψ ⟨word, rfl⟩
  exact hwords word

/-- Centered / vacuum-complement form: if the slab projection vanishes on the
vacuum vector and `D` spans a dense subspace of `(ℂ ∙ Ω)ᗮ`, then per-state heat
bounds on `D` at common rate `m > 0` imply `HasEnergyGapAt T m`. -/
theorem hasEnergyGapAt_of_vacuum_orth_heat_bounds (T : WightmanTheory H Labels)
    {D : Set H.carrier} {m : ℝ} (hm : 0 < m)
    (hvac : T.energyMomentum.projection
      {p : Spacetime | 0 < time p ∧ time p < m} T.fields.vacuum.1 = 0)
    (hD : (ℂ ∙ T.fields.vacuum.1)ᗮ ≤ (Submodule.span ℂ D).topologicalClosure)
    (hheat : ∀ ψ ∈ D, ∃ C : ℝ, ∀ t : ℝ, 0 ≤ t →
      Integrable (fun e : ℝ => Real.exp (-t * e)) (positiveEnergyMeasure T ψ) ∧
      (∫ e : ℝ, Real.exp (-t * e) ∂(positiveEnergyMeasure T ψ)) ≤
        C * Real.exp (-t * m)) :
    HasEnergyGapAt T m := by
  let Ω := T.fields.vacuum.1
  have hspan_top : (Submodule.span ℂ (insert Ω D)).topologicalClosure = ⊤ := by
    rw [eq_top_iff]
    have horth : (ℂ ∙ Ω) ⊔ (ℂ ∙ Ω)ᗮ = ⊤ :=
      Submodule.sup_orthogonal_of_hasOrthogonalProjection
    rw [← horth, sup_le_iff]
    constructor
    · exact (Submodule.span_mono (Set.singleton_subset_iff.mpr (Set.mem_insert Ω D))).trans
        (Submodule.le_topologicalClosure _)
    · exact hD.trans (Submodule.topologicalClosure_mono
        (Submodule.span_mono (Set.subset_insert Ω D)))
  have hdense : Dense (Submodule.span ℂ (insert Ω D) : Set H.carrier) :=
    Submodule.dense_iff_topologicalClosure_eq_top.mpr hspan_top
  refine ⟨hm, clm_eq_zero_of_dense_span _ hdense ?_⟩
  intro ψ hψ
  rcases Set.mem_insert_iff.mp hψ with rfl | hmem
  · exact hvac
  · obtain ⟨C, hC⟩ := hheat ψ hmem
    exact pvm_slab_apply_zero_of_heat_bound T ψ hC

/-- Full `W0` + `W1` + `W2` centered criterion: per-state positive-energy heat
bounds at one common rate `m > 0` on any set `D` whose span is dense in
`(ℂ ∙ Ω)ᗮ` imply `HasEnergyGapAt T m` (vacuum handled automatically). -/
theorem hasEnergyGapAt_of_W0_W1_W2_vacuum_orth_heat_bounds
    (T : WightmanTheory H Labels) (hW0 : T.W0) (hW1 : T.W1) (hW2 : T.W2)
    {D : Set H.carrier} {m : ℝ} (hm : 0 < m)
    (hD : (ℂ ∙ T.fields.vacuum.1)ᗮ ≤ (Submodule.span ℂ D).topologicalClosure)
    (hheat : ∀ ψ ∈ D, ∃ C : ℝ, ∀ t : ℝ, 0 ≤ t →
      Integrable (fun e : ℝ => Real.exp (-t * e)) (positiveEnergyMeasure T ψ) ∧
      (∫ e : ℝ, Real.exp (-t * e) ∂(positiveEnergyMeasure T ψ)) ≤
        C * Real.exp (-t * m)) :
    HasEnergyGapAt T m :=
  hasEnergyGapAt_of_vacuum_orth_heat_bounds T hm
    (vacuum_slab_projection_eq_zero T hW0 hW1 hW2 m) hD hheat

/-- Unconditional direction of `T01` review Proposition 2: `InvariantMassGap`
implies `EnergySlabEmpty` (and `HasEnergyGapAt`) via `S_m ⊆ R_m` and PVM
idempotence on intersections. -/
theorem energySlabEmpty_of_invariantMassGap (T : WightmanTheory H Labels)
    {m : ℝ} (hinv : SpecReview.InvariantMassGap T m) :
    SpecReview.EnergySlabEmpty T m := by
  rcases hinv with ⟨hm, hR0⟩
  refine ⟨hm, ?_⟩
  let S : Set Spacetime := {k : Spacetime | 0 < time k ∧ time k < m}
  let R : Set Spacetime := {k : Spacetime | k ≠ 0 ∧ minkowskiSquare k < m ^ 2}
  have hsub : S ⊆ R := by
    rintro k ⟨ht0, htm⟩
    refine ⟨?_, ?_⟩
    · intro hk0
      have : time k = 0 := by simp [time, hk0]
      linarith
    · unfold minkowskiSquare
      have hsq : time k ^ 2 < m ^ 2 := sq_lt_sq.mpr (by rw [abs_of_pos ht0, abs_of_pos hm]; exact htm)
      have hnorm : 0 ≤ ‖spatial k‖ ^ 2 := sq_nonneg _
      linarith
  have hinter : S ∩ R = S := Set.inter_eq_self_of_subset_left hsub
  calc
    T.energyMomentum.projection S
      = T.energyMomentum.projection (S ∩ R) := by rw [hinter]
    _ = (T.energyMomentum.projection S).comp (T.energyMomentum.projection R) :=
        (T.energyMomentum.intersection (measurableSet_energySlab m)
          (measurableSet_massRegion m)).symm
    _ = (T.energyMomentum.projection S).comp 0 := by rw [hR0]
    _ = 0 := ContinuousLinearMap.comp_zero _

end WightmanBridge

section Controls

/-- Failure control (`T02` failure criterion): state-dependent positive rates
`m_n = m / (n + 2)` tending to zero do NOT exclude positive spectral weight
below `m`, even when every member `n` has an exact exponential Laplace bound at
its own positive rate `m_n`. -/
theorem state_dependent_rates_allow_subthreshold_atoms {m : ℝ} (hm : 0 < m) :
    ∃ μ : ℕ → Measure ℝ,
      (∀ n, IsFiniteMeasure (μ n)) ∧
      (∀ n, ∃ r > 0, ∀ t : ℝ, 0 ≤ t →
        Integrable (fun e : ℝ => Real.exp (-t * e)) (μ n) ∧
        (∫ e : ℝ, Real.exp (-t * e) ∂(μ n)) ≤ 1 * Real.exp (-t * r)) ∧
      (∀ n, μ n (Iio m) ≠ 0) := by
  refine ⟨fun n => Measure.dirac (m / ((n : ℝ) + 2)), ?_, ?_, ?_⟩
  · intro n; infer_instance
  · intro n
    let r := m / ((n : ℝ) + 2)
    have hpos : 0 < (n : ℝ) + 2 := by positivity
    have hr : 0 < r := div_pos hm hpos
    refine ⟨r, hr, fun t _ht => ?_⟩
    constructor
    · exact integrable_dirac (by simp)
    · rw [integral_dirac, one_mul]
  · intro n
    have hpos : 0 < (n : ℝ) + 2 := by positivity
    have hlt : m / ((n : ℝ) + 2) < m := by
      rw [div_lt_iff₀ hpos]
      nlinarith
    simp [Set.mem_Iio.mpr hlt]

end Controls

#print axioms continuous_time
#print axioms measurable_time
#print axioms measurableSet_energySlab
#print axioms measurableSet_massRegion
#print axioms pvm_norm_sq_eq_diagonal_real
#print axioms pvm_apply_eq_zero_iff_diagonal_zero
#print axioms clm_eq_zero_of_dense_span
#print axioms diagonal_eq_of_same_translations
#print axioms vacuum_diagonal_eq_dirac_zero
#print axioms vacuum_slab_projection_eq_zero
#print axioms pvm_slab_apply_zero_of_heat_bound
#print axioms hasEnergyGapAt_of_spanning_heat_bounds
#print axioms energySlabEmpty_of_spanning_heat_bounds
#print axioms hasEnergyGapAt_of_word_heat_bounds
#print axioms hasEnergyGapAt_of_vacuum_orth_heat_bounds
#print axioms hasEnergyGapAt_of_W0_W1_W2_vacuum_orth_heat_bounds
#print axioms energySlabEmpty_of_invariantMassGap
#print axioms state_dependent_rates_allow_subthreshold_atoms

end YangMills.MassGapResearch
