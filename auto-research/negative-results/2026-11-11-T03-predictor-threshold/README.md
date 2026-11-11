# Predictor thresholds prevent an unqualified polynomial replacement

- Date / author: 2026-11-11; Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03 and T06; base `3699c4d41ed1bbd95d719976651bd75b979e8c18`.
- Outcome: written obstruction to dropping the predictor mask or replacing uniqueness by a uniform norm margin.
- Evidence: exact rational controls and written analysis; no Lean proof or independent review.

The [predictor-average derivation](../../general/2026-11-11-T03-predictor-average/README.md) shows that the fundamental SU(2) bond-tag mean is $M/|M|$ on the strict minimizing branch $1-|M|<c$, and $M$ on fallback.

For $M=rI$ and $0<c<1$, this map jumps by $c$ at $r=1-c$. A continuous approximation across that boundary has uniform error at least $c/2$. Thus an ordinary polynomial approximation with arbitrarily small uniform error cannot replace the branch mask on the full moment domain. The geometric approximation in the companion record explicitly preserves the mask.

At $c=1$, the minimizer is unique for every $r>0$, but $r$ can approach zero. For every fixed truncation degree, $r\sum_{n=0}^K b_n(1-r^2)^n$ then approaches zero while the exact normalized mean is one. Uniqueness alone does not give the uniform geometric remainder needed for a volume/cutoff-uniform argument.

These radial examples concern the moment map, not a proof that the actual selected fine configurations realize every threshold crossing. Nor do they exclude smoothing after subsequent integration. The inspected source structure supplies $c>0$; an upper bound $c<1$ for the particular fixed kernel was not established here. Changing that kernel would change the target history.

The [script](../../general/2026-11-11-T03-predictor-average/check_predictor.py), [output](../../general/2026-11-11-T03-predictor-average/check-output.json), and [receipt](../../general/2026-11-11-T03-predictor-average/verification.json) give the exact finite checks. They passed with Python 3.9.6 in 0.044 seconds. The argument about all truncation degrees is written, not checked by enumerating infinitely many degrees.

Future attempts must retain cutoff masks and shared frame choices, prove a uniform margin or suitable integrated substitute, and bound the correlations of the resulting observables. Small approximation error alone is not spatial decay. These lessons are reflected in the [agent prompt](../../../auto-research.md). Independent review remains open.
