"""Exact controls for conditional normalization and local noise.

These finite probability models are not Yang--Mills histories. The source
application and general measure inequalities are written in README.md.
"""
import itertools
import json
from fractions import Fraction as F
import sympy as s

spins = (-1, 1)
a, b, t = s.symbols('a b t', positive=True)
upper = (b-a)/(b+a)
chord = (b**2-t)*(t-a**2)/(t*(b**2-a**2))
residual = s.factor(upper-chord-(t-a*b)**2/(t*(b**2-a**2)))
assert residual == 0  # Inequality uses b>a and t>0 in the written proof.

alpha, q, r = s.symbols('alpha q r', positive=True)
def gas(h, x, y):
    return 1 if h == 0 else alpha*(1+q*x*y)

states = list(itertools.product((0, 1), spins, spins))
z = s.simplify(sum(gas(*state) for state in states)/8)
bad_probability = s.simplify(sum(gas(h,x,y) for h,x,y in states if h == 1)/(8*z))
xy = s.simplify(sum(x*y*gas(h,x,y) for h,x,y in states)/(8*z))
assert z == (1+alpha)/2
assert bad_probability == alpha/(1+alpha)
assert xy == alpha*q/(1+alpha)
for coordinate in (1, 2):
    assert s.simplify(sum(state[coordinate]*gas(*state) for state in states)) == 0
def bad_conditional(x, y):
    return s.simplify(gas(1,x,y)/sum(gas(1,u,y) for u in spins))
bad_tv = s.simplify(bad_conditional(1,1)-bad_conditional(1,-1))
assert bad_tv == q  # q in (0,1); the two differences have opposite signs.
cross_ratio = s.factor(gas(1,1,1)*gas(1,-1,-1)/(gas(1,1,-1)*gas(1,-1,1)))
assert s.simplify(cross_ratio-((1+q)/(1-q))**2) == 0

def latent_density(xs, parameter):
    result = 0
    for latent in spins:
        term = 1
        for x in xs:
            term *= (1+parameter*latent*x)/2
        result += term/2
    return s.factor(result)

joint = {xs: latent_density(xs,r) for xs in itertools.product(spins,repeat=4)}
assert s.simplify(sum(joint.values())-1) == 0
assert s.simplify(sum(xs[0]*p for xs,p in joint.items())) == 0
latent_covariance = s.simplify(sum(xs[0]*xs[1]*p for xs,p in joint.items()))
assert latent_covariance == r**2

def rational_probability(xs, parameter):
    result = F(0)
    for latent in spins:
        term = F(1,2)
        for x in xs:
            term *= (1+parameter*latent*x)/2
        result += term
    return result

def conditional_plus(exterior, parameter):
    plus = rational_probability((1,)+exterior, parameter)
    minus = rational_probability((-1,)+exterior, parameter)
    return plus/(plus+minus)

enumerations = []
for n in (4, 6, 8):
    for parameter in (F(1,5), F(1,2), F(3,4)):
        probabilities = [conditional_plus(ext,parameter)
                         for ext in itertools.product(spins,repeat=n-1)]
        whole_boundary = max(probabilities)-min(probabilities)
        assert whole_boundary <= parameter
        influence = max(abs(conditional_plus((1,)+rest,parameter)
                            -conditional_plus((-1,)+rest,parameter))
                        for rest in itertools.product(spins,repeat=n-2))
        assert influence == parameter**2
        enumerations.append({'sites':n, 'noise_bias':str(parameter),
                             'whole_boundary_TV':str(whole_boundary),
                             'single_neighbor_influence':str(influence),
                             'row_sum':str((n-1)*influence)})

print(json.dumps({
    'sympy_version':s.__version__,
    'parameter_domains':'alpha>0; 0<q,r<1; b>a>0; a^2<=t<=b^2',
    'TV_bound_algebra_residual':str(residual),
    'flag_model_partition':str(z),
    'flag_model_bad_probability':str(bad_probability),
    'flag_model_covariance':str(xy),
    'flag_model_bad_conditional_TV':str(bad_tv),
    'flag_model_cross_ratio':str(cross_ratio),
    'latent_model_covariance':str(latent_covariance),
    'rational_enumerations':enumerations,
    'scope':'Exact finite controls and optimization algebra; no Yang--Mills decay, Lean formalization, or upstream replay.'
},indent=2))
