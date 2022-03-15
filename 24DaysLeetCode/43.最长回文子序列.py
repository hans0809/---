# 代码图解，为什么从后往前遍历的解释：https://leetcode-cn.com/problems/longest-palindromic-subsequence/solution/shu-ju-jie-gou-he-suan-fa-dong-tai-gui-h-e79i/
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        #dp[i][j]表示字符串中从i到j之间的最长回文子序列,i<j
        dp=[[0 for _ in range(n)] for _ in range(n)]
        # 必须从后往前遍历
        for i in range(n-1,-1,-1):
            dp[i][i]=1# 初始条件
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]          