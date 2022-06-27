# 编写一个程序，通过填充空格来解决数独问题。

# 一个数独的解法需遵循如下规则： 数字 1-9 在每一行只能出现一次。
#  数字 1-9 在每一列只能出现一次。 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
# 空白格用 '.' 表示。

# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。

# N皇后问题需要for遍历每一行，递归遍历每一列
# 解数独需要两个for遍历每一行每一列，递归遍历数字1到9
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board)#board:9x9
        digits=list(range(1,10))

        def is_valid(board,row,col,d):
            # 同行不能重复
            for i in range(9):
                if board[row][i]==str(d):
                    return False
            # 同列不能重复
            for i in range(9):
                if board[i][col]==str(d):
                    return False
            # 九宫格不能重复
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == str(d):
                        return False
            return True

        def backtrack(board):
            for row in range(n):
                for col in range(n):
                    if board[row][col]!='.':
                        continue
                    for d in digits:
                        if is_valid(board,row,col,d):
                            board[row][col]=str(d)
                            if backtrack(board):
                                return True
                            board[row][col]='.'
                    # 若数字1-9都不能成功填入空格，返回False无解
                    return False
            return True
        
        backtrack(board)