#!/usr/bin/env python3
"""Bakry-Emery matrix of the gauge QUOTIENT of the bare SU(2) Wilson measure.

Setting.  M = (S^3)^E with the product of round unit metrics, tangent vectors written xi with
V = U exp(xi) (Euclidean in xi, Ric_M = 2).  The gauge group acts by U_e -> g_s U_e g_t^{-1}; the
orbit tangent map is G eps = (Ad(U_e^{-1}) eps_s - eps_t)_e = (G1 - G2) eps.  The quotient B = M/G
carries the pushed-forward measure exp(-beta S) V(b) dvol_B, V = orbit volume ~ det(G^T G)^{1/2}.
For horizontal X (orthogonal to the orbit) the quotient Bakry-Emery quadratic form is

   Ric_B(X,X) + Hess_B(beta S - log V)(X,X)
 = 2|X|^2                                   (Ric_M)
 + X^T Q1 X                                 (- sum_V K_M(X,V), vertical sectional curvatures)
 + X^T Q2 X                                 (+ 3 sum_Y |A_X Y|^2, O'Neill)
 + beta X^T Hess_M S X                      (S gauge invariant: Hess_B S = Hess_M S on horizontals)
 + X^T Hess_M psi X,  psi = -1/2 log det(G^T G)   (-log V, gauge invariant)

with Ric_B(X,X) = Ric_M(X,X) - sum_V K_M(X,V) + 3 sum_Y |A_X Y|^2 (O'Neill, sectional form;
independent of the shape of the fibres).  Closed forms (derivation in the record):

  P = (G^T G)^{-1},  Pi = G P G^T (vertical projector),  Pi_h = I - Pi,
  S1 = G1 P G^T,  N = G1 P G1^T,  M = G P G1^T,  C_i = [e_i]_x (cross-product matrices),
  Q1 = - blockdiag_e ( tr(Pi_ee) I - Pi_ee ),
  Q2 = 3 sum_a B_a^T Pi_h B_a,   B_a = blockdiag_e [c_{a,e}]_x,  c_a = (G1+G2) eps_a,  eps = P^{1/2},
  Hess psi = T1 + T2,
    T1[(e,i),(e,j)] = -2 tr( (C_i C_j + C_j C_i) (S1 - N)_{ee} ),
    T2[(e,i),(f,j)] = 4 tr(C_i M_ef C_j M_fe) - 4 tr(C_i Pi_ef C_j N_fe).

Modes:
  validate  -- (a) Hess psi vs finite differences on a lattice; (b) full quotient Ricci pieces vs an
               independent computation of the Ricci tensor of M/SU(2) for the 1-site 2-link toy,
               obtained from the pushed-forward metric of the invariants (Re a, Re b, Re ab).
  run L betas nsamples therm gap out.json [dim=4]  -- sampled Wilson configurations (needs check_typical_curvature.py).
Floating point; no claim about infinite volume.
"""
import itertools, json, os, sys, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_typical_curvature import Lat, sweep, qmul, qc, qexp

E3 = np.eye(4)[1:]
C = np.zeros((3, 3, 3))                      # C[i] = [e_i]_x  (C[i] v = e_i x v)
for i in range(3):
    for a in range(3):
        for b in range(3):
            C[i, a, b] = np.linalg.det(np.array([np.eye(3)[a], np.eye(3)[i], np.eye(3)[b]]))


def adj_blocks(U):
    """A_e: v -> U^{-1} v U as 3x3 matrices, shape (nl,3,3)."""
    out = np.zeros((len(U), 3, 3))
    for i, e in enumerate(E3):
        v = qmul(qmul(qc(U), np.broadcast_to(e, U.shape)), U)[:, 1:]
        out[:, :, i] = v
    return out


def gauge_G(U, ls, lt, ns):
    nl = len(U)
    A = adj_blocks(U)
    G1 = np.zeros((3*nl, 3*ns)); G2 = np.zeros((3*nl, 3*ns))
    for e in range(nl):
        G1[3*e:3*e+3, 3*ls[e]:3*ls[e]+3] += A[e]
        G2[3*e:3*e+3, 3*lt[e]:3*lt[e]+3] += np.eye(3)
    return G1, G2


def blocks4(Mx):
    n = Mx.shape[0]//3
    return Mx.reshape(n, 3, n, 3)


def psi_value(U, ls, lt, ns):
    G1, G2 = gauge_G(U, ls, lt, ns); G = G1 - G2
    return -0.5*np.linalg.slogdet(G.T @ G)[1]


def quotient_pieces(U, ls, lt, ns):
    """Returns dict of dense matrices (3nl x 3nl): Pi, Q1, Q2, Hpsi, and G."""
    nl = len(U)
    G1, G2 = gauge_G(U, ls, lt, ns); G = G1 - G2; Gp = G1 + G2
    K = G.T @ G; P = np.linalg.inv(K)
    Pi = G @ P @ G.T; Pih = np.eye(3*nl) - Pi
    S1 = G1 @ P @ G.T; N = G1 @ P @ G1.T; Mm = G @ P @ G1.T
    # Q1
    Pi4 = blocks4(Pi); Q1 = np.zeros((3*nl, 3*nl))
    for e in range(nl):
        Pee = Pi4[e, :, e, :]
        Q1[3*e:3*e+3, 3*e:3*e+3] = -(np.trace(Pee)*np.eye(3) - Pee)
    # Q2 = 3 sum_a B_a^T Pih B_a
    w, Vv = np.linalg.eigh(K); eps = (Vv*(w**-0.5)) @ Vv.T         # P^{1/2}
    Pih4 = blocks4(Pih)
    cvec = (Gp @ eps).T.reshape(3*ns, nl, 3)                         # c[a, e, :]
    Cx = np.einsum('aek,kij->aeij', cvec, C)                         # [c_{a,e}]_x   (3ns, nl, 3, 3)
    Q2 = np.zeros((nl, 3, nl, 3))
    for f in range(nl):
        # T[a,e,k,j] = sum_l Pih4[e,k,f,l] Cx[a,f,l,j]
        T = np.einsum('ekl,alj->aekj', Pih4[:, :, f, :], Cx[:, f])
        # Q2[e,i,f,j] += sum_{a,k} Cx[a,e,k,i] T[a,e,k,j]
        Q2[:, :, f, :] += np.einsum('aeki,aekj->eij', Cx, T)
    Q2 = 3*Q2.reshape(3*nl, 3*nl)
    # Hess psi = T1 + T2
    D = S1 - N; D4 = blocks4(D); M4 = blocks4(Mm); N4 = Pi4*0 + blocks4(N); R4 = Pi4
    T1 = np.zeros((3*nl, 3*nl))
    CC = np.einsum('iab,jbc->ijac', C, C); CCs = CC + CC.transpose(1, 0, 2, 3)   # C_i C_j + C_j C_i
    for e in range(nl):
        T1[3*e:3*e+3, 3*e:3*e+3] = -2*np.einsum('ijac,ca->ij', CCs, D4[e, :, e, :])
    Mef = M4.transpose(0, 2, 1, 3); Mfe = Mef.transpose(1, 0, 2, 3)           # [e,f,b,c], [e,f,d,a]=M_fe
    Ref = R4.transpose(0, 2, 1, 3); Nfe = N4.transpose(0, 2, 1, 3).transpose(1, 0, 2, 3)
    t2a = 4*np.einsum('iab,efbc,jcd,efda->efij', C, Mef, C, Mfe, optimize=True)
    t2b = -4*np.einsum('iab,efbc,jcd,efda->efij', C, Ref, C, Nfe, optimize=True)
    T2 = (t2a + t2b).transpose(0, 2, 1, 3).reshape(3*nl, 3*nl)
    Hpsi = T1 + T2
    return {"G": G, "Pi": Pi, "Q1": Q1, "Q2": Q2, "Hpsi": 0.5*(Hpsi + Hpsi.T)}


# ----------------------------------------------------------------------------- validation
def validate_psi():
    rng = np.random.default_rng(3)
    lat = Lat(3, 3); ns = len(lat.sites)
    ls = np.arange(lat.nl)//lat.d
    lt = np.zeros(lat.nl, int)
    for l in range(lat.nl):
        t = list(lat.sites[ls[l]]); t[l % lat.d] = (t[l % lat.d]+1) % lat.L; lt[l] = lat.sid[tuple(t)]
    U = rng.normal(size=(lat.nl, 4)); U /= np.linalg.norm(U, axis=1, keepdims=True)
    H = quotient_pieces(U, ls, lt, ns)["Hpsi"]
    worst = 0.0
    for _ in range(5):
        xi = rng.normal(size=(lat.nl, 3))
        f = lambda t: psi_value(qmul(U, qexp(t*xi)), ls, lt, ns)
        cd = lambda h: (f(h) - 2*f(0) + f(-h))/h**2
        fd = (4*cd(1e-3) - cd(2e-3))/3; an = xi.reshape(-1) @ H @ xi.reshape(-1)
        worst = max(worst, abs(fd - an)/max(1, abs(an)))
    return worst


def validate_A(d=2, L=3, trials=4):
    """A-tensor on a lattice with distinct link endpoints (s != t), by finite differences.

    <A_X Y, V_a> = <nabla_X Y, V_a> for a horizontal FIELD Y(U) = Pi_h(U) eta, with
    nabla_X Y = dY(X) + 1/2 [X, Y] (bi-invariant metric, left trivialization, [X,Y]_e = 2 X_e x Y_e).
    Compared with the closed form  <A_X Y, K_eps> = sum_e (X_e x c_e) . Y_e,  c = (G1+G2) eps.
    """
    rng = np.random.default_rng(21)
    lat = Lat(d, L); ns = len(lat.sites); nl = lat.nl
    ls, lt = lat_maps(lat)
    U = rng.normal(size=(nl, 4)); U /= np.linalg.norm(U, axis=1, keepdims=True)
    def horizontal_projector(V):
        G1, G2 = gauge_G(V, ls, lt, ns); G = G1 - G2
        return np.eye(3*nl) - G @ np.linalg.solve(G.T @ G, G.T)
    G1, G2 = gauge_G(U, ls, lt, ns); G = G1 - G2; Gp = G1 + G2
    Ph = horizontal_projector(U)
    worst_rel = 0.0; worst_abs = 0.0; sizes = []
    for _ in range(trials):
        X = Ph @ rng.normal(size=3*nl); eta = rng.normal(size=3*nl); Y = Ph @ eta
        h = 1e-5
        Vp = qmul(U, qexp(h*X.reshape(nl, 3))); Vm = qmul(U, qexp(-h*X.reshape(nl, 3)))
        dY = (horizontal_projector(Vp) @ eta - horizontal_projector(Vm) @ eta)/(2*h)
        br = np.cross(X.reshape(nl, 3), Y.reshape(nl, 3)).reshape(-1)          # 1/2 [X,Y] = X x Y
        nab = dY + br
        K = G.T @ G; w, Vv = np.linalg.eigh(K); eps = (Vv*(w**-0.5)) @ Vv.T
        Va = G @ eps                                                              # vertical ONB (columns)
        lhs = Va.T @ nab                                                          # <nabla_X Y, V_a>
        c = (Gp @ eps).T.reshape(3*ns, nl, 3)
        rhs = np.array([np.sum(np.cross(X.reshape(nl, 3), c[a]) * Y.reshape(nl, 3)) for a in range(3*ns)])
        worst_abs = max(worst_abs, float(np.abs(lhs - rhs).max())); sizes.append(float(np.abs(rhs).max()))
        worst_rel = max(worst_rel, float(np.linalg.norm(lhs - rhs)/max(np.linalg.norm(rhs), 1e-12)))
    return {"worst_abs_diff": worst_abs, "worst_relative_norm_diff": worst_rel, "typical_size": sizes}


def toy_checks(npoints=6):
    """1 site, 2 links (a,b), gauge = simultaneous conjugation.  Invariants x=Re a, y=Re b, z=Re ab."""
    rng = np.random.default_rng(11)
    ls = np.array([0, 0]); lt = np.array([0, 0]); ns = 1

    def lift(p):
        x, y, z = p
        sa = np.sqrt(1 - x*x); b1 = (x*y - z)/sa; b2 = np.sqrt(1 - y*y - b1*b1)
        return np.array([[x, sa, 0, 0], [y, b1, b2, 0]])

    def grads(U):
        a, b = U
        ga = np.concatenate([-a[1:], np.zeros(3)])
        gb = np.concatenate([np.zeros(3), -b[1:]])
        gz = np.concatenate([-qmul(b, a)[1:], -qmul(a, b)[1:]])
        return np.array([ga, gb, gz])

    def gup(p):                                   # g^{ij} = <grad x^i, grad x^j>
        g = grads(lift(p)); return g @ g.T

    def glow(p): return np.linalg.inv(gup(p))

    def ricci(p, h=1e-3):
        n = 3
        g = glow(p); gi = np.linalg.inv(g)
        d1 = np.zeros((n, n, n)); d2 = np.zeros((n, n, n, n))
        ev = lambda dv: glow(np.array(p) + dv)
        for k in range(n):
            ek = np.eye(n)[k]*h
            d1[k] = (ev(ek) - ev(-ek))/(2*h)
            for l in range(n):
                el = np.eye(n)[l]*h
                d2[k, l] = (ev(ek+el) - ev(ek-el) - ev(-ek+el) + ev(-ek-el))/(4*h*h)
        Gam = 0.5*np.einsum('mn,kij->mkij', gi, np.zeros((n, n, n)))   # placeholder
        # Gamma^m_{ij} = 1/2 g^{mn}(d_i g_jn + d_j g_in - d_n g_ij)
        Gam = 0.5*np.einsum('mn,inj->mij', gi, np.einsum('ijn->inj', d1)*0)  # replaced below
        Gam = np.zeros((n, n, n))
        for m in range(n):
            for i in range(n):
                for j in range(n):
                    Gam[m, i, j] = 0.5*sum(gi[m, q]*(d1[i, j, q] + d1[j, i, q] - d1[q, i, j]) for q in range(n))
        dgi = -np.einsum('ma,kab,bn->kmn', gi, d1, gi)
        dGam = np.zeros((n, n, n, n))                  # d_k Gamma^m_{ij}
        for k in range(n):
            for m in range(n):
                for i in range(n):
                    for j in range(n):
                        dGam[k, m, i, j] = 0.5*sum(
                            dgi[k, m, q]*(d1[i, j, q] + d1[j, i, q] - d1[q, i, j])
                            + gi[m, q]*(d2[k, i, j, q] + d2[k, j, i, q] - d2[k, q, i, j]) for q in range(n))
        Ric = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                Ric[i, j] = (sum(dGam[m, m, i, j] for m in range(n)) - sum(dGam[j, m, i, m] for m in range(n))
                             + sum(Gam[m, m, q]*Gam[q, i, j] for m in range(n) for q in range(n))
                             - sum(Gam[m, j, q]*Gam[q, i, m] for m in range(n) for q in range(n)))
        return Ric

    rows = []
    pts = [(0.3, -0.2, 0.1), (0.1, 0.4, -0.3), (-0.5, 0.2, 0.0), (0.0, 0.0, 0.5), (0.6, 0.5, 0.2), (-0.3, -0.4, 0.1)][:npoints]
    for p in pts:
        U = lift(p); pieces = quotient_pieces(U, ls, lt, ns)
        g = grads(U); gp = g @ g.T; Ric = ricci(p)
        Qtot = 2*np.eye(6) + pieces["Q1"] + pieces["Q2"]
        for i in range(3):
            X = g[i]; v = gp[i]                       # push-forward components v^j = g^{ji}
            ric_num = v @ Ric @ v
            ric_formula = X @ Qtot @ X
            rows.append({"point": p, "dir": i, "Ric_B_numeric": float(ric_num),
                         "Ric_B_formula": float(ric_formula),
                         "abs_diff": float(abs(ric_num - ric_formula)),
                         "Q1_part": float(X @ pieces["Q1"] @ X), "Q2_part": float(X @ pieces["Q2"] @ X),
                         "horizontal_residual": float(np.linalg.norm(pieces["Pi"] @ X))})
    return rows


# ----------------------------------------------------------------------------- run
def lat_maps(lat):
    ls = np.arange(lat.nl)//lat.d; lt = np.zeros(lat.nl, int)
    for l in range(lat.nl):
        t = list(lat.sites[ls[l]]); t[l % lat.d] = (t[l % lat.d]+1) % lat.L; lt[l] = lat.sid[tuple(t)]
    return ls, lt


def analyse(lat, U, beta):
    ls, lt = lat_maps(lat); ns = len(lat.sites); nl = lat.nl
    H = lat.hess(U).toarray()
    q = quotient_pieces(U, ls, lt, ns)
    Qfull, _ = np.linalg.qr(q["G"], mode='complete'); r = 3*ns
    Qh = Qfull[:, r:]
    def low(M, k=3): return [float(x) for x in np.linalg.eigvalsh(Qh.T @ M @ Qh)[:k]]
    I = np.eye(3*nl)
    return {"plaq": float(lat.plaq(U).mean()),
            "compressed": low(2*I + beta*H),
            "plus_vertical_sectional_Q1": low(2*I + beta*H + q["Q1"]),
            "plus_Q1_Q2_oneill": low(2*I + beta*H + q["Q1"] + q["Q2"]),
            "full_quotient": low(2*I + beta*H + q["Q1"] + q["Q2"] + q["Hpsi"]),
            "volume_term_only_added": low(2*I + beta*H + q["Hpsi"]),
            "Q1_range": [float(np.linalg.eigvalsh(Qh.T @ q["Q1"] @ Qh)[0]), float(np.linalg.eigvalsh(Qh.T @ q["Q1"] @ Qh)[-1])],
            "Q2_range": [float(np.linalg.eigvalsh(Qh.T @ q["Q2"] @ Qh)[0]), float(np.linalg.eigvalsh(Qh.T @ q["Q2"] @ Qh)[-1])],
            "Hpsi_range": [float(np.linalg.eigvalsh(Qh.T @ q["Hpsi"] @ Qh)[0]), float(np.linalg.eigvalsh(Qh.T @ q["Hpsi"] @ Qh)[-1])]}


def run(a):
    beta, seed, L, ns_, therm, gap, dim = a
    rng = np.random.default_rng(seed); lat = Lat(dim, L)
    if beta < 2.0:
        U = rng.normal(size=(lat.nl, 4)); U /= np.linalg.norm(U, axis=1, keepdims=True)
    else:
        U = np.tile([1., 0, 0, 0], (lat.nl, 1))
    t0 = time.time()
    for _ in range(therm): sweep(lat, U, beta, rng)
    out = []
    for _ in range(ns_):
        for _ in range(gap): sweep(lat, U, beta, rng)
        out.append(analyse(lat, U, beta))
    return {"beta": beta, "L": L, "seconds": round(time.time()-t0, 1), "samples": out}


if __name__ == "__main__":
    if sys.argv[1] == "validate":
        print("psi_hessian_vs_finite_difference_worst_relative", validate_psi())
        print("A_tensor_lattice_s_ne_t", validate_A())
        rows = toy_checks()
        print("toy_quotient_ricci_worst_abs_diff", max(r["abs_diff"] for r in rows))
        for r in rows[:6]:
            print(r)
    else:
        from multiprocessing import Pool
        L = int(sys.argv[2]); betas = [float(x) for x in sys.argv[3].split(',')]
        with Pool(min(len(betas), 12)) as p:
            dim = int(sys.argv[8]) if len(sys.argv) > 8 else 4
            res = p.map(run, [(b, 1000+i, L, int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), dim) for i, b in enumerate(betas)])
        json.dump(res, open(sys.argv[7], 'w'), indent=1)
