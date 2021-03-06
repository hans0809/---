# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

# 要求时间复杂度为O(n)。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)

        dp=[0 for _ in range(n)]

        dp[0]=nums[0]

        for i in range(1,n):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
        return max(dp)