# def add(a,b):
#     return a+b

# add = lambda x,y : x+y
# print(add(5,6))
def a_first(a):
    return a[1]

a=[[1,34],[4,7],[6.7]]
a.sort(key=a_first)
a.sort(key=lambda x:x[1])
print(a)