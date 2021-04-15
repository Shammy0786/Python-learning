# Iterable - __iter__() or __getitem__()
# Iterator - __next__()
# Iteration -

def gen(n):
    for i in range(n):
        yield i

# g=gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

s="Shammy"
# s=54
ier=iter(s)
print(ier.__next__())
print(ier.__next__())
for c in s:
    print(c)