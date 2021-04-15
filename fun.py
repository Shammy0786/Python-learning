# def fun1(a,b):
#     print("you are in fun1", a+b)
#     # print(fun1(5,4))


def function2(a,b):
    """this is a function which calculate avg of two numbers"""  #doc strings
    avg=(a+b)/2
    return avg

v=function2(4,7)
print(function2.__doc__)
print(v)