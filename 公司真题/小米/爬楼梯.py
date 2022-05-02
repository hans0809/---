# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return n
        #dp[i]:爬到第i阶不同的方法数
        dp=[0 for _ in range(n+1)]

        # 初始化
        dp[1]=1
        dp[2]=2

        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n]