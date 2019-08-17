import os

# newFile = open("pythonfile.txt","w+")
#
# for i in range(1,11):
#     newFile.write("\n welcome to python")

newFile = open("pythonfile.txt","r")

for i in range(1,12):
    print(newFile.read(5))

os.rename("pythonfile.txt","newFilepython.txt")
os.remove("newFilepython.txt")
newFile.close()

# gives in which mode file is working
print(newFile.mode)
# gives the name of the file
print newFile.name
# softspace() method returns a boolean , whether a space cahracter needs to be printed before another value

print(newFile.softspace)
# seek() method gives the pointer that to which sapce file is pointing
#
print newFile.seek(322)
# tell() meythod gives us the
print(newFile.tell())