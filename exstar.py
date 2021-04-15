#star printing

print("pattern printing")
num=int(input("enter rows : "))
print("enter 0 or 1 : ")
bool_val=input("1 is ture and 0 is false : ")
if bool_val=="1":
    for i in range(0,num+1):
        print("*"*i)
if bool_val=="0":
    for i in range(num,0,-1):
        print("*"*i)