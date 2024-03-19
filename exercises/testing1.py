"""
generate a unit test suite for this module.
Follow the examples seen in the slides and
already present under tests/.
"""


def divide(numerator: float, denominator: float) -> float:
    return numerator / denominator


def is_prime(number: int) -> bool:
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True
