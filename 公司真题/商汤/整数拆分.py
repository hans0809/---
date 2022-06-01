# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
# 返回 你可以获得的最大乘积 。

class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i]:拆分数字i能够得到的最大乘积
        dp=[0 for _ in range(n+1)]

        #初始化
        #0和1无法拆分，无意义，忽略
        dp[2]=1

        for i in range(3,n+1):
            # 计算每一个dp[i]
            for j in range(1,i):
                # 将i拆分成j和i-j，对应的乘积有两种情况：
                # 1. 不对i-j继续拆分，此时最大乘积等于(i-j)*j
                # 2. 继续拆分i-j， 此时最大乘积等于dp[i-j]*j 
                cur_max_product=max((i-j)*j, dp[i-j]*j)
                dp[i]=max(dp[i], cur_max_product)
                
        return dp[n]
