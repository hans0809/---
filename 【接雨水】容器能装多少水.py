# 题目：给定一个数组arr，已知其中所有的值都非负，将这个数组看作一个容器，请返回容器能装下多少水。

# 动态规划：数组(容器)第i个位置能装的水量=
# max(min( max(arr[0..i-1]), max(arr[i+...len(arr-1)]) )-arr[i],0)
# 具体操作时，
# 准备两个数组l和r，遍历arr，l[i]代表arr[0...i-1]最大值，r[i]代表arr[i+1...len(arr)-1]最大值，
# 然后arr[i]位置的容水量为l[i]和r[i]中的最小的值减去当前arr[i]。
# 累加起来即可。
def maxWater(arr):
    n=len(arr)
    l=[0 for _ in range(n)]
    r=[0 for _ in range(n)]
    l[0]=arr[0]
    r[n-1]=arr[n-1]

    for i in range(1,n):
        l[i]=max(l[i-1],arr[i])
        r[n-1-i]=max(r[n-i],arr[n-1-i])
    
    res=0
    for i in range(1,n-1):# 两个边是不能盛水的
        t= min(l[i],r[i])-arr[i]
        if t >0:
            res+=t
    return res
arr=[3,1,2,5,2,4]  
print('最多能盛的水是：',maxWater(arr))

# 双指针
def maxWater2(arr):
    n=len(arr)
    maxL,maxR=arr[0],arr[n-1]# 当前左/右最大值
    L,R=1,n-2# 左右指针

    res=0
    while L<=R:
        if maxL<=maxR:
            t=maxL-arr[L]
            if t>0:
                res+=t
            maxL=max(maxL,arr[L])
            L+=1
        else:
            t=maxR-arr[R]
            if t>0:
                res+=t
            maxR=max(maxR,arr[R])
            R-=1
    return res
arr=[3,1,2,5,2,4]  
print('最多能盛的水是：',maxWater2(arr))

