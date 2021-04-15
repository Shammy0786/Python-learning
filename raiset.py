# a = input("Whats your name")
# b = input(f"How mush do you earn ")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so can't process")
# if a.isnumeric():
#     raise Exception("number not allowed")
# print(f"Hello {a}")

# a= input("Enter your name")
# try:
#     print(b)
# except Exception as e:
#     if a=="shammy":
#         raise ValueError("shammy is blocked")
#     print("exception handle")
# == and is
a = [3,5,"53"]
b = [3,5,"53"]
print(b is a)
print(a is b)
print(a==b)