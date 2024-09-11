from scipy.special import roots_genlaguerre
from scipy.special import genlaguerre

# play with Laguerre integration
def genLaguerreInt():
    # extract the coefficients
    n = 4
    alpha = 1/2
    x,w = roots_genlaguerre(n, alpha, False)

    # print the result
    print("Sample points: ")
    print(x)
    print("Weights: ")
    print(w)

    # print the result
    print("")
    print("Access a single point")
    print("Sample point: ")
    print(x[0])
    print("Weights: ")
    print(w[0])

# radial function to be integrated
def integrand(s):
    # parameters
    l = 1
    alpha = l + 1/2
    k = 0

    # compute the result
    result = 0
    x = 2*s
    result = genlaguerre(k, alpha)(x)
    result = result*(s**(l/2))
    result = result*(2**((l+1)/2))
    
    # return 
    # print(result)
    return result     

# 
def integrating_integrand():
    # extract the coefficients
    n = 6
    alpha = 1/2
    x,w = roots_genlaguerre(n, alpha, False)

    sum = 0
    i = 0
    for node in x:
        print(node)
        sum = sum + w[i]*integrand(node)
        i = i + 1

    print("integration result: ", sum)

# The main function
def main():
    integrating_integrand()

if __name__ == "__main__":
    main()
