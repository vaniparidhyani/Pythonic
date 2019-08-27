#!/usr/bin/python

my_integer = 3
my_binary = format(my_integer, "b")
print "Binary format of %s is %s" %(str(my_integer), my_binary)


# Convert the binary to integer
print "Convert binary back to integer"
back_to_integer = int(my_binary, 2)
print back_to_integer
