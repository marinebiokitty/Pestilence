#!/usr/bin/env python
from random import randint

numwords = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']

def evidencetype(item, char):
    if item in legalnonweapon:
        return 5
    if item in legalweapon and char != pilot:
        return 5
    if item in legalweapon and char == pilot:
        return 4 # parole violation
    if item in legalbroke and char in [goodcop, badcop, pilot, vone]: 
        return 5 
    if item in legalbroke and char not in [goodcop, badcop, pilot, vone]: 
        return 2 # unfair wages
    if item in illegalslavery:
        return 2 # evidence of slavery on Chivalry regardless of character
    if item in illegalother:
        if char == goodcop:
            return 6
        if char == badcop:
            return 3
        if char == pilot:
            return 4 # parole violation
        return 1
    raise Exception('No evidence type assigned for %d, %d' % i, j)

def starttable():
    print """        \\begin{tabular}{|c|c||c|}
        \\hline
        \\bf A/I/S & \\bf C & \\bf E \\\\
        \\hline"""

def endtable():
    print """
        \\hline
        \\end{tabular}"""

def endpage():
    print """    }
}"""

def startpage(n, outof):
    print """
\\NEW{Label}{\\sAnodyneTerminal%s}{
    \\s\\MYname   {Evidence Terminal %d/%d}
    \\s\\MYloc    {}
    \\s\\MYtext   {
        \\centering""" % (numwords[n],n,outof)

legalnonweapon=[9221, 7690, 1036, 7694, 2063, 3603, 7188, 2137, 9242, 29, 9246, 7173, 9221, 9253, 8827, 124, 638, 8324, 1156, 4229, 2697, 5785, 5275, 8348, 0, 9259, 1580, 9779, 564, 7742, 2626, 579, 8772, 2632, 8703, 5710, 7249, 9226, 3155, 2574, 2647, 9817, 9819, 2142, 6757, 0103, 1642, 1127, 8300, 4719, 7280, 8511, 3700, 2677, 2680]
legalweapon=[4157, 63]
legalbroke=[6413]
illegalslavery=[9820, 5216, 8745, 5333, 3284]
illegalother=[4650, 1294, 4135, 552]
goodcop=31479
badcop=39875
pilot=84785
vone=97248
charnums=[0, 31479, 39875, 84785, 64825, 34875, 67128, 54781, 64817, 97254, 24873, 69752, 97248]
charnums.sort()
itemnums=legalnonweapon+legalweapon+illegalslavery+illegalother
itemnums.sort()

allitems={}
for i in range(1,7):
    allitems[i] = []

rowcount = 0
rowspertable=40
tablecount = 0
tablesperpage=3
pagecount = 1
numpages = 1 + int(len(itemnums) * len(charnums) / rowspertable / tablesperpage)
startpage(pagecount, numpages)
print """When uploading evidence, consult this table to determine the evidence type, then place the recording in the corresponding small envelope (behind these sheets). Unless you know otherwise, try not to look at rows other than the one you're uploading.
"""

starttable()
for i in itemnums:
    for j in charnums:
        k = evidencetype(i, j)
        allitems[k] = allitems[k] + [(i,j)]
        if rowcount >= rowspertable:
            tablecount = tablecount + 1
            rowcount = 0
            endtable()
            if tablecount >= tablesperpage:
                pagecount = pagecount + 1
                tablecount = 0
                endpage()
                startpage(pagecount, numpages)
            else:
                print "        \\quad"
            starttable()
            
        if j == 0:
            print "%04d& &%d\\\\" % (i, k),
        else:
            print "%04d&%05d&%d\\\\" % (i, j, k),
        rowcount = rowcount+1
endtable()
endpage()

# For debugging
#for i in range(1,7):
#    print 'Evidence type '+str(i)+':'
#    print allitems[i]
