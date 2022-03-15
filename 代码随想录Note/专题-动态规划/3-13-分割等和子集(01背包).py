# 给你一个 只包含正整数 的 非空 数组 nums 。
# 请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100

# 直接套0-1背包:

# 背包的体积为target=sum / 2
# 背包要放入的商品（集合里的元素）重量为 元素的数值，价值也为元素的数值
# 背包如果正好装满，说明找到了总和为 sum / 2 的子集。
# 背包中每一个元素是不可重复放入。

# 思路分析: 对于nums里的'物品', 从这些物品里面拿, 每个物品只能拿一次
# 如果能够恰好装满target的背包,那么没有被拿到的物品组成的价值也是target,这样正好满足题意

# 二维dp, 好理解, 但慢
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #套背包问题，nums的 每个元素的值既代表每个物品的重量，又代表每个物品的价值
        weights=nums
        values=nums

        n=len(nums)# 物品数，这里就是nums所含元素的个数
        
        # 如果和是奇数，那么不可能完成划分，直接返回False
        if sum(nums)%2==1:
            return False
            
        target=sum(nums)//2# 背包容量w

        # dp[i][j]: 假设第0...i-1件物品都搞完了，只考虑拿不拿第i件物品，在背包容量为j时，能获得的最大价值
        dp=[[0 for _ in range(target+1)] for _ in range(n)]
        # 初始化
        # 背包容量为0时，啥也装不进去，所获最大价值全是0
        for i in range(n):
            dp[i][0]=0
        # 只考虑前1件物品时，只有当背包容量大于等于第一件物品的重量时，才能装得下这第一件物品
        for i in range(target+1):
            if i>=weights[0]:
                dp[0][i]=values[0]
     
        for i in range(1,n):# 遍历物品
            for j in range(0,target+1):#遍历背包
                #如果背包装不下,那只能选择不装第i件物品
                if j<weights[i]:
                    dp[i][j]=dp[i-1][j]
                # 如果装得下，那可以装也可以不装第i件物品，取两者中能获得最大价值的那种
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i]]+values[i])
        return dp[n-1][target]==target

# 一维dp
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #套背包问题，nums的 每个元素的值既代表每个物品的重量，又代表每个物品的价值
        weights=nums
        values=nums

        n=len(nums)# 物品数，这里就是nums所含元素的个数
        
        # 如果和是奇数，那么不可能完成划分，直接返回False
        if sum(nums)%2==1:
            return False
            
        target=sum(nums)//2# 背包容量w

        # dp[j]: 背包容量为j时，能够获得的最大价值
        dp=[0 for _ in range(target+1)]

        # 初始化：背包容量为0时，能够获得的最大价值是0
        dp[0]=0

        for i in range(n):#遍历物品
            for j in range(target,-1,-1):# 遍历背包，由递推式可知，后面的依赖于前面的，因此为了避免发生覆盖，需要从后往前遍历背包
                #如果背包装不下,那只能选择不装第i件物品
                if j<weights[i]:
                    dp[j]=dp[j]
                # 如果装得下，那可以装也可以不装第i件物品，取两者中能获得最大价值的那种
                else:
                    dp[j]=max(dp[j],dp[j-weights[i]]+values[i])

        return dp[target]==target







# 更新：二维dp物品标从1开始
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #套背包问题，nums的 每个元素的值既代表每个物品的重量，又代表每个物品的价值
        weights=nums
        values=nums

        n=len(nums)# 物品数，这里就是nums所含元素的个数
        
        # 如果和是奇数，那么不可能完成划分，直接返回False
        if sum(nums)%2==1:
            return False
            
        target=sum(nums)//2# 背包容量w

        # dp[i][j]: 假设第前i-1件物品都搞完了，只考虑拿不拿第i件物品，在背包容量为j时，能获得的最大价值
        dp=[[0 for _ in range(target+1)] for _ in range(n+1)]
        # 初始化
        # 背包容量为0时，啥也装不进去，所获最大价值全是0
        for i in range(1,n+1):
            dp[i][0]=0
        # 只考虑前1件物品时，只有当背包容量大于等于第一件物品的重量时，才能装得下这第一件物品
        for i in range(target+1):
            if i>=weights[0]:
                dp[1][i]=values[0]
     
        for i in range(2,n+1):# 遍历物品
            for j in range(0,target+1):#遍历背包
                #如果背包装不下,那只能选择不装第i件物品
                if j<weights[i-1]:
                    dp[i][j]=dp[i-1][j]
                # 如果装得下，那可以装也可以不装第i件物品，取两者中能获得最大价值的那种
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i-1]]+values[i-1])
        return dp[n][target]==target