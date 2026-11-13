# Small average frame energy does not fix the anchored frame

- Date / author: 2026-11-11; Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03, T06. Evidence: written finite quaternion example and exact rational checks.
- Scope: failure of an energy-only inference, not a counterexample to the minimizing-frame theorem or Yang–Mills.

In the relaxed all-pairs problem take every transport equal to one, the centre spin equal to one, and the other $N-1$ spins equal to minus one. The normalized score is $4(N-1)/N^2$, tending to zero as $N$ grows, while the maximum distance from the anchored centre remains two. The candidate is **not** a minimizer: the constant frame has score zero. The [checker](../../general/2026-11-11-T03-frame-axial-control/check_frame.py) verifies the energy exactly at five sizes; [output](../../general/2026-11-11-T03-frame-axial-control/check-output.json) and [receipt](../../general/2026-11-11-T03-frame-axial-control/verification.json) preserve the execution.

Thus a small average energy alone cannot imply a pointwise anchored bound tending to zero uniformly in patch size. The [companion derivation](../../general/2026-11-11-T03-frame-axial-control/README.md) avoids that inference by using global minimality and local variations, including at the centre after reanchoring. Do not apply that step to an arbitrary low-energy or approximately minimizing frame without quantifying the optimization error.

The resulting loop replacement also leaves an additive error of order loop length times the two cutoff parameters, plus a bad-branch probability. A fixed additive error floor cannot establish decay to zero with separation. Future work must control the actual branch probabilities, retained fine-path covariances, and any approximation/scale costs; it must not count deterministic frame closeness as a mass-gap estimate. No Lean formalization or independent review is claimed.

Follow-up, 2026-11-11: the [uniqueness certificate](../../general/2026-11-11-T03-frame-uniqueness/README.md) bounds excess-score distance only modulo common gauge rotation. It does not contradict this example or justify a patch-size-independent anchored approximation bound. Its auxiliary matrix gap is an optimization property, not the Yang–Mills mass gap.
