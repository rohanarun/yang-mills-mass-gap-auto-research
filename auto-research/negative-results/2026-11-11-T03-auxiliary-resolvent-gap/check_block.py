"""Finite Gaussian block control; not a Yang--Mills model."""
import json
import sympy as s

eps = s.symbols('epsilon', positive=True)
x, y = s.symbols('x y', real=True)
A = s.Matrix([[1, -1], [-1, 1 + eps]])
v = s.Matrix([x, y])
inverse = A.inv()
schur = s.simplify(A[1, 1] - A[1, 0] * A[0, 0]**(-1) * A[0, 1])
ray = s.Matrix([1, 1])
rayleigh = s.simplify((ray.T * A * ray)[0] / (ray.T * ray)[0])
assert s.expand((v.T * A * v)[0] - ((x-y)**2 + eps*y**2)) == 0
assert s.simplify(A.det() - eps) == 0
assert (A * inverse - s.eye(2)).applyfunc(s.simplify) == s.zeros(2)
expected = s.Matrix([[1 + 1/eps, 1/eps], [1/eps, 1/eps]])
assert (inverse - expected).applyfunc(s.simplify) == s.zeros(2)
assert schur == eps
assert rayleigh == eps/2
print(json.dumps({
    'sympy_version': s.__version__,
    'precision': str(A), 'inverse': str(inverse),
    'fast_precision': str(A[0, 0]), 'schur_complement': str(schur),
    'determinant': str(A.det()), 'rayleigh_quotient': str(rayleigh),
    'scope': 'Exact finite-matrix identities only; no physical Hamiltonian or Yang--Mills identification.'
}, indent=2))
