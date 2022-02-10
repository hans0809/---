# 输入一个长度为n的整型数组array，数组中的一个或连续多个整数组成一个子数组。
# 求所有子数组的和的最大值。

# 方法1：前缀和（超时）
class Solution:
    def FindGreatestSumOfSubArray(self , array):
        # write code here
        n=len(array)
        if n==1:
            return array[0]
        
        pre_sum=[array[0]]# 前缀和
        msum=array[0]# 连续子数组的最大和
        for i in range(1,n):
            s=pre_sum[i-1]+array[i]
            pre_sum.append(s)
            msum=max(msum,s)
        print(pre_sum)
        
        for i in range(n):
            for j in range(i+1,n):
                msum=max(msum,pre_sum[j]-pre_sum[i])
        return msum

# 方法2：动态规划
class Solution:
    def FindGreatestSumOfSubArray(self , array):
        # write code here
        n=len(array)

        #dp[i]: 以i结尾的连续子数组的最大和
        dp=[0 for _ in range(n)]
        dp[0]=array[0]
        
        msum=array[0]
        for i in range(1,n):
            dp[i]=max(dp[i-1]+array[i],array[i])
            msum=max(msum,dp[i])
        return msum
