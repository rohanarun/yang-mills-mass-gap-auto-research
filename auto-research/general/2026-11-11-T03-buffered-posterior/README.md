# Buffered conditionals and local hidden predictions

## Metadata and bounded question

- Date / tracks: 2026-11-11; T03-B/C, with T04 and T06.
- Author: Rohan Arun, with OpenAI Codex assistance in the current research chat.
- Base commit: `72f573c274bf0a53717bb4a98f0691908a39bc45`.
- Upstream: `yang-mills-group/OpenAI-YM-20261028`, pinned at `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).
- Evidence: written source-matched probability argument and exact finite controls. No Lean formalization, upstream kernel replay, or independent mathematical review in this result.
- Question: which hidden-field response actually controls a coarse block across an integrated buffer, and what does local noise alone bound?
- Falsification criterion: an incorrect normalization, a dependence on integrated buffer outputs, or a failed exact finite identity invalidates the proposed reduction. The bounded checks require only Python/SymPy and small finite sums.

This refines the [coarse block bound](../2026-11-11-T03-block-conditional-bounds/README.md). For singleton input and output changes it improves the written upper bound from $\tanh\kappa$ to $\tanh^2\kappa$. **Neither bound decays with separation. No Yang–Mills mass gap follows.**

## Exact joint law and an integrated buffer

Fix a selected history, cutoff $N\geq1$, volume $p$, and its step from level 1 to level 0. Write $S$ for the actual step, $v_1$ for its fine density, $\beta_1$ for its coupling, $\lambda$ for the fixed kernel penalty, and $\kappa=\lambda\beta_1>0$. Retain all generated interactions in $v_1$.

Let $Z=(U,t)$ contain the fine configuration and the **joint** site/bond choices. Define

$$
\rho(dU,t)=Z_1^{-1}v_1(U)\,S.\mathrm{likelihood}(U,t)\,d\mu_1(U),
\qquad Q_e(Z)=S.\mathrm{prediction}(U,t)_e.
$$

Here $Z_1=\int v_1\,d\mu_1>0$. The likelihood sums to one; the tags share site frames and are not an unconditional product over bonds. With probability Haar measure $dH$ on each coarse link, put

$$
k_\kappa(v\mid q)=z_\kappa^{-1}
 \exp[-\kappa\,\mathrm{price}(vq^{-1})].
$$

The joint law is

$$
\rho(dZ)\prod_e k_\kappa(V_e\mid Q_e(Z))\,dH(V_e).
$$

Its coarse marginal is the actual normalized $v_0$, by the selected history's exact push identity and mass preservation. Its factors integrate to one. These assertions use [Block.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Block.lean) (`prediction`, `likelihood`, `noise`, `density`, `chosen`, `noise_mass`), [Push.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Push.lean) (`push_integral`), and [History.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/History.lean) (`Transfer`, `Selected`, `partition_eq`). Positivity/integrability follow from the source-matched finite laws audited in the preceding record; no new replay is claimed.

Choose coarse output links $A\subseteq\Lambda$, with buffer $\Lambda\setminus A$, and exterior $O=\Lambda^c$. Condition only on $V_O=\eta$. Integrating every buffer link removes its noise factor. Define the posterior

$$
\pi_\eta(dZ)=
\frac{\prod_{j\in O}k_\kappa(\eta_j\mid Q_j(Z))\rho(dZ)}
{\int\prod_{j\in O}k_\kappa(\eta_j\mid Q_j)\,d\rho}.
$$

All factors are bounded and strictly positive on a finite lattice, so the displayed denominator is finite and positive for every exterior. The canonical buffered conditional is

$$
\gamma_A^\eta=\pi_\eta^A K_A,
\qquad K_A(q_A,dv_A)=\prod_{e\in A}k_\kappa(v_e\mid q_e)dH(v_e),
$$

where $\pi_\eta^A$ is the marginal law of $Q_A$. Fixing the intervening outputs would define a different conditional law.

## Two noise factors, with no spatial rate

Use $\mathrm{TV}(\nu,\nu')=\sup_E|\nu(E)-\nu'(E)|$, with maximum one. Let
$\delta_A=\sup_{q,q'}\mathrm{TV}(K_A(q),K_A(q'))$.
For an output event $E$, the function $K_A(\cdot,E)$ has oscillation at most $\delta_A$. Integrating a bounded function against the difference of two probability laws gives

$$
\mathrm{TV}(\gamma_A^\eta,\gamma_A^\xi)
\leq\delta_A\,\mathrm{TV}(\pi_\eta^A,\pi_\xi^A).
$$

This is the standard Dobrushin contraction argument, not a new theorem; see [Gaubert–Qu, introduction](https://www.cmap.polytechnique.fr/~gaubert/PAPERS/GaubertQuIEOTD14QuFinal.pdf). The preceding record gives the elementary likelihood-ratio/Hilbert comparison: if the log-density ratio has oscillation at most $h$, normalized TV is at most $\tanh(h/4)$.

The source bound $0\leq\mathrm{price}\leq2$ implies an oscillation at most $4\kappa|A|$ between two product output densities. Hence $\delta_A\leq\tanh(\kappa|A|)$. If the exterior changes only on $D\subseteq O$, its posterior likelihood ratio before normalization is

$$
R_D(Z)=\prod_{j\in D}
\frac{k_\kappa(\xi_j\mid Q_j(Z))}{k_\kappa(\eta_j\mid Q_j(Z))}
\in[e^{-2\kappa|D|},e^{2\kappa|D|}].
$$

The same comparison and marginal contraction give

$$
\mathrm{TV}(\gamma_A^\eta,\gamma_A^\xi)
\leq\tanh(\kappa|A|)\tanh(\kappa|D|).
$$

For one changed exterior link and one output link this is $\tanh^2\kappa$. Since the selected history satisfies $\beta_1\leq2\widehat\beta_1$, replacing $\kappa$ by $2\lambda\widehat\beta_1$ gives a bound uniform in $N\geq1$ and $p$ for fixed history and cardinalities. It may be very close to one, and summing it over remote links need not be bounded uniformly in volume. This is a conditional-law influence bound, not a contraction of the physical heat operator.

## The missing local posterior estimate

For a change at a single exterior link $j$, write $R_j$ for its likelihood ratio. For any bounded real output observable $F$,

$$
\gamma_A^\xi(F)-\gamma_A^\eta(F)=
\frac{\mathrm{Cov}_{\pi_\eta}(K_AF,R_j)}{\mathbb E_{\pi_\eta}R_j}.
$$

This follows directly by posterior reweighting. Define

$$
\alpha_\eta(A,j)=
\sup_{E\in\sigma(Q_A),\,B\in\sigma(Q_j)}
|\mathrm{Cov}_{\pi_\eta}(1_E,1_B)|.
$$

For bounded real functions of these respective variables, layer-cake integration gives
$|\mathrm{Cov}(f,g)|\leq\mathrm{osc}(f)\mathrm{osc}(g)\alpha_\eta(A,j)$:
subtract each infimum, represent each nonnegative function by its level sets, and integrate their event covariances. Applying this to output events yields

$$
\mathrm{TV}(\gamma_A^\eta,\gamma_A^\xi)
\leq \delta_A\frac{\mathrm{osc}(R_j)}{\mathbb E_{\pi_\eta}R_j}
\alpha_\eta(A,j)
\leq\tanh(\kappa|A|)(e^{4\kappa}-1)\alpha_\eta(A,j).
$$

The coefficient on the right can be large. The useful target would be an independently derived, distance-dependent bound on the **actual local posterior** coefficient, uniform over the relevant exterior configurations, cutoffs, and volumes. A bound $\alpha_\eta(A,j)\leq C_Ae^{-\mu d(A,j)}$ would control single-link changes. Extending to arbitrary exteriors needs telescoping through intermediate exteriors and uniform shell counting; physical units, transported observables, phase/density, and limit bridges would still be required. An observable-specific covariance estimate may be weaker and more attainable than this full event bound.

Controlling the TV distance between the **entire hidden posteriors** is unnecessarily strong: changing distant data can change its own hidden coordinate even when that coordinate is independent of $Q_A$. The first contraction inequality needs only the $Q_A$ marginal.

## Source audit: localization is not posterior independence

- [Localization.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Extra/MULTISOURCE_TRAJECTORIES/Localization.lean) defines `project` by integrating a dummy exterior against Haar. `project_local` establishes locality of that projection, not independence or small covariances under $\pi_\eta$.
- [KernelReads.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Extra/MULTISOURCE_TRAJECTORIES/KernelReads.lean) records full-route footprints and shared tags. Its `Probability` section at this pin is empty; its header is not a proved conditional-marginal theorem.
- [Service.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Extra/MULTISOURCE_TRAJECTORIES/Service.lean) makes `Offers` an explicitly speculative quantitative hypothesis; `circle` takes it as an assumption. A correspondence from those observables/budgets to the posterior coefficient above is not established here.
- [Marginal.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/AnalyticNext/CONNECTED_LOG_IDENTITY/Marginal.lean) requires a measure-preserving map into a product law in `Keep.block`. Disjoint supports alone do not supply this for the interacting posterior.

These are scoped source observations, not a claim to have excluded every possible upstream estimate.

## Exact controls and reproduction

Run from this repository root:

```sh
python3 auto-research/general/2026-11-11-T03-buffered-posterior/check_posterior.py
```

[Receipt](verification.json): Python 3.9.6, SymPy 1.14.0, exit 0, 0.406 seconds. [Output](posterior-check.json) records symbolic identities and ten exact rational buffered-chain cases.

For two hidden signs with prior $(1+cuv)/4$, $0<c,r<1$, give both the remote observation and local output independent binary noise of bias $r$. Conditioning on remote output $+1$ versus $-1$ gives global hidden TV $r$, local hidden TV $cr$, and output TV $cr^2$. The covariance identity is exact; its event coefficient is $c(1-r^2)/4$. At $c=0$ the local effect vanishes while the global hidden TV remains $r$. As $c\uparrow1$, the output effect approaches $r^2$; extra hidden structure is needed to improve the generic two-channel bound.

For a hidden Markov chain with transition $(1+cuv)/2$ and the same observation noise, explicitly integrating all intervening observations gives endpoint influence $r^2c^L$. The code checks lengths 1 through 5 for two rational parameter pairs. The noise reduces the amplitude; the spatial rate comes from the hidden correlation factor $c^L$.

These are finite probability models, without the Yang–Mills gauge, reconstruction, or phase hypotheses. Symbolic identities do not verify the general written source application.

## Next contribution and review

Derive a bound on $\mathrm{Cov}_{\pi_\eta}(K_AF,R_j)$ from actual fine-field/tag estimates across a buffer, retaining all generated interactions. First attempt an observable-specific bound and list its exterior/scale quantifiers. Success means obtaining spatial smallness from Yang–Mills input, rather than assuming it or proving another abstract implication. The [external 3D audit](../2026-11-11-T03-ym3d-transfer-audit/README.md) supplies useful finite checks but no such posterior estimate.

Review status: author/assistant checks only, 2026-11-11. Independent review and formalization remain open. The [agent prompt](../../../auto-research.md) now requires local posterior response and distinguishes Haar localization from conditional mixing.
