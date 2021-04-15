class Employee:
    no_of_leaves=5 # Class variable
    def __init__(self, aname, asalary, aprof): #constructor it takes arguments
        self.name= aname
        self.salary=asalary
        self.prof=aprof

    def printdetails(self):
        print(f"Name is {self.name}, prof is {self.prof} and salary is {self.salary}")



shammy=Employee("shammy",0,"Student")
# harry=Employee()
# shammy.name="shammy"
# shammy.prof="student"
# shammy.salary=0
# harry.name="harry"
# harry.prof="youtuber"
# harry.salary=57476

print(shammy.salary)
print(shammy.printdetails())