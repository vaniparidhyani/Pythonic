#!/usr/bin/python

# reverse a list

mylist = [5, 6, 7, 8, 9] 
print list(reversed(mylist))
print mylist[::-1]

# pop removes item from the last
#for i in range(len(mylist)):
#  print mylist.pop()


def rverseArray(arr):
    start = 0
    end = len(arr)-1 
    while (start < end): 
#        temp = arr[start] 
#        arr[start] = arr[end] 
#        arr[end] = temp 
	arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end = end-1
    print arr

rverseArray(mylist)

#for i in range(len(mylist),-1):
#  print mylist.pop()
