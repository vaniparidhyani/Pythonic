#!/usr/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
  p = 0
  for i in ar:
    c = ar.count(i)
    print c
    if c%2 == 0:
      p += c/2
    else:
      p += (c-1)/2
    ar = filter(lambda a: a != i, ar)
    print p
    print ar
  return p




if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

