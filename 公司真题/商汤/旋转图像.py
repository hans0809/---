# 把一个矩阵顺时针旋转90度

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rotateEdge(matrix,a,b,c,d):
            # 要交换的组数为d-b
            for i in range(d-b):
                temp=matrix[a][b+i]
                matrix[a][b+i]=matrix[c-i][b]#左上角=左下角（针对i=0时）
                matrix[c-i][b]=matrix[c][d-i]# 左下角=右下角（针对i=0时）
                matrix[c][d-i]=matrix[a+i][d]# 右下角=右上角（针对i=0时）
                matrix[a+i][d]=temp# 右上角=左上角（针对i=0时）

        # 设置左上角是(a,b)，右下角是(c,d)，每次处理一圈
        a,b=0,0 # a：行 b：列
        c,d=len(matrix)-1,len(matrix[0])-1 # c：行 d：列
        while a<c and b<d:# 等价于while a<c 或者while b<d，因为是正方形。注意这里用<还是<=都可以：奇数行时取的到等号，最中间的元素直接不动；偶数行时取不到等号
            # 打印一圈
            rotateEdge(matrix,a,b,c,d)
            # 更新，准备打印下一圈
            a+=1
            b+=1
            c-=1
            d-=1