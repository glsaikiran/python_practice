c={'a':10,'c':1,'e':22,'d':1} # sorting by values instead of keys
tmp=list()
for k,v in c.items():
    tmp.append((v,k))
tmp=sorted(tmp,reverse=True)
print(tmp)
