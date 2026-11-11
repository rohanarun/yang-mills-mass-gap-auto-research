# Exact RG covariance decomposition and the nontrivial coarse endpoint

## Metadata and question

- Date: 2026-11-11. Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03, T04, T06. Outcome: written reduction to an explicit terminal estimate; no new dynamical bound or mass gap.
- Evidence: source inspection, written conditional-expectation argument, and an exact finite-state check. No new Lean proof or independent review is claimed.
- Repository base: `bac4f9dfb438546e7f584e154e85ee288316a67d`; upstream: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).
- Related: [connected-source bridge](../2026-11-11-T03-connected-source-bridge/README.md).

Can repeated blocking eliminate the retained covariance identified in the previous investigation? The exact recursion shows what would have to be controlled. The source's coarsest endpoint remains a growing-volume interacting measure; it does not become a scalar merely by removing more UV scales.

## A probability kernel from the actual vacuum transport

Fix a selected history, fine cutoff $N$, volume index $p$, and $0\leq j<N$. Suppress these parameters where convenient. Let $k_j(U,V)$ be the actual blocking density from fine level $j+1$ to coarse level $j$, and let $v_j$ be the actual positive vacuum density. The source supplies

$$
v_j(V)=\int k_j(U,V)v_{j+1}(U)\,d\mu_{j+1}(U),\qquad
\int k_j(U,V)\,d\mu_j(V)=1.
$$

The first identity comes from [`Selected.steps`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/History.lean) and `Signals.vac_eq`. The second is [`StepData.IsKernel.total`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Block.lean#L158); its integration direction matters. `History.partition_eq` and [`push_integral`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Push.lean#L37) preserve the partition function $Z$.

With $dP_j=v_j\,d\mu_j/Z$, define the reverse conditional kernel

$$
Q_j(V,dU)=\frac{k_j(U,V)v_{j+1}(U)}{v_j(V)}\,d\mu_{j+1}(U).
$$

It is a probability kernel wherever $v_j>0$, and $P_jQ_j=P_{j+1}$. The positive source vacuum provides the denominator. For the following formulas assume the requisite products are integrable; bounded fine observables suffice at each finite cutoff. This is a written construction from the source identities, not a formal replay of their measure-theoretic application.

## Remove the engineering factors before identifying conditional expectations

Let $r_{s,j}=T_{s,j}/v_j$ be `Insertions.ratios`, and let $D_s$ be the sum of the marker loads. [`Signals.total_step`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Extra/MULTISOURCE_TRAJECTORIES/Signals.lean#L112) and [`Ride.bump`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Overlay/Engine.lean#L36) give

$$
r_{s,j}=L_j^{D_s}Q_jr_{s,j+1}.
$$

The schedule satisfies $a_{j+1}=a_j/L_j$. Consequently the corrected ratios $f_{s,j}=a_j^{-D_s}r_{s,j}$ satisfy the exact conditional-expectation relation

$$
f_{s,j}=Q_jf_{s,j+1}.
$$

At level $N$, the source formula makes $f_{s,N}$ the product of the specified fine insertions. The raw ratios themselves are not a martingale: ignoring their engineering multipliers would change the observable normalization.

For two fine observables $F,G$, put $f_N=F$, $g_N=G$ and recursively $f_j=Q_jf_{j+1}$, $g_j=Q_jg_{j+1}$. With complex insertions use bilinear covariance; introduce the appropriate adjoint in $F$ or $G$ for a physical reflected correlation.

## The retained term survives exact telescoping

Define the one-step conditional covariance

$$
\Delta_j=Q_j(f_{j+1}g_{j+1})-(Q_jf_{j+1})(Q_jg_{j+1}).
$$

The kernel identity gives

$$
\mathrm{Cov}_{P_{j+1}}(f_{j+1},g_{j+1})
=\mathbb E_{P_j}\Delta_j+\mathrm{Cov}_{P_j}(f_j,g_j).
$$

Adding these equalities yields the exact finite-cutoff decomposition

$$
\boxed{\mathrm{Cov}_{P_N}(F,G)
=\mathrm{Cov}_{P_0}(f_0,g_0)+
\sum_{j=0}^{N-1}\mathbb E_{P_j}\Delta_j.}
$$

For $G=\overline F$, each averaged conditional variance is nonnegative and the terminal variance is nonnegative. For general pairs there is no such sign guarantee; use absolute bounds when estimating the sum. A correlation bound requires both the terminal covariance and a summable budget for the fluctuation terms in physical separation. A bound on an aggregate conditional cumulant is not automatically a separate bound on each summand.

## The source endpoint is not an infrared limit

[`Schedule`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Lattice/Scale.lean) defines

$$
a_0=1,\qquad \mathrm{side}(0,p)=\mathrm{period}(p),
$$

and `period_strict` makes the period tend to infinity. Its four-dimensional coarse lattice therefore still has $\mathrm{period}(p)^4$ sites. Sending $N\to\infty$ adds finer UV levels above this endpoint; it does not add levels below zero or integrate the entire retained field into one number. Even at a fixed finite volume, stopping at a nontrivial field space does not make its covariance vanish.

`Selected.reaches` fixes the representation's scalar inverse coupling at level zero to `bar`. `Calendar.Fits.delayed 0`, `hatBeta`, and `scale_zero` imply `bar > 1`. This does not identify $P_0$ as a bare Wilson law: `Rep.eval` retains its path-dependent reference action, activities, and scalar normalization, and only the fine endpoint is required by `starts` to be bare.

As a diagnostic for $SU(2)$ in four dimensions, the **specific** strong-coupling theorem and normalization audited [earlier](../../negative-results/2026-11-11-T04-strong-coupling-scope/README.md) would require a bare Wilson inverse coupling below $4/[16(4-1)]=1/12$. The source's `bar > 1` fails that sufficient range even before the generated interactions are considered. This does not exclude other mixing theorems or a further justified infrared RG extension. It prevents invoking that cited theorem directly at this endpoint.

## Exact finite-state check

[The script](check_terminal.py) uses two symmetric two-state kernels $Q_j(v,u)=(1+q_jvu)/2$, with $|q_j|\leq1$, uniform marginals, and $F=G=\sigma$. Direct symbolic summation gives

$$
1=\underbrace{q_0^2q_1^2}_{\text{terminal variance}}
+\underbrace{q_1^2(1-q_0^2)}_{\text{level 0 increment}}
+\underbrace{1-q_1^2}_{\text{level 1 increment}}.
$$

The terminal term is nonzero when both $q_j$ are nonzero. The script also checks the engineering-factor cancellation for arbitrary positive block lengths and the quoted $SU(2)$ threshold arithmetic. This is an algebraic control of recursion orientation and normalization, not a Yang–Mills model or proof of a spatial decay estimate.

From the repository root:

```sh
python3 auto-research/general/2026-11-11-T03-terminal-covariance/check_terminal.py
```

[Output](terminal-check.json) and [receipt](verification.json) record the actual run and source/output hashes. No new Lean theorem was added: the unresolved task is dynamical rather than another abstract covariance identity.

## Next analytic target and failure lesson

Attempt a uniform mixing estimate for the actual level-zero measures $P_{0,N,p}$ and the transported observables $f_{0,N,p},g_{0,N,p}$. Track their localization and normalization; they need not remain strictly local after transport. Combine it with an absolutely summable bound for the fluctuation terms, at one positive physical rate, and then prove the required limits and reconstruction bridge. Alternatively derive a justified continuation to larger physical blocking scales, with those same observables and complete generated interactions.

Do not infer that iterating an exact UV recursion removes the terminal covariance. Do not replace the blocked law by a bare Wilson measure from knowledge of its scalar coupling. This record identifies necessary work for this route; it does not prove that such work is feasible or that every mass-gap proof must follow it. No independent review is recorded.

## Follow-up — 11 November 2026

The [single-link influence audit](../../negative-results/2026-11-11-T03-single-link-influence/README.md) excludes one simple route: the bare SU(2) single-link total-variation contraction test fails at beta at least one. This covers the selected N=0 endpoint, but does not determine the large-N coarse measures. Block criteria and the actual generated interactions still require analysis.
