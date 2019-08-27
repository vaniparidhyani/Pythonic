#!/usr/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
  level = valley = 0
  for i in s:
    if i == 'U':
      level += 1
      if level == 0:
        valley += 1
    else:
      level -= 1
    print i
    print level
    print valley
    print
  return valley

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

