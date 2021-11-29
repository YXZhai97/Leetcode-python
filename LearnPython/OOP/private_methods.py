class Women:
    def __init__(self,name):
        self.name=name
        #私有属性
        self.__age=18
    # 私有方法， 外部无法访问
    def __secret(self):
        print("my age is %d" % self.__age)

    # 内部方法可以访问私有方法
    def secret(self):
        self.__secret()

xiaofang=Women("xiaofang")
# print(xiaofang.age)
xiaofang.secret()
