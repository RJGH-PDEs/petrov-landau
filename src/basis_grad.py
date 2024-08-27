# Import
from weight import *
from scipy.special import genlaguerre


# Play with Laguerre polynomial
def laguerre_example():
    n       = 2
    alpha   = 0.5
    x       = 13

    # Evaluate an associated Laguerre
    print(genlaguerre(n,alpha)(x))


# Partial derivative w.r.t r
def Phi_r(l, m, k, r):
    result = 0

    # first part
    # parameters
    n       = k + 1
    alpha   = l + 2/3
    x       = r**2

    result  = (-2)*genlaguerre(n, alpha)(x)
    result  = result*(r**(l+1))

    # second part
    if l==0:
        return result
    else: 
        # parameters
        n       = k 
        alpha   = l + 1/2

        result  = result + genlaguerre(n, alpha)(x)*(r**(l-1))
    
    # return
    return result 

# The main function
def main():
    # First, we define the two points in spherical
    r_p = 100
    t_p = np.pi/2
    p_p = np.pi/8
    
    r_q = 2
    t_q = np.pi/2
    p_q = np.pi/2

    # Compute the weight
    laguerre_example()


# Main function
if __name__ == "__main__":
    main()
