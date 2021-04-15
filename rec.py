# def factorial_iterative(n):
#     """
#     :param n: integer
#     :return: n*n-1*n-2.....1
#     """
#
#     fsc=1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
# number = int(input("enter the number"))
# print("factoral using iteration",factorial_iterative(number))
#
# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
# num=int(input("enter number\n"))
# print("factorial using recursive",factorial_recursive(num))

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
number=int(input("enter number"))
print(fibonacci(number))
