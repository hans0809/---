# 众所周知，美团外卖的口号是:”美团外卖,送啥都快”。
# 身着黄色工作服的骑手作为外卖业务中商家和客户的重要纽带，在工作中，以快速送餐突出业务能力；
# 工作之余，他们会通过玩智力游戏消遣闲暇时光，以反应速度彰显智慧，
# 每位骑手拿出装有货物的保温箱，参赛选手需在最短的时间内用最少的保温箱将货物装好。


# 我们把问题简单描述一下:

# 1 每个货物占用空间都一模一样

# 2 外卖小哥保温箱的最大容量是不一样的,每个保温箱由两个值描述:
#   保温箱的最大容量 bi ,当前已有货物个数 ai ,(ai<=bi)

# 3 货物转移的时候,不必（用'不能'可能会更好理解些）一次性全部转移,每转移一件货物需要花费 1秒 的时间

# 输入描述:
# 第一行包含n个正整数(1<=n<=100)表示保温箱的数量

# 第二行有n个正整数a1,a2,…,an(1<=ai<=100)

# ai表示第i个保温箱的已有货物个数

# 第三行有n个正整数b1,b2,…,bn(1<=bi<=100),bi表示第i个保温箱的最大容量

# 显然,每一个ai<=bi


# 输出描述:
# 输出为两个整数k和t, k表示能容纳所有货物的保温箱的最少个数,t表示将所有货物转移到这k个保温箱所花费的最少时间,单位为秒.


# 输入例子1:
# 4 
# 3 3 4 3
# 4 7 6 5

# 输出例子1:
# 2 6

# 例子说明1:
# 我们可以把第一个保温箱中的货物全部挪到第二个保温箱中,花费时间为3秒,此时第二个保温箱剩余容量为1,
# 然后把第四个保温箱中的货物转移一份到第二个保温箱中,转移最后两份到第三个保温箱中.
# 总花费时间也是3秒,所以最少保温箱个数是2,最少花费时间为6秒

# 我用贪心只能过3个测试用例，总共10个测试用例。。。。（只能保证最少的保温箱数，不能保证最少的转移时间？）


# 正确方法：动态规划，看做01背包问题







# 我用贪心只能过3个测试用例，总共10个测试用例。。。。（只能保证最少的保温箱数，不能保证最少的转移时间？）
def run(already,max_size):
    '''
    already: 每个保温箱中已有货物数
    max_size: 每个保温箱最多能容纳的货物数

    return:
        装完所有货物所需最少的保温箱数+货物转移花费的最少时间
    '''
    n=len(max_size)#n=len(already) 保温箱的个数

    total=sum(already)# 货物总数
    
    remain=total# 剩余未装的货物数

    # 按照保温箱的容量对already从大到小排序
    info=zip(max_size,already)
    info=sorted(info,key=lambda x:x[0],reverse=True)
    # print(info)
    min_time=0# 装完所有货物所需最少的时间
    min_boxes_num=0# 装完所有货物所需最少的保温箱数

    # 求解装完所有货物所需最少的保温箱数min_boxes_num
    for i in range(n):
        size,alrea=info[i]# size：当前保温箱的最大容量，alrea：当前保温箱中已装货物的数量

        min_boxes_num+=1
        remain-=size
        if remain<=0:
            break

    # 求解装完所有货物所需最少的时间
    min_box_all_size=0# 已经选择好的min_boxes_num个保温箱中已经装入的总的货物数量
    for i in range(min_boxes_num):
        size,alrea=info[i]# size：当前保温箱的最大容量，alrea：当前保温箱中已装货物的数量
        min_box_all_size+=alrea
    min_time=total-min_box_all_size# 全部货物数量-已经装好的货物数量=需要转移的货物数量=转移所需最少时间

    # 到这里，这个最少时间还不一定是最少的
    

    return min_boxes_num, min_time


while True:
    try:
        n=int(input())
        already=list(map(int,input().split(' ')))
        max_size=list(map(int,input().split(' ')))
        res=run(already,max_size)
        print(res[0],res[1])
    except:
        break