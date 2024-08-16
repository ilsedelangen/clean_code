# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:36:16 2024

@author: ilsed
"""
from astropy.io import fits

from ...exercises.functions4 import fits_parse_op_keywords

def test_fits_parse_op_keywords():
    hdr = fits.Header()
    hdr['OP1_KEY1'] = 'operation_1'
    hdr['OP1_KEY2'] = 'operation_2'
    hdr['OP1_KEY3'] = 'operation_3'
    hdr['OP1_KEY4'] = 'operation_4'
    queue = fits_parse_op_keywords([], hdr)
    print(queue)
    
test_fits_parse_op_keywords()
    