# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:54:01 2020

@author: Diana McSpadden
"""
 
#Prompts the user for their name (e.g. “Sage”) and two numbers (three separate prompts)

inputName = input("What is your name? ")

firstNum = int(input("Please give me one number: "))

secondNum = int(input("Please give me another number: "))


#Perform the calculation: Multiply the two numbers and divide by 7.
resultNum = (firstNum * secondNum) / 7

#Display an output like the following: Hi, 
#<NAME>! You entered <NUM1> and <NUM2>. Your personal code is: <RESULT>
#Display the result as a floating-point number (not an integer). Don’t worry about rounding the number, but you can if you like.

print("Hi, {name}! You entered {num1} and {num2}. Your personal code is: {result:.2f}".format(name=inputName, num1=firstNum, num2=secondNum, result = resultNum))

#Create a dictionary called “kidsClub” and 
#insert an entry into this dictionary where the name is the key and the code (result) is the associated value.

kidsClub = {inputName:resultNum}

#%%

en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow" : "gelb"}

answerRed = en_de['red']

print(answerRed)

de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb" : "jaune"}

answerFrenchRed = de_fr[en_de['red']]

print(answerFrenchRed)


#%%

class Alien:
    def __init__(self, name, numArms, home):
        self.name = name
        self.numArms = numArms
        self.planet = home
        
    def __str__(self):
        return self.name + ' ' + self.planet + ' ' + str(self.numArms)
    
    def changeName(self, name):
        self.name = name
        
    def growArms(self):
        self.numArms = self.numArms + 1
        

class SonicAlien(Alien):
    def __init__(self, name, numArms, home, spots):
        Alien.__init__(self, name, numArms, home)
        self.spots = spots
        
    def __str__(self):
        return self.name + " " + self.planet + " " + str(self.numArms) + \
            " " + str(self.spots)
            
    def growArms(self):
        self.numArms = self.numArms + 3
        

alien1 = Alien("K00kie",3,"Mars")     # create alien1 object
alien2 = Alien("L33tAlien",5,"Titan")     # create alien2 object
alien3 = SonicAlien("Sonny",7,"Pluto",True)    # SonicAlien has spots! (boolean) 

print('Alien 1: ' + str(alien1))

alien1.growArms()                    # Line 1
alien1.changeName('MarsK00kie')      # Line 2
alien3.growArms()                    # Line 3
alien3.changeName('Sonnie')          # Line 4 


print("Alien 1: " + str(alien1))

print("Alien 3: " + str(alien3))

#%%
# QUESTION 5
def beginWithVowel(theKey):
	vowels = ['A', 'E', 'I', 'O', 'U']  # a list of vowels
	# if the first letter is a vowel, return true.
	if theKey[0] in vowels :
		return True
	else:  # else, return false
		return False
    
bankDB = {'Michael':6494, 'Angela':2982, 'Sage':7771, 'Oliver':3612}

VowelNames = list(filter(beginWithVowel, bankDB.keys())) # added .keys() to be specific about which part of the dict we are using.

for clientName in VowelNames:
    bankDB[clientName] = int(bankDB[clientName]) + 500
    
print(bankDB)

#%%
#QUESTION 6

try:
    #name = input("Enter the name of a file: ") 
    #file = open(name, 'r')  # try to open this file for reading
    special = input("Enter a special boolean input: ") # assume no casting
    if type(special) is not bool:	
        raise TypeError()  # (direct subclass to ‘Exception’)
    # Line 7:  OTHER PYTHON CODE HERE (a few lines) 
except TypeError as errType:
    print("you raised a type error")
    
##ARGH, I messed up here .. READ THE QUESTION IN ITS ENTIERTY!!!
    
#%%
#QUESTION 8

class Horse:
    def __init__(self, name, owner, age, breed, injuryLst = None):
        self.name = name
        self.owner = owner
        self.age = age
        self.breed = breed
        self.injuryLst = []
        if injuryLst != None:
            self.injuryLst = injuryLst