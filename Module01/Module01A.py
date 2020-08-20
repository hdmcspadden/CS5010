# -*- coding: utf-8 -*-
"""
Activity: Module 01 Exercise: Python Part A
Created on Thu Aug 20 17:47:58 2020
@author: Diana McSpadden
Name: H. Diana McSpadden
UVa Computing ID: hdm5s

Create a dictionary and 

For 4 simulated users:
    Prompt user for:   First name, Last name,  and Age. [Note: Feel free to be creative here if you like!] 
    Eliminate any whitespace from either the left-hand side or the right-hand side.
    Concatenate the First name and the Last name into a single string so it looks like “Last-First” (with a dash separating the last and first names).
    To the dictionary add this information to it where the name (“Last-First”) is the key and the age (an integer) is the value.
    Print out the dictionary to a simple text file (e.g., “myOutput.txt”). 
"""
# import libraries
import sys 

# initialize variables,
#mainly just to have a reference for variables we will be using (helps with tab/autocomplete)
responseFirstName = ""
responseLastName = ""
responseAge = ""
dictNameAge = {}
originalStdout = sys.stdout # save standard output


for x in range(0, 4):
    if (x == 3):
        responseFirstName = (input("For the last time, what is your first name? ")).strip()
        responseLastName = (input("and, again, what is your last name? ")).strip()
        responseAge = (input("Finally, what is your age? ")).strip()
    else:
        responseFirstName = (input("What is your first name? ")).strip()
        responseLastName = (input("What is your last name? ")).strip()
        responseAge = (input("What is your age? ")).strip()
    
    # add the item to the dictionary
    dictNameAge[responseLastName + "-" + responseFirstName] = responseAge
    
 

# set output to the myOutput.txt file
# open file for appending ('a'), will create if it doesn't exist
sys.stdout = open('hdm5sOutput.txt', 'a') 
print(dictNameAge)

# reset output
sys.stdout = originalStdout
print("\n All done!")