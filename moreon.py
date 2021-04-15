f=open("shammy.txt")
print(f.tell()) #it tell us where is the pointer
print(f.readline())
# f.seek(0) #reset pointer from 0
print(f.readline())
f.seek(10) #reset pointer from 10
f.close()