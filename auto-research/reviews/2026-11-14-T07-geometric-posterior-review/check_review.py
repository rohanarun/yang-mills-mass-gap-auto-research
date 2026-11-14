#!/usr/bin/env python3
"""Independent numerical re-check of four claims about the geometric posterior
Hessian of the generated coarse law (PRs #11 and #12 of this repository).

Written from the README formulas only; the authors' checker scripts were not
read.  numpy only; floating point.  Quaternions are (w, x, y, z); SU(2) = S^3.

C1  Haar cancellation: for one link with Haar prediction, posterior density of
    x = Re(Q^-1 V) is proportional to exp(kappa x) sqrt(1-x^2); then
    E y_j^2 = a/kappa with a = I_2(kappa)/I_1(kappa), so kappa*a - kappa^2*(a/kappa) = 0.
C2  Hessian identity (1):  Hess S_eff(xi,xi) = kappa*sum_e E[x_e]|xi_e|^2
                                             - kappa^2 Var(sum_e y_e . xi_e),
    on a finite latent mixture with several coupled links.
C3  Noise-only counterexample: noise output of rho=(1+c W_p) is 1 + b W_p with
    b = c a^4 (Monte Carlo, plus an exact quadrature of the a^4 factor), and
    S_eff'' along the stated geodesic equals -16 b/(1-b), so the unit-direction
    Bakry-Emery value is 2 - 4b/(1-b).
C4  Non-uniform Poincare: for f_n = 1/2 prod(1+bW_i) + 1/2 prod(1-bW_i) with
    edge-disjoint plaquettes, the test function g = sum_i W_i has Rayleigh
    quotient Var(g)/E|grad g|^2 >= n b^2/64, hence unbounded.
"""
import json
import sys

import numpy as np

RNG = np.random.default_rng(20261114)
OUT = {"scope": ("independent floating-point re-check of formulas in PRs #11 and #12; "
                 "does not check source correspondence, Lean, or physical implications"),
       "seed": 20261114}


def qmul(a, b):
    a0, a1, a2, a3 = np.moveaxis(a, -1, 0)
    b0, b1, b2, b3 = np.moveaxis(b, -1, 0)
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1,
                     a0*b3 + a1*b2 - a2*b1 + a3*b0], -1)


def qconj(a):
    return a*np.array([1.0, -1, -1, -1])


def qexp(v):
    n = np.linalg.norm(v, axis=-1, keepdims=True)
    s = np.where(n < 1e-300, 1.0, n)
    return np.concatenate([np.cos(n), np.sin(n)*v/s], -1)


def runit(shape=()):
    x = RNG.normal(size=tuple(shape) + (4,))
    return x/np.linalg.norm(x, axis=-1, keepdims=True)


def bessel_i(n, k, terms=80):
    from math import factorial
    return sum((k/2)**(2*m+n)/(factorial(m)*factorial(m+n)) for m in range(terms))


def a_of(kappa):
    return bessel_i(2, kappa)/bessel_i(1, kappa)


# ---------------------------------------------------------------- C1
def c1():
    rows = []
    # Gauss-Chebyshev (2nd kind) nodes for weight sqrt(1-x^2)
    n = 400
    j = np.arange(1, n+1)
    x = np.cos(j*np.pi/(n+1))
    w = np.pi/(n+1)*np.sin(j*np.pi/(n+1))**2
    for kappa in (0.5, 1.0, 3.0, 10.0, 40.0):
        dens = np.exp(kappa*(x-1))
        z = (w*dens).sum()
        ex = (w*dens*x).sum()/z
        ey2 = (w*dens*(1-x**2)/3).sum()/z        # E y_j^2 = E[(1-x^2)/3]
        a = a_of(kappa)
        rows.append({"kappa": kappa, "E_x": ex, "a_bessel": a,
                     "E_y_j^2": ey2, "a_over_kappa": a/kappa,
                     "abs_err_Ex": abs(ex-a), "abs_err_Ey2": abs(ey2-a/kappa),
                     "cancellation_residual": kappa*ex - kappa**2*ey2})
    OUT["C1_haar_cancellation"] = rows
    assert all(r["abs_err_Ex"] < 1e-9 and r["abs_err_Ey2"] < 1e-9 for r in rows)


# ---------------------------------------------------------------- C2
def c2():
    M, K, kappa = 3, 9, 1.7
    Q = runit((K, M))
    w = RNG.dirichlet(np.ones(K))

    def S(V):
        # V: (M,4).  Phi = kappa * sum_e (1 - Re(V_e Q_e^{-1}))
        re = qmul(V[None, :, :], qconj(Q))[..., 0]
        phi = kappa*(1 - re).sum(1)
        return -np.log((w*np.exp(-phi)).sum())

    worst = 0.0
    for _ in range(6):
        V = runit((M,))
        xi = RNG.normal(size=(M, 3))
        def at(s):
            return S(qmul(V, qexp(s*xi)))
        def cd(h):
            return (at(h) - 2*at(0.0) + at(-h))/h**2
        # Richardson extrapolation of the O(h^2) central difference.  A first
        # version used plain h = 2e-3 and failed a 1e-5 tolerance; the error
        # then scaled exactly as h^2 (1.9e-4, 4.9e-5, 1.2e-5 for h = 4e-3, 2e-3,
        # 1e-3), i.e. truncation error of the method, not a formula error.
        fd = (4*cd(1e-3) - cd(2e-3))/3
        qi_v = qmul(qconj(Q), V[None])                 # Q^{-1} V = (x, y)
        x_e, y_e = qi_v[..., 0], qi_v[..., 1:]
        phi = kappa*(1 - x_e).sum(1)
        pi = w*np.exp(-phi); pi /= pi.sum()
        t1 = kappa*sum((pi*x_e[:, e]).sum()*np.dot(xi[e], xi[e]) for e in range(M))
        lin = np.einsum('kei,ei->k', y_e, xi)           # sum_e y_e . xi_e per atom
        var = (pi*lin**2).sum() - (pi*lin).sum()**2
        an = t1 - kappa**2*var
        worst = max(worst, abs(fd-an)/max(1.0, abs(an)))
    OUT["C2_hessian_identity"] = {"links": M, "atoms": K, "kappa": kappa,
                                  "worst_relative_error_vs_finite_difference": worst,
                                  "covariance_term_is_nonzero": bool(var > 1e-6)}
    assert worst < 1e-5


# ---------------------------------------------------------------- C3
def sample_noise(kappa, n):
    """Quaternions with Re density ~ exp(kappa x) sqrt(1-x^2), uniform direction."""
    grid = np.linspace(-1, 1, 400001)
    pdf = np.exp(kappa*(grid-1))*np.sqrt(np.maximum(1-grid**2, 0))
    cdf = np.cumsum(pdf); cdf /= cdf[-1]
    x = np.interp(RNG.random(n), cdf, grid)
    d = RNG.normal(size=(n, 3)); d /= np.linalg.norm(d, axis=1, keepdims=True)
    return np.concatenate([x[:, None], np.sqrt(1-x**2)[:, None]*d], 1)


def plaq(V):
    """W_p = Re(V0 V1 V2^{-1} V3^{-1}) for V of shape (..., 4, 4)."""
    q = qmul(qmul(V[..., 0, :], V[..., 1, :]), qconj(V[..., 2, :]))
    return qmul(q, qconj(V[..., 3, :]))[..., 0]


def c3():
    kappa, c = 10.0, 0.75
    a = a_of(kappa)
    b = c*a**4
    # (i) noise output via Monte Carlo at several V; also the exact value
    n = 2_000_000
    rows = []
    for _ in range(3):
        V = runit((4,))
        G = np.stack([sample_noise(kappa, n) for _ in range(4)], 1)      # (n,4,4)
        Qs = qmul(qconj(G), V[None])                                     # Q = G^{-1} V
        f_mc = (1 + c*plaq(Qs)).mean()
        se = (c*plaq(Qs)).std()/np.sqrt(n)
        f_th = 1 + b*plaq(V)
        rows.append({"f_mc": float(f_mc), "f_formula": float(f_th),
                     "abs_diff": abs(float(f_mc-f_th)), "mc_standard_error": float(se)})
    # (ii) geodesic curvature
    V0 = np.array([[-1.0, 0, 0, 0], [1.0, 0, 0, 0], [1.0, 0, 0, 0], [1.0, 0, 0, 0]])
    I = np.array([0.0, 1, 0, 0])[1:]
    xi = np.array([I, I, -I, -I])                  # V0 exp(t i), V1 exp(t i), V2 exp(-t i), V3 exp(-t i)
    S = lambda t: -np.log(1 + b*plaq(qmul(V0, qexp(t*xi))))
    h = 1e-3
    s2 = (S(h) - 2*S(0.0) + S(-h))/h**2
    predicted = -16*b/(1-b)
    unit = np.sum(xi**2)
    out = {"kappa": kappa, "c": c, "a": a, "b": b,
           "noise_output_checks": rows,
           "S_eff_second_derivative_numeric": s2,
           "S_eff_second_derivative_predicted": predicted,
           "tangent_norm_squared": float(unit),
           "unit_direction_BE_value": 2 + s2/unit,
           "formula_2-4b/(1-b)": 2 - 4*b/(1-b),
           "claimed_upper_bound_-223378/389437": -223378/389437,
           "exceeds_claimed_bound": bool(2 - 4*b/(1-b) > -223378/389437)}
    OUT["C3_noise_only_counterexample"] = out
    assert all(r["abs_diff"] < 6*r["mc_standard_error"] + 2e-4 for r in rows)
    assert abs(s2-predicted) < 1e-4*abs(predicted)
    assert not out["exceeds_claimed_bound"]


# ---------------------------------------------------------------- C4
def c4():
    rows = []
    # W_i = Re of a Haar element: density (2/pi) sqrt(1-x^2); mixture sign +/-.
    n_nodes = 600
    j = np.arange(1, n_nodes+1)
    x = np.cos(j*np.pi/(n_nodes+1))
    wq = np.pi/(n_nodes+1)*np.sin(j*np.pi/(n_nodes+1))**2*(2/np.pi)   # sums to 1
    assert abs(wq.sum()-1) < 1e-12
    for b in (0.2, 0.5, 0.9):
        m2 = (wq*x**2).sum()                                   # E_H W^2 = 1/4
        m1p = (wq*x*(1+b*x)).sum()                              # E_+ W = b/4
        v1p = (wq*x**2*(1+b*x)).sum() - m1p**2
        for n in (1, 5, 25, 125, 625):
            mean_plus = n*m1p
            ex2 = n*v1p + mean_plus**2                          # same under the - sign
            var_g = ex2 - 0.0                                   # E g = 0 by symmetry
            # E|grad g|^2 = sum_i E 4(1-W_i^2); under the mixture E W^2 is the same
            en = n*4*(1 - (wq*x**2*(1+b*x)).sum())
            rows.append({"b": b, "n": n, "Var_g": var_g, "Energy": en,
                         "rayleigh": var_g/en, "claimed_lower_bound_n*b^2/64": n*b*b/64,
                         "holds": bool(var_g/en >= n*b*b/64 - 1e-12)})
    OUT["C4_variational_poincare"] = {
        "m2_should_be_0.25": m2, "rows": rows,
        "note": ("exact quadrature, no sampling; gradient energy uses |grad_a W|^2 = 1-W^2 "
                 "per link and disjoint links, which is an assumption of this check")}
    assert all(r["holds"] for r in rows)


def c5():
    """Per-link gradient identity |grad_a W|^2 = 1 - W^2 for W = Re(V0 V1 V2^-1 V3^-1),
    all four orientations, by central finite differences in tangent coordinates."""
    worst = 0.0
    for _ in range(40):
        V = runit((4,))
        W = plaq(V)
        tot = 0.0
        for a in range(4):
            g2 = 0.0
            for k in range(3):
                xi = np.zeros((4, 3)); xi[a, k] = 1.0
                h = 1e-5
                d = (plaq(qmul(V, qexp(h*xi))) - plaq(qmul(V, qexp(-h*xi))))/(2*h)
                g2 += d**2
            worst = max(worst, abs(g2 - (1 - W**2)))
            tot += g2
        worst = max(worst, abs(tot - 4*(1 - W**2)))
    OUT["C5_link_gradient_identity"] = {"samples": 40, "worst_abs_error": worst}
    assert worst < 1e-8


if __name__ == "__main__":
    c1(); c2(); c3(); c4(); c5()
    OUT["all_passed"] = True
    json.dump(OUT, sys.stdout, indent=2)
    print()
