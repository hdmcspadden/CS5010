# -*- coding: utf-8 -*-
# File: pyScript27_SortingIntro.py

"""
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Brief introduction to soring in Python (using built in functions)
"""

"""
Sorting a Simple List
"""
simpleList = [3,7,22,8,14,55,1,23,45,9]
# Sorting in ascending order
# Can use built in function sorted that doesn't modify the original list,
#   and returns a new sorted list
newLst = sorted(simpleList)
print(newLst)       # [1, 3, 7, 8, 9, 14, 22, 23, 45, 55]
print(simpleList)   # [3, 7, 22, 8, 14, 55, 1, 23, 45, 9]
# For in-place sorting call "sort"
simpleList.sort()
print(simpleList)   # [1, 3, 7, 8, 9, 14, 22, 23, 45, 55]
print(">>>.....................<<<\n")

#%%

# Descending order? Sure!
simpleList = [3,7,22,8,14,55,1,23,45,9]
print(sorted(simpleList, reverse=True))  # [55, 45, 23, 22, 14, 9, 8, 7, 3, 1]
simpleList.sort(reverse=True)
print(simpleList)   # [55, 45, 23, 22, 14, 9, 8, 7, 3, 1]
print(">>>.....................<<<\n")
# What is going on?  Well, behind the scenes Python is calling a 
# version of *mergesort* on the list. 

#%%

"""
Sorting a Simple Tuple
"""
# Important note:
# Tuples must always use the "sorted" function to return a sorted * list *
# You cannot modify tuples, so there isn't an in-place sort function.
simpleTup = (2,6,9,22,1,45,16,34)
sortedTup = sorted(simpleTup)
print(sortedTup)    # [1, 2, 6, 9, 16, 22, 34, 45]
print(">>>.....................<<<\n")

#%%
"""
Sorting a List of Tuples or Lists of Lists
"""
# The sorted function takes in a keyword argument called "key"
# Key provides a way to specify a function and returns what you would like
# your items sorted by.

# Sorting List of Tuples 
q = "Are you suggesting coconuts migrate" # Fun quote from Monty Python
print(q)
wordslist =  q.split(' ') # split by the ' ' delimiter. Result: a list!
wlen = [(word, len(word)) for word in wordslist]
# "wlen" is a list of tuples (word, word length) at index positions 0 and 1
wlen_sorted = sorted(wlen, key=lambda wlen: wlen[1]) # sort by length
# using the method "sorted" on wlen, sorting elements by length
print(wlen_sorted)
# *** The above could also be achieved in the following way (w/out using lambda) ***
# def getKey(item):
#     return item[1]
# sorted(wlen, key=getKey)
print(">>>.....................<<<\n")

#%%

# Sorting List of Lists
def getKey(item):
    return item[0]


lst = [[2, 3], [6, 7], [7, 14], [25, 15], [35, 8], [1, 44]]
sortedLst = sorted(lst, key=getKey) # sort by the FIRST item in the sub-list
print(sortedLst)    # [[1, 44], [2, 3], [6, 7], [7, 14], [25, 15], [35, 8]]

#%%

# Sorting by the SECOND item in each sub-list is a simple matter of
# changing what the function returns, as follows:
def getKey2(item):
	return item[1]
lst = [[2, 3], [6, 7], [7, 14], [25, 15], [35, 8], [1, 44]]
sortedLst2 = sorted(lst, key=getKey2) # sort by the SECOND item in the sub-list
print(sortedLst2)  
print(">>>.....................<<<\n")
#%%

"""
Sorting a List (or Tuple) of Custom Python Objects
"""
# Let's create a class:
class Pet():
    def __init__(self, name, age): # Constructor
        self.name = name
        self.age = age
    
    # Tells Python how we want the object to be represented
    # In this case, we tell Python to represent an object of type Pet
    # by it's class name, name, and age
    def __repr__(self): 
        return '{}: {} {}'.format(self.__class__.__name__,self.name, self.age)
        # Tells the interpreter how to display the object when it is printed
        
# Create some 'Pet' objects:
g = Pet('Ginger', 5)
f = Pet('Fido', 12)
t = Pet('Tiger', 9)
s = Pet('Sparky', 8)

# Example of __repr__ being called:
print(t)

# Make a list of these Pet objects, so that we can sort them:
petLst = [g,f,t,s]

# Print out the Pet list
print(petLst)  # [Pet: Ginger 5, Pet: Fido 12, Pet: Tiger 9, Pet: Sparky 8]

# Sort by age:
def getPetKey(aPet):
    return aPet.age

sortedPetLst = sorted(petLst, key=getPetKey)
print("Sorted pet list (by age): \n" + str(sortedPetLst))
# [Pet: Ginger 5, Pet: Sparky 8, Pet: Tiger 9, Pet: Fido 12]
