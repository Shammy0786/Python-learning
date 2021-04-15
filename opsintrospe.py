class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f" This employee is {self.fname} {self.lnane}"

    @property # This for calling without parenthesis email
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter #Setting the email and changing also fname and lname
    def email(self,string):
        name=string.split("@")[0]
        self.fname=name.split(".")[0]
        self.lname=name.split(".")[1]

    @email.deleter # delete the email
    def email(self):
        self.fname=None
        self.lname=None

# object introspection
sham=Employee("sham","kam")
# print(type(sham))
# print(id(sham))
# print(type("this is me"))
# print(id("this is me"))
print(dir(sham)) #It will shows the all things which i can perform with this

import inspect
print(inspect.getmembers(sham))