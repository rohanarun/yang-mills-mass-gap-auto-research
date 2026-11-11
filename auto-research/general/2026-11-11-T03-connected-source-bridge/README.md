# Connected-source audit: a separation estimate and the missing retained covariance

## Metadata and outcome

- Date: 2026-11-11. Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03, T02, T04, T06, T07.
- Outcome: conditional exponential bound for intermediate coefficients; identification of an unresolved physical-correlation bridge. **No Yang–Mills mass gap is proved.**
- Evidence: selective source inspection, written application to cluster budgets, and author-run Lean trust-zero check of the abstract series estimate. No independent review or upstream replay.
- Base repository commit: `1fac2ea99ebdfe40ca8c2a51d42b522d9f54e77b`; upstream commit: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).
- [Formal source](CoverDecay.lean), [log](CoverDecay.log), [receipt](verification.json). These are standard analytic steps; no novelty claim.

## Bounded question

The [previous audit](../../negative-results/2026-11-11-T03-auxiliary-resolvent-gap/README.md) showed that local fluctuation covariance gaps do not control retained modes. Can the upstream connected-source expansion instead yield exponential decay for the physical connected correlation? This investigation separates three tasks: geometric decay of coefficient sums, identification with a normalized correlation, and preservation of a positive physical rate.

## What the source supplies

| Source | Inspected statement | Scope |
| --- | --- | --- |
| [`Lattice.Support.covers`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Lattice/Support.lean#L52) | The union of covering balls must be connected | `coverNumber` charges connecting geometry, not just the number of disconnected support points |
| [`Corona.extent`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Corona/Fit.lean#L84) | $d(x,y)\leq (4B+2)N_B(X)+2B$ when $x,y\in X$ | Actual periodic lattice separation and connected covering number |
| [`Ac.Hit`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Ac/Tree.lean#L12) | At each site, a summable nonnegative budget for $b_i e^{aN_B(X_i)}$ over incident labels | Explicit hypothesis on coefficient majorants |
| [`Price.logWeighed`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/AnalyticNext/CONNECTED_LOG_IDENTITY/Prices.lean#L41) | Transfers a `Ready` budget to logarithmic cluster prices | It does not derive the underlying physical coefficient estimates |
| [`Layer.logs`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Extra/MULTISOURCE_BOUNDS/Layers.lean#L78) | Produces a marked coefficient budget at exponent $a$ from exponent $a+2$, regularity and a smallness condition | Coefficients remain functions of the retained configuration; the returned `Pool` contains `Hit` |
| [`Emit.recovers`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/AnalyticNext/CONNECTED_LOG_IDENTITY/Emitter.lean#L223) | Exact formula for an unnormalized vacuum density evaluated at fixed $V$ | Its right side still includes the reference action and a gas; it is not a normalized log partition function |
| [`Insertions.ratios` and `cumulant`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Extra/MULTISOURCE_TRAJECTORIES/Signals.lean#L139) | Joint marker coefficients divided by the same positive vacuum density, followed by a square-zero-marker logarithm | Normalization is pointwise at the retained field, explicitly not by the partition function |

The intro to `MULTISOURCE_BOUNDS/LogTerms.lean` explicitly separates its coefficient estimates from a formal-to-analytic logarithm identity. `Layer.logs` assumes $a\geq0$; a **strictly positive** unused exponent is needed for exponential decay. Its smallness condition is $8(2B+1)^4\gamma\leq1$, and the output budget includes derivative/translation costs. Those hypotheses must be obtained for the same application, not selected independently.

## Extracting the separation rate

Fix lattice points $x,y$ at separation $d$, a scale $B\geq0$, and an exponent $a\geq0$. Suppose coefficients $c_i$ have supports $X_i$ containing both points and

$$
\sum_i |c_i|e^{aN_B(X_i)}\leq\Gamma,
$$

with a convergent nonnegative series. `Ac.Hit` at $x$, restricted to these labels and combined with a suitable majorant, supplies such a budget when its hypotheses hold. The covering inequality gives

$$
-aN_B(X_i)\leq\frac{a(2B-d)}{4B+2}.
$$

Multiply each weighted term by this common upper bound for its removed exponential. Absolute convergence and the triangle inequality yield

$$
\boxed{\left|\sum_i c_i\right|\leq
\Gamma\exp\left(\frac{2Ba}{4B+2}\right)
\exp\left(-\frac{a}{4B+2}d\right).}
$$

The theorem `decay_of_cover_budget` checks this complete series comparison, including absolute convergence, for complex coefficients on an arbitrary index type. It assumes the budget and geometry explicitly. No upstream modules are imported by the proof file.

For the marked `Layer.logs` output, the budget is on `duty w names * g`, not directly on the unweighted coefficient. Restrict to labels with exactly the two distinct names $\{\alpha,\beta\}$ and require $w_\alpha w_\beta>0$. If the corresponding source anchors $x,y$ belong to every nonzero coefficient's full support and the coefficient is dominated by $g_i$, the bound above applies with $\Gamma/(w_\alpha w_\beta)$. These incidence and normalization conditions are additional: the bare `Layer` structure does not put named anchors into supports. Do not divide by zero weights or silently discard other marker weights. Zero coefficients can be removed from the index set.

This gives separation dependence for the **specified coefficient sum**. It does not identify that sum with a physical connected correlation. The nonzero exponent and all majorants remain explicit prerequisites.

## Why this has not closed the gap

`Emit.recovers` reconstructs a density at a fixed retained configuration, retaining the reference factor `exp (-R.inChannels ... V)` and the remaining gas. It has no source parameters or conclusion about the logarithm of the fully integrated partition function. The marked coefficient theorems inspected here also leave their values as functions of the retained configuration. Other source files may supply parts of the integration bridge; this selective audit does not claim an exhaustive absence theorem.

For a positive source-deformed retained density $\rho_{s,t}$, write $L=\log\rho$ and $Z=\int\rho\,d\mu$. With differentiation under integration justified,

$$
\partial_s\partial_t\log Z\big|_0
=\mathbb E[L_{st}]+\mathrm{Cov}(L_s,L_t).
$$

Bounding the first term by exponentially small mixed coefficients is insufficient without a bound on the second term. This formula describes the required additional step; it does not assert that the inspected unmarked theorem already constructs such a source deformation. The [exact local Ising-chain control](../../negative-results/2026-11-11-T03-log-integration-order/README.md) has $L_{st}=0$ at every configuration while its endpoint connected correlation is $(\tanh J)^R$. It verifies why the missing term cannot be erased by local coefficient bounds.

One possible route is a weighted expansion for the **fully integrated** log partition function, with exact source identification and enough exponent reserve after all mergers. Another is a quantitative mixing theorem for the retained measure controlling the covariance above. Neither has been derived here for the Yang–Mills hierarchy.

## Matching the missing term to the actual trajectory definitions

Further inspection makes the boundary explicit without needing an analytic logarithm. At a fixed cutoff, volume, and level $j\leq N$, use `Signals.lean`'s actual total marker coefficients $T_s(U)$ and positive vacuum density $v_j(U)$. For an allowed pair of distinct markers $\alpha,\beta$, set

$$
r_s(U)=T_s(U)/v_j(U),\qquad
dP_j(U)=\frac{v_j(U)}{Z_j}\,d\mu_{\mathrm{prior}}(U),\quad
Z_j=\int v_j\,d\mu_{\mathrm{prior}}.
$$

Assume $0<Z_j<\infty$ and integrability of the coefficients and products used below. `vac_eq` identifies the vacuum density with `H.rep N p j` for a selected history. `ratios` is exactly $r_s$, including all of the source's `Ride.bump` physical-dimension factors in $T_s$; those factors must not be dropped. `compound_eq` says the marker exponential of the source's `cumulant` is `ratios`.

For two commuting square-zero markers the pair coefficient of that exponential is $c_{\alpha\beta}+c_\alpha c_\beta$. Its singleton coefficients are $c_\alpha=r_\alpha$ and $c_\beta=r_\beta$. Hence the same source-defined conditional cumulant satisfies

$$
c_{\alpha\beta}(U)=r_{\alpha\beta}(U)-r_\alpha(U)r_\beta(U).
$$

The connected coefficient of the integrated, normalized moments at this level is therefore exactly

$$
\underbrace{\mathbb E_j[r_{\alpha\beta}]
-\mathbb E_j[r_\alpha]\mathbb E_j[r_\beta]}_{\text{integrated connected coefficient}}
=\mathbb E_j[c_{\alpha\beta}]
+\mathrm{Cov}_j(r_\alpha,r_\beta).
$$

For complex coefficients this is the **bilinear** covariance, with no conjugation; a reflected or adjoint observable must be inserted explicitly when required for a physical Hilbert-space correlation. The identity follows by adding and subtracting $\mathbb E_j[r_\alpha r_\beta]$. It preserves the same retained measure and source normalizations. It is a written source-matched identity, not a Lean check of the trajectory modules or a completed limiting/reconstruction argument.

Thus the concrete remaining quantity is $\mathrm{Cov}_{P_j}(T_\alpha/v_j,T_\beta/v_j)$ for the actual selected history, uniformly in the required cutoffs and volumes. A valid exponential estimate for $c_{\alpha\beta}$ bounds only the first term. Cauchy–Schwarz alone bounds the covariance by variances and adds no separation dependence. The chain control demonstrates why a separate estimate is necessary.

## Physical scales and a discriminating target

At lattice spacing $\ell$, a separation $d$ in lattice steps corresponds to $D=\ell d$. The candidate coefficient rate in physical units is

$$
\kappa=\frac{a}{\ell(4B+2)}.
$$

At a blocked level use that level's physical spacing. In a direct correlation-limit argument, both the prefactor, including source-normalization costs, and a common positive lower bound for $\kappa$ must be controlled. A support-first argument could relax original prefactor bounds only after the actual positive spectral measures and their convergence have been identified; no such identification is supplied by this coefficient calculation.

`SOURCE_HISTORIES/Reserve.lean` defines $L^{-2/5}$ as numerical local-error currency. It is not a physical correlation rate. Even if a proposed argument converted those factors into multiplicative contractions, a product $\prod_jL_j^{-2/5}$ is only a power of the accumulated length ratio. The linked negative result checks this algebra and explains its limited scope.

The next bounded target is an estimate for this retained covariance of the actual normalized one-marker ratios, or an expansion of the fully integrated logarithm that bounds it together with the conditional term. Also check that the priced localized coefficients sum to the same source-defined $c_{\alpha\beta}$ and that source anchors remain in their charged supports. Success must go beyond a small local correction or per-block error.

## Reproduction and review

Using the recorded Lean 4.32.0 runtime and the existing pinned Lake project, from `auto-research/general/2026-11-11-T02-uniform-projection-criterion/lean`:

```sh
lake env lean --trust=0 -j1 -R ../../2026-11-11-T03-connected-source-bridge ../../2026-11-11-T03-connected-source-bridge/CoverDecay.lean
```

The run exited zero in 21.243 seconds without warnings. Axioms: `propext`, `Classical.choice`, `Quot.sound`. The receipt records the final source/output hashes and dependency revisions; the earlier prerequisite build is identified separately. The code checks the abstract series estimate only. The source application, marking/incidence conditions, covariance identity, and physical reconstruction remain written or open as specified above. No independent review is recorded.
