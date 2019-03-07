#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
7cf244cfbcc55a41070a891838e397b4
python
Elevensval - Labb 1
Magnus Andersson
2018-11-22 09:21:27

Generated 2016-01-24 10:21:28 by dbwebb lab-utility v2.0.1x (2015-09-29).
https://github.com/mosbth/lab
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 1 - python

If you need to peek at examples or just want to know more, take a look at
the page: https://docs.python.org/3/library/index.html. Here you will find
everything this lab will go through and much more.
"""

"""
--------------------------------------------------------------------------
Section 1. Integers, strings, floats and basic arithmetics

The foundation of numbers and basic arithmetic.
"""

"""
Exercise 1.1

Create a variable called 'numOne' and give it the value 76. Create another
variable called 'numTwo' and give it the value 76. Create a third variable
called 'result' and assign to it the sum of the first two variables. Answer
with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

Create a variable called 'numThree' and give it the value 81. Create
another variable called 'numFour' and give it the value 61. Subtract
'numThree' from 'numFour' and answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Find out the product of 'numOne' and 'numThree' and answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Divide 30 with 5 and answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Create a variable called 'floatOne' and give it the value 98.76. Create
another variable called 'floatTwo' and give it the value 21.93. Sum the two
values and answer with the result, rounded to 2 decimals.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

Subtract 'floatTwo' from 'floatOne' and answer with the result. Round to 2
decimals.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7

Answer with the product of 'floatOne' and 'floatTwo', rounded to 4
decimals.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8

Create three variables: 'n1' = 327, 'n2' = 209 and 'n3' = 80. Sum up 'n1'
and 'n2'. Subtract 'n3' and answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""


ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9

Answer with the result of 507 modulo (%) 35.

Write your code below and put the answer into the variable ANSWER.
"""
result = 507 % 35


ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10

Add the word: 'device' to the word: 'beach' and answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Conditions, exceptions, booleans, if, else and elif


"""

"""
Exercise 2.1

Answer with the boolean value of: 70 is less than 259.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2

Answer with the boolean value of: 444 is larger than 490.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3

Answer with the boolean value of: 70 == 444.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4

Create three variables representing dice values: 'd1' = 1, 'd2' = 6 and
'd3' = 6. Sum them up and answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5

Create an if statement to see if the total value of your dices is 11 or
higher. If that is the case, answer with the string: 'big', else answer
with the string: 'nothing'.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6

Create an elif statement that checks your total dice value. The checks and
results should be: three of the same value = 'triple', total of 11 or
higher = 'big', total of 10 or lower = 'small'. If you get a triple you
should not make more checks.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Built-in functions

Some useful built-in functions
"""

"""
Exercise 3.1

Use max() to find the largest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2

Use min() to find the smallest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))

"""
Exercise 3.3

Use len() to find the number of letters in the word: error. Answer with the
result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.3", ANSWER, False))

"""
Exercise 3.4

Convert the number 353 to a string and add it to the word 'error'. Answer
with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.4", ANSWER, False))

"""
Exercise 3.5

Convert the number 640.49 to an integer and then to a string. Add it to the
beginning of the word: 'error'. Answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.5", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 4. Functions

Basic functions
"""

"""
Exercise 4.1

Create a function called 'prodNr' that takes two arguments, 34 and 77. The
function should return the product of the numbers. Answer with a call to
the function.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.1", ANSWER, False))

"""
Exercise 4.2

Create a function called 'funnyWord' that takes one argument and adds it to
the string ' is a funny word'. If the argument is 'water', the function
should return: 'water is a funny word'. Use the argument 'restaurant' and
answer with a call to the function.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.2", ANSWER, False))

"""
Exercise 4.3

Create a function called 'inRange' that takes one argument. The function
should return 'true' if the argument is higher than 50 and lower than 100.
If the number is out of range, the function should return 'false'. The
return type should be boolean. Use the argument 31 and answer with a call
to the function.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.3", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 5. Iteration and loops

For-loops and while-loops.
"""

"""
Exercise 5.1

Create a while-loop that adds 8 to the number 64, 73 times. Answer with the
result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.1", ANSWER, False))

"""
Exercise 5.2

Create a while-loop that subtracts 5 from 28, 68 times. Answer with the
result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.2", ANSWER, False))

"""
Exercise 5.3

Create a for-loop that counts the number of elements in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.3", ANSWER, False))

"""
Exercise 5.4

Create a for-loop that sums up the numbers in the serie:
67,2,12,28,128,15,90,4,579,450. Answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.4", ANSWER, False))

"""
Exercise 5.5

Create a for-loop that finds the largest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.5", ANSWER, False))

"""
Exercise 5.6

Create a for-loop that goes through the numbers:
67,2,12,28,128,15,90,4,579,450. If the current number is even, you should
add it to a variable and if the current number is odd, you should subtract
it from the variable. Answer with the final result.

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = "Replace this text with the variable holding the answer."

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.6", ANSWER, False))


dbwebb.exitWithSummary()
