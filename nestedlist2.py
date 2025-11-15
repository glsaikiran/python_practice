#find the secong lowest student names,if 2 has same score display as per alphabetical order
full_list=[]
score_list=[]
score_sorted=[]
sec_low_grade_list=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    full_list.append([name,score])
    score_list.append(score)
for i in score_list:
  if i not in score_sorted:
    score_sorted.append(i)
score_sorted.sort()
sec_low_grade=score_sorted[1]
for i in full_list:
  if sec_low_grade==i[1]:
    sec_low_grade_list.append(i[0])
sec_low_grade_list.sort()
for i in sec_low_grade_list:
  print(i)



