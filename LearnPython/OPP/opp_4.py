
class Math:
    @staticmethod #do some without change anything
    def add(a,b):
        return a+b

    @staticmethod
    def minus(a,b):
        return a-b

    @staticmethod
    def abs(a):
        if a>=0:
            return a
        else: return -a

#test something of the Module Math
#but this part will not be run when other file import Math
if __name__=="__main__":
    print(Math.add(2,3))
    print(Math.abs(-5))
    print(Math.minus(1,4))