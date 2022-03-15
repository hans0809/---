class Solution:
    def calculate(self, s: str) -> int:
        n=len(s)
        stack=[]
        preSign='+'
        num=0
        for i in range(n):
            if s[i] !=' ' and s[i].isdigit():
                num=num*10+int(s[i])#处理13+5*2中的13这种情况
            if i==n-1 or s[i] in '+-*/':
                if preSign=='+':
                    stack.append(num)
                elif preSign=='-':
                    stack.append(-num)
                elif preSign=='*':
                    stack.append(stack.pop()*num)
                elif preSign=='/':
                    stack.append(int(stack.pop()/num))
                preSign=s[i]
                num=0# 此时i指向运算符，下一次就要新开一个数字了，所以num重新设置为0
        return sum(stack)