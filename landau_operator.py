import numpy as np
# integration 
from scipy.special import roots_genlaguerre
from pylebedev import PyLebedev
# weight
from landau_weight import weight_new
from landau_weight import weight_evaluator
# function
from test_func import f_integrated

# from cartesian to polar
def theta(x, y, z):
    return np.acos(z/np.sqrt(x**2+ y**2 + z**2))

# from cartesian to polar
def phi(x, y):
    if x == 0 and y == 0: return 0
    return (np.sign(y))*np.acos(x/np.sqrt(x**2 + y**2))

# spherical function to be integrated against two Gaussians
def f(rp, tp, pp, rq, tq, pq):
    result = 1
    return result

# spherical function that is actually sampled
def f_samp(xp, tp, pp, xq, tq, pq):
    rp = np.sqrt(2 * xp)
    rq = np.sqrt(2 * xq)
    return 2 * f_integrated(rp, tp, pp, rq, tq, pq)

# integration
def operator(k, l, m):
    # produce required pieces for the weight
    u, g, p, h = weight_new(k, l, m)

    '''
    choose the integration order here
    '''
    n_laguerre = 3
    n_lebedev = 3
    ''''''

    # extract the coefficients
    alpha = 1/2
    x,w_r = roots_genlaguerre(n_laguerre, alpha, False)
    print(w_r)

    # build library
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
                    
                    # compute the weight
                    weight = weight_evaluator(l, m, u, g, p, h, np.sqrt(2 * x_p), t_p, p_p, np.sqrt(2 * x_q), t_q, p_q)
                    func = f_samp(x_p, t_p, p_p, x_q, t_q, p_q)

                    # update the partial sum
                    print("Landau weight: ", weight)
                    print("function: ", func)

                    sum = sum + rw_p*sw_p*rw_q*sw_q*func*weight

                    # increment total number of iterations
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

    '''
    out of the loop
    '''

    # compute and print result
    print("result before final scaling: ", sum)
    result = sum*(4*np.pi)**2 
    print("result: ", result)
    print("total number of loops: ", total_iter)

# The main function
def main():
    # choose a test function for the weight
    k = 2
    l = 1
    m = 1

    # evaluate the operator
    operator(k, l, m)

# Call to the main function
if __name__ == "__main__":
    main()
