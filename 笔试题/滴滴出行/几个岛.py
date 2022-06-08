# 给定一个m行n列的二维地图, 初始化每个单元都是水.
# 操作addLand 把单元格(row,col)变成陆地.
# 岛屿定义为一系列相连的被水单元包围的陆地单元, 横向或纵向相邻的陆地称为相连(斜对角不算).
# 在一系列addLand的操作过程中, 给出每次addLand操作后岛屿的个数.
# 二维地图的每条边界外侧假定都是水.

# 输入描述:
# 多组测试数据，请参考例题处理 每组数据k+3行, k表示addLand操作次数 第一行:表示行数m 第二行:表示列数n 第三行:表示addLand操作次数k 第4~k+3行:row col 表示addLand的坐标。注意超过边界的坐标是无效的。

# 输出描述:
# 一行,k个整数, 表示每次addLand操作后岛屿的个数, 用空格隔开，结尾无空格

# 输入例子1:
# 3
# 3
# 4
# 0 0
# 0 1
# 1 2
# 2 1

# 输出例子1:
# 1 1 2 3

def run(m,n,coors):
    '''mxn的岛屿，初始化全是水(0)，本函数将给定的k个坐标coors所在位置变成岛屿(1)，并计算每次修改后的岛屿数量'''
    grid=[[0 for _ in range(n)] for _ in range(m)]

    k=len(coors)# coors:kx2

    res=[0]# 存储最终答案

    def dfs(grid,visited,i,j):
        visited[i][j]=1
        
        for delta_i,delta_j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            new_i,new_j=i+delta_i,j+delta_j
            if 0<=new_i<=m-1 and 0<=new_j<=n-1 and not visited[new_i][new_j] and grid[new_i][new_j]==1:
                dfs(grid,visited,new_i,new_j)


    def get_cur_ans(grid,visited):
        m,n=len(grid),len(grid[0])
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not visited[i][j]:
                    ans+=1
                    dfs(grid,visited,i,j)
        return ans



    for kk in range(k):
        x,y=coors[kk]

        # 判断输入的坐标是否越界
        if x<0 or x>m-1 or y<0 or y>n-1:
            res.append(res[-1])
            continue

        grid[x][y]=1

        visited=[[0 for _ in range(n)] for _ in range(m)]#0:未访问；1：已访问
        ans=get_cur_ans(grid,visited)

        res.append(ans)
    
    return res[1:]

while True:
    try:
        m=int(input())
        n=int(input())
        k=int(input())
        coors=[]
        for _ in range(k):
            x,y=map(int, input().split(' '))
            coors.append([x,y])
        res=run(m,n,coors)
        res=map(str,res)
        res=' '.join(res)
        print(res)
    except:
        break