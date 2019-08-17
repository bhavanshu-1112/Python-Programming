# sequences are thye continuous collection of datatype
# it allows us to do different operations like indexing or slicing
# sequience operstions : concatenation, repetition, indexing , slicing, membership testing
list = ["python","android", "web"]

print(list[1])
print list[0:2]
print list[-1]
print list[-2]

list = list + ["React", "Angular","ML"]
print list
print list*3
 # membership testing
print("android" in list, "Data Science" in list)
