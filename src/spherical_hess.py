# Import
import numpy as np
from spherical_grad import *

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

'''
This section will contain the second partials,
the way the hessian requires them
'''

'''
f_{rr}
'''
def m_11(r,t,p):
    result = 0
    return result

'''
(1/r) f_{r \theta} - (1/r^2) f_{\theta}
'''
def m_12(r,t,p):
    result = 0
    return result

'''
(1/r \sin \theta) f_{\phi r} - (1/r^2 \sin \theta) f_{\theta}
'''
def m_13(r,t,p):
    result = 0
    return result 

'''
(1/r^2) f_{\theta \theta} + (1/r) f_{r}
'''
def m_22(r,t,p):
    result = 0 
    return result

'''
(1/(r^2 \sin \theta)) f_{\phi \theta} - (\cos \theta)/(r^2 \sin^2 \theta) f_{\phi}
'''
def m_23(r,t,p):
    result = 0
    return result

'''
(1/(r^2 \sin^2 \theta))f_{\phi \phi} + (1/r) f_{r} + (\cot \theta)/(r^2)f_{\theta}
'''
def m_33(r,t,p):
    result = 0
    return result

# Now we put everything together to form the Hessian
def hessian(r, t, p):
    '''
    We start by building the 
    basis vectors.
    '''
    rad     = np.array([r_1(r,t,p),r_2(r,t,p),r_3(r,t,p)])
    theta   = np.array([t_1(r,t,p),t_2(r,t,p),t_3(r,t,p)])
    phi     = np.array([p_1(r,t,p),p_2(r,t,p),p_3(r,t,p)])
    
    '''
    We build the tensor basis
    '''
    # First row 
    a_11 = np.outer(rad, rad)
    a_12 = np.outer(rad, theta)
    a_13 = np.outer(rad, phi)

    # Second row
    a_21 = np.outer(theta, rad)
    a_22 = np.outer(theta,theta)
    a_23 = np.outer(theta, phi)

    # Third row
    a_31 = np.outer(phi, rad)
    a_32 = np.outer(phi,theta)
    a_33 = np.outer(phi,phi)
    
        