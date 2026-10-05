# they are special type of methods starts and ends with __ double underscores
# print(dir(int))

class Animal:

    def __init__(self,name):
        self.name=name 

    def __str__(self):
        return f"Hello my name is {self.name}"

obj = Animal("Lion")
obj2= Animal("Giraffe")

print(obj)
print(obj2)



class numbers:

    def __init__(self,num):
        self.num=num

    def __add__(self,other):
        return self.num + other.num

    def __eq__(self,value):
        return self.num == value.num 

num1 = numbers(20)
num2 = numbers(30)

print(num1 + num2)
print(num1 == num2)