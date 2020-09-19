# -*- coding: utf-8 -*-
"""
Activity: Module 5 Exercise: Python Unit Testing
Name: H. Diana McSpadden
UID: hdm5s
"""

import unittest
from AStudent_Class import *

class GradesTestCases(unittest.TestCase): # inherit from unittest.TestCase
    # Unit testing courses list in AStudent_Class.py
    
    def test_is_add_grade_adding_grades(self):
        # Are grades being added to an object's grades

        # Set up
        studentD = AStudent('Diana', '5010', 0) # create instance
        studentD.addGrade(99)
        studentD.addGrade(0)
        studentD.addGrade(-5)
        #print("What grades are in the list?  " + str(studentD.grades))
        
        # Test
        # Does the list of grades contain  ['99', '0', '-5']?
        self.assertEqual(studentD.grades, [99, 0, -5]) 
    
    def test_is_add_grade_adding_to_correct_instance(self):
        # Are grades being added to the correct instance's grade list
        
        # Setup: create two instances of the AStudent class
        #   add grades to one instance
        #   make sure the grades are only added to the correct instance
        studentD = AStudent('Diana', '5010', 0) # create first instance
        studentH = AStudent('Harper', '5010', 0) # create first instance
        
        # add grades to Diana AStudent object
        studentD.addGrade(99)
        studentD.addGrade(0)
        studentD.addGrade(-5)
        
        
        self.assertNotEqual(studentD.grades, studentH.grades)
    
    def test_is_average_grades_calculated_correctly(self):
        # Is the average grade for a student calculated correctly
        
        # Setup: create an instance of AStudent
        #   add some grades
        #   check that the average equals what we would expect
        studentD = AStudent('Diana', '5010', 0) # create instance
        studentD.addGrade(0)
        studentD.addGrade(100)
        studentD.addGrade(25)
        studentD.addGrade(50)
        studentD.addGrade(75)
        studentD.addGrade(99)
        #print("What is the grade average?  " + str((0+100+25+50+75+99)/6))
        
        self.assertEqual(studentD.average(), 58.166666666666664)
            
if __name__ == '__main__':
    unittest.main()  