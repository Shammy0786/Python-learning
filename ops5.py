class Employee:
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
    def fron_dash(cls, string):
        # pr=string.split("-")
        # return cls(pr[0],pr[1],pr[2])
        return cls(*string.split("-"))


shammy=Employee("shammy",0,"Student")
harry=Employee("harry", 6554, "Youtuber")
kim=Employee.fron_dash("kim-76-stu")
print(kim.printdetails())