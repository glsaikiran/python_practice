counts=dict()
fhandle=open(input('Enter File name: '))
for line in fhandle:
    line=line.rstrip()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
#Until above only gets count of words in a file ,now below we go to the dictionary and print largest count word
bigword=None
bigcount=None
for key,value in counts.items():
    if bigcount is None or value > bigcount:
        bigword=key
        bigcount=value
print("Largest counted word: ",bigword," ",bigcount)
