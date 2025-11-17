#EG1
fhandle=open('mbox.txt')  #if no  specific attribute its read mode.it gives sequence with each line in a file as string
count=0
for line in fhandle:
    count=count+1
print(count)

#EG2   Reading whole file
#As in previous for loop file handler is at end of string so if i didnot again initiate fhandle it will start to read file from end and returns 0
fhandle=open('mbox.txt')
inpt= fhandle.read()  # reads whole files saves as single string as line1\nline2\n...
print(len(inpt))
list1=inpt.split('\n')
print(len(list1)) #gives number of line same as above EG1 but print has extra \n so additional line is counted


