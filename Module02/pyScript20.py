# File: pyScript20
# CS 5010
# Learning Python (Python version: 3)

class Person:
    def __init__(self, name, sex, age):  # constructor
        self.name = name
        self.sex = sex
        self.age = age
        
    def __str__(self):  # toString method
        return self.name + ' ' + self.sex + ' ' + str(self.age)
        
    def changeName(self, name): # Change the name attribute
        print("  ... changing name ...")
        self.name = name
       
    def changeAge(self): # increment age by one
        print("  ... changing age ...")
        self.age = self.age + 1
        
#=======================================
print("** Output from pyScript20 **")
person1 = Person('Jane Doe','F',23)  # create person1 object
person2 = Person('Bob Smith','M',55) # create person2 object

print('Person 1: ' + str(person1))
person1.changeAge()
print('Person 1: ' + str(person1))

print('Person 2: ' + str(person2))
person2.changeName('John Smith')
print('Person 2: ' + str(person2))

print(person1)
print("** END of output from pyScript20 **\n")
