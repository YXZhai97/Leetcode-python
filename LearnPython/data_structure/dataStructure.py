class Stack:
    """
    栈
    define stack data structure with python built-in list
    """
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self, item):
        # 在list首插入
        self.items.insert(0, item)


    def dequeue(self):
        #在list的尾部出队列
        self.items.pop()

    def size(self):
        return len(self.items)

class Deque():
    """
    双端队列: 两端都可以添加和删除
    [队尾， 队首]
    """
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class UnorderedList:

    def __init__(self):
        self.head=None #head 是对首个Node的引用


class MyTree:



class Pqueue:

