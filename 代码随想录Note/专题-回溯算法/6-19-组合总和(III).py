# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

# 说明：

# 所有数字都是正整数。
# 解集不能包含重复的组合。
# 示例 1: 输入: k = 3, n = 7 输出: [[1,2,4]]

# 示例 2: 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]]

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        path=[]
        def backtrack(k,n,start_index):
            if len(path)==k:
                if sum(path)==n:
                    res.append(path[:])
                return
            
            for i in range(start_index,9+1):
                path.append(i)
                backtrack(k,n,i+1)
                path.pop()
            
        backtrack(k,n,1)

        return res

# 剪枝优化
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        path=[]
        def backtrack(k,n,start_index):
            if len(path)==k:
                if sum(path)==n:
                    res.append(path[:])
                return
                
            # 剪枝优化
            for i in range(start_index,9-(k-len(path))+1+1):
                path.append(i)
                backtrack(k,n,i+1)
                path.pop()
            
        backtrack(k,n,1)

        return res