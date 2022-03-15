# 有n件物品和一个最多能背重量为w 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。
# 每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。

def bag(w,weights,values):
    """
    w: int 背包能够承受的最大重量
    weights:list 每件物品的种类
    values: list 每件物品的价值
    """
    n=len(values)# 物品数
    
    # dp[i][j]：只考虑第0...i件物品，装入容量为j的背包，能够获得的最大价值
    # (假设前i-1件物品都 整好了，只需考虑装还是不(能)装第i件物品)
    dp=[[0 for _ in range(w+1)] for _ in range(n)]

    # 初始化：
    # 背包容量为0时，啥也装不进去，所获最大价值全是0
    for i in range(n):
        dp[i][0]=0
    # 只考虑前1件物品时，只有当背包容量大于等于第一件物品的重量时，才能装得下这第一件物品
    for i in range(w+1):
        if i>=weights[0]:
            dp[0][i]=values[0]
    
    # 遍历剩余的地方
    for i in range(1,n):#遍历物品，，从0或1开始都行，反正前面都初始化了第0行了，
                        #但如果没初始化，那就必须从0开始
        for j in range(0,w+1):# 遍历背包，从0或1开始都行
            #如果背包装不下,那只能选择不装第i件物品
            if j<weights[i]:
                dp[i][j]=dp[i-1][j]
            # 如果装得下，那可以装也可以不装第i件物品，取两者中能获得最大价值的那种
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i]]+values[i])
    return dp[n-1][w]

weights=[1,3,4]
values=[15,20,30]
w=4
print(bag(w,weights,values))


# 滚动数组(将二维dp变成一维dp)
def bag2(w,weights,values):
    n=len(weights)#物品数
    #dp[j]: 背包容量为j时能够获得的最大价值
    dp=[0 for _ in range(w+1)]
    # 初始化：背包容量为0时能够装入的最大价值为0
    dp[0]=0

    for i in range(n):# 遍历物品，不能从1开始，否则报错。。。
        for j in range(w,-1,-1):#背包倒序遍历，否则发生覆盖，因为后一个是依赖于前一个的
            #如果背包装不下,那只能选择不装第i件物品
            if j<weights[i]:
                dp[j]=dp[j]
            # 如果装得下，那可以装也可以不装第i件物品，取两者中能获得最大价值的那种
            else:
                dp[j]=max(dp[j],dp[j-weights[i]]+values[i])
    return dp[w]
print(bag2(w,weights,values))



# 二维dp：物品下标从1开始
def bag_(w,weights,values):
    """
    w: int 背包能够承受的最大重量
    weights:list 每件物品的种类
    values: list 每件物品的价值
    """
    n=len(values)# 物品数
    
    # dp[i][j]：只考虑第0...i件物品，装入容量为j的背包，能够获得的最大价值
    # (假设前i-1件物品都 整好了，只需考虑装还是不(能)装第i件物品)
    dp=[[0 for _ in range(w+1)] for _ in range(n+1)]

    # 初始化：
    # 背包容量为0时，啥也装不进去，所获最大价值全是0
    for i in range(1,n+1):
        dp[i][0]=0
    # 只考虑前1件物品时，只有当背包容量大于等于第一件物品的重量时，才能装得下这第一件物品
    for i in range(w+1):
        if i>=weights[0]:
            dp[1][i]=values[0]
    
    # 遍历剩余的地方
    for i in range(2,n+1):#遍历物品，，从0或1开始都行，反正前面都初始化了第0行了，
                        #但如果没初始化，那就必须从0开始
        for j in range(0,w+1):# 遍历背包，从0或1开始都行
            #如果背包装不下,那只能选择不装第i件物品
            if j<weights[i-1]:
                dp[i][j]=dp[i-1][j]
            # 如果装得下，那可以装也可以不装第i件物品，取两者中能获得最大价值的那种
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i-1]]+values[i-1])
    return dp[n][w]

print(bag_(w,weights,values))