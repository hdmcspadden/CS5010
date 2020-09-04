# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:29:59 2020

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

def exceptionGauntlet():
    output = None
    try:
        # try to get a type error
        #  couldn't figure out how to use user input to generate this
        
        # try to get a value error
        inputValueError = input("I am going to try to make this a number: ")
        tryNumber = int(inputValueError)
        
        # try to get a zero division error
        inputZeroDivError = input("Divide by what number? ")
        tryZeroDiv = 2 / int(inputZeroDivError)
        
        # try to get an arithmetic error
        
        
        # try to get a file not found error
        inputFileName = input("What file should we open? ")
        file = open(inputFileName, 'r')
        file.close()
        
        # try to get an IO Error
        
        # try to get a general Exception
        
    
    except TypeError as errType:
        output = errType
    
    except ValueError as errValue:
        output = errValue
        
    except ZeroDivisionError as errZeroDivision:
        output = errZeroDivision
    
    except ArithmeticError as errArithmetic:
        output = errArithmetic
        
    except FileNotFoundError as errFileNotFound:
        output = errFileNotFound
    
    except IOError as errIO:
        output = errIO.message
    
    except Exception as errException:
        output = errException
    finally:
        if (output == None):
            print("You completed the Exception Gauntlet")
        else:
            print("You encountered an error: ", output)
            exceptionGauntlet()
    
    return None
    
# Run the Exception Gauntlet
exceptionGauntlet()