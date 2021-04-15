class Employee:
    no_of_leaves=5 # Class variable
    pass

shammy=Employee()
harry=Employee()

shammy.prof="student"
shammy.salary=0
harry.prof="youtuber"
harry.salary=57476

print(shammy.salary,harry.salary)
shammy.no_of_leaves=6 # you cannot change by the instance variable to class variable
print(Employee.no_of_leaves)
print(harry.__dict__) # It shows the dictionary of the object

Employee.no_of_leaves=6 #you can change no of leaves by only class variale not instance variable
print(harry.no_of_leaves)