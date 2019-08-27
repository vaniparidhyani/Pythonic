#!/usr/bin/python

#a = [3, 4, -1, 1]
a = [1, 2, 0]
# Remove negatives and zero for the list
b = sorted(filter(lambda x: x>0, a))
print b
for i in b:
  if i+1 not in b:
    print i+1
    break
  

