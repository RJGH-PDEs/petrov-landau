import numpy as np
from scipy.special import roots_genlaguerre
from scipy.special import genlaguerre
from pylebedev import PyLebedev
from landau_weight import weight_new
from landau_weight import weight_evaluator

# from cartesian to polar
def theta(x, y, z):
    return np.acos(z/np.sqrt(x**2+ y**2 + z**2))

# from cartesian to polar
def phi(x, y):
    if x == 0 and y == 0: return 0
    return (np.sign(y))*np.acos(x/np.sqrt(x**2 + y**2))

# spherical function to be integrated against two Gaussians
def ff(rp, tp, pp, rq, tq, pq):
    k = 2
    l = 2
    m = 1
    result = 1
    return result

# spherical function that is actually sampled
def gg(xp, tp, pp, xq, tq, pq):
    rp = np.sqrt(2 * xp)
    rq = np.sqrt(2 * xq)
    return 2 * ff(rp, tp, pp, rq, tq, pq)

# integration
def operator(k, l, m):
    # produce required pieces for the weight
    u, g, p, h = weight_new(k, l, m)

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
                    
                    # compute the function value
                    function = 2*weight_evaluator(l, m, u, g, p, h, np.sqrt(2 * x_p), t_p, p_p, np.sqrt(2 * x_q), t_q, p_q)

                    # update the partial sum
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
    # choose a test function for the weight
    k = 3
    l = 3
    m = 0

    # evaluate the operator
    operator(k, l, m)

if __name__ == "__main__":
    main()
