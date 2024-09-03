from basis_grad import *
from basis import *
from basis_hess import *

# w.r.t r
def partial_r(k, l, m, r, t, p):
    result = 0

    # radial part
    result = Phi_r(l, k, r)

    # theta part
    result = result * Leg_t(m, l, t)

    # phi part
    result = result * azim_p(m, p)

    # constant
    result = result * spher_const(l, m)

    return result

# w.r.t. theta
def partial_theta(k, l, m, r, t ,p):
    """
    This function will compute (1/r) f_(theta) where
    f is a basis function. Note that this takes 
    care of the division by r automatically
    """
    result = 0

    # Radial part
    result = Phi_over_r(l, k, r)

    # theta part 
    result = result * Leg_t(m, l, t)

    # phi part
    result = result * azimuth(m, p)

    # Constant
    result = result*spher_const(l, m)

    return result

# w.r.t. phi
def partial_phi(k, l, m, r, t ,p):
    """
    This function will compute (1/r sin(theta)) f_(phi) where
    f is a basis function. Note that this takes 
    care of the division by r automatically
    """
    result = 0

    # Radial part
    result = Phi_over_r(l, k, r)

    # theta part 
    result = result * Leg(m, l, t)

    # phi part
    result = result * azim_p(m, p)

    # Constant
    result = spher_const(l, m)

    # divide by sin(theta)
    result = result/np.sin(t)

    return result

"""
The following are the entries of the hessian matrix 
for out choice of basis

For now this will only be valid for r not zero,
and theta different to multiples of pi
"""

"""
f_{rr}
"""
def h_11(k, l, m, r,t,p):
    result = 0

    # Radial part
    result = Phi_rr(l, k, r)

    # theta part 
    result = result * Leg(m, l, t)

    # phi part
    result = result * azim_p(m, p)

    # Constant
    result = result * spher_const(l, m)
   
    return result

"""
(1/r) f_{r \theta} - (1/r^2) f_{\theta}
"""
def h_12(k, l, m, r,t,p):
    # first term
    a = 0
    a = spher_const(l,m) * Phi_r(l, k, r) * Leg_t(m, l, t) * azimuth(m, p)
    a = a/r
    # second term
    b = 0
    b = spher_const(l, m) * Phi(l, k, r) * Leg_t(m, l, t) * azimuth(m, p)
    b = b/(r*r)

    return a + b

"""
(1/r \sin \theta) f_{\phi r} - (1/r^2 \sin \theta) f_{\phi}
"""
def h_13(k,l,m,r,t,p):
    # first term
    a = 0
    a = spher_const(l,m) * Phi_r(l, k, r) * Leg(m, l, t) * azim_p(m, p)
    a = a/(r*np.sin(t))
    # second term
    b = 0
    b = spher_const(l, m) * Phi(l, k, r) * Leg(m, l, t) * azim_p(m, p)
    b = (-1)*b/(r*r*np.sin(t))

    return a + b

"""
(1/r^2) f_{\theta \theta} + (1/r) f_{r}
"""
def h_22(k,l,m,r,t,p):
    # first term
    a = 0
    a = spher_const(l,m) * Phi(l, k, r) * Leg_tt(m, l, t) * azimuth(m, p)
    a = a/(r*r)
    # second term
    b = 0
    b = spher_const(l, m) * Phi_r(l, k, r) * Leg(m, l, t) * azimuth(m, p)
    b = b/(r)

    return a + b

"""
(1/(r^2 \sin \theta)) f_{\phi \theta} - (\cos \theta)/(r^2 \sin^2 \theta) f_{\phi}
"""
def h_23(k,l,m,r,t,p):
    # first term
    a = 0
    a = spher_const(l,m) * Phi(l, k, r) * Leg_t(m, l, t) * azim_p(m, p)
    a = a/(r*r*np.sin(t))
    # second term
    b = 0
    b = spher_const(l,m) * Phi(l, k, r) * Leg(m, l, t) * azim_p(m, p)
    b = (-1*np.cos(t))*b/(r*r*np.sin(t)*np.sin(t))

    return a + b


"""
(1/(r^2 \sin^2 \theta))f_{\phi \phi} + (1/r) f_{r} + (\cot \theta)/(r^2)f_{\theta}
"""
def h_33(k, l, m, r,t,p):
    # first term
    a = 0
    a = spher_const(l,m) * Phi(l, k, r) * Leg_t(m, l, t) * azim_pp(m, p)
    a = a/(r*r*np.sin(t)*np.sin(t))

    # second term
    b = 0
    b = spher_const(l,m) * Phi_r(l, k, r) * Leg(m, l, t) * azimuth(m, p)
    b = (np.cos(t))*b/(r*r*np.sin(t))

    # third term
    c = 0
    c = spher_const(l,m) * Phi(l, k, r) * Leg_t(m, l, t) * azimuth(m, p)
    c = (np.cos(t))*b/(r*r*np.sin(t))

    return a + b + c

# The main function
def main():
    k = 0
    l = 0
    m = 0

    r = 1 
    t = np.pi/2
    p = 0
    # Compute the derivative 
    print('Partial derivative: 11 ', h_11(k, l, m, r, t, p))
    print('Partial derivative: 12 ', h_12(k, l, m, r, t, p))
    print('Partial derivative: 13 ', h_13(k, l, m, r, t, p))
    print('Partial derivative: 22 ', h_22(k, l, m, r, t, p))
    print('Partial derivative: 23 ', h_23(k, l, m, r, t, p))
    print('Partial derivative: 33 ', h_33(k, l, m, r, t, p))


    # Legendre function
    # legendre_example()

    # Partial derivative of the associated legendre
    m       = 4
    l       = 4
    theta   = np.pi/5

    # Compute the derivative 
    # print('Partial derivative: ', Leg_tt(m,l,theta))    


# Main function
if __name__ == "__main__":
    main()
