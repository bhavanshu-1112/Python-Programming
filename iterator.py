# iterator
nums = [5,6,8,9,11]
it= iter(nums)
print(it)

print(it.__next__())
print(it.__next__())
print(next(it))
for i in it:
    print(i)

