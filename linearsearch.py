def search(arr,n,x):
    for i in range(0,n):
        if arr[i]==x:
            return i

arr = [2,3,5,6,7,98];
x = 3
n = len(arr)
result = search(arr,n,x)
if result==-1:
    print("element not present in array")
else:
    print("element is present at index",result)

