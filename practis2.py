n = int(input("How many apple Shammy got \n"))
mn = int(input("Enter Min. numbers of people \n"))
mx = int(input("Enter max. numbers of people \n"))

# if n%mn == 0:
#     print(f"Diviser of {n} is {mn}")
#
# else:
#     print(f"{mn} is not diviser of {n} \n")
#
# if n%mx ==0:
#     print(f"Diviser of {n} is {mx} \n")
#
# else:
#     print(f"{mx} is not diviser of {n} ")
#
for i in range(mn,mx+1):
    if n%i == 0:
        print(f"{i} is divisor of {n} \n")
    else:
        print(f"{i} is not divisor of {n} \n")

