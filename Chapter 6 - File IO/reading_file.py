file1= open("FileOperations.txt","r")
print(file1.read())
print(file1.read())
print(file1.tell())
file1.seek(0,0)
print(file1.read())
file1.seek(0,0)
print(file1.read(22))
print(file1.read(22))
print(file1.read(11))