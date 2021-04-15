# def function_name_print(a,b,c,d)
#     print(a,b,c,d)
#
# function_name_print("shammy","amir","div","umar")

# def funags(*args):
#     for item in args:
#         print(item)
#
# el=["shammy","amir","div","umar"] #just add more it will added automatically
# funags(*el)


# def funags(normal,*args): # normal must befor *arge not after that
#     print(normal)
#     for item in args:
#         print(item)
#
# el=["shammy","amir","div","umar"]#just add more it will added automatically
# normal="yes this can do"
# funags(normal, *el)

def funags(normal,*args ,**kwargs): # normal must befor *arge not after that
    print(normal)
    for item in args:
        print(item)
    print("\nwe some other kind of people")
    for key, value in kwargs.item():
        print(f"{key} is a {value}")

el=["shammy","amir","div","umar"]#just add more it will added automatically
normal="yes this can do"
kw={"shammy":"Engeneer","amit":"ambani","danesh":"kid"} #here we add just write it will add automatically
funags(normal, *el,**kw)