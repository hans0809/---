# 多多鸡有N个魔术盒子（编号1～N），其中编号为i的盒子里有i个球。
# 多多鸡让皮皮虾每次选择一个数字X（1 <= X <= N），多多鸡就会把球数量大于等于X个的盒子里的球减少X个。
# 通过观察，皮皮虾已经掌握了其中的奥秘，并且发现只要通过一定的操作顺序，可以用最少的次数将所有盒子里的球变没。
# 那么请问聪明的你，是否已经知道了应该如何操作呢？

# 输入描述：
# 第一行，有1个整数T，表示测试用例的组数。
# （1 <= T <= 100）
# 接下来T行，每行1个整数N，表示有N个魔术盒子。
# （1 <= N <= 1,000,000,000）

# 输出描述:
# 共T行，每行1个整数，表示要将所有盒子的球变没，最少需要进行多少次操作。


# 要用最少的次数把所有盒子减到0，第一次必然是减少中间盒子的球数
# 比如 1，2，3，4，5， 第一次减3 得到1，2，0，1，2 ,这时我们可以看到左右两边相等的，分冶求解
def cal(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return 1+cal(n//2)
T=int(input())
for i in range(T):
    n=int(input())
    res=cal(n)
    print(res)




# def run(N):
#     # 背包容量
#     w=sum(list(range(1,N+1)))

#     # 可选物品：[1,2,...,N], 并且可以重复选择，所以可以看做是完全背包问题
#     n=N# 物品数
#     weights=list(range(1,N+1))# 物品重量
#     values=list(range(1,N+1))# 物品价值

#     # dp[i]:背包容量为i时装满背包所需最少次数
#     big=999999999999
#     dp=[big for _ in range(w+1)]

#     # 初始化
#     #背包容量为0时，啥也不用装背包就满了，因此装满背包所需最少次数是0
#     dp[0]=0

#     for i in range(n):
#         for j in range(1,w+1):
#             if j<weights[i]:
#                 dp[j]=dp[j-1]
#             else:
#                 dp[j]=min(dp[j-1],dp[j-weights[i]]+1)# 错误！
#     return dp[w]