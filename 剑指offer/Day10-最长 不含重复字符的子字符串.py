# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        s=list(s)
        n=len(s)

        rec=dict()

        #dp[i]：s[0...i]中最长的不包含重复字符的子字符串的长度
        dp=[1 for _ in range(n)]

        dp[0]=1
        rec[s[0]]=0

        for i in range(1,n):
            # 如果s[i]是新出现的，那么直接dp[i]=dp[i-1]+1
            if s[i] not in rec:
                dp[i]=dp[i-1]+1
                rec[s[i]]=i
            # 此时s[i]已经出现过了
            else:
                # 获取距离i最近的s[i]出现的下标j
                j=rec[s[i]]
                if i-j>dp[i-1]:
                    dp[i]=dp[i-1]+1
                else:
                    dp[i]=i-j
                rec[s[i]]=i# 更新哈希表中最近的下标

        return max(dp)