# Introduction to Vulprita Python Programming
# Winter 2015/2016
# 1nd exercise sheet
import math
''' 1. Leap years (2 Points)

Write a function that checks whether or not a year is a leap year or not.
The function should return True or False.
'''

def is_leap(year):
    if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False
    '''correct. whenever you return just True or False depending on a
    condition, just return that condition instead:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    2/2 points.
    '''

''' 2. Prime numbers (4 Points)

Implement a funktion is_prime(n) that returns True if n is a prime, False
otherwise
'''

def is_prime(n):
    if n < 0:
        return False
    for j in range(2, int(math.sqrt(n))+1):
        if n%j == 0:
            return False
    return True
    '''4/4 points'''


''' 3. Zeller's Congruence (4 Points)

(see additional pdf file)
'''

def zeller(day, month, year):
    x = {0: "Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}
    q = day
    m = month
    k = year % 100
    j = year // 100
    h = (q + (((m+1)*13)//5) + k  + (k//4) + (j//4) + 5*j) %7
    return x[h]
    '''Incorrect results, you didn't special-case january and february.
    You can check for yourself by testing for some 31st of December and than
    for the 1st of January afterwards. Everything except for January and
    February works, so:

    2.5/4 points.
    '''


''' 4. Iterative fib (4 Points)


Implment a non-recursive version of the function fib(n) from the lecture.
Compare runtimes for inputs 10, 20, 30, 35.
'''
def fitbit(n):

def fibonaci():
    yield 1
    yield 1
    a = 1
    b = 1
    while True:
        a,b = a+b, a
        yield a



