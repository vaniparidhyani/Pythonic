#!/usr/bin/python

#Python Program for How to check if a given number is Fibonacci number?

#A number is Fibonacci if and only if one or both of  (5*n*n + 4) or (5*n*n - 4) is a perfect square

import math


#print int(math.sqrt(5))   ->   2



def isPerfectSquare(x):
  s = int(math.sqrt(x))
  return s*s == x

def isfibonacci(n):
  return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

print isfibonacci(10)

