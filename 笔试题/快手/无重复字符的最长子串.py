# 链接：https://www.nowcoder.com/questionTerminal/f8cc4c89060e4ce89b6f43076b770293
# 来源：牛客网

# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 输入描述:
# 输入字符串(长度<=100000)


# 输出描述:
# 不含有重复字符的最长子串长度
# 示例1
# 输入
# abcabcbb
# 输出
# 3
# 说明
# 因为无重复字符的最长子串是"abc"，所以其长度为 3。
# 示例2
# 输入
# bbbbb
# 输出
# 1
# 说明
# 因为无重复字符的最长子串是"b"，所以其长度为 1。

def run(s):
    n=len(s)
    #dp[i]:s[0...i]中最长不重复子串的长度,i=0,1,...,n-1
    dp=[1 for _ in range(n)]

    dp[0]=1

    for i in range(1,n):
        p=-1
        for j in range(i-1,i-dp[i-1]-1,-1):
            if s[j]==s[i]:
                p=j#与s[i]重复字符所在下标j
                break

        # 如果当前字符未出现过
        if p==-1:
            dp[i]=dp[i-1]+1
        # 如果当前字符出现过
        else:
            dp[i]=i-p
    
    return max(dp)

while True:
    try:
        s=input()
        res=run(s)
        print(res)
    except:
        break


# leetcode 打法：使用哈希表记录遍历过的字符最近一次出现位置所在下标
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
                # 产生重复的字符不在前dp[i-1]范围内，那么直接取dp[i-1]+1作为dp[i]即可
                if i-j>dp[i-1]:
                    dp[i]=dp[i-1]+1
                # 否则直接取dp[i]=i-j
                else:
                    dp[i]=i-j
                rec[s[i]]=i# 更新哈希表中最近的下标

        return max(dp)