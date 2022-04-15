# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        #dp[i]:nums[0...i-1]的最大连续子数组的和,i=1,2,...,n
        dp=[0 for _ in range(n+1)]

        #初始化
        dp[0]=0#dp[0]无意义

        for i in range(1,n+1):
            if dp[i-1]>0:
                dp[i]=dp[i-1]+nums[i-1]
            else:
                dp[i]=nums[i-1]
        return max(dp[1:])