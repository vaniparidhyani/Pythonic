MAX_POINT = 3; 
ARR_SIZE = 100; 
  
count = 0
arr = [0] * ARR_SIZE; 
def printCompositions(n, i): 
      
    # array must be static as we  
    # want to keep track of values  
    # stored in arr[] using current  
    # calls of printCompositions() in 
    # function call stack*/ 
    if (n == 0): 
        printArray(arr, i); 
    elif(n > 0): 
        for k in range(1,MAX_POINT + 1): 
            arr[i] = k; 
            printCompositions(n - k, i + 1); 
  
# UTILITY FUNCTIONS */ 
# Utility function to print array arr[] */ 
def printArray(arr, arr_size): 
    for i in range(arr_size): 
        print arr[i]
    count = count + 1 
    print
  
# Driver Code 
n = 4; 
print("Different compositions formed " + 
         "by 1, 2 and 3 of", n, " are"); 
printCompositions(n, 0);
print "TOTAL COUNT"
print count 
