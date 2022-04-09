# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

# 示例：

# 输入： A: [1,2,3,2,1] B: [3,2,1,4,7] 输出：3 解释： 长度最长的公共子数组是 [3, 2, 1] 。


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2=len(nums1),len(nums2)
        # dp[i][j]：只考虑使用nums1[0...i-1]和nums2[0...j-1]，能得到的长度最长的子数组的长度
        dp=[[0 for _ in range(n2+1)] for _ in range(n1+1)]#n1 x n2 的矩阵

        # 初始化
        # 当其中有一个长度为0时，dp取值为0
        for i in range(n1+1):# 第0列全是0
            dp[i][0]=0
        for i in range(n2+1):#第0行全是0
            dp[0][i]=0
        
        res=0
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                res=max(res,dp[i][j])
        return res