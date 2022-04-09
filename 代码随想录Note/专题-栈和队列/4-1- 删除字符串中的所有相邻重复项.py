# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

# 在 S 上反复执行重复项删除操作，直到无法继续删除。

# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。


class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return s
        s=list(s)
        stack=[]
        stack.append(s[0])

        for ch in s[1:]:
            if stack:
                cur=stack[-1]
                if cur==ch:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        if not stack:
            return ''
        else:
            return ''.join(stack)

# 精简下
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return s
        s=list(s)
        stack=[]
        stack.append(s[0])

        for ch in s[1:]:
            if stack and stack[-1]==ch:
                stack.pop()
            else:
                stack.append(ch)

        if not stack:
            return ''
        else:
            return ''.join(stack)
            