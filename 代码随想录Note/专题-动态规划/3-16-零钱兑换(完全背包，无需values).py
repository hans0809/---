# 给定不同面额的硬币 coins 和一个总金额 amount。
# 编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 你可以认为每种硬币的数量是无限的。

# 题目中说每种硬币的数量是无限的，可以看出是典型的完全背包问题。

# 本题求钱币最小个数，那么钱币有顺序和没有顺序都可以，都不影响钱币的最小个数。
# 所以本题并不强调集合是组合还是排列。

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 背包容量为amount
        weights=coins#物品重量
        values=coins#物品价值, 本题用不到

        n=len(coins)# 物品数

        # dp[j]: 能够凑够金额j所需最少钱币数
        dp=[amount+1 for _ in range(amount+1)]

        # 初始化：需要凑成的金额为0时，只需0个钱币
        dp[0]=0
        # 由于接下来的递推公式是求min，因此其余位置全部初始化为很大的值，
        # 比如amount+1，因为要凑够金额amount所需钱币数肯定小于等于amount

        # 本题求得是装满背包所需最少的物品数，因此先遍历背包还是先遍历物品都可以
        for i in range(n):# 遍历物品，由于物品可以拿无限次
            for j in range(amount+1):# 遍历背包，由于每个物品可拿无限次，所以要正序遍历
                # 如果当前要凑的金额j小于硬币i的面值，只能不用硬币i
                if j<weights[i]:
                    dp[j]=dp[j]
                else:# 可以用也可以不用第i个硬币
                    dp[j]=min(dp[j],dp[j-weights[i]]+1)# 不用/用 第i个硬币 凑成金额j的钱币数，取最小的那个

        return dp[amount] if dp[amount]!=amount+1 else -1

# 二维dp
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 背包容量为amount
        weights=coins#物品重量
        values=coins#物品价值, 本题用不到

        n=len(coins)# 物品数

        # dp[i][j]: 前i-1个硬币已经搞定，只考虑用不用第i个硬币，能够凑够金额j所需最少钱币数
        dp=[[amount+1 for _ in range(amount+1)] for _ in range(n)]

        # 初始化：需要凑成的金额为0时，只需0个钱币
        for i in range(n):
            dp[i][0]=0
        # 由于接下来的递推公式是求min，因此其余位置全部初始化为很大的值，
        # 比如amount+1，因为要凑够金额amount所需钱币数肯定小于等于amount

        # 本题求得是装满背包所需最少的物品数，因此先遍历背包还是先遍历物品都可以
        for i in range(n):# 遍历物品，由于物品可以拿无限次
            for j in range(amount+1):# 遍历背包，由于每个物品可拿无限次，所以要正序遍历
                # 如果当前要凑的金额j小于硬币i的面值，只能不用硬币i
                if j<weights[i]:
                    dp[i][j]=dp[i-1][j]
                else:# 可以用也可以不用第i个硬币
                    dp[i][j]=min(dp[i-1][j],dp[i][j-weights[i]]+1)# 不用/用 第i个硬币 凑成金额j的钱币数，取最小的那个

        return dp[n-1][amount] if dp[n-1][amount]!=amount+1 else -1

# 二维dp: 物品下标从1开始
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 背包容量为amount
        weights=coins#物品重量
        values=coins#物品价值, 本题用不到

        n=len(coins)# 物品数

        # dp[i][j]: 前i-1个硬币已经搞定，只考虑用不用第i个硬币，能够凑够金额j所需最少钱币数
        dp=[[amount+1 for _ in range(amount+1)] for _ in range(n+1)]

        # 初始化：需要凑成的金额为0时，只需0个钱币
        for i in range(n+1):
            dp[i][0]=0
        # 由于接下来的递推公式是求min，因此其余位置全部初始化为很大的值，
        # 比如amount+1，因为要凑够金额amount所需钱币数肯定小于等于amount

        # 本题求得是装满背包所需最少的物品数，因此先遍历背包还是先遍历物品都可以
        for i in range(1,n+1):# 遍历物品，由于物品可以拿无限次
            for j in range(amount+1):# 遍历背包，由于每个物品可拿无限次，所以要正序遍历
                # 如果当前要凑的金额j小于硬币i的面值，只能不用硬币i
                if j<weights[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:# 可以用也可以不用第i个硬币
                    dp[i][j]=min(dp[i-1][j],dp[i][j-weights[i-1]]+1)# 不用/用 第i个硬币 凑成金额j的钱币数，取最小的那个

        return dp[n][amount] if dp[n][amount]!=amount+1 else -1