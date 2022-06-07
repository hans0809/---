# A[n,m]是一个n行m列的矩阵，a[i,j]表示A的第i行j列的元素，
# 定义x[i,j]为A的第i行和第j列除了a[i,j]之外所有元素(共n+m-2个)的乘积，
# 即x[i,j]=a[i,1]*a[i,2]*...*a[i,j-1]*...*a[i,m]*a[1,j]*a[2,j]...*a[i-1,j]*a[i+1,j]...*a[n,j],
# 现输入非负整形的矩阵A[n,m]，求MAX(x[i,j])，即所有的x[i,j]中的最大值。

# 输入描述:
# 第一行两个整数n和m。之后n行输入矩阵，均为非负整数。

# 输出描述:
# 一行输出答案。

# 输入例子1:
# 3 5
# 5 1 8 5 2
# 1 3 10 3 3
# 7 8 5 5 16

# 输出例子1:
# 358400
def run(matrix):
    n,m=len(matrix),len(matrix[0])#nxm
    
    def get_x(i,j):
        sum_=1
        for row in range(n):
            if row!=i:
                sum_*=matrix[row][j]
        for col in range(m):
            if col != j:
                sum_*=matrix[i][col]
        return sum_

    res=-1
    for i in range(n):
        for j in range(m):
            cur=get_x(i,j)
            res=max(res,cur)
    return res

while True:
    try:
        n,m=map(int,input().split(' '))

        matrix=[[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            s=input().split(' ')
            for j in range(m):
                matrix[i][j]=int(s[j])

        res=run(matrix)
        print(res)
    except:
        break