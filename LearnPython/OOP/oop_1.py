# Object Orientated Programming in Python

# x is a int object
x = 1

# y is  str object
y = "hello"
# a method upper() work on string object y
print(y.upper())


# creak our own class
class Dog:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age

    def set_age(self,age):
        self.age=age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


    def add(self,x):
        return x+1

    def bark(self):
        print("bark")

# create a dog object with class Dog
dog = Dog("Tim",2)

# '__main__.Dog' DOG class in model Main
print(type(dog))

print(dog.get_name())
print(dog.get_age())
dog.set_age(5)
print(dog.get_age())

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.grade
        return value/len(self.students)


# define 3 students
s1=Student("Tim", 19, 95)
s2=Student("Bill", 20, 90)
s3=Student("Jill", 18, 80)

# define a course
course = Course("science", 2)
course.add_student(s1)
course.add_student(s2)

# a list of object students
print(course.students[1].name)
print(course.get_average_grade())





    

        











