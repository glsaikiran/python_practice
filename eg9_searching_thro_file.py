#EG3  Searching through a file
#first inintiate fhandler to start position of file as we used previously above but if its fresh program not to initiate again and again
fhandle =open('mbox.txt')
for line in fhandle:
    if line.startswith('From:'):
        #print(line) #between print we are getting extra line because \n at end of each line read and print also add a \n
        #to remove with need to remove \n at end of each line before printing
        print(line.rstrip())
