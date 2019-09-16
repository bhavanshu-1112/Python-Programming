A = []
n = int(input("enter size : "))
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)
print(A)
# print(len(A))
# print(len(A[0]))
B = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    B.append(row)
print(B)
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(B)):
            result[i][j] += A[i][j]*B[k][j]
for r in result:
    print(r)


