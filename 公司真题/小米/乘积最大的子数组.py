# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

# 测试用例的答案是一个 32-位 整数。

# 子数组 是数组的连续子序列。


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        #dp_max[i]: nums[0...i-1]的乘积最大的非空连续组数组的元素乘积
        dp_max=[0 for _ in range(n+1)]
        #dp_min[i]: nums[0...i-1]的乘积最小的非空连续组数组的元素乘积
        dp_min=[0 for _ in range(n+1)]

        #初始化
        dp_max[0]=1
        dp_min[0]=1

        for i in range(1,n+1):
            if nums[i-1]>0:
                dp_max[i]=max(dp_max[i-1]*nums[i-1],nums[i-1])
                dp_min[i]=min(dp_min[i-1]*nums[i-1],nums[i-1])
            else:
                dp_max[i]=max(dp_min[i-1]*nums[i-1],nums[i-1])
                dp_min[i]=min(dp_max[i-1]*nums[i-1],nums[i-1])
        return max(dp_max[1:])