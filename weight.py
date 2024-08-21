# Import
from spherical_grad import *

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
    if   i == 1:
        zi = x
    elif i == 2:
        zi = y
    elif i == 3:
        zi = z

    # second component 
    if  j  == 1:
        zj = x
    elif j == 2:
        zj = y
    elif j == 3:
        zj = z

    # Add the second part of 
    # the projection
    result = result - zi*zj

    # Return statement    
    return result

# Compute the weight
def weight(r_p, theta_p, phi_p, r_q, theta_q, phi_q):
    # We start by computhing the 
    # components of the cartesian coordinates
    xp = x(r_p, theta_p, phi_p)
    yp = y(r_p, theta_p, phi_p)
    zp = z(r_p, theta_p, phi_p)
    
    xq = x(r_p, theta_p, phi_p)
    yq = y(r_p, theta_p, phi_p)
    zq = z(r_p, theta_p, phi_p)

    # The relative position
    ux = xp - xq
    uy = yp - yq
    uz = zp - zq

    # Now we compute the components of the 
    # gradient on the two locations and q
    f_x_p = f_x(r_p, theta_p, phi_p)
    f_y_p = f_y(r_p, theta_p, phi_p)
    f_z_p = f_z(r_p, theta_p, phi_p)
    
    f_x_q = f_x(r_q, theta_q, phi_q)
    f_y_q = f_y(r_q, theta_q, phi_q)
    f_z_q = f_z(r_q, theta_q, phi_q)

    # Compute the inner product 
    result = (ux)*(f_x_p - f_x_q) + (uy)*(f_y_p - f_y_q) + (uz)*(f_z_p - f_z_q)
    result = (-2)*result

    for i in range(0,2):
        for j in range(0,2):
            result = result 

    # Return statement
    return result

# The main function
def main():
# First, we define the two points in spherical
    r_p = 0
    t_p = np.pi/2
    p_p = -np.pi/2
    
    r_q = 0
    t_q = np.pi/2
    p_q = -np.pi/2


# Main function
if __name__ == "__main__":
    main()
