# -*- coding: utf-8 -*-
"""
Activity: Module 4 Exercise: Binary Search
Name: H. Diana McSpadden
UID: hdm5s

"""

"""
Directions: Write an algorithm for a binary search using the instructions below.
   
def BinarySearch(item_list,target):
   
Inputs:
 
A list
An element (target value)
Output:
 
A sequence of indices (of mid) compared to the target value [This can be a simple print statement embedded within your binarySearch function. It doesn’t have to be a value that is returned.]
True or False [This has to be returned by the function.]
def BinarySearch(item_list,target):
    
"""

from math import floor # need floor in order to set mid values
import random # using the random library to test my binary list search

def BinarySearch(item_list, target):
    """function to to a binary search. linearSearch(item_list = list to search within, target = ITEM TO BE FOUND IN my_list)"""
    low = 0 # the low value is zero to start
    high = (len(item_list) - 1) # the high value is the length of the list - 1 == highest index
    mid = None # mid starts as empty, but will be floor of sum of low and high divided by 2.
    
    
    # search for the algorithm until the value is Found OR low and high equal each other or swtich places
    while low <= high:
            
        mid = floor((low + high)/2) # mid, is the floor of sum of low and high divided by 2.
        
        if (item_list[mid] == target):
            # we found it, return True
            return True
        elif (item_list[mid] < target):
            # mid value is less than target
            # need to search to the higher end of the values == to the right of ascending list
            low = mid + 1
        else :
            # item_list[mid] is < the target
            # need to search the lower end of the list == to the left of ascending list
            high = mid - 1
    
    return False
    
    
# create a list that is ascending sorted
primesNumbersBetween1And100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]   

# test if a random number between 1 and 100 is in the prime list
for x in range(10):
    testNum = random.randint(1,101)
    isPrime = BinarySearch(primesNumbersBetween1And100,testNum)
    if (isPrime):
        print("The random number {} IS in the prime list.".format(testNum))
    else:
        print("The random number {} is NOT is the prime list.".format(testNum))
      
  

    