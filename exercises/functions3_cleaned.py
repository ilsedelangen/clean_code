import os
import csv
import numpy as np
from scipy import interpolate

INPUT_FLUX_PATH = os.path.join(os.path.dirname(__file__), '..', 'resources', 'flux.csv')


# A refactored version
# This a class now as a first step towards a state aware object.
# In the future the self._flux table can be read only once (behavior change)...
# Why is this cleaner?
#    - Naming conventions are fulfilled
#    - Integration and Operation are separated in their own methods
#    - small methods focus on one thing, each part is straight-forward
#    - See test examples for further arguments
class InputFlux:
    # 0 is scipy magic number for no smoothing.
    SMOOTHING = 0

    def __init__(self, data_path: str = INPUT_FLUX_PATH):
        self._data_path = data_path
        self._flux = None

    def estimate(self, wavelength: float) -> np.array:
        self._load_flux_table()
        return self._interpolate_flux_at(wavelength)

    def _load_flux_table(self) -> None:
        flux = np.array([[0, 0]])
        with open(self._data_path, newline='') as csv_file:
            for row in csv.reader(csv_file):
                flux = np.concatenate((flux, [np.array(row).astype(float)]))
        self._flux = flux[1:, :]

    def _interpolate_flux_at(self, wavelength: float) -> np.array:
        tck = interpolate.splrep(self._flux[:, 0], self._flux[:, 1], s=InputFlux.SMOOTHING)
        return np.array(interpolate.splev(wavelength, tck))


# Another refactored version.
# This uses a method from the numpy package.
# Still only one operation method, neatly compressed.
# What are the implications on testability?
def estimate_flux_for_wavelength(wavelength: float, flux_path: str = INPUT_FLUX_PATH) -> np.array:
    data = np.loadtxt(flux_path, delimiter=',')
    tck = interpolate.splrep(data[:, 0], data[:, 1], s=0)
    return np.array(interpolate.splev(wavelength, tck))
