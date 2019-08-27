#!/usr/bin/python

import random

l1 = random.sample(range(1,100),5)
l2 = random.sample(range(1,100),5)



print l1,l2
print set(l1).intersection(l2)

print "Common elements from above lists"
print (set(l1).intersection(l2))

print "Combine the above lists without duplicates"
print ( set( l1 + l2 ) )
