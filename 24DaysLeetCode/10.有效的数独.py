# 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

# 哈希表
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[[0 for i in range(9)] for j in range(9)]
        cols=[[0 for i in range(9)] for j in range(9)]
        subboxes=[[[0 for i in range(9)] for j in range(3)] for k in range(3)]
        for i in range(9):
            for j in range(9):
                c=board[i][j]
                if c!='.':
                    index=int(c)-1
                    rows[i][index]+=1
                    cols[j][index]+=1
                    subboxes[i//3][j//3][index]+=1
                    if rows[i][index]>1 or cols[j][index]>1 or subboxes[i//3][j//3][index]>1:
                        return False
        return True
# 仍然是哈希表
class Solution:
    def isValidSudoku(self, board):
        row, col, sqrt = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                point = i // 3 * 3 + j // 3# 9*9的格子可以分为9个3*3的（编号0...8）
                if val in row[i] or val in col[j] or val in sqrt[point]:
                    print(i, j, val)
                    print(row, col, sqrt)
                    return False
                row[i].add(val)
                col[j].add(val)
                sqrt[point].add(val)
        return True


