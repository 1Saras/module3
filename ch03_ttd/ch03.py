# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:19:49 2019

@author: saras
"""

#The advantages of TDD:

#-matches the ideals and principles of the Agile Development process, by delivering incremental updates to a product with quality, not quantity
#-makes the developer consider different routes through the code and create tests
#-ensures code works prperly under given set of conditions 
#-allows to ensure hat changes to the code won't break exising functionality
#-makes you think about the code under unusual conditions, potentially revealing logical errors
#– Before writing code, it forces you to detail your requirements in a useful fashion.
#– While writing code, it keeps you from over-coding. When all the test cases pass, the function is complete.
#– When refactoring code, it assures you that the new version behaves the same way as the old version.
#– When maintaining code or writing code in a team, it increases confidence that the code you are committing will not break other people’s code, as you can run their unit tests first 




#Step-by-step TDD procedure:

#– Write a test
#– Test fails as there is no code
#– Write the minimum code to make the test pass
#– Write another test
#– Test fails
#– Adapt and extend current code
#– Repeat until you can write no more tests




#Pair programming in TTD:

#-one person could write the unit test, see it fail, then allow the other developer to write the code to pass the test.
#-roles can be switched as often as you see fit. This helps both parties in the pair to stay engaged, focused on what they are doing, and checking each other’s work at every stage.
#-Test code is just as important as production code, so it requires the same level of thought, design, and care




#Why always write to expect a failure?

#-you write a test before writing the development code, so you should have expected failure. This means that the test fails in the way that you expect it to.
#Building this habit gives you a safe scenario.

