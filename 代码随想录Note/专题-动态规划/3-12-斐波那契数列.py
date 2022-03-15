# 动规五部曲：
# 1. 确定dp数组以及下标的含义
# 2. 确定递推公式
# 3. dp数组如何初始化
# 4. 确定遍历顺序
# 5. 举例推导dp数组，如果代码写出来，发现结果不对，就把dp数组打印出来看看和我们推导的结果是不是一致的。

class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        #1.dp数组的含义： dp[i]#  F(i)
        dp=[0 for _ in range(n+1)]
        # dp数组初始化
        dp[0]=0
        dp[1]=1
        # 3.确定遍历顺序以及开始遍历
        # 由于dp[i]=dp[i-1]+dp[i-2]，因此一定是从前往后遍历的
        for i in range(2, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
