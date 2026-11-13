"""Exact finite checks for the T01 gap-target specification review.

These checks support the explicit Lorentz boosts used in the written
argument that an energy-slab gap and an invariant-mass gap are equivalent
under the upstream W0 hypotheses. They do NOT verify the measure-theoretic
argument, the upstream Lean source, or any Yang--Mills estimate.

Convention (matches upstream PublicTheory.lean): four real coordinates,
time is the LAST coordinate, minkowskiSquare p = time^2 - |spatial|^2,
forwardCone = {|spatial| <= time}.

Only the Python standard library is used; all arithmetic is exact
(fractions.Fraction). The script exits nonzero on any failure.
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction as Fr

ETA = [[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def transpose(a):
    return [[a[j][i] for j in range(4)] for i in range(4)]


def apply(a, p):
    return [sum(a[i][k] * p[k] for k in range(4)) for i in range(4)]


def det(a):
    # Laplace expansion; exact for Fractions.
    n = len(a)
    if n == 1:
        return a[0][0]
    total = Fr(0)
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in a[1:]]
        total += (-1) ** j * a[0][j] * det(minor)
    return total


def msq(p):
    return p[3] ** 2 - p[0] ** 2 - p[1] ** 2 - p[2] ** 2


def boost(axis, sinh, cosh):
    """Boost along a spatial axis with rational (sinh, cosh), cosh^2 - sinh^2 = 1."""
    assert cosh * cosh - sinh * sinh == 1 and cosh >= 1
    b = [[Fr(int(i == j)) for j in range(4)] for i in range(4)]
    b[axis][axis] = cosh
    b[3][3] = cosh
    b[axis][3] = -sinh
    b[3][axis] = -sinh
    return b


def rotation(i, j, c, s):
    """Rotation in the spatial (i, j) plane with rational (c, s), c^2 + s^2 = 1."""
    assert c * c + s * s == 1
    r = [[Fr(int(a == b)) for b in range(4)] for a in range(4)]
    r[i][i] = c
    r[j][j] = c
    r[i][j] = -s
    r[j][i] = s
    return r


def is_lorentz(a):
    return matmul(matmul(transpose(a), ETA), a) == [[Fr(x) for x in row] for row in ETA]


def is_proper_orthochronous(a):
    return is_lorentz(a) and det(a) == 1 and a[3][3] >= 1


def rapidities():
    # (sinh, cosh) = ((u - 1/u)/2, (u + 1/u)/2) for rational u = e^s > 0.
    out = []
    for u in [Fr(2), Fr(3), Fr(1, 2), Fr(5, 3), Fr(7, 4), Fr(1, 9)]:
        out.append(((u - 1 / u) / 2, (u + 1 / u) / 2))
    return out


def main() -> int:
    report = {"checks": {}, "failures": []}

    def record(name, ok, count):
        report["checks"][name] = {"passed": bool(ok), "cases": count}
        if not ok:
            report["failures"].append(name)

    # 1. Generators and products are proper orthochronous; so are their
    #    Euclidean transposes (the map acting on the spectral variable).
    gens = []
    for axis in range(3):
        for sh, ch in rapidities():
            gens.append(boost(axis, sh, ch))
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        for c, s in [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(-8, 17), Fr(15, 17))]:
            gens.append(rotation(i, j, c, s))
    ok = all(is_proper_orthochronous(g) for g in gens)
    record("generators_proper_orthochronous", ok, len(gens))

    products = [matmul(matmul(a, b), c) for a, b, c in itertools.islice(
        itertools.product(gens[::4], gens[1::5], gens[2::6]), 400)]
    ok = all(is_proper_orthochronous(m) for m in products)
    record("products_proper_orthochronous", ok, len(products))
    ok = all(is_proper_orthochronous(transpose(m)) for m in products)
    record("euclidean_transpose_is_proper_orthochronous", ok, len(products))
    nonsym = sum(1 for m in products if transpose(m) != m)
    record("products_include_nonsymmetric_matrices", nonsym > 0, nonsym)

    # 2. Pairing identity <p, L x>_Euclid = <L^T p, x>_Euclid on samples.
    vecs = [[Fr(a), Fr(b), Fr(c), Fr(d)] for a, b, c, d in
            [(1, 0, 2, 3), (-2, 5, 1, 7), (0, 0, 0, 1), (3, -4, 12, 13), (1, 1, 1, -2)]]
    dot = lambda x, y: sum(a * b for a, b in zip(x, y))
    ok = all(dot(p, apply(m, x)) == dot(apply(transpose(m), p), x)
             for m in products[:60] for p in vecs for x in vecs)
    record("euclidean_pairing_transpose_identity", ok, 60 * len(vecs) ** 2)

    # 3. Timelike orbit: a forward timelike p = boost^{-1}(mu * e_time) has
    #    invariant mass mu; boosting back gives energy exactly mu and zero
    #    momentum. Every point with 0 < mu < m is therefore in an image of
    #    the open slab {0 < time < m}.
    cases = 0
    ok = True
    for mu in [Fr(1, 7), Fr(1, 2), Fr(9, 10), Fr(3), Fr(41, 5)]:
        rest = [Fr(0), Fr(0), Fr(0), mu]
        for m in products[:80]:
            p = apply(m, rest)
            back = apply(_inverse_lorentz(m), p)
            cases += 1
            ok &= msq(p) == mu * mu and p[3] >= mu and back == rest
    record("timelike_orbit_reaches_rest_energy_mu", ok, cases)

    # 4. Lightlike orbit: p = E (n, 1) boosted along n with e^s = u has
    #    energy E / u. For any m > 0 a rational u makes 0 < E/u < m.
    cases = 0
    ok = True
    for axis in range(3):
        for energy in [Fr(1, 3), Fr(1), Fr(250)]:
            p = [Fr(0)] * 4
            p[axis] = energy
            p[3] = energy
            for gap in [Fr(1, 1000), Fr(1, 2), Fr(7)]:
                u = energy / gap * 2 + 1
                b = boost(axis, (u - 1 / u) / 2, (u + 1 / u) / 2)
                q = apply(b, p)
                cases += 1
                ok &= msq(p) == 0 and msq(q) == 0 and q[3] == energy / u
                ok &= 0 < q[3] < gap and is_proper_orthochronous(b)
    record("lightlike_orbit_enters_every_slab", ok, cases)

    # 5. Slab is inside the mass region, and the mass region meets the
    #    forward cone only in points with 0 <= msq < m^2, p != 0 (grid).
    grid = [Fr(k, 4) for k in range(-8, 9)]
    cases = 0
    ok = True
    for gap in [Fr(1, 2), Fr(1), Fr(7, 4)]:
        for t in grid:
            for k1 in grid[::2]:
                for k2 in grid[::4]:
                    p = [k1, k2, Fr(0), t]
                    cases += 1
                    in_slab = 0 < t < gap
                    in_mass = p != [0, 0, 0, 0] and msq(p) < gap * gap
                    if in_slab:
                        ok &= in_mass
                    in_cone = k1 * k1 + k2 * k2 <= t * t and t >= 0
                    if in_cone and in_mass:
                        ok &= 0 <= msq(p) < gap * gap and t > 0
    record("slab_subset_mass_region_grid", ok, cases)

    # 6. Sharpness control: the energy slab alone is NOT boost invariant.
    #    A point at energy exactly m (outside the slab) on the mass shell
    #    mu = m stays outside every boosted slab only because its mass is m;
    #    a point with mass mu < m but energy >= m is outside the slab and is
    #    moved inside by a boost. So Lorentz covariance is a real hypothesis.
    gap = Fr(1)
    mu = Fr(3, 5)
    sh, ch = Fr(4, 3), Fr(5, 3)
    p = apply(boost(0, -sh, ch), [Fr(0), Fr(0), Fr(0), mu])
    ok = p[3] == mu * ch and p[3] >= gap and msq(p) == mu * mu
    q = apply(boost(0, sh, ch), p)
    ok &= q == [Fr(0), Fr(0), Fr(0), mu] and 0 < q[3] < gap
    record("covariance_hypothesis_is_used", ok, 1)

    report["all_passed"] = not report["failures"]
    report["python"] = sys.version.split()[0]
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["all_passed"] else 1


def _inverse_lorentz(a):
    # For a Lorentz matrix, a^{-1} = eta a^T eta.
    eta = [[Fr(x) for x in row] for row in ETA]
    return matmul(matmul(eta, transpose(a)), eta)


if __name__ == "__main__":
    raise SystemExit(main())
