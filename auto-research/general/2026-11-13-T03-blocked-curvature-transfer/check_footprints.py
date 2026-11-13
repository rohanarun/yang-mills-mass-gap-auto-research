"""Exact finite footprint diagnostics; not an analytic proof or YM simulation."""

from fractions import Fraction
from itertools import combinations, product
import json
import platform


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def step(axis, length):
    return tuple(length if k == axis else 0 for k in range(4))


def main():
    rows = []
    for block_side, depth in product((3, 5, 7), (4, 6)):
        radius = (depth + 3) * block_side
        reach = radius + block_side
        coarse_side = (2 * reach + block_side) // block_side
        fine_side = coarse_side * block_side
        assert fine_side >= 2 * reach + 1 and coarse_side >= 3
        checked_points = 0
        for i, j in combinations(range(4), 2):
            origin = (0, 0, 0, 0)
            vi, vj = step(i, block_side), step(j, block_side)
            corners = (origin, vi, vj, add(vi, vj))
            # Cartesian box inclusion is determined by its corners.
            for center in corners:
                for offset in product((-radius, radius), repeat=4):
                    point = add(center, offset)
                    assert all(-reach <= x <= reach for x in point)
                    checked_points += 1
            # Each independent positive link read by the oriented plaquette.
            for base, axis in ((origin, i), (vi, j), (vj, i), (origin, j)):
                for offset in product((-radius, radius), repeat=4):
                    segment = [add(add(base, offset), step(axis, k))
                               for k in range(block_side + 1)]
                    assert len(segment) == len(set(segment))
                    assert all(all(-reach <= x <= reach for x in p) for p in segment)
                    checked_points += len(segment)
        # Check cover coordinates inject into the periodic lattice per axis.
        coordinates = range(-reach, reach + 1)
        assert len({x % fine_side for x in coordinates}) == 2 * reach + 1
        faces = 6 * (2 * reach) ** 2 * (2 * reach + 1) ** 2
        coefficient = (3200 * (2 * reach + 1) * faces) ** 2
        # Two independently expanded versions of the propagated constant.
        assert coefficient == Fraction(1, 2) * 200**2 * (16 * (2 * reach + 1))**2 * 2 * faces**2
        rows.append({"block_side": block_side, "J": depth, "patch_radius": radius,
                     "footprint_radius": reach, "fine_side": fine_side,
                     "points_checked": checked_points, "K_R": coefficient})

    print(json.dumps({"python": platform.python_version(), "cases": rows,
                      "scope": "Finite footprint containment, injectivity, and exact constant arithmetic only",
                      "all_assertions_passed": True}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
