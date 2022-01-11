# 题目1：假设有排成一行的N个位置，记为1~N，N一定大于或等于2
# 开始时机器人在其中的M位置上(M一定是1~N中的某一个)
# 如果机器人来到1位置，那么下一步只能来到2位置
# 如果机器人来到N位置，那么下一步只能来到N-1位置
# 如果在其它位置，则下一步可以往左走或者往右走
# 规定机器人必须走K步，最终能来到P位置(P也是1~N中的一个)的方法总共有几种？
# 给定4个参数N,M,K,P，返回方法数

# 暴力递归
def ways1(N,M,K,P):
    # 参数无效直接返回0
    if N<2 or K<1 or M<1 or M>N or P<1 or P>N:
        return 0
    
    return walk1(N,M,K,P)
def walk1(N,cur,rest,P):
    """
    N:位置为1~N，固定参数
    cur:当前在cur位置，可变参数
    rest:还剩rest步没走，可变参数
    P:目标位置，固定参数
    """
    if rest==0:
        return 1 if cur==P else 0
    # 来到边界
    if cur==1:
        return walk1(N,2,rest-1,P)
    if cur==N:
        return walk1(N,N-1,rest-1,P)
    # 没来到边界，可以向左走，也可以向右走
    return walk1(N,cur-1,rest-1,P)+walk1(N,cur+1,rest-1,P)
N,M,K,P=5,2,6,4
print(ways1(N,M,K,P))
    


# 加数组作为缓存(记忆化搜索)
def ways2(N,M,K,P):
    # 参数无效直接返回0
    if N<2 or K<1 or M<1 or M>N or P<1 or P>N:
        return 0

    #把所有(cur,rest)加入缓存
    #dp=[[-1]*(K+1) for _ in range(N+1)]
    dp=[[-1 for _ in range(K+1)] for _ in range(N+1)]
    # 上面两种写法都可以，但是写成dp=[[-1]*(K+1)]*(N+1)就不对，为什么？

    def walk2(N,cur,rest,P):
        if dp[cur][rest]!=-1:
            return dp[cur][rest]

        ans=0
        if rest==0:
            ans=1 if cur==P else 0

        elif cur==1:
            ans=walk2(N,2,rest-1,P)
   
        elif cur==N:
            ans=walk2(N,N-1,rest-1,P)
 
        else:
            ans=walk2(N,cur-1,rest-1,P)+walk2(N,cur+1,rest-1,P)

        dp[cur][rest]=ans
        return ans
    res=walk2(N,M,K,P)
    return res
N,M,K,P=5,2,6,4
print(ways2(N,M,K,P))


# 加哈希表作为缓存(记忆化搜索)
def ways3(N,M,K,P):
    # 参数无效直接返回0
    if N<2 or K<1 or M<1 or M>N or P<1 or P>N:
        return 0
    dic=dict()
    return walk3(N, M,K,P,dic)
def walk3(N,cur,rest,P,dic):
    """
    N:位置为1~N，固定参数
    cur:当前在cur位置，可变参数
    res:还剩rest步没走，可变参数
    P:目标位置，固定参数
    """

    # 已经在缓存中，直接返回
    if (cur,rest) in dic:
        return dic[(cur,rest)]

    #不在缓存中，就先计算出来，然后加入缓存
    if rest==0:
        dic[(cur,rest)]=1 if cur==P else 0
        return dic[(cur,rest)]
    # 来到边界
    if cur==1:
        dic[(cur,rest)] = walk3(N,2,rest-1,P,dic)
        return dic[(cur,rest)]
    if cur==N:
        dic[(cur,rest)] = walk3(N,N-1,rest-1,P,dic)
        return dic[(cur,rest)]
    # 没来到边界，可以向左走，也可以向右走
    dic[(cur,rest)] = walk3(N,cur-1,rest-1,P,dic)+walk3(N,cur+1,rest-1,P,dic)
    return dic[(cur,rest)]
N,M,K,P=5,2,6,4
print(ways3(N,M,K,P))

# 动态规划
"""
N=7
M=2
K=5
P=3
    rest  0     1    2    3    4    5
cur         
 0        X     X    X    X    X    X   
 1        0     0    1    0    3    0
 2        0     1    0    3    0    9
 3        1     0    2    0    6    0
 4        0     1    0    3    0    10
 5        0     0    1    0    4    0
 6        0     0    0    1    0    5
 7        0     0    0    0    1    0

"""
# 根据记忆化搜索方法，写出动态规划
# 外层循环遍历列rest，内层循环遍历行cur，不能改顺序，因为有依赖关系
def ways4(N,M,K,P):
    if N<2 or K<1 or M<1 or M>N or P<1 or P>N:
        return 0 

    dp=[[0 for _ in range(K+1)] for _ in range(N+1)]

    # 剩余步数rest为0时来到了目标位置P，于是找到一种方法
    # 第0列除了第P行外，其余取值都是默认的0
    dp[P][0]=1
    
    # 处理剩余步数rest取值是1...K的情况
    for rest in range(1,K+1):
        # 来到左边界
        # 当前位于1位置，只能向2位置走，
        # 即：等于其左下角的元素值
        dp[1][rest]=dp[2][rest-1]

        # 非边界，此时cur取值为2...N-1
        # 即：等于其左上角的元素值+左下角的元素值
        for cur in range(2,N):
            dp[cur][rest]=dp[cur-1][rest-1]+dp[cur+1][rest-1]
        
        # 来到右边界
        # 当前位于N位置，只能向N-1位置走
        # 即：等于其左上角的元素值
        dp[N][rest]=dp[N-1][rest-1]
    
    return dp[M][K]
N,M,K,P=5,2,6,4
print(ways4(N,M,K,P))



# 动态规划常用的4种尝试模型
# 1) 从左往右的尝试模型
# 2) 范围上的尝试模型
# 3) 多样本位置全对应的尝试模型
# 4) 寻找业务限制的尝试模型



