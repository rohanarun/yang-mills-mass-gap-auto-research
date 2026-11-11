# Gauge symmetry alone does not bound loop correlations

- Date / tracks: 2026-11-11; T06, related T03 and T05.
- Author: Rohan Arun, with OpenAI Codex assistance.
- Base: `d95fa752e993c81ce2e01008efb75862aaf39ab6`.
- Outcome: exact finite controls against two unsupported inferences; not a counterexample to Yang–Mills.
- Evidence: written finite-group argument and exact Python enumeration; no Lean proof or independent review.

The companion [gauge-orbit response record](../../general/2026-11-11-T03-gauge-orbit-response/README.md) proves a written forest-conditioning identity and supplies [the executable control](../../general/2026-11-11-T03-gauge-orbit-response/check_gauge_response.py), [output](../../general/2026-11-11-T03-gauge-orbit-response/check-output.json), [receipt](../../general/2026-11-11-T03-gauge-orbit-response/verification.json), and source provenance.

## Unsupported inference 1

“Acyclic observed links reveal no gauge-invariant information, so gauge symmetry forces distant physical observables to become independent.”

For two loops with independent $Q_8$ Haar link variables, put $w=1+c\phi_1\phi_2$, where $0<c<1$ and each $\phi_i$ is a normalized loop trace. This positive, gauge-invariant density has covariance $c/16$. Observing only a forest from the second loop gives no information about the first, yet observing the completed cycle does. Inserting independent bridge edges of arbitrary length does not change the covariance. The interaction explicitly couples the distant loops; it is not local Wilson dynamics and does not satisfy the full construction's hypotheses.

What failed: screening of forest data was extended to a cyclic exterior without justification. Always specify exactly which links are observed and which are integrated. Reopen a spatial-decay claim only with an actual local dynamical estimate, uniform in the required limits.

## Unsupported inference 2

“Individual traces of a chosen set of fundamental loops retain all physical information.”

For based loops in the same connected component, holonomy pairs $(i,i)$ and $(i,j)$ have individual normalized traces $(0,0)$ but product traces $-1$ and $0$. They cannot be simultaneously conjugate. The trace test applies to these unit quaternions in SU(2) as well as in $Q_8$; it is not a claim that all possible Wilson-loop traces fail to separate orbits.

What failed: separate conjugacy information was substituted for a joint conjugacy orbit. Retain relative non-Abelian loop information or prove the proposed observable family sufficient. Also account for the full tree paths used to form based loops.

## Verification and handoff

The companion script enumerates two rational couplings, checks forest and cycle conditionals exactly, and tests the trace counterexample. It passed with Python 3.9.6 in 0.518 seconds. No simulation or numerical fit was used. Its bounds do not transfer to the continuum theory merely because $Q_8$ embeds in SU(2).

These controls narrow the next target to gauge-invariant connected response under the actual law. The [agent prompt](../../../auto-research.md) incorporates both lessons. Independent review remains open.
