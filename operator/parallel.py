import multiprocessing

# Landau weight
from landau_operator import operator 
from landau_operator import weight_new

# time
import time

# test with an individual 
def individual_test():
    # choose a trial function for the weight
    k = 1
    l = 1
    m = 0 

    # chose test functions
    kp = 1
    lp = 1
    mp = 1

    kq = 0
    lq = 0
    mq = 0

    # package on a vector
    select = [kp, lp, mp, kq, lq, mq]

    # print
    print("weight on: ", k, l, m)
    print("integrating against", select)
    
    # produce required pieces for the weight
    u, g, p, h = weight_new(k, l, m)
    # compute the operator
    operator(u, g, p, h, select, k, l, m)

# create arguments list
def arguments_creator(u, g, p, h, k, l, m, n):
    # empty list
    args = []

    # p iteration
    for kp in range(0, n):
        for lp in range(0,n):
            for mp in range(-lp, lp+1):
                
                # choose selection
                select = [kp, lp, mp, 0, 0, 0]

                # compute the 
                args.append((u, g, p, h, select, k, l, m))

 
    # print(args)
    return args


# iterates over different test functions
def iteration_selector(args):
    '''
    iterates over all possible test functions for 
    the operator
    '''

    # processes
    processes = []
 
    # create and start processes
    for argument in args:
        # operator(u, g, p, h, select, k, l, m)
        # operator(argument[0], argument[1], argument[2], argument[3], argument[4], argument[5], argument[6], argument[7])
        process = multiprocessing.Process(target= operator, args=argument)
        processes. append(process)
        process.start()
    
    # wait for all the processes to complete 
    for pro in processes:
        pro.join()

    print("All processes complete. ")
        
# another implementation of the previous
# iterates over different test functions
def test_iterator(u, g, p, h, k, l, m, n):
    '''
    iterates over all possible test functions for 
    the operator
    '''

    # processes
    processes = []

    # p iteration
    for kp in range(0, n):
        for lp in range(0,n):
            for mp in range(-lp, lp+1):

                # form the argument
                select = [kp, lp, mp, 0, 0, 0]
                argument = (u, g, p, h, select, k, l, m)

                # start processes
                pro = multiprocessing.Process(target=operator, args=argument)
                processes.append(pro)
                pro.start()

    # wait for all the processes to complete
    for pro in processes:
        pro.join()

# produce collision matrix
def weight_iteration(n):
    # iterate over all possible weights
    for k in range(0, n):
        for l in range(0, n):
            for m in range(-l, l+1):
                # print the weight
                print("weight on: ", k, l, m)

                # produce required pieces for the weight
                u, g, p, h = weight_new(k, l, m)

                # args = arguments_creator(u, g, p, h, k, l, m, n)
                # compute for all combinations of basis functions
                # iteration_selector(args)

                start = time.time()
                test_iterator(u, g, p, h, k, l, m, n)
                end = time.time()

                # Calculate elapsed time
                elapsed_time = end - start
                print(f"Elapsed time: {elapsed_time:.6f} seconds") 
                print()

 
# The main function
def main():
    # individual_test()

    # compute
    n = 2

    start_time = time.time()
    weight_iteration(n)
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time
    print(f"Total ellapsed time: {elapsed_time:.6f} seconds")

# Call to the main function
if __name__ == "__main__":
    main()
