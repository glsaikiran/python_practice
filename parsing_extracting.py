data='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos=data.find('@')
spce_pos=data.find(' ',pos)
print(data[pos+1:spce_pos])
