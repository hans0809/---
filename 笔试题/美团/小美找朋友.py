#   小美将自己朋友的名字写在了一块，惊讶地发现她写出的那个字符串S有一个惊人的性质：一个人是小美的朋友当且仅当她/他的名字是那个字符串的子序列。现在小团想根据那个字符串判断一个人是不是小美的朋友。

#        *子序列：一个字符串A是另外一个字符串B的子序列，当且仅当可以通过在B中删除若干个字符（也可能一个都不删），其他字符保留原来顺序，使得形成的新字符串B’与A串相等。例如，ABC是AABDDC的子序列，而ACB不是AABDDC的子序列。


# 输入描述:
# 第一行两个正整数n，m分别表示小美朋友字符串S的长度，以及小团想了解是不是小美朋友的那个人的名字字符串T的长度。

# 第二行长度为n且仅包含小写字母的字符串S

# 第三行长度为m且仅包含小写字母的字符串T


# 输出描述:
# 如果小团想了解的那个人不是小美的朋友(即，T不是S的子序列)，输出一行”No”,否则输出一行”Yes”，并在第二行将T对应到S中的位置之和输出出来(从1开始编号)，由于可能有多种对应方式，请输出最小的位置之和。请参见样例解释获取更详细说明


# 输入例子1:
# 6 3
# aabddc
# abc

# 输出例子1:
# Yes
# 10

# 例子说明1:
# 对于样例1

# S=aabddc T=abc，T中a可以与S中第1个字符a对应起来，b可以与S中第3个字符b对应起来，c可以与S中第6个字符c对应起来，这样一来就找到了一个S中的子序列(仅保留第1、3、6个字符形成的子序列)，使其与T相等。这种情况下，位置之和为1+3+6=10

# 还有一种方案，是S仅保留第2、3、6个字符形成的子序列abc,仍然满足与T相等的条件。但是位置之和为2+3+6=11，并不是位置之和最小的，因而输出第一种对应方案的位置之和：10


# 输入例子2:
# 6 3
# aabddc
# acb

# 输出例子2:
# No

# 例子说明2:
# 对于样例2

# 可以保留S中的第1、3、6个字符，形成子序列abc，但于T串acb不相等，因为b、c位置并不对应。可以证明，没有任何一种取S子序列的方式，可以使得取出的子序列和T相等，因而输出No

# 最终AC 的代码
def judge_is_friend(s,t):
    ns,nt=len(s),len(t)

    def judge_one_time(start,s,t):
        k=0
        sum_=0
        while start < ns:
            if s[start] ==t[k]:
                sum_+=(start+1)
                k+=1
            start += 1

        if k==nt:
            return True, sum_
        return False,sum_
    res, sum_=judge_one_time(0,s,t)
    if res:
        return True, sum_
    else:
        return False, sum_

n,m=map(int,input().split(' '))
s=input()
t=input()
res,min_sum_=judge_is_friend(s,t)
if res:
    print('Yes')
    print(min_sum_)
else:
    print('No')


# 我一开始好像想复杂了。。。以下代码仅仅通过3个测试用例
def judge_is_friend(s,t):
    ns,nt=len(s),len(t)

    def judge_one_time(start,s,t):
        k=0
        sum_=0
        while start < ns:
            if s[start] ==t[k]:
                sum_+=(start+1)
                k+=1
            start += 1

        if k==nt:
            return True, sum_
        return False,sum_
    
    min_sum_=99999
    res=False
    for start in range(0,ns):
        judge_res,sum_=judge_one_time(start,s,t)
        # print(judge_res,sum_)
        if judge_res:
            min_sum_=min(min_sum_,sum_)
            res=True
            # print('Yes')
    if res:
        return True, min_sum_
    else:
        return False, min_sum_

n,m=map(int,input().split(' '))
s=input()
t=input()
res,min_sum_=judge_is_friend(s,t)
if res:
    print('Yes')
    print(min_sum_)
else:
    print('No')