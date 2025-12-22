#instead of checking for match,if we want to extract the match we use re.findall()
#extract only numbers from string
import re
x='My 2 favorite numbers are 19 and 42'
y=re.findall(r'\d+',x)
print(y)
#if r is not kept in regular expre.Python handles backslashes in strings
#before passing them to regex.​
#The Problem Step-by-Step
#You wrote: "\d+" (normal string)
#Python sees \d and thinks "is this an escape like \n (new line)" → but its not found
# so SyntaxWarning
#Regex engine gets d+ only (backslash lost) → No digit matching! gives empty output
#if you keep r it takes raw string not removing backlash to regex.