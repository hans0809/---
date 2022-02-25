class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 双指针，O(N^2)
        # 固定一个:O(N)，另外两个用双指针:O(N)
        nums.sort()
        n=len(nums)
        res=0
        gap=10000000000000
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            a=nums[i]
            left,right=i+1,n-1
            while left<right:
                newGap=abs(a+nums[left]+nums[right]-target)
                if newGap<gap:
                    gap=newGap
                    res=a+nums[left]+nums[right]
                # 剪枝
                if gap==0:
                    return res
                elif a+nums[left]+nums[right]>target:
                    right-=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif a+nums[left]+nums[right]<target:
                    left+=1
                    while left <right and nums[left]==nums[left-1]:
                        left+=1
        return res
# 由于只有一个答案，且返回值是和，所以也可以不判重
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 双指针，O(N^2)
        # 固定一个:O(N)，另外两个用双指针:O(N)
        nums.sort()
        n=len(nums)
        res=0
        gap=10000000000000
        for i in range(n):

            a=nums[i]
            left,right=i+1,n-1
            while left<right:
                newGap=abs(a+nums[left]+nums[right]-target)
                if newGap<gap:
                    gap=newGap
                    res=a+nums[left]+nums[right]
                # 剪枝
                if gap==0:
                    return res
                elif a+nums[left]+nums[right]>target:
                    right-=1

                elif a+nums[left]+nums[right]<target:
                    left+=1

        return res