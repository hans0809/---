# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
# 一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

class Solution:
    def translateNum(self, num: int) -> int:
        if num==0:
            return 1

        s=list(str(num))
        n=len(s)

        if n==1:
            return 1

        #dp[i]：nums[0...i]的不同翻译方法总数
        dp=[0 for _ in range(n)]# 初始化成0或1都可以

        dp[0]=1
        if s[0]+s[1]<='25':
            dp[1]=2
        else:
            dp[1]=1
        
        for i in range(2,n):
            if '10'<=s[i-1]+s[i]<='25':
                dp[i]=dp[i-2]+dp[i-1]
            else:
                dp[i]=dp[i-1]
        
        return dp[n-1]