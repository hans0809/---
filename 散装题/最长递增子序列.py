def run(nums):
    n=len(nums)
    #dp[i]:nums[0..i-1]中最长递增子序列的长度
    dp=[1 for _ in range(n)]

    for i in range(1,n):
        for j in range(0,i):
            if nums[i]>nums[j]:
                dp[i]=max(dp[i],dp[j]+1)
    print(dp)
    return max(dp)

if __name__=='__main__':
    nums=[1,8,2,3,4,5,1]
    res=run(nums)
    print(res)