n = int(input())
f = lambda s:s*s
rs = f(n)
print(rs)
print("-----------")

# n = int(input())
f = lambda a,b,c,d,e,f,g:a*b*c*d*e*f*g
rs = f(4,5,6,4,8,9,10)
print(rs)
print("-----------")
# n = int(input())
f = lambda s,*b:s*(b)
rs = f(2,3,4,5)
print(rs)
print("-----------")

