class Person:
    number_of_people=0 # same for all person instances

    def __init__(self, name):
        self.name=name
        Person.add_person() #when create a person instance the number adds one

    @classmethod  #act on the class itself
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people +=1

print(Person.number_of_people)
p1=Person("eason")
print(p1.number_of_people)
p2=Person("Tim")
print(p2.number_of_people)
print(Person.number_of_people)
Person.add_person()
print(Person.number_of_people)
print(p1.number_of_people)

