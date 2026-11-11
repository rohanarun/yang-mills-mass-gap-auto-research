# The admissible cutoff endpoint does not supply a uniform norm margin

- Date / author: 2026-11-11; Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03, T04, T06; base `f43cf0d76f1cc90aff46006ddc112159abd9c0ca`.
- Evidence: written source-weight construction and exact integer/rational controls; no Lean proof or independent review.

The [companion derivation](../../general/2026-11-11-T03-cutoff-endpoint/README.md) constructs unit-quaternion connectors with weighted mean $rI$ for every $r\in[0,1]$, using the source's actual convolution weights. It shows that fundamental SU(2) predictor uniqueness over all active connectors is equivalent to $c\leq1$ when $c>0$.

**Failed inference:** uniqueness forces the strict cutoff margin $c<1$. At $c=1$ every active connector has a unique minimizer, but the source-weight family has arbitrarily small positive mean norms. No uniform positive norm margin follows. This is a statement about the source's universally quantified connector domain, not a realization theorem for actual fine-field configurations or a complete selected history at that cutoff.

**Failed inference:** a small-ball estimate automatically restores geometric truncation convergence. With the illustrative probability density $2r$ on $(0,1)$, one has $\Pr(R\leq\varepsilon)=\varepsilon^2$, but the exact mean error of degree-$K$ predictor truncation is $1/(2K+3)$. The finite polynomial integrals are checked at six degrees. The identity for all degrees follows by telescoping $2/[(2n+1)(2n+3)]$, and is a written argument.

The [checker](../../general/2026-11-11-T03-cutoff-endpoint/check_endpoint.py), [output](../../general/2026-11-11-T03-cutoff-endpoint/check-output.json), and [receipt](../../general/2026-11-11-T03-cutoff-endpoint/verification.json) record successful exact controls. They do not establish a small-ball law for Yang–Mills or a physical decay estimate.

Future agents must distinguish the source's connector quantifier from connectors actually induced by fine fields, prove any regulator-uniform small-ball hypothesis under the correct joint law, and separately bound correlations of retained observables. The [agent prompt](../../../auto-research.md) records these lessons. Independent review remains open.
