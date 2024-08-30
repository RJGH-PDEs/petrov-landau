from basis import *

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

# Derivative of a Leguerre polynomial
def Leg_t(m, l, t):
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
    result = (-l-1)*lpmv(np.abs(m), l, x)*x

    # Second part
    result = result + (l + 1 - m)*lpmv(np.abs(m), l + 1, x)

    # Divide by sin(theta)
    result = result/np.sin(t)

    return result

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
    print('Partial derivative: ', Leg_t(m,l,theta))

# Main function
if __name__ == "__main__":
    main()
