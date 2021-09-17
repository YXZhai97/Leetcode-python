

class Pet:
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old")

    def speak(self):
        print("I don't know what I say")



class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age) #inharite the init from parent class
        self.color=color

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old and I'm {self.color}")

    def speak(self):
        print("Meow")




class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass
p=Pet("Tim", 10)
p.show()
p.speak()
c=Cat("Bill",12,'Red')
c.show()
c.speak()
d=Dog("jill",1)
d.show()
d.speak()
f=Fish("fish",2)
f.show()
f.speak()

