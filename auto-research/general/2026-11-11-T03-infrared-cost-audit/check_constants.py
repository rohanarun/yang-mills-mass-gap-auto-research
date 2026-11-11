"""Check the coefficient extracted from the inspected shell bound.
This does not replay the upstream proof or establish uniform state costs.
"""
import json
import sympy as s
R, M = s.symbols("R M", nonnegative=True)
unit_ball = 4 * s.pi / 3
fee = unit_ball * R**3 * M * 8 * unit_ball
annulus = s.simplify(fee * (2*s.pi)**(-3) * (2*s.pi))
low = s.simplify(2 * annulus)
assert s.simplify(annulus - s.Rational(32,9)*M*R**3) == 0
assert s.simplify(low - s.Rational(64,9)*M*R**3) == 0
print(json.dumps({"sympy_version":s.__version__, "annulus":str(annulus),
                  "low_energy":str(low), "passed":True,
                  "scope":"Scalar coefficient algebra; not a Yang--Mills gap proof"},indent=2))
