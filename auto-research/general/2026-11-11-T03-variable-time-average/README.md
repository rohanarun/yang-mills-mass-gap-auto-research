# Variable-time averaging: quadratic localization cost

## Status and provenance

- Date: 2026-11-11. Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03, T04, T06, T07. Outcome: refinement of a conditional estimate; no mass gap.
- Evidence: written measure-rescaling/locality argument and author-run Lean check of scalar algebra. The measure bridge and upstream construction have **not** been independently kernel-replayed or reviewed.
- Repository base: `574ec1821df2a19a4e5a275b3d3956c090d8242d`. Upstream: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).
- [Lean source](AveragingScale.lean), [output](AveragingScale.log), [verification receipt](verification.json). No novelty claim.

## Question and hypotheses

Can the unit-time averaging used by the [earlier cost audit](../2026-11-11-T03-infrared-cost-audit/README.md) be optimized? Fix a phase, a finite compactly supported word polynomial $A$, and $r>0$ bounding both absolute time and spatial norm of all its test supports. Adjoint reversal preserves these support bounds. Put

$$
v=A\Omega,\quad v^*=A^*\Omega,\quad M=\|v\|^2+\|v^*\|^2.
$$

Let $\mu,\nu$ be their finite diagonal momentum measures, supported in the forward cone. Write $F(u)=\mu(\{p:0<p_0\leq u\})$. Use the same positive-energy convention, Fourier normalization, and ordinary Euclidean spatial volume as the previous audit. The proposed improvement concerns the dependence on support radius; it does not improve the quadratic energy power.

## Written rescaling argument

The geometry in [`Polynomials.distant`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/EveryPhase/Polynomials.lean#L146) works for any $T>0$: the absolute time difference of two translated support points is at most $2r+T$, and their spatial distance is at least $\|x\|-2r$. Consequently the commutator expectation $\Delta(x,t)$ vanishes whenever

$$
|t|\leq T,\qquad \|x\|>4r+T.
$$

Push both measures forward by $p\mapsto Tp$, denoting them $\mu_T,\nu_T$. This preserves their masses and forward-cone support. Bilinearity of the Fourier pairing gives $\widehat\mu_T(z)=\widehat\mu(Tz)$ and $\Delta_T(x,t)=\Delta(Tx,Tt)$. Therefore the unit-time average defined in [`Average.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/EveryPhase/Average.lean) vanishes for

$$
\|x\|>(4r+T)/T.
$$

The preimage of the dilated low-energy window at $Tu$ is exactly the original window at $u$. Apply [`annulus` and `dyadic`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/EveryPhase/Light.lean) to these finite measures, with threshold $Tu$. For $u>0$ and $Tu\leq1$, this gives

$$
F(u)\leq\frac{64}{9}\left(\frac{4r+T}{T}\right)^3M(Tu)^2
=\frac{64}{9}\frac{(4r+T)^3}{T}Mu^2.
$$

This is a reparameterization of spectral measures, not scale invariance of Yang–Mills. The measures need not arise from a separately constructed dilated Yang–Mills model: the invoked shell theorem is stated for arbitrary finite measures satisfying its cone and commutator-average hypotheses. Both measures must be dilated together.

## Optimization and scope

For $r\geq0$ and $T>0$,

$$
\frac{(4r+T)^3}{T}-108r^2
=\frac{(T-2r)^2(T+16r)}{T}\geq0.
$$

For $r>0$, the minimum occurs at $T=2r$. When $2ru\leq1$, it is an admissible choice and yields

$$
\boxed{F(u)\leq768r^2Mu^2.}
$$

On the domain where both apply, this optimizes the earlier unit-time coefficient $(64/9)(4r+1)^3$. The new estimate remains valid for $0<u\leq1/(2r)$, which is the condition on the *dilated* threshold. No assertion about an optimizer outside that domain is needed. The coefficient retains the upstream factor-two dyadic bound; no sharper summation is silently substituted.

This improves a localization cost from cubic to quadratic in $r$. It does not supply a uniform bound on the cost of representing or approximating low-energy states.

For an orthogonal spectral projection $P_u$, a nonzero $x=P_ux$, and an approximant $v=A\Omega$ with $\|x-v\|\leq\eta\|x\|$, $0\leq\eta<1$, the contraction property implies

$$
(1-\eta)^2\|x\|^2\leq\|P_uv\|^2\leq768r^2Mu^2
$$

provided $2ru\leq1$. Thus a nonzero low-energy vector forces $r^2M\geq(1-\eta)^2\|x\|^2/(768u^2)$ for such an approximant. Conversely, a uniform strict upper bound below that threshold would rule out the vector. No such upper bound has been derived for Yang–Mills.

At radius $r=c/u$, the factor $r^2u^2=c^2$ does not improve as $u$ decreases. The [massless local-field control](../../negative-results/2026-11-11-T06-massless-locality/README.md) realizes this scaling and has nonzero weight arbitrarily near zero. Optimizing time alone cannot close the gap argument.

## Reproduction and verification boundary

With the previously recorded Lean 4.32.0 runtime on PATH, from `auto-research/general/2026-11-11-T02-uniform-projection-criterion/lean`:

```sh
lake env lean --trust=0 -j1 -R ../../2026-11-11-T03-variable-time-average ../../2026-11-11-T03-variable-time-average/AveragingScale.lean
```

The final run exited zero in 21.142 seconds with no warnings. Axiom reports contain only `propext`, `Classical.choice`, and `Quot.sound`. Dependency revisions and final source/output hashes are in the receipt. The prerequisite `GapCriteria` build was already completed in the previous investigation; its receipt is inherited, not a new upstream replay.

Lean checks the scalar identities, minimization, and substitution into an **assumed** rescaled inequality. The four-dimensional measure argument, support geometry, physical PVM application, and norm-approximation consequence above are written derivations. They are not certified by this scalar file. The initial successful run contained harmless tactic-linter warnings; those redundant tactics were removed before the final run.

## Next research step and review

Seek a dynamics-dependent bound on the dimensionless preparation cost $u^2r^2M/\|x\|^2$, retaining the admissibility condition $2ru\leq1$. The [auxiliary-resolvent audit](../../negative-results/2026-11-11-T03-auxiliary-resolvent-gap/README.md) identifies a separate missing bridge in a candidate source route. T03 remains open. T04 must track physical scales; T06 supplies controls; T07 must review and formalize the actual measure bridge. No independent review is recorded.
