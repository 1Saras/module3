# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:51:53 2019

@author: saras
"""

import unittest
from is_prime import is_prime

class Prime_test(unittest.TestCase):
    def test_prime_float(self):
       self.assertTrue(is_prime(1.1))
       
if __name__ == "__main__":
    unittest.main()

       
#
#class prime_test(unittest.TestCase):
#    def test_prime(self):
#        self.assertIsInstance(sys.argsv[1], int)       
#        self.assertTrue(is_prime(sys.argsv[1]))
#       
#    def sys_input(self):
#        self.assertIsInstance(sys.argsv[1], int)
#
#
#if __name__ =="__main__":
#    unittest.main()
#    prime_test.test_prime()
       
   
    
#class prime_test(unittest.TestCase):
#    def test_prime(self):
##        self.assertIsInstance(sys.argsv[1], int)       
#        self.assertTrue(is_prime(5))
#       
##    def sys_input(self):
##        self.assertIsInstance(sys.argsv[1], int)
#
#

    


#if don't want to use class:
      
#import unittest
#from unittest import TestCase 
#from is_prime import is_prime
#    
#def test_prime(TestCase):
#       TestCase.assertTrue(is_prime(5))
    
#unittest.TestCase.assertTrue(is_prime(5))
    
    
    
    
    
    
    