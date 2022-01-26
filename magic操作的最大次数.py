# 题目：给一个包含n个整数的集合a，一个包含m个整数的集合b
# 定义magic的操作为：从一个集合中取出一个元素，放到另一个集合里，且操作过后每个集合的平均值都大于操作前，
# 注意以下两点：
# 1) 不可以把一个集合的元素取空，这样就没有平均值了
# 2)值为x的元素从集合b取出放入集合a，但集合a中已经有值为x的元素，则a的平均值不变(因为集合中没有重复元素)，
#   b的均值可能改变(因为x被取出了)。
# 问最多可以进行多少次magic操作？

# 分析：
# 1. a和b的均值相等，假设是100：
# 1)从a中拿出一个小于100的数，那么a均值上升，b均值下降
# 2)从a中拿出一个大于100的数，那么a均值下降，b均值上升
# 3)从a中拿出一个等于100的数，那么a均值不变，b均值不变
# 以上都不满足magic操作的要求

# 2. a和b的均值不等，假设a均值小，为50，b均值大，为100
# 1)从a中拿出一个小于50的数，那么a均值上升，b均值下降
# 2)从a中拿出一个大于50小于100的的数，那么a均值下降，b均值下降
# 3)从a中拿出一个大于100的的数，那么a均值下降，b均值上升
# 4)从a中拿出一个等于50的数，那么a均值不变，b均值不下降
# 以上都不满足magic操作的要求

# 3. a和b的均值不等，假设a均值大，为100，b均值小，为50
# 此时，只要拿a中大于50小于100的数(且在b中不存在这样的数)，就满足magic操作的要求
# 为了使得magic操作次数尽可能大，优先拿满足要求的数中最小的(小贪心)

def solve(a,b):
    sum1=sum(a)
    sum2=sum(b)
    # 集合a和b的均值相等，直接返回0
    if sum1/len(a)==sum2/len(b):
        return 0

    # 不相等
    sumMore=0
    sumLess=0
    arrMore=a
    arrLess=b
    if sum1/len(a)>sum2/len(b):
        sumMore=sum1
        sumLess=sum2
        arrMore=a
        arrLess=b
    else:
        sumMore=sum2
        sumLess=sum1
        arrMore=b
        arrLess=a
    
    # 将均值较大的集合arrMore中满足要求的元素从小到大拿出来
    arrMore.sort()
    setLess=set()
    for num in arrLess:
        setLess.add(num)
    
    moreSize=len(arrMore)
    lessSize=len(arrLess)
    ops=0
    for i in range(len(arrMore)):
        cur=arrMore[i]
        if cur<sumMore/moreSize and cur >sumLess/lessSize and cur not in setLess:
            print('拿',cur)
            sumMore-=cur
            moreSize-=1
            sumLess+=cur
            lessSize+=1
            setLess.add(cur)
            ops+=1
    return ops

a=[1,2,5] 
b=[2,3,4,5,6]
print('magic操作的最大次数：',solve(a,b))





