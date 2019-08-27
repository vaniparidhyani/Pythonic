#!/usr/bin/python

#Given an array of integers greater than zero, find if it is possible to split it in two (without reordering the elements), such that the sum of the two resulting arrays is the same. Print the resulting arrays.

def split(l1):
    if sum(l1)%2!=0:
        return False
    else:
        for splice in range(0,len(l1)):
            if sum(l1[:splice+1])==sum(l1[splice+1:]):
                print l1[:splice + 1]
                print l1[splice + 1:]
split ([1,2,3,4,5,6,21])
