# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

# 若这两个字符串没有公共子序列，则返回 0。

# 示例 1:

# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace"，它的长度为 3。

# 示例 2:
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc"，它的长度为 3。

# 示例 3:
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1,n2=len(text1), len(text2)
        
        # dp[i][j]: 只考虑text1[0...i-1]和text2[0...j-1]，能够获得的最长公共子序列的长度
        dp=[[0 for _ in range(n2+1)] for _ in range(n1+1)]

        # 初始化
        # 当有一个字符串长度为0时，dp值肯定是0
        for i in range(n1):# 第0列全是0
            dp[i][0]=0
        for i in range(n2):# 第0行全是0
            dp[0][i]=0
        
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                # 如果text1[i - 1] 与 text2[j - 1]相同，那么找到了一个公共元素
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                # 如果text1[i - 1] 与 text2[j - 1]不相同，那就看看text1[0...i - 2]与text2[0...j - 1]的
                # 最长公共子序列 和 text1[0...i - 1]与text2[0...j - 2]的最长公共子序列，取最大的。
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n1][n2]