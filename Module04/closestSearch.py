# -*- coding: utf-8 -*-
"""
Activity: Module 4 Exercise: Binary Search
Name: H. Diana McSpadden
UID: hdm5s

"""
from math import floor # need floor in order to set mid values
import random # using the random library to test my binary list search

def closestBinarySearch(item_list, target):
    """function to to a binary search. closestBinarySearch(item_list = list to search within, target = ITEM TO BE FOUND, or find closest to IN item_list. returns closest VALUE)"""
    low = 0 # the low value is zero to start
    high = (len(item_list) - 1) # the high value is the length of the list - 1 == highest index
    mid = None # mid starts as empty, but will be floor of sum of low and high divided by 2.
    
    currentClosestValue = None
    currentDifference = max(map(abs,map(lambda x: (x - target), item_list))) # initialize to the maximum difference of the target value and items in the list
    originalMid = floor((high)/2) # set the original mid, because we always need to go and check the mid +/- 1 from the direction we started
    originalDirection = None
    
    
    # search for the algorithm until the value is Found OR low and high equal each other or swtich places
    while low <= high:
            
        mid = floor((low + high)/2) # mid, is the floor of sum of low and high divided by 2.
        
        if (item_list[mid] == target):
            # we found it, return this value
            currentClosestValue = item_list[mid]
            # we can leave the while loop, we found it
            break
        elif (item_list[mid] < target):
            if (originalDirection == None):
                originalDirection = 'HIGH'
            # mid value is less than target
            
            if (abs(currentDifference) > abs(item_list[mid] - target)):
                currentDifference = item_list[mid] - target
                currentClosestValue = item_list[mid]
            
            
            # need to search to the higher end of the values == to the right of ascending list
            low = mid + 1
        else :
            if (originalDirection == None):
                originalDirection = 'LOW'
            # item_list[mid] is > the target
            
            if (abs(currentDifference) > abs(item_list[mid] - target)):
                currentDifference = item_list[mid] - target
                currentClosestValue = item_list[mid]
            
            # need to search the lower end of the list == to the left of ascending list
            high = mid - 1
    
    # check in the opposite direction from the standard binary search
    if (originalDirection == 'HIGH'):
        # check one lower than the mid
        if (abs(currentClosestValue - target) > abs(item_list[originalMid - 1] - target)):
            currentClosestValue = item_list[originalMid - 1]
    else:
        if (abs(currentClosestValue - target) > abs(item_list[originalMid + 1] - target)):
            currentClosestValue = item_list[originalMid + 1]
    
    return currentClosestValue
    
    
# create a list that is ascending sorted
primesNumbersBetween1And100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]   

# test if a random number between 1 and 100 is in the prime list
for x in range(10):
    testNum = random.randint(1,101)
    closestPrime = closestBinarySearch(primesNumbersBetween1And100,testNum)
    print("The random number {} IS closest to the prime Number {}.".format(testNum, closestPrime))
 
      
  

    