# -*- coding: utf-8 -*-
"""
Assignment: Module 4 Exercise: Sequential Search
Name: H. Diana McSpadden
UI: hdm5s
"""

"""
Directions: Write an algorithm for a linear search using the instructions below.
 
#def linearSearch(target,my_list):
 
#Inputs:
A list
An element (target value)

Output:
 
The (index) position of the element in the list
If the element is not in the list, the function should return a sentinel value.
If the element is in the list multiple times, return the first position.
def linearSearch(target,my_list):
"""

sentinel = -1 #value to be returned if the item is not found
    
def linearSearch(target, my_list):
    """function to to a linear search. linearSearch(target = ITEM TO BE FOUND IN my_list, my_list = list to search within)"""
    
    indexOfItem = sentinel
    
    for idx, item in enumerate(my_list):
        if (item == target):
            indexOfItem = idx
            break
        
    return indexOfItem

# Test the function
# create a list
testList1 = [0,1,2,3,4,5,6,7,8,9,'0','1','2','3','4','5','6','7','8','9']

# test an item in the list
testIndex1 = linearSearch(4,testList1)
print(testIndex1)

# test the str version of 4
testIndex2 = linearSearch('4',testList1)
print(testIndex2)

# test something not there
testIndex3 = linearSearch([0,0],testList1)
print(testIndex3)