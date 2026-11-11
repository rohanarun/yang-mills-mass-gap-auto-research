# Fundamental SU(2) predictor average with cutoff-preserving truncation

## Metadata and bounded question

- Date / author: 2026-11-11; Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03-B/C; T04 and T06.
- Base: `3699c4d41ed1bbd95d719976651bd75b979e8c18`.
- Upstream pin: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).
- Publication: branch `research/su2-predictor-average`, submitted for PR review; no direct push to main or automatic merge.
- Outcome: written exact bond-tag average for fundamental SU(2), a uniform approximation bound, and a conditional geometric truncation bound. No spatial covariance decay or mass gap.
- Evidence: source inspection, written quaternion/matrix arguments, and exact rational controls. No Lean proof, upstream replay, or independent mathematical review.
- Question: can the averaged prediction observable in the [one-step loop formula](../2026-11-11-T03-loop-noise-transfer/README.md) be represented more explicitly while retaining the actual branch choices?
- Falsification: incorrect normalization, removal of a cutoff mask, or an unproved lower bound on the mean's norm invalidates the proposed expansion. Checks use finite rational arithmetic and no new dependencies.

## 1. Exact minimizing predictor

Specialize to SU(2) in its two-dimensional fundamental representation and identify its elements with unit quaternions. For a fixed connector family $Y_x$, the source weights satisfy $w_x\geq0$ and $\sum_xw_x=1$. Write

$$
M=\sum_xw_xY_x,\qquad r=|M|\in[0,1],
\qquad c=\mathrm{predictor\_cut}>0.
$$

Quaternion norm equals matrix operator norm in this representation. Since the source price is $1-\tfrac12\mathrm{Re}\,\mathrm{Tr}(g)$, its predictor objective is

$$
\mathrm{bondCost}(Y,u)=1-\langle M,u\rangle_{\mathbb R^4},\qquad |u|=1.
$$

Cauchy–Schwarz shows the minimum is $1-r$. When $r>0$, the unique minimizer is $M/r$. If $r=0$, every unit quaternion minimizes. Under the source `Branches.predictor_unique` obligation, the minimizing branch therefore cannot be active at $r=0$.

The relevant definitions are [Patch.lean, `weight`, `bondCost`, `best`, `usesBest`, `predict`, and `predictorMass`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Patch.lean), with the price convention in [MatrixGroup.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Gauge/MatrixGroup.lean#L112).

On the minimizing branch every bond tag predicts the same minimizer and its tag masses sum to one. On fallback, the prediction is $Y_x$ with mass $w_x$. Thus the **exact bond-tag mean**, conditional on the fine field and site tags, is

$$
A_c(M)=
\begin{cases}
M/r,&1-r<c,\\
M,&1-r\geq c.
\end{cases}
$$

The first case is only used where $r>0$, as above. Equality belongs to fallback because the source test is strict. Both branches have norm at most one, and

$$
\|A_c(M)-M\|=(1-r)1_{\{1-r<c\}}\leq c.
$$

This identifies the nonlinearity explicitly. It does not replace the predictor by an unnormalized connector mean.

## 2. Exact loop expression after summing bond tags

For an edge-distinct coarse loop $C$, retain the full joint site tags $s$ and their source probability
$p_U(s)=\prod_x\mathrm{frameMass}(U,s_x)$.
For each oriented positive link $e$, form its connector mean $M_e(U,s)$ and set $A_e=A_c(M_e)$. Independence of bond tags **conditional on $U,s$** gives

$$
\overline W_C(U)=
\sum_s p_U(s)\,\frac12\mathrm{Tr}
\left(\prod_{e\in C} A_e^{[\epsilon_e]}\right),
\qquad A^{[+1]}=A,\quad A^{[-1]}=A^*.
$$

For reverse traversal, expectation commutes with adjoint; one must not invert the mean matrix, which may be singular. The product is in path order, with noncommuting factors retained. [Block.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Block.lean) supplies the likelihood factorization and `chosen`; [Measurable.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Measurable.lean) supplies the site/bond normalization identities.

Replacing $A_e$ by $M_e$ defines a connector-mean observable $W_C^{(0)}$, with the same site frames and probabilities. A telescoping matrix-product identity, operator norms at most one, and $|\mathrm{Tr}(B)|/2\leq\|B\|$ give

$$
\|\overline W_C-W_C^{(0)}\|_\infty\leq\ell_C c.
$$

The same proof permits the smaller, configuration-dependent bound obtained by averaging $\sum_{e\in C}(1-r_e)1_{\{1-r_e<c\}}$ over site tags. Neither version gives separation decay. Site frames, their configuration-dependent masses, and the full fine-field law remain in the observable.

## 3. A controlled truncation under an explicit extra hypothesis

**Assume additionally $0<c<1$ for the fixed kernel being studied.** The inspected `KernelChoices` definition requires positivity only; this result has not established that its chosen cutoff is below one. Changing the cutoff would change the kernel and is not a proof about the same fixed history.

On the minimizing branch, $r>1-c>0$. Put

$$
\delta=1-r^2,\quad q=2c-c^2<1,\quad
b_n=\binom{2n}{n}4^{-n}.
$$

The standard [binomial expansion, DLMF 4.6.7](https://dlmf.nist.gov/4.6.E7) yields

$$
\frac Mr=M\sum_{n=0}^\infty b_n\delta^n.
$$

Define $A_{c,K}(M)$ by using the sum through $K$ on the minimizing branch and $M$ on fallback. **The original branch mask remains in this definition.** Since $0<b_n\leq1$ and $0\leq\delta<q$, the partial sum is a positive scalar multiple of $M$ with norm at most one. Its error satisfies

$$
\|A_c-A_{c,K}\|
\leq r\sum_{n=K+1}^\infty\delta^n
=\frac{\delta^{K+1}}r
\leq\frac{q^{K+1}}{1-c}.
$$

The error is zero on fallback. The corresponding site-tag-averaged loop $W_{C,K}$ therefore satisfies

$$
\|\overline W_C-W_{C,K}\|_\infty
\leq\ell_C\frac{q^{K+1}}{1-c}.
$$

This is uniform over fine configurations, tag assignments, and lattice volume at fixed $c$ and loop length. On a specified branch, each bond expression is a polynomial of degree at most $2K+1$ in connector quaternion coordinates. Globally it is **a polynomial expression multiplied by a cutoff mask**; the source frame choices and their masses are still present. It is not a finite Wilson-loop expansion with configuration-independent coefficients.

For real loop observables of norm at most one, Cauchy–Schwarz for covariance gives

$$
\left|\mathrm{Cov}_{P_1}(\overline W_C,\overline W_D)
-\mathrm{Cov}_{P_1}(W_{C,K},W_{D,K})\right|
\leq(\ell_C+\ell_D)\frac{q^{K+1}}{1-c}.
$$

Indeed, subtract the two covariances as $\mathrm{Cov}(\overline W_C-W_{C,K},\overline W_D)+\mathrm{Cov}(W_{C,K},\overline W_D-W_{D,K})$ and bound each by the product of the sup norms. Combining with the earlier vertex-disjoint loop identity supplies an explicit truncation error multiplied by the known noise factor $a^{\ell_C+\ell_D}$. The covariance of the truncated observables is still unbounded spatially.

## 4. Why the mask and lower bound cannot be omitted

For the radial moment $M=rI$ and $0<c<1$, the mean equals $rI$ for $r\leq1-c$ and $I$ for $r>1-c$. The one-sided jump at the threshold has norm $c$. No continuous function on a neighborhood crossing this boundary can approximate this moment map uniformly with error below $c/2$: continuity and the triangle inequality would have to bridge two limits separated by $c$.

This is a statement about the predictor moment map. It does not prove that every actual selected fine-field family realizes a transverse crossing, nor that subsequent site-tag or field integration cannot smooth a particular quantity. It does show why discarding a mask and claiming uniform polynomial approximation needs an additional argument. A fixed two-connector family $Y_\pm=(r,\pm\sqrt{1-r^2},0,0)$ with equal weights realizes this radial moment, but those are illustrative weights, not an identification with the source convolution weights.

Uniqueness on the active branch ensures $r>0$, not a uniform gap from zero. At $c=1$, the active branch includes arbitrarily small positive radial moments in this control, and every fixed polynomial truncation has error approaching one as $r\downarrow0$. A uniform geometric estimate therefore needs a proved positive margin, such as the additional $c<1$ hypothesis above.

## Verification and reproducibility

From this repository root:

```sh
python3 auto-research/general/2026-11-11-T03-predictor-average/check_predictor.py
```

[Receipt](verification.json): Python 3.9.6, standard library, exit 0, 0.044 seconds. [Output](check-output.json) records 378 rational scalar truncation checks and three noncommuting loop cases, each summing 16 bond-tag configurations exactly. The fixtures include selected and fallback edges, inverse traversal via quaternion conjugation, and truncations through several degrees. A radial sequence checks the strict-threshold jump. Candidate minimizers are checked against selected finite competitors; the general minimization theorem is the written Cauchy–Schwarz argument, not established by a finite search.

These controls test algebra and finite instances. They do not check the whole source construction, supply actual fine-field samples, or establish a spatial covariance bound. The supporting [failure record](../../negative-results/2026-11-11-T03-predictor-threshold/README.md) preserves the rejected mask-free and uniqueness-only shortcuts.

## Next bounded task and review

First identify a cutoff margin for the exact fixed history, or use a proved probability-weighted estimate near small $r$. Then seek a covariance bound for the masked truncated observables, including the source frame selectors, all read supports, and degree-dependent costs. Choosing a large truncation degree controls approximation error but does not prove clustering of the retained terms. The continuum, phase, dense-family, and physical-time bridges remain open.

Review status: author/assistant derivation and finite checks only; submitted for PR review. No new Yang–Mills decay estimate, mathematical novelty, or mass-gap proof is claimed.
