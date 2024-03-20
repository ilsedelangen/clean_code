import numpy as np


class Square:
    """Represents a geometrical object: A square in 2D"""
    def __init__(self, side_length: float):
        self._side = side_length

    def compute_area(self) -> float:
        return self._side**2


class Circle:
    """Represents a geometrical object: A circle in 2D"""
    def __init__(self, radius: float):
        self._radius = radius

    def compute_area(self) -> float:
        return np.pi * self._radius**2


class Shape:
    """Abstract concept of a shape"""
    def __init__(self, shape):
        self._shape = shape

    def compute_area_in_px(self, cm2px_ratio: float) -> float:
        return self._shape.compute_area() * cm2px_ratio
