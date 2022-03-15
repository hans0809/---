# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=[]
        # 大写->小写
        for ch in s:
            if ord('A')<=ord(ch)<=ord('Z'):
                ss.append(chr(ord(ch)+32))
            elif ord('a')<=ord(ch)<=ord('z'):
                ss.append(ch)
            elif ord('0')<=ord(ch)<=ord('9'):
                ss.append(ch)
        return ss==ss[::-1]