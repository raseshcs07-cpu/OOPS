# possession that comes to heir . 
# in python it works for classes .

class Animals:                    #parent class
     a = 12

     def __init__(self,name):
        self.name=name

     def details(self):
        print(f"Hello your name is {self.name}")

class humans(Animals):                   #inherit class
    pass

obj = Animals("Lion")
obj2 = humans("Harsh")

print(obj.name)
obj2.details()
print(obj2.a)


class bagfactory:

    def __init__(self,material,zips,pockets):
        self.material=material
        self.zips=zips
        self.pockets=pockets


    def details(self):
        print(self.material)
        print(self.zips)
        print(self.pockets)

class reebok(bagfactory):

    def __init__(self,material,zips,pockets,color):
        super().__init__(material,zips,pockets)
        self.color=color

    def details(self):
        print(self.color)
        return super().details()

class Campus(reebok):
    def __init__(self,material,zips,pockets,color,size):
        super().__init__(material,zips,pockets,color)
        self.size=size

    def detials(self):
        print(self.size)
        return super().details()


bag1 = bagfactory("Leather",3,2)
bag2 = reebok("Polyster",2,4,"red")
bag3 = Campus("Travel",3,7,"orange",5)

print(bag1.material)
print(bag2.zips)
print(bag3.pockets)