# Import
from func import *
from basis_partials import *
import numpy as np

"""
Here we write the matrix that
transforms gradient in spherical
to gradient in cartessian
"""

# Matrix
def jacob_sph_car(r, t, p):
    # Extract the coefficients
    m11 = r_x(r,t,p); m12 = r_y(r,t,p); m13 = r_z(r,t,p);
    m21 = t_x(r,t,p); m22 = t_y(r,t,p); m23 = t_z(r,t,p);
    m31 = p_x(r,t,p); m32 = p_y(r,t,p); m33 = p_z(r,t,p);
    # Define the matrix
    m = np.array([[m11,m12, m13],[m21, m22, m23],[m31, m32, m33]])
    # Return it
    return m

'''

After checking again, we will use another approach
The following are the components of the unit vectors
in spherical coordinates

'''

'''
radius hat 
'''
# first entry
def r_1(r,t,p):
    result = np.sin(t)*np.cos(p)
    return result

# second entry
def r_2(r,t,p):
    result = np.sin(t)*np.sin(p)
    return result

# third entry
def r_3(r,t,p):
    result = np.cos(t)
    return result

'''
theta hat
'''
# first entry
def t_1(r,t,p):
    result = np.cos(t)*np.cos(p)
    return result

# second entry
def t_2(r,t,p):
    result = np.cos(t)*np.sin(p)
    return result

# third entry
def t_3(r,t,p):
    result = (-1)*np.sin(t)
    return result

'''
phi hat
'''
# first entry
def p_1(r,t,p):
    result = (-1)*np.sin(p)
    return result

# second entry
def p_2(r,t,p):
    result = np.cos(p)
    return result

# third entry
def p_3(r,t,p):
    result = 0
    return result

'''
Putting the previous coefficients 
together we can obtain the partials
with respect of x, y, z
'''

# Partial x
def f_x(k,l,m,r,t,p):
    result = r_1(r,t,p)*f_r(k,l,m,r,t,p) + t_1(r,t,p)*f_t(k,l,m,r,t,p) + p_1(r,t,p)*f_p(k,l,m,r,t,p)
    return result

# Partial y
def f_y(k,l,m,r,t,p):
    result = r_2(r,t,p)*f_r(k,l,m,r,t,p)+ t_2(r,t,p)*f_t(k,l,m,r,t,p) + p_2(r,t,p)*f_p(k,l,m,r,t,p)
    return result

# Partial z
def f_z(k,l,m,r,t,p):
    result = r_3(r,t,p)*f_r(k,l,m,r,t,p) + t_3(r,t,p)*f_t(k,l,m,r,t,p) + p_3(r,t,p)*f_p(k,l,m,r,t,p)
    return result

'''
Here we write functions defining the
partial derivatives of the function
with respect of the radial variables 

Now we are ready to start using the ones
that are specific for our test functions
'''

# Partial r
def f_r(k,l,m,r,t,p):
    result = partial_r(k,l,m,r,t,p)

    # The result should be partial/1
    return result

# Partial t
def f_t(k,l,m,r,t,p):
    result = partial_theta(k,l,m,r,t,p)

    # The result should be partial/r
    return result

# Partial p
def f_p(k,l,m,r,t,p):
    result = partial_phi(k,l,m,r,t,p)

    # The result should be partial/(r sin(theta))
    return result

# The main function
def main():
    k = 1
    l = 0
    m = 0

    radius = 3
    theta  = np.pi/4
    phi    = np.pi/5

    # Compute the cartesian coordinates
    print('x:', x(radius, theta, phi))
    print('y:', y(radius, theta, phi))
    print('z:', z(radius, theta, phi))
    print(" ")

    # Compute the radial partials
    print("part r: ", f_r(k, l, m, radius, theta, phi))
    print("part t: ", f_t(k, l, m, radius, theta, phi))   
    print("part p: ", f_p(k, l, m, radius, theta, phi))   
    print(" ")

    # Compute the gradient in cartesian
    print('f_x:', f_x(k, l, m, radius, theta, phi))
    print('f_y:', f_y(k, l, m, radius, theta, phi))
    print('f_z:', f_z(k, l, m, radius, theta, phi))


if __name__ == "__main__":
    main()
