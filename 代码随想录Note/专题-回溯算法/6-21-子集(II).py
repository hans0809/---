# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:

# 输入: [1,2,2]
# 输出: [ [2], [1], [1,2,2], [2,2], [1,2], [] ]

# 相对于子集，只需要加个过滤重复的判断条件就好了
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        path=[]

        nums.sort()

        def backtrack(nums,start_index):
            res.append(path[:])
            if start_index>n-1:
                return
            
            for i in range(start_index,n):
                if i>start_index and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(nums,i+1)
                path.pop()
        
        backtrack(nums,0)

        return res