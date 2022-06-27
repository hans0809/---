# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例: 输入: nums = [1,2,3] 输出: [ [3],   [1],   [2],   [1,2,3],   [1,3],   [2,3],   [1,2],   [] ]




# 如果把 子集问题、组合问题、分割问题都抽象为一棵树的话，
# 那么组合问题和分割问题都是收集树的叶子节点，而子集问题是找树的所有节点！

# 其实子集也是一种组合问题，因为它的集合是无序的，子集{1,2} 和 子集{2,1}是一样的。

# 那么既然是无序，取过的元素不会重复取，写回溯算法的时候，for就要从startIndex开始，而不是从0开始！

# 有同学问了，什么时候for可以从0开始呢？

# 求排列问题的时候，就要从0开始，因为集合是有序的，{1, 2} 和{2, 1}是两个集合

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        path=[]

        def backtrack(nums,start_index):
            res.append(path[:])
            if start_index>n-1:
                return
            
            for i in range(start_index,n):
                path.append(nums[i])
                backtrack(nums,i+1)
                path.pop()
        
        backtrack(nums,0)

        return res