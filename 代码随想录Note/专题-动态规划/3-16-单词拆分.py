# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

# 说明：

# 拆分时可以重复使用字典中的单词。

# 你可以假设字典中没有重复的单词。

# 示例 1： 输入: s = "leetcode", wordDict = ["leet", "code"] 输出: true 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

# 示例 2： 输入: s = "applepenapple", wordDict = ["apple", "pen"] 输出: true 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。   注意你可以重复使用字典中的单词。

# 示例 3： 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"] 输出: false


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 完全背包问题，背包容量为len(s)，wordDict中的每个单词都是一件物品
        
        n=len(wordDict)# 物品个数，本题用不到
        w=len(s)# 背包容量

        # dp[i] : 字符串长度为i的话，dp[i]为true，表示可以拆分为一个或多个在字典中出现的单词。
        dp=[False for _ in range(w+1)]

        # 初始化：字符串长度为0，即空字符串是可以由wordDict中的单词组成(只需空单词就好了)，当然题目说了非空字符串，因此这里只是为了初始化便于后序的推导
        dp[0]=True

        for i in range(1, w+1):# 遍历背包(字符串s),
            for j in range(0,i):# 遍历物品(单词)
                sub=s[j:i]
                if sub in wordDict and dp[j]:#对于字符串s，下标j之前的字符串可以拆分为一个或多个在字典中出现的单词 (dp[j]=True)，
                                             #并且从j开始到i-1（j<i）这一段组成的子串是一个出现在wordDict中的单词，
                                            # 那么下标i之前的字符串也可以拆分为一个或多个在字典中出现的单词（dp[i]也是True）
                    dp[i]=True
        return dp[w]

# 这题没太懂