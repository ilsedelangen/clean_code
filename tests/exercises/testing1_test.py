# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:54:26 2024

@author: ilsed
"""

from ...exercises.testing1 import divide, is_prime

def test_divide():
    assert divide(2,0) == float("inf")
    assert divide(0,0) == float("NaN")
    assert divide(10,2) == 5
    
def test_is_prime_():
    assert is_prime(29) == True
    assert is_prime(1) == False  
    assert is_prime(27) == False  