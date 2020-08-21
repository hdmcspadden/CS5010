"""
Activity: Module 01 Exercise: Python Part B
Name: H. Diana McSpadden
UVa Computing ID: hdm5s
Date: 08/21/2020
"""

#%%

##################
# -- EXERCISE -- #
##################

# Create a long sentence of words [assume NO punctuation]
# Put the words into a list (hint, how are the words separated?)
#        (separating the words can be done before the list comprehension)
# Use a list comprehension to return the word along with the length of it
# Use this -->  (word, len(word))   in your list comprehension
# [finally, print out the words along with its length ] - at the end

# create the sentence
sentence = "Emerging data about the virus and thoughtful public health tactics can help"
# split the sentence into a list of words
words = sentence.split(" ")
#print(words) 

words = [[word, len(word)] for word in words]

# print the words list with length to a file
outFile = open('hdm5s-CS5010-Module01-PartB-1.txt', 'w')
outFile.write(str(words))
outFile.close()



#%%
'''
Print out the word-size tuples in sorted order by length (smallest to largest)
'''
# create a function to get the length from the words tuple
def getLength(item):
    return item[1]

# set the sort key to the length item of the "sub-tuple"
words.sort(key=getLength)


# print the words sorted in order of length to a file
outFile = open('hdm5s-CS5010-Module01-PartB-2.txt', 'w')
outFile.write(str(words))
outFile.close()

#%%
'''
Done that, too?   Print out only unique words (i.e., no repetitions).'
'''
from more_itertools import locate

# new sentence from The Cure lyrics to Pictures of You
newSentence = "I've been looking so long at these pictures of you \
That I almost believe that they're real I've been living so long with my pictures of you \
That I almost believe that the pictures are \
All I can feel"

words2 = newSentence.split(" ")
# make all lowercase so that case differences don't matter
words2 = [word.lower() for word in words2]

# create a new list to store the unique words
words3 = []

# loop through all words in words2 list. If word doesn't exist in word3, add it
for word in words2:
    index_pos_list = list(locate(words3, lambda a: a == word))
    if (len(index_pos_list) == 0):
        words3.append(word)


# print unique words to a file
outFile = open('hdm5s-CS5010-Module01-PartB-3.txt', 'w')
outFile.write(str(words3))
outFile.close()


  