#!/usr/bin/env python
from random import randint
charnums=[]
for i in range(12):
    charnums.append(randint(0,99999))
charnums.sort()
itemnums=[]
for i in range(20):
    itemnums.append(randint(0,99999))
itemnums.sort()

print """
\\begin{tabular}{l|c||r}
\\bf Item/sign/ability number & \\bf Character badge number & \\bf Evidence type \\\\
\\hline"""
for i in itemnums:
    for j in charnums:
        print "%05d&%05d&%d\\\\" % (i, j, randint(1,5)),
print "\end{tabular}"
