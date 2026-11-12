# Curvature (Bakry–Émery) methods reach only the strong-coupling regime the notebook already excludes

## Metadata

- Result ID and date: `2026-11-12-T03-bakry-emery-scope`; 2026-11-12.
- Author: Rohan Arun, with Claude (Anthropic) assistance in a Claude Code session.
- Tracks: T03-D primary (a different mechanism); T04 and T06 related.
- Outcome: **negative / scope result.** The natural geometric route (Ricci curvature of the link manifold plus the Hessian of the Wilson action) reproduces the known strong-coupling threshold and stops there. It does not reach the coarse endpoint of the selected history, let alone the running continuum family. No mass-gap estimate.
- Evidence: written derivation (standard Bakry–Émery argument) and floating-point numerical observation on small tori. No Lean proof, no upstream replay, no independent review.
- Repository base commit: `3e43466` (main after PR #2). Toolchain: Python 3.9.6, numpy 2.0.2.
- Related: [strong-coupling scope](../2026-11-11-T04-strong-coupling-scope/README.md), [single-link influence obstruction](../2026-11-11-T03-single-link-influence/README.md).

## Question and exact claim

Question: does a geometric (curvature) criterion give a volume-uniform estimate for the bare SU(2) Wilson law in a range of couplings that includes the couplings the selected history actually uses?

Setting: SU(2) as unit quaternions, weight $\exp(-\beta\sum_p\mathrm{price}(U_p))$ with $\mathrm{price}(q)=1-\mathrm{Re}\,q$ (the repository convention, once per plaquette), each link carrying the round unit $S^3$ with $\mathrm{Ric}=2$, periodic lattice in dimension $d$.

Claim A (written). If $\mathrm{Ric}+\beta\,\mathrm{Hess}\sum_p\mathrm{price}\geq\rho>0$ everywhere, the Bakry–Émery criterion gives a Poincaré inequality with constant $\rho$ for this measure, independent of the volume. For the Hessian, $\rho\geq2-8(d-1)\beta$, so the criterion holds for $\beta<1/[4(d-1)]$.

Claim B (numerical). The analytic Hessian bound $8(d-1)$ is not far from the truth: sampled configurations and a local search find $-\lambda_{\min}$ about $9.2$ ($d=3$, bound 16) and $8.9$ ($d=4$, bound 24). Those are lower bounds on the true supremum, not a proof of a better threshold.

Falsification: a wrong Hessian formula, a wrong Ricci constant, or a coupling-convention mismatch.

## Derivation

**Hessian.** For one plaquette $f=\mathrm{Re}(U_1U_2U_3^{-1}U_4^{-1})$ and tangent vectors $\xi_a\in\mathrm{Im}\,\mathbb H$ at its four links, along $U_a\exp(t\xi_a)$: the diagonal term for link $a$ is $-\mathrm{Re}(U_p)|\xi_a|^2$, and each mixed term is $\mathrm{Re}(P\xi_aQ\xi_bR)$ with $P,Q,R$ unit quaternions, so it has modulus at most $|\xi_a||\xi_b|$. Hence $|\mathrm{Hess}\,\mathrm{price}_p(\xi,\xi)|\leq(\sum_a|\xi_a|)^2\leq4\sum_a|\xi_a|^2$. Each link lies in $2(d-1)$ plaquettes, so $\mathrm{Hess}(\beta\sum_p\mathrm{price})\geq-8(d-1)\beta$.

**Threshold.** $2-8(d-1)\beta>0\iff\beta<1/[4(d-1)]$, which is $1/12$ in $d=4$.

**Cross-check against the literature record.** The notebook's [strong-coupling comparison](../2026-11-11-T04-strong-coupling-scope/README.md) records the cited stochastic-analysis result's condition $\beta_{\rm paper}<1/[16(d-1)]$ and the coefficient map $\beta_{\rm repo}=N^2\beta_{\rm paper}$. For $N=2$ that is $\beta_{\rm repo}<1/[4(d-1)]$, identical to the threshold above for every $d$. This agreement of coefficients supports both the coupling-convention comparison and the Hessian constant; it does not show the two arguments coincide, and the cited paper's proofs were not reproduced.

## Why the route stops

1. **Wrong regime for the endpoint.** The notebook's single-link record reads from `History.Selected` (`starts`, `reaches`) that the $N=0$ coarse endpoint is exactly bare at $\beta=\mathrm{bar}>1$. The `starts` and `reaches` clauses were re-read in the source this session; the value $\mathrm{bar}>1$ is inherited from that record and was not re-derived. Since $\mathrm{bar}>1>1/12$, even the simplest coarse measure is outside the proved range; the numerical hint $\beta\lesssim0.2$ does not close the gap.
2. **Wrong regime along the family.** The running-coupling requirement forces the fine-cutoff couplings to infinity (notebook's strong-coupling record).
3. **The generated measures are not Wilson.** For $N\geq1$ the coarse law carries generated interactions, so even an improved Wilson threshold would need a Hessian bound for those, which does not exist in the record.
4. **What the criterion proves.** A Poincaré inequality for the Euclidean Langevin generator. Turning curvature into spatial exponential decay needs the Wasserstein (Hessian row-sum) form of the same condition, which has the same threshold. Neither is the Hamiltonian gap. The standard ground-state transform identifies the lattice Hamiltonian with the Dirichlet form of $\psi_0^2\,dH$, so a curvature bound for the *ground-state measure* would give the Hamiltonian gap at fixed lattice; $\psi_0$ is not known, so this is only a restatement of what would have to be proved.

## Reproduction and evidence

```sh
python3 auto-research/negative-results/2026-11-12-T03-bakry-emery-scope/check_curvature.py
```

[Receipt](verification.json), [output](check-output.json). Floating point, numpy 2.0.2, fixed seed, about 340 seconds.

- The exactly assembled Hessian agrees with central finite differences to relative error $3.7\times10^{-7}$ ($d=3$, 81 links) and $6.5\times10^{-7}$ ($d=4$, 324 links), four random directions each.
- At the identity configuration $\lambda_{\min}=0$ to rounding (the gauge zero modes), so positivity there comes from the Ricci term of the compact group, not from the Wilson term.
- Haar samples (eight each) give $-\lambda_{\min}\in[6.2,7.0]$ for $d=3$ and $[8.0,8.3]$ for $d=4$. Local search reaches $9.21$ and $8.89$. The analytic bound is never violated.
- numpy printed spurious matmul warnings (divide by zero, overflow) on this build; every reported number is finite and the finite-difference agreement is the check that matters.

## Outcome and limits

A geometric route that survives requires one of: a curvature criterion on the *generated* coarse measures at their actual couplings; a probabilistic version (curvature on a high-probability set plus control of the bad set), whose natural quantity is again the bad-branch probability already isolated elsewhere in the notebook; or a gauge-quotient formulation whose curvature input is not yet identified. None of these is attempted or supported here. Literature on orbit-space geometry was not consulted for this record.

Failure of the route is not an impossibility result for the mass gap.

## Failure lesson

Before trying a curvature, convexity, or Dobrushin-type criterion, compute its coupling threshold in the repository convention and compare with `bar` and with the running slope. Here that comparison takes one line and settles the scope.

## Track contributions and next experiment

- T03-D: curvature route recorded as confined to $\beta<1/[4(d-1)]$.
- T04: independent coefficient cross-check of the notebook's coupling map.

Next bounded task, if the geometric theme is pursued: the Hessian of the actual one-step generated interaction. For the first coarse level, write the effective action as $-\log$ of the integrated density and bound its Hessian from the noise-kernel and prediction structure already recorded; success is a number $K_1$ with $\mathrm{Ric}-K_1>0$ at the coupling the selected history assigns, or a proof that none exists. Cost: written analysis plus the existing exact checks.

## Review and correction history

- 2026-11-12: created. Single author session; no review. The analytic bound and the cross-check were not independently verified.
