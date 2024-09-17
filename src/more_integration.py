import numpy as np
from scipy.special import roots_genlaguerre
from scipy.special import genlaguerre
from pylebedev import PyLebedev

def theta(x, y, z):
    return np.acos(z/np.sqrt(x**2+ y**2 + z**2))

def phi(x, y):
    if x == 0 and y == 0: return 0
    return (np.sign(y))*np.acos(x/np.sqrt(x**2 + y**2))

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
    r,w = leblib.get_points_and_weights(3)

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

# spherical function to be integrated against a Gaussian
def f(r, t, p):
    return (r*np.cos(t))**4

# spherical function that is actually sampled
def g(x, t, p):
    r = np.sqrt(2 * x)
    return np.sqrt(2)*f(r, t, p)

# integration
def integration():
    # extract the coefficients
    n_laguerre = 5
    alpha = 1/2
    x,w_r = roots_genlaguerre(n_laguerre, alpha, False)
    print(w_r)

    # build library
    n_lebedev = 5
    leblib = PyLebedev()
    s,w_spher = leblib.get_points_and_weights(n_lebedev)
    print(w_spher)

    # now we have both weights and positions, we need to do a tensor product
    sum = 0

    # radial counter
    i = 0
    for radial_weight in w_r:
        # spherical counter
        j = 0
        for spherical_weight in w_spher:
            print("")
            # print the weights
            print("i ", i, " j ", j)
            print("radial weight: ", radial_weight, "spherical weight: ", spherical_weight)

            # from the lebedev points, compute the radial coordinate
            rad = x[i]
            th = theta(s[j, 0], s[j, 1], s[j, 2])
            ph = phi(s[j, 0], s[j, 1])
            print("r ", rad, " theta ", th, " phi ", ph)
            print("function at this point: ", g(rad, th, ph))

            # update the integral sum
            print("partial sum: ", sum)
            sum = sum + radial_weight*spherical_weight*g(rad, th, ph)

            # increment the spherical counter
            j = j + 1
        # increment the radial counter
        i = i + 1

    # for lebedev integration, need to multiply by 4 pi
    result = 4 * np.pi * sum

    print(" ")
    print("integration result: ", result)

# The main function
def main():
    integration()

if __name__ == "__main__":
    main()
