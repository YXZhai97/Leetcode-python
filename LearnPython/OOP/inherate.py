"""
继承和多态
"""
class Animal:

    def __init__(self):
        self.weight=10
        self.high=10
        self.__secret="secret"

    def eat(self):
        print("eat")
        print(self.__secret)

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animal):
    def bark(self):
        print("dog bark")

    def game(self):
        print("game with itself")

class XiaoTianQuan(Dog):
    count=0
    def __init__(self):
        super().__init__()
        XiaoTianQuan.count+=1



    def fly(self):
        print("fly")

    def bark(self):
        # 针对子类特有需求编写代码
        print("xtq bark")
        # 使用super().
        super().bark()
        # 增加其他子类代码
        print("abcdf")

 




wangcai=Dog()
wangcai.run()
wangcai.bark()
wangcai.eat()
print(wangcai.weight)
xtq=XiaoTianQuan()
xtq.sleep()
xtq.bark()
print(XiaoTianQuan.__mro__)
xxx=XiaoTianQuan()
print(XiaoTianQuan.count)
print(xxx.weight)

