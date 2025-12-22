#tuples and dictionaries
d={'sa':1,'sr':2,'ju':4}
for key,value in d.items():  # here d.items() convert dict 'd' to a list of tuple pairs(key,value)
    print(key,value)
print(d.items())  #creates a List with (key,value) tuple pairs in it
