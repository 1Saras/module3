# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:18:29 2019

@author: amina
"""

from phonebook import *
import unittest


class phonebook_tests(unittest.TestCase):

#DB function tests    
    def test_check_db(self):    
        self.assertTrue(check_db())
   
    def test_findPeople(self):
        self.assertIsInstance(findPeople(),list)
       
    def test_findBusiness(self):
        self.assertIsInstance(findBusiness(),list)

        
#Validation function tests     
    def test_has_numbers(self):
        self.assertTrue(has_numbers('abc123'))
        self.assertFalse(has_numbers('abc'))
        
    def test_has_symbols(self):
        self.assertTrue(has_symbols('abc?#--'))
        self.assertFalse(has_symbols('abc'))
        
    def test_has_symbols_excludeHyphens(self):
        self.assertTrue(has_symbols_excludeHyphens('abc?#'))
        self.assertFalse(has_symbols_excludeHyphens('abc'))
        self.assertFalse(has_symbols_excludeHyphens('a-b-c'))
    
    def test_check_locationType(self):
        postcode=check_locationType('se1 3bd')
        expected_p='SE1 3BD'
        city=check_locationType('london')
        expected_c='London'
        postcode_w=check_locationType('se13')
        
        self.assertEqual(postcode,expected_p)
        self.assertEqual(city,expected_c)
        self.assertFalse(len(postcode_w)<5)
        
#User input tests
    def test_get_userSurname(self):
        self.assertRaises(ValueError,int,get_userSurname())
        self.assertTrue(get_userSurname())
        
    def test_get_userLocation(self):
        self.assertRaises(ValueError,int,get_userLocation())
        
    def test_initial_askSort(self):
        result=initial_askSort()
        self.assertIsInstance(result,int)
        
    def test_ask_sort(self):
        result=askSort()
        self.assertIsInstance(result,int)
        
           
if __name__=='__main__':
    unittest.main()