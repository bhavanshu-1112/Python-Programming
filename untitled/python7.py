from array import *

a = array('i',[])
x = int(input())


for i in range(0,x):
    j = int(input())
    a.append(j);
flag = 0
f = int(input())
for i in a:
    if f==i:
        print("yes number is present",id)
        break
else:
    print("no number is not present")

