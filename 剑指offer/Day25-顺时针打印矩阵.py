# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

#  

# 示例 1：

# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：

# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix

        m,n=len(matrix),len(matrix[0])

        a=[0,0]# 左上角
        b=[m-1,n-1]# 右下角

        res=[]

        while a[0]<=b[0] and a[1]<=b[1]:
            # 只剩下一行
            if a[0]==b[0]:
                # 就只需打印这一行
                for j in range(a[1],b[1]+1):
                    # print(matrix[a[0]][j])
                    res.append(matrix[a[0]][j])
            # 只剩下一列
            elif a[1]==b[1]:
                # 就只需打印这一列
                for i in range(a[0],b[0]+1):
                    # print(matrix[i][a[0]])
                    res.append(matrix[i][a[1]])
            else:
                # 打印上面一行
                for j in range(a[1],b[1]):
                    # print(matrix[a[0]][j])
                    res.append(matrix[a[0]][j])
                
                # 打印右面一列
                for i in range(a[0],b[0]):
                    # print(matrix[i][b[1]])
                    res.append(matrix[i][b[1]])
                
                # 打印下面一行
                for j in range(b[1],a[1],-1):
                    # print(matrix[b[0]][j])
                    res.append(matrix[b[0]][j])
                
                # 打印左面一列
                for i in range(b[0],a[0],-1):
                    # print(matrix[i][a[0]])
                    res.append(matrix[i][a[0]])
            
            a[0]+=1
            a[1]+=1
            b[0]-=1
            b[1]-=1
        
        return res