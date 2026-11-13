"""Finite diagnostics for the written bound; not a Yang--Mills proof or sampler."""

import itertools
import json
import math
import platform


def route_edges(start, end, order):
    point = list(start)
    edges = []
    visited = [tuple(point)]
    for axis in order:
        direction = 1 if end[axis] >= point[axis] else -1
        while point[axis] != end[axis]:
            following = point.copy()
            following[axis] += direction
            # Identify a negative traversal with its positive unoriented edge.
            edges.append((min(tuple(point), tuple(following)), axis))
            point = following
            visited.append(tuple(point))
    assert tuple(point) == end
    return edges, visited


def main():
    points = list(itertools.product(range(-1, 2), repeat=4))
    orders = list(itertools.permutations(range(4)))
    route_count = 0
    for start in points:
        for end in points:
            for order in orders:
                edges, visited = route_edges(start, end, order)
                assert len(edges) == len(set(edges))
                assert len(edges) == sum(abs(a - b) for a, b in zip(start, end))
                assert all(all(-1 <= x <= 1 for x in point) for point in visited)
                route_count += 1

    faces = []
    for radius in range(4):
        count = 0
        for point in itertools.product(range(-radius, radius + 1), repeat=4):
            for i, j in itertools.combinations(range(4), 2):
                if point[i] < radius and point[j] < radius:
                    count += 1
        expected = 6 * (2 * radius) ** 2 * (2 * radius + 1) ** 2
        assert count == expected
        faces.append({"radius": radius, "internal_faces": count})

    caps = []
    # Double-precision diagnostics only; the concavity proof is in the note.
    for delta in (1 / 32, 1 / 16, 1 / 8, 1 / 4, 1 / 2, 1):
        exact_formula = (delta - math.sin(2 * delta) / 2) / math.pi
        lower_bound = 8 * delta ** 3 / (3 * math.pi ** 3)
        assert exact_formula >= lower_bound
        caps.append({"delta": delta, "cap_mass_formula": exact_formula,
                     "lower_bound": lower_bound})

    gibbs_checks = 0
    # Test the sign of beta E[S] <= -log Z on finite nonnegative energies.
    # Uniform finite priors have total mass one, as does the source Haar prior.
    for energies in ((0, 1), (0, 2, 5), (1, 1, 1), (0, 0, 1, 4)):
        for beta in (0.125, 0.5, 1, 4, 16):
            weights = [math.exp(-beta * e) for e in energies]
            z = sum(weights) / len(weights)
            expected_energy = sum(e * w for e, w in zip(energies, weights)) / sum(weights)
            assert beta * expected_energy <= -math.log(z) + 1e-12
            gibbs_checks += 1

    optimizations = []
    for beta in (1, 2, 16, 256, 65536):
        delta = (8 * beta) ** -0.5
        expanded = 8 * delta ** 2 + 2 / (3 * beta) * math.log(3 * math.pi ** 3 / 8) - 2 / beta * math.log(delta)
        formula = (1 + math.log(8 * beta) + 2 / 3 * math.log(3 * math.pi ** 3 / 8)) / beta
        assert math.isclose(expanded, formula, rel_tol=1e-14)
        assert math.isclose(16 * delta, 2 / (beta * delta), rel_tol=1e-14)
        optimizations.append({"beta": beta, "one_plaquette_upper_bound": min(2, formula)})

    print(json.dumps({
        "python": platform.python_version(),
        "scope": "Finite geometry and floating-point scalar diagnostics; no Lean proof, no YM simulation",
        "routes_checked_radius_one": route_count,
        "face_counts": faces,
        "haar_cap_checks": caps,
        "finite_gibbs_convexity_checks": gibbs_checks,
        "optimized_bounds": optimizations,
        "all_assertions_passed": True,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
