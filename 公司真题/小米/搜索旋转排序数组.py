# 整数数组 nums 按升序排列，数组中的值 互不相同 。

# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分查找 O(logN)
        n=len(nums)
        left,right=0,n-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[0]<=nums[mid]:#[left,mid]是有序数组
                if nums[0]<=target<=nums[mid]:# >=nums[0]保证target存在
                    right=mid-1
                else:
                    left=mid+1
            elif nums[0]>nums[mid]:#[mid,right]是有序数组
                if nums[mid]<=target<=nums[n-1]:# <=nums[n-1]保证target存在
                    left=mid+1
                else:
                    right=mid-1
        return -1
