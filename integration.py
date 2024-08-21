# Import 
from sympy import *

def lag_weights_roots(n):
    x = Symbol("x")

    roots = Poly(laguerre(n, x)).all_roots()
    
    x_i = [rt.evalf(20) for rt in roots]
    w_i = [(rt / ((n + 1) * laguerre(n + 1, rt)) ** 2).evalf(20) for rt in roots]
    
    return x_i, w_i

# The function to be integrated
def integrand(x):
    return 1 

# Integration example
def int_example():
    n = 3

    # Extract the weights and the points 
    x, w = lag_weights_roots(n)

    # Partial sum
    s=0

    # Perform the summation 
    for i in range(n):
        # Convert to float
        x[i] = float(x[i])
        w[i] = float(w[i])
        
        # print(w[i])

        # Update the partial sum
        s = s + w[i]*integrand(x[i])

    print(s)

# Perform the example
int_example()