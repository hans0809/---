# 在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。

# 给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。

# 重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。

# 如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # print(mat)#mat有可能是一维的，比如[[1,2,3,4]],而不是二维的[[1,2],[3,4]]
        n=0#总的元素个数
        nums=[]#总的元素(一维)
        for d in mat:
            n+=len(d)
            nums+=d

        if r*c!=n:
            return mat
    
        k=0#遍历nums

        ret=[[0 for _  in range(c)] for _ in range(r)]#rxc
        for i in range(r):
            for j in range(c):
                ret[i][j]=nums[k]
                k+=1
        return ret