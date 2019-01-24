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



##TASK 3: Validating string content

#Option = input("Please input yes or no \n").lower()
#print(Option)

#Option = input("Please input yes or no \n").upper()
#print(Option)


##TASK 4: Validating string length

#password = input("What’s your password? \n")
#if len(password) <=7:
#    print("Password must be minimum 8 characters long")
#else:
#    print("That's 'A-OK'! Thanks!")


##TASK 5 & 6 - while true input validation

choice = 0
while True:
    try:
        while choice < 1 or choice > 3:
            print('***choice****')
            print('1. Display my name')
            print('2. Display my age')
            print('3. Display my city')
            choice = int(input('What is your choice? \n'))  
        break
    except ValueError:
        print('Please type number 1, 2 or 3! \n')
if choice == 1:
    print('Your name is: Sarika')
elif choice == 2:
    print('You are: 20 years old')
elif choice == 3:
    print('Your city is: London')


##TASK 7 - OOP user input validation

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













