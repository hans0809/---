# 统计一个数字在排序数组中出现的次数。

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        # find第一个大于target的下标p2（右侧边界）
        # find第一个大于等于target的下标p1（左侧边界）
        # 两者相减即是结果p2-p1+1

        # find 右侧边界p2
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid-1
        p2=left

        # 剪枝：若数组中无 target ，则提前返回，
        # 因为查找完右边界后， nums[j] 指向最右边的 target （若存在）。
        if right >= 0 and nums[right] != target: 
            return 0

        # find p1左侧边界
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        p1=left

        return p2-p1