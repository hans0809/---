# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i,j=0,n-1
        while i<j:
            while i<j and nums[i]%2==1:
                i+=1
            while i<j and nums[j]%2==0:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
        
        return nums