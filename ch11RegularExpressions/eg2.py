#using startswith() to print lines starting with "From:"
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if line.startswith('From:'):
        print(line)
#using regular expression to print lines starting with "From:"
import re
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^From:'): # here  "^" indicates string should startwith  
        print(line)