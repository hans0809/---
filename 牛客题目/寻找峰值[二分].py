
# 给定一个长度为n的数组nums，请你找到峰值并返回其索引。
# 数组可能包含多个峰值，在这种情况下，返回任何一个所在位置即可。

# 思想:上坡一定有波峰，下坡不一定有波峰
class Solution:
    def findPeakElement(self , nums):
        # write code here
        n=len(nums)
        l,r=0,n-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                r=mid
        return l