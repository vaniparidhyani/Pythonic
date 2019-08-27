#!/usr/bin/python

#Increment alphabets by integers
# Example
#Java=Mdyd Python=Sbwkrq
#J + 3 = M
#a + 3 = d
#v + 3 = y
#a + 3 = d


mystr = raw_input("Input string: ")
outputstr=""
for s in mystr:
  outputstr+=chr(ord(s) + 3) 


print outputstr

