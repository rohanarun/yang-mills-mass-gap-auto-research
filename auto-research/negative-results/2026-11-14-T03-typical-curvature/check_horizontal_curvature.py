#!/usr/bin/env python3
"""Horizontal (gauge-orthogonal) part of the Bakry-Emery matrix of the bare SU(2) Wilson measure.

Imports the sampler and exact Hessian from check_typical_curvature.py (same directory).
Tangent vectors at U are written xi with V = U exp(xi), product metric = Euclidean in xi.
Gauge orbit tangent: eps -> xi_e = Ad(U_e^{-1}) eps_x - eps_{x+mu}.  Horizontal subspace =
orthogonal complement.  Reports, per sample:
  - lowest eigenvalues of the compressed matrix Q_h^T (2I + beta Hess) Q_h,
  - gauge weight ||Q_g^T v||^2 of the lowest eigenvectors of the full matrix.
NOTE: the compressed matrix is NOT the Ricci curvature of the quotient (O'Neill terms and the
orbit-volume weight are not included); it answers only where the negative band lives.
  python3 check_horizontal_curvature.py validate
  python3 check_horizontal_curvature.py run L betas nsamples therm gap out.json
"""
import json, sys, time, os
import numpy as np
from scipy.sparse import identity
from scipy.sparse.linalg import eigsh
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_typical_curvature import Lat, sweep, qmul, qc, qexp

def gauge_map(lat, U):
    d, ns = lat.d, len(lat.sites)
    G = np.zeros((3*lat.nl, 3*ns))
    E = np.eye(4)[1:]
    for l in range(lat.nl):
        s, mu = l//d, l % d
        t = list(lat.sites[s]); t[mu] = (t[mu]+1) % lat.L; s2 = lat.sid[tuple(t)]
        cols = []
        for e in E:
            v = qmul(qmul(qc(U[l]), e), U[l])        # U^{-1} e U
            cols.append(v[1:])
        A = np.array(cols).T                          # 3x3, column i = Ad(U^{-1}) e_i
        G[3*l:3*l+3, 3*s:3*s+3] += A
        G[3*l:3*l+3, 3*s2:3*s2+3] -= np.eye(3)
    return G

def init(L, beta, rng):
    lat = Lat(4, L)
    if beta < 2.0:
        U = rng.normal(size=(lat.nl, 4)); U /= np.linalg.norm(U, axis=1, keepdims=True)
    else:
        U = np.tile([1., 0, 0, 0], (lat.nl, 1))
    return lat, U

def analyse(lat, U, beta):
    H = lat.hess(U); N = H.shape[0]
    BE = (2*identity(N, format='csr') + beta*H)
    G = gauge_map(lat, U)
    Q, _ = np.linalg.qr(G, mode='complete'); ng = G.shape[1]
    # numerical rank check of G (global/stabilizer directions would reduce it)
    sv = np.linalg.svd(G, compute_uv=False); rank = int((sv > 1e-9).sum())
    Qg, Qh = Q[:, :rank], Q[:, rank:]
    BEd = BE.toarray(); Hd = H.toarray()
    wh = np.linalg.eigvalsh(Qh.T @ BEd @ Qh)[:6]
    whh = np.linalg.eigvalsh(Qh.T @ Hd @ Qh)[:3]
    wg = np.linalg.eigvalsh(Qg.T @ BEd @ Qg)[:3]
    w, v = eigsh(BE, k=6, which='SA', ncv=60)
    o = np.argsort(w); w, v = w[o], v[:, o]
    gw = [float(np.sum((Qg.T @ v[:, i])**2)) for i in range(6)]
    return {"be_full_lowest": [float(x) for x in w], "be_horizontal_lowest": [float(x) for x in wh],
            "be_gauge_block_lowest": [float(x) for x in wg], "hess_horizontal_lowest": [float(x) for x in whh],
            "gauge_weight_of_lowest_eigvecs": gw, "gauge_rank": rank, "gauge_dim": ng,
            "plaq": float(lat.plaq(U).mean())}

def run(a):
    beta, seed, L, ns, therm, gap = a
    rng = np.random.default_rng(seed); lat, U = init(L, beta, rng); t0 = time.time()
    for _ in range(therm): sweep(lat, U, beta, rng)
    out = []
    for _ in range(ns):
        for _ in range(gap): sweep(lat, U, beta, rng)
        out.append(analyse(lat, U, beta))
    return {"beta": beta, "L": L, "seconds": round(time.time()-t0, 1), "samples": out}

if __name__ == "__main__":
    if sys.argv[1] == "validate":
        rng = np.random.default_rng(7); lat, U = init(3, 1.0, rng)
        G = gauge_map(lat, U)
        ps = lambda V: (1-lat.plaq(V)).sum()
        worst1 = worst2 = 0.0
        for _ in range(5):
            eps = rng.normal(size=G.shape[1]); xi = (G@eps).reshape(-1, 3)
            f = lambda t: ps(qmul(U, qexp(t*xi)))
            h = 1e-5; d1 = (f(h)-f(-h))/(2*h)
            # finite gauge transformation leaves price invariant exactly
            g = qexp(0.8*rng.normal(size=(len(lat.sites), 3)))
            V = U.copy()
            for l in range(lat.nl):
                s, mu = l//lat.d, l % lat.d
                t = list(lat.sites[s]); t[mu] = (t[mu]+1) % lat.L; s2 = lat.sid[tuple(t)]
                V[l] = qmul(qmul(g[s], U[l]), qc(g[s2]))
            worst1 = max(worst1, abs(d1)); worst2 = max(worst2, abs(ps(V)-ps(U)))
        # tangent-direction check: infinitesimal gauge move equals G eps
        eps = rng.normal(size=G.shape[1]); t = 1e-6
        g = qexp(t*eps.reshape(-1, 3)); V = U.copy()
        for l in range(lat.nl):
            s, mu = l//lat.d, l % lat.d
            tt = list(lat.sites[s]); tt[mu] = (tt[mu]+1) % lat.L; s2 = lat.sid[tuple(tt)]
            V[l] = qmul(qmul(g[s], U[l]), qc(g[s2]))
        xi_true = np.array([qmul(qc(U[l]), V[l])[1:] for l in range(lat.nl)])/t   # U^{-1}V ~ exp(xi)
        err = np.abs(xi_true.reshape(-1) - G@eps).max()
        print("first_derivative_along_gauge", worst1, "finite_gauge_invariance", worst2, "tangent_map_error", err,
              "rank", int((np.linalg.svd(G, compute_uv=False) > 1e-9).sum()), "of", G.shape[1])
    else:
        L = int(sys.argv[2]); betas = [float(x) for x in sys.argv[3].split(',')]
        with Pool(min(len(betas), 12)) as p:
            res = p.map(run, [(b, 1000+i, L, int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])) for i, b in enumerate(betas)])
        json.dump(res, open(sys.argv[7], 'w'), indent=1)
