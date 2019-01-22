# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:14:38 2019

@author: saras
"""

##TASK 1
#
#try:
#    f = open('testfile.txt')
#except Exception:
#    print('Error!') 

#when no file called testfile.txt, prints: Error!
#when there is a file called testfile.txt prints nothing


   
##TASK 2

#try:
#    f = open('testfile.txt')
#    s1 = not_exsit
#except FileNotFoundError:
#    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
#except Exception:
#    print('Sorry. Something is wrong after opening function.')

##when no file called testfile.txt, prints: Sorry, this file does not exist, or the file name is wrong. Please double check.  
##when there is a file called testfile.txt prints: Sorry. Something is wrong after opening function.    
   
    
    
##TASK 3
    
#try:
#    f = open('testfile.txt')
#    s1 = not_exist
#except Exception as e:
#    print(e)
 
##Prints: name 'not_exist' is not defined 

   
    
##TASK 4 - else block

#try:   
#    f = open('testfile.txt')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()

#prints: ï»¿testing exceptions 



##TASK 5 - finally block, test with error and without error

##with error:
#try:
#    f = open('testfile')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()
#finally:
#    print('executing finally…')
    
##prints:   [Errno 2] No such file or directory: 'testfile'
            #executing finally…

##without error:

#try:
#    f = open('testfile.txt')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()
#finally:
#    print('executing finally…')
 
#prints:    ï»¿testing exceptions
            #executing finally…
  
 
    
##TASK 6 - manually raise an exception
    
#try:
#    f = open('testfile.txt')
#    if f.name == 'testfile.txt':
#        raise Exception
#except Exception as e:
#    print('File names are the same!')

#prints: File names are the same!
            
            
            
            
            
