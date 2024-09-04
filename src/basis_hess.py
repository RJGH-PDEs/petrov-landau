from basis_grad import *
from basis import *
from scipy.special import genlaguerre

# Second derivative of Legendre
def Leg_tt(m, l, t):
    """
    Compute the second derivative of ...
    """
    result = 0

    # Handle the l == 0 case 
    if l == 0:
        return 0

    # Compute the position on x
    x = np.cos(t)

    # First part
    result = (l+1)*(3+l+(1+l)*np.cos(2*t))*lpmv(np.abs(m), l, x)

    # Second part
    par_result = 2*(2+l)*x*lpmv(np.abs(m), l+1, x) + (-2 -l + m)*lpmv(np.abs(m), l+2, x)
    par_result = (-2)*(1+l-np.abs(m))*par_result

    # Add them
    result = result + par_result
    
    # Scale them
    result = result/(2*np.sin(t)*np.sin(t))
    
    return result

# Second derivative of the radial part
def Phi_rr(l, k, r):
    """
    Compute the second derivative of...
    """
    result = 0
    x = r**2
    
    if (k >= 2):
        # Parameters
        n       = k - 2
        alpha   = l + 5/2
        result = result + 4*(genlaguerre(n, alpha)(x))*r**(l+2)
    
    if (k >= 1):
        # Parameters
        n       = k - 1
        alpha   = l + 3/2
        result = result + (-2)*(1+2*l)*(genlaguerre(n, alpha)(x))*r**(l)
    
    if (l >= 2):
        # Parameters
        n       = k
        alpha   = l + 1/2
        result = result + (l-1)*l*(genlaguerre(n, alpha)(x))*r**(l-2)

    # Compute the end result 
    return result

# Second derivative of the azimunth part
def azim_pp(m, p):
    """
    Compute the second derivative of...
    """
    if m > 0:
        return (-1)*(m*m)*np.cos(m*p)
    elif np.abs(m) == 0:
        return 0
    else:
        return (-1)*(m*m)*np.sin(np.abs(m)*p)

# The main function
def main():
    l = 0
    k = 1
    r = 1
    # Compute the derivative 
    print('Partial derivative:', Phi_rr(l,k,r))

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
