"""Exact convolution, truncation, and radial-distribution controls.

Written compact-group and source-application arguments are not formalized here.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import comb
import json


def b(n):
    return F(comb(2*n, n), 4**n)


# The single coordinate marginal of the source's four-dimensional Small box
# is uniform on L consecutive integers. Compute its J-fold convolution.
convolutions = []
for length in (3, 5, 7, 9):
    half = length//2
    for rolls in (4, 5, 6):
        counts = {0: 1}
        for _ in range(rolls):
            new = defaultdict(int)
            for x, count in counts.items():
                for step in range(-half, half+1):
                    new[x+step] += count
            counts = new
        residues = [sum(n for x, n in counts.items() if x % length == r)
                    for r in range(length)]
        assert sum(counts.values()) == length**rolls
        assert residues == [length**(rolls-1)]*length
        # Thus the Laurent generating polynomial modulo z^L-1 is a multiple
        # of 1+z+...+z^(L-1), which vanishes at every nontrivial Lth root.
        convolutions.append({'L': length, 'J': rolls, 'coordinate_roll_count': length**rolls,
                             'residue_counts': residues,
                             'four_dimensional_roll_count': length**(4*rolls)})

scalar_checks = 0
for cutoff in map(F, ('1/4','1/2','3/4','1')):
    q = 2*cutoff-cutoff*cutoff
    for radius in sorted(set([F(j,32) for j in range(33)]+[1-cutoff])):
        active = 1-radius < cutoff
        assert not active or radius > 0  # all tested cutoffs <= 1
        for degree in (0,1,2,4,8,16):
            exact = F(1) if active else radius
            approx = (radius*sum(b(n)*(1-radius*radius)**n for n in range(degree+1))
                      if active else radius)
            error = exact-approx
            bound = (1-radius*radius)**(degree+1) if active else F(0)
            assert 0 <= approx <= exact <= 1
            assert 0 <= error <= bound
            if cutoff < 1:
                assert error <= q**(degree+1)
            scalar_checks += 1

# Cutoffs above one activate a zero mean, where every unit vector has the
# same objective value. At c=1 every positive radial mean is active.
assert 1-F(0) < F(5,4)
endpoint_radii = [F(1,2**n) for n in (2,4,8,12)]
assert all(1-r < 1 for r in endpoint_radii)


def radial_error_integral(degree, density_power):
    # density is a*r^(a-1), a=density_power; integrate the polynomial
    # 1 - r*sum b_n*(1-r^2)^n by its monomial coefficients.
    integral = F(1)
    for n in range(degree+1):
        for j in range(n+1):
            integral -= b(n)*(-1)**j*comb(n,j)*F(density_power, density_power+1+2*j)
    return integral


integrated = []
for degree in (0,1,2,4,8,12):
    uniform = radial_error_integral(degree, 1)
    quadratic = radial_error_integral(degree, 2)
    assert uniform == b(degree+1)
    assert quadratic == F(1,2*degree+3)
    assert quadratic <= F(1,degree+1)  # small-ball C=1, alpha=2 bound
    integrated.append({'degree':degree,'uniform_radius_error':str(uniform),
                        'density_2r_error':str(quadratic),
                        'density_2r_small_ball_upper_bound':str(F(1,degree+1))})

print(json.dumps({'convolution_certificates':convolutions,
                  'scalar_remainder_checks':scalar_checks,
                  'cutoff_one_active_radii':[str(r) for r in endpoint_radii],
                  'integrated_radial_controls':integrated,
                  'scope':'Exact finite convolution and rational controls; no actual fine-law small-ball estimate or spatial decay.'},indent=2))
