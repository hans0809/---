# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
# 例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

# 示例 1：

# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4


# 一维dp
class Solution:
    def numSquares(self, n: int) -> int:
        # 先求小于等于n的完全平方数，存入nums，这就是所有可选物品
        nums=[i**2 for i in range(1,n+1) if i**2<=n]

        m=len(nums)# 物品数

        weights=nums# 物品重量
        values=nums# 物品价值
        # 背包最大容量是n

        # 问题转化为：求恰好装满背包所需最少物品数
        # 由示例1可以看到，每一个物品可重复拿多次，因此这是一个完全背包问题

        #dp[i]：装满容量为j的背包所需最少物品数
        dp=[n+1 for _ in range(n+1)]

        # 初始化：n=0时，不需要任何物品就能装满容量为0的背包
        dp[0]=0
        # 由于递推式求的是min，因此其余位置应该初始化为1个比较大的数，比如n+1
        # 因为装满容量为n的版本最多需要的物品数是n，一定小于n+1

        for i in range(m):#遍历物品
            for j in range(n+1):# 遍历背包
                if j<weights[i]:
                    dp[j]=dp[j]
                else:
                    dp[j]=min(dp[j],dp[j-weights[i]]+1)
        return dp[n] if dp[n]!=n+1 else -1

# 二维dp：略

# 本题和零钱兑换一样