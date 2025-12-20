d={'a':10,'c':1,'e':22,'d':1}
print(d.items()) #here dict is converted o tuples air list and sorted function only sorts keys of the dict as its first in tuple pair.
print(sorted(d.items()))

# to extract sorted items
for k,v in sorted(d.items()):
    print(k,v)
