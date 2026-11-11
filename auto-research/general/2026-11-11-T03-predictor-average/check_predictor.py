"""Exact finite checks for the SU(2) predictor average and masked truncation.

General source application is a written derivation, not executed by this file.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import json


def coefficient(n):
    return F(comb(2*n, n), 4**n)


def amplitude(r, cutoff):
    return F(1) if 1-r < cutoff else r


def truncated(r, cutoff, degree):
    if 1-r >= cutoff:
        return r
    return r*sum(coefficient(n)*(1-r*r)**n for n in range(degree+1))


def multiply(a, b):
    w, x, y, z = a
    v, i, j, k = b
    return (w*v-x*i-y*j-z*k, w*i+x*v+y*k-z*j,
            w*j-x*k+y*v+z*i, w*k+x*j-y*i+z*v)


def conjugate(a):
    return (a[0], -a[1], -a[2], -a[3])


def scale(a, value):
    return tuple(value*x for x in a)


def trace_word(values, orientations):
    result = (F(1), F(0), F(0), F(0))
    for value, orientation in zip(values, orientations):
        result = multiply(result, value if orientation == 1 else conjugate(value))
    return result[0]


scalar_checks = 0
for n in range(32):
    assert 0 < coefficient(n) <= 1
    assert coefficient(n+1) == coefficient(n)*F(2*n+1, 2*n+2)
for cutoff in map(F, ('1/4', '1/2', '3/4')):
    q = 2*cutoff-cutoff*cutoff
    for r in sorted(set([F(k, 20) for k in range(21)]+[1-cutoff])):
        exact = amplitude(r, cutoff)
        assert 0 <= exact <= 1
        assert abs(exact-r) <= cutoff
        for degree in (0, 1, 2, 4, 8, 16):
            approx = truncated(r, cutoff, degree)
            error = exact-approx
            bound = q**(degree+1)/(1-cutoff)
            assert 0 <= approx <= exact <= 1
            assert 0 <= error <= bound
            scalar_checks += 1

# Unit-quaternion connectors with exact rational coordinates. Their average
# is r*q; the best unit quaternion is q. Noncommuting directions are retained.
directions = [(F(0),F(1),F(0),F(0)), (F(0),F(0),F(1),F(0)),
              (F(0),F(0),F(0),F(1)), (F(1),F(0),F(0),F(0))]
radii = list(map(F, ('4/5', '3/5', '12/13', '5/13')))
heights = list(map(F, ('3/5', '4/5', '5/13', '12/13')))
cutoff = F(1,4)
options = []
averages = []
for direction, r, h in zip(directions, radii, heights):
    assert r*r+h*h == 1
    connectors = [multiply(direction, (r, sign*h, F(0), F(0))) for sign in (-1,1)]
    for connector in connectors:
        assert sum(x*x for x in connector) == 1
    mean = tuple(sum(y[k] for y in connectors)/2 for k in range(4))
    assert mean == scale(direction,r)
    best_cost = sum(1-sum(x*y for x,y in zip(connector,direction))
                    for connector in connectors)/2
    assert best_cost == 1-r
    # This checks selected test competitors, not the general minimization proof.
    for competitor in directions+list(map(conjugate,directions)):
        cost = sum(1-sum(x*y for x,y in zip(y0,competitor)) for y0 in connectors)/2
        assert cost >= best_cost
    options.append([direction,direction] if best_cost < cutoff else connectors)
    averages.append(scale(direction,amplitude(r,cutoff)))

loop_results=[]
for orientations in [(1,1,1,1),(1,-1,1,-1),(-1,-1,1,1)]:
    enumerated = sum(trace_word(choice,orientations) for choice in product(*options))/16
    factored = trace_word(averages,orientations)
    assert enumerated == factored
    connector_only = trace_word([scale(q,r) for q,r in zip(directions,radii)],orientations)
    assert abs(enumerated-connector_only) <= len(radii)*cutoff
    errors=[]
    for degree in (0,1,2,4,8):
        approximate = trace_word([scale(q,truncated(r,cutoff,degree))
                                  for q,r in zip(directions,radii)],orientations)
        error=abs(enumerated-approximate)
        bound=len(radii)*(2*cutoff-cutoff*cutoff)**(degree+1)/(1-cutoff)
        assert error<=bound
        errors.append({'degree':degree,'error':str(error),'bound':str(bound)})
    loop_results.append({'orientations':orientations,'exact_mean':str(enumerated),
                         'connector_only_mean':str(connector_only),'truncations':errors})

# Strict threshold: equality uses fallback. Radial points on opposite sides
# approach different limits. This is a moment-map control, not a realization
# of every branch boundary by an actual selected fine-field configuration.
threshold=1-cutoff
assert amplitude(threshold,cutoff)==threshold
jumps=[]
for n in (8,16,32,64):
    low,high=threshold-F(1,n),threshold+F(1,n)
    jump=amplitude(high,cutoff)-amplitude(low,cutoff)
    assert jump==cutoff+F(1,n)
    jumps.append({'n':n,'radial_separation':str(F(2,n)),'mean_separation':str(jump)})

print(json.dumps({'scalar_truncation_checks':scalar_checks,
                  'bond_tag_configurations_per_loop':16,
                  'loop_results':loop_results,
                  'strict_threshold_control':jumps,
                  'scope':'Exact rational finite controls; no spatial covariance estimate or Lean proof.'},indent=2))
