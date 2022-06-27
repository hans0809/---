# 给定一个无重复元素的数组 candidates 和一个目标数 target ，
# 找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的数字可以无限制重复被选取。

# 说明：

# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 示例 1： 输入：candidates = [2,3,6,7], target = 7, 所求解集为： [ [7], [2,2,3] ]

# 示例 2： 输入：candidates = [2,3,5], target = 8, 所求解集为： [   [2,2,2,2],   [2,3,3],   [3,5] ]

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        res=[]
        path=[]

        def backtrack(candidates,target,strat_index):
            if sum(path)==target:
                res.append(path[:])
                return
            
            if sum(path)>target:
                return
            
            for i in range(strat_index,n):#for遍历树的宽度，backtrack遍历树的高度
                path.append(candidates[i])
                backtrack(candidates,target,i)#元素可以重复使用，所以还是i
                path.pop()
        
        backtrack(candidates,target,0)

        return res

#优化：如果当前的path元素和大于target，就不用进入下一层递归了
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        res=[]
        path=[]

        def backtrack(candidates,target,strat_index):
            if sum(path)==target:
                res.append(path[:])
                return
            
            if sum(path)>target:
                return
            
            for i in range(strat_index,n):
                if sum(path)>target:
                    return
                path.append(candidates[i])
                backtrack(candidates,target,i)
                path.pop()
        
        backtrack(candidates,target,0)

        return res