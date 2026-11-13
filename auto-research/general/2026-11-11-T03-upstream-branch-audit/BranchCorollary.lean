import YM.Branch.Pick

/-! A corollary of the existing upstream synchronization lemmas.
No new dynamical or mass-gap estimate is asserted. -/
set_option autoImplicit false
noncomputable section
namespace Research.BranchAudit
open YM YM.Branch
open scoped Matrix.Norms.Frobenius

variable {G : Gauge} {n L : Type} [Fintype n] [Fintype L]
  [Nonempty n] [Nonempty L]

theorem pairwise_bound (A : Pairs n L G) {d : ℝ} (hd : 0 ≤ d)
    (hw : ∀ x y k, ‖G.mat (A.W x y k) - 1‖ ≤ d)
    {h : n → G.El} (hs : A.Solves h) (i j : n) :
    ‖G.mat (h i) - G.mat (h j)‖ ≤ 12 * d := by
  obtain ⟨a, ha⟩ := G.nearest_exists (Pairs.centroid h)
  let q : n → G.El := fun x => a⁻¹ * h x
  have hq : A.Solves q := by
    intro f
    change A.cost (fun x => a⁻¹ * h x) ≤ A.cost f
    rw [A.moves]
    exact hs f
  have hc : G.Nearest 1 (Pairs.centroid q) := by
    change G.Nearest 1 (Pairs.centroid (fun x => a⁻¹ * h x))
    rw [Pairs.turns, ← inv_mul_cancel a]
    exact (G.nearest_left a⁻¹ a _).mpr ha
  have close (x : n) : ‖G.mat (q x) - 1‖ ≤ 6 * d := by
    have hf := A.closeness hd hw hq hc x
    have hn := A.self_consistent hq x 1
    simp only [G.mat_one] at hn
    have ht := norm_sub_le_norm_sub_add_norm_sub (G.mat (q x)) (A.feedback q x) 1
    rw [norm_sub_rev (G.mat (q x)) (A.feedback q x)] at ht
    linarith
  have hp : ‖G.mat (q i) - G.mat (q j)‖ ≤ 12 * d := by
    have ht := norm_sub_le_norm_sub_add_norm_sub (G.mat (q i)) 1 (G.mat (q j))
    rw [norm_sub_rev 1 (G.mat (q j))] at ht
    linarith [close i, close j]
  have he : ‖G.mat (q i) - G.mat (q j)‖ = ‖G.mat (h i) - G.mat (h j)‖ := by
    dsimp only [q]
    rw [G.mat_mul, G.mat_mul, ← mul_sub,
      Gauge.mul_frob_eq _ _ (G.mat_star_mul _)]
  rwa [he] at hp

#print axioms pairwise_bound
end Research.BranchAudit
