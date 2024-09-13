from pylebedev import PyLebedev
import numpy as np

def main():
    """
    Test Lebedev quadrature for probe function
    """
    # build library
    # leblib = PyLebedev()
    
    # exact answer to function "testfunc"
    # exact = 216.0 * np.pi / 35.0
    # r,w = leblib.get_points_and_weights(9)
    # integral = 4.0 * np.pi * np.sum(w * tfunc(r[:,0], r[:,1], r[:,2]))
    
    # print('Integral: %f vs Exact: %f' % (integral, exact))
    spherical_lebedev()


def tfunc(x,y,z):
    """
    Trial function to test
    
    Adapted from: https://cbeentjes.github.io/files/Ramblings/QuadratureSphere.pdf
    
    This function has the exact result upon integration over a unit sphere
    of 216/35 * pi
    """
    return 1 + x + y**2 + x**2*y + x**4 + y**5 + x**2*y**2*z**2


def spherical_lebedev():
    """
    Test Lebedev quadrature 
    """
    # build library
    leblib = PyLebedev()
    n = 5
    print()
    r,w = leblib.get_points_and_weights(n)

    print(r)
    for i in range(len(r)):
        print("number:", i)
        print("x: ", r[i,0])
        print("y: ", r[i,1])
        print("z: ", r[i,2])
        print("theta: ", theta(r[i,0],r[i,1],r[i,2]))
        print("phi: ", phi(r[i,0],r[i,1]))
        print("")

def theta(x, y, z):
    return np.acos(z/np.sqrt(x**2+ y**2 + z**2))

def phi(x, y):
    if x == 0 and y == 0: return 0
    return (np.sign(y))*np.acos(x/np.sqrt(x**2 + y**2))

if __name__ == '__main__':
    main()