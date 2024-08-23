# File: func.py

# Import
import numpy as np

""" 
    Here we will compile a bunch of functions that will be useful for
    computing the Hessian in spherical coordinates.
"""
# Change of variables

"""
    -> r: radius
    -> t: theta
    -> p: phi
"""

# Polar to cartesian 

# x
def x(r, t, p):
    return r * np.cos(p) * np.sin(t)

# y
def y(r, t, p):
    return r * np.sin(p) * np.sin(t)

# z - no dependence on phi 
def z(r,t,p):
    return r * np.cos(t)

# Cartesian to polar

# r
def r(x,y,z):
    return np.sqrt(x**2 + y**2 + z**2)

# theta
def t(x,y,z):
    # return np.atan(y/x) # This was before we realized the difficulty with atan
    result = np.acos((x/np.sqrt(x**2 + y**2)))
    if y > 0:
        return result
    elif y < 0:
        return -1*result
    else:
        print("Avoid using y = 0")
        return result

# phi
def p(x,y,z):
    return np.acos(z/r(x,y,z))

"""
First partials of r
"""

# r_x 
def r_x(r, t, p):
   return np.sin(t) * np.cos(p)

# r_y
def r_y(r, t, p):
    return np.sin(t) * np.sin(p)

# r_z
def r_z(r, t, p):
    return np.cos(t)

"""
First partials of theta 
"""

# theta_x
def t_x(r, t, p):
    #return (z(r,t,p)*x(r,t,p))/(np.sqrt(x**2+y**2)*(r**2))
    return np.cos(t)*np.sin(p)/r

# theta_y
def t_y(r,t,p):
    #return (z(r,t,p)*y(r,t,p))/(np.sqrt(x**2+y**2)*(r**2))
    return np.cos(t)*np.sin(p)/r

# theta_z
def t_z(r,t,p):
    #return (-1)*np.sqrt(x**2 + y**2)/r**2
    return (-1)*np.sin(t)/r

"""
First partials of phi
"""

# phi_x
def p_x(r,t,p):
    # First calculate y
    why = y(r,t,p)

    # Calculate result
    result = 0

    # Proceed by cases
    if why > 0:
        return result
    elif why < 0:
        return -1*result
    else:
        print("Be careful with y = 0 case")
        return 0

# phi_y
def p_y(r,t,p):
    # First calculate y
    why = y(r,t,p)

    # Calculate result
    result = 0

    # Proceed by cases
    if why > 0:
        return result
    elif why < 0:
        return -1*result
    else:
        print("Be careful with y = 0 case")
        return 0


# phi_z
def p_z(r,t,p):
    # First calculate y
    why = y(r,t,p)

    # Calculate result
    result = 0

    # Proceed by cases
    if why > 0:
        return result
    elif why < 0:
        return -1*result
    else:
        print("Be careful with y = 0 case")
        return 0
