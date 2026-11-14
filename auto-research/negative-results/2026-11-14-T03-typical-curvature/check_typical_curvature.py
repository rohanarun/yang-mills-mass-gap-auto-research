#!/usr/bin/env python3
"""Typical-configuration Bakry-Emery spectrum of the bare 4D SU(2) Wilson measure.

Weight exp(beta * sum_p Re U_p) = exp(-beta * sum_p price(U_p)) (repository
convention; equals the usual beta_std).  Sampled by Metropolis on an L^4 torus.
For each sampled configuration the matrix 2*I + beta*Hess(sum_p price) (round
unit S^3 per link, Ric = 2) is assembled exactly and its lowest eigenvalues are
found with ARPACK.  Usage:
  python3 check_typical_curvature.py validate
  python3 check_typical_curvature.py run L betas nsamples thermalization gap out.json
Floating point, Monte Carlo; no claim about infinite volume or the continuum.
"""
import itertools, json, sys, time
import numpy as np
from scipy.sparse import coo_matrix, identity
from scipy.sparse.linalg import eigsh
from multiprocessing import Pool

def qmul(a,b):
    a0,a1,a2,a3=np.moveaxis(a,-1,0); b0,b1,b2,b3=np.moveaxis(b,-1,0)
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3,a0*b1+a1*b0+a2*b3-a3*b2,a0*b2-a1*b3+a2*b0+a3*b1,a0*b3+a1*b2-a2*b1+a3*b0],-1)
def qc(a): return a*np.array([1.,-1,-1,-1])
def qexp(v):
    n=np.linalg.norm(v,axis=-1,keepdims=True); s=np.where(n<1e-300,1.0,n)
    return np.concatenate([np.cos(n),np.sin(n)*v/s],-1)
E3=np.eye(4)[1:]

class Lat:
    def __init__(s,d,L):
        s.d,s.L=d,L
        s.sites=list(itertools.product(range(L),repeat=d)); s.sid={t:i for i,t in enumerate(s.sites)}
        s.nl=len(s.sites)*d
        lid=lambda t,mu: s.sid[t]*d+mu
        def sh(t,k):
            t=list(t); t[k]=(t[k]+1)%L; return tuple(t)
        ids=[];sg=[]
        for t in s.sites:
            for mu in range(d):
                for nu in range(mu+1,d):
                    ids.append([lid(t,mu),lid(sh(t,mu),nu),lid(sh(t,nu),mu),lid(t,nu)]); sg.append([1,1,-1,-1])
        s.ids=np.array(ids); s.sg=np.array(sg); s.np_=len(ids)
        s.inc=[[] for _ in range(s.nl)]
        for p in range(s.np_):
            for a in range(4): s.inc[s.ids[p,a]].append((p,a))
    def factors(s,U):
        F=U[s.ids]                                  # (np,4,4)
        return np.where((s.sg>0)[...,None],F,qc(F))
    def plaq(s,U):
        F=s.factors(U); q=qmul(qmul(F[:,0],F[:,1]),qmul(F[:,2],F[:,3])); return q[:,0]
    def hess(s,U):
        F=s.factors(U); n=s.np_
        D=[]
        for a in range(4):
            pos=np.stack([qmul(F[:,a],np.broadcast_to(e,(n,4))) for e in E3],1)       # F e_i
            neg=-np.stack([qmul(np.broadcast_to(e,(n,4)),F[:,a]) for e in E3],1)      # -e_i F
            D.append(np.where((s.sg[:,a]>0)[:,None,None],pos,neg))
        one=np.tile([1.,0,0,0],(n,1))
        pre=[one]
        for a in range(3): pre.append(qmul(pre[-1],F[:,a]))
        post=[None]*4; post[3]=one
        for a in range(2,-1,-1): post[a]=qmul(F[:,a+1],post[a+1])
        P=qmul(qmul(F[:,0],F[:,1]),qmul(F[:,2],F[:,3]))[:,0]
        rows=[];cols=[];vals=[]
        for a in range(4):
            for i in range(3):
                rows.append(3*s.ids[:,a]+i); cols.append(3*s.ids[:,a]+i); vals.append(P)
        for a in range(4):
            for b in range(a+1,4):
                mid=one
                for c in range(a+1,b): mid=qmul(mid,F[:,c])
                X=qmul(qmul(pre[a][:,None,:],D[a]),mid[:,None,:])                      # (n,3,4)
                Y=qmul(D[b],post[b][:,None,:])                                       # (n,3,4)
                R=X[:,:,None,0]*Y[:,None,:,0]-np.einsum('nik,njk->nij',X[:,:,1:],Y[:,:,1:])
                for i in range(3):
                    for j in range(3):
                        r=3*s.ids[:,a]+i; c=3*s.ids[:,b]+j
                        rows+= [r,c]; cols+=[c,r]; vals+=[-R[:,i,j],-R[:,i,j]]
        r=np.concatenate(rows);c=np.concatenate(cols);v=np.concatenate(vals)
        N=3*s.nl
        return coo_matrix((v,(r,c)),shape=(N,N)).tocsr()
    def stap(s,U,l):
        F=s.factors(U); S=np.zeros(4)
        for p,a in s.inc[l]:
            # Re(plaquette) = Re(F_a R) with R the cyclic product of the other three factors
            R=F[p,(a+1)%4]; R=qmul(R,F[p,(a+2)%4]); R=qmul(R,F[p,(a+3)%4])
            S+= R if s.sg[p,a]>0 else qc(R)
        return S

def sweep(lat,U,beta,rng,hits=3):
    for l in rng.permutation(lat.nl):
        S=lat.stap(U,l); k=np.linalg.norm(S)
        sig=min(1.2,1.4/np.sqrt(max(beta*k,0.3)))
        u=U[l]; cur=qmul(u,S)[0]
        for _ in range(hits):
            up=qmul(u,qexp(sig*rng.normal(size=3)))
            new=qmul(up,S)[0]
            if np.log(rng.random())<beta*(new-cur): u,cur=up,new
        U[l]=u/np.linalg.norm(u)

def run(args):
    beta,seed,L,nsamp,therm,gap=args
    rng=np.random.default_rng(seed); lat=Lat(4,L)
    if beta<2.0:
        U=rng.normal(size=(lat.nl,4)); U/=np.linalg.norm(U,axis=1,keepdims=True)
    else: U=np.tile([1.,0,0,0],(lat.nl,1))
    t0=time.time()
    for _ in range(therm): sweep(lat,U,beta,rng)
    out=[]
    for k in range(nsamp):
        for _ in range(gap): sweep(lat,U,beta,rng)
        H=lat.hess(U); BE=2*identity(H.shape[0],format='csr')+beta*H
        w=eigsh(BE,k=6,which='SA',ncv=60,return_eigenvectors=False); w.sort()
        wh=eigsh(H,k=3,which='SA',ncv=60,return_eigenvectors=False); wh.sort()
        out.append({"plaq":float(lat.plaq(U).mean()),"be_lowest":[float(x) for x in w],"hess_lowest":[float(x) for x in wh]})
    return {"beta":beta,"L":L,"seconds":round(time.time()-t0,1),"samples":out}

if __name__=="__main__":
    if sys.argv[1]=="validate":
        rng=np.random.default_rng(1); lat=Lat(3,3)
        U=rng.normal(size=(lat.nl,4)); U/=np.linalg.norm(U,axis=1,keepdims=True)
        H=lat.hess(U).toarray(); worst=0
        ps=lambda V:(1-lat.plaq(V)).sum()
        for _ in range(5):
            xi=rng.normal(size=(lat.nl,3)); f=lambda t:ps(qmul(U,qexp(t*xi)))
            cd=lambda h:(f(h)-2*f(0)+f(-h))/h**2
            fd=(4*cd(1e-3)-cd(2e-3))/3; an=xi.reshape(-1)@H@xi.reshape(-1)
            worst=max(worst,abs(fd-an)/max(1,abs(an)))
        # staple check: plaquette sum = Re(U_l S_l) + rest, compare derivative wrt link scaling
        l=5; S=lat.stap(U,l); base=lat.plaq(U).sum()
        V=U.copy(); V[l]=qmul(U[l],qexp(0.37*np.array([1.,0,0]))); 
        # only the part linear in Re(U_l S_l) changes: difference must equal Re((V_l-U_l) S)
        diff=lat.plaq(V).sum()-base; pred=qmul(V[l]-U[l],S)[0]
        print("hess_fd_worst",worst,"staple_diff",diff,pred)
    else:
        L=int(sys.argv[2]); betas=[float(x) for x in sys.argv[3].split(',')]; ns=int(sys.argv[4])
        with Pool(min(len(betas),12)) as p:
            res=p.map(run,[(b,1000+i,L,ns,int(sys.argv[5]),int(sys.argv[6])) for i,b in enumerate(betas)])
        json.dump(res,open(sys.argv[7],'w'),indent=1)
