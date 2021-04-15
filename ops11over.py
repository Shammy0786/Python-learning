class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.va1="I am inside class A' constructor"
        self.classvar1="Instance variable in class A" # Whenever classvar1 print that will look at this 1st
        self.sp="Special"

class B(A):
    classvar1="I am in class B"
    def __init__(self):
        super().__init__() # Super class calling upper class constructor
        self.var1="I am inside class B's constructor"
        self.classvar1="Instance variable in class B"
        # super().__init__() # Super class calling upper class constructor
        print(super().classvar1) # Calling directelly
a=A()
b=B()

# print(b.sp)
# print(b.classvar1)