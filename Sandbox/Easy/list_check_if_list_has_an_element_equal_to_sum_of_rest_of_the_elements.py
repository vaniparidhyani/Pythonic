#!/usr/bin/python



# Logic: Since the nos are all non-decimal integers the sum of all the elements can be divided into 2 set only if the sum is even and there exists an element equal to half of the sum


a = [2, 6, 2, 4, 4]

#Find sum of all nos. in list
s = sum(a)

#Find the half of the sum
half = s/2

# Sum should be evenly divisible into 2 sets
if s%2 == 0:

# the half should exist in the list
    if half in a:
        print True
    else:
        print False
else:
    print False
    

