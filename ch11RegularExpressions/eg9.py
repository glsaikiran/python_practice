import re
x= 'We Just received $10:00 for Cookies'
y=re.findall(r'\$[0-9]+',x)
print(y)