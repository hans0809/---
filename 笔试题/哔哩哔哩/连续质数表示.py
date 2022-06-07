# 一些正数能被表示成一个或者多个连续质数的和。那一个数会有多少种这样的表示方式呢？
# 比如说数字41能有3种表示方式：2+3+5+7+11+13，11+13+17，和41；数字3只有本身这一种表示方式；而20没有这样的表示方式。
# 写一个程序生成给定数字的表示方式数量吧。数字大小范围从2到10，000。


# 输入描述:
# 一行，包含一个2到10000的正整数


# 输出描述:
# 一行, 非负整数, 给定数字的表示方式数量

# 输入例子1:
# 41

# 输出例子1:
# 3


def is_prime(n):
    """判断数字n是否为质数"""
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def get_prime(n):
    """获取2到n之间(左右都是闭区间)的所有质数"""
    primes=[]
    for i in range(2,n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def run(n):
    ans=0
    primes=get_prime(n)
    # print(primes)

    for i in range(0,len(primes)):
        sum_=0
        res=[]
        tmp=[]
        for j in range(i,len(primes)):
            sum_+=primes[j]
            tmp.append(primes[j])
            if sum_==n:
                ans+=1
                res.append(tmp)
            elif sum_>n:
                break

    return ans

while True:
    try:
        n=int(input())
        res=run(n)
        print(res)
    except:
        break