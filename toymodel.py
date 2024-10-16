import numpy as np
import matplotlib.pyplot as plt

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))



def calc_lc(ph,incl=90,spot_lat=0):
    # calculate the observer vector
    v_obs = [np.sin(np.radians(incl)),0,np.cos(np.radians(incl))] 

    # the spot position on the surface of the WD
    x = np.cos(2*np.pi*ph)*np.cos(np.radians(spot_lat))
    y = np.sin(2*np.pi*ph)*np.cos(np.radians(spot_lat))
    z = np.sin(np.radians(spot_lat))*np.ones_like(ph)

    # as a vector
    v = np.c_[x,y,z]

    # calculate the viewing angle
    viewangle = np.array([angle_between(v_obs,_v) for _v in v])

    # calculate intensity; sin is for dipole, cos is for solid angle correction
    intensity = 2*np.sin(viewangle)*np.cos(viewangle)
    intensity[viewangle>0.5*np.pi] = 0
    
    return intensity
