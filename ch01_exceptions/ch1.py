# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:14:38 2019

@author: saras
"""


##TASK 1 -  meaningful & precise error messages

##incorrect code:

#f = open('testfile')
##prints: [Errno 2] No such file or directory: 'testfile'
##this is not in plain English


##still incorrect code: 

#try:
#    f = open('testfile')
#except Exception:
#    print('Error!')    
##when file called testfile.txt is called incorrectly, prints: Error!


##still incorrect code but written a more comprehensive error message:

#try:
#    f = open('testfile')
#except Exception:
#    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
#prints: Sorry, this file does not exist, or the file name is wrong. Please double check. 


##Now with the correct code:

#try:
#    f = open('testfile.txt')
#except Exception:
#    print('Error!') 
##when the file name correct prints no error
    
    
   
##TASK 2 -  multiple errors/exceptions


##define a wrong variable:
#try:
#    f = open('testfile.txt')
#    s1 = not_exsit
#except Exception:
#    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
##if we wrote the correct file name, but this time defined a wrong variable right afterwards it still prints the same error message as above. Even though the open file function has passed correctly 



##To solve the above we can use specific exceptions to filter out the error reporting process: e.g. change ‘Exception’ to ‘FileNotFoundError’:
#try:
#    f = open('testfile.txt')
#    s1 = not_exsit
#except FileNotFoundError:
#    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
##prints: NameError: name 'not_exsit' is not defined


##The ‘Exception’ key word was used for general exceptions, and ‘FileNotFoundError ‘is one of the built in exceptions. 
##print(math.sqrt(-1)) is a ValueError.
##1+2+’three’ is a TypeError.
##1/0 is a ZeroDivisionError.
##For i in range (5), forget ‘:’ is a SyntaxError.    


##Multiple exceptions
##If you would like to have all pre-written error messages rather than default Python errors, you can go through multiple exceptions.
#try:
#    f = open('testfile.txt')
#    s1 = not_exsit
#except FileNotFoundError:
#    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
#except Exception:
#    print('Sorry. Something is wrong after opening function.')
#
###when no file called testfile.txt, prints: Sorry, this file does not exist, or the file name is wrong. Please double check.  
###when there is a file called testfile.txt prints: Sorry. Something is wrong after opening function.    



   
##TASK 3 -  using variable to automatic raise exceptions
   
#try:
#    f = open('testfile.txt')
#    s1 = not_exist
#except Exception as e:
#    print(e)
##e is a variable that represents anything wrong, the system will then print the actual error if there is something wrong in the try block.
##Prints: name 'not_exist' is not defined 


   
##TASK 4 - else block

##When used in exceptions, the else block is more to confirm whether code is correct than to actually do something after it passes. 
##The else clause will be executed if the try block does not raise an exception.

#try:   
#    f = open('testfile.txt')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()
##prints out the information inside the text file: ï»¿testing exceptions 



###TASK 5 - finally block, test with error and without error

##with error:
try:
    f = open('testfile')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('executing finally…')
    
##prints:   [Errno 2] No such file or directory: 'testfile'
            #executing finally…

##without error:
try:
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('executing finally…')
 
##prints:    ï»¿testing exceptions
            #executing finally…
  
 
    
##TASK 6 - manually raise an exception
    
try:
    f = open('testfile.txt')
    if f.name == 'testfile.txt':
        raise Exception
except Exception as e:
    print('File names are the same!')

##prints: File names are the same!
            
            
            
            
            
