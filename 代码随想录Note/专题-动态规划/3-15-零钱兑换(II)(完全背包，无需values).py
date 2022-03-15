# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。

# 一看到钱币数量不限，就知道这是一个完全背包。

# 如果求组合数就是外层for循环遍历物品，内层for遍历背包。
# 如果求排列数就是外层for遍历背包，内层for循环遍历物品。
# 本题求的是组合数

# 一维dp
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 在完全背包中，先遍历物品还是先遍历背包得到的结果是一样的
        # 但是本题求的是不同组合数有多少，不是排列数有多少！必须先遍历物体，再遍历背包 (i.e. 1,2 和 2,1 是不同的排列，相同的组合)

        weights=coins# 物品容量
        values=coins# 本题和目标和一样，求得是恰好凑成背包容量的不同方案数，用不到values
        # 背包容量就是amount

        n=len(coins)# 物品数

        # dp[j]:凑成金额j共有dp[j]方案
        dp=[0 for _ in range(amount+1)]

        # 初始化：凑成总金额0的货币组合数为1
        dp[0]=1

        for i in range(n):# 遍历物品
            for j in range(amount+1):# 遍历背包，由于每个物品可拿无限次，所以要正序遍历
                # 如果背包容量小于第i个物品的重量，只能是选择不拿物品i,此时要凑成金额j，共有dp[j]种方案
                if j <weights[i]:
                    dp[j]=dp[j]
                else:
                    # 可拿可不拿第i个物品
                    dp[j]=dp[j]+dp[j-weights[i]]#不拿/拿第i件物品时，凑成金额j的不同方案数。求装满背包有几种方法类似的题目，递推公式基本都是这样的。
        return dp[amount]

# 二维dp
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 求不同组合数有多少，不是排列数有多少！

        weights=coins# 物品容量
        values=coins# 本题和目标和一样，求得是恰好凑成背包容量的不同方案数，用不到values
        # 背包容量就是amount

        n=len(coins)# 物品数

        # dp[i][j]:在前i-1个硬币已经搞定的前提下，只考虑拿不拿(用不用)第i件物品(硬币)，凑成金额j共有dp[i][j]种组合方案
        dp=[[0 for _ in range(amount+1)] for _ in range(n)]

        # 初始化：凑成总金额0的货币组合数为1
        for i in range(n):
            dp[i][0]=1

        for i in range(n):# 遍历物品
            for j in range(amount+1):# 遍历背包，由于每个物品可拿无限次，所以要正序遍历
                # 如果背包容量小于第i个物品的重量，只能是选择不拿物品i时的dp[j]
                if j <weights[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    # 可拿可不拿第i个物品
                    dp[i][j]=dp[i-1][j]+dp[i][j-weights[i]]#不拿/拿第i件物品时，凑成j的不同方案数是dp[j]
        return dp[n-1][amount]

# 二维dp：物品下标从1开始
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 求不同组合数有多少，不是排列数有多少！

        weights=coins# 物品容量
        values=coins# 本题和目标和一样，求得是恰好凑成背包容量的不同方案数，用不到values
        # 背包容量就是amount

        n=len(coins)# 物品数

        # dp[i][j]:在前i-1个硬币已经搞定的前提下，只考虑拿不拿(用不用)第i件物品(硬币)，凑成金额j共有dp[i][j]种组合方案
        dp=[[0 for _ in range(amount+1)] for _ in range(n+1)]

        # 初始化：凑成总金额0的货币组合数为1，这也包括没有可选物品时，因此要从0开始
        for i in range(0,n+1):
            dp[i][0]=1
        

        for i in range(1,n+1):# 遍历物品
            for j in range(amount+1):# 遍历背包，由于每个物品可拿无限次，所以要正序遍历
                # 如果背包容量小于第i个物品的重量，只能是选择不拿物品i时的dp[j]
                if j <weights[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    # 可拿可不拿第i个物品
                    dp[i][j]=dp[i-1][j]+dp[i][j-weights[i-1]]#不拿/拿第i件物品时，凑成j的不同方案数。求装满背包有几种方法类似的题目，递推公式基本都是这样的。
        return dp[n][amount]