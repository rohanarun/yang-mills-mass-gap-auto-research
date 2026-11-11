"""Exact finite controls and rational SU(2) coefficient enclosures.

No numerical quadrature, continuum correlation estimate, or Lean replay.
"""
from fractions import Fraction as F
import itertools
import json
import math
from collections import defaultdict


def bessel_interval(order, x, cutoff=40):
    term = (x/2)**order / math.factorial(order)
    total = term
    for k in range(cutoff):
        term *= x*x / (4*(k+1)*(k+order+1))
        total += term
    first_omitted = term*x*x / (4*(cutoff+1)*(cutoff+order+1))
    ratio_bound = x*x / (4*(cutoff+2)*(cutoff+order+2))
    assert 0 <= ratio_bound < 1
    return total, total + first_omitted/(1-ratio_bound)


scale = 10**12
coefficient_bounds = []
for x in map(F, ('1/2', '1', '2', '5', '10')):
    lo1, hi1 = bessel_interval(1, x)
    lo2, hi2 = bessel_interval(2, x)
    lower, upper = lo2/hi1, hi2/lo1
    assert 0 < lower <= upper < 1
    left = lower.numerator*scale // lower.denominator
    right = -((-upper.numerator*scale) // upper.denominator)
    assert F(left, scale) <= lower <= upper <= F(right, scale)
    coefficient_bounds.append({'kappa': str(x), 'lower_numerator': left,
                               'upper_numerator': right, 'denominator': scale})


def multiply(a, b):
    w, x, y, z = a
    v, i, j, k = b
    return (w*v-x*i-y*j-z*k, w*i+x*v+y*k-z*j,
            w*j-x*k+y*v+z*i, w*k+x*j-y*i+z*v)


group = [tuple(sign*int(k == axis) for k in range(4))
         for axis in range(4) for sign in (1, -1)]
identity = group.index((1, 0, 0, 0))
mul = [[group.index(multiply(a, b)) for b in group] for a in group]
inv = [next(b for b in range(8) if mul[a][b] == identity) for a in range(8)]
for a, b, c in itertools.product(range(8), repeat=3):
    assert mul[mul[a][b]][c] == mul[a][mul[b][c]]


def trace(q):
    return group[q][0]


def word(values, orientations):
    product = identity
    for value, orientation in zip(values, orientations):
        product = mul[product][value if orientation == 1 else inv[value]]
    return product


finite_checks = []
for exponential in (F(2), F(3)):
    # Exact Boltzmann weights at kappa=log(exponential), because the trace
    # takes only -1,0,1. exp(-kappa) cancels from the normalized density.
    rational_weights = [exponential**trace(q) for q in range(8)]
    common_denominator = math.lcm(*(v.denominator for v in rational_weights))
    weights = [int(w*common_denominator) for w in rational_weights]
    mass = sum(weights)
    average = [F(sum(weights[q]*group[q][k] for q in range(8)), mass)
               for k in range(4)]
    alpha = average[0]
    assert average[1:] == [0, 0, 0] and 0 < alpha < 1
    for g, q in itertools.product(range(8), repeat=2):
        assert weights[mul[mul[g][q]][inv[g]]] == weights[q]
        assert weights[inv[q]] == weights[q]
    loop_checks = 0
    overlap_variance = None
    loop_distributions = {}
    predictions = [(0, 0, 0, 0), (1, 0, 0, 0), (2, 4, 2, 4), (2, 4, 6, 0)]
    for predicted in predictions:
        for orientations in [(1, 1, 1, 1), (1, -1, 1, -1), (-1, -1, 1, 1)]:
            first = second = 0
            histogram = defaultdict(int)
            for noise in itertools.product(range(8), repeat=4):
                weight = math.prod(weights[q] for q in noise)
                values = [mul[n][q] for n, q in zip(noise, predicted)]
                observable = trace(word(values, orientations))
                first += weight*observable
                second += weight*observable*observable
                histogram[observable] += weight
            mean = F(first, mass**4)
            assert mean == alpha**4*trace(word(predicted, orientations))
            if predicted == (0, 0, 0, 0) and orientations == (1, 1, 1, 1):
                overlap_variance = F(second, mass**4) - mean**2
                assert overlap_variance > 0  # same-loop covariance has noise variance
            if predicted in [(0, 0, 0, 0), (1, 0, 0, 0)] and orientations == (1, 1, 1, 1):
                loop_distributions[trace(word(predicted, orientations))] = {
                    v: F(w, mass**4) for v, w in histogram.items()}
            loop_checks += 1
    # Independent link noises on two disjoint squares, with correlated hidden
    # loop signs. The output distributions above were enumerated directly.
    coupling = F(1, 2)
    joint = defaultdict(F)
    for s, t in itertools.product((-1, 1), repeat=2):
        prior = (1+coupling*s*t)/4
        for x, px in loop_distributions[s].items():
            for y, py in loop_distributions[t].items():
                joint[x, y] += prior*px*py
    assert sum(joint.values()) == 1
    mean_x = sum(p*x for (x, y), p in joint.items())
    mean_y = sum(p*y for (x, y), p in joint.items())
    covariance = sum(p*x*y for (x, y), p in joint.items())-mean_x*mean_y
    assert covariance == coupling*alpha**8 > 0
    # A repeated edge followed by its inverse cancels before integration.
    backtrack = F(sum(weights[n]*trace(mul[n][inv[n]]) for n in range(8)), mass)
    assert backtrack == 1 and backtrack != alpha**2
    repeated_edge = F(sum(weights[n]*trace(mul[n][n]) for n in range(8)), mass)
    assert repeated_edge != alpha**2
    # A reducible representation need not have scalar average. Adding a
    # trivial summand to the fundamental representation gives diag(1,a,a).
    assert alpha != 1
    finite_checks.append({'exp_kappa': str(exponential), 'mean_quaternion_scalar': str(alpha),
                          'edge_distinct_loop_checks': loop_checks,
                          'noise_assignments_per_loop_check': 8**4,
                          'same_loop_conditional_variance': str(overlap_variance),
                          'disjoint_loop_covariance_hidden_coupling_half': str(covariance),
                          'backtracking_trace_mean': str(backtrack),
                          'repeated_edge_square_trace_mean': str(repeated_edge),
                          'incorrect_per_occurrence_factor': str(alpha**2)})

print(json.dumps({'SU2_fundamental_alpha_enclosures': coefficient_bounds,
                  'bessel_last_included_index': 40,
                  'Q8_controls': finite_checks,
                  'scope': 'Rational special-function enclosures and finite-group checks; no Yang--Mills spatial decay.'}, indent=2))
