import re
x= 'From: using the: character'
y= re.findall(r'^F.+?:',x)
print(y)