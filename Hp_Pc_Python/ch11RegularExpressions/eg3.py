#instead of checking for match,if we want to extract the match we use re.findall()
#extract only numbers from string
import re
x='My 2 favorite numbers are 19 and 42'
y=re.findall('[0-9]+',x)
print(y)