#!/usr/bin/python

from __future__ import print_function

def removeDups(arr, n):

#Create a dictionary which keeps count of occurrence of each element. Initialise it with 1
 mp = {i : 1 for i in arr}


 for i in range(n):
#Check if count is still 1 and then increment it to 2 for next check
  if mp[arr[i]] == 1:
   print(arr[i], end = " ")
   mp[arr[i]] = 2

arr = [ 1, 2, 5, 1, 7, 2, 4, 2 ]


n = len(arr)

removeDups(arr,n)

print()

# Using lambda and list comprehension
unique_list = []
map(lambda x: unique_list.append(x) if (x not in unique_list) else False, arr)
print (unique_list)



#Easiest way: But might not maintain order
print (list(dict.fromkeys(arr)))

