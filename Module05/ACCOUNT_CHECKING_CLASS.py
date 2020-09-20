"""
Activity: Homework 4: Testing and Debugging
Name: H. Diana McSpadden
UID: hdm5s
"""


#%%
#Classes and Inheritance: (4 pts)
''' 
Create a base class called ACCOUNT.
Account should have the following attributes: accountNumber and balance, 
which should be correctly initialized in the constructor (_ _init_ _) method for the class.
Create a to-string (_ _str_ _) method that prints “Account number 1234” on one line and “Balance: 2000” 
on the next line (example with account number of 1234 and balance of 2000).
'''

# *** BASE CLASS *** #
class ACCOUNT:
   def __init__(self, accountNumber, balance):  # constructor
        #fields: accountNumber(int), balance (float)"""
         
        self.accountNumber = accountNumber # set account number
        
        # throw exception if balance is not a valid float
        try:
            self.balance = float(balance)
        except ValueError:
            self.balance = 0
            print("Balance must be a valid dollar amount.")
      
   def __str__(self):
        # return account number and balance (balance in 0.00 format)
         return "Account number {} \nBalance: {:.2f}".format(str(self.accountNumber), self.balance)

# create and print the account object                     
#acnt1 = ACCOUNT(1234, 2000)
#print(acnt1)
'''
Create another class called CHECKING. This class should inherit from the Account class. 
Therefore, the Checking class is the derived class.
In addition to the accountNumber and balance attributes, the Checking class has a fee attribute 
(that is used when withdrawing money from the Checking account). 
Initialize all variables correctly in the constructor (_ _init_ _) method.
Create a to-string method (_ _str_ _) that is identical to the two-line to-string method of the 
Account class, but has an additional header (a new first line): "Account type: Checking". 
Therefore, the to-string method of this class should produce a three-line output.
Add a method getFee(self) that returns the fee attribute (remember to use: self.fee).
Add a method deposit(self, amount) that adds the "amount" to the balance. 
It doesn't produce any output or return anything.
Add a method withdraw(self, amount) that does the following:
    (1) checks to see if the amount to withdraw + fee is greater than the balance;
    if so, display a message "Insufficient funds!", 
    (2) otherwise, adjust the balance so that the amount AND the fee are subtracted. 
    (Remember when you make a withdrawal, there is a fee involved that also needs to be subtracted from the balance. -- Example: Balance is $500. If you want to withdraw $100, and if the fee is $10, the method checks 110 is not greater than 500, so the resulting balance will be 500 - 100 - 10, so balance = $390.)
To test this out: 
    (1) create an instance of the Checking class 
    (call it check1) with account number 1234 and a balance of 500 with a fee of 0.50, 
    (2) print check1 out, 
    (3) withdraw $100, 
    (4) print check1 out, 
    (5) deposit $200, 
    (6) print check1 out.
'''

## TO DO: COMMENT CODE, ADD INT, FLOAT ERROR HANDLING, PRINT 0.00 format for balances

class CHECKING(ACCOUNT):
    def __init__(self, accountNumber, balance, fee):  # constructor
      ACCOUNT.__init__(self, accountNumber, balance) # call base class constructor
      
      # validate that fee is a valid float
      try:
          self.fee = float(fee) # fee property added to the checking class
      except ValueError:
          self.fee = 0
          print("Fee must be a valid dollar amount.")
        
    def __str__(self):
      # add the Account type: Checking to the __str__ of the base class
      strReturn = "Account type: Checking\n" # additional part of __str__ for the checking class
      strReturn += ACCOUNT.__str__(self)
      return strReturn
      
    def getFee(self):
        # return the fee for the object
        return round(self.fee, 2)
    
    def deposit(self, amount):
        # throw exception if amount is not valid float
        # if valid add the deposit amount to the balance        
        try:
            # set local deposit amount to float of amount. 
            # This will throw a Value Error if amount cannot be a valid float
            depositAmount = float(amount)
            if (depositAmount < 0.00001): # Test if depositAmount > 0.00001
                raise ValueError()
            
            self.balance += depositAmount # add the deposit amount to self.balance
        except ValueError:
            print("Deposit amount must be valid positive dollar amount.")
        
    def withdrawal(self, amount):
        # check the current balance
        
        # throw error is amount is not a valid dollar amount
        # else, check balance, if enough, then deduct from balance, else return Insufficient funds message
        try:
            # set local withdrawal amount to float of amount. 
            # This will throw a Value Error if amount cannot be a valid float
            withdrawalAmount = float(amount)
            
            if (withdrawalAmount <= 0 ): # Test if withdrawalAmount <= 0
                raise ValueError()
            
            if(float(amount) + self.fee > self.balance):
                print("Insufficient funds") # not enough funds
            else:
                self.balance = self.balance - self.fee - amount # deduct the withdrawal from self.balance
        except ValueError:
            print("Withdrawal amount must be a valid dollar amount.")