# 给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
# 每步 可以删除任意一个字符串中的一个字符。

# 示例：

# 输入: "sea", "eat"
# 输出: 2 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

# 确定dp数组（dp table）以及下标的含义
# dp[i][j]：以i-1为结尾的字符串word1，和以j-1为结尾的字符串word2，想要达到相等，所需要删除元素的最少次数。

# 这里dp数组的定义有点点绕，大家要撸清思路。

# 本题和动态规划：不同的子序列 相比，其实就是两个字符串都可以删除了，情况虽说复杂一些，但整体思路是不变的。

# 这次是两个字符串可以相互删了，这种题目也知道用动态规划的思路来解，动规五部曲，分析如下:

# 确定递推公式
# 当word1[i - 1] 与 word2[j - 1]相同的时候
# 当word1[i - 1] 与 word2[j - 1]不相同的时候

# 当word1[i - 1] 与 word2[j - 1]相同的时候，dp[i][j] = dp[i - 1][j - 1];

# 当word1[i - 1] 与 word2[j - 1]不相同的时候，有三种情况：

# 情况一：删word1[i - 1]，最少操作次数为dp[i - 1][j] + 1

# 情况二：删word2[j - 1]，最少操作次数为dp[i][j - 1] + 1

# 情况三：同时删word1[i - 1]和word2[j - 1]，操作的最少次数为dp[i - 1][j - 1] + 2

# 那最后当然是取最小值，所以当word1[i - 1] 与 word2[j - 1]不相同的时候，递推公式：dp[i][j] = min({dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1, dp[i][j - 1] + 1});

# dp数组如何初始化
# 从递推公式中，可以看出来，dp[i][0] 和 dp[0][j]是一定要初始化的。

# dp[i][0]：word2为空字符串，以i-1为结尾的字符串word1要删除多少个元素，才能和word2相同呢，很明显dp[i][0] = i。

# dp[0][j]的话同理

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1,len2=len(word1),len(word2)
        #dp[i][j]:word1[0...i-1]和word2[0...j-1]中，想要达到相等，所需要的最少删除次数
        dp=[[0 for _ in range(len2+1)] for _ in range(len1+1)]

        # 初始化
        for i in range(len1+1):
            dp[i][0]=i
        for j in range(len2+1):
            dp[0][j]=j
        
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+2)
        return dp[len1][len2]