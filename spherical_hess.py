# Import
import numpy as np

'''
Here we wrtie the different 
functions that are required to 
compute the second derivatives
in spherical coordintates
'''

'''
Note that these might be changed later
as the Jacobian for the volume element
is introduced for integration
'''

'''
With respect of r_hat
'''
# First coordinate
def r_1_r(r,t,p):
    return 0
def r_1_t(r,t,p):
    return np.cos(p)*np.cos(t)
def r_1_p(r,t,p):
    return (-1)*np.sin(p)*np.sin(t)
# Second coordinate
def r_2_r(r,t,p):
    return 0
def r_2_t(r,t,p):
    return np.cos(t)*np.sin(p)
def r_2_p(r,t,p):
    return np.cos(p)*np.sin(t)
# Third coordinate
def r_3_r(r,t,p):
    return 0
def r_3_t(r,t,p):
    return (-1)*np.sin(t)
def r_3_p(r,t,p):
    return 0

'''
With respect of theta_hat
'''
# First coordinate
def t_1_r(r,t,p):
    return 0 
def t_1_t(r,t,p):
    return -1*np.cos(p)*np.sin(t)
def t_1_p(r,t,p):
    return -1*np.cos(t)*np.sin(p)
# Second coordinate 
def t_2_r(r,t,p):
    return 0
def t_2_t(r,t,p):
    return -1*np.sin(p)*np.sin(t)
def t_2_p(r,t,p):
    return np.cos(p)*np.cos(t)
# Third coordinate
def t_3_r(r,t,p):
    return 0
def t_3_t(r,t,p):
    return -1*np.cos(t)
def t_3_p(r,t,p):
    return 0

'''
With respect of phi_hat
'''
# First coordinate
def p_1_r(r,t,p):
    return 0
def p_1_t(r,t,p):
    return 0  
def p_1_p(r,t,p):
    return -1*np.cos(p)
# Second coordinate 
def p_2_r(r,t,p):
    return 0
def p_2_t(r,t,p):
    return 0
def p_2_p(r,t,p):
    return -1*np.sin(p)
# Third coordinate
def p_3_r(r,t,p):
    return 0
def p_3_t(r,t,p):
    return 0