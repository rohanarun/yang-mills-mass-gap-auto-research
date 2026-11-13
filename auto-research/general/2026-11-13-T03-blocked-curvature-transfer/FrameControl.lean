import BranchCorollary

/-! Source-level frame control. This is not a physical mass-gap theorem. -/
set_option autoImplicit false
noncomputable section
namespace Research.BlockedCurvature
open YM YM.Branch YM.Lattice YM.Wilson YM.RG
open scoped Matrix.Norms.Frobenius BigOperators

variable {G : Gauge}

theorem minimizing_chord (P : Patch) (U : CoverConfig G) {T : ℝ}
    (hT : 0 ≤ T)
    (hr : ∀ (i j : P.Points) (l : Lattice.Order),
      G.chord (travel U i.val (route i.val j.val l)) ≤ T)
    {h : P.Frame G} (hm : P.minimizing U h) (i : P.Points) :
    G.chord (h i) ≤ 12 * T := by
  let A : Pairs P.Points Lattice.Order G :=
    { W := fun i j l => travel U i.val (route i.val j.val l)
      mirror := backOrder
      same := fun i l => by simp [travel]
      reflect := fun i j l => by
        rw [back_route]
        convert (travel_reverse (route i.val j.val l) U i.val) using 1
        simp only [route_end] }
  have hs : A.Solves h := by
    intro f
    let q : P.Frame G := fun i => (f P.center)⁻¹ * f i
    have hx := hm.2 q (by simp [q])
    change A.cost h ≤ A.cost q at hx
    dsimp only [q] at hx
    rwa [A.moves] at hx
  have hw (x y : P.Points) (l : Lattice.Order) :
      ‖G.mat (A.W x y l) - 1‖ ≤ G.colorScale * T := by
    have ht := (div_le_iff₀ G.colorScale_pos).mp (hr x y l)
    simpa only [mul_comm] using ht
  have hp := Research.BranchAudit.pairwise_bound A
    (mul_nonneg G.colorScale_pos.le hT) hw hs i P.center
  rw [hm.1, G.mat_one] at hp
  apply (div_le_iff₀ G.colorScale_pos).mpr
  change ‖G.mat (h i) - 1‖ ≤ 12 * T * G.colorScale
  nlinarith

theorem frame_chord (P : Patch) (K : KernelChoices) (U : CoverConfig G)
    {T : ℝ} (hT : 0 ≤ T)
    (hr : ∀ (i j : P.Points) (l : Lattice.Order),
      G.chord (travel U i.val (route i.val j.val l)) ≤ T)
    (tag : P.FrameTag) (i : P.Points) :
    G.chord (P.frame K U tag i) ≤ 12 * T := by
  unfold Patch.frame
  split
  · exact minimizing_chord P U hT hr (P.min_exists U).choose_spec i
  · have ht := G.chord_triangle (P.axial U tag P.center)⁻¹ (P.axial U tag i)
    rw [G.chord_inv] at ht
    have hc := hr tag.1 P.center tag.2
    have hi := hr tag.1 i tag.2
    change G.chord (P.axial U tag P.center) ≤ T at hc
    change G.chord (P.axial U tag i) ≤ T at hi
    linarith

theorem best_chord (P : Patch) (Y : P.Connector G) {q : ℝ}
    (_hq : 0 ≤ q) (hy : ∀ i, G.chord (Y i) ≤ q) :
    G.chord (P.best Y) ≤ 2 * q := by
  let M := ∑ i, P.weight i • G.mat (Y i)
  have hn : G.Nearest (P.best Y) M :=
    (min_iff P.weight P.weight_sum Y (P.best Y)).mpr (P.bond_min Y).choose_spec
  have he : M - 1 = ∑ i, P.weight i • (G.mat (Y i) - 1) := by
    simp only [smul_sub, Finset.sum_sub_distrib, ← Finset.sum_smul,
      P.weight_sum, one_smul, M]
  have hb : ‖M - 1‖ ≤ G.colorScale * q := by
    rw [he]
    calc
      _ ≤ ∑ i, ‖P.weight i • (G.mat (Y i) - 1)‖ := norm_sum_le _ _
      _ = ∑ i, P.weight i * ‖G.mat (Y i) - 1‖ := by
        simp only [norm_smul, Real.norm_of_nonneg (P.weight_nonneg _)]
      _ ≤ ∑ i, P.weight i * (G.colorScale * q) := by
        apply Finset.sum_le_sum
        intro i _
        apply mul_le_mul_of_nonneg_left _ (P.weight_nonneg i)
        have hi := (div_le_iff₀ G.colorScale_pos).mp (hy i)
        simpa only [mul_comm] using hi
      _ = G.colorScale * q := by rw [← Finset.sum_mul, P.weight_sum, one_mul]
  have hc := hn 1
  simp only [G.mat_one] at hc
  have ht := norm_sub_le_norm_sub_add_norm_sub (G.mat (P.best Y)) M 1
  rw [norm_sub_rev (G.mat (P.best Y)) M] at ht
  apply (div_le_iff₀ G.colorScale_pos).mpr
  change ‖G.mat (P.best Y) - 1‖ ≤ 2 * q * G.colorScale
  nlinarith

theorem predict_chord (P : Patch) (K : KernelChoices) (Y : P.Connector G)
    {q : ℝ} (hq : 0 ≤ q) (hy : ∀ i, G.chord (Y i) ≤ q) (i : P.Points) :
    G.chord (P.predict K Y i) ≤ 2 * q := by
  unfold Patch.predict
  split
  · exact best_chord P Y hq hy
  · exact (hy i).trans (by linarith)

#print axioms minimizing_chord
#print axioms frame_chord
#print axioms best_chord
#print axioms predict_chord
end Research.BlockedCurvature
