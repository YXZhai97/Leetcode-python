class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # 设置栈用来存储数组
        plus = '+'  # 设首个符号为+号，方便首次将第一个数压入栈
        num = 0  # 设初始值为0
        for i, j in enumerate(s):
            if j.isdigit():  # 判断是否为数字，如果是位置，则将值赋给num
                num = num * 10 + int(j)  # 这句的原因主要在于有的测试用例是两个数中间没有符号的，比如“42”这样的
            if i == len(s) - 1 or j in '+-*/':  # 如果到最后一个数了，或者j为符号，需要进行以下比较
                if plus == '+':  # 如果为 ‘+’ 直接压入栈
                    stack.append(num)
                elif plus == '-':  # 如果为‘-’ 则将num变为-num再压入栈
                    stack.append(-num)
                elif plus == '*':  # 如果为‘*’，则弹出栈顶的值与num相乘
                    stack.append(stack.pop() * num)
                elif plus == '/':  # 如果为‘/’,则弹出栈顶的值，判断top是否小于0，如果小于0，则进行/  否则//
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                plus = j  # 这次的符号赋给plus
                num = 0  # num重新置0
        return sum(stack)  # 对stack求和
