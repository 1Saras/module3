# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:54:04 2018

@author: saras
"""


def passwordCheck(truePasscode, balance):
    attemptcounter = 3
    while attemptcounter > 0:
        userattempt = input('Please enter your password ')
        if userattempt != truePasscode:
            attemptcounter = attemptcounter -1        
        else: 
            return ask_transaction(balance)                        
    print("You've used up all your attempts - sorry")
  
 
def ask_transaction(balance):
    ask = 0   
    while True:
        try:
            while ask < 1 or ask > 3:    
                print ('Which transaction would you like you carry out? Please input the number 1 or 2. To quit enter 3')    
                print ('1 Check balance')
                print ('2 Purchase data bundle')
                print ('3 To quit')
                ask = int(input())
            break
        except ValueError:
            print('Please type 1, 2 or 3 only! \n')                
    if ask == 1:
        print ('Your balance is {}'.format(balance)) 
    elif ask == 2:   
        return checkPhoneNo(balance)
    elif ask ==3:
        print('Thanks - you are now logged out')
    else:
        print ('You must input the number 1, 2 or 3')


def checkPhoneNo(balance):
    number1="1"
    while len(number1) !=11 or number1[0] !="0":    
        number1 = input('Please type your mobile number: \n')
    number2 = input('Please type your mobile number again: \n')   
    while number1 != number2:
        number2 = input('Your phone numbers do not match - please type your mobile number again: \n') 
    checkCredit(balance)    



def checkCredit(balance):
    maxpurchase=100   
    while True:
        try:
            creditpurchase=int(input('How much credit would you like to purchase? Your input must be a multiple of 5:\n£'))
            while creditpurchase > maxpurchase or creditpurchase > balance or creditpurchase %5!=0 or creditpurchase <0:
                if creditpurchase > maxpurchase:
                    creditpurchase=int(input('Your input must be less than £100. Please re-enter an amount: \n£'))
                elif creditpurchase > balance:
                    creditpurchase=int(input('Your input must be less than your current balance. Your balance is £{}.\nPlease re-enter an amount: \n£'.format(balance)))
                elif creditpurchase %5!=0:
                    creditpurchase=int(input('Your input must be a multiple of 5. Please re-enter an amount: \n£'))
                elif creditpurchase <0:
                    creditpurchase=int(input('Your input must be a positive number. Please re-enter an amount: \n£'))
            break 
        except ValueError:
            print('Please enter a number')
    calculate_new_balance(creditpurchase, balance)


def calculate_new_balance(creditpurchase, balance):
    balance = round((balance - creditpurchase),2)
    print ('Congrats on your credit purchase.\nYour balance is now £{}.'.format(balance))
    
    
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    


    