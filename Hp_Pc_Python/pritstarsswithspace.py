# Desired Output
#       *
#       * *
#       * * * *
#inp= int(input('Enter a number'))
#rg=range(1,inp+1)
#for itera in rg:
#    print(("*"+" ")*itera)

# in traingle shape
inp= int(input('Enter a number'))
row_and_no_of_stars=range(1,inp+1)
no_of_spaces=inp
for itera in row_and_no_of_stars:
    no_of_spaces-=1
    print(str(" "*(no_of_spaces))+"* "*itera)
