# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:03:33 2019

@author: saras
"""

class Person():
    def __init__ (self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def 
    
        print(self.name,self.age,self.gender)        
    
    def changeName(self, newName):
        self.name = newName

    def tenperless(self, salary):
        self.newSalary = salary-(salary*0.10)
       
#looking for a funcion named main, if not will sart running at the top of the script   
if __name__ == "__main__": 
    aminat = Person("Aminat", 20 "Female") 
    aminat.getDetails()
    aminat.changeName("Aminat2")  
 #Good practice to have this in OOP. To do something as above is just the blueprint, not linked to any specific function or class. Links to the main function of the whole script if this is not defined the will take the first function. Here there is no main at the moment.   