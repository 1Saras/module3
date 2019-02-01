# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:58:00 2019

@author: saras
"""

class Calculator(object):
#    def add(self, x, y):
#        Pass
    def add(self,x,y):
        return x+y
    def multiply(self,x,y):
        return x*y
    def subract(self,x,y):
        return x-y

if __name__=='__main__':
    unittest.main()