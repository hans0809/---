# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '
        rec=dict()
        for ch in s:
            if ch not in rec:
                rec[ch]=1
            else:
                rec[ch]+=1
        for ch in s:
            if ch in rec and rec[ch]==1:
                return ch
        return ' '