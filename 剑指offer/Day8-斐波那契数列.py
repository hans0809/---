# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        
        res=[0,1]
        for i in range(2,n+1):
            res.append(res[i-1]+res[i-2])
        
        return res[n]%1000000007


class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

