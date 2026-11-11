# A sufficient small-cutoff condition for SU(2) frame uniqueness

## Metadata and question

- Date / author: 2026-11-11; Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03, T04, T06. Base: `566f44c322142ebd14f8fc3a86f82341a3d61ac4`, the head of [PR #4](https://github.com/rohanarun/yang-mills-mass-gap-auto-research/pull/4).
- Dependency: the written [frame-localization argument](../2026-11-11-T03-frame-axial-control/README.md). This PR is stacked on that unmerged work; it does not independently verify it.
- Upstream: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [provenance and source hashes](provenance.json).
- Outcome: written sufficient condition for the source's `frame_unique` clause in fundamental SU(2), and quantitative control of optimization error modulo common gauge rotation.
- Evidence: written proof, source inspection, exact rational matrix certificates on finite relaxed arrays. No Lean formalization, upstream replay, or independent review.
- Bounded question: does a uniformly small frame cutoff imply uniqueness, rather than only closeness of all minimizers?
- Falsification: incorrect quaternion multiplication orientation, unjustified scalar row sums, or failure of the certificate's positive-definiteness bound invalidates the argument. Planned tests: small exact rational matrices and noncommuting transport arrays, seconds of local compute.

## 1. Statement and precise scope

For fundamental SU(2), any source patch, and a kernel with

$$
0<\varepsilon=\mathrm{frame\_cut}\leq\frac1{16},
$$

the following holds at the **written proof level**:

> For every cover configuration satisfying `usesMin`, there is exactly one centre-normalized global minimizer of `score`.

This is the statement of the [source `Branches.frame_unique` field](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Patch.lean#L181), under an explicit sufficient parameter condition. The proof uses the source's compactness existence theorem, but **does not assume** `frame_unique`, the other branch hypotheses, measurability of `selected`, or any probability law. It concerns exact global minimizers, not arbitrary stationary points.

We have not established that the existing selected history uses this cutoff. Shrinking its cutoff would change its kernel and would require checking the remaining analytic obligations again. This does not prove all of `Branches`: `axial_exists` remains separate, and predictor uniqueness needs its own condition (the [fundamental SU(2) audit](../2026-11-11-T03-cutoff-endpoint/README.md) gives `predictor_cut <= 1`). No Lean declaration implementing the source field has been added.

The constant $1/16$ is conservative; no optimal threshold or novelty is claimed.

## 2. Localization without assuming uniqueness

Use the notation of PR #4. Fix a centre-based axial frame $A$, and write a global minimizer as $h_i=k_iA_i$, with $k_o=1$. The routed transports in axial coordinates obey

$$
|E_{ij,l}-1|\leq\varepsilon,\qquad E_{ii,l}=1.
$$

The proof in PR #4 gives, for $\bar k=N^{-1}\sum_i k_i$,

$$
|\bar k|\geq\sqrt{1-2\varepsilon^2},\qquad
\left|k_i-\frac{\bar k}{|\bar k|}\right|
\leq\frac{2\varepsilon}{\sqrt{1-2\varepsilon^2}}.
$$

Thus the diameter, not just distance from the pinned centre, satisfies

$$
|k_i-k_j|\leq\frac{4\varepsilon}{\sqrt{1-2\varepsilon^2}}
\leq5\varepsilon.
$$

The last inequality follows from $1-2\varepsilon^2\geq16/25$ in the stated range. Express the transports in the minimizing frame:

$$
F_{ij,l}=k_iE_{ij,l}k_j^{-1},\qquad
|F_{ij,l}-1|\leq6\varepsilon=:\delta\leq3/8.
$$

No reciprocal-path assumption is made about $F_{ij,l}$ and $F_{ji,l}$. The score averages all ordered pairs and all route orders; both orientations are retained below.

## 3. A real quaternion matrix certificate

Let $R(q)$ be the real $4\times4$ matrix for right multiplication by a quaternion $q$: $R(q)x=xq$ for column-coordinate vectors. Then

$$
R(q)^T=R(\bar q),\qquad \|R(q)\|=|q|.
$$

Let $m$ denote the number of route orders, and set

$$
a_{ij}=\frac1{2m}\sum_l\left(\overline{F_{ij,l}}+F_{ji,l}\right),
\qquad C_{ij}=R(a_{ij}).
$$

The block matrix $C$ is real symmetric: $a_{ji}=\overline{a_{ij}}$. Also $C_{ii}=I_4$ and $\|C_{ij}-I_4\|\leq\delta$. A competitor can be written as $h'_i=v_i h_i$ with unit quaternions $v_i$. Its score is

$$
S_F(v)=1-\frac1{N^2}v^TCv.
$$

This equality follows by symmetrizing $\mathrm{Re}(v_iF_{ij,l}v_j^{-1})$ over the ordered pair. The ordering of quaternion products is essential.

At the minimizing frame, $v_i=1$. Common left multiplication preserves the score, so any variation at the centre can be reanchored as in PR #4. The local-optimality equation at **every** site therefore makes the quaternion row sum real:

$$
\sum_j a_{ij}=\alpha_i\in\mathbb R,\qquad
\sum_j C_{ij}=\alpha_i I_4.
$$

More explicitly, the local field excluding $j=i$ is $\lambda_i1$ with $\lambda_i\geq0$; the diagonal term adds one, so $\alpha_i=\lambda_i+1$. Quaternion linearity is why the row sum is a scalar matrix, rather than merely an equation on a single vector.

Define

$$
L=\mathrm{diag}(\alpha_i I_4)-C,\qquad
L_0=(NI_N-\mathbf1\mathbf1^T)\otimes I_4.
$$

Both matrices annihilate all constant quaternion blocks. Their difference satisfies

$$
\|L-L_0\|\leq2N\delta.
$$

Indeed, each diagonal row-sum error is at most $N\delta$. For the symmetric block matrix $C-\mathbf1\mathbf1^T\otimes I_4$, its quadratic form is bounded in absolute value by $\delta(\sum_i|z_i|)^2\leq N\delta\sum_i|z_i|^2$. Combining these two bounds proves the claim.

On the orthogonal complement of constant blocks, $L_0=NI$, and hence

$$
z^TLz\geq N(1-2\delta)\sum_i|z_i|^2
\geq\frac N4\sum_i|z_i|^2.
$$

Thus $L$ is positive semidefinite, with kernel **exactly** the four-dimensional space of constant quaternion blocks. This is a finite optimization certificate. Its positive eigenvalues are not energies of the physical Yang–Mills Hamiltonian.

## 4. Uniqueness and an optimization-error estimate

For any unit-quaternion competitor $v$, the scalar row sums give the exact identity

$$
S_F(v)-S_F(1)=\frac1{N^2}v^TLv.
$$

Writing $\bar v=N^{-1}\sum_i v_i$ and $\gamma=1-2\delta\geq1/4$ yields

$$
S_F(v)-S_F(1)
\geq\frac\gamma N\sum_i|v_i-\bar v|^2
=\gamma(1-|\bar v|^2).
$$

Another global minimizer has the same score, so $v_i=g$ for a single unit quaternion $g$. Since both frames are normalized at the centre, $v_o=1$, forcing $g=1$. This proves uniqueness. For $N=1$, the centre constraint already fixes the frame; actual source patches have more than one point.

For a competitor with excess score $\eta$, distance modulo a common left rotation obeys

$$
\inf_{|g|=1}\frac1N\sum_i|v_i-g|^2
=2(1-|\bar v|)
\leq\frac{2\eta}{\gamma}\leq8\eta.
$$

If $\bar v=0$, the displayed infimum formula still holds. This bound is uniform in patch size **modulo common gauge rotation**. It is not uniform pointwise stability of the anchored frame. The [previous energy-only control](../../negative-results/2026-11-11-T03-frame-energy-only/README.md), with one pinned spin and all others reversed, still rules out that stronger inference from small excess score alone.

## 5. Relation to existing synchronization methods

This is an application of a standard certificate strategy, not a claimed new general method. Bandeira, Boumal and Singer construct dual certificates from optimality conditions in [their angular-synchronization paper, sections 4.2–4.4](https://arxiv.org/html/1411.3272v3). Their stated probabilistic complex-phase setting differs from the deterministic quaternion source application here. Chen, Zhao, Cui and So also study [quaternion synchronization and semidefinite certificates](https://www1.se.cuhk.edu.hk/~manchoso/papers/rot_sync_qtn_sdr-icassp26.pdf) under a quaternion-normal noise model. Only that paper's abstract/introduction was inspected; its exact theorems have not been compared to this bound. Novelty remains unestablished.

The local contribution is the explicit source dictionary, sufficient cutoff, and written derivation of the `frame_unique` clause. The displayed proof supplies its own deterministic argument rather than importing a random-noise theorem into Yang–Mills.

## Reproduction and evidence

From the repository root:

```sh
python3 auto-research/general/2026-11-11-T03-frame-uniqueness/check_certificate.py
```

[Receipt](verification.json): Python 3.9.6, standard library, seed `2026111105`, exit zero, 0.468 seconds. [Output](check-output.json) contains:

- Nine exact certificate fixtures at $N=3,4,5$. Three transport layers carry balanced triangular fluxes along different quaternion axes; the layers do not commute and the minimizer has strictly positive score. These are not merely flat zero-energy fixtures.
- Exact symmetry and scalar-row checks. Rational Schur-complement pivots certify positivity of the grounded matrix for $L-\tfrac14L_0$; its constant-block kernel is checked separately. This certifies the stated lower bound on each finite fixture.
- 108 exact comparisons of directly evaluated score differences with $v^TLv/N^2$, together with the quantitative lower bound.
- Twelve ordered-pair symmetrization checks on nonreciprocal arrays without stationarity assumptions.
- Rational verification of the conservative cutoff arithmetic.

The fixture arrays belong to the relaxed quaternion model. We have not constructed them from physical fine fields, and the tests do not certify the general source theorem. They test algebra and finite certificates; the general result remains a written proof depending on the written localization argument of PR #4.

## Handoff and limitations

This resolves the *written sufficient-condition question* for frame uniqueness in fundamental SU(2). It does not establish the chosen history's parameters, arbitrary groups, `axial_exists`, analytic control of branch probabilities, spatial clustering, or the continuum mass gap. It does not strengthen the heat-correlation bound.

Next bounded tasks: formalize this implication against the actual source declarations, or audit `axial_exists` with explicit patch-size dependence. Keep the cutoff hypothesis attached and do not silently replace the existing kernel. For the physical mass gap, probability and retained-field covariance estimates remain necessary. Submit this as a dependent PR without automatic merge; independent review remains open.
