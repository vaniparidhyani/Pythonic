#!/usr/bin/python

#Given two positive integer start and end. The task is to write a Python program toprint all Prime numbers in an Interval.

import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)
start = int(arguments[0])
end = int(arguments[1])

for i in range(start,end+1):
  count = 0
  for j in range(2,i):
    if i%j == 0:
      count += 1
  if count == 0 :
    print i
