class Employee:
    var=7
    no_of_leaves=5 # Class variable
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

    def __add__(self, other): #Dunder addition (operator overloading)
        return self.salary+other.salary

    def __truediv__(self, other): # div overloading
        return self.salary/other.salary

    def __repr__(self):
        return f"Epmloye '{self.name}' '{self.salary}' '{self.prof}' "

    def __str__(self):
        return (f"Name is {self.name}, prof is {self.prof} and salary is {self.salary}")



emp1=Employee("rima",58,"staf")
# emp2=Employee("rim",8,"stafif")
# print(emp1+emp2)
# print(emp1/emp2)
print(emp1) # Here is 1st priority for str() whether rper() present or not
print(str(emp1)) # when you camment out str() method it will not show any error repr() will executed
print(repr(emp1)) # you have to call repr() like this but in case os str() you dinnt required

