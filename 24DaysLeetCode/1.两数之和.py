class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 方法1：双层循环，O(N^2)
        #for i in range(len(nums)):
        #    for j in range(i+1,len(nums)):
        #        if nums[i]+nums[j]==target:
        #            return [i,j]
        # 方法2：哈希表， O(N)
        record=dict()
        for i in range(len(nums)):
            if target-nums[i] in record:
                return [record[target-nums[i]],i]
            else:
                record[nums[i]]=i