# decorators:
def timer(func):

    def wrapper():
        print("\nStarting...")
        func()
        print("Done....")
        print("_" * 45)
    return wrapper

@timer
def say_hello():
    print("Hello, My name is Rasesh!")

say_hello()



# *args & **kwargs
# def addition(a,b):
#     return a + b
# print(addition(20,30,50))

def addition(*args):
    s = 0
    for i in args:
        s = s + i
    return s

print(addition(20,30,50,60,7,4,4,4,3,3,2,22))


def info(**kwargs):
    return kwargs

print(info(name="Rasesh",age=19,profession= "engineer"))


def timer(func):

    def wrapper(*args,**kwargs):
        print("\nStarting...")
        func(*args,**kwargs)
        print("Done....")
        print("_" * 45)
    return wrapper
        
@timer
def addition(a,b,c):
    print(a+b+c)
addition(10,20,30)



# ternary operations:
a=20
print("even number") if a%2 == 0 else print("odd number")



# Comprehension
squares = [x**2 for x in range(5)]
print(squares)

even = [x for x in range(10) if x%2==0]
print(even)

square = {x : x**2 for x in range(10)}
print(square)

squres = {x%3 for x in range(100)}
print(squres)

a = [1,2,3,4,5,6,7,8,90,2334,5,6,5,67876,54567,87654,34567,65,432,2345,4321]
b = [i for i in a if i%2==0]
# for i in a:
#     if i%2 ==0:
#         b.append(i)
print(b)



# Lambda func:
square = lambda x: x**2
add = lambda a, b: a+b
check = lambda x: "even" if x%2==0 else "odd"

print(square(199))
print(add(10,99))
print(check(200))


squares = lambda *args : sum(args)
print(square(10,2,30,40))




# map(),filter(),zip():
num = [1.2,3,45,6,7,89,44]

doubled = list(map(lambda x: x+2 , num))
print(doubled)
even = list(filter(lambda x: x%2==0 , num))
print(even)

name = ["A","B","C","D"]
score = [10,20,30,40]
pairs = list(zip(name , score))
print(pairs)