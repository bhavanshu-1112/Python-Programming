n = int(input("enter size of list : " ))
ls = []
for i in range(n):

    ls.append(int(input()))
print(ls)
ls1 = []
ls2 = []
def func(ls):
    for i in range(ls):
        if i%2==0:
            ls1.append(i)
        else:
            ls2.append(i)
    print(ls1)
    print(ls2)