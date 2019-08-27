#!/usr/bin/python

string = "1123"

codes = [ chr(ord('a') + i) for i in range(0, 26) ]


def find_codes(num, code=[]):

    if len(num) == 0:
        try:
            print ''.join([ codes[int(char) - 1] for char in code ])

            
        except:
            
            pass
    else:
        if num[0] != '0':

            find_codes(num[1:], code + [num[0]])

            if len(num) > 1:

                find_codes(num[2:], code + [num[:2]])

find_codes(string)
