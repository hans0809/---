# 给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 的长度。

# 在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。


class Solution:
    def longestPalindrome(self, s: str) -> int:
        rec=dict()
        for ch in s:
            if ch not in rec:
                rec[ch]=1
            else:
                rec[ch]+=1
        res=0
        flag=False
        for ch,freq in rec.items():
            if freq%2==0:
                res+=freq
            else:
                res+=(freq-1)
                flag=True

        return res+1 if flag else res