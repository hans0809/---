# 题目1：
#num=nums[-1],所有小于num的数都在左边，所有大于num的数都在右边
#希望找到最右边的小于num的数，比如这里就是6
nums=[3,2,5,4,1,6,    100,11,13,12,19,17,18,         10]
#    [0,1,2,3,4,5,       6, 7,  8 ,9,10,11 12          13

#nums=[2,1,0,5,4,3]

n=len(nums)

left,right=0,n-2
num=nums[-1]
index=0

#两种写法

# while(left <= right):
#     mid=(left+right)//2
    
#     if nums[mid]>num:#往左走
#         right=mid-1
#     elif nums[mid]<num:#往右走
#         index=mid#更新
#         left=mid+1

while(left < right):
    mid=(left+right)//2
    
    if nums[mid]>num:#往左
        right=mid
    elif nums[mid]<num:#往右
        index=mid#更新
        left=mid+1

print(nums[index])




# 题目2：请实现有重复数字的升序数组的二分查找
# 给定一个 元素有序的（升序）长度为n的整型数组 nums 和一个目标值 target，
# 写一个函数搜索 nums 中的第一个出现的target，如果目标值存在返回下标，否则返回 -1
# 进阶：时间复杂度O(logn) ，空间复杂度O(n)

# 我的答案：
class Solution:
    def search(self , nums, target):
        # write code here
        n=len(nums)
        left,right=0,n-1
        res=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                res=mid
                right=mid-1
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        return res
