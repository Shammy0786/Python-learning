# def func1():
#     print("shammy")
#
# func2=func1
# del func1
# func2()

# def funret(n1):
#     if n1==0:
#         return  print
#     if n1==1:
#         return int
#
# a=funret(1)
# print(a)

# def exictor(func):
#     func("shammy")
#
# exictor(print)


def dec1(func1):
    def nowexec():
        print("executing now...")
        func1()
        print("executed.")
    return nowexec
@dec1 #decorator
def who_is_shammy():
    print("shammy is a good boy")

# who_is_shammy=dec1(who_is_shammy) #decorator
who_is_shammy()

