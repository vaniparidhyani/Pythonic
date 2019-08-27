#!/usr/bin/python

#Write a program that prints the numbers in the given range. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". Print a new line after each string or number.

#Input Format First line will be the number of testcases, T. Next line will have T integers, denoted by N.

#Output Format For each testcase, print the number from 1 to N. But follow the rules given in the problem statement.

#Constraints

#1 <= T <= 10

#N is an integer.
#
#
#
#
print "hi"

T = raw_input()
s = raw_input()
numbers = map(int, s.split())
for n in numbers:
  print "Lets do for"+str(n)
  for i in range(1,n+1):
    if i%15 == 0:
      print "FizzBuzz"
    elif i%5 == 0:
      print "Buzz"
    elif i%3 == 0:
      print "Fizz"
    else:
      print i
