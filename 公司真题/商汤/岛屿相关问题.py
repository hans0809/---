## 岛屿数量
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        visited=[[0]*n for _ in range(m)]

        def dfs(grid,x,y):
            visited[x][y]=1
            for d in [[0,1],[1,0],[0,-1],[-1,0]]:
                newx=x+d[0]
                newy=y+d[1]
                if 0<=newx<m and 0<=newy<n and not visited[newx][newy] and grid[newx][newy]=='1' :
                    dfs(grid,newx,newy)
            return

        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j]:
                    res+=1
                    dfs(grid,i,j)
        return res

## 岛屿的最大面积
# 给你一个大小为 m x n 的二进制矩阵 grid 。

# 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

# 岛屿的面积是岛上值为 1 的单元格的数目。

# 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

class Solution:
    """
    #方法1：DFS
    def dfs(self,grid,cur_i,cur_j):
        if (cur_i <0) or (cur_i>=len(grid)) or (cur_j<0) or cur_j>=len(grid[0]) or grid[cur_i][cur_j]!=1:
            return 0#当前位置是水，不再进行dfs，土地面积为0
        #否则，当前位置是土地
        #为了避免重复计数，将当前土地位置置为0
        grid[cur_i][cur_j]=0
        ans=1#已经找到一块土地
        #然后开始搜索这块土地的四周
        for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            next_i,next_j=cur_i+di,cur_j+dj
            ans+=self.dfs(grid,next_i,next_j)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        for i ,l in enumerate(grid):
            for j,n in enumerate(l):
                ans=max(ans,self.dfs(grid,i,j))
        return ans
    """
    """
    #方法2：DFS+栈
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0#初始化土地面积为0
        for i,l in enumerate(grid):#遍历每一个像素点
            for j ,n in enumerate(l):#遍历每一个像素点
                cur=0
                stack=[(i,j)]
                while stack:
                    cur_i, cur_j = stack.pop()
                    if cur_i<0 or cur_i>=len(grid) or cur_j<0 or cur_j>=len(grid[0]) or grid[cur_i][cur_j]!=1:
                        continue
                    
                    cur+=1
                    grid[cur_i][cur_j]=0#！！！已经访问过的需要置为0，避免重复计算
                    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                        next_i=di+cur_i
                        next_j=dj+cur_j
                        stack.append((next_i, next_j))
                ans=max(ans,cur)
        return ans
        """
    #方法3：BFS，只需把方法二中的栈改为队列，每次从队首取出土地，并将接下来想要遍历的土地放在队尾
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:   
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                cur = 0
                q = collections.deque([(i, j)])
                while q:
                    cur_i, cur_j = q.popleft()
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    cur += 1
                    grid[cur_i][cur_j] = 0
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        q.append((next_i, next_j))
                ans = max(ans, cur)
        return ans                                                                       