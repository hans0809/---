# 某次漫展，已知有n个打卡点，每个打卡点的活动需要 m_i 分钟完成，完成后获得奖励点 r_i，已经打卡过的点不能再去。

# 需要在规定 m 分钟内完成，尽可能多的收获奖励点，求获得最多的奖励点数。


# 输入描述:
# 第一行两个整数，打卡点的数量 n 和限制时间 m

# 第 2 到 1 + n 行，每行两个整数 m_i，r_i

# 数字以空格分割，其中 0 < n <= 100，1 <= m <= 120，1 <= m_i <= 10，1 <= r_i <= 100


# 输出描述:
# 整数, 最大的奖励点数

# 输入例子1:
# 4 6
# 2 4
# 2 35
# 1 43
# 2 10

# 输出例子1:
# 88

def run(n,m,ms,rs):
    # 背包容量
    w=m
    # 物品数量
    n=len(rs)
    # 物品重量
    weights=ms
    # 物品价值
    values=rs
    
    # 已经打卡过的地方不能再去，所以是01背包问题

    #dp[i]：背包容量为i时能够获得最大价值
    dp=[0 for _ in range(w+1)]

    # 初始化
    dp[0]=0# 背包容量为0时，啥也装不下，能够获得的最大价值为0

    for i in range(n):# 正序遍历物品
        for j in range(w,0,-1):# 倒叙遍历背包
            if j<weights[i]:
                dp[j]=dp[j]
            else:
                dp[j]=max(dp[j],dp[j-weights[i]]+values[i])
    
    return dp[w]

while True:
    try:
        n,m=map(int,input().split(' '))
        ms=[]
        rs=[]
        for i in range(n):
            cur_m,cur_s=map(int,input().split(' '))
            ms.append(cur_m)
            rs.append(cur_s)
        

        res=run(n,m,ms,rs)
        print(res)

    except:
        break