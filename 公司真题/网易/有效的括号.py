# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if ch==')' and stack[-1]=='(' or ch=='}' and stack[-1]=='{' or ch==']' and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True