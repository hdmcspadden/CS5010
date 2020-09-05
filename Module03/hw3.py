# -*- coding: utf-8 -*-
"""
Name of activity: Homework 2: Python I (Module 3))
Name: H. Diana McSpadde
UID: hdm5s

Date: 9/6/2020

@author: Diana McSpadden
"""

#%%
# Q1: Dictionary basics: (2 pts)
''' 
Create a dictionary of 10 key-value pairs. Choose a domain that interests you. What might you want to look up?
'''
dictFavoriteSongs = {0:"Castanets",1:"Soy Yo",2:"Ooh La La", 3:"Long Slow Goodbye", \
                     4:"Respect", 5:"Let My People Go", 6:"Working Woman",7:"Lust For Life", \
                     8:"99 Pounds",9:"Girls Just Wanna Have Fun"}

#print(dictFavoriteSongs)
'''
Demonstrate retrieving at least three different values.
Display each of the results.
'''

print("One of my favoritesong is '{}'.".format(dictFavoriteSongs[0]))

print("A great song fro the 1980's is '{}'.".format(dictFavoriteSongs.get(9)))

i = 1
for song in dictFavoriteSongs:
    print("Fav song #{0}: {1}".format(str(i),dictFavoriteSongs[song]))
    i+=1

#%%
#Q2: Getting user input: (2 pts)
''' 
Ask user for his or her name and two numbers (separately).
'''
responseName = input("What is your name? ")

responseNumber1 = float(input("Give me a number, any number: "))

responseNumber2 = float(input("And another number, any number: "))
'''
Multiply the two numbers.
'''
multNumbers = responseNumber1 * responseNumber2
'''
Display an output like the following: Hi, <NAME>! Multiplying <NUM1> and <NUM2> is: <RESULT>
Display the result as a floating-point number (not an integer).
'''
print("Hi, {name}! Multiplying {num1} and {num2} is: {result}".format(name=responseName,num1=responseNumber1,num2=responseNumber2,result=float(multNumbers)))

#%%
#Q3: Converting code to use a while loop: (3 pts)
''' 
Rewrite the guessing game using a while loop (code in pyScript08.py 
-- Guessing game that asks the user to guess "What is the name of the computer that played on Jeopardy?")
You may need to use if statements in this solution.
You may need to use the break statement or the continue statement in this solution
Remember to mimic the print statements after each try exactly like the original code 
(therefore, remember to keep track of which try the guesser is on to output the appropriate response).
'''
print("Here is a guessing game. Try until you get it right.")
tries = 0
answer = "Diana"
response = ""
while response != answer:
    tries += 1
    response = input("This is try number {}. What is my name? ".format(str(tries)))
    
print("That is right!")
    

#%%
#Q4: Counting each of the vowels: (3 pts)
''' 
Using ONE for-loop, count the number of each of the vowels in a string 
(use the following: sentence = "are you suggesting coconuts migrate")
Display how many a’s, e’s, i’s, o’s, and u’s are in the sentence.
'''
sentence = "are you suggesting coconuts migrate"
dictVowelCount = {"a": 0, "e": 0, "i" : 0, "o": 0, "u": 0}

for letter in sentence:
    if letter in dictVowelCount:
        dictVowelCount[letter] += 1
    
print(dictVowelCount)


#%%
#Q5: Length of all the words in a sentence (based on exercise in pyScript13.py) (3 pts)
'''
Create a long sentence of words (assume NO punctuation).
'''

longsentence = "The Gulf Livestock 1 a 450-foot ship with a cargo of some 5800 cows en route from New Zealand to China issued a distress call early Wednesday Japan time near the island of Amami Oshima north of Okinawa"

'''
Put the words into a list (Hint: How are the words separated?). 
Separating words can be done before the list comprehension.
'''

listLongSentence = longsentence.split(' ')
#print(listLongSentence)

'''
Use a list comprehension to return each word along with the length of it. 
Use: (word, len(word)) in your list comprehension.
'''
words = [[word, len(word)] for word in listLongSentence]
#print(words)

'''
Finally, print out each word and its length (you may use a simple for-loop to do this), 
but sort by smallest size first (Hint: Search for a method that can sort a list. 
What do you have to do when you are trying to sort a list of tuples?w)
'''
def getLength(item):
    return item[0]

words.sort(key=getLength)
#print(words)

for wordlist in words:
    print("{w} is {length} characters in length".format(w=wordlist[0],length=wordlist[1]))

#%%
#Q6: Map-Filter-Reduce examples: (3 pts)
''' 
In the PowerPoint slides describing "higher-order functions" (02-Python - Map Filter Reduce.pdf) 
there are three examples: one illustrating the use of map, the next one illustrating the use of filter, 
and the last one illustrating the use of reduce. 
Rewrite these three examples without using the map(), filter(), and functools.reduce() functions.
'''

# function to square a number.
# will use in rewrite of map functionality
def square(number):
    return number * number 


# function to identify even numbers
# will use in rewrite of the filter functionality
def even(number):
    if number % 2 == 0:
        return True
    else:
        return False 

# function to add two numbers
# will use in rewrite of the reduce functionality
def sum(x,y):
    return x + y

# create a list of numbers to use 1-10
numbers = list(range(1,11))
#print(numbers)

# Here is my rewrite of map, without using map()
def pseudosqauremap(numbers):
    ''' pseudosquaremap takes a list of numbers and returns a list of the squares of the numbers '''
    newnumbers = []
    
    for number in numbers:
        newnumbers.append(number * number)
        
    return newnumbers

# call pseudosquaremap
print(pseudosqauremap(numbers))
    
# Here is my rewrite of filter, without using filter()
def pseudoevenfilter(numbers):
    '''pseudoevenfilter takes a list of numbers and returns a list of the even numbers from the input list'''
    newnumbers = []
    
    for number in numbers:
        if (even(number)):
            newnumbers.append(number)
        
    return newnumbers

# call pseudoevenfilter
print(pseudoevenfilter(numbers))

# Here is my rewrite of reduce, without using reduce
def pseudoaddreduce(numbers):
    '''pseudoaddreduce takes a list of numbers adding each number to the su of the previous two numbers in the list'''
    # initialize how the return variable in case the input list is empty
    reducedSumNumber = 0
    
    # get the length of the list
    listLength = len(numbers)
    
    # if the list has items ...
    if (listLength > 0):
                
        # initialize a counter
        i = 0
        # while counter is less than the list length add the numbers together
        while i < listLength:
            reducedSumNumber = reducedSumNumber + numbers[i]
            i += 1    
    else:
        # empty list, return 0
        reducedSumNumber = 0
    
    return reducedSumNumber


# call pseudoaddreduce
print(str(pseudoaddreduce(numbers)))
#%%
#Classes and Inheritance: (4 pts)
''' 
Create a base class called ACCOUNT.
Account should have the following attributes: accountNumber and balance, 
which should be correctly initialized in the constructor (_ _init_ _) method for the class.
Create a to-string (_ _str_ _) method that prints “Account number 1234” on one line and “Balance: 2000” 
on the next line (example with account number of 1234 and balance of 2000).
'''

## TO DO: COMMENT CODE, ADD INT, FLOAT ERROR HANDLING, PRINT 0.00 format for balances

# *** BASE CLASS *** #
class ACCOUNT:
   def __init__(self, accountNumber, balance):  # constructor
      self.accountNumber = accountNumber
      self.balance = balance
      
   def __str__(self):
        return "Account number {accountnumber} \nBalance: {balance}".format(accountnumber = str(self.accountNumber), balance = str(self.balance))

acnt1 = ACCOUNT(1234,2000)
print(acnt1)
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
      ACCOUNT.__init__(self, accountNumber, balance)
      self.fee = fee
      
    def __str__(self):
      strReturn = "Account type: Checking\n"
      strReturn += ACCOUNT.__str__(self)
      return strReturn
      
    def getFee(self):
        return self.fee.fee
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdrawal(self, amount):
        if(amount + self.fee > self.balance):
            print("Insufficient funds")
        else:
            self.balance = self.balance - self.fee - amount


check1 = CHECKING(1234,500,.50)

print(check1)

check1.withdrawal(100)

print(check1)

check1.deposit(200)

print(check1)

check1.withdrawal(2000)




