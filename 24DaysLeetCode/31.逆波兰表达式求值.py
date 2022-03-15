class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            # 操作符
            if ch in '+-*/':
                a=stack.pop()
                b=stack.pop()
                if ch=='+':
                    res=b+a
                elif ch=='-':
                    res=b-a
                elif ch=='*':
                    res=b*a
                elif ch=='/':
                    res=int(b/a)# Python负数除法有点怪
                stack.append(res)
            # 操作数
            else:
                stack.append(int(ch))
                
        return stack.pop()
                