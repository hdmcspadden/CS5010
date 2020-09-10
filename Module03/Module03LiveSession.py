# -*- coding: utf-8 -*-
"""
Name of Activity: Module 03: Live Session Exercise: Exception Handling
Name: Diana McSpadden
UID: hdm5s

@author: Diana McSpadden

Write some code using try-except-finally blocks that has the potential to throw a lot of errors. 
Include the following "except" blocks: 
 
*Exception (all built-in exceptions are derived from this class — yes, it's simply called "Exception")
*TypeError
*ValueError
*ZeroDivisionError
*FileNotFoundError
*IOError
ArithmeticError
Your task is to figure out the appropriate order of these "except" blocks so that 
no "except" block is unreachable.
 
Test your code out by running it multiple times and allowing your code to encounter various kinds of exceptions (you can do this by incorporating user input or otherwise.) Have unique bodies of code in each of the "except" blocks (at the very least, different print() statements), and run your code enough times and force your code to encounter the various kinds of exceptions such that output from EACH "except" block is printed, proving that no "except" block is unreachable.
"""

i = 0
j = 0
k = 0
m = 0
n = 0
p = 0
q = 0

def exceptionGauntlet():
    '''
    I want to throw each error once. In order to test, 
    you will need to generate each error one time to not be prompted with the "input" statement again.
    '''
    global i 
    global j
    global k
    global m
    global n
    global p
    global q
    
    output = None
    
    try:
        # try to get a type error
        if (i == 0):
            raise TypeError("This is a Type exception.")
        
        # try to get a value error
        if (j == 0):
            inputValueError = input("I am going to try to make this a number: ")
            tryNumber = int(inputValueError)
        
        # try to get a zero division error
        if (k == 0):
            inputZeroDivError = input("Divide by what number? ")
            tryZeroDiv = 2 / int(inputZeroDivError)
        
        # try to get an arithmetic error
        if (m == 0):
            raise ArithmeticError("This is an arithmetic exception.")
        
        # try to get a file not found error
        if (n == 0):
            inputFileName = input("What file should we open? ")
            file = open(inputFileName, 'r')
            file.close()
        
        # try to get an IO Error
        if (p == 0):
            raise IOError("This is an IO/OS exception.")
        
        # try to get a General Exception
        if (q == 0):
            raise Exception("This is a general exception.")
        
    
    # when each error is caught in its except, set the output variable to the text of the error
    except TypeError as errType:
        i += 1 # increment i
        output = "This is a Type Error: " + str(errType)
    
    except ValueError as errValue:
        j += 1 # increment j
        output = "This is a Value Error: " + str(errValue)
        
    except ZeroDivisionError as errZeroDivision:
        k += 1 # increment k
        output = "This is a Divide by Zero Error: " + str(errZeroDivision)
    
    except ArithmeticError as errArithmetic:
        m += 1 # increment m
        output = "This is an Arithmetic Error: " + str(errArithmetic)
        
    except FileNotFoundError as errFileNotFound:
        n += 1 # increment n
        output = "This is a File Not Found Error: " + str(errFileNotFound)
    
    except IOError as errIO:
        p += 1 # increment p
        output = "This is an IO/OS Error: " + str(errIO)
    
    except Exception as errException:
        q += 1 # increment q
        output = "This is a General Exception: " + str(errException)
    finally:
        if (output == None):
            print("You completed the Exception Gauntlet")
        else:
            print("You encountered an error: ", output)
            exceptionGauntlet()
    
    return None
    
# Run the Exception Gauntlet
exceptionGauntlet()