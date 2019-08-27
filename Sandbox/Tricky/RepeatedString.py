#!/usr/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

  segment_length = len(s)
  segment_count = s.count("a")
  ratio = n // segment_length  #10//3 = 3
  remainder = segment_length - n % segment_length #3 - 1 = 2
  first_segments_count = ratio * segment_count #3 * 2 = 6
  last_partial_segment_count = s.count("a", 0, segment_length - remainder) #1	
  result = first_segments_count + last_partial_segment_count #6+1 = 7
  return result
if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

