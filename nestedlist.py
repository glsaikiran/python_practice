for i in range(int(input())):
        name = input()
        score = float(input())
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list1.append([name,score])
        list2.append(score)
for i in list1:
    if i not in list3:
        list3.append(i)
sec_low=list3[-2]
for i in list1:
    if i[1]==sec_low:
        list4.append(i[0])
list4.sort()
for i in list4:
    print(i)
