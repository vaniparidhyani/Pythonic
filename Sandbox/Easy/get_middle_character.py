#!/usr/bin/python

def get_middle(s):
    #your code here
    l = len(s)-1
    if l%2 == 0:
      return s[(l)/2]
    else:
      return s[l/2:(l/2)+2]
    


if __name__ == "__main__":
  print get_middle('avania')
