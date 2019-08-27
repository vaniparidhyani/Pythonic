#!/usr/bin/python

# ofcourse we can just do set and check but here is another way

import sys

a = [2, 5, 6, 8, 10, 2, 2,0,0]
b = [2, 5, 6, 8, 10,2,2,10,10]
 
if len(a) != len(b):
    print "Lists are not of same length"
    sys.exit()
    

    
    
dic1 = {i:a.count(i) for i in a}
dic2 = {i:b.count(i) for i in b}

print dic1
print dic2

if not (all(i in a for i in b) and all(i in b for i in a) ):
    print "all items not present"
    sys.exit()


for k,v in dic1.items():

    if dic2[k] != v:
        print "Count/Occurrence of each element did not match"
        sys.exit()
print "The lists are the same"
