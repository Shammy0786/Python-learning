f=open("shammy.txt")
f=open("shammy.txt","rb") #binary reading
content=f.read()
# content=f.read(6)
# print("1",content)
print("2", content)
for line in f:
    print(line)

print(f.readline())
print(f.readline())

print(f.readlines())

f.close()
