# Import
from spherical_hess import *
import random
# from basis_partials import *

'''
The following handles both the 
projection matrix and the 
|u|^(lamda + 2) term.

In this case lamda = 0
for simplicity
'''
# Projection matrix
def projection(x,y,z,i,j):
    result = 0

    # Components 
    zi = 0
    zj = 0

    # Compute the delta 
    if i == j:
        result = (x*x + y*y + z*z)

    # first component 
    if   i == 0:
        zi = x
    elif i == 1:
        zi = y
    elif i == 2:
        zi = z

    # second component 
    if  j  == 0:
        zj = x
    elif j == 1:
        zj = y
    elif j == 2:
        zj = z

    # Add the second part of 
    # the projection
    result = result - zi*zj

    # Return statement    
    return result

# Compute the weight
def weight(k,l,m, r_p, theta_p, phi_p, r_q, theta_q, phi_q):
    # We start by computhing the 
    # components of the cartesian coordinates
    xp = x(r_p, theta_p, phi_p)
    yp = y(r_p, theta_p, phi_p)
    zp = z(r_p, theta_p, phi_p)
    
    xq = x(r_q, theta_q, phi_q)
    yq = y(r_q, theta_q, phi_q)
    zq = z(r_q, theta_q, phi_q)

    # Print these 
    print('p:')
    print(xp)
    print(yp)
    print(zp)
    print()
    print('q:')
    print(xq)
    print(yq)
    print(zq)
    print()
    
    # The relative position
    ux = xp - xq
    uy = yp - yq
    uz = zp - zq

    # Now we compute the components of the 
    # gradient on the two locations and q
    f_x_p = f_x(k,l,m,r_p, theta_p, phi_p)
    f_y_p = f_y(k,l,m,r_p, theta_p, phi_p)
    f_z_p = f_z(k,l,m,r_p, theta_p, phi_p)
    
    f_x_q = f_x(k,l,m,r_q, theta_q, phi_q)
    f_y_q = f_y(k,l,m,r_q, theta_q, phi_q)
    f_z_q = f_z(k,l,m,r_q, theta_q, phi_q)

    # Print these 
    print('Gradient p:')
    print(f_x_p)
    print(f_y_p)
    print(f_z_p)
    print()
    print('Gradient q:')
    print(f_x_q)
    print(f_y_q)
    print(f_z_q)
    print()
    print('Relative position:')
    print(ux)
    print(uy)
    print(uz)
    print()
    # Compute the inner product 
    result = 0
    result = (ux)*(f_x_p - f_x_q) + (uy)*(f_y_p - f_y_q) + (uz)*(f_z_p - f_z_q)
    result = (-2)*result

    print('Partial result: ', result)
    # Now we compute the contraction
    # of the hessians with the projection
    hess = hessian(k,l,m,r_p,theta_p,phi_p) + hessian(k,l,m,r_q, theta_q, phi_q) # This part needs to be checked to see if it does what we want
    hess = hess/2
    print('hessian to be contracted: ')
    print(hess)
    '''
    First we need to make sure that the 
    previous is the correct way of computhing 
    the sum of two hessians 
    '''

    contraction_result = 0
    # Compute the contraction -- this is wrong
    for i in range(0,3):
        for j in range(0,3):
            contraction_result = contraction_result + projection(ux, uy, uz, i, j) * hess[i][j]

    # Scale this part by 1/2
    contraction_result = contraction_result
    print('contraction result: ', contraction_result)

    # Update result 
    result = result + contraction_result

    # Return statement
    return result

# The main function
def main():
    k = 0
    l = 1
    m = 1
    # First, we define the two points in spherical
    r_p = 10*random.random()
    t_p = np.pi*random.uniform(0.1, 0.9)
    p_p = 2*np.pi*random.random()
    
    r_q = 10*random.random()
    t_q = np.pi*random.uniform(0.1, 0.9)
    p_q = 2*np.pi*random.random()

    # Compute the weight
    print('weight: ', weight(k,l,m,r_p, t_p, p_p, r_q, t_q, p_q))


# Main function
if __name__ == "__main__":
    main()
