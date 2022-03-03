# 题目：在一个数组中，一个数左边比它小的数的总和，叫做数的小和，
# 所有数的小和累加起来，叫做数组小和
# 求数组小和。
# 比如，[1,3,4,2,5]
# 1左边比1小的数：没有
# 3左边比3小的数：1
# 4左边比4小的数：1,3
# 2左边比2小的数：1
# 5左边比5小的数：1,3,4,2
# 所以数组的小和为1+1+3+1+1+3+4+2=16


#先回顾一下归并排序：
def mergeSort(arr):
    if not arr or len(arr)<2:
        return
    process(arr,0,len(arr)-1)
def process(arr,L,R):
    if L==R:#base case，此时只有一个元素，自然是有序的
        return
    mid=(L+R)//2
    process(arr,L,mid)#对左半部分进行排序
    process(arr,mid+1,R)#对右半部分进行排序
    merge(arr,L,mid,R)#合并两个有序数组
def merge(arr,L,mid,R):
    res=[]
    # i=0#记录res数组长度
    p1=L#左半部分的指针
    p2=mid+1#右半部分的指针
    while p1<=mid and p2<=R:
        if arr[p1]<=arr[p2]:
            res.append(arr[p1])
            p1+=1
        else:
             res.append(arr[p2])
             p2+=1
        # i+=1
    while p1<=mid:
        res.append(arr[p1])
        # i+=1
        p1+=1
    while p2<=R:
        res.append(arr[p2])
        # i+=1
        p2+=1
    #当前的L到R部分用merge好的结果(即res)进行覆盖
    arr[L:(L+len(res))]=res#这一句和下面的for等价
    # for i in range(len(res)):
    #     arr[L+i]=res[i]




# 现在来解题：
# 每一次都将arr一分为2。
# **对于左侧中的每一个元素**，比如元素值为element
# 看右侧有几个比它大的，比如有x个
# 那么对应的小和就等于element*x
# 左侧每一个都能得到小和，把这些小和统统加起来就是要求的数组小和
def smallSum(arr):
    if not arr or len(arr)<2:
        return 0
    return process(arr,0,len(arr)-1)
def process(arr,L,R):
    if L==R:#base case，此时只有一个元素，自然是有序的,
        #只有一个元素，对应的小和为0
        return 0
    mid=(L+R)//2
    left_small_sum=process(arr,L,mid)#对左半部分进行排序(求小和)
    right_small_sum=process(arr,mid+1,R)#对右半部分进行排序（求小和）
    left_right_small_sum=merge(arr,L,mid,R)#合并两个有序数组(求左右两个部分之间的小和)
    return left_small_sum+right_small_sum+left_right_small_sum
def merge(arr,L,mid,R):
    res=[]
    # i=0#记录res数组长度
    p1=L#左半部分的指针
    p2=mid+1#右半部分的指针
    s=0#左右pk得到的小和
    while p1<=mid and p2<=R:
        if arr[p1]<arr[p2]:#相等时取右侧，左侧不动，这样才能求小和
            s+=arr[p1]*(R-p2+1)
            res.append(arr[p1])
            p1+=1
        else:
             res.append(arr[p2])
             p2+=1
        # i+=1
    while p1<=mid:
        res.append(arr[p1])
        # i+=1
        p1+=1
    while p2<=R:
        res.append(arr[p2])
        # i+=1
        p2+=1
    #当前的L到R部分用merge好的结果(即res)进行覆盖
    arr[L:(L+len(res))]=res#这一句和下面的for等价
    # for i in range(len(res)):
    #     arr[L+i]=res[i]
    return s#返回左右pk得到的小和

arr=[1,3,4,2,5]
print(smallSum(arr))