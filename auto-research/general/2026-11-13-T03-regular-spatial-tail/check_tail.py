"""Finite diagnostics for a written source-budget bound; not a Yang--Mills simulation."""
from fractions import Fraction as F
from itertools import product, combinations
import json
import platform
import random


def distance(x, y, n):
    return max(min((a-b) % n, (b-a) % n) for a, b in zip(x, y))


def faces(n):
    for x in product(range(n), repeat=4):
        for i, j in combinations(range(4), 2):
            vertices = []
            for a, b in ((0, 0), (1, 0), (1, 1), (0, 1)):
                z = list(x)
                z[i] = (z[i]+a) % n
                z[j] = (z[j]+b) % n
                vertices.append(tuple(z))
            yield frozenset(vertices)


def main():
    rng = random.Random(2026111304)
    halo_cases = 0
    for n in (3, 4, 5):
        sites = list(product(range(n), repeat=4))
        fs = list(faces(n))
        for _ in range(8):
            support = set(rng.sample(sites, rng.randint(1, 4)))
            inspected = set(support)
            for f in fs:
                if f & support:
                    inspected.update(f)
            # Source proof uses the conservative two-step path bound.
            assert all(min(distance(x, y, n) for y in support) <= 2 for x in inspected)
            halo_cases += 1

    # alpha=4 log 2: the infinite product majorant is ((1+1/2)/(1-1/2))^4=81.
    shell_sums = {}
    for n in range(2, 9):
        sites = product(range(n), repeat=4)
        total = sum((F(1, 2**(4*distance(x, (0,)*4, n))) for x in sites), F(0))
        assert total <= 81
        shell_sums[str(n)] = str(total)

    # Check the algebraic exponent split against independent integer premises.
    split_cases = 0
    for B in (1, 2, 5):
        L = 4*B+2
        for k in range(1, 9):
            for d in range(0, L*k+2*B+5):
                r = rng.randint(0, L*k+2*B+2)
                assert d+r <= 2*L*k+4*B+6
                # For alpha=log 2, s=2 L log 2, this is exactly the exponential comparison.
                assert F(2)**(-2*L*k) <= F(2)**(6+4*B-d-r)
                split_cases += 1

    # Buffer integration of a nearest-neighbour spin chain, all sums exact.
    chain_cases = 0
    for q in (F(1, 5), F(2, 3), F(9, 10)):
        for length in range(2, 9):
            endpoints = {(a, b): F(0) for a, b in product((-1, 1), repeat=2)}
            for spins in product((-1, 1), repeat=length+1):
                weight = F(1, 2)
                for i in range(length):
                    weight *= (1+q*spins[i]*spins[i+1])/2
                endpoints[spins[0], spins[-1]] += weight
            for (a, b), value in endpoints.items():
                assert value == (1+q**length*a*b)/4
            covariance = sum(a*b*value for (a, b), value in endpoints.items())
            assert covariance == q**length
            # No local edge term sees both endpoints for length>=2.
            assert all(not {0, length}.issubset({i, i+1}) for i in range(length))
            chain_cases += 1
    print(json.dumps({'scope':'Finite halo/geometry and exact chain controls; all-volume source estimate remains written',
        'python':platform.python_version(), 'seed':2026111304,
        'flag_halo_cases':halo_cases, 'torus_sum_cases':len(shell_sums),
        'exponent_split_cases':split_cases, 'buffer_chain_cases':chain_cases,
        'torus_sums_at_alpha_4_log_2':shell_sums, 'all_assertions_passed':True},indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
