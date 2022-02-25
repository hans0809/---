class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return n
        p1=0#[0...p1]是所求不重复数组段
        p2=1# 遍历

        while p2<n:
            if nums[p2]!=nums[p1]:

                nums[p1+1]=nums[p2]
                p1+=1
            p2+=1
        return p1+1