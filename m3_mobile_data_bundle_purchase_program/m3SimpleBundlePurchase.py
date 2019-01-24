# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:54:04 2018

@author: saras
"""


"""
Creating an empty function
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
            while ask < 1 or ask > 2:    
                print ('Which transaction would you like you carry out? Please input the number 1 or 2')    
                print ('1 Check balance')
                print ('2 Purchase data bundle')
                ask = int(input())
            break
        except ValueError:
            print('Please type 1 or 2 only! \n')                
    if ask == 1:
        print ('Your balance is {}'.format(balance)) 
    elif ask == 2:   
        return checkPhoneNo(balance)
    else:
        print ('You must input the number 1 or 2')


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
    calculate_new_balance(creditpurchase, balance)


def calculate_new_balance(creditpurchase, balance):
    balance = round((balance - creditpurchase),2)
    print ('Congrats on your credit purchase.\nYour balance is now £{}.'.format(balance))
    
    
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    


    