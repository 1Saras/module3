# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:24:31 2019

@author: saras
"""

#print("What’s your age?")
#age = input()

#age = int(input("What’s your age? \n"))
#print(type(age))

#option = input("Please input yes or no \n").lower()
#print(option)
#
#'ASBnda'.lower()
##prints: 'asbnda'
#
#'ASBnda'.upper()
##prints: 'ASBNDA'


##TASK 1

#age = int(input("What’s your age? \n")
#if len(userInput) ==3:



##TASK 2 - USING WHILE TRUE INFINITE LOOP

#choice = 0
#while choice < 1 or choice > 3:
#    print('***choice****')
#    print('1. Display my name')
#    print('2. Display my age')
#    print('3. Display my city')
#    choice = int(input('What is your choice? '))   
#    if choice == 1:
#        print('Ms Wu')
#    elif choice == 2:
#        print('5 years old')
#    elif choice == 3:
#        print('London')

#will get error if input is a string (or anything but an int)
  

      
#Handling errorful input of a word e.g. three:


#choice = 0
#while True:
#    try:
#        while choice < 1 or choice > 3:
#            print('***choice****')
#            print('1. Display my name')
#            print('2. Display my age')
#            print('3. Display my city')
#            choice = int(input('What is your choice? \n'))  
#        break
#    except ValueError:
#        print('please type a number! \n')
#if choice == 1:
#    print('Your name is: Ms Wu')
#elif choice == 2:
#    print('You are: 5 years old')
#elif choice == 3:
#    print('Your city is: London')
    


#Futher on validation
#CLASS -BASED USER INPUT VALIDATION

class Spam(object):
    def __init__(self, description, value):
        if not description or value <= 0:
            raise ValueError
        self.description = description
        self.value = value
s = Spam('s', 5)
print(s.value) #prints 5, if input is <=0 then will print raise ValueError


#assert statement:

class Spam(object):
    def __init__(self, description, value):
        assert description != ""
        assert value > 0
        self.description = description
        self.value = value













