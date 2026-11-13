"""Exact quaternion certificate controls on relaxed finite transport arrays.

No source fine-field realization, Lean proof, or physical spectral estimate.
"""
from fractions import Fraction as F
import json
import random

ONE = (F(1), F(0), F(0), F(0))
ZERO = (F(0),)*4
BASIS = [tuple(F(i == j) for i in range(4)) for j in range(4)]


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c*x for x in a)


def sub(a, b):
    return add(a, scale(-1, b))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def conj(q):
    return (q[0], -q[1], -q[2], -q[3])


def mul(a, b):
    w, x, y, z = a
    v, r, s, t = b
    return (w*v-x*r-y*s-z*t, w*r+x*v+y*t-z*s,
            w*s-x*t+y*v+z*r, w*t+x*s-y*r+z*v)


def total(vectors):
    out = ZERO
    for v in vectors:
        out = add(out, v)
    return out


def stereo(v):
    s = dot(v, v)
    return ((1-s)/(1+s),)+tuple(2*x/(1+s) for x in v)


def right(q):
    columns = [mul(e, q) for e in BASIS]
    return [[columns[j][i] for j in range(4)] for i in range(4)]


def quad(a, x):
    return sum(x[i]*a[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))


def positive_ldl(a):
    """Exact Schur-complement pivots certify positive definiteness."""
    a = [list(row) for row in a]
    assert all(a[i][j] == a[j][i] for i in range(len(a)) for j in range(len(a)))
    pivots = []
    for k in range(len(a)):
        pivot = a[k][k]
        assert pivot > 0, (k, pivot)
        pivots.append(pivot)
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                a[i][j] -= a[i][k]*a[k][j]/pivot
    return min(pivots)


def score(k, e):
    n, m = len(k), len(e[0][0])
    return sum(1-mul(mul(k[i], e[i][j][l]), conj(k[j]))[0]
               for i in range(n) for j in range(n) for l in range(m))/(n*n*m)


rng = random.Random(2026111105)
epsilon, gamma = F(1, 16), F(1, 4)
# D(epsilon) <= 5 epsilon follows by squaring its positive denominator.
assert 1-2*epsilon**2 >= F(16, 25)
assert 1-12*epsilon == gamma
fixtures = []
energy_checks = 0
for n in (3, 4, 5):
    for denominator in (128, 256, 512):
        m = 3
        # Each layer carries a balanced oriented triangular quaternion flux.
        # Different layers use different imaginary axes, so they do not commute.
        f = [[[ONE for _ in range(m)] for _ in range(n)] for _ in range(n)]
        qs = []
        for l in range(m):
            q = stereo(tuple(F(int(a == l), denominator) for a in range(3)))
            qs.append(q)
            cycle = (0, 1, 2+l % (n-2))
            for i, j in zip(cycle, cycle[1:]+cycle[:1]):
                f[i][j][l], f[j][i][l] = q, conj(q)
        assert mul(mul(qs[0], qs[0]), qs[0]) != ONE
        assert mul(qs[0], qs[1]) != mul(qs[1], qs[0])
        p = [ONE]+[stereo(tuple(F(rng.randint(-2, 2), 1024) for _ in range(3)))
                   for _ in range(n-1)]
        e = [[[mul(mul(conj(p[i]), f[i][j][l]), p[j]) for l in range(m)]
              for j in range(n)] for i in range(n)]
        max_error_sq = max(dot(sub(q, ONE), sub(q, ONE))
                           for row in e for cell in row for q in cell)
        assert max_error_sq < epsilon**2
        a = [[scale(F(1, 2*m), total(add(conj(f[i][j][l]), f[j][i][l])
                                         for l in range(m))) for j in range(n)] for i in range(n)]
        rows = [total(row) for row in a]
        assert all(row[1:] == (0, 0, 0) for row in rows)
        alpha = [row[0] for row in rows]
        blocks = [[right(a[i][j]) for j in range(n)] for i in range(n)]
        lap = [[(alpha[i//4] if i == j else F(0))-blocks[i//4][j//4][i % 4][j % 4]
                for j in range(4*n)] for i in range(4*n)]
        assert all(lap[i][j] == lap[j][i] for i in range(4*n) for j in range(4*n))
        assert all(sum(lap[i][4*j+c] for j in range(n)) == 0
                   for i in range(4*n) for c in range(4))
        comparison = [[lap[i][j]-gamma*((n if i == j else 0)-int(i % 4 == j % 4))
                       for j in range(4*n)] for i in range(4*n)]
        # Both matrices annihilate constant blocks. Grounding one block is
        # therefore an exact test of strict positivity on their quotient.
        min_pivot = positive_ldl([row[4:] for row in comparison[4:]])
        baseline = score(p, e)
        assert baseline > 0  # genuinely frustrated, not the zero-energy fixture
        for _ in range(12):
            v = [stereo(tuple(F(rng.randint(-4, 4), 3) for _ in range(3))) for _ in range(n)]
            competitor = [mul(v[i], p[i]) for i in range(n)]
            energy = score(competitor, e)-baseline
            flat = [x for q in v for x in q]
            assert energy == quad(lap, flat)/(n*n)
            mean = scale(F(1, n), total(v))
            variance = 1-dot(mean, mean)
            assert energy >= gamma*variance
            energy_checks += 1
        fixtures.append({'N': n, 'noise_denominator': denominator,
                         'max_input_error_squared': str(max_error_sq),
                         'minimizer_score': str(baseline),
                         'comparison_min_ldl_pivot': str(min_pivot)})
# Independently exercise the ordered-pair symmetrization without reciprocity
# or stationarity; these cases are algebra checks, not minimizer certificates.
general_checks = 0
for n in (3, 4):
    for _ in range(6):
        m = 2
        f = [[[ONE if i == j else stereo(tuple(F(rng.randint(-3, 3), 5) for _ in range(3)))
               for _ in range(m)] for j in range(n)] for i in range(n)]
        a = [[scale(F(1, 2*m), total(add(conj(f[i][j][l]), f[j][i][l])
                                     for l in range(m))) for j in range(n)] for i in range(n)]
        blocks = [[right(a[i][j]) for j in range(n)] for i in range(n)]
        c = [[blocks[i//4][j//4][i % 4][j % 4] for j in range(4*n)] for i in range(4*n)]
        assert all(c[i][j] == c[j][i] for i in range(4*n) for j in range(4*n))
        v = [stereo(tuple(F(rng.randint(-3, 3), 4) for _ in range(3))) for _ in range(n)]
        assert score(v, f) == 1-quad(c, [x for q in v for x in q])/(n*n)
        general_checks += 1
print(json.dumps({'seed': 2026111105, 'epsilon': str(epsilon), 'gamma': str(gamma),
                  'frustrated_certificate_fixtures': fixtures,
                  'exact_energy_identity_and_coercivity_checks': energy_checks,
                  'nonreciprocal_symmetrization_checks': general_checks,
                  'scope': 'Relaxed noncommuting quaternion arrays; exact matrix certificates, not actual fine fields or a physical mass gap.'}, indent=2))
