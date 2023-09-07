'''
Anna Hauk
"I pledge my honor that I have abided by the Stevens Honor System" -Anna Hauk
Cs 115 Lab1
9/15/2022
'''

import math
from functools import reduce

def dbl(x): 
    """Returns twice its input x input x: a number (int or float)""" 
    return 2 * x


#sum function takes a list/sequence of numbers as input and returns the 
#sum of the numbers in the list/sequence


def inverse(n):
    '''takes a number n as input and returns its reciprocal'''
    if n==0:
        return ("undefined")
    n = float(1/n)
    return n
    
def factorial(c):
    '''returns the factorial of input c'''
    c = math.factorial(c)
    return c

def e(n):
    '''approximates the mathematical value e using a Taylor expansion'''
    if n==0:
        return 1
    if n<0:
        return ("Negative input; doesn't work")
    list1 = list(range(1,n+1))
    list2= list(map(factorial, list1))
    list3= list(map(inverse, list2))
    return 1 + reduce(lambda x,y: x+y,list3)
