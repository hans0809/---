# 给定一个非负整数数组nums，假定最开始处于下标为0的位置，
# 数组里面的每个元素代表下一跳能够跳跃的最大长度。如果能够跳到数组最后一个位置，则输出true，否则输出false。

# 链接：https://www.nowcoder.com/questionTerminal/07484f4377344d3590045a095910992b
# 来源：牛客网

# 输入
# 7
# 2 1 3 3 0 0 100
# 输出
# true
# 说明
# 首先位于nums[0]=2，然后可以跳2步，到nums[2]=3的位置，再跳到nums[3]=3的位置，再直接跳到nums[6]=100，可以跳到最后，输出true   
# 示例2
# 输入
# 7
# 2 1 3 2 0 0 100
# 输出
# false
# 说明
# 无论怎么样，都跳不到nums[6]=100的位置 

nums1=[2,1,3,3,0,0,100]
nums2=[2,1,3,2,0,0,100]
n1, n2=len(nums1),len(nums2) 

def jumpGame(n,nums):
    # dp[i]:到达第i个台阶所需要的最少步数
    big=100000000000000000000
    dp=[big for _ in range(n)]

    dp[0]=0# 初始就位于第0个台阶上

    for i in range(1,n):
        minSteps=big
        for j in range(0,i):
            if j+nums[j]>=i:#从第j个台阶，能不能一步跳到第i个台阶
                minSteps=min(minSteps,dp[j]+1)
        dp[i]=minSteps
    return dp[n-1]!=big,dp[n-1]
print(jumpGame(n1,nums1))
print(jumpGame(n2,nums2))