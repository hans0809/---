# 比如nums=[1,2,3,7,8,8,8,9],查找target=8出现的第一个位置和最后一个位置就是4和6

#思路：查找第一个等于target的下标位置，以及最后一个等于target的下标位置


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #查找左边界
        def left_bound(nums,target):
            n=len(nums)
            left,right=0,n-1
            left_bounder=-2
            while left <=right:
                mid=(left+right)//2
                if nums[mid]>=target:
                    right=mid-1
                    left_bounder=right
                else:
                    left=mid+1
            return left_bounder
        
        #查找右边界
        def right_bound(nums,target):
            n=len(nums)
            left,right=0,n-1
            right_bounder=-2
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<=target:
                    left=mid+1
                    right_bounder=left
                else:
                    right=mid-1
            return right_bounder
        
        # 开始查找
        left_b,right_b=left_bound(nums,target),right_bound(nums,target)
        print(left_b,right_b)

        # target不在升序数组范围内
        if left_b==-2 or right_b==-2:
            return [-1,-1]
        # target在升序数组范围内，且存在于升序数组中
        if right_b-left_b>1:
            return [left_b+1,right_b-1]
        # target在升序数组范围内，但是不存在于升序数组中，比如[1,2,5],target=4, 此时right_b-left_b=2-1=1
        return [-1,-1]