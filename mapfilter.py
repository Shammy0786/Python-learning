numbers = ["3","4","6","66"]
numbers=list(map(int,numbers)) # same as below

# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])

# numbers[3]=numbers[3]+1
# print(numbers[3])

# def sq(a):
#     return a*a
# num=[2,5,55,5,2,3,5,3]
# square=list(map(sq,num))
# print(square)

# num=[2,5,55,5,2,3,5,3]
# square=list(map(lambda a:a*a ,num))
# print(square)

# def sq(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func=[sq,cube]
# for i in range(5):
#     val=list(map(lambda x:x(i),func))
#     print(val)

#filter function

# list1=[5,3,8,79,42,6]
# def is_greter_5(item):
#     return item>5
# gr_than_5=list(filter(is_greter_5,list1))
# print(gr_than_5)

# reduce funvtion

from functools import reduce

list=[4,4,5,7]
# num=reduce(lambda x,y:x+y, list)
num=0
for i in list:
    num =num+i
print(num)
