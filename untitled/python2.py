# x=1
# while x<5:
#     print("Bhavanshu")
#     x+=1
# i=1
# while i<5:
#     j=1
#     print("IIIt")
#     while j<3:
#         print("kota")
#         j+=1
#     i+=1
# x =1
# while x<5:
#     y=1
#     print("IIIT", end=" ")
#     while y<3:
#         print("Kota", end = " ")
#         y+=1
#     x+=1
#     print()
 # for loop
# x = "Python"
# for i in x:
#     print(i)
# for i in range(1,5):
#     print(i)
# x = [1,2,'A', 'B']
# for i in x:
#     print(i)
# for i in range(5):
#     print(i)
# x = [1,2,"A","B"]
# for i in range(len(x)):
#     print(i,x[i])

# x = int(input())
# if x==1:
#     f = 2
# elif x==0:
#     f = 2
# else:
#
#     for i in range(2,x):
#         if x%i==0:
#            f = 0
#            break;
#         else:
#           f = 1
# if f==0:
#     print("not prime")
# elif f==2:
#     print("neither composite and nor prime")
# else:
#     print("prime")
x = int(input())
for i in range(1,x+1):
    for j in range (1,x+1):
        print("*",end=" ")
    print("\n")