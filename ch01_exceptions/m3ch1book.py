# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:51:40 2019

@author: saras
"""

#TASK 1

try:
    f = open('testfile.txt')
    s1 = not_exists
except Exception as e:
    print(e)  
#prints: [Errno 2] No such file or directory: 'testfile.txt'

    

#TASK 2
    
#try:
#    f = open('testfile.txt')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()   


  
#TASK 3 
#try:
#    f = open('testfile')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()
#finally:
#    print('Executing finally…')
#    
#try:
#    f = open('testfile.txt')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()
#finally:
#    print('Executing finally…')
    
#try:
#    f = open('testfile.txt')
#    if f.name == 'testfile.txt':
#        raise Exception
#except Exception as e:
#    print('File name are the same')  
    
    