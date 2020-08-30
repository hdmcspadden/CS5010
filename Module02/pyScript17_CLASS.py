# File: pyScript17_CLASS.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Object-oriented programming (OOP)


## Class, Fields, and Constructors

# -- Defining a class
# Keyword class followed by the name and ":"

class Name:
    
# -- The constructor method  ("__init__")
# Used for instantiation
# Creating an instance of a class
# A constructor is a special kind of method (in OO functions are called methods)
# with a special name called __init__  (it's a built-in name) followed by
# a parameter list

# The parameter list defines the rest of the class (the attributes)
# Attributes: (there is no declaration as in Java - look at __init__)
# first (string)
# middle (string)
# last (string)

    def __init__(self, first, middle, last):
        # Note: always first parameter is called "self"
        # self refers to the current instance of a class
        
        # Assign the class attributes to the values passed in via the params
        # self is used here to describe the current object/instance
        # i.e. the current object's first variable is assigned the value first
        # that is passed in by the parameter, etc...
        self.first = first 
        self.middle = middle
        self.last = last
        

    # This method is invoked when you use "print"
    

    # To print name in the format: Last, First
    
    
    # To print name initials e.g MES
    

# ===============================================================

# -- Working program

aName = Name('Mary','Elizabeth','Smith')
print(aName)
print(aName.lastFirst())
print(aName.initials())

print(Name.lastFirst(aName)) # Is the incorrect usage, however will still work
# Why does this work? Because the 'self' parameter is an implicit way of
# passing the actual object to the method! So when doing this explicitly
# it will still work. Even if this does work it should still be avoided.
# Notice, also, cannot just say  lastFirst(aName) need to qualify it with Name


# aName = variable name of the current object
# Name = class name followed by the data that makes up the name
#         creating an instance of the class

# ===============================================================

# Notes:
# self refers to the current object, where here is aName
# if you create another object then self refers to that object 
# (e.g. yourName) at the time of instantiation
# e.g. yourName = Name('John', 'Alexander', 'Doe')

