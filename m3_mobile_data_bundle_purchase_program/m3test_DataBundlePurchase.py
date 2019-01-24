# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:39:52 2018

@author: saras
"""

from m3SimpleBundlePurchase import passwordCheck

# Test call to programme:
print ('TEST EXAMPLE 1')
# database input, you will still need to check user pin
result = passwordCheck('1234', 34.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 2')
result = passwordCheck('2345', -22.00)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 3')
result = passwordCheck('3456', 17.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')
