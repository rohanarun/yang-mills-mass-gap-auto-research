"""Exact finite-chain control for interchanging log and integration.

Enumeration checks short chains; the all-length statement follows from the
two transfer-matrix eigenspaces described in README.md. This is not YM.
"""
import itertools
import json
import sympy as s

z, X, Y = s.symbols('z X Y', positive=True)
T = s.Matrix([[z, 1/z], [1/z, z]])
plus = s.Matrix([[1, 1], [1, 1]]) / 2
minus = s.eye(2) - plus
lp, lm = z + 1/z, z - 1/z
assert T == lp * plus + lm * minus
assert plus**2 == plus and minus**2 == minus
assert plus * minus == s.zeros(2)
checks = []
for edges in range(1, 6):
    Z = s.Add(*(z**sum(v[i]*v[i+1] for i in range(edges)) * X**v[0] * Y**v[-1]
                for v in itertools.product([-1, 1], repeat=edges+1)))
    at_zero = {X: 1, Y: 1}
    Z0 = s.simplify(Z.subs(at_zero))
    ds = (X * s.diff(Z, X)).subs(at_zero)
    dt = (Y * s.diff(Z, Y)).subs(at_zero)
    dst = (X * Y * s.diff(Z, X, Y)).subs(at_zero)
    cov = s.factor((dst * Z0 - ds * dt) / Z0**2)
    expected = ((z**2 - 1) / (z**2 + 1))**edges
    assert s.simplify(Z0 - 2*lp**edges) == 0
    assert s.simplify(cov - expected) == 0
    checks.append({'edges': edges, 'covariance': str(cov)})

R = s.symbols('R', positive=True)
scaled_limit = s.limit(((R-1)/(R+1))**R, R, s.oo)
assert scaled_limit == s.exp(-2)
s1, s2, J, A, B, interaction = s.symbols('s t J A B interaction', real=True)
assert s.diff(J*interaction+s1*A+s2*B, s1, s2) == 0
L1, L2, L3 = s.symbols('L1 L2 L3', positive=True)
p = s.Rational(2, 5)
product = L1**(-p) * L2**(-p) * L3**(-p)
assert s.simplify(product - (L1*L2*L3)**(-p)) == 0
print(json.dumps({
    'sympy_version': s.__version__,
    'transfer_matrix_decomposition': 'Exact complementary projections; eigenvalues z+1/z and z-1/z',
    'enumerated_chains': checks,
    'mixed_log_density_derivative': '0',
    'covariance_limit_at_J_R_equal_half_log_R': str(scaled_limit),
    'conditional_scale_contraction_identity': str(product) + ' = (L1*L2*L3)^(-2/5)',
    'scope': 'Exact algebra and finite enumeration; general chain formula has a written transfer-matrix proof. Not a Yang--Mills model.'
}, indent=2))
