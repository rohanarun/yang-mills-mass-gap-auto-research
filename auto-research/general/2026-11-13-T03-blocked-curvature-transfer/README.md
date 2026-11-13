# Local curvature transfer through the actual blocking kernel

## Metadata and scope

- Date: 2026-11-13. Rohan Arun with OpenAI Codex assistance.
- Tracks: T03-B/C, T04, T07. Base: `04454a0789335f13fd2aa4bb70a759fd2dad396e`.
- Upstream pin: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [provenance](provenance.json).
- New result: a written one-step plaquette-moment bound for the **actual normalized kernel push of any fine input law**, retaining generated interactions and every tag branch. This is a propagation estimate, not a contraction or a mass-gap theorem.
- Formal evidence: four frame/predictor bounds against source definitions pass Lean 4.32.0 with `--trust=0`; [source](FrameControl.lean), [log](lean-check.log), [receipt](lean-verification.json). The full geometric/probability application below is written, not Lean-checked or independently reviewed.
- Related: [bare Wilson branch probability](../2026-11-11-T03-bare-branch-probability/README.md), [upstream branch audit](../2026-11-11-T03-upstream-branch-audit/README.md), [exact SU(2) loop-noise transfer](../2026-11-11-T03-loop-noise-transfer/README.md).
- No novelty claim. The purpose is to bridge the recorded bare-law estimate to a generated law without replacing its density by a Wilson action.

## Exact claim and hypotheses

Fix one `StepData S` with block side L, patch radius r, and the source condition `S.patch.Branches S.kernel G`. Use fundamental SU(2). Assume the coarse side is at least three and the fine side is at least 2R+1, where R = r+L. These assumptions keep the four plaquette links distinct and permit a box gauge to extend to a periodic fine gauge. The source's `fitsPatch` field is stronger than the latter size condition, since r = (J+3)L with J >= 4.

Let mu be any fine probability law for which the measurable kernel push is defined, and let mu' be that push with the actual positive kernel coupling kappa = penalty * beta. For the history application, mu is the normalized `Rep.eval`, including all generated interactions. Set

$$
u=\sup_p\mathbb E_\mu\mathrm{price}(U_p),\quad
a=I_2(\kappa)/I_1(\kappa),\quad
N_R=6(2R)^2(2R+1)^2,\quad
K_R=[3200(2R+1)N_R]^2.
$$

No translation invariance or independence of fine plaquettes is assumed. The finite supremum u lies in [0,2]. For every coarse plaquette p, the written conclusion is

$$
1-a^4\ \leq\ \mathbb E_{\mu'}\mathrm{price}(V_p)
\ \leq\ 1-a^4+a^4\min\{2,K_Ru\}.
\tag{1}
$$

One can also cap the upper bound at 2. All constants are independent of the total torus volume subject to the size hypotheses. They depend very badly on the local footprint R. The bound is often trivial.

Falsification criteria: losing shared tags, changing the fine law, using four independent noises for a repeated link, dropping the normalization, or using a nonextendible gauge would invalidate the application. Each is addressed explicitly below.

## 1. Source-level bounds for both branches

Suppose that, in a fixed gauge, every coordinate route in a patch has transport chord at most T >= 0.

**Minimizing frame.** Construct `Pairs` from the raw route transports. Reversal is the source's `backOrder`; the normalized frame minimizer is also a global minimizer modulo common left multiplication. Applying the previously checked `pairwise_bound` and using h(center)=1 gives

$$
\mathrm{chord}(h_x)\leq12T.
$$

The matrix-to-chord scale cancels. The new theorem `minimizing_chord` checks this dictionary against `Patch.minimizing` in Lean. It imposes no small-cutoff condition.

**Fallback frame.** `Patch.frame` uses a reanchored axial frame outside `usesMin`. It is the product of two route transports, one inverted, so its chord is at most 2T. Thus `frame_chord` proves the bound 12T for every frame tag on either branch. No probability estimate for branch failure is needed for this bound.

**Predictor.** If every connector Y_x has chord at most q, the weighted matrix mean M lies within normalized distance q of the identity. Source `min_iff` makes `Patch.best Y` a nearest group element to M. Comparing it with the identity and using the triangle inequality gives chord(best Y) <= 2q. Fallback prediction selects one Y_x and satisfies the same bound. Theorems `best_chord` and `predict_chord` check both conclusions in Lean, with no predictor cutoff margin.

These inequalities hold for the general upstream `Gauge`; SU(2) enters the exact noise coefficient later. They do not assert a new uniqueness theorem. All four axiom reports contain only `propext`, `Classical.choice`, and `Quot.sound`.

## 2. One common gauge for a plaquette footprint

Lift a coarse plaquette's four corners to fine coordinates 0, L e_i, L e_j, L(e_i+e_j), relative to its base. Their four patch boxes and every straight connector segment fit inside X = [-R,R]^4, R=r+L. Let

$$
F_X(U)=\sum_{p\subset X}\mathrm{chord}(U_p).
$$

The existing upstream [`Axial.existence`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Branch/Pick.lean#L80) gives a gauge with total internal edge chord

$$
T\leq16(2R+1)F_X(U).
$$

Each coordinate route and each straight connector segment stays inside X and traverses each unoriented edge at most once. Its chord is bounded by T. The box injects into the torus by the size assumption, so its gauge values extend to a periodic fine gauge, chosen arbitrarily elsewhere. This is a pointwise argument: no measurable selection of that gauge is required, because the final bound contains only the original gauge-invariant F_X.

Under `Branches`, source `frame_gauged`, `updateGauged`, and `bond_gauge` transport the actual chosen frames and predictors with the same tags. Consequently a predicted closed plaquette has gauge-invariant price. No independent choice of gauge at its four corners is being made.

For each connector, its two frames cost at most 12T each and the straight transport costs at most T. Every connector therefore has chord at most 25T. The predictor bound gives 50T for each predicted coarse link. Four links give

$$
\mathrm{chord}(Q_p)\leq200T
\leq3200(2R+1)F_X(U),
$$

and hence

$$
\mathrm{price}(Q_p)\leq\tfrac12[3200(2R+1)]^2 F_X(U)^2.
\tag{2}
$$

This is uniform over all joint tags, including fallback branches and tags of zero likelihood. It uses neither a favorable-tag conditioning nor separate copies of shared site tags.

## 3. Normalize and integrate the actual input law

Cauchy-Schwarz and chord squared = 2 price give

$$
\mathbb E_\mu F_X^2
\leq N_R\sum_{p\subset X}2\mathbb E_\mu\mathrm{price}(U_p)
\leq2N_R^2u.
$$

Let rho(dU,t) = mu(dU) `S.likelihood U t`. Source `chosen` says the tag weights sum to one. Integrating (2) therefore gives

$$
\mathbb E_\rho\mathrm{price}(Q_p)\leq\min\{2,K_Ru\}.
\tag{3}
$$

The full coarse law is the marginal of rho times the independent normalized output-noise factors. The [previous loop calculation](../2026-11-11-T03-loop-noise-transfer/README.md) gives, conditionally on U and all tags,

$$
\mathbb E[\tfrac12\mathrm{Tr}(V_p)\mid U,t]
=a^4\tfrac12\mathrm{Tr}(Q_p).
$$

Thus, exactly,

$$
\mathbb E_{\mu'}\mathrm{price}(V_p)
=1-a^4+a^4\mathbb E_\rho\mathrm{price}(Q_p).
\tag{4}
$$

Combining (3)-(4) proves (1) as a written argument. The positive term 1-a^4 is unavoidable even for a perfectly flat prediction field. It is a one-plaquette noise contribution, not a spectral gap or a lower bound on a bad-branch probability.

For the selected history, [`Transfer`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/History.lean#L223) identifies the unnormalized push, and `partition_eq` supplies equal normalization on both levels. Thus mu' here is its actual normalized generated measure. This use of the history interface is source inspection and written integration, not a new full-history Lean replay.

## 4. What can now be propagated

At the bare starting level N, the [previous written estimate](../2026-11-11-T03-bare-branch-probability/README.md) supplies u_N <= B(beta_N), provided beta_N >= 1. At each step satisfying the stated geometry and kernel conditions, (1) gives

$$
u_m\leq\min\{2,\ 1-a_m^4+a_m^4\min\{2,K_{R_m}u_{m+1}\}\}.
\tag{5}
$$

This keeps every generated interaction through the actual input expectation u_(m+1). At any level, the geometric argument in the earlier branch record also converts u_m into

$$
P_m(\neg\mathrm{usesMin})
\leq\min\{1,\ 2[48(2r+1)]^2N_r^2u_m/\epsilon^2\}.
$$

The bare-law beta formula has not been substituted at intermediate levels. The extension is the recurrence (5), which may provide only a trivial bound after iteration.

## Limits and next target

K_R grows like R^10 and is already enormous at small radius. There is no established inequality a_m^4 K_(R_m) < 1. For fixed R, that coefficient tends to K_R > 1 as kappa grows. Consequently this estimate supplies no uniform multiscale contraction in the weak-coupling regime. It does not show that contraction is impossible under a sharper method.

Contraction of this unscaled plaquette moment is not itself a necessary condition for a mass gap: lattice spacing changes between levels. Any proposed improvement must specify the rescaling and connect the controlled quantity to the required physical covariance.

The source step transforms a local curvature moment, not the spatial covariance needed for a mass gap. Even a useful small value of u_m would leave smooth-sector correlations, defect connections, physical scaling, and dense-state reconstruction unresolved. Neither (1) nor its positive noise floor establishes exponential heat decay.

The next discriminating task is to replace the uniform tag-by-tag triangle estimate by an estimate of the **likelihood-weighted prediction plaquette**, retaining cancellations between shared frames. Derive it for a specific actual input law or document why a proposed bound fails. Merely optimizing the existing numerical constant cannot turn the current R^10 upper bound into the required physical correlation estimate.

## Reproduction and verification boundaries

Use the Lean 4.32.0 runtime and matching pinned Mathlib packages from the [branch replay](../2026-11-11-T03-upstream-branch-audit/README.md). First build its unchanged `BranchCorollary.lean` into REPLAY_LIB. Put that directory and each package's `.lake/build/lib/lean` in LEAN_PATH, then run:

```sh
lean --trust=0 -j1 -DmaxHeartbeats=0 -R RESULT_DIR -o BUILD_DIR/FrameControl.olean RESULT_DIR/FrameControl.lean
```

The receipt records source/log hashes, the imported corollary hash, compiler version, and elapsed time. The formal statements concern source `Patch` frames and predictors only. The common-gauge footprint, moment integration, Bessel identity, and history application are not included in that formalization.

Run `python3 auto-research/general/2026-11-13-T03-blocked-curvature-transfer/check_footprints.py` from the repository root for the finite footprint and constant checks. [Output](checks.json) and [receipt](verification.json) are archived. These finite checks are diagnostics, not general geometric proofs or Yang–Mills simulations. No independent mathematical review or proof of novelty has been obtained.

## Review history

2026-11-13: initial source application and bounded formal checks proposed for review. The Yang–Mills mass gap remains unproved.
