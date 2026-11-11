"""Exact scalar checks only; this does not construct a quantum field."""
import json
import sympy as s

u, L, c, r, E, t = s.symbols('u L c r E t', positive=True)
prefactor = 4 * s.pi / (2 * (2 * s.pi) ** 3)
low_coefficient = s.simplify(prefactor * s.integrate(E, (E, 0, u)) / u**2)
heat_coefficient = s.simplify(prefactor * s.integrate(E * s.exp(-t * E), (E, 0, s.oo)) * t**2)
norm_scaling = s.simplify(L**2 * L**(-3) * L)
dimensionless_cost = s.simplify((L * r)**2 * (c / L)**2)
assert low_coefficient == 1 / (8 * s.pi**2)
assert heat_coefficient == 1 / (4 * s.pi**2)
assert norm_scaling == 1
assert dimensionless_cost == r**2 * c**2
print(json.dumps({
    'sympy_version': s.__version__,
    'low_energy_coefficient_per_abs_fourier_zero_squared': str(low_coefficient),
    'heat_coefficient_per_abs_fourier_zero_squared': str(heat_coefficient),
    'mass_shell_norm_scaling_factor': str(norm_scaling),
    'radius_energy_squared': str(dimensionless_cost),
    'scope': 'Scalar constants and scaling only; field model and limit interchanges are written arguments.'
}, indent=2))
