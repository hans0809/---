# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1=list(text1)
        text2=list(text2)

        n1=len(text1)
        n2=len(text2)

        if n1==0 or n2==0:
            return 0
        
        # dp[i][j]: text1[0...i-1]和text2[0...j-1]的最长公共子序列的长度
        dp=[[0 for _ in range(n2+1)] for _ in range(n1+1)]

        # 初始化
        for i in range(n1+1):
            dp[i][0]=0
        for j in range(n2+1):
            dp[0][j]=0
        
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    # 看看谁退一步得到的公共子序列的长度最大
                    # 以下两行代码都可以
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
                    #dp[i][j]=max(dp[i][j-1],dp[i-1][j], dp[i-1][j-1])

        return dp[n1][n2]