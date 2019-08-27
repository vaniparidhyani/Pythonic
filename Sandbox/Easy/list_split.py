#!/usr/bin/python

#There is a given an array and split it from a specified position, and move the first part of array add to the end.

def splitList(mylist,n):
  first_half = []
  second_half = []
  for i in range(0,n):
    first_half.append(mylist[i])
  for j in range(n,len(mylist)):
    second_half.append(mylist[j])
  print second_half+first_half

li = [1,2,3,4,5,6]
splitList(li,2)
