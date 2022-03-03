# 题目1：牛牛有一些排成一行的正方形。每个正方形已经被染成红色或绿色。牛牛现在可以选择任意一个正方形然后用这两种颜色
# 的任意一种进行染色，这个正方形的颜色将会被覆盖。牛牛的目标是在完成染色之后，
# 每个红色R都在每个绿色G左侧，牛牛想要知道他最少需要染几个正方形
# 比如s=RGRGR，染完变成RRRGG满足要求了，最少要染2个正方形，没有比这个更好的方案。

def minPaint(s):
    s=list(s)
    N=len(s)

    # 打表预处理
    # 统计arr[0...index1]一共有多少个G，用于全部染成R 
    countG=[]
    numG=0
    for i in range(N):
        if s[i]=='G':
            numG+=1
        countG.append(numG)
    # 统计arr[index2...N-1]一共有多少个R，用于全部染成G
    countR=[]
    numR=0
    for i in range(N-1,-1,-1):
        if s[i]=='R':
            numR+=1
        countR.append(numR)
    countR=countR[::-1]
    print(countG,countR)
    # 左R 右G
    # 枚举左侧部分为0...L，右侧为L+1...N-1
    ans=9999999999999
    now=-1# debug用，无实际意义
    for L in range(N):
        if L==0:
            now=0
            # 统计arr[L...N-1]一共有多少个R，全部染成G
            ans=min(ans,countR[0])

        elif L==N-1:
            now=1
            # 统计arr[0...L]一共有多少个G，全部染成R
            ans=min(ans,countG[N-1])
        else:
            now=2
            # 统计arr[0...L]一共有多少个G，全部染成R 
            # +
            # 统计arr[L+1...N-1]一共有多少个R，全部染成G
            ans=min(ans,countG[L]+countR[L+1])
        print(L,now,ans)
    return ans
s='RGRGR'
print(minPaint(s))


# 题目2：给定一个N*N的矩阵，只有0和1两种取值，
# 返回边框全是1的最大正方形的边长长度
# 比如：
"""
01111
01001
01001
01111
01011
"""
# 其中边框全是1的最大正方形的大小为4*4，所以返回4

def maxRecLen(mt):
    N=len(mt)
    M=len(mt[0])

    # 打表，right和down是两个和mt同维度的矩阵
    # right[row][col]:mt[row][col]及其右侧出现连续的1的个数
    # down[row][col]:mt[row][col]及其下方出现连续的1的个数
    # 比如示例对应的right和down如下：
    """
    right:
    04321
    01001
    04321
    01021

    down:
    05115
    04004
    03003
    02122
    01011
    """
    right=[[0 for _ in range(N)] for _ in range(M)]
    down=[[0 for _ in range(N)] for _ in range(M)]
    for row in range(M):
        for col in range(N-1,-1,-1):
            if mt[row][col]==0:
                right[row][col]=0
            elif mt[row][col]==1:
                if col==N-1:# 最后一列
                    right[row][col]=1
                else:
                    right[row][col]=1+right[row][col+1]
    for col in range(N):
        for row in range(M-1,-1,-1):
            if mt[row][col]==0:
                down[row][col]=0
            elif mt[row][col]==1:
                if row==M-1:# 最后一列
                    down[row][col]=1
                else:
                    down[row][col]=1+down[row+1][col]

    # print(right,'\n',down)

    ans=-1
    for row in range(N):
        for col in range(M):
            # (row,col)确定矩阵左上角坐标
            # 然后枚举边长border
            border=1
            while border<=min(N-row,M-col):
                # 验证这个正方形的四条边，是不是上面的值都是1
                if right[row][col]>=border and down[row][col]>=border:
                    ans=max(ans,border)
                border+=1
    return ans
mt=[[0,1,1,1,1],[0,1,0,0,1],[0,1,0,0,1],[0,1,1,1,1],[0,1,0,1,1]]
print('全是1的正方形的最大边长为：',maxRecLen(mt))
# 时间复杂度：O(N^3)


# 题目3：

