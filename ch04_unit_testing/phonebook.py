# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:55:32 2019

@author: amina
"""
import string
import sqlite3
import os
db_path = '../phonebook.db'

#DATABASE RETRIEVAL
def check_db():
    if os.path.exists(db_path):
        return True
    else:
        return False

def getdb():
    conn=sqlite3.connect(db_path)
    c=conn.cursor()
    return (c,conn)

def findPeople():
    c,conn=getdb()
    c.execute('SELECT * FROM phonebookpeople INNER JOIN postcodes ON postcodes.Postcode=phonebookpeople.Postcode')  
    results_people=c.fetchall()
    return results_people

def findBusiness():
    c,conn=getdb()
    c.execute('SELECT * FROM phonebookbusiness INNER JOIN postcodes ON postcodes.Postcode=phonebookbusiness.Postcode')  
    results_business=c.fetchall()
    return results_business

#VALIDATION FUNCTIONS 
def has_numbers(inputStr):
    for char in inputStr:
        if char.isdigit():
            return True
    return False

def has_symbols(inputStr):
    invalidSymbols = set(string.punctuation)
    for char in inputStr:
        if char in invalidSymbols:
            return True
    return False

def has_symbols_excludeHyphens(inputStr):
    invalidSymbols = set(string.punctuation.replace('-',''))
    for char in inputStr:
        if char in invalidSymbols:
            return True
    return False
        
def check_locationType(searched_location):
    if has_numbers(searched_location):
        while len(searched_location)<5:
            print('Invalid Postcode provided. Please enter a full postcode (e.g. AB12 3DB)')
            searched_location=get_userLocation()   
        searched_location=searched_location.upper()
    else:
        searched_location=searched_location.title()
    return searched_location

#GET AND VALIDATING USER INPUT

def get_userSurname():
    searched_surname=input('Enter Surname: ').title()
    while has_numbers(searched_surname) or has_symbols_excludeHyphens(searched_surname) or searched_surname=='':
        check_userSurname(has_numbers,has_symbols_excludeHyphens, searched_surname)
        searched_surname = input('Enter Surname: ').title()
    return searched_surname

def get_userLocation():
    searched_location = input('Enter Town, City or Postcode: ')
    while searched_location.isdigit() or has_symbols(searched_location) or searched_location=='':
        check_userLocation(has_symbols, searched_location)
        searched_location = input('Enter Town, City or Postcode: ')
    return check_locationType(searched_location)

#SORTING FUNCTIONS

def initial_askSort():
    try:
        ask=int(input('How would you like to sort the results? Please enter the number 1 or 2.\n1. Sort by Distance.\n2. Sort by Alphabetical order\n'))        
    except ValueError:
        ask=0  
    return ask  

def askSort():
    ask=initial_askSort()
    while ask < 1 or ask > 2:
        print("Please enter '1' or '2' only!\n")                
        ask=initial_askSort()
    return ask

