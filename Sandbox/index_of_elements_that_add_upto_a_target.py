#!/usr/bin/python

nums = [3,3,2,4,1]
target = 6

myHash = {}
for index, value in enumerate(nums):
#  print myHash
  if target - value in myHash:
    print [myHash[target-value], index]
  myHash[value] = index
