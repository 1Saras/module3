# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:10:54 2019

@author: saras
"""

import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
# """Tests for 'primes.py'"""
 def test_is_five_prime(self):
# """Is five successfully determined to be prime?"""
     self.assertTrue(is_prime(5))
     
def test_is_four_non_prime(self):
# """Is four correctly determined not to be prime?"""
 self.assertTrue(is_prime(4), msg="Four is not prime!")
     
     
if __name__ == '__main__':
  unittest.main()