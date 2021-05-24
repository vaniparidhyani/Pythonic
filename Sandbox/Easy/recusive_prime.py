#!/usr/bin/python

def prime(n,q):
    if(n<2):
        return False
    if(q==n):
        return True
    if(n%q==0):
        return False
    return prime(n,q+1)
n = int(input("enter"))
print(prime(n,2))
