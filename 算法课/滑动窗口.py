# 题目1：给定一个有序数组，代表数周上从左到右有n个点arr[0],arr[1],...,arr[n-1],
# 给定一个正数L，代表一根长度为L的绳子，求绳子最多能覆盖其中的几个点。

# 左右边界无需回退
def mySolve(arr,L):
    if L<=0:
        return 0

    left_ind=0
    right_ind=0

    ans=0
    while right_ind<len(arr):
        if arr[right_ind]-arr[left_ind]<=L:
            ans=max(ans,right_ind-left_ind+1)
            right_ind+=1
        else:
            left_ind+=1
    return ans
arr=[10,11222]
L=1
print(mySolve(arr,L))

# 
        


