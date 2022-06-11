# 判断一个字符串在任意位置(包括最前面和最后面)插入一个字符后能不能构成一个回文串。
# 输入为一个由字母和数字组成的字符串s，如果在插入一个字符之后可以构成回文串，则输出Yes, 否则输出No。（回文串:一个正读和反读都一样的字符串，如a, aba, abccba都是回文串）

# 输入描述:
# 输入一个字符串，例如"inkenike"

# 输出描述:
# 输出插入一个字符后给定字符串能不能构成一个回文串，如果能，输出Yes，否则输出No

# 输入例子1:
# abcdba

# 输出例子1:
# Yes

# 例子说明1:
# abcdba插入一个d可以构成回文串abdcdba，或者插入一个c可以构成回文串abcdcba

def judge(s):
    n=len(s)
    i,j=0,n-1
    while i<=j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def run(s):
    rec=set(s)
    n=len(s)
    for ch in rec:
        if judge(ch+s) or judge(s+ch):
            return True
        for i in range(0,n):
            if judge(s[:i]+ch+s[i:]):
                return True
    return False
# while True:
#     try:
#         s=input()
#         res=run(s)
#         if res:
#             print('Yes')
#         else:
#             print('No')
#     except:
#         break

# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# 9/11 组用例通过
# 运行时间
# 2001ms
# 占用内存
# 6644KB


# 正确的解法：双指针
def judge(s):
    n=len(s)
    i,j=0,n-1
    while i<=j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
def run(s):
    n=len(s)
    # 本身就是回文就直接返回True
    if n==1 or judge(s):
        return True
    i,j=0,n-1
    while i<j:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            # 在i左侧插入一个s[j]，或者在j右侧插入一个s[i]，并判断剩余部分是否是回文
            if judge(s[i:j]) or judge(s[i+1:j+1]):
                return  True
            else:
                return False
while True:
    try:
        s=input()
        res=run(s)
        if res:
            print('Yes')
        else:
            print('No')
    except:
        break