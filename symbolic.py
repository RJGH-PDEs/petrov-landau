from sympy import *
import numpy as np

# x
def x(r, t, p):
    return r * np.cos(p) * np.sin(t)

# y
def y(r, t, p):
    return r * np.sin(p) * np.sin(t)

# z - no dependence on phi 
def z(r,t,p):
    return r * np.cos(t)

# relative position vector
def rel_pos(rp, tp, pp, rq, tq, pq):
    u = np.array([x(rp,tp,pp) - x(rq, tq, pq),
                  y(rp,tp,pp) - y(rq, tq, pq),
                  z(rp,tp,pp) - z(rq, tq, pq)])

    return u

# The constant for the spherical harmonic
def spher_const(l,m):
    """
    The constant that goes in front of the Legendre polynomial to produce a spherical harmonic.
    """
    result = 0

    result = (2*l+1)/(2*np.pi)
    if m == 0:
        return np.sqrt(result/2)

    result = result*factorial(l-np.abs(m))
    # print(factorial(l-np.abs(m)))
    result = result/factorial(l+np.abs(m))
    # print(factorial(l+np.abs(m)))
    return np.sqrt(result)

# Computes the weight
def weight(rp, tp, pp, rq, tq, pq):
    # symbols
    r = symbols('r')
    t = symbols('t')
    p = symbols('p')

    # Parameters
    k = 0
    l = 1
    m = -1

    # alpha
    a = 1 + 1/2

    # Spherical harmonic
    sphr = simplify(assoc_legendre(l,abs(m), cos(t)))
    sphr = refine(sphr, Q.positive(sin(t)))

    if m >= 0:
        sphr = sphr*cos(m*p)
    else:
        sphr = sphr*sin(abs(m)*p)

    # Radial part
    radial = 1
    if k > 0:
        radial = assoc_laguerre(k, a, r**2)
    radial = radial*r**l

    # the test function
    f = sphr*radial
    # multiply by constant
    # f = f*spher_const(l,m)

    # print the test function
    print("test function: ", f)

    # compute first partials
    fr = simplify(diff(f, r))
    print("fr: ", fr)
    ft = simplify(diff(f,t)/r)
    print("ft: ", ft)
    fp = simplify(diff(f,p)/(r*sin(t)))
    print("fp: ", fp)

    # basis vectors
    v1 = np.array([sin(t)*cos(p), sin(t)*sin(p), cos(t)])
    v2 = np.array([cos(t)*cos(p), cos(t)*sin(p), -sin(t)])
    v3 = np.array([-sin(p), cos(p), 0 ]) 

    print("v1: ", v1)
    print("v2: ", v2)
    print("v3: ", v3)

    # compute the gradient
    gradient = simplify(fr*v1 + ft*v2 + fp*v3)
    # print it
    print("gradient: ")
    print(gradient)

    # evaluate grad p
    arr = [gradient[0].evalf(subs={r:rp, t:tp, p:pp}), gradient[1].evalf(subs={r:rp, t:tp, p:pp}), gradient[2].evalf(subs={r:rp, t:tp, p:pp})] 
    gradp = np.array(arr)
    print("gradient in p: ", gradp)
    arr = [gradient[0].evalf(subs={r:rq, t:tq, p:pq}), gradient[1].evalf(subs={r:rq, t:tq, p:pq}), gradient[2].evalf(subs={r:rq, t:tq, p:pq})]    
    gradq = np.array(arr)
    print("gradient in q: ", gradq)

    # Difference in gradientsy
    gradDiff = gradp - gradq
    print("Difference in gradient: ", gradDiff)
    # print(gradient.evalf(subs={r:rp, t:tp, p:pp}))


def main():
    rp = 1
    tp = pi/3
    pp = 0

    rq = 2
    tq = 0
    pq = 0

    weight(rp, tp, pp, rq, tq, pq)

if __name__ == '__main__':
    main()