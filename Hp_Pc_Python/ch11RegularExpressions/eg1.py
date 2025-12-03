#using find print all the line which has "From:" in it
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    pos=line.find('From:')
    if pos>=0:
        print(line)
#using regular expression
import re
print("\nNow using RE\n")
hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('From:',line):
        print(line)