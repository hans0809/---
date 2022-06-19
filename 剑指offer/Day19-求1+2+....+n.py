# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

class Solution:
    def sumNums(self, n: int) -> int:
        def run(n):
            if n==1:
                return 1
            return n+run(n-1)
        return run(n)
# 利用短路效应，去掉if        
class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res