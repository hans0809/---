# 链接：https://www.nowcoder.com/questionTerminal/58e31b785f4b4ced9695dd4fcd60c1ce
# 来源：牛客网

# 给定一个非负整数数组nums，假定最开始处于下标为0的位置，
# 数组里面的每个元素代表下一跳能够跳跃的最大长度，如果可以跳到数组最后一个位置，
# 请你求出跳跃路径中所能获得的最多的积分。
# 如果能够跳到数组最后一个位置，才能计算所获得的积分，否则积分值为-1

def jumpGame2(n,nums):
    if n==0:
        return 0

    #dp[i]:跳到第i个台阶能够获得的最大积分
    dp=[0 for _ in range(n)]

    dp[0]=0#本来一开始就在第0个台阶，因此跳到第0个台阶能够获得的最大积分是0

    for i in range(1,n):
        maxScore=0# 跳跃到第i个台阶能够获得最大积分
        for j in range(0,i):
            if j+nums[j]>=i:# 能够跳到第i个台阶
                maxScore=max(maxScore, dp[j]+nums[j])
        dp[i]=maxScore
    return dp[n-1]+nums[n-1] if dp[n-1]!=0 else -1
n=6
nums=[2, 4, 0, 2, 0, 100]
print(jumpGame2(n,nums))

n2=6
nums2=[2, 3, 2, 1, 0, 100]
print(jumpGame2(n2,nums2))