#!/usr/bin/python

#You are given two integers N and A .

#Write a program to find the number of integer sequences which contain the elements that lie between 1 and A and the sum of whose elements is equal to N.

#Input format
#First line: Two space-separated integers N and A

 
#Output format
#Print the number of integer sequences which contain the elements that lie between 1 and A and the sum of whose elements is equal to N.


import itertools

input_no = map(int,raw_input().split())
N = input_no[0]
A = input_no[1]
lst = []
for i in range(1,A+1):
  lst.append(i)
print lst

out = 0
if sum(lst) == N:
  out = out+1
for i in lst:
  if N%i == 0:
    out = out+1
  if N-i == sum(



print out
print
print 
combs = []

for i in xrange(1, len(lst)+1):
    combs.append(i)
    els = [list(x) for x in itertools.combinations(lst, i)]
    combs.append(els)

print combs
for d in combs:
  print type(d)
result = []
for x in range(len(combs)):
  result.extend([c for c in itertools.combinations(combs,x) if sum(c) == N ])
print result
