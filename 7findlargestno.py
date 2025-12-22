nolist=input('enter list of numbers to find  largest value')
nolist=list(nolist)
a=nolist[0]
for i in nolist:
    if i>a:
        largestvalue=i
        a=i
        print('a: ',a)
print('Largest value is:',largestvalue)