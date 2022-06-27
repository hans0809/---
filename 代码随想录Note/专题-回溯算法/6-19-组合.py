# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

# 示例:
# 输入: n = 4, k = 2
# 输出:
# [
# [2,4],
# [3,4],
# [2,3],
# [1,2],
# [1,3],
# [1,4],
# ]

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        path=[]

        def backtrack(n,k,start_index):
            if len(path)==k:
                res.append(path[:])
                return
            
            for i in range(start_index,n+1):
                path.append(i)
                backtrack(n,k,i+1)
                path.pop()

        backtrack(n,k,1)

        return res

# 优化：如果后续不足k个，就没必要继续回溯了
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        path=[]

        def backtrack(n,k,start_index):
            if len(path)==k:
                res.append(path[:])
                return
            # 如果后续不足k个，就没必要继续回溯了
            for i in range(start_index,n-(k-len(path))+1+1):
                path.append(i)
                backtrack(n,k,i+1)
                path.pop()

        backtrack(n,k,1)

        return res