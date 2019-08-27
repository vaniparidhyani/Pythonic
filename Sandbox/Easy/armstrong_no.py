#!/usr/bin/python


#Given a number x, determine whether the given number is Armstrong number or not.
# Examples: 
#Input : 153
#Output : Yes
#153 is an Armstrong number.
#1*1*1 + 5*5*5 + 3*3*3 = 153

#Input : 120
#Output : No
#120 is not a Armstrong number.
#1*1*1 + 2*2*2 + 0*0*0 = 9

no = raw_input("Enter no to check if it's armstrong or not : ")
no_of_digits = len(no)
sum = 0
for i in no:
  sum += pow(int(i),no_of_digits)
if sum == int(no):
  print "It is Armstrong"
else:
  print "It is not Armstrong"   
