# Coarse block conditional laws: a uniform noise bound and the missing spatial estimate

## Metadata and question

- Date: 2026-11-11. Rohan Arun, with OpenAI Codex assistance.
- Tasks: T03-B, T03-D; related tracks T04 and T06.
- Outcome: written source-matched finite-block conditional bound, uniform in cutoff and volume for a fixed block size and selected history. It has no decay in separation and does not establish a mass gap.
- Evidence: source inspection and written derivations; exact symbolic/rational controls. No new Lean proof, upstream kernel replay, or independent review.
- Repository base: `2c86f4fca925a7c64973e6573059329e446af56a`; upstream: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`. [Source hashes](provenance.json).
- Related: [terminal covariance](../2026-11-11-T03-terminal-covariance/README.md), [normalization and latent-field controls](../../negative-results/2026-11-11-T03-conditional-normalization/README.md).

Can the actual coarse density supply a quantitative conditional-law estimate? The bounded task is to derive that law and distinguish a uniform finite-block bound from spatial mixing. The falsification tests are normalization cancellation and survival of a shared latent correlation under local noise. Computation is limited to small exact finite-state models.

## Conditional law of the actual representation

Fix a selected history, $N\geq1$, volume index $p$, and a finite set $B$ of coarse **link variables**, with $s=|B|\geq1$. Let $\eta$ denote all exterior links, $\mu_B$ product probability Haar on the links of $B$, and

$$
v(V)=(H.\mathrm{rep}\ N\ p\ 0).\mathrm{eval}(V).
$$

[`Signals.vac_pos`, `vac_smooth`, and `vac_eq`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Extra/MULTISOURCE_TRAJECTORIES/Signals.lean#L96) identify this with a positive continuous vacuum density on the compact finite configuration space. The conditional law is therefore well defined for every exterior configuration:

$$
\gamma_B(du\mid\eta)=\frac{v(u,\eta)\,d\mu_B(u)}{Z_B(\eta)},\qquad
Z_B(\eta)=\int v(w,\eta)\,d\mu_B(w)>0.
$$

This is a written application of finite product-measure disintegration; the exact upstream application has not been formally replayed. Positivity and compactness give finite-cutoff bounds, not by themselves uniform constants in the limits.

Write the source's [`Rep.eval`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/History.lean#L177) as

$$
v(V)=e^{c-S(V)-E(V)}G(V),\qquad
S=R.\mathrm{path.inChannels},\quad E=R.\mathrm{activities.additive},\quad G=R.\mathrm{activities.gas}.
$$

The selected positive density implies $G>0$ pointwise here; `Activities.Valid` alone is not being asserted to prove that positivity. Define $F=-S-E+\log G$. For two exteriors $\eta,\xi$, the useful quantity is

$$
\delta_B(\eta,\xi)=\sup_{u,w}\left|F(u,\eta)-F(u,\xi)-F(w,\eta)+F(w,\xi)\right|.
$$

The scalar $c$ and the conditional partition functions cancel in this double difference. Any term independent of the interior, or independent of the changed exterior links, cancels too. A bound on the entire extensive action misses this cancellation.

## From log-density oscillation to a conditional bound

With total variation defined as $\|P-Q\|_{\rm TV}=\sup_A|P(A)-Q(A)|$, one has

$$
\boxed{\|\gamma_B(\cdot\mid\eta)-\gamma_B(\cdot\mid\xi)\|_{\rm TV}
\leq\tanh\!\left(\frac{\delta_B(\eta,\xi)}4\right).}
$$

This is a standard Hilbert-metric comparison; see [Cohen–Fausti, Corollary 5.2.1](https://arxiv.org/html/2309.02413v2#S5.SS2). Their total-variation norm is twice the convention used here. No novelty is claimed.

For completeness, let $r=v(u,\eta)/v(u,\xi)$, $Q=\gamma_B(\cdot\mid\xi)$ and $t=\mathbb E_Qr$. If $0<a\leq r\leq b$, convexity of $|r-t|$ gives

$$
\|P-Q\|_{\rm TV}=\frac{\mathbb E_Q|r-t|}{2t}
\leq\frac{(b-t)(t-a)}{t(b-a)}
\leq\frac{\sqrt b-\sqrt a}{\sqrt b+\sqrt a}.
$$

The last difference is $(t-\sqrt{ab})^2/[t(b-a)]\geq0$. If $a=b$, the laws coincide. Taking infimum/supremum of the positive ratio gives $\log(b/a)=\delta_B$ and the displayed hyperbolic tangent. The ratio is continuous on a compact space at each fixed cutoff/exterior pair. The algebraic identity is checked in the accompanying script; the measure argument is written.

## A source-derived uniform bound from the noise kernel

There is a concrete bound available without estimating the logarithm of the gas separately. At the step from level one to zero, let

$$
\lambda=H.\mathrm{levels.clock.kernel.penalty}>0,\quad
\beta_1=H.\beta(N,p,1)>0,\quad \kappa=\lambda\beta_1.
$$

[`StepData.noise`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Block.lean#L68) is a product over coarse links of

$$
z_\kappa^{-1}\exp[-\kappa\,\mathrm{price}(V_eQ_e^{-1})].
$$

[`Gauge.price_range`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Gauge/MatrixGroup.lean#L141) gives $0\leq\mathrm{price}\leq2$. For configurations $V,W$ equal outside $B$, each changed factor has ratio between $e^{-2\kappa}$ and $e^{2\kappa}$, hence

$$
e^{-2\kappa s}\,\mathrm{noise}(Q,W)\leq\mathrm{noise}(Q,V)
\leq e^{2\kappa s}\,\mathrm{noise}(Q,W).
$$

The same inequalities survive the nonnegative sum over branch likelihoods and integration against the positive fine vacuum. `Selected.steps` therefore gives

$$
e^{-2\kappa s}\leq\frac{v(u,\eta)}{v(w,\eta)}\leq e^{2\kappa s}.
$$

Subtract the corresponding logarithmic relations for $\eta$ and $\xi$ to obtain $\delta_B(\eta,\xi)\leq4\kappa s$. Applying the comparison above yields

$$
\|\gamma_B(\cdot\mid\eta)-\gamma_B(\cdot\mid\xi)\|_{\rm TV}
\leq\tanh(\lambda\beta_1s).
$$

The band's upper bound in [`History.Conv`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/History.lean#L213), supplied by `Selected.represents` at level one, gives $\beta_1\leq2\widehat\beta_1$. Thus for this fixed history and block cardinality, all $N\geq1$, all $p$, and every pair of exteriors,

$$
\boxed{\|\gamma_{B,N,p}(\cdot\mid\eta)-\gamma_{B,N,p}(\cdot\mid\xi)\|_{\rm TV}
\leq\tanh(2\lambda\widehat\beta_1s)<1.}
$$

This written bound is uniform in cutoff and volume but **does not decay with the distance of the changed boundary**. It also deteriorates with block cardinality. It is not an operator-norm contraction of the physical heat semigroup, and does not supply a summable matrix of spatial influences. The [latent-variable control](../../negative-results/2026-11-11-T03-conditional-normalization/README.md) shows why independent local smoothing can satisfy such a bound while correlations survive at arbitrary separation.

## What would turn this into spatial control?

If $F$ had an absolutely summable local expansion $F=\sum_X\Phi_X$ with the full read supports, and $D$ were the changed exterior links, then only terms meeting both $B$ and $D$ would survive the double difference. In particular,

$$
\delta_B(\eta,\xi)\leq4\sum_{X:\,X\cap B\ne\varnothing,\ X\cap D\ne\varnothing}\|\Phi_X\|_\infty.
$$

Here $X$ denotes actual link read sets, after converting the source's site supports and flag halos. A crossing budget bounded by $\Gamma e^{-\rho d(B,D)}$ would give conditional TV at most $\tanh(\Gamma e^{-\rho d})\leq\Gamma e^{-\rho d}$. This is conditional algebra, not a supplied expansion or budget for the actual $\log G$. Even such a far-boundary estimate needs a valid block influence/smallness argument: short-range interactions can propagate correlations through intermediate blocks.

Two support facts should be retained when looking for that budget. [`UsesFinal.allReads`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Masks.lean#L108) uses the enlarged `inspected` support, not only the activity's nominal support. Also [`PathData.kept`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/PathActions.lean#L210) tests become automatic for face bases with

$$
\mathrm{separation}(x,p.1)\geq c.\mathrm{relaxation}\,\log(2/\theta),\qquad \theta=R.p.\mathrm{threshold}>0,
$$

because the group chord is at most two. Thus this flag test has a finite face-read radius at a fixed stage, with the face footprint added for actual links. The remaining path arrays can have longer supports. Their exponential length budgets do not by themselves bound the fully normalized conditional law. Mask indicators also prevent assuming global differentiability term by term, even though the total selected vacuum has a smooth representation.

## Verification and next step

Run from the repository root:

```sh
python3 auto-research/general/2026-11-11-T03-block-conditional-bounds/check_conditionals.py
```

[Output](conditional-check.json) and [receipt](verification.json) record Python 3.9.6, SymPy 1.14.0, exit zero, and 0.528 seconds. The script verifies the optimization identity, exact normalization in the flagged-sector control, and a latent-noise model symbolically and by nine rational enumerations. It does not execute the general Yang–Mills inequalities above. No formal or independent mathematical review is claimed.

Next: derive a relative crossing estimate for the actual block marginal, or integrate/average exceptional flagged sectors with a proved probability bound. For the noise representation, this means controlling how the conditional distribution of the hidden fine field and branch choices changes with distant coarse data. Preserve the terminal covariance and transported insertions. An absolute activity estimate alone, or the uniform finite-block bound just derived, is not enough.
