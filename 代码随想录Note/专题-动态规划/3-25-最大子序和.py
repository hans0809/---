# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例: 输入: [-2,1,-3,4,-1,2,1,-5,4] 输出: 6 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)#元素个数
        #dp[i]:只考虑nums[0...i-1]，能够得到的最大子序和
        dp=[0 for _ in range(n+1)]

        # 初始化
        dp[0]=0# 无意义，只是为了推导，因为dp[1]=dp[0]+nums[0]，恰好能凑出来
        # dp[1]=nums[0]

        for i in range(1,n+1):
            if dp[i-1]<0:
                dp[i]=nums[i-1]
            else:
                dp[i]=dp[i-1]+nums[i-1]
                
        # nums只包含一个负数，比如-1时，如果从0开始，那么dp[0]=0，返回0，但答案是-1
        return max(dp[1:])