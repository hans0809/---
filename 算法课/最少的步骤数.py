# 题目：假设s和m初始化为：s="a", m=s
# 再定义两种操作：
# 1)m=s;s=s+s
# 2)s=s+m
# 求最少的操作步骤数，可以将s拼接到长度等于N

# 解题：
# 情况(1): N是质数，此时只需调用N-1次操作2
# 情况(2): N不是质数，那么可以拆成某些质数的乘积，假设最好的结合顺序是N=x*y*z*p，p是质数，那么就想办法搞出x*y*z*p，
# 意思是需要搞出p份x*y*z，由于p是质数，所以只需调用p-1次操作2；那么接下来就只需考虑如何搞出x*y*z，z是质数，
# 意思是需要搞出z份x*y，由于z是质数，所以只需调z-1次操作2，那么接下来只需考虑如何搞出x*y, 且y是质数
# 意思是需要搞出y份x，由于y是质数，所以只需调y-1次操作2，
# 最后剩1个x也是质数，只需调x-1次操作2
# 所以总共调用次数为：p-1+z-1+y-1+x-1=x+y+z+p-4

def isPrime(num):
    if num<2:
        return False
    import math
    max_num=int(math.sqrt(num))
    for i in range(2,max_num+1):
        if num%i==0:
            return False
    return True

# 保证n不是质数
# 返回1)所有因子的和，2)所有因子的个数，这里的因子不包括1
def divsSumAndCount(num):
    summ=0
    count=0
    for i in range(2,num+1):
        while num %i==0:
            summ+=i
            count+=1
            num/=i
    return summ,count

def minOps(num):
    if num<2:
        return 0
    if isPrime(num):
        return num-1
    # n不是质数
    summ,count=divsSumAndCount(num)
    return summ-count
n=8
print(minOps(n))
        
    



