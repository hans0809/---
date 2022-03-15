# 有一堆石头，每块石头的重量都是正整数。
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。
# 假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
# 如果 x == y，那么两块石头都会被完全粉碎； 
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。 
# 最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。

# 示例： 输入：[2,7,4,1,8,1] 输出：1 解释： 组合 2 和 4，得到 2，
# 所以数组转化为 [2,7,1,8,1]， 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
#  组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
#  组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

# 转化为0-1背包问题
# 本题物品的重量为store[i]，物品的价值也为store[i],
# 对应着01背包里的物品重量weight[i]和 物品价值value[i]。

# stones中的每个元素都是备选的物品,从这些物品里拿(每个只能拿一次),
# 使得恰好能装满容量为sum(stones)//2的背包

# 将石头分成两个集合，用一个集合粉碎另一个集合，
# 要使粉碎后的剩余重量最小，应该使得两个集合的石头重量之后尽可能地接近 
# 这个问题等价于：求在不超过sum(stones)//2的前提下，所能形成的最大数组序列和是多少？

# 二维dp
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 套背包：stones中的每一个元素都是一件物品，同时也是其自身对应的价值
        weights=stones
        values=stones

        n=len(stones)# 物品数
        target=sum(stones)//2# 背包容最大容量

        # dp[i][j]: 在第0...i-1件物品都已经搞定的前提下，只需考虑拿还是不拿第i件物品时，在背包容量为j时能获得的最大价值
        dp=[[0 for _ in range(target+1)] for _ in range(n)]

        #初始化
        # 背包容量为0时，啥也装不下，因此能够获得的最大价值为0
        for i in range(n):
            dp[i][0]=0
        # 只考虑前1件物品，初始化第0行
        for i in range(target+1):
            if i>=weights[0]:
                dp[0][i]=values[0]
        
        for i in range(1,n):
            for j in range(0,target+1):
                # 求dp[i][j]，其中0...i-1件物品已经搞完了，只需考虑拿还是不拿第i件物品

                # 如果背包已经装不下第i件物品，那么只能选择不拿第i件物品
                if j<weights[i]:
                    dp[i][j]=dp[i-1][j]
                # 否则，可以拿第i件物品，也可以不拿，取能够获得最大价值的选择
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i]]+values[i])

        #在计算target的时候，target = sum // 2 因为是向下取整，
        #所以sum(stones) - dp[n-1][target] 一定是大于等于dp[n-1][target]的。
        return (sum(stones)-dp[n-1][target]) - dp[n-1][target]
        

# 一维dp
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 套背包：stones中的每一个元素都是一件物品，同时也是其自身对应的价值
        weights=stones
        values=stones

        n=len(stones)# 物品数
        target=sum(stones)//2# 背包容最大容量

        # dp[j]: 在背包容量为j时能够获得的最大价值
        dp=[0 for _ in range(target+1)]

        # 初始化
        dp[0]=0 # 背包容量为0时，能够获得的最大价值是0

        for i in range(n):# 遍历物品
            for j in range(target,-1,-1):# 遍历背包
                if j<weights[i]:
                    dp[j]=dp[j]
                else:
                    dp[j]=max(dp[j],dp[j-weights[i]]+values[i])
        
        return (sum(stones)-dp[target]) - dp[target]


# 更新：二维dp，物品下标从1开始
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 套背包：stones中的每一个元素都是一件物品，同时也是其自身对应的价值
        weights=stones
        values=stones

        n=len(stones)# 物品数
        target=sum(stones)//2# 背包容最大容量

        # dp[i][j]: 在第1...i-1件物品都已经搞定的前提下，只需考虑拿还是不拿第i件物品时，在背包容量为j时能获得的最大价值
        dp=[[0 for _ in range(target+1)] for _ in range(n+1)]

        #初始化
        # 背包容量为0时，啥也装不下，因此能够获得的最大价值为0
        for i in range(1,n+1):
            dp[i][0]=0
        # 只考虑前1件物品，初始化第1行
        for i in range(target+1):
            if i>=weights[0]:
                dp[1][i]=values[0]
        
        for i in range(2,n+1):
            for j in range(0,target+1):
                # 求dp[i][j]，其中1...i-1件物品已经搞完了，只需考虑拿还是不拿第i件物品

                # 如果背包已经装不下第i件物品，那么只能选择不拿第i件物品
                if j<weights[i-1]:
                    dp[i][j]=dp[i-1][j]
                # 否则，可以拿第i件物品，也可以不拿，取能够获得最大价值的选择
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i-1]]+values[i-1])

        #在计算target的时候，target = sum // 2 因为是向下取整，
        #所以sum(stones) - dp[n-1][target] 一定是大于等于dp[n-1][target]的。
        return (sum(stones)-dp[n][target]) - dp[n][target]