# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

class Solution:
    def __init__(self):
        self.path=[]
        self.flag=False
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row,col,k):
            if not 0<=row<m or not 0<=col<n or board[row][col]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            
            board[row][col]='#'
            res=dfs(row+1,col,k+1) or dfs(row-1,col,k+1) or dfs(row,col+1,k+1) or dfs(row,col-1,k+1)
            board[row][col]=word[k]

            return res
        m,n=len(board),len(board[0])
        for row in range(m):
            for col in range(n):
                if dfs(row,col,0):
                    return True
        return False

# 用visited
class Solution:
    def __init__(self):
        self.path=[]
        self.flag=False
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row,col,k):
            if not 0<=row<m or not 0<=col<n or board[row][col]!=word[k] or visited[row][col]:
                return False
            if k==len(word)-1:
                return True
            
            visited[row][col]=1
            res=dfs(row+1,col,k+1) or dfs(row-1,col,k+1) or dfs(row,col+1,k+1) or dfs(row,col-1,k+1)
            visited[row][col]=0

            return res
        m,n=len(board),len(board[0])
        visited=[[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if dfs(row,col,0):
                    return True
        return False