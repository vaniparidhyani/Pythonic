#!/usr/bin/python



#Perfect no

#Write a program to determine whether a number N is equal to the sum of its proper positive divisors (excluding the number itself).

#Input format

#First line: T (number of test cases)
#For each test case
#First line: N
#Output format

#Print YES, if N is equal to the sum of its proper positive divisors else print NO.

def perfect_no(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n



T = int(input("No of Test Cases"))
for i in range(T):
  print perfect_no(i)

#list = ()
#listRange = list(range(1,num+1))

#divisorList = []

#for number in listRange:
#    if num % number == 0:
#        divisorList.append(number)

#print(divisorList)
