# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:34:04 2019

@author: saras
"""

##TASK 1

#Ask for user input with a pre-coded new line:

#print("What’s your age?")
#Age = input()

#Ask for user input with a pre-coded space:
#Age = input("What’s your age? ")
#print(type(Age)) #prints: <class 'str'>  Output data type is string. ALL user input is a string. 



##TASK 2:

#write a function to cast into an integer, a few different ways to do this:

#print("What’s your age?")
#Age = int(input())
#print(type(Age)) #prints <class 'int'>
#
#Age = int(input("What’s your age? "))  # this is the best version as it has less steps
#print(type(Age)) #prints <class 'int'>

#or cast variable:

#Age = input("What’s your age? ")
#Age_int = int(Age)
#print(type(Age_int))



##TASK 3:

#Option = input("Please input yes or no \n").lower()
#print(Option)

#Option = input("Please input yes or no \n").upper()
#print(Option)


##TASK 4: An example for validating string length
#page 30 to do

password = input("What’s your password? \n")
if len(password) <=7:
    print("Password must be minimum 8 characters long")
else:
    print("That's 'A-OK'! Thanks!")





















