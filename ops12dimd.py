class A:
    def po(self):
        print(" This a method from class A")

class B(A):
    def po(self):
        print(" This a method from class B")

class C(A):
    def po(self):
        print(" This a method from class C")

class D(B,A):
    def po(self):
        print(" This a method from class D")

a=A()
b=B()
c=C()
d=D()
print(d.po())