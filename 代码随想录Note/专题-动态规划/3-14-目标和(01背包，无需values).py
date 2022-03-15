# 每个数字都有两种状态：被进行“+”， 或者被进行“-”，因此可以将数组分成A和B两个部分：
# A部分的数字全部进行“+”操作，B部分的数字全部进行“-”操作。

# 设数组的和为sum，A部分的和为sumA，B部分的和为sumB
# 根据上面的分析，我们可以得出： sumA + sumB = sum (1)
# 同时有： sumA - sumB = target (2)
# 将(1)式与(2)式相加，可以得到： 2sumA = sum + target (3)

# 即：sumA = (sum + target) / 2 ，自此，原问题可以转化为0-1背包问题：
# 有一些物品，第i个物品的重量为nums[i]， 背包的容量为sumA，问：有多少种方式将背包【恰好填满】

# 这里需要注意的是，由于每个数字都是非负整数，因此sumA, sumB, sum都是非负整数。
# 根据(3)， 2sumA一定为偶数(自然数的性质，2n是偶数)，因此sum + target也应该是偶数。如果计算出的sum + target不是偶数，则与推导过程矛盾，本题无解。

# 接下来推导状态转移方程：dp[i][j]的意义是，在前i个数字中，凑出和为j的组合(可以理解成放入A堆)，有多少种方法。
# 对于第i个数字，我们有两种选择：
# 1.选择将第i个数字放入A堆，此时，数字还剩i - 1个，背包的容量需要减去nums[i]。递推式为
# dp[i][j] = dp[i - 1][j - nums[i]]；
# 2.选择放弃第i个数字，直接来到第i - 1个数字，背包的容量不变。递推式为dp[i - 1][j]；
# 3.当背包的容量小于第i个数字时，即j < nums[i]，无法将第i个数字放入背包，只能跳过，递推式同2。

# 考虑到dp数组的意义，dp[0][0]即为“在前0个数字中，凑出和为0的组合，有几种方法”，我们只能选择放弃“第0个数字”，因此dp[0][0] = 1。

# 接下来说说遍历顺序。先遍历数字，再遍历背包。数字应该从第1个数字开始，而**背包应该从容量为0开始！！**这是因为，题目中指出了
# nums[i] >=0，可能为0，因此需要考虑到背包容量也为0的情况(比如，第1个数字为0，背包容量也为0时，有两种选择：选择0，或者不选，这两种选择都可以填满容量为0的背包)。本人在这个地方卡了半天，始终无法ac，最终发现了问题。。。

# 二维dp
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 假设加法的总和为x，那么减法的总和就是sum(nums)-x
        # 有：x - (sum(nums)-x)=target，即 2x = (target+sum(nums))
        
        # 由于2x一定是偶数，又因为2x = (target+sum(nums))，所以等号右侧也是偶数
        if (target+sum(nums))%2==1:
            return 0

        # 当abs(target)>sum(nums)时，无法使用nums凑出target
        # 如果这个数组如果可以用加法凑出某个正数，那么也一定能用减法凑出它的相反数，因此用abs
        if abs(target)>sum(nums):
            return 0

        # 此时，x=(target+sum(nums))//2，问题已经转化为01背包问题，即：
        # 有n=len(nums)个物品，每个物品的价值为nums[i]，重量也是nums[i]，
        # 给定背包的容量为x，求恰好装满背包的方案数(每个物品只能拿一次)
        x=(target+sum(nums))//2#背包容量

        weights=nums#重量
        values=nums#价值，这道题用不着价值

        n=len(nums)#物品数

        # dp[i][j]: 第0...i-1个物品已经搞定，只考虑装不装第i个物品时，恰好能够装满容量为j的背包的方案数
        dp=[[0 for _ in range(x+1)] for _ in range(n)]

        # 初始化
        #背包容量为0时，啥也不用装就符合题意了
        for i in range(n):
            dp[i][0]=1# 第0列全是0
        
        for i in range(n):# 遍历物品
            for j in range(x+1):# 遍历背包容量
                # 如果背包容量装不下第i个物品，只能不拿
                if j<weights[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    # 装得下，可以拿也可以不拿,总方案数=装的方案数+不装的方案数
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-weights[i]]# 不拿/拿 第i件物品的方案数
        return dp[n-1][x]  

# 一维dp
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 假设加法的总和为x，那么减法的总和就是sum(nums)-x
        # 有：x - (sum(nums)-x)=target，即 2x = (target+sum(nums))
        
        # 由于2x一定是偶数，又因为2x = (target+sum(nums))，所以等号右侧也是偶数
        if (target+sum(nums))%2==1:
            return 0

        # 当abs(target)>sum(nums)时，无法使用nums凑出target
        # 如果这个数组如果可以用加法凑出某个正数，那么也一定能用减法凑出它的相反数，因此用abs
        if abs(target)>sum(nums):
            return 0

        # 此时，x=(target+sum(nums))//2，问题已经转化为01背包问题，即：
        # 有n=len(nums)个物品，每个物品的价值为nums[i]，重量也是nums[i]，
        # 给定背包的容量为x，求恰好装满背包的方案数(每个物品只能拿一次)
        x=(target+sum(nums))//2#背包容量

        weights=nums#重量
        values=nums#价值，这道题用不着价值

        n=len(nums)#物品数

        # dp[j]: 恰好能够装满容量为j的背包的方案数
        dp=[0 for _ in range(x+1)]

        #初始化：背包容量为0时，啥也不用装就符合题意了，因此方案数为1
        dp[0]=1

        for i in range(n):# 遍历物品
            for j in range(x,-1,-1):# 遍历背包
                # 如果当前背包容量dp[j]装不下第i件物品，只能选择不装
                if j <weights[i]:
                    dp[j]=dp[j]
                else:
                    # 装得下第i件物品，可装可不装，总方案数=装的方案数+不装的方案数
                    dp[j]=dp[j]+dp[j-weights[i]]# 不拿/拿 第i件物品的方案数
        return dp[x]


# 更新：二维dp，物品下标从1开始（这样才准确，否则出现dp[-1][...]）
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 假设加法的总和为x，那么减法的总和就是sum(nums)-x
        # 有：x - (sum(nums)-x)=target，即 2x = (target+sum(nums))
        
        # 由于2x一定是偶数，又因为2x = (target+sum(nums))，所以等号右侧也是偶数
        if (target+sum(nums))%2==1:
            return 0

        # 当abs(target)>sum(nums)时，无法使用nums凑出target
        # 如果这个数组如果可以用加法凑出某个正数，那么也一定能用减法凑出它的相反数，因此用abs
        if abs(target)>sum(nums):
            return 0

        # 此时，x=(target+sum(nums))//2，问题已经转化为01背包问题，即：
        # 有n=len(nums)个物品，每个物品的价值为nums[i]，重量也是nums[i]，
        # 给定背包的容量为x，求恰好装满背包的方案数(每个物品只能拿一次)
        x=(target+sum(nums))//2#背包容量

        weights=nums#重量
        values=nums#价值，这道题用不着价值

        n=len(nums)#物品数

        # dp[i][j]: 前i-1个物品已经搞定，只考虑装不装第i个物品时，恰好能够装满容量为j的背包的方案数
        dp=[[0 for _ in range(x+1)] for _ in range(n+1)]

        # 初始化
        #背包容量为0时，啥也不用装就符合题意了,这也包括没有可选物品时，因此0(没有物品可选的情况)也要初始化
        for i in range(0, n+1):
            dp[i][0]=1# 第0列全是0
        
        for i in range(1,n+1):# 遍历物品，从1开始，因为没有初始化第1行（这题没有用到values，而求的是方案数）
            for j in range(x+1):# 遍历背包容量
                # 如果背包容量装不下第i个物品，只能不拿
                if j<weights[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    # 装得下，可以拿也可以不拿,总方案数=装的方案数+不装的方案数
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-weights[i-1]]# 不拿/拿 第i件物品的方案数
        return dp[n][x]  