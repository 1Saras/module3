# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:54:04 2018

@author: saras
"""


"""
Creating an empty function
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
            return ask_transaction(balance)
    else:
        return 'Wrong password'


def passwordCheck(truePasscode):
    attempt = input('Please enter your password ')
    if attempt == truePasscode:
        return True
    else:
        return False
    
    
def ask_transaction(balance):
    print ('Which transaction would you like you carry out? Please input the number 1 or 2')
    print ('1 Check balance')
    print ('2 Purchase data bundle')
    ask = input()
    if ask == '1':
        print ('Your balance is {}'.format(balance)) 
    elif ask == '2':   
        return checkPhoneNo(balance)
    else:
        print ('You must input the number 1 or 2')


def checkPhoneNo(balance):
    maxpurchase=100
    number1 = input('please type your phone number: ')
    number2 = input('please type your phone number again: ')
    if number1 == number2: 
        creditpurchase=int(input('How much credit would you like to purchase? Your input must be a multiple of 5: '))
        if creditpurchase > maxpurchase:
            print ('You can only top up to £100')
        elif creditpurchase > balance:
            return ('You do not have enough balance')
        else:
            multiple_of_five(creditpurchase)
    else:
        return ('Your phone numbers do not match')
    

def multiple_of_five(creditpurchase):
    if creditpurchase %5==0:
        print ('Congrats you can purchase')
    else:
        print ('Amount entered must be a multiple of 5')
    
    
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False