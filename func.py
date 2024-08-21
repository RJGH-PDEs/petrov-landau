# File: func.py

# Import
import math

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
    return r * math.cos(p) * math.sin(t)

# y
def y(r, t, p):
    return r * math.sin(p) * math.sin(t)

# z - no dependence on theta
def z(r,t,p):
    return r * math.cos(p)

# Cartesian to polar

# r
def r(x,y,z):
    return math.sqrt(x**2 + y**2 + z**2)

# theta
def t(x,y,z):
    # return math.atan(y/x) # This was before we realized the difficulty with atan
    result = math.acos((x/math.sqrt(x**2 + y**2)))
    if y > 0:
        return result
    elif y < 0:
        return -1*result
    else:
        print("Avoid using y = 0")
        return result

# phi
def p(x,y,z):
    return math.acos(z/r(x,y,z))

"""
First partials of r
"""

# r_x 
def r_x(r, t, p):
   return math.sin(t) * math.cos(p)

# r_y
def r_y(r, t, p):
    return math.sin(t) * math.sin(p)

# r_z
def r_z(r, t, p):
    return math.cos(t)

"""
First partials of theta 
"""

# theta_x
def t_x(r, t, p):
    #return (z(r,t,p)*x(r,t,p))/(math.sqrt(x**2+y**2)*(r**2))
    return math.cos(t)*math.sin(p)/r

# theta_y
def t_y(r,t,p):
    #return (z(r,t,p)*y(r,t,p))/(math.sqrt(x**2+y**2)*(r**2))
    return math.cos(t)*math.sin(p)/r

# theta_z
def t_z(r,t,p):
    #return (-1)*math.sqrt(x**2 + y**2)/r**2
    return (-1)*math.sin(t)/r

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
