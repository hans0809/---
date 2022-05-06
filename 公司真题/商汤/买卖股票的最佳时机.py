# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)

        #dp[i][0]：第i天处于持有股票状态所获得的最大收益
        #dp[i][1]：第i天处于不持有股票状态能够获得的最大收益
        dp=[[0 for _ in range(2)] for _ in range(n)]

        # 初始化
        # 第0天，持有股票的收益就是-prices[0]
        dp[0][0]=-prices[0]
        # 第0天，不持有股票的最大收益是0
        dp[0][1]=0

        for i in range(1,n):
            # 计算第i天持有股票的最大收益: 有两种情况
            # 1. 第i-1天就持有股票：dp[i][0]=dp[i-1][0]
            # 2. 第i-1天不持有股票，第i天买入股票：dp[i][0]=-prices[i]，因为股票全程只能买卖一次
            dp[i][0]=max(dp[i-1][0],-prices[i])

            # 计算第i天不持有股票的最大收益: 有两种情况
            # 1. 第i-1天就不持有股票：dp[i][1]=dp[i-1][1]
            # 2. 第i-1天持有股票，在第i天卖出了：dp[i][1]=prices[i]+dp[i-1][0]
            dp[i][1]=max(dp[i-1][1],prices[i]+dp[i-1][0])
        return dp[n-1][1]