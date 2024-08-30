# Import
import numpy as np
from weight import *
from scipy.special import genlaguerre
from scipy.special import lpmv
from scipy.special import factorial

# Play with Laguerre polynomial
def laguerre_example():
    """
    Play with laguerre polynomial
    """
    n       = 1
    alpha   = 0.5
    x       = 2

    # Evaluate an associated Laguerre
    print(genlaguerre(n,alpha)(x)) 

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


# Phi(r): the radial part of the test functions
def Phi(l, k, r):
    """
    radial part of the test functions
    """
    result  = 0

    # Parametes for the Laguerre
    x       = r**2
    n       = k
    alpha   = l + 1/2

    result = genlaguerre(n, alpha)(x)*(r**(l))

    return result

# Legendre polynomial
def Leg(m, l, t):
    """
    Computes the Laguerre polynomial evaluated
    at x = cos(theta)
    """
    result = 0

    x = np.cos(t)
    result = lpmv(np.abs(m), l, x)

    return result 

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

# Test function
def test(m, l, k, r, theta ,phi):
    """
    The test function
    """
    result = 0

    result = azimuth(m, phi)            # azimunth:     phi
    print('azimuth (phi): ', azimuth(m, phi))

    result = result*Leg(m, l, theta)    # Legendre:     theta
    print('Legendre (theta): ', Leg(m, l, theta))

    result = result*Phi(l, k, r)        # Phi:          r
    print('radial: ', Phi(l, k, r))
    
    result = result*spher_const(l, m)   # Constant      
    print('constant: ', spher_const(l,m))

    return result


# The main function
def main():
    # Parameters
    m = 0
    l = 0
    k = 1
    # Coefficients
    r = 3
    phi = np.pi/2
    theta = np.pi/4 

    print('test function: ', test(m, l, k, r, theta, phi))

# Main function
if __name__ == "__main__":
    main()
