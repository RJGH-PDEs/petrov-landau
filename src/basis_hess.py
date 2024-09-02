from basis_grad import *


# Second derivative of Legendre
def Leg_tt(m, l, t):
    """
    Computes the second derivative of ...
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
    par_result = (-2)*(1+l-m)*par_result

    # Add them
    result = result + par_result
    
    # Scale them
    result = result/(2*np.sin(t)*np.sin(t))
    
    return result

# Second derivative of the radial part
def Phi_rr(l, k, r):
    result = 0
    x = r**2
    
    # Parameters
    n       = k - 2
    alpha   = l + 5/2
    a = 4*(genlaguerre(n, alpha)(x))*r**(4)
    
    # Parameters
    n       = k - 1
    alpha   = l + 3/2
    b = (-2)*(1+2*l)*r**(2)*(genlaguerre(n, alpha)(x))
    
    # Parameters
    n       = k
    alpha   = l + 1/2
    c = (l-1)*l*(genlaguerre(n, alpha)(x))

    # Compute the end result 
    result = (a + b + c)*(r**(l-2)) 
    return result

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
    m       = 4
    l       = 4
    theta   = np.pi/5

    # Compute the derivative 
    print('Partial derivative: ', Leg_tt(m,l,theta))

# Main function
if __name__ == "__main__":
    main()
