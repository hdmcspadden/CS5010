# File: pyScript20_using
# CS 5010
# Learning Python (Python version: 3)

# Quick examples to show usage of a class doesn't have to be in the same file!
# [ Refer to / use with  pyScript20.py ; this file contains the Person Class ]

# ------------------------------
# from <filename> import <Class>
#-------------------------------
from pyScript20 import Person

person1 = Person('Jane Doe','F',23)  # create person1 object, as usual
person2 = Person('Bob Smith','M',55) # create person2 object, as usual

print('Person 1: ' + str(person1))
person1.changeAge()
print('Person 1: ' + str(person1))

print('Person 2: ' + str(person2))
person2.changeName('John Smith')
print('Person 2: ' + str(person2))

print(person1)
print('\n\n')

# ----------------------------
# import <filename>
#-----------------------------
import pyScript20

person_one = pyScript20.Person('Sara','F', 25) # filename.Classname
print(person_one)
person_one.changeAge() # use 'person_one' variable to call any method as usual
print(person_one)
person_one.changeName('Sara B.')
print(person_one)
#-----------------------------
