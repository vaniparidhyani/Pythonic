#!/usr/bin/python


# Function to check if a string can become empty 
# by recursively deleting a given sub-string 

def checkEmpty(input, pattern): 
	
	if len(input)== 0: 
		return 'false'

	while (len(input) != 0): 

		# find sub-string in main string 
		index = input.find(pattern) 
			
		# check if sub-string founded or not 
		if (index ==(-1)): 
			return 'false'
			
		# slice input string in two parts and concatenate 
		input = input[0:index] + input[index + len(pattern):]			 

	return 'true'

# Driver program 
if __name__ == "__main__": 
	input ='GEEGEEKSKS'
	pattern ='GEEKS'
	print checkEmpty(input, pattern) 

