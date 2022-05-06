# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
# 例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

# 示例 1：

# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4

class Solution:
    def numSquares(self, n: int) -> int:
        #每一个物品可重复拿多次，因此这是一个完全背包问题
        
        #所有物品
        nums=[i**2 for i in range(1,n+1) if i**2<=n]

        m=len(nums)#物品数

        #背包容量是n

        weights=nums
        values=nums

        #dp[i]:装满容量为n的背包所需最少物品数
        dp=[n+1 for _ in range(n+1)]

        #初始化
        dp[0]=0#背包容量为0时，啥也不用装，所需最少物品数为0

        for i in range(m):#遍历物品
            for j in range(n+1):#遍历背包
                if j<weights[i]:#如果当前背包容量小于当前物品容量，只能不装
                    dp[j]=dp[j]
                else:#否则则可装可不装，选择所需物品数最少的
                    dp[j]=min(dp[j],dp[j-weights[i]]+1)
        return dp[n] if dp[n]!=n+1 else -1
