#With Break
count=5
while count>0:
  count=count-1
  if count == 1:
    print('With break')
    break
  print(count)



  #Without Break
count2=5
while count2>0:
  count2=count2-1
  print(count2)
print('without Break')

#One more example of Break
while(True) :
  a= input("Enter No. to double it Or enter 'done' to exit ")
  if a=='done':
    print('Bye')
    break #Breaks the while loop goes to next stt after while loop
  b=int(a)
  c=b*2
  print('Result: ',c)
#Note:Here if i input other words than 'done' it gives
#type error at line 25 int conve. to resolve this we use try continue in 
#next chapter it will be covered.
    