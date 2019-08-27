#!/usr/bin/python

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print ([x for x in a if x%2 == 0])
print filter(lambda x: x % 2 == 0, a )

print (list(map(lambda x: x, 'human')))

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print squared
#print reduce(lambda x: x**2, items)
print list(x**2 for x in items)
print [x**2 for x in items]

print reduce(lambda x, y: x * y,items)
