# 给定一个字符串，求在其中包含的最长的有效括号子串(连续)
# 比如"()) ()(())()  ))(())"的最长有效括号子串的长度为8(为了观察，已用空格分开)

# dp[i]: 子串必须以i位置字符结尾时，最长的有效括号子串的长度是多少
# 遇到i位置为左括号，dp[i]直接填0
# 遇到i位置为左括号，需要求dp[i]

def maxLength(s):
    if not s:
        return 0
    
    s=list(s)
    n=len(s)
    dp=[0 for _ in range(n)]# dp[0]=0 ,一个字符肯定不匹配
    pre=0
    res=0
    for i in range(1,n):
        # 左括号直接默认为0，不再显式写出
        if s[i]==')':
            # 与s[i]配对的左括号的位置pre
            pre=i-dp[i-1]-1
            if pre>=0 and s[pre]=='(':
                dp[i]=dp[i-1]+2
                if pre>0:
                    dp[i]=dp[i]+dp[pre-1]
    return max(dp)
s="())()(())()))(())"
print('最大有效括号子串的长度为：',maxLength(s))