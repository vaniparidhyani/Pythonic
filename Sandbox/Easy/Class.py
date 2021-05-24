#!/usr/bin/python

class Classy(object):
    def __init__(self):
        self.items = []
    def addItem(self,i):
        self.items.append(i)
    def getClassiness(self):
        out = 0
        for j in self.items:
            if j == "tophat":
                out += 2
            elif j == "bowtie":
                out += 4
            elif j == "monocle":
                out += 5
        return out

# Test cases
me = Classy()

# Should be 0
print me.getClassiness()

me.addItem("tophat")
# Should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print me.getClassiness()

me.addItem("bowtie")
# Should be 15
print me.getClassiness()
