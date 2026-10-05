# putting data (variables) and code (functions) together in one place . 

class Factory:
    # name = "Kia"                                                 #public class attribute 
    __name = "Kia"                                                 #private class attribute 
    a = 12                                                    

    def __init__(self,type,tyre,color):
        self.color=color                                          #public object attribute
        self.__type=type
        self.tyre=tyre

    def __details(self):                                         #public MEthod
        print("Hello your details are :")

class hello(Factory):                                              #inherited class
    print(Factory.a)
    # print(Factory.__name)

obj = Factory("Sedan","MRF","Black")

# obj.name = "maruti"
# print(obj.name)
# print(obj.tyre)

# obj.details()



class hello:
    __a = 12

    @classmethod
    def info(self):
        print(self.__a)

obj = hello()
obj.info()

# print(obj.__a)