from scipy.special import roots_genlaguerre
from scipy.special import genlaguerre
from pylebedev import PyLebedev

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

# Play with Lebedev integration
def lebedev_integration():
    # build library
    leblib = PyLebedev()
    r,w = leblib.get_points_and_weights(5)

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

# integration
def integration():
    # extract the coefficients
    alpha = 1/2
    r,w_r = roots_genlaguerre(6, alpha, False)

    # build library
    leblib = PyLebedev()
    s,w_spher = leblib.get_points_and_weights(5)

    # now we have both weights and positions, we need to do a tensor product
    sum = 0
    i = 0
    for radial_node in w_r:
        for spherical_node in w_spher:
    
            print(radial_node)
            print(spherical_node)
        # sum = sum + w[i]*integrand(node)
        # i = i + 1

    print("integration result: ", sum)

# The main function
def main():
    integration()

if __name__ == "__main__":
    main()
