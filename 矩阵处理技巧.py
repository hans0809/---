# 题目1：zigzag打印(伪)矩阵(不一定是方阵)。
"""
1   2   3   4  
5   6   7   8 
9   10  11  12
13  14  15  16
"""
# 打印输出顺序：1,2,5,9,6,3,4,7,10,13,14,11,8,12,15,16

# 解题：用四个变量定义两个点(Ar,Ac)和(Br,Bc)，初始都指向(0,0)位置
# r表示向右(按行)走，c表示向下(按列)走
# A和B同时走，
# A先向右走，直到最右边就开始向下走
# B先向下走，直到最下边开始往右走
#这样，A和B所在位置总能连成一条斜线，斜线经过的位置就是要打印输出的内容所在位置

def printZigZag(matrix):
    Ar,Ac,Br,Bc=0,0,0,0#(Ar,Ac)和(Br,Bc)是两个点
    Endr=len(matrix)-1#最大行号
    Endc=len(matrix[0])-1#最大列号

    fromUp2Down=False#是否是按照从右上到左下的顺序进行打印，第一次不是，因此初始化为False

    while Ar!=Endr+1:
    #while Bc!=Endc+1:# 都可以
        # 打印(Ar,Ac)和(Br,Bc)连成的斜线上的元素，打印的方向由fromUp2Down指定
        printLevel(matrix,Ar,Ac,Br,Bc,fromUp2Down)

        # 更新下一条斜线：A先更新r，再更新c；B先更新c，后更新r
        # 先更新A还是B都可以，但A和B各自内部的r和c的更新顺序不能改，原因如下：
        # 比如对于A来说，如果先更新Ac，那么再更新Ar时用到的Ac已经不是原来的Ac了，而是更新后的，这样就会出错，B同理

        # A先向右走，走到最右就向下走
        Ar=Ar if Ac!=Endc else Ar+1#下
        Ac=Ac+1 if Ac!=Endc else Ac#右

        # B先向下走，走到最下就向右走
        Bc=Bc if Br!=Endr else Bc+1#右
        Br=Br+1 if Br!=Endr else Br#下

        fromUp2Down=not fromUp2Down
def printLevel(matrix,Ar,Ac,Br,Bc,fromUp2Down):
    if fromUp2Down:
        while Ar<=Br:
            print(matrix[Ar][Ac],end=",")
            Ar+=1
            Ac-=1
    else:
        while Br>=Ar:
            print(matrix[Br][Bc],end=",")
            Br-=1
            Bc+=1

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
printZigZag(matrix)#1,2,5,9,6,3,4,7,10,13,14,11,8,12,15,16,
        

# 题目2：转圈打印(伪)矩阵
"""
1   2   3   4  
5   6   7   8 
9   10  11  12
13  14  15  16
"""
# 打印输出顺序：1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10

# 解题：用4个变量定义两个点(a,b)和(c,d)，(a,b)是左上角元素位置，(c,d)是右下角元素位置
# 比如初始时(a,b)=(0,0)，对应元素是1，(c,d)=(3,3)，对应元素是16
# 当遍历完最外面一圈后，(a,b)->(a+1,b+1),(c,d)->(c-1,d-1)

# 当不是方阵时，可能出现a=c或者b=d的情况，此时直接遍历这条直线即可
# 比如
"""
1   2   3
4   5   6
7   8   9
10  11  12
"""
# 最后剩下
"""
    5
    8
"""

# 或者
"""
1   2   3   4 
5   6   7   8 
9   10  11  12
"""
# 最后会剩下
"""
    6    7
"""

def printCircle(matrix):
    a,b=0,0 # a：行 b：列
    c,d=len(matrix)-1,len(matrix[0])-1 # c：行 d：列
    while a<=c and b<=d:# 取等号时，说明只剩一行或者一列
        # 打印一圈
        printEdge(matrix,a,b,c,d)
        # 更新，准备打印下一圈
        a+=1
        b+=1
        c-=1
        d-=1
def printEdge(matrix,a,b,c,d):
    # 如果只剩一行或者一列，那么就直接处理，完事儿
    if a==c:# 只剩一行
        for i in range(b,d+1):
            print(matrix[a][i],end=",")
    elif b==d:# 只剩一列
        for i in range(a,c+1):
            print(matrix[i][b],end=",")
    else:# 打印一圈
        curR=a# 遍历行用到的指针
        curC=b# 遍历列用到的指针
        # 左上->右上-1
        while curC<d:
            print(matrix[a][curC],end=",")
            curC+=1
        # 右上->右下-1
        while curR<c:
            print(matrix[curR][d],end=",")
            curR+=1
        # 右下->左下-1
        while curC>b:
            print(matrix[c][curC],end=",")
            curC-=1
        # 左下->左上-1
        while curR>a:
            print(matrix[curR][b],end=",")
            curR-=1
print('\n')
"""
1   2   3   4  
5   6   7   8 
9   10  11  12
13  14  15  16
"""
printCircle(matrix)#1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10,

matrix2=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
"""
1   2   3
4   5   6
7   8   9
10  11  12
"""
print('\n')
printCircle(matrix2)# 1,2,3,6,9,12,11,10,7,4,5,8,
    


# 题目3：原地旋转正方形(顺时针旋转90度)
"""
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
"""
# 旋转后：
"""
13   9   5   1
14  10   6   2
15  11   7   3
16  12   8   4
"""
# 解题：和上题一样，仍设置左上角是(a,b)，右下角是(c,d)，每次处理一圈
def rotate(matrix):
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
def rotateEdge(matrix,a,b,c,d):
    # 要交换的组数为d-b
    # 比如在下面的例子中，第一组是[1,4,16,13],第二组是[2,8,15,9],
    # 第三组是[3,12,14,5]
    # 看着第一组，就能推出下面的代码了
    for i in range(d-b):
        temp=matrix[a][b+i]
        matrix[a][b+i]=matrix[c-i][b]#左上角=左下角（针对i=0时）
        matrix[c-i][b]=matrix[c][d-i]# 左下角=右下角（针对i=0时）
        matrix[c][d-i]=matrix[a+i][d]# 右下角=右上角（针对i=0时）
        matrix[a+i][d]=temp# 右上角=左上角（针对i=0时）
"""
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
"""
# 旋转后：
"""
13   9   5   1
14  10   6   2
15  11   7   3
16  12   8   4
"""
print('\n')
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotate(matrix)
print(matrix)#[[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]



matrix2=[[1,2,3],[4,5,6],[7,8,9]]
"""
1 2 3
4 5 6
7 8 9
"""
rotate(matrix2)
# 旋转后：
"""
7 4 1
8 5 2
9 6 3
"""
print(matrix2)#[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
