# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。

# 示例:

# 输入: [1,2,3]
# 输出: [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]

#和组合问题的区别在于，不需要start_index，而是需要一个表来记录nums中的元素是否已经使用

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)

        res=[]
        path=[]

        used=[False for _ in range(n)]

        def backtrack(nums,used):
            if len(path)==n:
                res.append(path[:])
                return
            
            for i in range(0,n):
                if not used[i]:
                    path.append(nums[i])
                    used[i]=True
                    backtrack(nums,used)
                    used[i]=False
                    path.pop()
            
        backtrack(nums,used)

        return res