#题目：求一个数组中的逆序对个数。
# 逆序对(x,y)满足：
# 1) x>y
# 2) x在y前面
# 比如数组[3,2,4,5,1]中，
# 对于3，前面没有比它大元素，因此3对应逆序对的个数为0
# 对于2，前面比它大的元素是3，因2对应逆序对为(3,2)
# 对于4，前面没有比它大的元素，因此4对应逆序对的个数为0
# 对于5，前面没有比它大的元素，因此5对应逆序对的个数为0
# 对于1，前面比它大的元素是3，2，4，5，因此1对应逆序对为(3,1),(2,1),(4,1),(5,1)


# 思路：在归并排序做merge时，对于一分为二的左右两侧，它们分别是有序的
# **对于右侧每一个元素**，每次都比较左右指针(L和R)所指元素的大小，
# 如果当前右侧元素小于当前左侧元素，那么当前右侧元素所对应的逆序对个数为(mid-p1+1)，p1是左指针下标
# 此时取下当前右侧元素，右侧指针前进一步
# (因为左侧是有序的嘛，是从小到大排列的，
# 当前左侧元素比当前右侧元素大，那当前左侧元素的后面那些元素肯定也比当前右侧元素大)
# 如果当前左右指针所指元素相等，就取下左侧当前元素，让左侧指针前进一步，重复上述步骤
def reverseOrderPair(arr):
    if not arr or len(arr)<2:
        return 0
    return process(arr,0,len(arr)-1)
def process(arr,L,R):
    if L==R:#base case，此时只有一个元素，自然是有序的,
        #只有一个元素，逆序对个数为0
        return 0
    mid=(L+R)//2
    left_reverseOrderPair_num=process(arr,L,mid)#对左半部分进行排序(求逆序对个数)
    right_reverseOrderPair_num=process(arr,mid+1,R)#对右半部分进行排序(求逆序对个数)
    left_right_reverseOrderPair_num=merge(arr,L,mid,R)#合并两个有序数组(求左右两个部分之间的逆序对个数)
    return left_reverseOrderPair_num+right_reverseOrderPair_num+left_right_reverseOrderPair_num
def merge(arr,L,mid,R):
    res=[]
    # i=0#记录res数组长度
    p1=L#左半部分的指针
    p2=mid+1#右半部分的指针
    s=0#左右pk得到的逆序对个数
    while p1<=mid and p2<=R:
        if arr[p1]>arr[p2]:
            s+=(mid-p1+1)
            res.append(arr[p2])
            p2+=1

        elif arr[p1]==arr[p2]:#相等时取左侧，右侧不动
            res.append(arr[p1])
            p1+=1
        else:
            res.append(arr[p1])
            p1+=1
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
    return s#返回左右pk得到的逆序对个数

arr=[3,2,4,5,1]
print(reverseOrderPair(arr))


# 总结：归并排序时，一分为二，两侧分别有序，
# 利用这个条件，可以求某个数的左/右侧比这个数大的数有几个，
# 之所以不找比这个数小的数有几个，是为了使用左/右侧是从小到大有序的特点，
# 这样，如果一个数比某个数大，那么这一个数后面的所有数都比某个数大，比较容易计算个数，
# 因此，总是将此类问题转为求比某个数大的数的个数的问题，
# 本题如此，小和问题亦如此。

