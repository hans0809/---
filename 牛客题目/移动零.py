# 给定一个数组，请你实现将所有 0 移动到数组末尾并且不改变其他数字的相对顺序。
class Solution:
    def moveZeroes(self , nums) :
        # write code here
        i=0
        j=0
        n=len(nums)
        while i<n and j<n:
            if nums[i]!=0:
                i+=1
            else:
                # 此时i位置元素为0
                j=i+1
                while j<n and nums[j]==0:
                    j+=1
                if j<n and nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums