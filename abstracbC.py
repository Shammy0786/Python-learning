# from abc import ABCMeta,abstractmethod
from abc import ABC,abstractmethod

class Shape(ABC):
# class Shape(ABCMeta==abstractmethod()):
    @abstractmethod
    def printarea(self): # This the order to define printarea() all the child class
        return 0

class Square(Shape):
    def __init__(self):
        self.side=4

    def printarea(self): # When you comment out this it will show error
        return self.side*self.side

sq=Square()
print(sq.printarea())
type=Shape() #you can create direct object to parent class