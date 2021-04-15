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

class Player:
    var=9
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def printplay(self):
        print(f"the name is {self.name} and game is {self.game}")

class coolprogrammer(Player,Employee):
    language="c++"
    def printlag(self):
        print(self.language)

shammy=Employee("shammy",0,"Student")
harry=Employee("harry", 6554, "Youtuber")
sumit=Player("sumit",["cricket","football"])
sam=coolprogrammer("sam",["cricket"],)
print(sam.printplay())
