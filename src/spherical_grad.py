# Import
from func import *
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
def f_x(r,t,p):
    result = r_1(r,t,p)*f_r(r,t,p) + t_1(r,t,p)*f_t(r,t,p) + p_1(r,t,p)*f_p(r,t,p)
    return result

# Partial y
def f_y(r,t,p):
    result = r_2(r,t,p)*f_r(r,t,p)+ t_2(r,t,p)*f_t(r,t,p) + p_2(r,t,p)*f_p(r,t,p)
    return result

# Partial z
def f_z(r,t,p):
    result = r_3(r,t,p)*f_r(r,t,p) + t_3(r,t,p)*f_t(r,t,p) + p_3(r,t,p)*f_p(r,t,p)
    return result

'''
Here we write functions defining the
partial derivatives of the function
with respect of the radial variables
'''

# Partial r
def f_r(r,t,p):
    partial = 2*r

    # The result should be partial/1
    result = partial
    return result

# Partial t
def f_t(r,t,p):
    partial = 0 

    # The result should be partial/r
    result = 0
    return result

# Partial p
def f_p(r,t,p):
    partial = 0

    # The result should be partial/(r sin(theta))
    result = 0
    return result

# The main function
def main():
    radius = 1
    theta  = np.pi/2
    phi    = np.pi

    # Compute the cartesian coordinates
    print('x:', x(radius, theta, phi))
    print('y:', y(radius, theta, phi))
    print('z:', z(radius, theta, phi))

    # Compute the gradient in cartesian
    print('f_x:', f_x(radius, theta, phi))
    print('f_y:', f_y(radius, theta, phi))
    print('f_z:', f_z(radius, theta, phi))
if __name__ == "__main__":
    main()
