from basis_grad import *
from basis import *

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