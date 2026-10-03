# putting data (variables) and code (functions) together in one place . 

class Factory:
    name = "Kia"                                                 #public class attribute 
    _old = 12                                                    #protected    

    def __init__(self,type,tyre,color):
        self.color=color                                          #public object attribute
        self.type=type
        self.tyre=tyre

    def details(self):
        print("Hello your details are :")

obj = Factory("Sedan","MRF","Black")

obj.name = "maruti"
print(obj.name)

obj.details()