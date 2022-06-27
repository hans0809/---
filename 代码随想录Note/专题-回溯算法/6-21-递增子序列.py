# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

# 示例:

# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# 说明:

# 给定数组的长度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。


# 不能用排序去重的思想，因为这道题是求递增子序列，所以元素之间的相对位置不能变

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)

        res=[]
        path=[]

        def backtrack(nums,start_index):
            if len(path)>=2:
                res.append(path[:])

            if start_index>n-1:
                return
            
            used=set()#过滤本层for循环中已经使用过的数字，以此达到去重的目的
            for i in range(start_index,n):
                if (not path or nums[i]>=path[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(nums,i+1)
                    path.pop()
        
        backtrack(nums,0)

        return res