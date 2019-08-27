#!/usr/bin/python

import random

l = sorted(random.sample(range(1,100),10))

print l

n = int(input("Enter no to search"))

print n

start = 0
end = len(l)-1

while True:
  mid = (end - start)/2
  mid_no = l[mid]
  if n == mid_no:
    print True
    break
  if mid < start or mid > end or mid == 0:
    print False
    break
  if n > mid_no:
    start = mid
  else:
    end = mid
