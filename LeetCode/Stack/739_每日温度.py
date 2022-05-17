class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        T = temperatures
        stack = []
        res = [0] * len(T)
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                small = stack.pop()
                res[small] = i - small
            stack.append(i)

        return res