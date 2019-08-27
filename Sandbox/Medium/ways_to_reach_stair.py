#!/usr/bin/python


# A program to count the number of ways to reach n'th stair 
  
# Recurssive program to find n'th fibonacci number 
def fib(n): 
    if n <= 1:
        print n 
        return n 
    return fib(n-1) + fib(n-2) 
  
# returns no. of ways to reach s'th stair 
def countWays(s): 
    return fib(s + 1) 
  
# Driver program 
  
s = 4
print "Number of ways = ", 
print countWays(s) 
