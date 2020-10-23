# -*- coding: utf-8 -*-
"""
Activity: Homework 4: Testing and Debugging
Name: H. Diana McSpadden
UID: hdm5sI 
"""

# This is the test code for the ACCOUNTING and CHECKING CLASSES
"""
Instructions:
    Refer to your written solution and write no fewer than two (2) unit tests for each method. 
    You do not need to test the “toString” (__str__) methods.
"""

import io # need for testing scenarios that test printed output
import sys # need for testing scenarios that test printed output
import unittest # import unittest library
from ACCOUNT_CHECKING_CLASS import * # import my python code for the ACCOUNT and derived CHECKED classes


# Class for testing ACCOUNT classes.
class AccountTestCases(unittest.TestCase): # inherit from unittest.TestCase
    # Unit testing courses list in AStudent_Class.py
    
    # used setUp - which runs each time a unit test method is called to set some fixutres
    # because I wanted to see how this works
    def setUp(self):
        self.non_float_balance_message = "Balance must be a valid dollar amount.\n"
    
    # __init__ TEST CASE #1
    def test_is_account_initialize_with_expected_values(self):
        # is ACCOUNT initialize with the values supplied

        # Set up
        accnt1 = ACCOUNT("1234","2000.34")
               
        # Test
        # Are the accountNumber and balance set as expected?
        self.assertEqual(str(accnt1.accountNumber) + ", " + str(accnt1.balance), '1234, 2000.34') 
     
    # __init__ TEST CASE #2
    def test_is_account_balance_must_initialize_a_float(self):
        # Does a non-float balance input result in the expected printed error message

        # Set up
        testAccountNumber = 1234
        testAccountBalance = "abcd" # this account balance must throw a value error
        
        originalStdOutput = sys.stdout # save original stdoutput
        capturedOutput = io.StringIO() # create StringIO object to capture print output
        sys.stdout = capturedOutput # redirect stdout.
        
        #call the initialize to capture the printed output
        ACCOUNT(testAccountNumber,testAccountBalance)
        
        sys.stdout = originalStdOutput # reset stdoutput
               
        # Is printed output from the non-float balance returned as expected?
        self.assertEqual(self.non_float_balance_message,capturedOutput.getvalue())
        
       
# Class for testing CHECKING classes.     
class CheckingTestCases(unittest.TestCase): # inherit from unittest.TestCase

    # used setUp - which runs each time a unit test method is called to set some fixutres
    # because I wanted to see how this works
    def setUp(self):
        self.check1AccountNumber = "1234" # check1 initialization value
        self.check1Balance = "2000.34" # check1 initialization value
        self.badWithdrawalAmount = 2000.35 # an overage withdrawal amount from the initialize balance
        self.check1Fee = "5.12" # check1 initialization value
        self.check1Attributes = "1234, 2000.34, 5.12" # expected string of check1 initialized values
        self.balanceValueErrorMessage = "Deposit amount must be valid positive dollar amount.\n" # Expected print statement if balance input for deposit is not a valid deposit amount
        self.withdrawlInsufficientFundsMessage = "Insufficient funds\n"
        self.withdrawalValueErrorMessage = "Withdrawal amount must be a valid dollar amount.\n"


    # __init__ TEST CASE #1
    def test_is_checking_initialize_with_expected_values(self):
        # is ACCOUNT initialize with the values supplied

        # Set up
        check1 = CHECKING(self.check1AccountNumber,self.check1Balance,self.check1Fee)
               
        # Test
        # Are the accountNumber and balance set as expected?
        self.assertEqual(str(check1.accountNumber) + ", " + str(check1.balance) + ", " + str(check1.fee), self.check1Attributes) 

    #__init__ TEST CASE #2
    def test_is_checking_intializing_each_checking_class_separately(self):
        # Set up first check object
        check1 = CHECKING(self.check1AccountNumber,self.check1Balance,self.check1Fee)
        #create another check object with different values
        check2 = CHECKING("1","2","3")
               
        # Test
        # Is the check1 object still setup as expected
        self.assertEqual(str(check1.accountNumber) + ", " + str(check1.balance) + ", " + str(check1.fee), self.check1Attributes)

    def test_getFee_returning_expected_fee(self):
        # Set up first check object
        check1 = CHECKING(self.check1AccountNumber,self.check1Balance,self.check1Fee)
        
        self.assertEqual(check1.fee, 5.12)
            
    def test_getFee_returning_two_decimal_place_fee(self):
        # Set up first check object with a non-2-decimal-place fee
        check1 = CHECKING(self.check1AccountNumber,self.check1Balance,5)
        
        # Test
        # Is the fee returned with two decimal places
        self.assertEqual(check1.fee, 5.00)
    
    def test_deposit_amount_is_not_zero(self):
        # Does a deposit of 0 produce expected printed error message
        
        originalStdOutput = sys.stdout # save original stdoutput
        capturedOutput = io.StringIO() # create StringIO object to capture print output
        sys.stdout = capturedOutput # redirect stdout.
        
        #call the initialize to capture the printed output
        check1 = CHECKING(self.check1AccountNumber,self.check1Balance,self.check1Fee)
        check1.deposit(0) # this zero deposit amount should print the expected error message
        
        sys.stdout = originalStdOutput # reset stdoutput
               
        # Is printed output from the non-float balance returned as expected?
        self.assertEqual(self.balanceValueErrorMessage,capturedOutput.getvalue())
    
    def test_deposit_amount_is_not_negative(self):
        # Does a deposit of a negative amount produces expected printed error message
        
        originalStdOutput = sys.stdout # save original stdoutput
        capturedOutput = io.StringIO() # create StringIO object to capture print output
        sys.stdout = capturedOutput # redirect stdout.
        
        #call the initialize to capture the printed output
        check1 = CHECKING(self.check1AccountNumber,self.check1Balance,self.check1Fee)
        check1.deposit(-50.55) # this negative deposit amount should print the expected error message
        
        sys.stdout = originalStdOutput # reset stdoutput
               
        # Is printed output from the non-float balance returned as expected?
        self.assertEqual(self.balanceValueErrorMessage,capturedOutput.getvalue())
        
    def test_withdrawl_amount_is_not_negative(self):
        # Does a withdrawal of a negative amount produces expected printed error message
        
        originalStdOutput = sys.stdout # save original stdoutput
        capturedOutput = io.StringIO() # create StringIO object to capture print output
        sys.stdout = capturedOutput # redirect stdout.
        
        #call the initialize to capture the printed output
        check1 = CHECKING(self.check1AccountNumber,self.check1Balance,self.check1Fee)
        check1.withdrawal(-1) # this negative withdrawal amount should print the expected error message
        
        sys.stdout = originalStdOutput # reset stdoutput
               
        # Is printed output from the non-float balance returned as expected?
        self.assertEqual(self.withdrawalValueErrorMessage,capturedOutput.getvalue())
    
    def test_withdrawl_insufficient_funds_message(self):
        # Does an attempted withdrawal of more than balance amount produce expected error
        
        originalStdOutput = sys.stdout # save original stdoutput
        capturedOutput = io.StringIO() # create StringIO object to capture print output
        sys.stdout = capturedOutput # redirect stdout.
        
        #call the initialize to capture the printed output
        check1 = CHECKING(self.check1AccountNumber,self.check1Balance,self.check1Fee)
        check1.withdrawal(self.badWithdrawalAmount)
        
        sys.stdout = originalStdOutput # reset stdoutput
               
        # Is printed output from the non-float balance returned as expected?
        self.assertEqual(self.withdrawlInsufficientFundsMessage,capturedOutput.getvalue())
        
        
if __name__ == '__main__':
    unittest.main()  

