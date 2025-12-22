#Top 10 most common words in a file
fhand=open('romeo.txt')
counts=dict()
tmp=list()

for line in fhand:
    line =line.rstrip()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
for k,v in counts.items():
    tmp.append((v,k))
tmp=sorted(tmp,reverse=True)
for k,v in tmp[:10]:  # taking only first 10 tuples in the list
    print(k,v)

#shorter version,List comprehension
c={'a':10,'b':1,'c':22}
print(sorted([(v,k) for k,v in c.items()]))
