# 给你一个字符串 s，找到 s 中最长的回文子串。

# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。

# 示例 2：
# 输入：s = "cbbd"
# 输出："bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)

        # dp[i][j]: s[i..j]是否回文，i=0,1,...n-1
        dp=[[False for _ in range(n)] for _ in range(n)]

        # 初始化
        # 当子串长度为1时，d[i][i]总是回文
        for i in range(n):
            dp[i][i]=True
        
        maxLen=1
        begin=0
        # 遍历子串的所有可能长度
        for L in range(2,n+1):
            # 求解当前长度下的dp[左边界i：右边界j]
            for i in range(n):#i是左边界下标
                j=i+L-1# j是右边界下标

                if j>=n:# 右侧边界越界
                    break

                if s[i]!=s[j]:
                    dp[i][j]=False
                else:
                    if j-i<3:# <2也可以，此时就相当于判断一个长度为1的子串是否是回文，显然是
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]

                if dp[i][j] and L>maxLen:
                    maxLen=L
                    begin=i
        
        return s[begin:begin+maxLen]