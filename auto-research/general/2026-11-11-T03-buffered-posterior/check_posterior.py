"""Exact finite controls for buffered hidden-prediction response.

The source application is written in README.md. No Yang--Mills mixing bound
or Lean proof is executed by this script.
"""
import itertools
import json
from fractions import Fraction as F
import sympy as s

spins = (-1, 1)
c, r = s.symbols('c r', positive=True)
prior = {(u,v): (1+c*u*v)/4 for u,v in itertools.product(spins, repeat=2)}
def channel(x, hidden, bias):
    return (1+bias*x*hidden)/2

def posterior(y):
    unnormalized = {state: p*channel(y,state[1],r) for state,p in prior.items()}
    z = s.factor(sum(unnormalized.values()))
    return {state:s.factor(p/z) for state,p in unnormalized.items()}

plus, minus = posterior(1), posterior(-1)
def expectation(law, f):
    return s.factor(sum(p*f(*state) for state,p in law.items()))

score = lambda u,v: channel(1,u,r)
ratio = lambda u,v: s.factor(channel(-1,v,r)/channel(1,v,r))
ratio_mean = expectation(plus,ratio)
response = s.factor(expectation(minus,score)-expectation(plus,score))
covariance = s.factor(expectation(plus,lambda u,v:score(u,v)*ratio(u,v))
                      -expectation(plus,score)*ratio_mean)
assert s.factor(response-covariance/ratio_mean) == 0
assert response == -c*r**2
assert ratio_mean == 1
for state in prior:
    assert s.factor(minus[state]-plus[state]*ratio(*state)/ratio_mean) == 0

# For 0<c,r<1, posterior change has sign v, and the local marginal change
# has sign u. These formulas compute TV by its maximizing positive set.
global_tv = s.factor(sum(plus[(u,1)]-minus[(u,1)] for u in spins))
local_tv = s.factor(sum(plus[(1,v)]-minus[(1,v)] for v in spins))
assert global_tv == r and local_tv == c*r
alpha = s.factor(plus[(1,1)]
                 -sum(plus[(1,v)] for v in spins)*sum(plus[(u,1)] for u in spins))
assert s.factor(alpha-c*(1-r**2)/4) == 0
ratio_oscillation = s.factor(ratio(1,-1)-ratio(1,1))
assert s.factor(r*ratio_oscillation*alpha/ratio_mean-c*r**2) == 0
assert local_tv.subs(c,0) == 0 and global_tv.subs(c,0) == r

def chain_joint(length, coupling, bias, left, right):
    total = F(0)
    for hidden in itertools.product(spins,repeat=length+1):
        p = F(1,2)
        for i in range(length):
            p *= (1+coupling*hidden[i]*hidden[i+1])/2
        p *= channel(left,hidden[0],bias)*channel(right,hidden[-1],bias)
        # Explicitly integrate all intermediate noisy outputs. They must
        # disappear from the buffered posterior likelihood, not be fixed.
        interior_mass = F(0)
        for observed in itertools.product(spins,repeat=length-1):
            term = F(1)
            for i,x in enumerate(observed,1):
                term *= channel(x,hidden[i],bias)
            interior_mass += term
        assert interior_mass == 1
        total += p*interior_mass
    return total

checks=[]
for length in range(1,6):
    for coupling,bias in [(F(1,3),F(1,2)),(F(2,3),F(3,4))]:
        joint={(x,y):chain_joint(length,coupling,bias,x,y)
               for x,y in itertools.product(spins,repeat=2)}
        assert sum(joint.values()) == 1
        conditional={y:joint[(1,y)]/sum(joint[(x,y)] for x in spins) for y in spins}
        influence=conditional[1]-conditional[-1]
        assert influence == bias**2*coupling**length
        checks.append({'hidden_edges':length,'hidden_coupling':str(coupling),
                       'noise_bias':str(bias),'buffered_influence':str(influence)})

print(json.dumps({
    'sympy_version':s.__version__,
    'symbolic_domain':'0<c,r<1; c=0 used separately for the independent control',
    'posterior_reweighting_mean':str(ratio_mean),
    'response':str(response),
    'covariance_identity_residual':str(s.factor(response-covariance/ratio_mean)),
    'global_hidden_TV':str(global_tv),
    'local_hidden_TV':str(local_tv),
    'posterior_event_mixing_coefficient':str(alpha),
    'layer_cake_bound_residual':str(s.factor(r*ratio_oscillation*alpha/ratio_mean-c*r**2)),
    'buffered_chain_checks':checks,
    'scope':'Exact finite probability controls and algebra; no general posterior mixing theorem or Yang--Mills spatial decay.'
},indent=2))
