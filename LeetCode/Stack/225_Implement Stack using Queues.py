# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 20:49:27 2021

@author: yixing
"""

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que=[]

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.que.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.que.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.que[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.que)==0:
            return True 
        else:
            return False 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()