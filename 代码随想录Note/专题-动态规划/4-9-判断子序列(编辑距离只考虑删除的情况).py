# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

# 动态规划五部曲分析如下：

# 确定dp数组（dp table）以及下标的含义
# dp[i][j] 表示以下标i-1为结尾的字符串s，和以下标j-1为结尾的字符串t，相同子序列的长度为dp[i][j]。

# 注意这里是判断s是否为t的子序列。即t的长度是大于等于s的。

# if (s[i - 1] == t[j - 1])，t中找到了一个字符在s中也出现了
# if (s[i - 1] != t[j - 1])，相当于t要删除元素，继续匹配

# if (s[i - 1] == t[j - 1])，那么dp[i][j] = dp[i - 1][j - 1] + 1;，
# 因为找到了一个相同的字符，相同子序列长度自然要在dp[i-1][j-1]的基础上加1

# if (s[i - 1] != t[j - 1])，此时相当于t要删除元素，
# t如果把当前元素t[j - 1]删除，那么dp[i][j] 的数值就是看s[i - 1]与 t[j - 2]的比较结果了，即：dp[i][j] = dp[i][j - 1];

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #dp[i][j]: s[0..i-1]和t[0...j-1]中相同子序列的长度
        # 最后如果dp[len(s)-1][len(t)-1]等于len(s)，那么就说明s是t的子序列
        slen,tlen=len(s),len(t)
        dp=[[0 for _ in range(tlen+1)] for _ in range(slen+1)]

        #初始化,t为空串时，dp[i][0]=0,第一列全0
        for i in range(slen):
            dp[slen][0]=0
        #s为空串时，dp[0][i]=0,第一行全0
        for i in range(tlen):
            dp[0][i]=0
        
        for i in range(1,slen+1):
            for j in range(1,tlen+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=dp[i][j-1]
        return dp[slen][tlen]==slen