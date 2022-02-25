class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ss=[i for i in s]
        for s in ss:
            if s in '({[':
                stack.append(s)
            else:# s in ')}]'
                if not stack:
                    return False
                match=stack[-1]
                if match=='(' and s==')' or match=='{' and s=='}' or match=='[' and s==']':
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False
            
            