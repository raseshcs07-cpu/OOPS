# many forms 

class animal:

    def speak(self):
        print("\nAnimals can not speak")

class humans:
    def speak(self):
        print("Humans can speak")

obj = animal()
obj1 = humans()

obj.speak()
obj1.speak()