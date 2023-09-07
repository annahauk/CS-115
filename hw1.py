'''
Anna Hauk
"I pledge my honor that I have abided by the Stevens Honor System." Anna Hauk
CS 115 HW1
9/13/2022
'''
import math
import functools

def mult(x, y): 
   """Returns the product of x and y""" 
   return x * y

def factorial(n):
   '''takes a positive integer n and returns n!'''
   s = 1
   if n<=1:
      return s
   while n>1:
      s *= mult(n,n-1)
      n = n-2
   return s
      
def add(x,y):
   '''takes 2 integers and sums them'''
   return x + y

def mean(L):
   '''takes a list as input and returns the mean'''
   b = len(L)
   return functools.reduce(add,L)/b
