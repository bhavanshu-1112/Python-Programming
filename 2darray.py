line = int(input("enter number of lines : "))
for i in range(line-1):
  print((line-i) * ' ' + (2*i+1) * '*')

for i in range(line-1, -1, -1):
  print((line-i) * ' ' + (2*i+1) * '*')



