#!/usr/bin/python

# recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has two digits, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

# Example number is 429 then => 4+2+9 => 15 => 1+5 => 6

def sum_of_digits(num):
  l = len(str(num))
  
  if l>0:
    sum = 0
    for i in str(num):
      sum = sum + int(i)
    if len(str(sum))>1:
      sum_of_digits(sum)
    else:
      print sum
if __name__ == "__main__":
  sum_of_digits(429)
