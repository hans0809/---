# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        n,m=len(matrix),len(matrix[0])
        col=m-1
        row=0
        while col>=0 and row<=n-1:
            if matrix[row][col]>target:
                col-=1
            elif matrix[row][col]<target:
                row+=1
            else:
                return True
        return False