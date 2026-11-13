"""Exact algebraic diagnostics, not a Yang--Mills simulation or full proof."""

from fractions import Fraction as F
import itertools
import json
import math
import platform
import random
import sympy as sp


def mul(a, b):
    w, x, y, z = a
    v, i, j, k = b
    return (w*v-x*i-y*j-z*k, w*i+x*v+y*k-z*j,
            w*j-x*k+y*v+z*i, w*k+x*j-y*i+z*v)


def inv(q):
    return (q[0], -q[1], -q[2], -q[3])


def rational_unit(rng):
    a, b, c = (rng.randint(-3, 3) for _ in range(3))
    r = a*a+b*b+c*c
    q = tuple(F(x, 1+r) for x in (1-r, 2*a, 2*b, 2*c))
    assert sum(x*x for x in q) == 1
    return q


def loop(links):
    q = (1, 0, 0, 0)
    for e, orientation in enumerate((1, 1, -1, -1)):
        q = mul(q, links[e] if orientation == 1 else inv(links[e]))
    return q[0]


def bessel_interval(order, x, cutoff=40):
    term = (x/2)**order / math.factorial(order)
    total = term
    for k in range(cutoff):
        term *= x*x / (4*(k+1)*(k+order+1))
        total += term
    omitted = term*x*x / (4*(cutoff+1)*(cutoff+order+1))
    ratio = x*x / (4*(cutoff+2)*(cutoff+order+2))
    assert 0 <= ratio < 1
    return total, total+omitted/(1-ratio)


def main():
    rng = random.Random(2026111302)
    gauge_cases = 0
    edges = ((0, 1), (1, 2), (3, 2), (0, 3))
    for _ in range(24):
        g = [rational_unit(rng) for _ in range(4)]
        v = [rational_unit(rng) for _ in range(4)]
        q = [rational_unit(rng) for _ in range(4)]
        def transform(fields):
            return [mul(mul(g[s], fields[e]), inv(g[t])) for e, (s, t) in enumerate(edges)]
        vg, qg = transform(v), transform(q)
        assert loop(vg) == loop(v)
        assert sum(mul(vg[e], inv(qg[e]))[0] for e in range(4)) == sum(mul(v[e], inv(q[e]))[0] for e in range(4))
        gauge_cases += 1

    t = sp.symbols('t', real=True)
    mixture_cases = 0
    for case in range(6):
        kappa = sp.Rational(case+1, 2)
        base = [rational_unit(rng) for _ in range(2)]
        predictions = [[rational_unit(rng) for _ in range(2)] for _ in range(3)]
        axes = (case % 3, (case+1) % 3)
        speeds = (1, 2 if case % 2 else -1)
        posterior = (sp.Rational(1, 6), sp.Rational(1, 3), sp.Rational(1, 2))
        terms, x0, scores = [], [], []
        for z in range(3):
            trace_sum = 0
            xs, bs = [], []
            for e in range(2):
                rotation = [sp.cos(speeds[e]*t), 0, 0, 0]
                rotation[axes[e]+1] = sp.sin(speeds[e]*t)
                trace_sum += mul(mul(base[e], rotation), inv(predictions[z][e]))[0]
                relative = mul(inv(predictions[z][e]), base[e])
                xs.append(sp.Rational(relative[0]))
                bs.append(sp.Rational(relative[axes[e]+1])*speeds[e])
            # Positive fixed base weights chosen so the posterior at t=0 is exact.
            terms.append(posterior[z]*sp.exp(kappa*(trace_sum-sum(xs))))
            x0.append(sum(xs[e]*speeds[e]**2 for e in range(2)))
            scores.append(sum(bs))
        partition = sum(terms)
        f1 = sp.simplify(sp.diff(-sp.log(partition), t).subs(t, 0))
        f2 = sp.simplify(sp.diff(-sp.log(partition), t, 2).subs(t, 0))
        mean_score = sum(posterior[z]*scores[z] for z in range(3))
        variance = sum(posterior[z]*scores[z]**2 for z in range(3))-mean_score**2
        expected = kappa*sum(posterior[z]*x0[z] for z in range(3))-kappa**2*variance
        assert sp.simplify(f1-kappa*mean_score) == 0
        assert sp.simplify(f2-expected) == 0
        mixture_cases += 1

    b = sp.symbols('b', positive=True)
    cycle_links = [(-sp.cos(t), -sp.sin(t), 0, 0),
                   (sp.cos(t), sp.sin(t), 0, 0),
                   (sp.cos(t), -sp.sin(t), 0, 0),
                   (sp.cos(t), -sp.sin(t), 0, 0)]
    w = sp.trigsimp(sp.expand_trig(loop(cycle_links)))
    assert sp.trigsimp(w+sp.cos(4*t)) == 0
    second = sp.simplify(sp.diff(-sp.log(1+b*w), t, 2).subs(t, 0))
    assert sp.simplify(second+16*b/(1-b)) == 0
    curvature = sp.simplify((8+second)/4)
    assert sp.simplify(curvature-(2-4*b/(1-b))) == 0
    incidence = sp.zeros(4, 4)
    for e, (s, target) in enumerate(edges):
        incidence[s, e], incidence[target, e] = -1, 1
    cycle = sp.Matrix([1, 1, -1, -1])
    assert incidence*cycle == sp.zeros(4, 1)

    lo1, hi1 = bessel_interval(1, F(10))
    lo2, hi2 = bessel_interval(2, F(10))
    assert lo2/hi1 > F(17, 20)
    assert hi2/lo1 < 1
    lower_b = F(3, 4)*F(17, 20)**4
    curvature_upper = 2-4*lower_b/(1-lower_b)
    assert lower_b > F(1, 3) and curvature_upper < 0

    print(json.dumps({
        'scope': 'Exact finite algebra and rational series enclosure; source measure analysis remains written, no Lean proof',
        'python': platform.python_version(), 'sympy': sp.__version__, 'seed': 2026111302,
        'gauge_covariance_cases': gauge_cases, 'finite_mixture_derivative_cases': mixture_cases,
        'cycle_hessian': str(second), 'cycle_unit_curvature': str(curvature),
        'cycle_divergence_zero': True, 'kappa': 10, 'input_coefficient': '3/4',
        'certified_a_lower': '17/20', 'certified_b_lower': str(lower_b),
        'certified_curvature_upper': str(curvature_upper),
        'all_assertions_passed': True,
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
