class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 方法1：3重循环，O(N^3)，提交超时
        #nums.sort()
        #print(nums)
        #res=[]
        #for i in range(len(nums)):
        #    if i>0 and nums[i]==nums[i-1]:
        #        continue
        #    for j in range(i+1,len(nums)):
        #        if j>i+1 and nums[j]==nums[j-1]:
        #            continue
        #        for k in range(j+1,len(nums)):
        #            if k>j+1 and nums[k]==nums[k-1]:
        #                continue
        #            if nums[i]+nums[j]+nums[k]==0:
        #                res.append([nums[i],nums[j],nums[k]])
        #return res
        
        # 方法2：双指针，O(N^2)
        # 固定一个:O(N)，另外两个用双指针:O(N)
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            a=nums[i]
            left,right=i+1,n-1
            while left<right:
                if a+nums[left]+nums[right]==0:
                    res.append([a,nums[left],nums[right]])
                    while left <right and nums[left+1]==nums[left]:
                        left+=1
                    while right>left and nums[right-1]==nums[right]:
                        right-=1
                    left+=1
                    right-=1
                elif a+nums[left]+nums[right]>0:
                    right-=1
                elif a+nums[left]+nums[right]<0:
                    left+=1
        return res