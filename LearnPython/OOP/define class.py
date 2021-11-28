class Cat:
    def __init__(self,name):
        print("inside init method")
        self.name=name

    def __str__(self):
        # must return a string
        return "I am a cat"

    def __del__(self):
        print("%s I am gone" %self.name)

    def eat(self):
        print("cat like fish")

    def drink(self):
        print("cat drink water")

class Person:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def __str__(self):
        return "My name is %s weight is %.2f kg" % (self.name, self.weight)

tom=Cat("Tom")
tom.eat()
tom.drink()
print(tom.name)
lazy_cat=Cat("Lazy")
print(lazy_cat.name)
print(tom)
xiaoming=Person("xiaoming",75)
print(xiaoming)




