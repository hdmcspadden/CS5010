# File: bookLover.py
# CS 5010
# Python version: 3

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  In-Class Activity 7 - All-day testing activity 
#  ::: SOLUTION to BookLover Class :::
#  Author: Nada Basit (basit@virginia.edu)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# === BookLover class ====
# Fields:
# name: the name of the person
# email: the person's email, serving as a unique identifier
# favGenre: the person's favorite book genre
# numBooks: keeps track of the number of books the person has read (optional)
# bookLst: a list of tuples, (title, rating) (optional) 

class BookLover:

    # Here we initialize a book lover with 3 required fields, and 2 optional ones
    # Notice how we used initializers for the default parameters
    # We could have also used None as the default value, in which case a check
    # for if the value was None would be required
    def __init__(self, name, email, favGenre, numBooks = None, bookLst = None):
        self.name = name
        self.email = email
        self.favGenre = favGenre
        if numBooks is None:  # Handling optional 'numBooks' parameter
            numBooks = 0
        self.numBooks = numBooks
        if bookLst is None:   # Handling optional 'bookLst' parameter
            bookLst = []
        self.bookLst = bookLst

    # A simple to string function
    def __str__(self):
        return "Name: {}, bookLst: {}".format(self.name, self.bookLst)

    # Adds a book to the list of books 'bookLst'
    # but only if the book has not been read before
    # Returns True if the book was added, False otherwise 
    def addBook(self, bookName, rating):
        if not self.hasRead(bookName):
            self.bookLst.append((bookName, rating))
			# Don't forget to increment the numBooks field to reflect one more book being added: 
            self.numBooks+=1		
            return True   # Book was added
        return False	  # Book was not added 

    # Returns True if a given book name has been read (it appears in bookLst)
    # False otherwise
    def hasRead(self, bookName):
        # Here we make use of the 'any' function which returns True
        # if any element in the array is true
        # We could also use a simple for loop
        for pair in self.bookLst:  # for every element in bookLst...
            if pair[0] == bookName:  # if I found a match
                return True
        return False
        #return any(True for pair in self.bookLst if pair[0] == bookName)

    # Returns the number of books read, an integer
    def numBooksRead(self):
        return self.numBooks

    # Returns a list of strings representing the books read with rating greater than 3
    def favBooks(self):
        return [pair[0] for pair in self.bookLst if pair[1] > 3]


# p1 = BookLover2("Nada", "basit@virginia.edu", "Mystery")
# print(p1)
# print("Adding a book!")
# p1.addBook("book1", 3)
# print("Num books read: " + str(p1.numBooksRead()))
# print(p1)
# print("Have I read 'book1'? " + str(p1.hasRead('book1')))

# p1.addBook("book1", 3) # add existing book
# print(p1)

# p1.addBook("bookX", 5) # add new book
# p1.addBook("bookY", 5) # add new book
# print(p1)
# print(p1.favBooks()) 