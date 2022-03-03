# 递归写法1：归并排序的递归写法
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
    res=[]#临时存储排序后结果，做后将其覆盖到arr中相应位置即可
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

#测试一下
arr=[8,9,4,3,5,6,7,2,1,-1,0,3]
mergeSort(arr)
print(arr)


# 递归写法2：归并排序还有一种更Pythonic的递归写法
def mergeSort(arr):
    if not arr or len(arr)<2:
        return arr
    return process(arr)

def process(arr):
    if len(arr)==1:#base case
        return arr
    mid=len(arr)//2
    left=process(arr[:mid])
    right=process(arr[mid:])
    return merge(left,right)
def merge(left,right):
    res=[]
    while left and right:
        if left[0]<=right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while left:
        res.append(left.pop(0))
    while right:
        res.append(right.pop(0))
    return res

#测试一下
arr=[8,9,4,3,5,6,7,2,1,-1,0,3]
arrSorted=process(arr)
print(arrSorted)

