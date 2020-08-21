# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:49:22 2020

@author: Diana McSpadden

Try This! 
Using pyScript09 as a base, try using pyScript09B 
 to show how you can use a while loop to write data to a file. 
 Using all the elements previously seen and carefully placed print() and input() statements, 
 you can make this example work very well.
"""

# set the output file
outFile = open('Module09TryThis.txt', 'w')

# prime the user input
text = input("Enter text (q to quit): ")

# while loop to add text to the file
while (text != 'q'):  # While the user did not enter 'q' (for quit) ...
    outFile.write(text + '\n')
    text = input("Enter text (q to quit): ")


outFile.close()
print("Done! Look at file: 'Module09TryThis.txt' in working directory")
