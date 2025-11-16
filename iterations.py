from itertools import combinations_with_replacement
inp=input()
inplist=[]
inplist=inp.split()
strg=inplist[0]
k=int(inplist[1])
list3=[x for x in strg]
list3.sort()
list2=list(combinations_with_replacement(list3,k))

for tuple_pair in list2: 
    fin_str=""  
    for j in range(len(tuple_pair)):
        fin_str=fin_str+ tuple_pair[j]
    print(fin_str)
