# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:44:15 2019

@author: saras
"""
#this script checks input number is a prime number:

def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            return False
        return True
#    
#print(is_prime(10))
