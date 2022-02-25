# 同向双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        if n==0:
            return 0
        p1=0# 停在元素值等于val的位置
        p2=0#遍历
        
        while p1<n and nums[p1]!=val:
            p1+=1
        p2=p1+1
        while p2<n:
            if p1<n and nums[p2]!=val:
                nums[p1]=nums[p2]
                p1+=1
            p2+=1
        return p1
            

# 对撞双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        if n==0:
            return 0
        left=0
        right=n-1
        while left<=right:
            if nums[left]==val:
                nums[left]=nums[right]
                right-=1
            else:
                left+=1
        return left
        