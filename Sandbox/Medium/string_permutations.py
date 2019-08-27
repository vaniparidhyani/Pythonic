#!/usr/bin/python

# Function to find permutations of a given string 
from itertools import permutations 

def allPermutations(str): 
	
	# Get all permutations of string 'ABC' 
	permList = permutations(str) 
#	print list(permList)
	# print all permutations 
	for perm in list(permList): 
		print (''.join(perm)) 
		
# Driver program 
if __name__ == "__main__": 
	str = '123'
	allPermutations(str) 

