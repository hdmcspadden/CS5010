# -*- coding: utf-8 -*-
"""
Activity: Module 5 Live Session Exercise: Testing Activity
Names: H. Diana McSpadden
UID: hdm5s
"""

import unittest
from BookLover_Class import BOOKLOVER

# Class for testing BOOKLOVER classes.
class BookLoverTestingClass(unittest.TestCase): # inherit from unittest.TestCase
    

    def setUp(self):
        one = 1 # placeholder for local fixtures
        
    # __init__ TEST CASE #1
    def test_does_BOOKLOVER_init_check_valid_name(self):
        # is BOOKLOVER initialize with the values supplied

        # Set up
        testName = ''
        testEmail = 'hdm5s@virginia.edu'
        testGenre = 'Historical Fiction'

        # found out I need to put the __init__ of BOOKLOVER in a wrapper function 
        #so that the error gets raised to something. I used a lambda.
        self.assertRaises(ValueError, lambda:BOOKLOVER(testName, testEmail, testGenre))
        
    # __init__ TEST CASE #1
    def test_does_BOOKLOVER_init_check_valid_email(self):
        # is BOOKLOVER initialize with the values supplied

        # Set up
        testName = 'Diana McSpadden'
        testEmail = 'NOT AN EMAIL ADDRESS'
        testGenre = 'Historical Fiction'

        # found out I need to put the __init__ of BOOKLOVER in a wrapper function 
        #so that the error gets raised to something. I used a lambda.
        self.assertRaises(ValueError, lambda:BOOKLOVER(testName, testEmail, testGenre))
        
    # hasRead TEST CASE #1
    def test_hasRead_does_not_find_unread_book(self):
        # test that hasRead returns False when a book has not been read
        
        # Set up
        testName = 'Diana McSpadden'
        testEmail = 'hdm5s@virginia.edu'
        testGenre = 'Historical Fiction'
        testBookNum = 2
        testBookLst = [('Black Hills: A Novel',4),('The Red Tent',5)]
        
        bookLvr1 = BOOKLOVER(testName, testEmail, testGenre, testBookNum, testBookLst)
        
        # assert that hasRead returns false for unread book
        self.assertFalse(bookLvr1.hasRead('Lonesome Dove'))
    
    # hasRead TEST CASE #2
    def test_hasRead_case_insensitive(self):
        # test that hasRead can find a bookName rgardless of case 
        
        # Set up
        testName = 'Diana McSpadden'
        testEmail = 'hdm5s@virginia.edu'
        testGenre = 'Historical Fiction'
        testBookNum = 2
        testBookLst = [('Black Hills: A Novel',4),('The Red Tent',5)]
        
        bookLvr1 = BOOKLOVER(testName, testEmail, testGenre, testBookNum, testBookLst)
        
        # assert that hasRead returns false for unread book
        self.assertTrue(bookLvr1.hasRead('tHE rED tENT'))
    
    # addBook TEST CASE #1
    def test_add_book_adds_correct_entry_to_bookLst(self):
        # test that addBook adds the correct bookName in new entry in bookLst
        
        # Set up
        testName = 'Diana McSpadden'
        testEmail = 'hdm5s@virginia.edu'
        testGenre = 'Historical Fiction'
        testBookNum = 2
        testBookLst = [('Black Hills: A Novel',4),('The Red Tent',5)]
        
        # create initial bookLvr
        bookLvr1 = BOOKLOVER(testName, testEmail, testGenre, testBookNum, testBookLst)
          
        # add a book
        bookLvr1.addBook('My Name Is Vittoria',3)
        
        # retrieve last item in book list
        bookLvrLastBook = bookLvr1.bookLst[-1]
        
        # test whether the last item in the list is the book added
        self.assertEqual(bookLvrLastBook, ('My Name Is Vittoria',3))
         
    
    # addBook TEST CASE #2
    def test_add_book_will_error_when_rating_greater_than_5(self):
        # test that addBook adds the correct bookName in new entry in bookLst
        
        # Set up
        testName = 'Diana McSpadden'
        testEmail = 'hdm5s@virginia.edu'
        testGenre = 'Historical Fiction'
        testBookNum = 2
        testBookLst = [('Black Hills: A Novel',4),('The Red Tent',5)]
        
        # create initial bookLvr
        bookLvr1 = BOOKLOVER(testName, testEmail, testGenre, testBookNum, testBookLst)
          
        # when adding a book with a rating greater than 5 test that the correct error is returned        
        with self.assertRaisesRegexp(ValueError, 'A book rating must be between 0 and 5.'): #use assertRaisesRegexp with a literal of the customer ValueError message
            bookLvr1.addBook('My Name Is Vittoria',6)
      
    # favBooks TEST CASE #1
    def test_favBooks_returns_correct_list(self):
        # test that favBooks() returns expected list
        
        # Set up
        testName = 'Diana McSpadden'
        testEmail = 'hdm5s@virginia.edu'
        testGenre = 'Historical Fiction'
        testBookNum = 2
        testBookLst = [('Black Hills: A Novel',4),('The Red Tent',5),('The Notebook',1),('The Color Purple',5)]
    
        # create initial bookLvr
        bookLvr1 = BOOKLOVER(testName, testEmail, testGenre, testBookNum, testBookLst)

    
        #test if favBooks returns correct list
        self.assertEqual(bookLvr1.favBooks(), ['Black Hills: A Novel','The Red Tent','The Color Purple'])
        
    # favBooks TEST CASE #2
    def test_favBooks_returns_correct_list_when_no_books_read(self):
        #test that when bookLst = None favBooks returns empty list
    
        # Set up
        testName = 'Diana McSpadden'
        testEmail = 'hdm5s@virginia.edu'
        testGenre = 'Historical Fiction'
        
        # create initial bookLvr
        bookLvr1 = BOOKLOVER(testName, testEmail, testGenre)
        
        #test if favBooks returns correct list
        self.assertEqual(bookLvr1.favBooks(), [])
        
    
if __name__ == '__main__':
    unittest.main() 