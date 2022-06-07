# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n=len(prices)
        #dp[i][0]：第i天处于买入状态时能够获得的利润
        #dp[i][1]：第i天处于卖出状态时能够获得的利润
        dp=[[0,0] for _ in range(n)]

        # 初始化
        dp[0][0]=-prices[0]
        dp[0][1]=0

        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i])
        return dp[n-1][1]