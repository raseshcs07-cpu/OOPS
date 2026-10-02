# constructor :
class Bags:
    def __init__(self,material,zips,pockets):
        self.material=material
        self.zips=zips
        self.pockets=pockets

reebok = Bags("\nleather",3,2)
campus = Bags("polyster\n",2,4)
# Bags()
# self - targets the location of the objects.
print(reebok.material)
print(campus.material)


class animal:
    a = 12                                  #class attibute

    def __init__(self,name):
        self.name=name                      #object\instance attribute

    def hello(self):                        #instance method
        print(f"hello how are you , my name is {self.name}")

    @classmethod
    def details(cls):                        #class method
        print(f"I am fine! {cls.a}")

    @staticmethod
    def speak():                             # static method, this will not target any location.
        print("hello i am a static method!")

obj = animal("Lion")
print(obj.name )
obj.hello()
obj.details()
obj.speak()