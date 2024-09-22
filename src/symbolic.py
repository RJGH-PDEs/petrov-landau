import sympy as sp
import numpy as np
from sympy.physics.quantum import TensorProduct
import math

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

    result = result*math.factorial(l-np.abs(m))
    # print(factorial(l-np.abs(m)))
    result = result/math.factorial(l+np.abs(m))
    # print(factorial(l+np.abs(m)))
    return np.sqrt(result)

# Computes the weight
def weight(k, l, m, rp, tp, pp, rq, tq, pq):
    # symbols
    r = sp.symbols('r')
    t = sp.symbols('t')
    p = sp.symbols('p')

    # alpha
    a = l + 1/2

    # Spherical harmonic
    sphr = sp.simplify(sp.assoc_legendre(l,abs(m), sp.cos(t)))
    sphr = sp.refine(sphr, sp.Q.positive(sp.sin(t)))

    print(sphr)
    if m >= 0:
        sphr = sphr*sp.cos(m*p)
    else:
        sphr = sphr*sp.sin(abs(m)*p)

    # Radial part
    radial = 1
    if k > 0:
        radial = sp.assoc_laguerre(k, a, r**2)
    radial = radial*r**l

    # the test function
    # print("radial: ", radial)
    f = sphr*radial

    # print the test function
    print("test function: ", f)

    # an evaluation of the test function
    # print(f.subs({"r":1}))
    # compute and print relative position
    u = rel_pos(rp, tp, pp, rq, tq, pq)

    # compute first partials
    fr = sp.simplify(sp.diff(f, r))
    # print("fr: ", fr)
    ft = sp.simplify(sp.diff(f,t)/r)
    # print("ft: ", ft)
    fp = sp.simplify(sp.diff(f,p)/(r*sp.sin(t)))
    # print("fp: ", fp)

    # basis vectors
    v1 = sp.Matrix([sp.sin(t)*sp.cos(p), sp.sin(t)*sp.sin(p), sp.cos(t)])
    v2 = sp.Matrix([sp.cos(t)*sp.cos(p), sp.cos(t)*sp.sin(p), -sp.sin(t)])
    v3 = sp.Matrix([-sp.sin(p), sp.cos(p), 0 ]) 

    # print("v1: ", v1)
    # print("v2: ", v2)
    # print("v3: ", v3)

    # compute the gradient
    gradient = sp.simplify(fr*v1 + ft*v2 + fp*v3)
    # print it
    # print("gradient: ")
    # print(gradient)

    # evaluate the gradients
    values_p={"r":rp,"t":tp,"p":pp}
    gradp = gradient.subs(values_p)

    values_q={"r":rq,"t":tq,"p":pq}
    gradq = gradient.subs(values_q)

    # Difference in gradients
    gradDiff = gradp - gradq
    gradDiff = (np.array(gradDiff).astype(np.float64)).ravel() # cast it to numpy 
    # print("Difference in gradient: ", gradDiff)

    # Partial result
    par_result = (-2)*np.dot(gradDiff, u)
    # print("partial result: ", par_result)

    # Now we need to compute the hessian entries
    a11 = sp.simplify(sp.diff(f, r, 2))
    # print("a11: ", a11)
    a12 = sp.simplify(sp.diff(f, t, r)/r - sp.diff(f, t)/(r**2))
    # print("a12: ", a12)
    a13 = sp.simplify(sp.diff(f, p, r)/(r*sp.sin(t)) - sp.diff(f,p)/(r*r*sp.sin(t)))
    # print("a13: ", a13)
    a22 = sp.simplify(sp.diff(f, t, 2)/(r*r) + sp.diff(f, r)/r)
    # print("a22: ", a22)
    a23 = sp.simplify(sp.diff(f, t, p)/(r*r*sp.sin(t)) - sp.cos(t)*sp.diff(f, p)/(r*r*sp.sin(t)*sp.sin(t)))
    # print("a23: ", a23)
    a33 = sp.simplify(sp.diff(f, p, 2)/(r*r*sp.sin(t)*sp.sin(t)) + sp.diff(f, r)/(r) + sp.cos(t)*sp.diff(f,t)/(r*r*sp.sin(t)))
    # print("a33: ", a33)
                
    # compute the tensor products
    m11 = TensorProduct(v1, v1.T)
    m22 = TensorProduct(v2, v2.T)
    m33 = TensorProduct(v3, v3.T)
    m12 = TensorProduct(v1, v2.T)
    m21 = TensorProduct(v2, v1.T)
    m13 = TensorProduct(v1, v3.T)
    m31 = TensorProduct(v3, v1.T)
    m23 = TensorProduct(v2, v3.T)
    m32 = TensorProduct(v3, v2.T)
    
    # compute the hessian
    hess = (a11*m11 + a22*m22 + a33*m33 + a12*(m12 + m21) + a13*(m13 + m31) + a23*(m23 + m32))
    # print(hess)
    hess = sp.simplify(hess)
    # print("hessian ", hess)

    # evaluate the hessian
    hessp = hess.subs(values_p)
    # print("hessian at p: ", hessp)
    hessq = hess.subs(values_q)
    # print("hessian at q: ", hessq)

    # hessian to be contracted
    sumhess = np.array(hessp + hessq).astype(np.float64)
    # projection matrix
    proj = np.dot(u,u)*np.identity(3) - np.outer(u, u)

    # contraction
    # print("matrix to be contracted: ")
    # print(sumhess)
    contraction = np.trace(np.matmul(sumhess, proj))/2
    # print("Contraction: ", contraction)

    # compute the weight
    weight = (par_result + contraction)*spher_const(l, m)
    # print("weight: ", weight)

    return(weight)

def main():
    k = 2
    l = 2
    m = 1

    rp = 1
    tp = np.pi/3
    pp = np.pi/5

    rq = 2
    tq = np.pi/7
    pq = np.pi/4

    print("weight: ", weight(k, l, m, rp, tp, pp, rq, tq, pq))

if __name__ == '__main__':
    main()
