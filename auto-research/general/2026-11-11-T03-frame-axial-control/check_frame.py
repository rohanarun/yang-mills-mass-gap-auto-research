"""Exact finite quaternion controls; not a replay of the source or a gap proof."""
from fractions import Fraction as F
import json
import random

ONE = (F(1), F(0), F(0), F(0))
ZERO = (F(0),) * 4


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c*x for x in a)


def sub(a, b):
    return add(a, scale(-1, b))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def inv(a):
    return (a[0], -a[1], -a[2], -a[3])


def mul(a, b):
    w, x, y, z = a
    v, r, s, t = b
    return (w*v-x*r-y*s-z*t, w*r+x*v+y*t-z*s,
            w*s-x*t+y*v+z*r, w*t+x*s-y*r+z*v)


def total(vectors):
    ans = ZERO
    for v in vectors:
        ans = add(ans, v)
    return ans


def stereo(rng, denominator):
    v = tuple(F(rng.randint(-3, 3), denominator) for _ in range(3))
    s = sum(x*x for x in v)
    q = ((1-s)/(1+s),) + tuple(2*x/(1+s) for x in v)
    assert dot(q, q) == 1
    return q


def score(k, edges):
    n, orders = len(k), len(edges[0][0])
    return sum(1-mul(mul(k[i], edges[i][j][l]), inv(k[j]))[0]
               for i in range(n) for j in range(n) for l in range(orders)) / (n*n*orders)


def field(k, edges, i):
    orders = len(edges[0][0])
    return scale(F(1, 2*orders), total(
        add(mul(k[j], inv(edges[i][j][l])), mul(k[j], edges[j][i][l]))
        for j in range(len(k)) if j != i for l in range(orders)))


rng = random.Random(2026111104)
epsilon = F(1, 4)
local_checks = centre_checks = dispersion_checks = 0
for n in (2, 3, 5):
    for _ in range(8):
        orders = 2
        edges = [[[ONE if i == j else stereo(rng, 100)
                   for _ in range(orders)] for j in range(n)] for i in range(n)]
        assert all(dot(sub(e, ONE), sub(e, ONE)) <= epsilon**2
                   for row in edges for cell in row for e in cell)
        k = [ONE] + [stereo(rng, 4) for _ in range(n-1)]
        old = score(k, edges)
        mean = scale(F(1, n), total(k))
        pair = sum(dot(sub(a, b), sub(a, b)) for a in k for b in k)/(n*n)
        assert pair == 2*(1-dot(mean, mean))
        assert pair <= 4*old+2*epsilon**2
        dispersion_checks += 1
        for i in range(n):
            si = field(k, edges, i)
            error = sub(si, total(k[j] for j in range(n) if j != i))
            assert dot(error, error) <= (n-1)**2*epsilon**2
            changed = list(k)
            changed[i] = stereo(rng, 3)
            assert score(changed, edges)-old == -F(2, n*n)*dot(sub(changed[i], k[i]), si)
            # A centre variation is admissible after a common left rotation.
            anchored = [mul(inv(changed[0]), q) for q in changed]
            assert anchored[0] == ONE
            assert score(anchored, edges) == score(changed, edges)
            local_checks += 1
            centre_checks += int(i == 0)

# Exact global minimizers of a relaxed routed-array problem: each term is zero.
# These arrays need not be realizable by a source fine field and axial gauge.
minimizer_checks = 0
for n in (2, 3, 5, 9):
    for _ in range(6):
        p = [ONE]+[stereo(rng, 200) for _ in range(n-1)]
        edges = [[[mul(inv(p[i]), p[j])] for j in range(n)] for i in range(n)]
        assert all(dot(sub(cell[0], ONE), sub(cell[0], ONE)) <= epsilon**2
                   for row in edges for cell in row)
        assert score(p, edges) == 0
        mean = scale(F(1, n), total(p))
        assert dot(mean, mean) >= 1-2*epsilon**2
        for i in range(n):
            si = field(p, edges, i)
            assert si == scale(n-1, p[i])
            error = sub(si, sub(scale(n, mean), p[i]))
            assert add(scale(n, mean), error) == scale(n, p[i])
            assert dot(sub(p[i], ONE), sub(p[i], ONE)) <= 16*epsilon**2/(1-2*epsilon**2)
        minimizer_checks += 1

energy_controls = []
for n in (4, 16, 64, 256, 1024):
    # One anchored +1 spin and n-1 spins at -1, all transports identity.
    weights = (F(1, n), F(n-1, n))
    points = (ONE, scale(-1, ONE))
    energy = sum(weights[i]*weights[j]*(1-dot(points[i], points[j]))
                 for i in range(2) for j in range(2))
    assert energy == F(4*(n-1), n*n)
    energy_controls.append({'N': n, 'score': str(energy), 'max_anchor_distance_squared': 4})

print(json.dumps({'seed': 2026111104, 'epsilon': str(epsilon),
                  'local_variation_identities': local_checks,
                  'centre_reanchoring_cases': centre_checks,
                  'dispersion_cases': dispersion_checks,
                  'known_minimizer_arrays': minimizer_checks,
                  'energy_only_controls': energy_controls,
                  'scope': 'Exact finite algebra in a relaxed routed-array model; no fine-field realization, Lean proof, or spatial estimate.'}, indent=2))
