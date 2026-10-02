"""
Types of programming

Imperative :
num = input()
if num % 2 == 0:
print("Even Number") 
else:
print("Odd Number )

Functional :
def evenodd(n):
   if n % 2 == 0 :
    return "Even"
   else :
     return "Odd"
print(Evenodd(56))
print(Evenodd(90))

Object orientd :
class checker :
 def __init__(self,n):
    if n%2==0:
      print("even)
    else:
      print("odd")
num1 = checker(34)
num2 = checker(56)
"""


# classes = blueprint for creation object.

"""
Encapsulation :
it is about keeping some information safe and only letting it to be changed or looked at in specific ways . 

Polymorphism :
having many forms .

Inheritance :
when one class inherit some feature from other class . 

Abstraction : 
When we see essential part of the code , and hide the rest .

"""


# class : it is a blueprint or template for creating objects . 
class car:
     print("\nI don't have a car , I'LL buy it before 2031\n")

class cars:
    brand = "Toyato "                                               #attributes!

    def hello() :
        print("Fortuner!\n")                                              #method

# accessing
print(cars.brand)
cars.hello()

# objects - a single class can have multiple objects.
class Bags:
    name = "notyourtype"

    def details():
        print("Hello , this is a company creates bags! \n")

r = Bags()
print(r.name)
print(Bags.name)
Bags.details()