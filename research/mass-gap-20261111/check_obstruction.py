"""Exact symbolic checks for a scalar spectral obstruction, not Yang--Mills."""
import json
import sympy as s
E, t, u, m = s.symbols("E t u m", positive=True)
rho = E * s.exp(-E)
heat = s.integrate(s.exp(-t*E)*rho, (E, 0, s.oo))
low = s.integrate(rho, (E, 0, u))
assert s.simplify(heat - 1/(1+t)**2) == 0
assert s.simplify(low - (1-(1+u)*s.exp(-u))) == 0
assert s.integrate(rho, (E, 0, s.oo)) == 1
assert s.limit(s.exp(m*t)*heat, t, s.oo) == s.oo
print(json.dumps({
    "scope": "Scalar spectral example only; not a Yang--Mills model or Lean proof",
    "sympy_version": s.__version__,
    "density": str(rho),
    "total_mass": "1",
    "heat": str(s.simplify(heat)),
    "low_energy_mass": str(s.simplify(low)),
    "exponentially_rescaled_limit_for_every_m_positive": "infinity",
    "passed": True
}, indent=2))
