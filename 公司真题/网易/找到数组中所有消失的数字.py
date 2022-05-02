# 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
# 请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

# 空间复杂的复O(N)的解法
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        counter=set(nums)
        res=[]
        for i in range(1,n+1):
            if i not in counter:
                res.append(i)
        return res

# 空间复杂的复O(1)的解法
#抄答案：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/solution/yi-zhang-dong-tu-bang-zhu-li-jie-yuan-di-uign/
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res