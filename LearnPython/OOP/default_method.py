import math


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coods = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    # when we want to print the object this method will be called
    # the dtr method must return a string
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):
        return self.length() <= p.length()

    def __eq__(self, p):
        return self.length() == p.length()

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)
p4.move(1, 1)
print(p4.coods)
print(p1==p2)
print(p1>p2)

p5 = p1 + p2
p6 = p4 - p2
p7 = p1 * p2
print(p5, p6, p7)
