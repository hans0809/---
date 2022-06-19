# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。

# 快速幂+递归
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def run(x,n):
            if n==0:
                return 1
            y=run(x,n//2)
            if n%2==0:
                return y*y
            else:
                return y*y*x
        if n>=0:
            return run(x,n)
        else:
            return 1/run(x,-n)