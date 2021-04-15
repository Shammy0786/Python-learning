print("Enter the element of the list \n")
size = int(input("Enter the size \n"))
mystr = []
for i in range(size):
    mystr.append(int(input("enter the element \n")))
print(f"your list is \n {mystr}")

Reverse1 = mystr[:]
Reverse1.reverse()
Reverse2 = mystr[::-1]

Reverse3 = mystr[:]
for i in range(len(Reverse3)//2):
    Reverse3[i],Reverse3[len(Reverse3) -i -1]= Reverse3[len(Reverse3) -i -1],Reverse3[i]

print(f"1st Reverse list of {mystr} is {Reverse1}")
print(f"2nd Reverse list of {mystr} is {Reverse2}")
print(f"3rd Reverse list of {mystr} is {Reverse3}")

if Reverse3 == Reverse1 == Reverse2 :
    print("All three gives same result")

