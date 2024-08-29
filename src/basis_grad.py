# Import
from weight import *
from scipy.special import genlaguerre
from scipy.special import lpmv

# Play with Laguerre polynomial
def laguerre_example():
    """
    Play with laguerre polynomial
    """
    n       = 1
    alpha   = 0.5
    x       = 2

    # Evaluate an associated Laguerre
    print(genlaguerre(n,alpha)(x)) # <-- need to check if it is computing right

# Play with Legendre polynomial 
def legendre_example():
    """
    Play with legendre polynomial
    """
    # Parameters for the polynomial
    m = 0
    l = 2
    x = 0

    # Evaluate a Laguerre polynomial
    print(lpmv(m,l,x))

# Phi(r): the radial part of the test functions
def Phi(l, k, r):
    result  = 0

    # Parametes for the Laguerre
    x       = r**2
    n       = k
    alpha   = l + 1/2

    result = genlaguerre(n, alpha)(x)*(r**(l))

    return result

# Partial derivative w.r.t r
def Phi_r(l, k, r):
    result  = 0
    x       = r**2

    if k != 0:
        # first part
        # parameters
        n       = k - 1
        alpha   = l + 3/2

        result  = (-2)*genlaguerre(n, alpha)(x)
        result  = result*(r**(l+1))

    # second part
    if l==0:
        return result
    else: 
        # parameters
        n       = k 
        alpha   = l + 1/2

        result  = result + (l)*genlaguerre(n, alpha)(x)*(r**(l-1))
    
    # return
    return result 

# Legendre polynomial
def Leg(m, l, t):
    """
    Computes the Laguerre polynomial evaluated
    at x = cos(theta)
    """
    result = 0

    x = np.cos(t)
    result = lpmv(m,l, x)

    return result 

# Derivative of a Leguerre polynomial
def Leg_theta(m, l, t):
    """
    Computes the partial derivative of Leg_{m,l}(cos theta)
    with respect of theta. Used for computing the partial
    derivative of a spherical harmonic. Recursive formula
    not valid for theta equal to multiples of pi

    Parameters:
        - m:    int
        - l:    int
        - t:    float, the angle theta
    """
    result = 0

    # handle the constant case
    if(m == 0 and l == 0):
        return 0

    # Conversion from theta to x
    x = np.cos(t)

    # First part
    result = (-l-1)*lpmv(m, l, x)*x

    # Second part
    result = result + (l + 1 - m)*lpmv(m, l + 1, x)

    # Divide by sin(theta)
    result = result/np.sin(t)

    return result

# The constant for the spherical harmonic
def spher_const(l,m):
    """
    The constant that goes in front of the Legendre polynomial to produce a spherical harmonic.
    """
    result = 0

    result = 2*(l+1)/(4*np.pi)
    if m == 0:
        return np.sqrt(result)

    result = result*np.math.factorial(l-np.ans(m))
    result = result*np.math.factorial(l+np.abs(m))
    return np.sqrt(result)

# The part of the spherical harmonic that depend on phi (the azimuth)
def azimuth(m, p):
    """
    the part of the spherical harmonic that depends on phi.
    It should handle all possible cases wrt m
    """
    if m > 0:
        return np.cos(m*p)
    elif m == 0:
        return 1
    else:
        return np.sin(np.abs(m)*p)

# The derivative of azimuth
def azim_p(m,p):
    if m > 0:
        return (-m)*(np.sin(p))
    elif m == 0:
        return 0
    else:
        return np.abs(m)*np.cos(np.abs(m)*p)

# The main function
def main():
    l = 3
    k = 2
    r = 1
    # Compute the derivative 
    # print('Partial derivative:', Phi_r(l,k,r))

    # Legendre function
    # legendre_example()

    # Partial derivative of the associated legendre
    m       = 2
    l       = 2
    theta   = np.pi/4

    # Compute the derivative 
    print('Partial derivative: ', Leg_theta(m,l,theta))

# Main function
if __name__ == "__main__":
    main()
