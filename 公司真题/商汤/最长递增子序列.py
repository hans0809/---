# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        #dp[i]：nums[0..i-1]中最长严格递增子序列的长度
        dp=[1 for _ in range(n+1)]

        #初始化
        dp[0]=0#dp[1...]=1
        
        for i in range(1,n+1):
            for j in range(1,i):
                if nums[j-1]<nums[i-1]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp[1:])