#!/usr/bin/python

#given a string, replace every letter with its position in the alphabet.

#If anything in the text isn't a letter, ignore it and don't return it.

# Example "a" = 1, "b" = 2, etc.  

#alphabet_position("The sunset sets at twelve o' clock.")
#Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

#ord() : It coverts the given string of length one, return an integer representing the unicode code point of the character.
# a-Z = 97-122
# A-Z = 65-90

def alphabet_position(text):

    # Below will remove all the spaces
    #text = text.replace(" ","")

    #Below will keep only alphabets and nothing else in the text
#    text = ''.join([i for i in text if i.isalpha()])

#    return " ".join((map(str,[ord(char) - 96 for char in text.strip().lower()])))
     

    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

if __name__ == "__main__":
  print alphabet_position("The sunset sets at twelve o' clock.")
