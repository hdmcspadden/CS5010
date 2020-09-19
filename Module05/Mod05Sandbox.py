# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 08:17:22 2020

@author: Diana McSpadden
"""

"""
TERMINOLOGY


verification:	Shows that the code meets the requirement specification 
    Example: You verify that I wrote the program you asked me to write.
    
validation:	Shows that the code meets the real requirements Example: You show that the program is a valid solution to the user’s problem.
    quality	Suggests that validations falls on a scale, not a black-and-white idea. Defining the scale can be difficult.

specification:	A precise and detailed statement about the properties some things must have
    Design specification: exact instructions for how to build something Requirements specifications: exact statements about what should be built


Types of Empirical Testing

Unit Testing:	Write code that tests the smallest possible units of the spec (must attempt to test every flow path). The programmer does unit testing as part of the coding process.

Integration Testing:	Test that units work together.

Acceptance Testing (Beta Testing):	Give product to real users to try it out.





"""

"""
5.2 Tests and Unit Testing

TWO APPROACHES TO UNIT TESTING

Black-box unit : software is a closed box. DO not look at code. Look at description of code. Refer to specification.
    Cover specified code as much as possible

White-box testing: looks at the code. Looks at how the code is written. Cover as much of the code behavior as possible.
    It can't reveal errors due to missing paths. Pay attention to flow paths
    NOt based on specification, so it doesn't know all that the code is supposed to do.
    Will make sure that every line of code is evaluated.
 
Q:What are the advantages and disadvantages of each? 
A: 
    BB: Way to test that the software does what the software is supposed to do because you are testinging to the spec. 
        But, cannot test if the code is optimized, or commented, or written well.
    WB: Way to test the code. Cna notice if the code is written in a way that isn't optimized, 
        or may ahve infinite loop issues, memory issues, or other problems, But WB testings isn't to the spec
        so you won't know if a use case is missing, or the code isn't returning the correct type of data to the spec, etc.



Q: At what level of testing would it be applicable to apply black-box or white-box testing? 
A:  Unit Testing == WB and BB
    INtegration Testing == WB and BB
    Acceptance Testing == BB
    
    
Q: What kind of programming or implementation knowledge would be needed to perform either type of testing?
A: 
    BB - need to know the specifications. Need some level of subject matter knowledge. Need to understnad the big picture.
    WB - need to understand the programming language and environment of the software.
    
"""


"""
5.3 Test-Driven Development (TDD) and Unit Testing

Unit Testing - shows code does what you think it does
Benefits:
    Developers can work in a predictable way of developing code.
    Programmers write their own unit tests.
    You can get a rapid response for testing small changes.
    It encourages programmers to build many highly-cohesive, loosely-coupled modules to make unit testing easier.
    Allows you to do what’s next knowing what you’ve done is okay
    Allows you to make changes
    Avoids a growing “house of cards”
    Documents your intentions to others
    Gives you a more satisfying experience == small successes along the way

UNIT TESTING STEPS
1. Decide how to test a method and write test
    write BEFORE or DURING writing code
2. Run your test (and other tests) YOURSELF (not someone else)
3. All tests must pass before adding other features

Write at least one unit test per method - usually more.

"assert" statements are code of a unit test
    assert checks if code has passed or failed test
    
Unit Testing Library: unittest.TestCase

Many methods
assertEqual(a,b)
assertNotEqual(a,b)

All of the assert methods (except assertRaises(),
assertRaisesRegexp()) accept a msg argument that, 
if specified, is used as the error message on failure.

To test your code, you must do the following:
 
1. Set up what’s needed for testing. Create objects, allocate resources, create relationships, etc.
2. Call the method to be tested.
3. Verify that the method did what you expected.
   The above two are achieved by using an assert statement.
4. Clean up (optional).
...

"""

"""
NAMING CONVENTIONS
Class names should be capitalized. 

Use “camelCase” when concatenating other words to your class names. 

Method names should begin with a lowercase letter. 

You can use camelCase or separate words with underscores (_). 

Test files should include the name of the class you are testing. 

Each unit test method should be appropriately named, 
    describing the kind of test being performed as closely as possible.




"""

