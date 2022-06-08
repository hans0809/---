# 连通区域（Connected Component）一般是指图像中具有相同像素值且位置相邻的像素点组成的图像区域。
# 每个像素点有8个邻接点，包括了上下左右和对角线的像素点。如果点a与b邻接，称之为a与b连通。
# 如果域A与B连通，B与C连通，则A与C也连通。
# 试找出一个二值矩阵的所有连通域（8邻接），并给出每个连通域的面积（邻接点的个数）和重心。

# 输入描述:
# 每组输入包括 M+1 行，第一行输入2个整数 M (1<M<100), N (1<N<100)，其中M是矩阵的行数，N是矩阵的列数。

# 第2至M+1行，每行 N 个整数，表示在矩阵N列的像素值（已二值化为 0 和 1， 连通域为 1 表示的区域）。

# 输出描述:
# 输出 K+1 行，第一行输出连通域个数K，第2至 K+1 行，每行输出3个数，依次表示为连通域的面积值和重心的坐标值（保留2位小数点），按照连通域起始点顺序输出。

# 输入例子1:
# 4 4
# 0 1 0 0
# 0 0 0 1
# 0 0 0 1
# 1 0 0 0

# 输出例子1:
# 3
# 1 1.00 0.00
# 2 3.00 1.50
# 1 0.00 3.00


# 中心点：就是组成连通域的所有格子的x和y各自的平均值。。。
def run(grid):
    m,n=len(grid),len(grid[0])
    areas=[]# 存储连通域的面积
    
    def dfs(grid,i,j):
        area=1
        grid[i][j]=0#已访问
        
        for delta_i,delta_j in [[0,1],[0,-1],[-1,0],[1,0],[-1,-1],[1,1],[-1,1],[1,-1]]:
            new_i,new_j=i+delta_i,j+delta_j
            if 0<=new_i<=m-1 and 0<=new_j<=n-1 and grid[new_i][new_j]==1:
                cur_coors.append([new_i,new_j])# 存储组成当前连通域的每一个格子的坐标信息
                cur_area=dfs(grid,new_i,new_j)
                area+=cur_area
        return area

    coors=[]
    for i in range(m):
        for j in range(n):
            cur_coors=[]# 存储对应的每个连通域的坐标(保留2位小数)
            if grid[i][j]==1:
                cur_coors.append([i,j])
                area=dfs(grid,i,j)
                areas.append(area)
                
            if cur_coors:
                coors.append(cur_coors)
    
    return areas,coors

while True:
    try:
        m,n=map(int,input().split(' '))
        grid=[]
        for _ in range(m):
            row=list(map(int,input().split(' ')))
            grid.append(row)

        areas,coors=run(grid)

        k=len(areas)
        print(k)

        for i in range(k):
            rows=[item[0] for item in coors[i]]
            cols=[item[1] for item in coors[i]]
            xc=sum(rows)/areas[i]
            yc=sum(cols)/areas[i]
            print('%d %.2f %.2f'%(areas[i],yc,xc))
    except:
        break