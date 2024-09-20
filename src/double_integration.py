import numpy as np
from scipy.special import roots_genlaguerre
from scipy.special import genlaguerre
from pylebedev import PyLebedev
from symbolic import weight

# from cartesian to polar
def theta(x, y, z):
    return np.acos(z/np.sqrt(x**2+ y**2 + z**2))

# from cartesian to polar
def phi(x, y):
    if x == 0 and y == 0: return 0
    return (np.sign(y))*np.acos(x/np.sqrt(x**2 + y**2))

# spherical function to be integrated against a Gaussian
def f(r, t, p):
    return 1

# spherical function that is actually sampled
def g(x, t, p):
    r = np.sqrt(2 * x)
    return np.sqrt(2)*f(r, t, p)

# spherical function to be integrated against two Gaussians
# now we test with the Gaussian 
def ff(rp, tp, pp, rq, tq, pq):
    k = 2
    l = 2
    m = 1
    result = 1
    result = weight(k, l, m, rp, tp, pp, rq, tq, pq)
    return result

# spherical function that is actually sampled
def gg(xp, tp, pp, xq, tq, pq):
    rp = np.sqrt(2 * xp)
    rq = np.sqrt(2 * xq)
    return 2 * ff(rp, tp, pp, rq, tq, pq)

# integration
def integration():
    # extract the coefficients
    n_laguerre = 4
    alpha = 1/2
    x,w_r = roots_genlaguerre(n_laguerre, alpha, False)
    print(w_r)

    # build library
    n_lebedev = 3
    leblib = PyLebedev()
    s,w_spher = leblib.get_points_and_weights(n_lebedev)
    print(w_spher)
    """
    # now we have both weights and positions, we need to do a tensor product
    sum = 0

    # radial counter
    i= 0
    for radial_weight in w_r:
        # spherical counter
        j= 0
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
    """

    # Now we try to repeat for both variables
    sum = 0
    total_iter = 0

    # radial p counter
    i_p = 0
    for rw_p in w_r:
        # spherical p counter
        j_p = 0
        for sw_p in w_spher:
            # radial q counter
            i_q = 0
            for rw_q in w_r:
                # spherical q counter
                j_q = 0
                for sw_q in w_spher:

                    '''
                    Code here repeats for all points
                    '''
                    # print(i_p, j_p, i_q, j_q)

                    # compute p radially
                    print("iteration ", total_iter)
                    print("partial sum: ", sum)
                    x_p = x[i_p]
                    t_p = theta(s[j_p, 0], s[j_p, 1], s[j_p, 2])
                    p_p = phi(s[j_p, 0], s[j_p, 1])

                    # compute q radially
                    x_q = x[i_q]
                    t_q = theta(s[j_q, 0], s[j_q, 1], s[j_q, 2])
                    p_q = phi(s[j_q, 0], s[j_q, 1])  

                    # update the partial sum
                    function = gg(x_p, t_p, p_p, x_q, t_q, p_q)
                    print("function: ", function)
                    sum = sum + rw_p*sw_p*rw_q*sw_q*function
                    total_iter = total_iter + 1
                    '''
                    Code here repeats for all points
                    '''
                    # increment j_q
                    j_q = j_q + 1
                # increment i_q
                i_q = i_q + 1
            # increment j_p
            j_p = j_p + 1
        # increment i_p
        i_p = i_p + 1                    

    print("result before final scaling: ", sum)
    # out of the loop
    result = sum*(4*np.pi)**2
    
    print("result: ", result)
    print("total number of loops: ", total_iter)
# The main function
def main():
    integration()

    # Testing the weight
    # print(weight(1, 1, 1, 1, 0, 0, 1, 0, 0))

if __name__ == "__main__":
    main()
