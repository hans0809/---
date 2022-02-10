# 题目1：https://www.nowcoder.com/practice/a4e34287fa1b41f9bd41f957efbd5dff?tpId=101&tqId=33076&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D101%26type%3D101&difficulty=undefined&judgeStatus=undefined&tags=&title=

# 滑动窗口
def solve(arr,k):
    n=len(arr)
    l=0
    r=0
    maxLen=-1
    sum=arr[0]
    while r<n:
        if sum<k:
            r+=1
            if r==n:
                break
            sum+=arr[r]
        elif sum>k:
            sum-=arr[l]
            l+=1
        else:
            maxLen=max(maxLen,r-l+1)
            sum-=arr[l]
            l+=1
    return maxLen
n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(solve(arr,k))


# 题目2： https://www.nowcoder.com/practice/36fb0fd3c656480c92b569258a1223d5?tpId=101&tags=&title=&difficulty=0&judgeStatus=0&rp=1

# 哈希表存储累加和
def solve(arr,k):
    n=len(arr)
    l=0
    r=0
    maxLen=-1
    sum=0
    dic={0:-1}
    for i in range(n):
        sum+=arr[i]
        if sum not in dic:
            dic[sum]=i
        if sum-k in dic:
            maxLen=max(maxLen,i-dic[sum-k])
    return maxLen
n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(solve(arr,k))
