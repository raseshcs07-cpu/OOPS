# it is not in python. , but we can acsess it with library.
# hiding unneecessary code. , that contains one or more abstract methods ., subclass must provide the implementation.

from abc import ABC , abstractmethod

class enforce(ABC):

    @abstractmethod
    def enginestart():
        pass


class bike(enforce):
    def enginestart():
     pass

class car(enforce):
    def enginestart():
     pass

class truck(enforce):
    def enginestart():
     pass

obj1 = bike()
obj2 = car()
obj3 = truck()