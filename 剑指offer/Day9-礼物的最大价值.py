# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
# 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
# 给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 有点像最大路径和
        m,n=len(grid),len(grid[0])
        #dp[i][j]：到达grid[i][j]位置能够获得的价值
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)]

        # 第一列
        for i in range(1,m+1):
            dp[i][1]=grid[i-1][0]+dp[i-1][1]
        # 第一行
        for j in range(1,n+1):
            dp[1][j]=grid[0][j-1]+dp[1][j-1]
        # print(dp)

        for i in range(2,m+1):
            for j in range(2,n+1):
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
        
        return dp[m][n]