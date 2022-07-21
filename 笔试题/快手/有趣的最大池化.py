# 链接：https://www.nowcoder.com/questionTerminal/2741361d86ca4d0c83c1ba9d8162527a
# 来源：牛客网

# 最近月神需要在移动端部署一个卷积神经网络模型,但是月神碰到了一个问题,即月神使用了一个核非常大的最大池化(max-pooling)操作,但现有推理引擎不支持这一操作,作为月神的好朋友,你能帮帮月神么。
# 所谓max-pooling,指的是给定一个数组（为了简化问题,暂定数组为一维）,在每一个滑动窗口内找出最大的那个数,举例如下：
# 假设数组为[16, 19, 15, 13, 16, 20],且核大小为3,则当窗口依次滑过数组时,取出如下4个子数组：
# [16, 19, 15], [19, 15, 13], [15, 13, 16], [13, 16, 20],这4个子数组中的最大值分别为19, 19, 16, 20,故该数组经过大小为3的核的max-pooling的结果为19 19 16 20.

# 输入描述:
# 输入由三行构成

# 第一行是一个整数n，  给出数组中元素个数

# 第二行是n个整数，     给出数组中的元素
# 第三行是一个整数 ks , 给出max-pooling核的大小


# 输出描述:
# 输出一行（没有换行符）

# 输出给定数组及给定核大小的后，max-pooling的结果,

# 每两个整数之间加一个空格
# 示例1
# 输入
# 5
# 31 24 21 14 22
# 1
# 输出
# 31 24 21 14 22
# 示例2
# 输入
# 5
# 18 14 31 1 26
# 2
# 输出
# 18 31 31 26
# 示例3
# 输入
# 16
# 61 53 2 13 51 30 48 44 58 46 36 8 2 8 34 10
# 7
# 输出
# 61 53 58 58 58 58 58 58 58 46

# 运行超时：6/10 组用例通过
def max_pooling(n,nums,ks):
    res=[]
    for i in range(n):
        if i+ks-1<n:
            max_pool_value=max(nums[i:i+ks])
            res.append(max_pool_value)
        else:
            break
    return res

while True:
    n=int(input())
    nums=list(map(int,input().split(' ')))
    ks=int(input())

    res=max_pooling(n,nums,ks)
    res=[str(i) for i in res]
    print(' '.join(res))