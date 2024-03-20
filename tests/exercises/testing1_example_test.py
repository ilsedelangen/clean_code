import numpy as np
import pytest
from ...exercises.testing1 import *


def test_division():
    np.testing.assert_almost_equal(divide(3, 4), 0.75)
    np.testing.assert_almost_equal(divide(133.7, np.pi), 42.5, 1)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)


def test_prime_has_a_bug():
    # This is a bug.
    # But since we only can see what we test for ... did you spot it?
    assert is_prime(1)


def test_prime_border_case():
    with pytest.raises(TypeError):
        is_prime(1.2)
    with pytest.raises(TypeError):
        is_prime('foo')
    with pytest.raises(TypeError):
        is_prime(None)
