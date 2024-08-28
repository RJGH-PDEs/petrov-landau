# Import
from weight import *
from scipy.special import genlaguerre


# Play with Laguerre polynomial
def laguerre_example():
    n       = 1
    alpha   = 0.5
    x       = 2

    # Evaluate an associated Laguerre
    print(genlaguerre(n,alpha)(x)) # <-- need to check if it is computing right

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

# The main function
def main():
    l = 3
    k = 2
    r = 1
    # Compute the derivative 
    print('Partial derivative:', Phi_r(l,k,r))


# Main function
if __name__ == "__main__":
    main()
