# File: pyScript18.py
# CS 5010
# Learning Python (Python version: 3)
# Topics:
#   - Object-oriented programming (OOP) - continue to build the Name class 
#        - adding methods including the to-string method

# Adding the to-string method allows us to display the name in different
# ways after the name has been instantiated via the constructor

# The to-string method allows us to (examine and) display the current
# state of a class object
# It has a particular name  __str__ with self as the parameter (to refer
# to the current instance of the object) We want to return (print) the fields
# that make up the Name class

# Without the to-string method it returns the object memory reference


class Name:
   #constructor method - instantiation
   def __init__(self, first, middle, last):
      self.first = first
      self.middle = middle
      self.last = last

   # to-string method
   # Allows for conversion from object to string (to achieve clear output)
   def __str__(self):
      return self.first + ' ' + self.middle + ' ' + self.last

   def lastFirst(self):
      return self.last + ', ' + self.first + ' ' + self.middle

   def initials(self):
      return self.first[0] + self.middle[0] + self.last[0] # get first char

# -----------------------------------------------------

aName = Name('Mary','Elizabeth','Smith')
#print('aName is ' + aName)  # This will NOT work because combining string 
#                              with object. BUT print(aName) will work!
print('aName is ' + str(aName))
# need str(..) because returns the obj reference not the obj data
# you cannot concatenate a string with an object (aName)

print(aName)  # This will work because of the "to-string" (__str__) method
print(aName.__str__()) # Overkill but you can do this (explicitly make call)

# Calling lastFirst and initials methods:
print(aName.lastFirst())
print(aName.initials())
print('aNames initials are: ' + aName.initials())
