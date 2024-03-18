import os
import csv
import numpy as np
from scipy import interpolate


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
