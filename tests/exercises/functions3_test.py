import os
import numpy as np
from ...exercises.functions3 import input_flux
from ...exercises.functions3_cleaned import estimate_flux_for_wavelength, InputFlux


def test_original_input_flux():
    np.testing.assert_almost_equal(input_flux(300), 0.173)
    np.testing.assert_almost_equal(input_flux(320.5), 0.5624889013291254)
    np.testing.assert_almost_equal(input_flux(399), 2.724)


def test_numpy_input_flux():
    np.testing.assert_almost_equal(estimate_flux_for_wavelength(300), 0.173)
    np.testing.assert_almost_equal(estimate_flux_for_wavelength(320.5), 0.5624889013291254)
    np.testing.assert_almost_equal(estimate_flux_for_wavelength(399), 2.724)


def test_input_flux_class():
    inpflx = InputFlux()
    np.testing.assert_almost_equal(inpflx.estimate(300), 0.173)
    np.testing.assert_almost_equal(inpflx.estimate(320.5), 0.5624889013291254)
    np.testing.assert_almost_equal(inpflx.estimate(399), 2.724)


def test_load_flux_table():
    flux = InputFlux(os.path.join(os.path.dirname(__file__), 'test_flux.csv'))
    flux._load_flux_table()
    assert flux._flux.shape == (6, 2)
    for i in range(6):
        assert flux._flux[i][0] == i + 1
        assert flux._flux[i][1] == (i + 1) / 2


def test_interpolate_flux():
    flux = InputFlux()
    flux._flux = np.array([[1, 0.5], [2, 1], [3, 1.5], [4, 2], [5, 2.5]])
    np.testing.assert_almost_equal(flux._interpolate_flux_at(2), 1.0)
    np.testing.assert_almost_equal(flux._interpolate_flux_at(2.5), 1.25)
    np.testing.assert_almost_equal(flux._interpolate_flux_at(3), 1.5)
