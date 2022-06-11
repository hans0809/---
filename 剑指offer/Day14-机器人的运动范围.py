# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
# 一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
# 也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
# 因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

class Solution:
    def __init__(self):
        self.res=0
    def movingCount(self, m: int, n: int, k: int) -> int:
        
        def sum_(i,j):
            s=0
            while i:
                s+=(i%10)
                i//=10
            while j:
                s+=(j%10)
                j//=10
            return s

        def dfs(i,j):
            self.res+=1
            visited[i][j]=1
            for delta_i,delta_j in [[0,1],[0,-1],[-1,0],[1,0]]:
                new_i,new_j=i+delta_i,j+delta_j
                if 0<=new_i<m and 0<=new_j<n and sum_(new_i,new_j)<=k and not visited[new_i][new_j]:
                    dfs(new_i,new_j)

        visited=[[0 for _ in range(n)] for _ in range(m)]
        visited[0][0]=1
        dfs(0,0)
        return self.res
