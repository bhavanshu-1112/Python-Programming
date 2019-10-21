#generator
def top():
    yield 1
    yield 4
    yield 5
    yield 7
    yield 8

value = top()
print(value)
print(value.__next__())
print(value.__next__())
for i in value:
    print(i)
