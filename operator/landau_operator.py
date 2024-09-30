import numpy as np
# integration 
from scipy.special import roots_genlaguerre
from pylebedev import PyLebedev
# weight
from landau_weight import weight_new
from landau_weight import weight_evaluator
# function
from test_func import f_integrated
# time
import time

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
def f_samp(select, xp, tp, pp, xq, tq, pq):
    rp = np.sqrt(2 * xp)
    rq = np.sqrt(2 * xq)
    return 2 * f_integrated(select, rp, tp, pp, rq, tq, pq)

# integration
def operator(u, g, p, h, select, k, l, m):
    '''
    choose the integration order here
    '''
    n_laguerre = 3
    n_lebedev = 5
    ''''''

    # extract the coefficients
    alpha = 1/2
    x,w_r = roots_genlaguerre(n_laguerre, alpha, False)
    # print(w_r)

    # build library
    leblib = PyLebedev()
    s,w_spher = leblib.get_points_and_weights(n_lebedev)
    # print(w_spher)

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
                    # print("iteration ", total_iter)
                    # print("partial sum: ", sum)
                    x_p = x[i_p]
                    t_p = theta(s[j_p, 0], s[j_p, 1], s[j_p, 2])
                    p_p = phi(s[j_p, 0], s[j_p, 1])

                    # compute q radially
                    x_q = x[i_q]
                    t_q = theta(s[j_q, 0], s[j_q, 1], s[j_q, 2])
                    p_q = phi(s[j_q, 0], s[j_q, 1])  
                    
                    # compute the weight
                    weight = weight_evaluator(l, m, u, g, p, h, np.sqrt(2 * x_p), t_p, p_p, np.sqrt(2 * x_q), t_q, p_q)
                    func = f_samp(select, x_p, t_p, p_p, x_q, t_q, p_q)

                    # update the partial sum
                    # print("Landau weight: ", weight)
                    # print("function: ", func)

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

    # print result
    print("integrating against", select)
    print("result: (4*Pi)^2 times ", sum)

    return (select, [k,l, m], sum)

    # result = sum*(4*np.pi)**2 
    # print("result: ", result)
    # print("total number of loops: ", total_iter)


# iterates over different test functions
def iteration_selector(u, g, p, h, k, l, m, n):
    # p iteration
    for kp in range(0, n):
        for lp in range(0,n):
            for mp in range(-lp, lp+1):
                select = [kp, lp, mp, 0, 0, 0]
                operator(u, g, p, h, select, k, l, m)


# collision matrix
def collision_matrix(n):
    for k in range(0, n):
        for l in range(0, n):
            for m in range(-l, l+1):
                # print the weight
                print("weight on: ", k, l, m)

                # produce required pieces for the weight
                u, g, p, h = weight_new(k, l, m)

                # compute for all combinations of basis functions (and time it)
                start = time.time()
                iteration_selector(u, g, p, h, k, l, m, n)
                end = time.time()
                
                # Calculate elapsed time
                elapsed_time = end - start
                print(f"Elapsed time: {elapsed_time:.6f} seconds")

                # operator(select, k, l, m)
                print()


# The main function
def main():
    # choose a trial function for the weight
    k = 2
    l = 1
    m = -1 

    # chose test functions
    kp = 2
    lp = 2
    mp = 2

    kq = 0
    lq = 1
    mq = -1

    # package on a vector
    select = [kp, lp, mp, kq, lq, mq]

    # number of basis functions
    n = 2
    collision_matrix(n)

    return 0
    
# Call to the main function
if __name__ == "__main__":
    main()
