"""Exact diagnostics for written identities; no Yang--Mills simulation."""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import importlib.util
import json
import platform
import random
import sympy as sp

helper = Path(__file__).resolve().parent.parent / '2026-11-13-T03-geometric-posterior-curvature/check_geometry.py'
spec = importlib.util.spec_from_file_location('geometry_helpers', helper)
geom = importlib.util.module_from_spec(spec)
spec.loader.exec_module(geom)


def haar_moment(k):
    # Scalar coordinate of uniform S^3: even moment Catalan(k/2)/4^(k/2).
    return sp.S.Zero if k % 2 else sp.Rational(comb(k, k//2), (k//2+1)*4**(k//2))


def haar_integral(poly, variables):
    return sp.expand(sum(coef * sp.prod(haar_moment(k) for k in powers)
                         for powers, coef in sp.Poly(sp.expand(poly), *variables).terms()))


def main():
    b = sp.symbols('b', positive=True)
    moment_cases = 0
    for n in range(1, 7):
        w = sp.symbols('w0:'+str(n))
        density = (sp.prod(1+b*x for x in w)+sp.prod(1-b*x for x in w))/2
        obs = sum(w)/n
        assert haar_integral(density, w) == 1
        assert haar_integral(obs*density, w) == 0
        var = haar_integral(obs**2*density, w)
        energy = haar_integral(sum(4*(1-x*x) for x in w)*density/n**2, w)
        assert sp.simplify(var-(sp.Rational(1, 4*n)+(n-1)*b*b/(16*n))) == 0
        assert energy == sp.Rational(3, n)
        assert sp.simplify(energy/var-48/(4+(n-1)*b*b)) == 0
        if n > 1:
            assert haar_integral(w[0]*w[-1]*density, w) == b*b/16
        moment_cases += 1

    # Actual quaternion derivatives of the plaquette trace, not a substituted formula.
    rng = random.Random(2026111303)
    gradient_cases = 0
    for _ in range(20):
        links = [geom.rational_unit(rng) for _ in range(4)]
        trace = geom.loop(links)
        for e in range(4):
            squared = F(0)
            for axis in range(3):
                unit = tuple(int(j == axis+1) for j in range(4))
                tangents = [None]*4
                tangents[e] = geom.mul(links[e], unit)
                q = (1, 0, 0, 0)
                for k, orientation in enumerate((1, 1, -1, -1)):
                    factor = tangents[k] if k == e else links[k]
                    # Quaternion conjugation is linear, including for a derivative.
                    q = geom.mul(q, factor if orientation == 1 else geom.inv(factor))
                squared += q[0]**2
            assert squared == 1-trace*trace
        gradient_cases += 1

    # Finite Z/3 channel: independent centered noise scores, correlated hidden input.
    covariance_cases = 0
    for d in (2, 3):
        states = list(product(range(3), repeat=d))
        for tilt in (1, 3):
            raw = {q: F(1+tilt*int(len(set(q)) == 1)) for q in states}
            total = sum(raw.values())
            prior = {q: p/total for q, p in raw.items()}
            noise = (F(1, 2), F(1, 4), F(1, 4))
            score = (0, 1, -1)
            ec = [[F(0) for _ in range(d)] for _ in range(d)]
            emm = [[F(0) for _ in range(d)] for _ in range(d)]
            for v in states:
                terms = []
                for q in states:
                    r = tuple((v[i]-q[i]) % 3 for i in range(d))
                    mass = prior[q]
                    for ri in r:
                        mass *= noise[ri]
                    terms.append((mass, tuple(score[ri] for ri in r)))
                pv = sum(p for p, _ in terms)
                means = [sum(p*y[i] for p, y in terms)/pv for i in range(d)]
                for i, j in product(range(d), repeat=2):
                    moment = sum(p*y[i]*y[j] for p, y in terms)/pv
                    ec[i][j] += pv*(moment-means[i]*means[j])
                    emm[i][j] += pv*means[i]*means[j]
            for i, j in product(range(d), repeat=2):
                assert ec[i][j]+emm[i][j] == (F(1, 2) if i == j else 0)
            covariance_cases += 1
    print(json.dumps({'scope':'Exact algebraic diagnostics; continuous SU(2) and source arguments remain written',
        'python':platform.python_version(), 'sympy':sp.__version__, 'seed':2026111303,
        'haar_polynomial_cases':moment_cases, 'quaternion_gradient_cases':gradient_cases,
        'finite_total_covariance_cases':covariance_cases,
        'variance':'1/(4*n)+(n-1)*b^2/(16*n)', 'dirichlet_energy':'3/n',
        'poincare_upper':'48/(4+(n-1)*b^2)', 'separated_loop_covariance':'b^2/16',
        'all_assertions_passed':True}, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
