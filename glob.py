# i=10 #global scoe vRIble
# def function1(n):
#     i=5 #local
#     m=6 #local
#     global i
#     i=i+7
#     print(i,m)
#     print(n,"yes it is")
#
# function1("really")
# print(m)
x=76
def shammy():
    x=3
    def azad():
        global x # it cannot be global becouse we didnt define outside the fun
        x=66
    # print("befor calling azad()",x)
    azad()
    print("after calling azad()",x)
shammy()
print(x) #its create global x

