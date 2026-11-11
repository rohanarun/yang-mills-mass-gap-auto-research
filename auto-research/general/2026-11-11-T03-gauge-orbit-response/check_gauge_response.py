"""Exact Q8 controls for forest conditioning and non-Abelian loop data.

Finite probability examples only; no SU(2) continuum claim or Lean replay.
"""
import itertools
import json
from collections import defaultdict
from fractions import Fraction


def quaternion_product(a, b):
    w, x, y, z = a
    v, i, j, k = b
    return (w*v-x*i-y*j-z*k, w*i+x*v+y*k-z*j,
            w*j-x*k+y*v+z*i, w*k+x*j-y*i+z*v)


group = [tuple(sign*int(k == axis) for k in range(4))
         for axis in range(4) for sign in (1, -1)]
identity = group.index((1, 0, 0, 0))
mul = [[group.index(quaternion_product(a, b)) for b in group] for a in group]
inv = [next(b for b in range(8) if mul[a][b] == identity
            and mul[b][a] == identity) for a in range(8)]
for a, b, c in itertools.product(range(8), repeat=3):
    assert mul[mul[a][b]][c] == mul[a][mul[b][c]]
assert any(mul[a][b] != mul[b][a] for a, b in itertools.product(range(8), repeat=2))


def holonomy(edges):
    result = identity
    for edge in edges:
        result = mul[result][edge]
    return result


def trace(q):
    # Normalized fundamental SU(2) trace on unit quaternions is the real part.
    return group[q][0]


def transform(edges, gauges):
    return tuple(mul[mul[gauges[e]][edges[e]]][inv[gauges[(e+1) % 3]]]
                 for e in range(3))


triples = list(itertools.product(range(8), repeat=3))
phi = {u: trace(holonomy(u)) for u in triples}
gauge_checks = 0
for u in triples:
    for gauges in triples:
        transformed = transform(u, gauges)
        assert phi[transformed] == phi[u]
        gauge_checks += 1

# Average gauge transformations with root fixed. Tree edges become independent
# uniform variables; the remaining chord becomes the based loop holonomy.
tree_assignment_checks = 0
for u in triples:
    counts = defaultdict(int)
    for g1, g2 in itertools.product(range(8), repeat=2):
        counts[transform(u, (identity, g1, g2))[:2]] += 1
    assert len(counts) == 8**2 and set(counts.values()) == {1}
    # g1=u0 and g2=u0*u1 fix the two tree links to the identity.
    fixed = transform(u, (identity, u[0], mul[u[0]][u[1]]))
    assert fixed[:2] == (identity, identity)
    assert fixed[2] == holonomy(u)
    tree_assignment_checks += len(counts)

assert sum(phi.values()) == 0
second_moment = Fraction(sum(x*x for x in phi.values()), len(triples))
assert second_moment == Fraction(1, 4)

# Two loops have positive gauge-invariant density 1 + c*phi(left)*phi(right).
# Enumerate raw edge assignments; do not generate output from the claimed formula.
results = []
for coupling in (Fraction(1, 2), Fraction(2, 3)):
    num, den = coupling.numerator, coupling.denominator
    mass = defaultdict(int)
    first = defaultdict(int)
    total = mean_left = mean_right = cross = 0
    minimum_weight = den
    for left in triples:
        for right in triples:
            weight = den + num*phi[left]*phi[right]
            minimum_weight = min(minimum_weight, weight)
            mass[right] += weight
            first[right] += weight*phi[left]
            total += weight
            mean_left += weight*phi[left]
            mean_right += weight*phi[right]
            cross += weight*phi[left]*phi[right]
    assert minimum_weight > 0
    assert total == den*8**6 and mean_left == mean_right == 0
    covariance = Fraction(cross, total)
    assert covariance == coupling*second_moment**2
    assignments = 0
    for count in range(3):
        for subset in itertools.combinations(range(3), count):
            marginal_mass = defaultdict(int)
            marginal_first = defaultdict(int)
            for right in triples:
                key = tuple(right[i] for i in subset)
                marginal_mass[key] += mass[right]
                marginal_first[key] += first[right]
            assert len(marginal_mass) == 8**count
            for key in marginal_mass:
                assert marginal_mass[key]*8**count == total
                assert marginal_first[key] == 0
                assignments += 1
    for right in triples:
        assert Fraction(first[right], mass[right]) == coupling*second_moment*phi[right]
    positive = (identity, identity, identity)
    negative = (identity, identity, group.index((-1, 0, 0, 0)))
    conditional_change = (Fraction(first[positive], mass[positive])
                          - Fraction(first[negative], mass[negative]))
    assert conditional_change == coupling/2
    results.append({'coupling': str(coupling), 'raw_configurations': 8**6,
                    'forest_assignments_checked': assignments,
                    'loop_covariance': str(covariance),
                    'cycle_conditionals_checked': len(triples),
                    'one_link_change_with_other_cycle_links_fixed': str(conditional_change)})

# Individual loop traces lose relative non-Abelian orientation.
i = group.index((0, 1, 0, 0))
j = group.index((0, 0, 1, 0))
pair_a, pair_b = (i, i), (i, j)
assert tuple(map(trace, pair_a)) == tuple(map(trace, pair_b))
assert trace(mul[pair_a[0]][pair_a[1]]) != trace(mul[pair_b[0]][pair_b[1]])
orbit_a = {(mul[mul[g][a]][inv[g]], mul[mul[g][b]][inv[g]])
           for g in range(8) for a, b in [pair_a]}
assert pair_b not in orbit_a

print(json.dumps({'group': 'Q8; finite non-Abelian control, not continuum SU(2)',
                  'triangle_gauge_checks': gauge_checks,
                  'root_fixed_tree_assignment_checks': tree_assignment_checks,
                  'normalized_trace_second_moment': str(second_moment),
                  'two_loop_results': results,
                  'equal_individual_traces': list(map(trace, pair_a)),
                  'distinguishing_product_traces': [trace(mul[pair_a[0]][pair_a[1]]),
                                                    trace(mul[pair_b[0]][pair_b[1]])],
                  'scope': 'Exact finite group and probability checks; no spatial decay or mass gap.'}, indent=2))
