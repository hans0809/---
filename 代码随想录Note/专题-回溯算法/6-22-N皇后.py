
# 回溯思想：棋盘的宽度就是for循环的长度，递归的深度就是棋盘的高

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[['.' for _ in range(n)] for _ in range(n)]

        def is_valid(board,row,col):
            #判断同一列是否冲突
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False
            # 判断左上角是否冲突
            i = row -1#row
            j = col -1#col
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # 判断右上角是否冲突
            i = row - 1#row
            j = col + 1#col
            while i>=0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True
            

        def backtrack(board,row):
            if row==n:
                temp_res = []
                for temp in board:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)
            
            for col in range(n):
                if is_valid(board,row,col):
                    board[row][col]='Q'
                    backtrack(board,row+1)
                    board[row][col]='.'
        
        backtrack(board,0)

        return res