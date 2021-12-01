from math import sqrt

# todo python abstractmethod
class Person(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self.__name

    # 访问器 - getter方法
    @property
    def age(self):
        return self.__age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self.__age = age

    @name.setter
    def name(self, name):
        self.__name=name

    def play(self):
        if self.__age <= 16:
            print('%s正在玩飞行棋.' % self.__name)
        else:
            print('%s正在玩斗地主.' % self.__name)


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main1():
    a, b, c = 4, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')




def main2():
    person = Person('王大锤', 12)

    print(person.age)
    print(person.name)
    person.play()
    person.age = 24
    person.name='Eason'
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main1()
    main2()