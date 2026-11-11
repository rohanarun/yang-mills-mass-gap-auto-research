#!/usr/bin/env python3
"""Exact checks for the Peter-Weyl diagonalization of the blocking noise.

Standard library only; all arithmetic is exact rational arithmetic with
outward interval enclosures.  Two kinds of evidence are produced:

A. SU(2) scalar coefficients c_j(kappa) = I_{2j+1}(kappa) / I_1(kappa),
   enclosed twice by independent routes (Bessel power series; semicircle
   moments of Chebyshev characters), plus ordering and power bounds.
B. A finite non-Abelian control on Q_8: the convolution operator is checked
   against its isotypic decomposition for observables that reuse links.

Nothing here bounds a spatial covariance or verifies the upstream source.
"""
import itertools
import json
import sys
from fractions import Fraction as Fr
from math import factorial

FAILURES = []


def check(name, ok):
    if not ok:
        FAILURES.append(name)
    return bool(ok)


# ---------------------------------------------------------------- intervals
class Iv:
    """Closed rational interval [lo, hi]."""

    def __init__(self, lo, hi=None):
        self.lo = Fr(lo)
        self.hi = Fr(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, o):
        o = o if isinstance(o, Iv) else Iv(o)
        return Iv(self.lo + o.lo, self.hi + o.hi)

    def scale(self, c):
        c = Fr(c)
        a, b = c * self.lo, c * self.hi
        return Iv(min(a, b), max(a, b))

    def div_pos(self, o):
        assert self.lo >= 0 and o.lo > 0
        return Iv(self.lo / o.hi, self.hi / o.lo)

    def div(self, o):
        assert o.lo > 0
        cands = [self.lo / o.lo, self.lo / o.hi, self.hi / o.lo, self.hi / o.hi]
        return Iv(min(cands), max(cands))

    def meets(self, o):
        return self.lo <= o.hi and o.lo <= self.hi

    def width(self):
        return self.hi - self.lo

    def dec(self, digits=15):
        return [f"{float(self.lo):.{digits}g}", f"{float(self.hi):.{digits}g}"]


# ------------------------------------------------- A1: Bessel power series
def bessel_iv(n, kappa, terms=60):
    """Enclose I_n(kappa), integer n >= 0, kappa > 0 (DLMF 10.25.2)."""
    half = Fr(kappa) / 2

    def t(k):
        return half ** (2 * k + n) / (factorial(k) * factorial(k + n))

    s = sum(t(k) for k in range(terms + 1))
    q = Fr(kappa) ** 2 / (4 * (terms + 2) * (terms + n + 2))
    assert q < 1
    return Iv(s, s + t(terms + 1) / (1 - q))


def c_bessel(twoj, kappa):
    return bessel_iv(twoj + 1, kappa).div_pos(bessel_iv(1, kappa))


# -------------------------------------- A2: independent moment computation
def semicircle_moment(p):
    """(2/pi) * int_{-1}^{1} x^p sqrt(1-x^2) dx, exactly."""
    if p % 2:
        return Fr(0)
    k = p // 2
    return Fr(factorial(2 * k), factorial(k) * factorial(k + 1) * 4 ** k)


def weighted_moment(p, kappa, terms=160):
    """Enclose (2/pi) int x^p exp(kappa x) sqrt(1-x^2) dx."""
    kappa = Fr(kappa)
    s = sum(kappa ** n / factorial(n) * semicircle_moment(p + n)
            for n in range(terms + 1))
    # |semicircle moments| <= 1, so the tail is at most the exponential tail.
    first = kappa ** (terms + 1) / factorial(terms + 1)
    r = kappa / (terms + 2)
    assert r < 1
    return Iv(s, s + first / (1 - r))


def chebyshev_u(n):
    """Coefficient list (ascending) of U_n; chi_j(x) = U_{2j}(x)."""
    a, b = [Fr(1)], [Fr(0), Fr(2)]
    if n == 0:
        return a
    for _ in range(n - 1):
        nxt = [Fr(0)] + [2 * c for c in b]
        for i, c in enumerate(a):
            nxt[i] -= c
        a, b = b, nxt
    return b


def expect_poly(coeffs, kappa):
    num = Iv(0)
    for p, c in enumerate(coeffs):
        if c:
            num = num + weighted_moment(p, kappa).scale(c)
    return num.div(weighted_moment(0, kappa))


def c_moment(twoj, kappa):
    return expect_poly(chebyshev_u(twoj), kappa).scale(Fr(1, twoj + 1))


def su2_section():
    out = {}
    kappas = [Fr(1, 2), Fr(1), Fr(2), Fr(5), Fr(10), Fr(40)]
    max_twoj = 6
    for kappa in kappas:
        rows = []
        cb = [c_bessel(tj, kappa) for tj in range(max_twoj + 1)]
        cm = [c_moment(tj, kappa) for tj in range(max_twoj + 1)]
        a = cb[1]
        # c_0 = 1 exactly; both enclosures (interval quotients) must contain it.
        ok_c0 = check(f"c0 kappa={kappa}", cb[0].meets(Iv(1))
                      and cm[0].meets(Iv(1)))
        for tj in range(max_twoj + 1):
            agree = check(f"routes agree 2j={tj} kappa={kappa}",
                          cb[tj].meets(cm[tj])
                          and cb[tj].width() < Fr(1, 10 ** 12)
                          and cm[tj].width() < Fr(1, 10 ** 12))
            pos = check(f"positive 2j={tj} kappa={kappa}", cb[tj].lo > 0)
            dec = True if tj == 0 else check(
                f"strictly decreasing 2j={tj} kappa={kappa}",
                cb[tj].hi < cb[tj - 1].lo)
            power = True if tj == 0 else check(
                f"c_j <= a^(2j) 2j={tj} kappa={kappa}",
                cb[tj].hi <= a.lo ** tj if tj > 1 else True)
            rows.append({"two_j": tj, "bessel": cb[tj].dec(),
                         "moments": cm[tj].dec(), "routes_agree": agree,
                         "positive": pos, "below_previous": dec,
                         "at_most_a_power_2j": power})
        # A link traversed twice: (1/2) Tr(g^2) = 2x^2 - 1 = (chi_1 - 1)/2.
        direct = expect_poly([Fr(-1), Fr(0), Fr(2)], kappa)
        predicted = cb[2].scale(3).__add__(Iv(-1)).scale(Fr(1, 2))
        twice_ok = check(f"twice-used link kappa={kappa}",
                         direct.meets(predicted))
        naive = Iv(a.lo ** 2, a.hi ** 2)
        naive_differs = check(f"naive a^2 differs kappa={kappa}",
                              not direct.meets(naive))
        out[str(kappa)] = {
            "c0_is_one": ok_c0,
            "coefficients": rows,
            "twice_used_link": {
                "direct_E[2x^2-1]": direct.dec(),
                "predicted_(3c_1-1)/2": predicted.dec(),
                "agree": twice_ok,
                "naive_a^2": naive.dec(),
                "naive_rule_fails": naive_differs,
            },
        }
    return out


# ------------------------------------------------------- B: Q_8 control
def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
            a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0)


def qinv(a):
    return (a[0], -a[1], -a[2], -a[3])


ONE = (1, 0, 0, 0)
Q8 = [tuple(s if i == k else 0 for i in range(4))
      for k in range(4) for s in (1, -1)]
assert len(set(Q8)) == 8 and all(qmul(a, b) in Q8 for a in Q8 for b in Q8)


def re(a):
    return Fr(a[0])


def sign_char(axis):
    return lambda g: Fr(1) if (g[0] != 0 or g[axis] != 0) else Fr(-1)


# (name, dimension, real character)
IRREPS = [("trivial", 1, lambda g: Fr(1)),
          ("sign_i", 1, sign_char(1)),
          ("sign_j", 1, sign_char(2)),
          ("sign_k", 1, sign_char(3)),
          ("fundamental", 2, lambda g: 2 * re(g))]


def q8_section(w):
    """Noise k(g) proportional to w^{Re g}, i.e. kappa = log w."""
    w = Fr(w)
    raw = {g: w ** g[0] for g in Q8}
    z = sum(raw.values())
    k = {g: raw[g] / z for g in Q8}
    out = {"noise_parameter_exp_kappa": str(w)}

    # Orthogonality and dimension count of the character table used.
    ortho = all(sum(ca(g) * cb(g) for g in Q8) == (8 if ia == ib else 0)
                for ia, (_, _, ca) in enumerate(IRREPS)
                for ib, (_, _, cb) in enumerate(IRREPS))
    out["character_orthogonality"] = check("Q8 characters", ortho and
                                           sum(d * d for _, d, _ in IRREPS) == 8)

    eig = {name: sum(k[g] * ch(g) for g in Q8) / d for name, d, ch in IRREPS}
    out["eigenvalues"] = {n: str(v) for n, v in eig.items()}
    out["eigenvalues_positive_and_below_one"] = check(
        "Q8 eigenvalue range",
        eig["trivial"] == 1 and all(0 < v < 1 for n, v in eig.items()
                                    if n != "trivial"))

    def project(f, slot, irrep):
        """Isotypic projection in argument `slot` of a function on Q8^2."""
        _, d, ch = IRREPS[irrep]

        def pf(q1, q2):
            tot = Fr(0)
            for g in Q8:
                c = ch(qinv(g))
                if c:
                    args = (qmul(g, q1), q2) if slot == 0 else (q1, qmul(g, q2))
                    tot += c * f(*args)
            return tot * d / 8
        return pf

    def transfer_direct(f):
        return {(q1, q2): sum(k[n1] * k[n2] * f(qmul(n1, q1), qmul(n2, q2))
                              for n1 in Q8 for n2 in Q8)
                for q1 in Q8 for q2 in Q8}

    def tabulate(f):
        return {(q1, q2): f(q1, q2) for q1 in Q8 for q2 in Q8}

    h, hp = (0, 1, 0, 0), (0, 0, 1, 0)
    observables = {
        "edge1_twice_edge2_back_and_forth":
            lambda a, b: re(qmul(qmul(a, b), qmul(a, qinv(b)))),
        "edge1_squared": lambda a, b: re(qmul(a, a)),
        "open_path_with_fixed_insertions":
            lambda a, b: re(qmul(qmul(a, h), qmul(b, hp))),
        "commutator": lambda a, b: re(qmul(qmul(a, b), qmul(qinv(a), qinv(b)))),
        "overlapping_product": lambda a, b: re(a) * re(qmul(a, b)),
    }
    results = {}
    for name, f in observables.items():
        table = tabulate(f)
        cached = lambda a, b, t=table: t[(a, b)]
        direct = transfer_direct(cached)
        recon = {key: Fr(0) for key in table}
        predicted = {key: Fr(0) for key in table}
        sectors = {}
        for i1 in range(len(IRREPS)):
            p1 = tabulate(project(cached, 0, i1))
            f1 = lambda a, b, t=p1: t[(a, b)]
            for i2 in range(len(IRREPS)):
                p12 = tabulate(project(f1, 1, i2))
                if any(p12.values()):
                    sectors[f"{IRREPS[i1][0]} x {IRREPS[i2][0]}"] = str(
                        eig[IRREPS[i1][0]] * eig[IRREPS[i2][0]])
                for key, val in p12.items():
                    recon[key] += val
                    predicted[key] += eig[IRREPS[i1][0]] * eig[IRREPS[i2][0]] * val
        results[name] = {
            "completeness": check(f"Q8 completeness {name} w={w}", recon == table),
            "transfer_matches_spectral_formula": check(
                f"Q8 transfer {name} w={w}", predicted == direct),
            "occupied_sectors_and_eigenvalues": sectors,
            "value_at_identity": str(direct[(ONE, ONE)]),
        }
    out["observables"] = results

    # Disjoint links factorize; a shared link leaves a noise covariance.
    fa = tabulate(lambda a, b: re(a))
    fb = tabulate(lambda a, b: re(qmul(b, h)))
    ta = transfer_direct(lambda a, b: fa[(a, b)])
    tb = transfer_direct(lambda a, b: fb[(a, b)])
    tab = transfer_direct(lambda a, b: fa[(a, b)] * fb[(a, b)])
    taa = transfer_direct(lambda a, b: fa[(a, b)] ** 2)
    out["disjoint_links_factorize"] = check(
        f"Q8 factorization w={w}", all(tab[key] == ta[key] * tb[key] for key in tab))
    gap = taa[(ONE, ONE)] - ta[(ONE, ONE)] ** 2
    out["shared_link_noise_covariance_at_identity"] = str(gap)
    check(f"Q8 shared-link covariance w={w}", gap > 0)
    return out


def main():
    report = {
        "scope": ("exact rational enclosures of SU(2) noise eigenvalues and a "
                  "finite Q_8 control; no spatial covariance bound, no upstream "
                  "replay, no Lean proof"),
        "su2": su2_section(),
        "q8": [q8_section(2), q8_section(3)],
        "failures": FAILURES,
        "all_passed": not FAILURES,
    }
    json.dump(report, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0 if not FAILURES else 1


if __name__ == "__main__":
    sys.exit(main())
