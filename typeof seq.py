# types of sequences:
 # list tuples dictionaries , strings, sets

list = [1,23,4,5,6,"fdfd",'dfd']
# remove() just removes the element

print list.remove(23)
print list
print ("--------")
# pop() just pop out the element from the list
# and returns
print list.pop(4)
print list
print ("--------")

list1 = []
for x in range(1,6):
    list1.append(x**2)
print list1
print ("--------")
list2 = [x**2 for x in [1,2,3,4,5,6]]
print list2
print ("--------")
print (x**2 for x in [1,2,3,4,5,6,7,8,9,0])
print ("--------")
# list comprehension
print [x**2 for x in [1,2,3,4,5,6]]