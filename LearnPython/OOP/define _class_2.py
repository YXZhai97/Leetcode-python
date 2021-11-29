class Gun:
    def __init__(self, model):
        # model of gun
        self.model=model
        self.bullet_count=0

    def add_bullet(self, count):
        self.bullet_count+=count

    def shoot(self):
        if self.bullet_count>0:
            self.bullet_count-=1
            print("%s shoot, remain bullet %d"%(self.model,self.bullet_count))
        else:
            print("%s has no bullet" %self.model)

class Soldier:
    def __init__(self, name):
        self.name=name
        # 一个对象的属性可以是另一个类
        self.gun=None

    def fire(self):
        # is 判断的是内存地址是否一致
        if self.gun is None:
            print("I have no gun")
            return

        else:
            print("go go go")
            self.gun.add_bullet(50)
            self.gun.shoot()




ak47=Gun("AK47")
xusanduo=Soldier("xusanduo")
xusanduo.gun=ak47
print(xusanduo.gun)
xusanduo.fire()
