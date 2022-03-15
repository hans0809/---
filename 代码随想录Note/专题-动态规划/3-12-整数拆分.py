# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

# 返回 你可以获得的最大乘积 。

class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i]: 拆分i得到的最大乘积
        dp=[0 for _ in range(n+1)]
        # dp[0],dp[1]无法拆，直接忽略
        # 初始化
        dp[2]=1

        # 递推
        for i in range(3,n+1):#对于每一个待拆分的数字i
            #dp[i]可以由dp[i-j]*j 或者(i-j)*j
            for j in range(1,i-1):#这里写i-1，i，还是i+1都能AC
                dp[i]=max(dp[i],max(dp[i-j]*j,(i-j)*j))
                # 内部的max：把数字i从j拆开，可以拆成j*(i-j)或者j*dp[i-j]，前者就是不对i-j继续拆了，后者则相反，取两者种策略能够得到的最大乘积
                # 外部的max: 遍历每一个合法的j，取能够得到最大乘积的那个
        
        return dp[n]