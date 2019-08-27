#!/usr/bin/python

#Write a program to find the mirror image of a binary tree? 

#if a tree is like 

#01 
#02 03 
#04 05 06 07 

#The mirror will be like 

#01 
#03 02 
#07 06 05 04

def mirror_image(tree):
  for i in tree:
    print ' '.join(str(e) for e in reversed(i))

tree=[['01'], ['02','03'],['04','05','06','07']]
mirror_image(tree)

