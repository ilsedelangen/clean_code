from ...examples.open_closed_principle import *


def test_square_area():
    for i in range(6):
        assert i**2 == Square(side_length=i).compute_area()


def test_circle_area():
    for i in range(6):
        assert np.pi * i**2 == Circle(radius=i).compute_area()


def test_shape_with_square():
    shape = Shape(Square(side_length=1))
    assert 0.5 == shape.compute_area_in_px(0.5)


def test_shape_with_circle():
    shape = Shape(Circle(radius=1))
    np.testing.assert_almost_equal(np.pi/2, shape.compute_area_in_px(0.5))
