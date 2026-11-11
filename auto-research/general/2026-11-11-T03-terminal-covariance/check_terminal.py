"""Exact two-state control of covariance transport; no YM identification."""
import json
import sympy as s

q0, q1 = s.symbols('q0 q1', real=True)
spins = [-1, 1]
half = s.Rational(1, 2)

def expectation(f):
    return s.simplify(sum(half * f(v) for v in spins))

def push(q, f, v):
    return s.simplify(sum((1+q*v*u)*half*f(u) for u in spins))

f2 = lambda u: u
f1 = lambda v: push(q1, f2, v)
f0 = lambda v: push(q0, f1, v)
for q in [q0, q1]:
    for v in spins:
        assert push(q, lambda u: 1, v) == 1
        assert s.simplify(sum(half*(1+q*v*u)*half for u in spins)-half) == 0

terminal = expectation(lambda v: f0(v)**2) - expectation(f0)**2
delta0 = expectation(lambda v: push(q0, lambda u: f1(u)**2, v) - f0(v)**2)
delta1 = expectation(lambda v: push(q1, lambda u: f2(u)**2, v) - f1(v)**2)
variance = expectation(lambda u: f2(u)**2) - expectation(f2)**2
assert s.simplify(variance-terminal-delta0-delta1) == 0
assert s.simplify(terminal-q0**2*q1**2) == 0
assert s.simplify(delta0-q1**2*(1-q0**2)) == 0
assert s.simplify(delta1-(1-q1**2)) == 0
L0, L1 = s.symbols('L0 L1', positive=True)
for degree in [1, 2, 3]:
    a0, a1, a2 = 1, 1/L0, 1/(L0*L1)
    for v in spins:
        assert s.simplify(a0**degree*f0(v)-L0**degree*push(q0, lambda u: a1**degree*f1(u), v)) == 0
        assert s.simplify(a1**degree*f1(v)-L1**degree*push(q1, lambda u: a2**degree*f2(u), v)) == 0
threshold = s.Rational(2**2, 16*(4-1))
assert threshold == s.Rational(1, 12) and threshold < 1
print(json.dumps({
    'sympy_version': s.__version__,
    'kernel_positivity_domain': '-1 <= q0,q1 <= 1',
    'fine_variance': str(variance),
    'terminal_variance': str(s.factor(terminal)),
    'coarse_increment': str(s.factor(delta0)),
    'fine_increment': str(s.factor(delta1)),
    'telescoping_residual': str(s.simplify(variance-terminal-delta0-delta1)),
    'engineering_degrees_checked': [1, 2, 3],
    'SU2_cited_bare_Wilson_threshold': str(threshold),
    'scope': 'Exact finite-state identities and threshold arithmetic; source-matched general derivation is written, no YM mixing bound.'
}, indent=2))
