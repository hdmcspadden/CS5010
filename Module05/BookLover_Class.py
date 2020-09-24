# -*- coding: utf-8 -*-
"""
Activity: Module 5 Live Session Exercise: Testing Activity
Names: H. Diana McSpadden
UID: hdm5s
"""



"""
name	The name of the person
email	The person’s email, serving as a unique identifier
favGenre	The person’s favorite book genre (e.g., mystery, fantasy, or historical fiction)
numBooks	Keeps track of the number of books the person has read
bookLst	a list of tuples, where each tuple consists of the title of the book the person has read, followed by the person’s rating of that book (scale of 0–5, where 0 means the person did not like the book at all, and 5 means the person loved the book.) Example: bookLst = [(“Jane Eyre”, 4), (“The Odyssey”, 3), (“The Divine Comedy”, 5)]
"""

import re # need regex for checking email address

class BOOKLOVER:    
    
    def __init__(self, name, email, favGenre, numBooks = None, bookLst = None):  # constructor
        """fields: name, email, favGenre, bookLst = None"""
        
        # validate input
        if (name == None or len(name) == 0): # name cannot be None, or zero length
            raise ValueError
        
        emailRegEx = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' #regex to test valid email syntax
        
        if(not re.search(emailRegEx,email)):
            raise ValueError
        
        # initialize the class variables
        self.name = name
        self.email = email
        self.favGenre = favGenre
        
        if (bookLst is None): # if bookLst was not included, or included as None
            self.bookLst = []
            self.numBooks = 0 # I am ignoring passed in numBooks, because I don't trust it.
        else:
            self.bookLst = bookLst
            self.numBooks = len(bookLst) # set numBooks to the length of the list
      
      
    def __str__(self):
        # return account number and balance (balance in 0.00 format)
         return "\nName: {} \nBook List: {}".format(str(self.name), str(self.bookLst))

    def hasRead(self, bookName):
        # return any(True for readbook in self.bookLst if readbook[0] == bookName)
        # loop through the bookLst and determine if the title is already there
        for book in self.bookLst: # every element in bookLst
            if str(book[0]).lower() == bookName.lower(): # check if bookName == return True
                return True
        return False
                

    # Add a book to the book list with the book title and rating (1 - 5)
    def addBook(self, bookName, rating):
        # validate input
        if (bookName == None or len(bookName) == 0): # bookName cannot be None, or zero length
            raise ValueError('Provide a valid book title.')
        
        try:
            int(rating)
        except:
            raise TypeError('A book rating must be between 0 and 5.')
            
        try:
            if (int(rating) < 0 or int(rating) > 5):
                raise ValueError()
        except:
            raise ValueError('A book rating must be between 0 and 5.')
        
        if not self.hasRead(bookName):
            self.bookLst.append((bookName, rating))
            self.numBooks = len(self.bookLst)
            return True
        return False
                                                     
    def numBooksRead(self):
        return len(self.bookLst)
    
    
    def favBooks(self):
        return [bookItem[0] for bookItem in self.bookLst if bookItem[1] > 3]
       

# Block of simple test code
"""
p1 = BOOKLOVER("Nada", "basit@virginia.edu", "Mystery")
print(p1)
print("Adding a book!")
p1.addBook("book1", 3)
print("Num books read: " + str(p1.numBooksRead()))
print(p1)
print("Have I read 'book1'? " + str(p1.hasRead('book1')))
res = p1.addBook("book2", 5)
print("Successful in adding the book? " + str(res))
p1.addBook("book3", 2)
print(p1)
print("Num books read: " + str(p1.numBooksRead()))
print("Fav books read: " + str(p1.favBooks()))
res = p1.addBook("book2", 5)
print("Successful in adding a duplicate book (book2)? " + str(res))
print(p1)
res2 = p1.addBook("book2", 1)
print("Successful in adding a duplicate book (book2) w/ different rating (1)? " + str(res2))
print(p1)
print("Has 'book0' been read? " + str(p1.hasRead('book0')))
print("Has 'book2' been read? " + str(p1.hasRead('book2')))
"""