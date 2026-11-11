# Perimeter attenuation is not separation decay

- Date / author: 2026-11-11; Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03, T04, T06.
- Base: `346263bc79c95062042078e7d20f4dac669f79da`.
- Evidence: written probability argument and exact finite non-Abelian checks; no Lean proof or independent review.
- Outcome: several shortcuts fail; the actual Yang–Mills decay question remains open.

The companion [one-step loop transfer](../../general/2026-11-11-T03-loop-noise-transfer/README.md) derives, for vertex-disjoint edge-distinct fundamental SU(2) loops,

$$
\mathrm{Cov}_{P_0}(W_C,W_D)
=a^{\ell_C+\ell_D}\mathrm{Cov}_{P_1}(\overline W_C,\overline W_D),
\qquad 0<a<1.
$$

## Failed inference: a factor below one proves spatial decay

The exponent is the sum of loop perimeters, not their separation. Moving two fixed-size loops farther apart leaves that factor unchanged. In the exact $Q_8$ control, hidden loop signs have covariance $1/2$ and independent link noise gives output covariance $(1/2)a^8>0$ for two squares. Gauge averaging preserves these loop traces and the equivariant noise calculation. Adding unused edges between the loops does not change the result.

The hidden law is a constructed correlated model, not the selected Wilson fine law or a continuum Yang–Mills theory. It tests only the inference that local smoothing alone forces spatial mixing. Reopen that inference only after deriving decay of the actual hidden averaged observables from dynamics.

## Failed inference: multiply a factor for every traversal

The one-loop formula requires distinct independent links. A backtrack $VV^{-1}$ cancels exactly. In the finite control its normalized trace is one, whereas $a^2<1$. Traversing the same edge twice also fails the rule: at finite-group noise parameter $\kappa=\log2$, the trace of $N^2$ has mean $-7/17$, while the proposed factor is $9/289$.

Overlapping loop supports similarly leave a conditional output-noise covariance. For edge-disjoint loops sharing a vertex, site tags can remain shared; their conditional tag covariance cannot simply be dropped. Vertex-disjointness is a sufficient condition for the stronger fine-law formula, not a consequence of link-disjointness alone.

## Failed inference: repeat the same factor at every RG level

The averaged prediction $\overline W_C$ need not be another simple Wilson loop. Actual predictions and their probabilities depend nonlinearly on the fine field. A further RG step requires a proved observable expansion or a direct estimate for this new function. Preserve complete read supports and all generated interactions; do not assume the observable class is closed.

## Reproduction and next question

The [script](../../general/2026-11-11-T03-loop-noise-transfer/check_loop_noise.py), [output](../../general/2026-11-11-T03-loop-noise-transfer/check-output.json), and [receipt](../../general/2026-11-11-T03-loop-noise-transfer/verification.json) record exact rational checks and their scope. Python 3.9.6 exited zero in 0.133 seconds. No simulation, continuum extrapolation, or upstream kernel replay was performed.

Next: derive a separation-dependent covariance bound for the actual $\overline W_C$, with regulator and observable costs. The [agent prompt](../../../auto-research.md) now requires distinguishing perimeter, separation, physical time, and RG-step counts. Independent review remains open.
