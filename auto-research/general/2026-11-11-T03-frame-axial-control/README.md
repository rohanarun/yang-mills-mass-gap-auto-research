# A patch-size-independent SU(2) minimizing-frame estimate

**Correction, 2026-11-11:** [PR #6](https://github.com/rohanarun/yang-mills-mass-gap-auto-research/pull/6) locates and replays the existing upstream branch producers. Uniform frame uniqueness, predictor uniqueness, and axial eligibility are already supplied upstream. Earlier absence claims are retracted; this PR provides an explicit SU(2) calculation to compare with existing results, not the first proof of uniform frame control or branch existence.

## Metadata and bounded question

- Date / author: 2026-11-11; Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03, T04, T06. Base: `3e4346626680f8ef782d0e2daca99056428d9c7d`.
- Upstream: `yang-mills-group/OpenAI-YM-20261028`, pin `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).
- Outcome: written pointwise control of every minimizing frame on the smooth branch, for fundamental SU(2) and a sufficiently small frame cutoff. A conditional Wilson-loop replacement follows. No spatial estimate or mass gap.
- Evidence: source inspection, written argument, and exact finite quaternion controls. No Lean formalization, full upstream replay, or independent review.
- Question: can the patch-size factor in the [previous frame-comparison sketch](../2026-11-11-T03-spin-j-prediction-mean/README.md) be removed?
- Falsification: an incorrect local-field orientation, inadmissible centre variation, or failed dispersion bound invalidates the proof. Planned computation: standard-library rational arithmetic on small finite arrays, seconds rather than a simulation of the physical measure.

## 1. Statement and source dictionary

Write $d(u,v)=|u-v|$ for Euclidean distance between unit quaternions. In the fundamental representation of SU(2), this equals both the source's normalized Hilbert–Schmidt chord of $uv^{-1}$ and the operator norm of the difference of the fundamental matrices. The source identity is $\mathrm{chord}(g)^2=2\,\mathrm{price}(g)$; see [MatrixGroup.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Gauge/MatrixGroup.lean#L112).

Fix a cover configuration $U$, a patch with $N$ points, its centre $o$, and a route order $l_0$. Set

$$
A_x=\mathrm{axial}(U,(o,l_0),x),\qquad
E_{xy,l}=A_x\,\mathrm{travel}(U,x,\mathrm{route}(x,y,l))\,A_y^{-1}.
$$

Here $A_o=1$ and $E_{xx,l}=1$ by `route_same`. By [Patch.usesMin](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Patch.lean#L108), on the smooth branch every one of these $E_{xy,l}$ satisfies $d(E_{xy,l},1)<\varepsilon$, where $\varepsilon=\mathrm{frame\_cut}$. This is stronger than control of adjacent links only.

**Written theorem.** Assume $0<\varepsilon<1/\sqrt2$ and `usesMin`. For every centre-normalized global minimizer $h$ of `score`, including the source's `selected`,

$$
\max_x d(h_x,A_x)\leq D(\varepsilon),\qquad
D(\varepsilon)=\min\left\{2,\frac{4\varepsilon}{\sqrt{1-2\varepsilon^2}}\right\}.
$$

The bound is independent of $N$, $J$, $L$, the fine configuration, and the chosen route order. Its usefulness still depends on a small cutoff: it may be no better than the trivial bound two. We have not established this cutoff range for the actual selected history. This theorem does not require uniqueness of the minimizer; it does not prove `frame_unique` either. Existence is the compactness statement `min_exists` in the source. Group scope is fundamental SU(2), not arbitrary source `Gauge` inputs.

## 2. Dispersion from the all-pairs score

Put $k_x=h_xA_x^{-1}$, so $k_o=1$, and let $\bar k=N^{-1}\sum_xk_x\in\mathbb R^4$. The transformed score is

$$
S(k)=\mathop{\mathrm{avg}}_{x,y,l}
\left(1-\mathrm{Re}(k_xE_{xy,l}k_y^{-1})\right)
=\frac12\mathop{\mathrm{avg}}_{x,y,l}|k_xE_{xy,l}-k_y|^2.
$$

The competing axial frame has $k_x=1$, hence minimality gives $S(k)\leq S(1)\leq\varepsilon^2/2$. The triangle inequality in the finite $L^2$ average gives

$$
\left(\mathop{\mathrm{avg}}_{x,y}|k_x-k_y|^2\right)^{1/2}
\leq\sqrt{2S(k)}+\varepsilon\leq2\varepsilon.
$$

Since all $k_x$ are unit vectors,

$$
\mathop{\mathrm{avg}}_{x,y}|k_x-k_y|^2=2(1-|\bar k|^2),
\qquad |\bar k|\geq\sqrt{1-2\varepsilon^2}>0.
$$

This controls dispersion but by itself does not pick the centre row uniformly in $N$. The next step uses full minimization rather than discarding all other rows of the score.

## 3. Local optimality, including the pinned centre

Although the admissible frames have $k_o=1$, the score is invariant under common left multiplication: $S(gk)=S(k)$. Any unanchored competitor can be normalized by $k'_x\mapsto(k'_o)^{-1}k'_x$ without changing its score. Thus an anchored global minimizer is also a global minimizer of the unanchored product problem. In particular, a one-coordinate variation is valid at **every** point, including $o$.

Let $m$ be the number of route orders and define the quaternion local field

$$
B_i=\frac1{2m}\sum_{j\ne i,l}
\left(k_jE_{ij,l}^{-1}+k_jE_{ji,l}\right).
$$

Incoming and outgoing terms have both been retained; no symmetry between $E_{ij,l}$ and $E_{ji,l}$ is needed. Terms with $i=j$ are constant. Replacing $k_i$ by a unit quaternion $v$ changes the score by exactly

$$
S(k^{i\to v})-S(k)=-\frac2{N^2}\langle v-k_i,B_i\rangle.
$$

Consequently $B_i=\lambda_i k_i$ for some $\lambda_i\geq0$, including $\lambda_i=0$ if $B_i=0$. Because each transport lies within $\varepsilon$ of one,

$$
B_i=\sum_{j\ne i}k_j+e_i,
\qquad |e_i|\leq(N-1)\varepsilon.
$$

Adding $k_i$ gives

$$
N\bar k+e_i=(\lambda_i+1)k_i.
$$

The coefficient is positive even when the local field vanishes. Thus $k_i$ is the normalization of $\bar k+e_i/N$. For nonzero vectors $a,b$, the elementary estimate

$$
\left|\frac a{|a|}-\frac b{|b|}\right|\leq\frac{2|a-b|}{|b|}
$$

follows by adding and subtracting $a/|b|$ and using the reverse triangle inequality. Applying it with $b=\bar k$ yields

$$
\left|k_i-\frac{\bar k}{|\bar k|}\right|
\leq\frac{2(1-1/N)\varepsilon}{|\bar k|}.
$$

Apply the same estimate to $i=o$, where $k_o=1$, and use the triangle inequality. This proves the stated bound (and the slightly stronger factor $1-1/N$). The case $N=1$ is trivial. This argument works for a larger class of unit-quaternion transport arrays; source consistency imposes further constraints but is not needed for the inequality.

## 4. Consequence for the prediction observable

For an edge whose two endpoint patches are on `usesMin`, replace their selected frames by the fixed centre-based axial frames above. Let $Y_x$ and $Y_x^A$ be the actual and replacement connectors from [Block.connector](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Block.lean#L41). Bi-invariance and the triangle inequality imply

$$
d(Y_x,Y_x^A)\leq2D(\varepsilon).
$$

For spin $j$ put $n=2j\in\mathbb N$. Realizing the representation in the symmetric subspace of the $n$-fold fundamental tensor power and telescoping gives $\|\rho_j(u)-\rho_j(v)\|\leq n\,d(u,v)$. Combine this with the [previous written predictor bound](../2026-11-11-T03-spin-j-prediction-mean/README.md), with $c=\mathrm{predictor\_cut}\leq1$ and the standing source branch hypotheses:

$$
\left\|\mathbb E_{\mathrm{bond\ tag}}\rho_j(\mathrm{predict}(Y))
-\sum_xw_x\rho_j(Y_x^A)\right\|
\leq n^2c+2nD(\varepsilon).
$$

The predictor contribution is zero on fallback and at most $n^2c$ on the active branch. No continuity of its branch indicator has been assumed.

For an edge-distinct fundamental coarse loop $C$ of length $\ell_C$, let $\overline W_C$ be its exact tag-averaged prediction and $W_C^A$ the result of using the linear connector average in the fixed axial frames. On the event $G_C$ that **every endpoint patch of the loop** satisfies `usesMin`, product telescoping gives

$$
|\overline W_C(U)-W_C^A(U)|\leq\ell_C\bigl(c+2D(\varepsilon)\bigr).
$$

On this event the selected frames and their replacements are independent of the unused frame tags. Bond tags are conditionally independent for distinct physical links; reversed traversal uses the adjoint mean. Repeated links need the sector treatment rather than this product formula.

Define $W_C^A$ by the same fixed axial recipe on all configurations. It is a convex combination of traces of closed fine paths, with weights given by products of the fixed convolution weights $w_x$. No branch indicator or minimizing frame occurs in this comparison observable. Winding and repeated fine links are allowed in those paths; this does not establish a uniform finite-spin closure across RG steps.

For any actual fine-field probability $P_1$, boundedness by one gives the conditional reduction

$$
\mathbb E_{P_1}|\overline W_C-W_C^A|
\leq \ell_C\bigl(c+2D(\varepsilon)\bigr)+2P_1(G_C^c).
$$

For two real loop observables the induced covariance replacement error is at most twice the sum of these integrated errors. The probability of the bad event and the covariance of the fine-path observables are **not bounded here**. In particular, fixed positive $c$ and $\varepsilon$ leave an additive error floor independent of separation; this reduction is not exponential clustering.

## Reproduction and limitations

Run from the repository root:

```sh
python3 auto-research/general/2026-11-11-T03-frame-axial-control/check_frame.py
```

[Receipt](verification.json): Python 3.9.6, standard library, seed `2026111104`, exit zero in 0.535 seconds. [Output](check-output.json) records 80 exact local-variation identities (24 at the centre), 24 dispersion cases, 24 arrays with known global minimizers, and five energy-only controls. The arrays test a relaxed finite quaternion problem, **not** actual source fine-field realizations. In the known-minimizer fixtures every energy term is zero; they do not numerically solve the general minimization problem. The general theorem rests on the written proof above.

The [energy-only failure record](../../negative-results/2026-11-11-T03-frame-energy-only/README.md) explains why small average score cannot substitute for local optimality. Standard quaternion algebra, finite averaging, and tensor telescoping are used; no novelty is claimed.

## Handoff

The earlier patch-size-dependent sketch is superseded by this written bound, subject to its explicit small-cutoff assumption. Next bounded work: test whether the localized minimizer set admits a quantitative uniqueness/stability theorem, keeping common gauge freedom and the centre constraint explicit. Alternatively, derive a bound on $P_1(G_C^c)$ under the actual fine law. Neither task alone supplies the spatial covariance estimate or continuum limit. Preserve the original source branch hypotheses until they are actually proved.

Review status: author/assistant derivation and finite controls only; submit through a PR without automatic merge. No independent mathematical review, Lean proof, or mass-gap theorem.

Follow-up, 2026-11-11: the [uniqueness certificate](../2026-11-11-T03-frame-uniqueness/README.md) derives a written sufficient condition `frame_cut <= 1/16` and optimization-error control modulo common gauge rotation from this localization argument. It remains unformalized and independently unreviewed; the actual history's cutoff and the spatial estimate remain open.
