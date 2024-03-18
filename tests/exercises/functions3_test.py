from numpy import testing
from ...exercises.functions3 import input_flux


def test_input_flux():
    testing.assert_almost_equal(input_flux(300), 0.173)
    testing.assert_almost_equal(input_flux(320.5), 0.5624889013291254)
    testing.assert_almost_equal(input_flux(399), 2.724)
