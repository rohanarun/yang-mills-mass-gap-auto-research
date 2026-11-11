# Polynomial decay does not imply a spectral gap

## Metadata

- Date: 2026-11-11.
- Author: rohanarun with OpenAI Codex assistance; historical baseline indexed for future agents.
- Primary track: [T06](../../tracks/T06-obstructions.md). Related: T02, T03.
- Outcome: counterexample to the inference from the stated scalar spectral bounds to a positive gap.
- Evidence: written operator construction plus exact symbolic checks of scalar integrals and asymptotics. The operator construction is not Lean-verified.
- Historical artifact commit: [`7148938bfe2fd8e1e545db7ece41f24f8aa98e51`](https://github.com/rohanarun/yang-mills-mass-gap-auto-research/tree/7148938bfe2fd8e1e545db7ece41f24f8aa98e51/research/mass-gap-20261111).
- Symbolic dependency: SymPy 1.14.0. The historical run exited successfully; the recorded output does not include its Python interpreter version.

## Claim tested

Does quadratic control of low-energy spectral weight, together with inverse-square heat decay and a unique zero-energy vacuum, force a positive spectral gap?

## Counterexample

Take the measure $d\mu(E)=Ee^{-E}\,dE$ on $(0,\infty)$. Then

$$
0<\mu((0,u])=1-(1+u)e^{-u}\leq u^2/2\quad(u>0),
\qquad \int_0^\infty e^{-tE}\,d\mu(E)=(1+t)^{-2}.
$$

The density is positive on every open interval inside $(0,\infty)$, so no positive interval above zero is spectrally empty. The notes realize this on $\mathbb C\oplus L^2(\mu)$ with vacuum in the first summand and multiplication by $E$ in the second. Its zero eigenspace is one-dimensional and it has no positive gap. The [full notes](../../../research/mass-gap-20261111/FirstPass.txt) explain the dense family and state-dependent constants.

## Reproduction and evidence

From the repository root, after installing [requirements.txt](../../../requirements.txt):

```sh
python3 research/mass-gap-20261111/check_obstruction.py
```

The [script](../../../research/mass-gap-20261111/check_obstruction.py) checks total mass, the low-energy integral, the heat integral, and divergence of the exponentially rescaled heat pairing for symbolic positive rate. The [historical output](../../../research/mass-gap-20261111/obstruction-check.json) records success. This entry indexes that evidence; it does not claim a new run or a proof-kernel check.

## Scope and lesson

This is a scalar spectral/operator example, **not** a four-dimensional Yang–Mills Wightman theory. Wilson origin, OPE, and the upstream trace properties have not been established for it. It does not refute the full construction or show that its stronger hypotheses cannot imply a gap.

The invalid inference is upgrading a polynomial upper bound to an empty low-energy interval. Agents should always test that inference against this example and require a genuinely stronger estimate. Reopen the route if an additional hypothesis, derived for the Yang–Mills hierarchy, excludes the example and supplies a valid gap argument. Merely improving a polynomial prefactor is insufficient.

## Track contributions

T06 retains a reproducible obstruction. T02 must use an actual common exponential rate or another sufficient hypothesis. T03 must derive new infrared information rather than relabel the polynomial bound. This lesson is incorporated in [auto-research.md](../../../auto-research.md).

## Review history

No independent review recorded.
