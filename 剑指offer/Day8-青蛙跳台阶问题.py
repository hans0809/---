# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

class Solution:
    def numWays(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 1

        #dp[i]: 青蛙跳到第i个台阶总共的跳法数量
        dp=[0 for _ in range(n+1)]

        # 初始化
        dp[0]=1# 初始位于第0个台阶，即不在台阶上，可以看做是跳到第0个台阶有1种跳法，那就是不跳。。。
        dp[1]=1# 跳到第一个台阶，只有一种跳法，那就是跳1步

        for i in range(2,n+1):
            # 可以从前一个台阶跳1步，或者从前两个台阶处跳两步
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n]%1000000007

class Solution:
    def numWays(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 1

        #dp[i]: 青蛙跳到第i个台阶总共的跳法数量
        dp=[0 for _ in range(n+1)]

        # 初始化
        dp[0]=0# 初始位于第0个台阶，即不在台阶上，不考虑
        dp[1]=1# 跳到第一个台阶，只有一种跳法，那就是跳1步
        dp[2]=2#跳到第一个台阶，有2种跳法，那就是跳两个1步，或者1个2步

        for i in range(3,n+1):
            # 可以从前一个台阶跳1步，或者从前两个台阶处跳两步
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n]%1000000007