import os
import csv
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


# Original version from the IOSP example
# Why is this not clean?
#    - Does more than one thing (reading csv, interpolation)
#    - Naming is suboptimal
#    - Nesting level too deep
def input_flux(wl):
    flux = np.array([[0, 0]])
    with open(os.path.join(os.path.dirname(__file__), '..', 'resources', 'flux.csv'), newline='') as csvfile:
        for row in csv.reader(csvfile):
            flux = np.concatenate((flux, [np.array(row).astype(float)]))
    flux = flux[1:, :]
    tck = interpolate.splrep(flux[:, 0], flux[:, 1], s=0)
    return np.array(interpolate.splev(wl, tck))

################################# Solution ####################################

def load_flux_from_csv(filename):
    flux = np.genfromtxt(filename, delimiter=',', dtype=float, skip_header=1)
    return flux 

def interpolate_flux(wavelength,flux):
    tck = interpolate.splrep(flux[:, 0], flux[:, 1], s=0)
    return np.array(interpolate.splev(wavelength, tck))   

def determine_input_flux(wavelength):
    filename = os.path.join(os.path.dirname(__file__), '..', 'resources', 'flux.csv')
    raw_flux = load_flux_from_csv(filename)
    return interpolate_flux(wavelength,raw_flux) 

# Not correct yet! 
wl = np.arange(0,100)
original = input_flux(wl)
solution = determine_input_flux(wl)
plt.plot(wl,original)
plt.plot(wl,solution)
plt.show()


    





