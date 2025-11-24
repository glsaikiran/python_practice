counts=dict()
fhandle=open(input('Enter File name: '))
for line in fhandle:
    line=line.rstrip()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
