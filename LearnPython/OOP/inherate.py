"""
继承和多态
"""
class Animal:

    def __init__(self):
        self.weight=10
        self.high=10

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animal):
    def bark(self):
        print("bark")

class XiaoTianQuan(Dog):
    def fly(self):
        print("fly")

wangcai=Dog()
wangcai.run()
wangcai.bark()
print(wangcai.weight)
xtq=XiaoTianQuan()
xtq.sleep()
