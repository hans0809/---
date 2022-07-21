# 有位老铁设计了一个跳格子游戏，游戏有N个格子顺序排成一行，编号从1到N，
# 每个格子有点数Qi，有标记Li（标记的范围是1-M），每次跳格子，要选择一个格子a，以任意正偶数距离x跳到格子b，
# 如果格子b在游戏区域内，且La=Lb，则称为一次合法跳跃，获得的分数是(a + b) * (Qa + Qb)。


# 在继续设计游戏玩法时，这位老铁纠结了很久，于是他决定放弃……但是他想知道所有合法跳跃总共能获得多少分。


# 输入描述:
# 第一行N，M，表示格子数和标记种类数，

# 第二行N个数，表示格子的点数

# 第三行N个数，表示每个格子的标记

# 输出描述:
# 一个整数P，表示总共能获得的分数，由于分数可能很大，这里只需要输出分数除以10007的余数

# 输入例子1:
# 5 2
# 1 2 3 4 5
# 1 2 1 2 1

# 输出例子1:
# 152

# 例子说明1:
# 样例输出

# 样例解析，从1号格子可以调到3，5，2号格子跳到4，3号格子跳到5，所以分数为

# (1+3)*(1+3) + (1 + 5)*(1+5) + (3+5)*(3+5) + （2+4）*(2+4) = 152

# 超时：4/10 组用例通过
def jump(N,M,points,flags):
    '''
    N: 格子数
    M: 标记
    points: 点数
    flags: 标记
    '''
    score=0
    for i in range(N):# 格子的每一个位置都可能是开始起跳的地方
        j=i# 遍历用的指针
        j+=2
        while j<N:
            if flags[j]==flags[i]:
                tmp=(i+j+2)*(points[i]+points[j])
                score+=tmp
                if score>10007:
                    score=score%10007
            j+=2

    return score

# 或者jump另一种写法
def jump(N,M,points,flags):
    '''
    N: 格子数
    M: 标记
    points: 点数
    flags: 标记
    '''
    score=0
    for i in range(N):# 格子的每一个位置都可能是开始起跳的地方
        j=i# 遍历用的指针
        while j+2<N:
            j+=2
            if flags[j]==flags[i]:
                tmp=(i+j+2)*(points[i]+points[j])
                score+=tmp
                if score>10007:
                    score=score%10007
    return score

while True:
    try:
        N,M=list(map(int,input().split(' ')))
        points=list(map(int,input().split(' ')))
        flags=list(map(int,input().split(' ')))
        # print(N,M,points,flags)
        res=jump(N,M,points,flags)
        print(res)
    except:
        break