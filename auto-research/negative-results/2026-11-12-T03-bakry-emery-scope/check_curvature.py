#!/usr/bin/env python3
"""Bakry-Emery curvature of the bare SU(2) Wilson measure on a periodic torus.

Weight: exp(-beta * sum_p price(U_p)), price(q) = 1 - Re(q), q a unit
quaternion, once per plaquette (repository convention).  Product metric: each
link carries the round unit S^3 (Ric = 2).  Bakry-Emery: if
Ric + beta * Hess(sum_p price) >= rho > 0 everywhere then the Wilson measure
satisfies a Poincare inequality with constant rho for the Laplace-Beltrami
form.  The Hessian is assembled exactly from quaternion algebra and checked
against central finite differences.

Evidence level: numerical observation (floating point, numpy).  Eigenvalue
minima over sampled configurations are LOWER bounds on the true supremum of
-lambda_min; only the analytic bound 4*2*(d-1) is an upper bound.
"""
import itertools
import json
import sys
import time

import numpy as np

RNG = np.random.default_rng(20261112)
IM = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], float)   # i, j, k


def qmul(a, b):
    a0, a1, a2, a3 = np.moveaxis(a, -1, 0)
    b0, b1, b2, b3 = np.moveaxis(b, -1, 0)
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1,
                     a0*b3 + a1*b2 - a2*b1 + a3*b0], -1)


def qinv(a):
    return a*np.array([1, -1, -1, -1])


def qexp(v):
    """exp of imaginary quaternion given as 3-vector."""
    n = np.linalg.norm(v, axis=-1, keepdims=True)
    safe = np.where(n < 1e-300, 1.0, n)
    return np.concatenate([np.cos(n), np.sin(n)*v/safe], -1)


def rand_unit(shape):
    x = RNG.normal(size=shape + (4,))
    return x/np.linalg.norm(x, axis=-1, keepdims=True)


class Torus:
    def __init__(self, d, L):
        self.d, self.L = d, L
        self.sites = list(itertools.product(range(L), repeat=d))
        self.sid = {s: i for i, s in enumerate(self.sites)}
        self.nlinks = len(self.sites)*d
        self.plaq = []                       # list of 4 (link, sign)
        for s in self.sites:
            for mu in range(d):
                for nu in range(mu+1, d):
                    def sh(t, k):
                        t = list(t); t[k] = (t[k]+1) % L; return tuple(t)
                    self.plaq.append([(self.lid(s, mu), +1),
                                      (self.lid(sh(s, mu), nu), +1),
                                      (self.lid(sh(s, nu), mu), -1),
                                      (self.lid(s, nu), -1)])

    def lid(self, s, mu):
        return self.sid[s]*self.d + mu

    def price_sum(self, U):
        tot = 0.0
        for p in self.plaq:
            q = np.array([1.0, 0, 0, 0])
            for l, s in p:
                q = qmul(q, U[l] if s > 0 else qinv(U[l]))
            tot += 1 - q[0]
        return tot

    def hess_price(self, U):
        """Exact Hessian of sum_p price in tangent coordinates U_l exp(xi), xi in R^3."""
        n = 3*self.nlinks
        H = np.zeros((n, n))
        for p in self.plaq:
            F = [U[l] if s > 0 else qinv(U[l]) for l, s in p]
            # derivative quaternion of factor a in direction e_i
            D = []
            for (l, s), f in zip(p, F):
                if s > 0:
                    D.append(np.stack([qmul(f, e) for e in np.eye(4)[1:]]))
                else:
                    D.append(np.stack([-qmul(e, f) for e in np.eye(4)[1:]]))
            # NB for s<0 the factor is (U exp(t xi))^{-1} = exp(-t xi) U^{-1};
            # f above is already U^{-1}, so the derivative is -e f.
            for a in range(4):
                la = p[a][0]
                pre = np.array([1.0, 0, 0, 0])
                for b in range(a):
                    pre = qmul(pre, F[b])
                for b in range(a, 4):
                    if b == a:
                        # diagonal block: second derivative of one factor = -|xi|^2 * factor
                        q = pre
                        for c in range(a, 4):
                            q = qmul(q, F[c])
                        for i in range(3):
                            H[3*la+i, 3*la+i] += q[0]          # price = 1-Re, Hess = +Re(U_p)|xi|^2
                        continue
                    for i in range(3):
                        for j in range(3):
                            q = qmul(pre, D[a][i])
                            for c in range(a+1, b):
                                q = qmul(q, F[c])
                            q = qmul(q, D[b][j])
                            for c in range(b+1, 4):
                                q = qmul(q, F[c])
                            lb = p[b][0]
                            H[3*la+i, 3*lb+j] -= q[0]
                            H[3*lb+j, 3*la+i] -= q[0]
        return H


def fd_hessian_check(T, U, nvec=4, h=1e-4):
    H = T.hess_price(U)
    worst = 0.0
    for _ in range(nvec):
        xi = RNG.normal(size=(T.nlinks, 3))
        def shifted(t):
            V = qmul(U, qexp(t*xi))
            return T.price_sum(V)
        f0, fp, fm = shifted(0.0), shifted(h), shifted(-h)
        fd = (fp - 2*f0 + fm)/h**2
        an = xi.reshape(-1) @ H @ xi.reshape(-1)
        worst = max(worst, abs(fd-an)/max(1.0, abs(an)))
    return worst


def lam_min(T, U):
    return float(np.linalg.eigvalsh(T.hess_price(U))[0])


def search(T, iters, step):
    """Greedy random local search for the most negative lambda_min."""
    best_U, best = None, np.inf
    for start in range(4):
        U = rand_unit((T.nlinks,)) if start else np.tile([1.0, 0, 0, 0], (T.nlinks, 1))
        cur = lam_min(T, U)
        for _ in range(iters):
            l = RNG.integers(T.nlinks)
            V = U.copy()
            V[l] = qmul(U[l], qexp(step*RNG.normal(size=3)))
            val = lam_min(T, V)
            if val < cur:
                U, cur = V, val
        if cur < best:
            best, best_U = cur, U
    return best, best_U


def main():
    out = {"scope": ("numerical observation of Bakry-Emery curvature for the bare SU(2) "
                     "Wilson law on small tori; not a statement about the actual coarse "
                     "measures and not a Hamiltonian gap"), "seed": 20261112, "runs": []}
    for d, L, iters in ((3, 3, 300), (4, 3, 60)):
        t0 = time.time()
        T = Torus(d, L)
        U0 = rand_unit((T.nlinks,))
        fd_err = fd_hessian_check(T, U0)
        ident = np.tile([1.0, 0, 0, 0], (T.nlinks, 1))
        l_id = lam_min(T, ident)
        l_haar = [lam_min(T, rand_unit((T.nlinks,))) for _ in range(8)]
        l_best, U_best = search(T, iters, 0.5)
        analytic = 4*2*(d-1)          # sup |Hess sum_p price| <= (sum|xi_a|)^2 per plaquette
        K = -l_best
        out["runs"].append({
            "d": d, "L": L, "links": T.nlinks, "plaquettes": len(T.plaq),
            "finite_difference_relative_error": fd_err,
            "lambda_min_at_identity": l_id,
            "lambda_min_haar_samples_min": min(l_haar),
            "lambda_min_haar_samples_max": max(l_haar),
            "lambda_min_after_local_search": l_best,
            "analytic_upper_bound_on_minus_lambda_min": analytic,
            "ratio_found_over_analytic": K/analytic,
            "bakry_emery_beta_threshold_from_analytic_bound": 2/analytic,
            "bakry_emery_beta_threshold_if_search_were_sharp": 2/K if K > 0 else None,
            "seconds": round(time.time()-t0, 1)})
        assert fd_err < 1e-5, "Hessian assembly disagrees with finite differences"
        assert l_best >= -analytic - 1e-9, "analytic bound violated"
    out["all_passed"] = True
    json.dump(out, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
