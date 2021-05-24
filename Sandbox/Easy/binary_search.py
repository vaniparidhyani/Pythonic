def binary_search(l, start_index, end_index, x): 
	if end_index >= start_index: 

		mid = (end_index + start_index) // 2

		if l[mid] == x: 
			return mid 

		elif l[mid] > x: 
			return binary_search(l, start_index, mid - 1, x) 

		else: 
			return binary_search(l, mid + 1, end_index, x) 

	else: 
		return -1

l = [ 1, 2, 3, 4, 5, 6 ] 
x = int(input("enter no to search"))
i=0
result = binary_search(l, i, len(l)-1, x) 

if result != -1: 
	print "Element present at index %d" % result 
else: 
	print "Element not present in list" 
