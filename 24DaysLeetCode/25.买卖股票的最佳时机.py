# 题目1
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i][0]: 第i天交易完成后手里没有股票的最大利润
        #dp[i][1]: 第i天交易完成后手里持有一支股票的最大利润
        n=len(prices)
        dp=[[0 for _ in range(2)] for _ in range(n)]#nx2
        dp[0][0]=0# 第一天交易完成后手里没有股票的最大利润是0
        dp[0][1]=-prices[0]# 第一天交易完成后手里没持有股票的最大利润是-prices[0]
        
        for i in range(1,n):
            # 前一天手里持有股票or前一天手里没有股票，取利润最大的
            dp[i][0]=max(dp[i-1][1]+prices[i],dp[i-1][0])
            # 前一天手里持有股票or前一天手里没有股票，取利润最大的
            dp[i][1]=max(dp[i-1][1],-prices[i])
        return dp[n-1][0]

# 题目2
# 给定一个数组 prices ，其中 prices[i] 表示股票第 i 天的价格。
# 在每一天，你可能会决定购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以购买它，然后在 同一天 出售。
# 返回 你能获得的 最大 利润 。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i][0]: 第i天交易完成后手里没有股票的最大利润
        #dp[i][1]: 第i天交易完成后手里持有一支股票的最大利润
        n=len(prices)
        dp=[[0 for _ in range(2)] for _ in range(n)]#nx2
        dp[0][0]=0# 第一天交易完成后手里没有股票的最大利润是0
        dp[0][1]=-prices[0]# 第一天交易完成后手里没持有股票的最大利润是-prices[0]
        
        for i in range(1,n):
            # 前一天手里持有股票or前一天手里没有股票，取利润最大的
            dp[i][0]=max(dp[i-1][1]+prices[i],dp[i-1][0])
            # 前一天手里持有股票or前一天手里没有股票，取利润最大的
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[n-1][0]


# 题目1更简单的写法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=100000000000# 最低价格
        max_profit=0#最大利润
        for price in prices:
            max_profit=max(max_profit,price-min_price)
            min_price=min(min_price,price)
        return max_profit