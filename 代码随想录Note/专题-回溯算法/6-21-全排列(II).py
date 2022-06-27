# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

# 示例 1：

# 输入：nums = [1,1,2]
# 输出： [[1,1,2], [1,2,1], [2,1,1]]
# 示例 2：

# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# 需要通过排序的方式去重
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()

        res=[]
        path=[]

        used=[False for _ in range(n)]

        def backtrack(nums,used):
            if len(path)==n:
                res.append(path[:])
                return
            
            for i in range(0,n):
                # 去重
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:#used[i-1]也可以
                    continue
                if not used[i]:
                    path.append(nums[i])
                    used[i]=True
                    backtrack(nums,used)
                    used[i]=False
                    path.pop()
            
        backtrack(nums,used)

        return res