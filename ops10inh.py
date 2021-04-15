class Employee:
    var=7 # Public variable
    no_of_leaves=5 # Class variable
    _n1=5 # Protected variable
    __n2=76 # Private variable
    def __init__(self, aname, asalary, aprof): #constructor it takes arguments
        self.name= aname
        self.salary=asalary
        self.prof=aprof

    def printdetails(self):
        print(f"Name is {self.name}, prof is {self.prof} and salary is {self.salary}")
    @classmethod
    def change_leaves(cls,newleaves): #This function capble to change class variable
        cls.no_of_leaves=newleaves

    @classmethod
    def fron_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(str):
        print("this is " + str)

emp=Employee("dr",58,"drc")
print(emp._n1) # Protected variable can acces like this
print(emp._Employee__n2) # Private variable can access like this (Nameanling) done by python