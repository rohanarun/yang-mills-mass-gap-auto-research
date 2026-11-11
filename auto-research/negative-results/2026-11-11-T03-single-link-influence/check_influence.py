"""Exact SU(2) Wilson boundary geometry and rational bounds; no gap proof.

The analytic Haar/tilt argument is written in README.md, not executed here.
No Monte Carlo, floating-point quadrature, or proof-kernel replay is used.
"""
import itertools
import json
import math
from fractions import Fraction as Q


def shift(x, axis, side):
    y = list(x)
    y[axis] = (y[axis] + 1) % side
    return tuple(y)


def faces(side, dimension):
    for x in itertools.product(range(side), repeat=dimension):
        for a, b in itertools.combinations(range(dimension), 2):
            yield ((x, a), (shift(x, a, side), b),
                   (shift(x, b, side), a), (x, b))


def check_geometry(side, dimension=4):
    lattice_faces = list(faces(side, dimension))
    rows = []
    for axis in range(dimension):
        e = ((0,) * dimension, axis)
        incident = [p for p in lattice_faces if e in p]
        assert len(incident) == 2 * (dimension - 1)
        staples = [tuple(edge for edge in p if edge != e) for p in incident]
        neighbors = [edge for p in staples for edge in p]
        # Central +/- I assignments make inverse orientation immaterial.
        assert all(len(p) == 3 for p in staples)
        assert len(set(neighbors)) == len(neighbors)
        witnesses = 0
        for f in neighbors:
            target = next(i for i, p in enumerate(staples) if f in p)
            negative = [i for i in range(len(staples)) if i != target][:dimension - 2]
            eta = {edge: 1 for edge in neighbors}
            for i in negative:
                eta[staples[i][0]] = -1
            xi = dict(eta)
            xi[f] *= -1
            assert [edge for edge in neighbors if eta[edge] != xi[edge]] == [f]
            def staple_sum(boundary):
                return sum(math.prod(boundary[edge] for edge in p) for p in staples)
            assert staple_sum(eta) == 2
            assert staple_sum(xi) == 0
            witnesses += 1
        rows.append({'axis': axis, 'incident_faces': len(incident),
                     'distinct_neighbors': len(neighbors), 'boundary_pairs': witnesses})
    return {'side': side, 'dimension': dimension, 'rows': rows}


# cosh(2): terms through n=2, then a geometric upper bound on n>=3.
# For n>=3, t_(n+1)/t_n = 4/((2n+2)(2n+1)) <= 1/14.
prefix = sum((Q(2 ** (2*n), math.factorial(2*n)) for n in range(3)), Q(0))
first_tail = Q(2**6, math.factorial(6))
ratio_bound = Q(4, 8*7)
cosh_upper = prefix + first_tail / (1-ratio_bound)
assert cosh_upper < 4
haar_second_moment = Q(1, 4)  # S^3 coordinate symmetry; written proof in README.
tilted_mean_lower = 2 * haar_second_moment / cosh_upper
influence_lower = tilted_mean_lower / 2
row_lower = 18 * influence_lower
assert influence_lower > Q(1, 16)
assert row_lower > Q(9, 8) > 1
# A per-boundary conditional TV error epsilon loses at most 2 epsilon/pair.
perturbation_radius = Q(1, 288)
assert Q(9, 8) - 2 * 18 * perturbation_radius == 1

print(json.dumps({
    'geometry': [check_geometry(side) for side in (3, 4, 5)],
    'cosh_2_upper': str(cosh_upper),
    'influence_lower_from_written_argument': str(influence_lower),
    'row_lower_from_written_argument': str(row_lower),
    'coarser_strict_row_lower': '9/8',
    'conditional_TV_perturbation_radius': str(perturbation_radius),
    'scope': 'Exact finite geometry and rational arithmetic only; the all-volume SU(2) argument is written, not formalized.'
}, indent=2))
